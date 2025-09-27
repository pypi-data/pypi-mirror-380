"""
Hosts file management for blocking websites
"""

import os
import platform
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional


class HostsManager:
    """Manages the system hosts file for website blocking"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.hosts_path = self._get_hosts_path()
        self.backup_path = self._get_backup_path()
        self.stopweb_marker = "# StopWeb:"
        
    def _get_hosts_path(self) -> Path:
        """Get the path to the system hosts file"""
        if self.system == "windows":
            return Path("C:/Windows/System32/drivers/etc/hosts")
        else:  # macOS and Linux
            return Path("/etc/hosts")
    
    def _get_backup_path(self) -> Path:
        """Get the path for hosts file backup"""
        return self.hosts_path.with_suffix('.stopweb_backup')
    
    def _requires_sudo(self) -> bool:
        """Check if we need sudo privileges"""
        return self.system != "windows"
    
    def backup_hosts_file(self) -> bool:
        """Create a backup of the hosts file"""
        try:
            if not self.backup_path.exists():
                shutil.copy2(self.hosts_path, self.backup_path)
            return True
        except (PermissionError, FileNotFoundError) as e:
            print(f"❌ Failed to backup hosts file: {e}")
            return False
    
    def read_hosts_file(self) -> List[str]:
        """Read all lines from the hosts file"""
        try:
            with open(self.hosts_path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except (PermissionError, FileNotFoundError) as e:
            print(f"❌ Failed to read hosts file: {e}")
            return []
    
    def write_hosts_file(self, lines: List[str]) -> bool:
        """Write lines to the hosts file"""
        try:
            # Create backup first
            if not self.backup_hosts_file():
                return False
            
            with open(self.hosts_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            return True
        except PermissionError:
            print(f"❌ Permission denied. Please run with {'administrator privileges' if self.system == 'windows' else 'sudo'}")
            return False
        except Exception as e:
            print(f"❌ Failed to write hosts file: {e}")
            return False
    
    def add_blocked_site(self, domain: str, expires_at: datetime) -> bool:
        """Add a blocked site to the hosts file"""
        lines = self.read_hosts_file()
        if not lines:
            return False
        
        # Remove existing entry for this domain
        lines = [line for line in lines if not (self.stopweb_marker in line and domain in line)]
        
        # Add new blocking entry
        expires_str = expires_at.strftime("%Y-%m-%d %H:%M:%S")
        blocking_line = f"127.0.0.1    {domain}    {self.stopweb_marker} expires {expires_str}\n"
        
        # Add both www and non-www versions
        lines.append(blocking_line)
        if not domain.startswith('www.'):
            www_line = f"127.0.0.1    www.{domain}    {self.stopweb_marker} expires {expires_str}\n"
            lines.append(www_line)
        elif domain.startswith('www.'):
            non_www = domain[4:]  # Remove 'www.'
            non_www_line = f"127.0.0.1    {non_www}    {self.stopweb_marker} expires {expires_str}\n"
            lines.append(non_www_line)
        
        return self.write_hosts_file(lines)
    
    def remove_blocked_site(self, domain: str) -> bool:
        """Remove a blocked site from the hosts file"""
        lines = self.read_hosts_file()
        if not lines:
            return False
        
        # Remove entries for this domain (both www and non-www)
        original_count = len(lines)
        lines = [line for line in lines if not (
            self.stopweb_marker in line and (
                f"    {domain}    " in line or
                f"    www.{domain}    " in line or
                f"    {domain.replace('www.', '')}    " in line
            )
        )]
        
        if len(lines) < original_count:
            return self.write_hosts_file(lines)
        
        return True  # No entries found to remove
    
    def get_blocked_sites(self) -> List[Tuple[str, datetime]]:
        """Get list of currently blocked sites with their expiration times"""
        lines = self.read_hosts_file()
        blocked_sites = []
        
        for line in lines:
            if self.stopweb_marker in line and "expires" in line:
                try:
                    # Parse: 127.0.0.1    domain.com    # StopWeb: expires 2024-01-15 14:30:00
                    parts = line.strip().split()
                    if len(parts) >= 6:
                        domain = parts[1]
                        expires_str = f"{parts[-2]} {parts[-1]}"
                        expires_at = datetime.strptime(expires_str, "%Y-%m-%d %H:%M:%S")
                        blocked_sites.append((domain, expires_at))
                except (ValueError, IndexError):
                    continue
        
        return blocked_sites
    
    def cleanup_expired_sites(self) -> int:
        """Remove expired blocked sites, return count of removed sites"""
        lines = self.read_hosts_file()
        if not lines:
            return 0
        
        now = datetime.now()
        original_count = len(lines)
        new_lines = []
        
        for line in lines:
            if self.stopweb_marker in line and "expires" in line:
                try:
                    parts = line.strip().split()
                    if len(parts) >= 6:
                        expires_str = f"{parts[-2]} {parts[-1]}"
                        expires_at = datetime.strptime(expires_str, "%Y-%m-%d %H:%M:%S")
                        if expires_at > now:  # Keep if not expired
                            new_lines.append(line)
                        # Skip expired entries (don't add to new_lines)
                    else:
                        new_lines.append(line)  # Keep malformed StopWeb lines
                except (ValueError, IndexError):
                    new_lines.append(line)  # Keep malformed lines
            else:
                new_lines.append(line)  # Keep non-StopWeb lines
        
        removed_count = original_count - len(new_lines)
        
        if removed_count > 0:
            self.write_hosts_file(new_lines)
        
        return removed_count
    
    def remove_all_blocked_sites(self) -> int:
        """Remove all StopWeb blocked sites, return count of removed sites"""
        lines = self.read_hosts_file()
        if not lines:
            return 0
        
        original_count = len(lines)
        lines = [line for line in lines if self.stopweb_marker not in line]
        removed_count = original_count - len(lines)
        
        if removed_count > 0:
            self.write_hosts_file(lines)
        
        return removed_count
    
    def check_permissions(self) -> bool:
        """Check if we have permission to modify hosts file"""
        try:
            # Try to read the hosts file
            with open(self.hosts_path, 'r') as f:
                pass
            
            # Try to write (append mode to avoid damaging the file)
            with open(self.hosts_path, 'a') as f:
                pass
            
            return True
        except PermissionError:
            return False
        except FileNotFoundError:
            return False


def get_domain_from_url(url: str) -> str:
    """Extract domain from URL"""
    # Remove protocol if present
    if url.startswith(('http://', 'https://')):
        url = url.split('://', 1)[1]
    
    # Remove path if present
    if '/' in url:
        url = url.split('/', 1)[0]
    
    # Remove port if present
    if ':' in url:
        url = url.split(':', 1)[0]
    
    return url.lower().strip()