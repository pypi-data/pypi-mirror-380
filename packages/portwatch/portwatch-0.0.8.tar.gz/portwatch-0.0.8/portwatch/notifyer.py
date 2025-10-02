# notifyer.py - Enhanced cross-platform notification system

import asyncio
import threading
import queue
import time
import sys
import os
import logging
from typing import Optional, Dict, Any, Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from enum import Enum
import platform

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class NotificationConfig:
    """Configuration for notifications"""
    enabled: bool = True
    max_notifications_per_minute: int = 10
    default_timeout: int = 5
    enable_sound: bool = True
    enable_system_tray: bool = True
    fallback_to_console: bool = True
    batch_similar: bool = True
    batch_timeout: float = 2.0  # seconds to wait before sending batched notifications

@dataclass
class Notification:
    """Notification data structure"""
    title: str
    message: str
    priority: NotificationPriority = NotificationPriority.MEDIUM
    timeout: int = 5
    app_name: str = "PortWatch"
    app_icon: Optional[str] = None
    category: str = "default"
    timestamp: float = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

class NotificationBackend:
    """Base class for notification backends"""
    
    def __init__(self, config: NotificationConfig):
        self.config = config
        self.available = False
    
    def test_availability(self) -> bool:
        """Test if this backend is available"""
        return False
    
    def send_notification(self, notification: Notification) -> bool:
        """Send a single notification"""
        raise NotImplementedError
    
    def cleanup(self):
        """Cleanup resources"""
        pass

class PlyerBackend(NotificationBackend):
    """Plyer-based notification backend (cross-platform)"""
    
    def __init__(self, config: NotificationConfig):
        super().__init__(config)
        self.plyer_notification = None
        self.available = self.test_availability()
    
    def test_availability(self) -> bool:
        try:
            from plyer import notification
            self.plyer_notification = notification
            # Test with a dummy notification
            return True
        except ImportError:
            logger.warning("Plyer not available for notifications")
            return False
        except Exception as e:
            logger.warning(f"Plyer backend test failed: {e}")
            return False
    
    def send_notification(self, notification: Notification) -> bool:
        if not self.available or not self.plyer_notification:
            return False
        
        try:
            self.plyer_notification.notify(
                title=notification.title,
                message=notification.message,
                app_name=notification.app_name,
                app_icon=notification.app_icon,
                timeout=notification.timeout
            )
            return True
        except Exception as e:
            logger.error(f"Plyer notification failed: {e}")
            return False

class WindowsBackend(NotificationBackend):
    """Windows-specific notification backend using win10toast or plyer"""
    
    def __init__(self, config: NotificationConfig):
        super().__init__(config)
        self.toaster = None
        self.available = self.test_availability()
    
    def test_availability(self) -> bool:
        if platform.system() != "Windows":
            return False
        
        try:
            # Try win10toast first (better Windows integration)
            from win10toast import ToastNotifier
            self.toaster = ToastNotifier()
            return True
        except ImportError:
            logger.info("win10toast not available, falling back to plyer")
            return False
        except Exception as e:
            logger.warning(f"Windows backend test failed: {e}")
            return False
    
    def send_notification(self, notification: Notification) -> bool:
        if not self.available or not self.toaster:
            return False
        
        try:
            self.toaster.show_toast(
                notification.title,
                notification.message,
                duration=notification.timeout,
                threaded=True  # Important for async operation
            )
            return True
        except Exception as e:
            logger.error(f"Windows notification failed: {e}")
            return False

