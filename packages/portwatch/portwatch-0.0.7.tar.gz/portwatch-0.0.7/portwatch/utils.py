# utils.py - Enhanced utilities for PortWatch with optimized configuration management

import yaml
import json
import asyncio
import threading
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple, Set
from concurrent.futures import ThreadPoolExecutor
import logging
import time
import hashlib
import psutil
from dataclasses import dataclass
from enum import Enum

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PortCategory(Enum):
    WEB_DEV = "Web Development"
    DATABASE = "Database"
    API_SERVICE = "API Service"
    SYSTEM = "System"
    DEVELOPMENT = "Development"
    CUSTOM = "Custom"

@dataclass
class PortInfo:
    """Enhanced port information structure"""
    port: int
    description: str
    category: PortCategory
    is_default: bool = False
    is_active: bool = False
    process_name: Optional[str] = None
    custom_description: Optional[str] = None
    last_seen: Optional[float] = None
    usage_count: int = 0

# Comprehensive default dev ports with categories and descriptions
DEFAULT_DEV_PORTS = {
    # System ports
    22: {"desc": "SSH Server", "category": PortCategory.SYSTEM},
    80: {"desc": "HTTP Web Server", "category": PortCategory.SYSTEM},
    443: {"desc": "HTTPS Web Server", "category": PortCategory.SYSTEM},
    53: {"desc": "DNS Server", "category": PortCategory.SYSTEM},
    21: {"desc": "FTP Server", "category": PortCategory.SYSTEM},
    25: {"desc": "SMTP Mail Server", "category": PortCategory.SYSTEM},
    
    # Web Development
    3000: {"desc": "React/Next.js Dev Server", "category": PortCategory.WEB_DEV},
    3001: {"desc": "React Dev Server (Alt)", "category": PortCategory.WEB_DEV},
    5173: {"desc": "Vite Dev Server", "category": PortCategory.WEB_DEV},
    4200: {"desc": "Angular Dev Server", "category": PortCategory.WEB_DEV},
    8080: {"desc": "Development Web Server", "category": PortCategory.WEB_DEV},
    8081: {"desc": "Alternative Web Server", "category": PortCategory.WEB_DEV},
    9000: {"desc": "Frontend Dev Server", "category": PortCategory.WEB_DEV},
    1234: {"desc": "Live Server", "category": PortCategory.WEB_DEV},
    
    # API & Backend Services
    8000: {"desc": "Django/FastAPI Dev Server", "category": PortCategory.API_SERVICE},
    5000: {"desc": "Flask Dev Server", "category": PortCategory.API_SERVICE},
    4000: {"desc": "Express.js Server", "category": PortCategory.API_SERVICE},
    3333: {"desc": "Node.js API Server", "category": PortCategory.API_SERVICE},
    9001: {"desc": "Backend API Server", "category": PortCategory.API_SERVICE},
    
    # Databases
    3306: {"desc": "MySQL Database", "category": PortCategory.DATABASE},
    5432: {"desc": "PostgreSQL Database", "category": PortCategory.DATABASE},
    27017: {"desc": "MongoDB Database", "category": PortCategory.DATABASE},
    6379: {"desc": "Redis Cache", "category": PortCategory.DATABASE},
    5984: {"desc": "CouchDB Database", "category": PortCategory.DATABASE},
    8086: {"desc": "InfluxDB Database", "category": PortCategory.DATABASE},
    9200: {"desc": "Elasticsearch", "category": PortCategory.DATABASE},
    
    # Development Tools
    9092: {"desc": "Apache Kafka", "category": PortCategory.DEVELOPMENT},
    8888: {"desc": "Jupyter Notebook", "category": PortCategory.DEVELOPMENT},
    9999: {"desc": "Development Tool", "category": PortCategory.DEVELOPMENT},
    1337: {"desc": "Development Server", "category": PortCategory.DEVELOPMENT},
    8765: {"desc": "Debug Server", "category": PortCategory.DEVELOPMENT},
}

