"""
Secure command execution for Amvka with environment awareness.
"""

import subprocess
import sys
import os
import shlex
from typing import Optional, List

from .utils import print_error, print_success, print_info, print_warning
from .environment import EnvironmentDetector


class CommandExecutor:
    """Handles secure execution of shell commands."""
    
    def __init__(self):
        self.env_detector = EnvironmentDetector()
        self.allowed_commands = self._get_allowed_commands()
    
    def _get_allowed_commands(self) -> List[str]:
        """Get list of allowed commands based on current environment."""
        env_context = self.env_detector.get_environment_context()
        supported_commands = env_context["supported_commands"]
        
        # Base commands that are generally safe
        base_commands = [
            # Programming tools
            'python', 'python3', 'pip', 'pip3', 'node', 'npm', 'npx',
            'java', 'javac', 'gcc', 'g++', 'make', 'cmake',
            
            # Git commands
            'git',
            
            # Text editors (view mode)
            'nano', 'vim', 'vi', 'emacs',
        ]
        
        # Combine environment-specific commands with base commands
        return list(set(supported_commands + base_commands))
    
    def execute(self, command: str) -> bool:
        """Execute a command safely."""
        if not command or not command.strip():
            print_error("Empty command provided.")
            return False
        
        # Parse the command
        try:
            args = shlex.split(command)
        except ValueError as e:
            print_error(f"Invalid command syntax: {e}")
            return False
        
        if not args:
            print_error("No command to execute.")
            return False
        
        base_command = args[0]
        
        # Additional safety checks
        if not self._is_command_safe(command, base_command):
            return False
        
        print_info(f"Executing: {command}")
        
        try:
            # Get environment context for better execution
            env_context = self.env_detector.get_environment_context()
            os_type = env_context["os"]
            shell = env_context["shell"]
            
            # Check if this is a PowerShell cmdlet on Windows
            if (os_type == "Windows" and shell == "powershell" and 
                base_command.startswith(('Get-', 'Set-', 'New-', 'Remove-', 'Copy-', 'Move-', 
                                       'Rename-', 'Test-', 'Select-', 'Where-', 'Sort-', 
                                       'Group-', 'Measure-', 'Format-', 'Out-', 'Write-', 
                                       'Invoke-', 'Start-', 'Stop-'))):
                # Execute PowerShell cmdlet
                ps_command = ['powershell', '-Command', command]
                result = subprocess.run(
                    ps_command,
                    capture_output=True,
                    text=True,
                    timeout=30,  # 30 second timeout
                    cwd=os.getcwd()
                )
            else:
                # Execute regular command
                result = subprocess.run(
                    args,
                    capture_output=True,
                    text=True,
                    timeout=30,  # 30 second timeout
                    cwd=os.getcwd()
                )
            
            # Display output
            if result.stdout:
                print(result.stdout.rstrip())
            
            if result.stderr:
                print_warning("Errors/Warnings:")
                print(result.stderr.rstrip(), file=sys.stderr)
            
            # Check return code
            if result.returncode == 0:
                print_success(f"Command completed successfully (exit code: {result.returncode})")
                return True
            else:
                print_error(f"Command failed with exit code: {result.returncode}")
                return False
        
        except subprocess.TimeoutExpired:
            print_error("Command timed out after 30 seconds.")
            return False
        
        except subprocess.CalledProcessError as e:
            print_error(f"Command failed: {e}")
            return False
        
        except FileNotFoundError:
            print_error(f"Command not found: {base_command}")
            print_info("Make sure the command is installed and in your PATH.")
            return False
        
        except Exception as e:
            print_error(f"Unexpected error executing command: {e}")
            return False
    
    def _is_command_safe(self, full_command: str, base_command: str) -> bool:
        """Check if the command is safe to execute."""
        # Check if base command is in allowed list
        if base_command not in self.allowed_commands:
            print_warning(f"Command '{base_command}' is not in the allowed commands list.")
            
            # Ask for confirmation for unknown commands
            response = input(f"Do you want to execute '{base_command}' anyway? (Y/n): ").lower().strip()
            if response in ['n', 'no']:
                print_info("Command execution cancelled.")
                return False
        
        # Additional pattern-based safety checks
        dangerous_patterns = [
            r'rm\s+.*-rf.*/',  # rm with recursive force on root-like paths
            r'chmod\s+777\s+/',  # chmod 777 on root
            r'chown\s+.*:\s*/',  # chown on root
            r'>\s*/dev/',  # redirecting to device files
            r'sudo\s+.*',  # any sudo command
            r'su\s+.*',  # any su command
            r'passwd\s*',  # password changing
            r'userdel\s+.*',  # user deletion
            r'groupdel\s+.*',  # group deletion
            r'crontab\s+.*',  # cron modifications
            r'systemctl\s+.*',  # systemd service management
            r'service\s+.*',  # service management
        ]
        
        import re
        for pattern in dangerous_patterns:
            if re.search(pattern, full_command, re.IGNORECASE):
                print_error(f"Command contains potentially dangerous pattern and will not be executed.")
                return False
        
        # Check for command injection patterns
        injection_patterns = [
            r'[;&|`$()]',  # Command separators and substitution
            r'\$\(',  # Command substitution
            r'`.*`',  # Backtick command substitution
        ]
        
        # Allow some safe uses of these characters
        safe_exceptions = [
            r'git\s+.*',  # Git commands often use these safely
            r'find\s+.*-exec.*',  # Find with exec
            r'awk\s+.*',  # AWK scripts
            r'sed\s+.*',  # Sed scripts
            r'netstat\s+.*\|\s+findstr.*',  # Netstat with findstr
            r'Get-NetTCPConnection.*',  # PowerShell networking cmdlets
        ]
        
        for pattern in injection_patterns:
            if re.search(pattern, full_command):
                # Check if it's a safe exception
                is_safe_exception = any(
                    re.search(exception, full_command, re.IGNORECASE)
                    for exception in safe_exceptions
                )
                
                if not is_safe_exception:
                    print_error("Command contains shell metacharacters that could be unsafe.")
                    response = input("Do you still want to execute this command? (Y/n): ").lower().strip()
                    if response in ['n', 'no']:
                        print_info("Command execution cancelled.")
                        return False
        
        return True
    
    def test_command(self, command: str) -> bool:
        """Test if a command would be allowed (dry run)."""
        if not command or not command.strip():
            return False
        
        try:
            args = shlex.split(command)
            if not args:
                return False
            
            base_command = args[0]
            return self._is_command_safe(command, base_command)
        
        except ValueError:
            return False