# scanner.py - Cross-platform optimized network scanner

import asyncio
import psutil
import platform
import subprocess
import socket
import threading
import time
import logging
from typing import Union, List, Dict, Any, Optional, Set, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from enum import Enum

from .utils import load_dev_ports, get_port_description

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScanMethod(Enum):
    PSUTIL = "psutil"
    NETSTAT = "netstat"
    SS = "ss"  # Linux modern replacement for netstat
    LSOF = "lsof"  # Unix/Linux
    POWERSHELL = "powershell"  # Windows

@dataclass
class ConnectionInfo:
    """Enhanced connection information"""
    pid: Optional[int]
    port: int
    process_name: str
    status: str
    local_address: str
    protocol: str
    process_path: Optional[str] = None
    process_cmdline: Optional[str] = None
    connection_time: Optional[float] = None
    note: str = ""

class CrossPlatformScanner:
    """Cross-platform network connection scanner with multiple fallback methods"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.available_methods = self._detect_available_methods()
        self.executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="scanner")
        self.cache = {}
        self.cache_timeout = 2.0  # Cache results for 2 seconds
        self.last_scan_time = 0
        self._dev_ports_cache = None
        self._dev_ports_cache_time = 0
        
        logger.info(f"Scanner initialized for {self.system} with methods: {[m.value for m in self.available_methods]}")

    def _detect_available_methods(self) -> List[ScanMethod]:
        """Detect available scanning methods for the current platform"""
        methods = []
        
        # Test psutil first (most reliable)
        try:
            psutil.net_connections()
            methods.append(ScanMethod.PSUTIL)
        except (psutil.AccessDenied, AttributeError) as e:
            logger.warning(f"psutil method not available: {e}")
        
        # Platform-specific methods
        if self.system == "windows":
            if self._test_command(["powershell", "-Command", "Get-NetTCPConnection | Select-Object -First 1"]):
                methods.append(ScanMethod.POWERSHELL)
            if self._test_command(["netstat", "-an"]):
                methods.append(ScanMethod.NETSTAT)
                
        elif self.system in ["linux", "darwin"]:  # Linux or macOS
            if self._test_command(["ss", "-tuln"]):
                methods.append(ScanMethod.SS)
            if self._test_command(["netstat", "-an"]):
                methods.append(ScanMethod.NETSTAT)
            if self._test_command(["lsof", "-i", "-P", "-n"]):
                methods.append(ScanMethod.LSOF)
        
        if not methods:
            logger.warning("No scanning methods available - will attempt basic psutil")
            methods.append(ScanMethod.PSUTIL)  # Fallback even if it might fail
            
        return methods

    def _test_command(self, cmd: List[str]) -> bool:
        """Test if a command is available and executable"""
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                timeout=5, 
                check=False
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return False

    def _get_cached_dev_ports(self) -> Set[int]:
        """Get cached dev ports to avoid repeated file I/O"""
        current_time = time.time()
        if (self._dev_ports_cache is None or 
            current_time - self._dev_ports_cache_time > 30):  # Cache for 30 seconds
            self._dev_ports_cache = set(load_dev_ports())
            self._dev_ports_cache_time = current_time
        return self._dev_ports_cache

    def check_for_conflict(self, port: int) -> bool:
        """Check if port conflicts with configured dev ports"""
        return port in self._get_cached_dev_ports()

    async def scan_ports(self, filter_str: Optional[str] = None) -> List[Dict[str, Any]]:
        """Main scanning method with fallbacks and caching"""
        # Check cache first
        cache_key = f"scan_{filter_str or 'all'}"
        current_time = time.time()
        
        if (cache_key in self.cache and 
            current_time - self.cache[cache_key]['timestamp'] < self.cache_timeout):
            logger.debug("Returning cached scan results")
            return self.cache[cache_key]['data']

        # Scan using available methods
        results = []
        scan_success = False
        
        for method in self.available_methods:
            try:
                logger.debug(f"Attempting scan with method: {method.value}")
                results = await self._scan_with_method(method, filter_str)
                scan_success = True
                logger.debug(f"Scan successful with {method.value}: {len(results)} connections")
                break
            except Exception as e:
                logger.warning(f"Scan method {method.value} failed: {e}")
                continue
        
        if not scan_success:
            logger.error("All scan methods failed, attempting emergency fallback")
            results = await self._emergency_fallback_scan(filter_str)

        # Process and enhance results
        processed_results = await self._process_scan_results(results, filter_str)
        
        # Cache results
        self.cache[cache_key] = {
            'data': processed_results,
            'timestamp': current_time
        }
        
        self.last_scan_time = current_time
        return processed_results

    async def _scan_with_method(self, method: ScanMethod, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using a specific method"""
        loop = asyncio.get_event_loop()
        
        if method == ScanMethod.PSUTIL:
            return await loop.run_in_executor(self.executor, self._scan_psutil, filter_str)
        elif method == ScanMethod.NETSTAT:
            return await loop.run_in_executor(self.executor, self._scan_netstat, filter_str)
        elif method == ScanMethod.SS:
            return await loop.run_in_executor(self.executor, self._scan_ss, filter_str)
        elif method == ScanMethod.LSOF:
            return await loop.run_in_executor(self.executor, self._scan_lsof, filter_str)
        elif method == ScanMethod.POWERSHELL:
            return await loop.run_in_executor(self.executor, self._scan_powershell, filter_str)
        else:
            raise ValueError(f"Unknown scan method: {method}")

    def _scan_psutil(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using psutil with enhanced error handling"""
        connections = []
        
        try:
            # Try different connection types based on platform
            connection_types = ['inet']
            if self.system == 'windows':
                connection_types.extend(['inet4', 'inet6'])
            
            for conn_type in connection_types:
                try:
                    for conn in psutil.net_connections(kind=conn_type):
                        if not conn.laddr or not hasattr(conn.laddr, 'port'):
                            continue
                        
                        connection_info = self._extract_psutil_info(conn)
                        if connection_info and self._matches_filter(connection_info, filter_str):
                            connections.append(connection_info)
                            
                except (psutil.AccessDenied, AttributeError) as e:
                    logger.debug(f"psutil {conn_type} failed: {e}")
                    continue
                    
                # If we got results, don't try other types
                if connections:
                    break
                    
        except Exception as e:
            logger.error(f"psutil scan completely failed: {e}")
            raise
        
        return connections

    def _extract_psutil_info(self, conn) -> Optional[ConnectionInfo]:
        """Extract connection information from psutil connection"""
        try:
            port = conn.laddr.port
            pid = conn.pid or 0
            status = conn.status or "UNKNOWN"
            local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
            protocol = "TCP" if hasattr(conn, 'type') and conn.type == socket.SOCK_STREAM else "UDP"
            
            process_name = ""
            process_path = None
            process_cmdline = None
            
            if pid and pid > 0:
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    try:
                        process_path = process.exe()
                        process_cmdline = ' '.join(process.cmdline()[:3])  # Limit cmdline length
                    except (psutil.AccessDenied, psutil.NoSuchProcess):
                        pass
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    process_name = f"PID:{pid}"
            
            return ConnectionInfo(
                pid=pid if pid > 0 else None,
                port=port,
                process_name=process_name,
                status=status,
                local_address=local_addr,
                protocol=protocol,
                process_path=process_path,
                process_cmdline=process_cmdline
            )
            
        except Exception as e:
            logger.debug(f"Failed to extract connection info: {e}")
            return None

    def _scan_netstat(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using netstat command"""
        connections = []
        
        try:
            if self.system == "windows":
                cmd = ["netstat", "-ano", "-p", "TCP"]
            else:  # Unix/Linux/macOS
                cmd = ["netstat", "-tuln", "-p"] if self.system == "linux" else ["netstat", "-an", "-f", "inet"]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_netstat_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"netstat scan failed: {e}")
            raise
        
        return connections

    def _parse_netstat_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse netstat output across different platforms"""
        connections = []
        lines = output.strip().split('\n')
        
        for line in lines:
            try:
                parts = line.split()
                if len(parts) < 4:
                    continue
                
                # Skip header lines
                if any(header in line.lower() for header in ['proto', 'active', 'local', 'foreign']):
                    continue
                
                protocol = parts[0].upper()
                if protocol not in ['TCP', 'UDP']:
                    continue
                
                local_addr = parts[1] if len(parts) > 1 else ""
                status = parts[3] if len(parts) > 3 else "UNKNOWN"
                
                # Extract port from address
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                else:
                    continue
                
                # Extract PID (Windows includes it, Unix might not)
                pid = None
                if len(parts) > 4 and self.system == "windows":
                    try:
                        pid = int(parts[4])
                    except ValueError:
                        pass
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name="",  # Will be filled later if we have PID
                    status=status,
                    local_address=local_addr,
                    protocol=protocol
                )
                
                # Try to get process info if we have PID
                if pid:
                    try:
                        process = psutil.Process(pid)
                        connection_info.process_name = process.name()
                    except:
                        connection_info.process_name = f"PID:{pid}"
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse netstat line: {line} - {e}")
                continue
        
        return connections

    def _scan_ss(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using ss command (Linux)"""
        connections = []
        
        try:
            # ss with process info
            cmd = ["ss", "-tulnp"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_ss_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"ss scan failed: {e}")
            raise
        
        return connections

    def _parse_ss_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse ss command output"""
        connections = []
        lines = output.strip().split('\n')[1:]  # Skip header
        
        for line in lines:
            try:
                parts = line.split()
                if len(parts) < 5:
                    continue
                
                protocol = parts[0].upper()
                status = parts[1] if len(parts) > 1 else "UNKNOWN"
                local_addr = parts[4] if len(parts) > 4 else ""
                
                # Extract port
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                else:
                    continue
                
                # Extract process info from last column
                process_name = ""
                pid = None
                if len(parts) > 6:
                    process_info = parts[-1]
                    if 'pid=' in process_info:
                        try:
                            pid_part = process_info.split('pid=')[1].split(',')[0]
                            pid = int(pid_part)
                            
                            # Extract process name
                            if 'users:((' in process_info:
                                name_part = process_info.split('users:((')[1].split(',')[0].strip('"')
                                process_name = name_part
                        except:
                            pass
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name,
                    status=status,
                    local_address=local_addr,
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse ss line: {line} - {e}")
                continue
        
        return connections

    def _scan_lsof(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using lsof command (Unix/Linux/macOS)"""
        connections = []
        
        try:
            cmd = ["lsof", "-i", "-P", "-n", "-sTCP:LISTEN,UDP:*"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            
            if result.returncode != 0 and result.stderr:
                # lsof might return non-zero but still have useful output
                if not result.stdout.strip():
                    raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_lsof_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"lsof scan failed: {e}")
            raise
        
        return connections

    def _parse_lsof_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse lsof command output"""
        connections = []
        lines = output.strip().split('\n')[1:]  # Skip header
        
        for line in lines:
            try:
                parts = line.split()
                if len(parts) < 9:
                    continue
                
                process_name = parts[0]
                pid = int(parts[1])
                protocol = parts[7].upper() if len(parts) > 7 else "TCP"
                local_addr = parts[8] if len(parts) > 8 else ""
                
                # Extract port from address format like "*:8080" or "127.0.0.1:3000"
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                else:
                    continue
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name,
                    status="LISTEN",
                    local_address=local_addr,
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse lsof line: {line} - {e}")
                continue
        
        return connections

    def _scan_powershell(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using PowerShell on Windows"""
        connections = []
        
        try:
            # PowerShell command to get network connections with process info
            ps_cmd = """
            Get-NetTCPConnection | Where-Object {$_.State -eq 'Listen'} | 
            ForEach-Object {
                try {
                    $proc = Get-Process -Id $_.OwningProcess -ErrorAction Stop
                    "$($_.LocalAddress):$($_.LocalPort):$($_.OwningProcess):$($proc.ProcessName):TCP"
                } catch {
                    "$($_.LocalAddress):$($_.LocalPort):$($_.OwningProcess)::TCP"
                }
            }
            """
            
            result = subprocess.run(
                ["powershell", "-Command", ps_cmd],
                capture_output=True, text=True, timeout=15
            )
            
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, ["powershell"])
            
            connections = self._parse_powershell_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"PowerShell scan failed: {e}")
            raise
        
        return connections

    def _parse_powershell_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse PowerShell command output"""
        connections = []
        lines = output.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            try:
                parts = line.split(':')
                if len(parts) < 4:
                    continue
                
                local_ip = parts[0]
                port = int(parts[1])
                pid = int(parts[2]) if parts[2] else None
                process_name = parts[3] if len(parts) > 3 else ""
                protocol = parts[4] if len(parts) > 4 else "TCP"
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name,
                    status="LISTEN",
                    local_address=f"{local_ip}:{port}",
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse PowerShell line: {line} - {e}")
                continue
        
        return connections

    def _matches_filter(self, connection: ConnectionInfo, filter_str: Optional[str]) -> bool:
        """Check if connection matches the filter string"""
        if not filter_str:
            return True
        
        filter_lower = filter_str.lower()
        return (
            filter_lower in connection.process_name.lower() or
            filter_lower in str(connection.port) or
            (connection.process_cmdline and filter_lower in connection.process_cmdline.lower())
        )

    async def _process_scan_results(self, connections: List[ConnectionInfo], filter_str: Optional[str]) -> List[Dict[str, Any]]:
        """Process and convert scan results to expected format"""
        results = []
        
        for conn in connections:
            # Skip invalid connections
            if not conn.port or conn.port <= 0:
                continue
            
            # Add conflict detection note
            note = ""
            if self.check_for_conflict(conn.port):
                note = get_port_description(conn.port)
            
            result = {
                "pid": conn.pid,
                "port": conn.port,
                "process_name": conn.process_name,
                "status": conn.status,
                "note": note,
                "protocol": getattr(conn, 'protocol', 'TCP'),
                "local_address": getattr(conn, 'local_address', f"*:{conn.port}")
            }
            
            # Add enhanced info if available
            if hasattr(conn, 'process_path') and conn.process_path:
                result["process_path"] = conn.process_path
            if hasattr(conn, 'process_cmdline') and conn.process_cmdline:
                result["process_cmdline"] = conn.process_cmdline
            
            results.append(result)
        
        # Remove duplicates based on port+pid combination
        unique_results = []
        seen = set()
        for result in results:
            key = (result["port"], result.get("pid"))
            if key not in seen:
                seen.add(key)
                unique_results.append(result)
        
        return unique_results

    async def _emergency_fallback_scan(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Emergency fallback when all other methods fail"""
        logger.warning("Using emergency fallback scan method")
        connections = []
        
        try:
            # Try basic socket approach for common ports
            common_ports = [22, 80, 443, 3000, 3001, 5000, 8000, 8080, 9000]
            
            async def check_port(port: int) -> Optional[ConnectionInfo]:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)  # Very short timeout
                    result = sock.connect_ex(('127.0.0.1', port))
                    sock.close()
                    
                    if result == 0:  # Port is open
                        return ConnectionInfo(
                            pid=None,
                            port=port,
                            process_name="Unknown",
                            status="LISTEN",
                            local_address=f"127.0.0.1:{port}",
                            protocol="TCP"
                        )
                except:
                    pass
                return None
            
            # Check ports concurrently
            tasks = [check_port(port) for port in common_ports]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for result in results:
                if isinstance(result, ConnectionInfo):
                    if not filter_str or self._matches_filter(result, filter_str):
                        connections.append(result)
            
        except Exception as e:
            logger.error(f"Emergency fallback failed: {e}")
        
        return connections

    def cleanup(self):
        """Cleanup scanner resources"""
        if hasattr(self, 'executor'):
            self.executor.shutdown(wait=True)