CONFIG_FILE_NAME = ".portconfig"
DESCRIPTIONS_FILE_NAME = "port_descriptions.yml"
USAGE_HISTORY_FILE_NAME = "port_usage_history.yml"

class ConfigManager:
    """Thread-safe configuration manager with caching and validation"""
    
    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or Path.cwd()
        self.config_path = self.config_dir / CONFIG_FILE_NAME
        self.descriptions_path = self.config_dir / DESCRIPTIONS_FILE_NAME
        self.usage_history_path = self.config_dir / USAGE_HISTORY_FILE_NAME
        
        # Thread safety
        self._lock = threading.RLock()
        self._cache = {}
        self._cache_timestamps = {}
        self._cache_timeout = 30  # seconds
        
        # Thread pool for I/O operations
        self._executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="config")
        
        # Initialize config directory
        self.config_dir.mkdir(exist_ok=True)
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if cache entry is still valid"""
        if key not in self._cache_timestamps:
            return False
        return time.time() - self._cache_timestamps[key] < self._cache_timeout
    
    def _update_cache(self, key: str, value: Any):
        """Update cache with new value"""
        with self._lock:
            self._cache[key] = value
            self._cache_timestamps[key] = time.time()
    
    def _get_from_cache(self, key: str) -> Optional[Any]:
        """Get value from cache if valid"""
        with self._lock:
            if self._is_cache_valid(key):
                return self._cache.get(key)
        return None

    def load_dev_ports(self) -> List[int]:
        """
        Load developer ports from config file with caching.
        Thread-safe with automatic fallback to defaults.
        """
        # Check cache first
        cached = self._get_from_cache('dev_ports')
        if cached is not None:
            return cached
        
        if not self.config_path.exists():
            default_ports = list(DEFAULT_DEV_PORTS.keys())
            self.save_dev_ports(default_ports)
            self._update_cache('dev_ports', default_ports)
            return default_ports

        try:
            with self.config_path.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load {CONFIG_FILE_NAME}: {e}")
            default_ports = list(DEFAULT_DEV_PORTS.keys())
            self._update_cache('dev_ports', default_ports)
            return default_ports

        ports = self._parse_ports_from_config(data)
        
        # Validate and clean ports
        valid_ports = [p for p in ports if self.validate_port(p)]
        valid_ports.sort()
        
        self._update_cache('dev_ports', valid_ports)
        return valid_ports

    def _parse_ports_from_config(self, data: Any) -> Set[int]:
        """Parse ports from various config formats"""
        ports = set()

        if isinstance(data, dict):
            for key in data.keys():
                try:
                    port = int(key)
                    if self.validate_port(port):
                        ports.add(port)
                except (ValueError, TypeError):
                    continue
                    
        elif isinstance(data, list):
            for item in data:
                try:
                    port = int(item)
                    if self.validate_port(port):
                        ports.add(port)
                except (ValueError, TypeError):
                    continue
        else:
            logger.warning(f"Unsupported config format in {CONFIG_FILE_NAME}")
            return set(DEFAULT_DEV_PORTS.keys())

        return ports

    def save_dev_ports(self, ports: List[int]) -> bool:
        """
        Save port list to config file with enhanced format.
        Thread-safe with validation and backup.
        """
        try:
            # Validate and deduplicate ports
            valid_ports = sorted(set(p for p in ports if self.validate_port(p)))
            
            # Create backup if file exists
            if self.config_path.exists():
                backup_path = self.config_path.with_suffix('.bak')
                self.config_path.replace(backup_path)
            
            # Build port dictionary with descriptions
            port_dict = {}
            custom_descriptions = self.load_custom_descriptions()
            
            for port in valid_ports:
                # Use custom description if available, otherwise default
                if port in custom_descriptions:
                    description = custom_descriptions[port]
                elif port in DEFAULT_DEV_PORTS:
                    description = DEFAULT_DEV_PORTS[port]["desc"]
                else:
                    description = f"Custom Port {port}"
                
                port_dict[str(port)] = description

            # Write config with proper formatting
            with self.config_path.open("w", encoding="utf-8") as f:
                yaml.safe_dump(
                    port_dict,
                    f,
                    sort_keys=False,
                    default_flow_style=False,
                    indent=2,
                    allow_unicode=True
                )
            
            # Update cache
            self._update_cache('dev_ports', valid_ports)
            logger.debug(f"Saved {len(valid_ports)} ports to config")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save {CONFIG_FILE_NAME}: {e}")
            return False

    def load_custom_descriptions(self) -> Dict[int, str]:
        """Load custom port descriptions"""
        cached = self._get_from_cache('custom_descriptions')
        if cached is not None:
            return cached
        
        try:
            if self.descriptions_path.exists():
                with self.descriptions_path.open("r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
                    # Convert string keys to int
                    descriptions = {int(k): v for k, v in data.items() 
                                 if str(k).isdigit() and isinstance(v, str)}
                    self._update_cache('custom_descriptions', descriptions)
                    return descriptions
        except Exception as e:
            logger.error(f"Failed to load custom descriptions: {e}")
        
        empty_dict = {}
        self._update_cache('custom_descriptions', empty_dict)
        return empty_dict

    def save_custom_descriptions(self, descriptions: Dict[int, str]) -> bool:
        """Save custom port descriptions"""
        try:
            # Convert int keys to string for YAML
            string_dict = {str(k): v for k, v in descriptions.items() 
                          if self.validate_port(k) and isinstance(v, str)}
            
            with self.descriptions_path.open("w", encoding="utf-8") as f:
                yaml.safe_dump(
                    string_dict,
                    f,
                    sort_keys=False,
                    default_flow_style=False,
                    indent=2,
                    allow_unicode=True
                )
            
            # Update cache
            self._update_cache('custom_descriptions', descriptions)
            return True
            
        except Exception as e:
            logger.error(f"Failed to save custom descriptions: {e}")
            return False

    def add_dev_port(self, port: int, description: Optional[str] = None) -> bool:
        """Add a single port to config with optional custom description"""
        if not self.validate_port(port):
            return False
        
        with self._lock:
            ports = self.load_dev_ports()
            if port in ports:
                return False  # Already exists
            
            ports.append(port)
            success = self.save_dev_ports(ports)
            
            # Save custom description if provided
            if success and description:
                custom_descriptions = self.load_custom_descriptions()
                custom_descriptions[port] = description
                self.save_custom_descriptions(custom_descriptions)
            
            return success

    def remove_dev_port(self, port: int) -> bool:
        """Remove a port from config"""
        with self._lock:
            ports = self.load_dev_ports()
            if port not in ports:
                return False
            
            ports.remove(port)
            success = self.save_dev_ports(ports)
            
            # Also remove custom description if exists
            if success:
                custom_descriptions = self.load_custom_descriptions()
                if port in custom_descriptions:
                    del custom_descriptions[port]
                    self.save_custom_descriptions(custom_descriptions)
            
            return success

    def reset_dev_ports_to_default(self):
        """Reset config to default dev ports"""
        default_ports = list(DEFAULT_DEV_PORTS.keys())
        self.save_dev_ports(default_ports)
        
        # Clear custom descriptions
        self.save_custom_descriptions({})
        
        # Clear cache
        with self._lock:
            self._cache.clear()
            self._cache_timestamps.clear()

    def get_port_description(self, port: int) -> str:
        """Get human-readable description for a port"""
        # Check custom descriptions first
        custom_descriptions = self.load_custom_descriptions()
        if port in custom_descriptions:
            return custom_descriptions[port]
        
        # Check default descriptions
        if port in DEFAULT_DEV_PORTS:
            return DEFAULT_DEV_PORTS[port]["desc"]
        
        # Fallback based on port number
        return self._generate_fallback_description(port)

    def _generate_fallback_description(self, port: int) -> str:
        """Generate a fallback description based on port number"""
        if port < 1024:
            return f"System Port {port}"
        elif port < 5000:
            return f"Development Port {port}"
        elif port < 10000:
            return f"Application Port {port}"
        else:
            return f"Custom Port {port}"

    def get_port_info(self, port: int) -> PortInfo:
        """Get comprehensive port information"""
        description = self.get_port_description(port)
        category = self.get_port_category(port)
        is_default = port in DEFAULT_DEV_PORTS
        
        return PortInfo(
            port=port,
            description=description,
            category=category,
            is_default=is_default
        )

    def get_port_category(self, port: int) -> PortCategory:
        """Get the category for a port"""
        if port in DEFAULT_DEV_PORTS:
            return DEFAULT_DEV_PORTS[port]["category"]
        
        # Categorize based on port number ranges
        if port < 1024:
            return PortCategory.SYSTEM
        elif port in range(3000, 3010) or port in [5173, 4200]:
            return PortCategory.WEB_DEV
        elif port in [3306, 5432, 27017, 6379]:
            return PortCategory.DATABASE
        elif port in range(8000, 8090):
            return PortCategory.API_SERVICE
        else:
            return PortCategory.CUSTOM

    @staticmethod
    def validate_port(port: int) -> bool:
        """Validate if port number is valid"""
        return isinstance(port, int) and 1 <= port <= 65535

    @staticmethod
    def validate_port_range(start: int, end: int) -> bool:
        """Validate if port range is reasonable"""
        return (ConfigManager.validate_port(start) and 
                ConfigManager.validate_port(end) and
                start <= end and 
                (end - start) <= 100)  # Limit range size to prevent abuse

    def get_ports_by_category(self, category: PortCategory) -> List[int]:
        """Get all ports belonging to a specific category"""
        ports = self.load_dev_ports()
        return [port for port in ports if self.get_port_category(port) == category]

    def export_config(self, export_path: Optional[Path] = None) -> bool:
        """Export complete configuration to a file"""
        try:
            export_path = export_path or (self.config_dir / "portwatch_export.yml")
            
            config_data = {
                'ports': self.load_dev_ports(),
                'descriptions': self.load_custom_descriptions(),
                'export_timestamp': time.time(),
                'version': '2.0'
            }
            
            with export_path.open("w", encoding="utf-8") as f:
                yaml.safe_dump(config_data, f, default_flow_style=False, indent=2)
            
            logger.info(f"Configuration exported to {export_path}")
            return True
            
        except Exception as e:
            logger.error(f"Export failed: {e}")
            return False

    def import_config(self, import_path: Optional[Path] = None) -> Tuple[bool, str]:
        """Import configuration from a file"""
        try:
            import_path = import_path or (self.config_dir / "portwatch_export.yml")
            
            if not import_path.exists():
                return False, "Import file not found"
            
            with import_path.open("r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f)
            
            if not isinstance(config_data, dict):
                return False, "Invalid configuration format"
            
            # Import ports
            if 'ports' in config_data:
                imported_ports = [p for p in config_data['ports'] if self.validate_port(p)]
                current_ports = set(self.load_dev_ports())
                new_ports = [p for p in imported_ports if p not in current_ports]
                
                if new_ports:
                    all_ports = sorted(list(current_ports) + new_ports)
                    self.save_dev_ports(all_ports)
            
            # Import descriptions
            if 'descriptions' in config_data:
                current_descriptions = self.load_custom_descriptions()
                new_descriptions = config_data['descriptions']
                current_descriptions.update(new_descriptions)
                self.save_custom_descriptions(current_descriptions)
            
            # Clear cache to force reload
            with self._lock:
                self._cache.clear()
                self._cache_timestamps.clear()
            
            logger.info(f"Configuration imported from {import_path}")
            return True, f"Successfully imported configuration"
            
        except Exception as e:
            error_msg = f"Import failed: {e}"
            logger.error(error_msg)
            return False, error_msg

    async def get_active_ports_async(self) -> Set[int]:
        """Asynchronously get currently active ports"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self._executor, self._get_active_ports_sync)

    def _get_active_ports_sync(self) -> Set[int]:
        """Synchronously get currently active ports"""
        active_ports = set()
        try:
            for conn in psutil.net_connections():
                if conn.laddr and conn.status == 'LISTEN':
                    active_ports.add(conn.laddr.port)
        except Exception as e:
            logger.error(f"Failed to get active ports: {e}")
        return active_ports

    def cleanup(self):
        """Cleanup resources"""
        if hasattr(self, '_executor'):
            self._executor.shutdown(wait=True)

