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

# Cleanup function
def cleanup_scanner():
    """Cleanup scanner resources"""
    global _scanner
    if _scanner is not None:
        _scanner.cleanup()
        _scanner = None

# Diagnostic functions for troubleshooting
async def diagnose_scanner() -> Dict[str, Any]:
    """Diagnose scanner capabilities and issues"""
    scanner = get_scanner()
    
    diagnosis = {
        'platform': platform.system(),
        'platform_version': platform.release(),
        'available_methods': [m.value for m in scanner.available_methods],
        'tests': {}
    }
    
    # Test each method
    for method in scanner.available_methods:
        test_result = {'available': True, 'error': None, 'result_count': 0}
        
        try:
            results = await scanner._scan_with_method(method, None)
            test_result['result_count'] = len(results)
        except Exception as e:
            test_result['available'] = False
            test_result['error'] = str(e)
        
        diagnosis['tests'][method.value] = test_result
    
    # Check permissions
    diagnosis['permissions'] = {
        'can_read_proc_net': False,
        'can_use_psutil': False,
        'effective_uid': None
    }
    
    try:
        import os
        diagnosis['permissions']['effective_uid'] = os.geteuid() if hasattr(os, 'geteuid') else 'N/A'
        
        # Check /proc/net access on Linux
        if scanner.system == 'linux':
            try:
                with open('/proc/net/tcp', 'r') as f:
                    f.read(100)
                diagnosis['permissions']['can_read_proc_net'] = True
            except:
                pass
        
        # Check psutil
        try:
            psutil.net_connections()
            diagnosis['permissions']['can_use_psutil'] = True
        except:
            pass
            
    except Exception as e:
        diagnosis['permissions']['error'] = str(e)
    
    return diagnosis

 

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
            # On Linux, psutil requires root for full connection info
            # Try with 'all' first, then fall back to 'inet'
            connection_types = ['all', 'inet', 'inet4', 'inet6', 'tcp', 'tcp4', 'tcp6']
            
            for conn_type in connection_types:
                try:
                    logger.debug(f"Trying psutil with kind='{conn_type}'")
                    conns_found = 0
                    
                    for conn in psutil.net_connections(kind=conn_type):
                        if not conn.laddr or not hasattr(conn.laddr, 'port'):
                            continue
                        
                        # On Linux, only get LISTEN connections
                        if self.system == 'linux' and hasattr(conn, 'status'):
                            if conn.status != psutil.CONN_LISTEN:
                                continue
                        
                        connection_info = self._extract_psutil_info(conn)
                        if connection_info and self._matches_filter(connection_info, filter_str):
                            connections.append(connection_info)
                            conns_found += 1
                    
                    logger.debug(f"psutil {conn_type} found {conns_found} connections")
                    
                    # If we got results, use them
                    if connections:
                        break
                            
                except (psutil.AccessDenied, AttributeError, PermissionError) as e:
                    logger.debug(f"psutil {conn_type} not accessible: {e}")
                    continue
                except Exception as e:
                    logger.debug(f"psutil {conn_type} error: {e}")
                    continue
            
            if not connections:
                # psutil failed completely, raise to try next method
                raise PermissionError("psutil requires elevated permissions or is not working")
                    
        except Exception as e:
            logger.error(f"psutil scan failed: {e}")
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
            elif self.system == "linux":
                # Linux: try with sudo first for better results, fallback to non-sudo
                cmd = ["netstat", "-tulpn"]  # -p requires root but try anyway
            else:  # macOS
                cmd = ["netstat", "-an", "-f", "inet", "-p", "tcp"]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            # On Linux, netstat might fail without sudo, that's okay
            if result.returncode != 0:
                logger.debug(f"netstat failed with code {result.returncode}, stderr: {result.stderr[:100]}")
                # Try without -p flag for Linux
                if self.system == "linux":
                    cmd = ["netstat", "-tuln"]  # Without process info
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.stdout:
                connections = self._parse_netstat_output(result.stdout, filter_str)
            else:
                raise subprocess.CalledProcessError(result.returncode, cmd)
            
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
            # Try with process info first
            cmd = ["ss", "-tulpn"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            # If failed (likely permission issue), try without process info
            if result.returncode != 0 or not result.stdout.strip():
                logger.debug(f"ss with -p failed, trying without process info")
                cmd = ["ss", "-tuln"]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0 and not result.stdout.strip():
                raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_ss_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"ss scan failed: {e}")
            raise
        
        return connections

    def _parse_ss_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse ss command output"""
        connections = []
        lines = output.strip().split('\n')
        
        # Skip header lines
        start_index = 0
        for i, line in enumerate(lines):
            if any(header in line.lower() for header in ['netid', 'state', 'recv-q']):
                start_index = i + 1
                break
        
        for line in lines[start_index:]:
            if not line.strip():
                continue
                
            try:
                parts = line.split()
                if len(parts) < 5:
                    continue
                
                protocol = parts[0].upper() if parts[0] else "TCP"
                status = parts[1] if len(parts) > 1 else "UNKNOWN"
                
                # Find local address (varies by format)
                local_addr = ""
                for i, part in enumerate(parts):
                    if ':' in part and not part.startswith('['):
                        local_addr = part
                        break
                
                if not local_addr:
                    continue
                
                # Extract port
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    # Handle asterisks
                    if '*' in port_str:
                        continue
                    try:
                        port = int(port_str)
                    except ValueError:
                        continue
                else:
                    continue
                
                # Extract process info from last column (if available)
                process_name = ""
                pid = None
                
                # Look for process info in format: users:(("name",pid=123,fd=4))
                process_col = ' '.join(parts[5:]) if len(parts) > 5 else ""
                if 'users:' in process_col or 'pid=' in process_col:
                    try:
                        if 'pid=' in process_col:
                            pid_match = process_col.split('pid=')[1].split(',')[0].split(')')[0]
                            pid = int(pid_match)
                        
                        if '(("' in process_col:
                            name_match = process_col.split('(("')[1].split('"')[0]
                            process_name = name_match
                    except Exception as e:
                        logger.debug(f"Failed to parse process info from: {process_col} - {e}")
                
                connection_info = ConnectionInfo(
                    pid=pid,
                    port=port,
                    process_name=process_name or "",
                    status=status if status != "UNCONN" else "LISTEN",
                    local_address=local_addr,
                    protocol=protocol
                )
                
                if self._matches_filter(connection_info, filter_str):
                    connections.append(connection_info)
                    
            except Exception as e:
                logger.debug(f"Failed to parse ss line: '{line}' - {e}")
                continue
        
        return connections

    def _scan_lsof(self, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Scan using lsof command (Unix/Linux/macOS)"""
        connections = []
        
        try:
            # lsof with various filter options
            # -i: network files
            # -P: no port name conversion
            # -n: no DNS resolution (faster)
            # -sTCP:LISTEN: only LISTEN state for TCP
            cmd = ["lsof", "-i", "-P", "-n"]
            
            # Add state filter if not already there (some systems might not support it)
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            
            # lsof might return non-zero but still have output
            if not result.stdout.strip():
                logger.warning(f"lsof returned no output, stderr: {result.stderr[:200]}")
                if result.returncode != 0:
                    raise subprocess.CalledProcessError(result.returncode, cmd)
            
            connections = self._parse_lsof_output(result.stdout, filter_str)
            
        except Exception as e:
            logger.error(f"lsof scan failed: {e}")
            raise
        
        return connections

    def _parse_lsof_output(self, output: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Parse lsof command output"""
        connections = []
        lines = output.strip().split('\n')
        
        # Skip header line
        start_index = 0
        for i, line in enumerate(lines):
            if line.startswith('COMMAND'):
                start_index = i + 1
                break
        
        for line in lines[start_index:]:
            if not line.strip():
                continue
                
            try:
                parts = line.split()
                if len(parts) < 8:
                    continue
                
                process_name = parts[0]
                pid = int(parts[1])
                
                # Protocol is usually at index 7
                protocol_col = parts[7] if len(parts) > 7 else ""
                protocol = "TCP"
                if "UDP" in protocol_col.upper():
                    protocol = "UDP"
                elif "TCP" in protocol_col.upper():
                    protocol = "TCP"
                
                # Local address is usually at index 8
                local_addr = parts[8] if len(parts) > 8 else ""
                
                # Status might be in the protocol field or separate
                status = "LISTEN"
                if "(" in protocol_col:
                    status_match = protocol_col.split('(')[1].split(')')[0]
                    status = status_match
                
                # Extract port from address format like "*:8080", "127.0.0.1:3000", or "[::1]:8080"
                port = None
                if ':' in local_addr:
                    port_str = local_addr.split(':')[-1]
                    # Remove any parentheses or other characters
                    port_str = port_str.split('(')[0].strip()
                    try:
                        port = int(port_str)
                    except ValueError:
                        # Might be a service name, skip it
                        continue
                else:
                    continue
                
                # Only include LISTEN connections
                if status.upper() not in ['LISTEN', 'BOUND']:
                    continue
                
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
                logger.debug(f"Failed to parse lsof line: '{line}' - {e}")
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
        logger.warning("Using emergency fallback scan method - checking /proc/net on Linux")
        connections = []
        
        try:
            # Linux-specific: read /proc/net/tcp and /proc/net/tcp6
            if self.system == 'linux':
                connections.extend(await self._read_proc_net('tcp', filter_str))
                connections.extend(await self._read_proc_net('tcp6', filter_str))
            
            # If still no connections, try socket probing
            if not connections:
                logger.warning("Trying socket probing as last resort")
                # Get dev ports and common ports
                dev_ports = list(self._get_cached_dev_ports())
                common_ports = [22, 80, 443, 3000, 3001, 3306, 5000, 5432, 8000, 8080, 9000, 27017]
                all_ports = list(set(dev_ports + common_ports))
                
                async def check_port(port: int) -> Optional[ConnectionInfo]:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.1)
                        result = sock.connect_ex(('127.0.0.1', port))
                        sock.close()
                        
                        if result == 0:
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
                tasks = [check_port(port) for port in all_ports]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                
                for result in results:
                    if isinstance(result, ConnectionInfo):
                        if not filter_str or self._matches_filter(result, filter_str):
                            connections.append(result)
            
        except Exception as e:
            logger.error(f"Emergency fallback failed: {e}")
        
        return connections
    
    async def _read_proc_net(self, protocol: str, filter_str: Optional[str]) -> List[ConnectionInfo]:
        """Read /proc/net/tcp or /proc/net/tcp6 directly (Linux only)"""
        connections = []
        
        try:
            proc_file = f"/proc/net/{protocol}"
            with open(proc_file, 'r') as f:
                lines = f.readlines()[1:]  # Skip header
            
            for line in lines:
                try:
                    parts = line.split()
                    if len(parts) < 10:
                        continue
                    
                    # Parse local address (format: "0100007F:1F90" = 127.0.0.1:8080)
                    local_addr_hex = parts[1]
                    if ':' not in local_addr_hex:
                        continue
                    
                    addr_hex, port_hex = local_addr_hex.split(':')
                    port = int(port_hex, 16)
                    
                    # Parse status (0A = LISTEN in hex)
                    status_hex = parts[3]
                    if status_hex != '0A':  # Only LISTEN connections
                        continue
                    
                    # Try to get PID from /proc
                    pid = None
                    inode = parts[9]
                    pid = self._find_pid_by_inode(inode)
                    
                    # Get process name if we have PID
                    process_name = ""
                    if pid:
                        try:
                            process = psutil.Process(pid)
                            process_name = process.name()
                        except:
                            process_name = f"PID:{pid}"
                    
                    connection_info = ConnectionInfo(
                        pid=pid,
                        port=port,
                        process_name=process_name,
                        status="LISTEN",
                        local_address=f"*:{port}",
                        protocol="TCP" if protocol.startswith('tcp') else "UDP"
                    )
                    
                    if not filter_str or self._matches_filter(connection_info, filter_str):
                        connections.append(connection_info)
                        
                except Exception as e:
                    logger.debug(f"Failed to parse /proc/net line: {line.strip()} - {e}")
                    continue
                    
        except Exception as e:
            logger.debug(f"Failed to read {proc_file}: {e}")
        
        return connections
    
    def _find_pid_by_inode(self, inode: str) -> Optional[int]:
        """Find PID by socket inode (Linux)"""
        try:
            import os
            import glob
            
            # Search /proc/*/fd/* for matching socket inode
            for pid_dir in glob.glob('/proc/[0-9]*'):
                try:
                    pid = int(os.path.basename(pid_dir))
                    fd_dir = os.path.join(pid_dir, 'fd')
                    
                    for fd in os.listdir(fd_dir):
                        try:
                            link = os.readlink(os.path.join(fd_dir, fd))
                            if f'socket:[{inode}]' in link:
                                return pid
                        except (OSError, PermissionError):
                            continue
                except (ValueError, PermissionError, FileNotFoundError):
                    continue
        except Exception as e:
            logger.debug(f"Failed to find PID for inode {inode}: {e}")
        
        return None

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