# Global scanner instance
_scanner: Optional[CrossPlatformScanner] = None

def get_scanner() -> CrossPlatformScanner:
    """Get or create the global scanner instance"""
    global _scanner
    if _scanner is None:
        _scanner = CrossPlatformScanner()
    return _scanner

# Backwards compatible functions
def check_for_conflict(port: int) -> bool:
    """Check if port conflicts with configured dev ports"""
    return get_scanner().check_for_conflict(port)

async def scan_ports(filter_str: Optional[str] = None) -> List[Dict[str, Any]]:
    """Main port scanning function with cross-platform support"""
    scanner = get_scanner()
    return await scanner.scan_ports(filter_str)

async def scan_changes(old_data: List[Dict[str, Any]], new_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect changes between scan results"""
    def _compute_changes():
        # Create comparison keys for more accurate change detection
        def make_key(item):
            return (item.get('port'), item.get('pid'), item.get('process_name'))
        
        old_keys = {make_key(item) for item in old_data}
        new_items = []
        
        for item in new_data:
            if make_key(item) not in old_keys:
                new_items.append(item)
        
        return new_items
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _compute_changes)

# Enhanced conflict checking with detailed process info
async def check_for_conflict_detailed(port: int) -> Optional[Dict[str, Any]]:
    """Get detailed conflict information for a port"""
    try:
        scanner = get_scanner()
        connections = await scanner.scan_ports()
        
        for conn in connections:
            if conn.get('port') == port:
                conflict_info = {
                    'port': port,
                    'pid': conn.get('pid'),
                    'process_name': conn.get('process_name', 'Unknown'),
                    'status': conn.get('status', 'Unknown'),
                    'is_conflict': scanner.check_for_conflict(port),
                    'description': get_port_description(port) if scanner.check_for_conflict(port) else None,
                    'protocol': conn.get('protocol', 'TCP'),
                    'local_address': conn.get('local_address', f'*:{port}')
                }
                
                if 'process_path' in conn:
                    conflict_info['process_path'] = conn['process_path']
                if 'process_cmdline' in conn:
                    conflict_info['process_cmdline'] = conn['process_cmdline']
                
                return conflict_info
        
        return None
    except Exception as e:
        logger.error(f"Detailed conflict check failed for port {port}: {e}")
        return None

# Cleanup function
def cleanup_scanner():
    """Cleanup scanner resources"""
    global _scanner
    if _scanner is not None:
        _scanner.cleanup()
        _scanner = None