# Global configuration manager instance
_config_manager: Optional[ConfigManager] = None

def get_config_manager() -> ConfigManager:
    """Get or create the global configuration manager"""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager

# Backwards compatibility functions
def load_dev_ports() -> List[int]:
    """Load developer ports (backwards compatible)"""
    return get_config_manager().load_dev_ports()

def save_dev_ports(ports: List[int]) -> bool:
    """Save developer ports (backwards compatible)"""
    return get_config_manager().save_dev_ports(ports)

def add_dev_port(port: int) -> bool:
    """Add a single port (backwards compatible)"""
    return get_config_manager().add_dev_port(port)

def remove_dev_port(port: int) -> bool:
    """Remove a port (backwards compatible)"""
    return get_config_manager().remove_dev_port(port)

def reset_dev_ports_to_default():
    """Reset to default ports (backwards compatible)"""
    get_config_manager().reset_dev_ports_to_default()

def get_port_description(port: int) -> str:
    """Get port description (backwards compatible)"""
    return get_config_manager().get_port_description(port)

def validate_port_range(start: int, end: int) -> bool:
    """Validate port range (new function)"""
    return ConfigManager.validate_port_range(start, end)

# Enhanced utility functions for the port configuration screen
async def check_for_conflict(port: int) -> Optional[str]:
    """Check if port has conflicts with expected usage"""
    try:
        config_manager = get_config_manager()
        active_ports = await config_manager.get_active_ports_async()
        
        if port not in active_ports:
            return None
        
        # Get process info for the port
        for conn in psutil.net_connections():
            if (conn.laddr and conn.laddr.port == port and 
                conn.status == 'LISTEN' and conn.pid):
                try:
                    process = psutil.Process(conn.pid)
                    process_name = process.name()
                    
                    # Check if process matches expected usage
                    expected_desc = config_manager.get_port_description(port).lower()
                    if any(keyword in expected_desc for keyword in 
                          ['react', 'node', 'npm', 'yarn'] if 'node' not in process_name.lower()):
                        return f"Expected Node.js process but found {process_name}"
                    
                    return f"In use by {process_name} (PID: {conn.pid})"
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        
        return "Port in use by unknown process"
        
    except Exception as e:
        logger.error(f"Conflict check failed for port {port}: {e}")
        return None