class MacOSBackend(NotificationBackend):
    """macOS-specific notification backend using osascript"""
    
    def __init__(self, config: NotificationConfig):
        super().__init__(config)
        self.available = self.test_availability()
    
    def test_availability(self) -> bool:
        if platform.system() != "Darwin":
            return False
        
        try:
            import subprocess
            # Test if osascript is available
            result = subprocess.run(['which', 'osascript'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def send_notification(self, notification: Notification) -> bool:
        if not self.available:
            return False
        
        try:
            import subprocess
            
            script = f'''
            display notification "{notification.message}" ¬
                with title "{notification.title}" ¬
                subtitle "{notification.app_name}"
            '''
            
            subprocess.run(['osascript', '-e', script], 
                         capture_output=True, check=True)
            return True
        except Exception as e:
            logger.error(f"macOS notification failed: {e}")
            return False

class LinuxBackend(NotificationBackend):
    """Linux-specific notification backend using notify-send"""
    
    def __init__(self, config: NotificationConfig):
        super().__init__(config)
        self.available = self.test_availability()
    
    def test_availability(self) -> bool:
        if platform.system() != "Linux":
            return False
        
        try:
            import subprocess
            # Test if notify-send is available
            result = subprocess.run(['which', 'notify-send'], capture_output=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def send_notification(self, notification: Notification) -> bool:
        if not self.available:
            return False
        
        try:
            import subprocess
            
            cmd = [
                'notify-send',
                '--app-name', notification.app_name,
                '--expire-time', str(notification.timeout * 1000),
                notification.title,
                notification.message
            ]
            
            subprocess.run(cmd, capture_output=True, check=True)
            return True
        except Exception as e:
            logger.error(f"Linux notification failed: {e}")
            return False

class ConsoleBackend(NotificationBackend):
    """Fallback console-based notification backend"""
    
    def __init__(self, config: NotificationConfig):
        super().__init__(config)
        self.available = True  # Always available as fallback
    
    def test_availability(self) -> bool:
        return True
    
    def send_notification(self, notification: Notification) -> bool:
        try:
            timestamp = time.strftime("%H:%M:%S", time.localtime(notification.timestamp))
            priority_symbol = {
                NotificationPriority.LOW: "ℹ️",
                NotificationPriority.MEDIUM: "📢",
                NotificationPriority.HIGH: "⚠️",
                NotificationPriority.CRITICAL: "🚨"
            }.get(notification.priority, "📢")
            
            print(f"\n{priority_symbol} [{timestamp}] {notification.title}")
            print(f"   {notification.message}")
            print(f"   (Category: {notification.category})\n")
            return True
        except Exception as e:
            logger.error(f"Console notification failed: {e}")
            return False

class NotificationManager:
    """Advanced notification manager with threading, batching, and rate limiting"""
    
    def __init__(self, config: Optional[NotificationConfig] = None):
        self.config = config or NotificationConfig()
        self.backends = []
        self.notification_queue = queue.Queue()
        self.rate_limiter = {}  # category -> list of timestamps
        self.batch_buffer = {}  # category -> list of notifications
        self.batch_timers = {}  # category -> timer
        
        # Threading
        self.executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="notification")
        self.worker_thread = None
        self.shutdown_event = threading.Event()
        
        # Statistics
        self.stats = {
            'sent': 0,
            'failed': 0,
            'rate_limited': 0,
            'batched': 0
        }
        
        self._initialize_backends()
        self._start_worker()
    
    def _initialize_backends(self):
        """Initialize available notification backends"""
        # Try platform-specific backends first
        if platform.system() == "Windows":
            windows_backend = WindowsBackend(self.config)
            if windows_backend.available:
                self.backends.append(windows_backend)
        
        elif platform.system() == "Darwin":
            macos_backend = MacOSBackend(self.config)
            if macos_backend.available:
                self.backends.append(macos_backend)
        
        elif platform.system() == "Linux":
            linux_backend = LinuxBackend(self.config)
            if linux_backend.available:
                self.backends.append(linux_backend)
        
        # Try cross-platform plyer backend
        plyer_backend = PlyerBackend(self.config)
        if plyer_backend.available:
            self.backends.append(plyer_backend)
        
        # Always add console backend as fallback
        if self.config.fallback_to_console:
            self.backends.append(ConsoleBackend(self.config))
        
        logger.info(f"Initialized {len(self.backends)} notification backends")
    
    def _start_worker(self):
        """Start the background worker thread"""
        self.worker_thread = threading.Thread(
            target=self._notification_worker,
            name="notification-worker",
            daemon=True
        )
        self.worker_thread.start()
    
    def _notification_worker(self):
        """Background worker that processes notifications"""
        while not self.shutdown_event.is_set():
            try:
                # Get notification with timeout to allow shutdown
                notification = self.notification_queue.get(timeout=1.0)
                
                if notification is None:  # Shutdown signal
                    break
                
                self._process_notification(notification)
                self.notification_queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Notification worker error: {e}")
    
    def _process_notification(self, notification: Notification):
        """Process a single notification with rate limiting and batching"""
        
        # Check rate limiting
        if not self._check_rate_limit(notification.category):
            self.stats['rate_limited'] += 1
            logger.debug(f"Rate limited notification for category: {notification.category}")
            return
        
        # Handle batching for similar notifications
        if self.config.batch_similar and notification.priority != NotificationPriority.CRITICAL:
            if self._should_batch(notification):
                self._add_to_batch(notification)
                return
        
        # Send notification immediately
        self._send_notification(notification)
    
    def _check_rate_limit(self, category: str) -> bool:
        """Check if notification should be rate limited"""
        current_time = time.time()
        
        if category not in self.rate_limiter:
            self.rate_limiter[category] = []
        
        # Clean old entries (older than 1 minute)
        self.rate_limiter[category] = [
            timestamp for timestamp in self.rate_limiter[category]
            if current_time - timestamp < 60
        ]
        
        # Check if under limit
        if len(self.rate_limiter[category]) >= self.config.max_notifications_per_minute:
            return False
        
        # Add current timestamp
        self.rate_limiter[category].append(current_time)
        return True
    
    def _should_batch(self, notification: Notification) -> bool:
        """Determine if notification should be batched"""
        return (notification.category in ['port_conflict', 'process_kill'] and 
                notification.priority in [NotificationPriority.LOW, NotificationPriority.MEDIUM])
    
    def _add_to_batch(self, notification: Notification):
        """Add notification to batch buffer"""
        category = notification.category
        
        if category not in self.batch_buffer:
            self.batch_buffer[category] = []
        
        self.batch_buffer[category].append(notification)
        
        # Cancel existing timer if any
        if category in self.batch_timers:
            self.batch_timers[category].cancel()
        
        # Set new timer
        timer = threading.Timer(self.config.batch_timeout, self._flush_batch, args=[category])
        self.batch_timers[category] = timer
        timer.start()
    
    def _flush_batch(self, category: str):
        """Flush batched notifications for a category"""
        if category not in self.batch_buffer or not self.batch_buffer[category]:
            return
        
        notifications = self.batch_buffer[category]
        self.batch_buffer[category] = []
        
        if len(notifications) == 1:
            # Single notification, send as is
            self._send_notification(notifications[0])
        else:
            # Multiple notifications, create a summary
            batch_notification = self._create_batch_notification(notifications)
            self._send_notification(batch_notification)
            self.stats['batched'] += len(notifications)
    
    def _create_batch_notification(self, notifications: list) -> Notification:
        """Create a single notification from multiple batched notifications"""
        count = len(notifications)
        category = notifications[0].category
        
        if category == 'port_conflict':
            ports = [notif.title.split()[1] for notif in notifications]
            title = f"⚠️ {count} Port Conflicts"
            message = f"Ports in conflict: {', '.join(ports)}"
        elif category == 'process_kill':
            title = f"🔄 {count} Processes Killed"
            message = f"Successfully terminated {count} processes"
        else:
            title = f"📢 {count} Notifications"
            message = f"Multiple {category} notifications"
        
        return Notification(
            title=title,
            message=message,
            priority=max(n.priority for n in notifications),
            category=category,
            timeout=max(n.timeout for n in notifications)
        )
    
    def _send_notification(self, notification: Notification):
        """Send notification through available backends"""
        if not self.config.enabled:
            return
        
        sent = False
        for backend in self.backends:
            try:
                if backend.send_notification(notification):
                    sent = True
                    break  # Successfully sent, no need to try other backends
            except Exception as e:
                logger.error(f"Backend {backend.__class__.__name__} failed: {e}")
                continue
        
        if sent:
            self.stats['sent'] += 1
            logger.debug(f"Notification sent: {notification.title}")
        else:
            self.stats['failed'] += 1
            logger.error(f"All notification backends failed for: {notification.title}")
    
    def notify(self, 
               title: str, 
               message: str, 
               priority: NotificationPriority = NotificationPriority.MEDIUM,
               category: str = "default",
               timeout: int = None,
               **kwargs) -> bool:
        """Send a notification (thread-safe)"""
        
        if not self.config.enabled:
            return False
        
        notification = Notification(
            title=title,
            message=message,
            priority=priority,
            category=category,
            timeout=timeout or self.config.default_timeout,
            **kwargs
        )
        
        try:
            # For critical notifications, send immediately in current thread
            if priority == NotificationPriority.CRITICAL:
                self._send_notification(notification)
                return True
            else:
                # Queue for background processing
                self.notification_queue.put(notification)
                return True
        except Exception as e:
            logger.error(f"Failed to queue notification: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get notification statistics"""
        return {
            **self.stats,
            'backends_available': len(self.backends),
            'queue_size': self.notification_queue.qsize(),
            'rate_limiter_active_categories': len(self.rate_limiter)
        }
    
    def shutdown(self):
        """Cleanup and shutdown notification manager"""
        logger.info("Shutting down notification manager")
        
        # Signal worker to stop
        self.shutdown_event.set()
        self.notification_queue.put(None)  # Shutdown signal
        
        # Wait for worker to finish
        if self.worker_thread and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=5.0)
        
        # Cancel batch timers
        for timer in self.batch_timers.values():
            timer.cancel()
        
        # Cleanup backends
        for backend in self.backends:
            backend.cleanup()
        
        # Shutdown thread pool
        self.executor.shutdown(wait=True)
        
        logger.info("Notification manager shutdown complete")

# Global notification manager instance
_notification_manager: Optional[NotificationManager] = None

def get_notification_manager() -> NotificationManager:
    """Get or create the global notification manager"""
    global _notification_manager
    if _notification_manager is None:
        _notification_manager = NotificationManager()
    return _notification_manager

def initialize_notifications(config: Optional[NotificationConfig] = None):
    """Initialize the notification system with custom configuration"""
    global _notification_manager
    if _notification_manager is not None:
        _notification_manager.shutdown()
    _notification_manager = NotificationManager(config)

# Convenient async wrappers for the main application

async def alert_conflict(port: str, app_name: str = ""):
    """Async wrapper for port conflict notifications"""
    def _send_notification():
        manager = get_notification_manager()
        manager.notify(
            title=f"⚠️ Port {port} in use",
            message=f"Dev port {port} is being used by {app_name or 'unknown process'}.",
            priority=NotificationPriority.HIGH,
            category="port_conflict",
            timeout=8
        )
    
    # Run in thread pool to avoid blocking
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _send_notification)

async def alert_process_killed(pid: int, process_name: str = ""):
    """Async wrapper for process kill notifications"""
    def _send_notification():
        manager = get_notification_manager()
        manager.notify(
            title=f"🔄 Process Killed",
            message=f"Successfully terminated {process_name or f'PID {pid}'}",
            priority=NotificationPriority.MEDIUM,
            category="process_kill",
            timeout=5
        )
    
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _send_notification)

 

def notification_is_enabled() -> bool:
    """Check if notifications are enabled and available"""
    try:
        manager = get_notification_manager()
        return manager.config.enabled and len(manager.backends) > 0
    except Exception:
        return False

# Convenience functions for backward compatibility
def alert_conflict_sync(port: str, app_name: str = ""):
    """Synchronous version for backwards compatibility"""
    manager = get_notification_manager()
    manager.notify(
        title=f"⚠️ Port {port} in use",
        message=f"Dev port {port} is being used by {app_name or 'unknown process'}.",
        priority=NotificationPriority.HIGH,
        category="port_conflict"
    )

# Cleanup function to be called on application exit
def cleanup_notifications():
    """Cleanup notification system on application exit"""
    global _notification_manager
    if _notification_manager is not None:
        _notification_manager.shutdown()
        _notification_manager = None