def get_process_using_port(port: int) -> Optional[Dict[str, Any]]:
    """Get detailed info about process using a port"""
    try:
        for conn in psutil.net_connections():
            if (conn.laddr and conn.laddr.port == port and 
                conn.status == 'LISTEN' and conn.pid):
                try:
                    process = psutil.Process(conn.pid)
                    return {
                        'pid': conn.pid,
                        'name': process.name(),
                        'cmdline': ' '.join(process.cmdline()),
                        'create_time': process.create_time(),
                        'memory_info': process.memory_info()._asdict(),
                        'cpu_percent': process.cpu_percent()
                    }
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        return None
    except Exception as e:
        logger.error(f"Failed to get process info for port {port}: {e}")
        return None

def suggest_alternative_ports(preferred_range: Tuple[int, int] = (3000, 9000), 
                            count: int = 10) -> List[int]:
    """Suggest alternative unused ports"""
    try:
        config_manager = get_config_manager()
        start, end = preferred_range
        
        # Get currently active ports
        active_ports = config_manager._get_active_ports_sync()
        configured_ports = set(config_manager.load_dev_ports())
        
        suggestions = []
        for port in range(start, min(end + 1, 65536)):
            if (port not in active_ports and 
                port not in configured_ports and 
                len(suggestions) < count):
                suggestions.append(port)
        
        return suggestions
    except Exception as e:
        logger.error(f"Failed to suggest alternative ports: {e}")
        return []

# Cleanup function
def cleanup_utils():
    """Cleanup utility resources"""
    global _config_manager
    if _config_manager is not None:
        _config_manager.cleanup()
        _config_manager = None