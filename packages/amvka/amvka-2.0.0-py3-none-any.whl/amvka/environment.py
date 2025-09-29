"""
Environment detection and command compatibility for Amvka.
"""

import os
import platform
import subprocess
import sys
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class EnvironmentDetector:
    """Detects the current shell, OS, and available commands."""
    
    def __init__(self):
        self.os_type = platform.system()
        self.shell_info = self._detect_shell()
        self.command_db = CommandDatabase()
    
    def _detect_shell(self) -> Dict[str, str]:
        """Detect the current shell environment."""
        shell_info = {
            "shell": "unknown",
            "version": "",
            "executable": "",
            "features": []
        }
        
        # Check environment variables for shell detection
        if os.getenv("PSModulePath"):  # PowerShell
            shell_info["shell"] = "powershell"
            shell_info["features"] = ["cmdlets", "aliases", "functions", "variables"]
            try:
                result = subprocess.run(
                    ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"],
                    capture_output=True, text=True, timeout=5
                )
                if result.returncode == 0:
                    shell_info["version"] = result.stdout.strip()
            except:
                pass
        
        elif os.getenv("COMSPEC") and "cmd.exe" in os.getenv("COMSPEC", ""):  # CMD
            shell_info["shell"] = "cmd"
            shell_info["features"] = ["batch_commands", "environment_variables"]
            shell_info["executable"] = os.getenv("COMSPEC", "")
        
        elif os.getenv("BASH_VERSION"):  # Bash
            shell_info["shell"] = "bash"
            shell_info["features"] = ["unix_commands", "pipes", "redirections", "scripting"]
            shell_info["version"] = os.getenv("BASH_VERSION", "")
        
        elif os.getenv("ZSH_VERSION"):  # Zsh
            shell_info["shell"] = "zsh"
            shell_info["features"] = ["unix_commands", "pipes", "redirections", "scripting", "advanced_completion"]
            shell_info["version"] = os.getenv("ZSH_VERSION", "")
        
        elif "fish" in os.getenv("SHELL", ""):  # Fish
            shell_info["shell"] = "fish"
            shell_info["features"] = ["unix_commands", "pipes", "redirections", "user_friendly"]
        
        else:
            # Fallback detection based on OS
            if self.os_type == "Windows":
                shell_info["shell"] = "cmd"  # Default assumption for Windows
                shell_info["features"] = ["batch_commands"]
            else:
                shell_info["shell"] = "bash"  # Default assumption for Unix-like
                shell_info["features"] = ["unix_commands", "pipes", "redirections"]
        
        return shell_info
    
    def get_environment_context(self) -> Dict:
        """Get comprehensive environment context."""
        return {
            "os": self.os_type,
            "shell": self.shell_info["shell"],
            "shell_version": self.shell_info["version"],
            "shell_features": self.shell_info["features"],
            "supported_commands": self.command_db.get_supported_commands(
                self.os_type, self.shell_info["shell"]
            ),
            "command_examples": self.command_db.get_command_examples(
                self.os_type, self.shell_info["shell"]
            )
        }
    
    def is_command_available(self, command: str) -> bool:
        """Check if a specific command is available in the current environment."""
        return self.command_db.is_command_supported(
            command, self.os_type, self.shell_info["shell"]
        )
    
    def get_alternative_command(self, intent: str) -> Optional[str]:
        """Get the appropriate command for the current environment based on intent."""
        return self.command_db.get_command_for_intent(
            intent, self.os_type, self.shell_info["shell"]
        )


class CommandDatabase:
    """Database of commands and their compatibility across different environments."""
    
    def __init__(self):
        self.commands = self._build_command_database()
        self.intent_map = self._build_intent_database()
    
    def _build_command_database(self) -> Dict:
        """Build comprehensive command compatibility database."""
        return {
            # File operations
            "Get-ChildItem": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "file_operations",
                "description": "List files and directories"
            },
            "ls": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "file_operations",
                "description": "List files and directories"
            },
            "dir": {
                "platforms": ["Windows"],
                "shells": ["cmd", "powershell"],
                "category": "file_operations",
                "description": "List files and directories"
            },
            
            # Navigation
            "Get-Location": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "navigation",
                "description": "Get current directory"
            },
            "pwd": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "navigation",
                "description": "Print working directory"
            },
            "cd": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "navigation",
                "description": "Change directory"
            },
            
            # File creation
            "New-Item": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "file_creation",
                "description": "Create new files or directories"
            },
            "touch": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "file_creation",
                "description": "Create empty file or update timestamp"
            },
            "echo": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "file_creation",
                "description": "Display text or create file with content"
            },
            
            # Programming languages and interpreters
            "python": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Python interpreter"
            },
            "python3": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Python 3 interpreter"
            },
            "node": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Node.js runtime"
            },
            "npm": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Node package manager"
            },
            "java": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Java runtime"
            },
            "javac": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "Java compiler"
            },
            "gcc": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "programming",
                "description": "GNU Compiler Collection"
            },
            "git": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "version_control",
                "description": "Git version control system"
            },
            
            # Networking commands
            "netstat": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "networking",
                "description": "Display network connections and listening ports"
            },
            "Get-NetTCPConnection": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "networking",
                "description": "Get TCP connections and listening ports"
            },
            "Test-NetConnection": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "networking",
                "description": "Test network connectivity"
            },
            "ss": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "networking",
                "description": "Display socket statistics"
            },
            "lsof": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "networking",
                "description": "List open files and network connections"
            },
            
            # Software detection commands
            "Get-Command": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "software_detection",
                "description": "Check if command/software exists"
            },
            "where": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "software_detection",
                "description": "Locate command or show path"
            },
            "which": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "software_detection",
                "description": "Locate command in PATH"
            },
            
            # Software detection commands
            "Get-Command": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "software_detection",
                "description": "Check if command/software exists"
            },
            "where": {
                "platforms": ["Windows", "Linux", "Darwin", "Unix"],
                "shells": ["cmd", "powershell", "bash", "zsh", "fish", "sh"],
                "category": "software_detection",
                "description": "Locate command or show path"
            },
            "which": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "software_detection",
                "description": "Locate command in PATH"
            },
            
            # File manipulation
            "Copy-Item": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "file_manipulation",
                "description": "Copy files or directories"
            },
            "cp": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "file_manipulation",
                "description": "Copy files or directories"
            },
            "copy": {
                "platforms": ["Windows"],
                "shells": ["cmd"],
                "category": "file_manipulation",
                "description": "Copy files"
            },
            
            # Process management
            "Get-Process": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "process_management",
                "description": "Get running processes"
            },
            "ps": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "process_management",
                "description": "Show running processes"
            },
            "tasklist": {
                "platforms": ["Windows"],
                "shells": ["cmd"],
                "category": "process_management",
                "description": "List running tasks"
            },
            
            # Text processing
            "Select-String": {
                "platforms": ["Windows"],
                "shells": ["powershell"],
                "category": "text_processing",
                "description": "Search text patterns"
            },
            "grep": {
                "platforms": ["Linux", "Darwin", "Unix"],
                "shells": ["bash", "zsh", "fish", "sh"],
                "category": "text_processing",
                "description": "Search text patterns"
            },
            "findstr": {
                "platforms": ["Windows"],
                "shells": ["cmd"],
                "category": "text_processing",
                "description": "Find strings in files"
            }
        }
    
    def _build_intent_database(self) -> Dict:
        """Build intent-to-command mapping."""
        return {
            "list_files": {
                "Windows": {
                    "powershell": "Get-ChildItem",
                    "cmd": "dir"
                },
                "Linux": {
                    "bash": "ls -la",
                    "zsh": "ls -la",
                    "fish": "ls -la"
                },
                "Darwin": {
                    "bash": "ls -la",
                    "zsh": "ls -la"
                }
            },
            "current_directory": {
                "Windows": {
                    "powershell": "Get-Location",
                    "cmd": "cd"
                },
                "Linux": {
                    "bash": "pwd",
                    "zsh": "pwd",
                    "fish": "pwd"
                },
                "Darwin": {
                    "bash": "pwd",
                    "zsh": "pwd"
                }
            },
            "create_file": {
                "Windows": {
                    "powershell": "New-Item -ItemType File -Name",
                    "cmd": "echo. >"
                },
                "Linux": {
                    "bash": "touch",
                    "zsh": "touch",
                    "fish": "touch"
                },
                "Darwin": {
                    "bash": "touch",
                    "zsh": "touch"
                }
            },
            "create_directory": {
                "Windows": {
                    "powershell": "New-Item -ItemType Directory -Name",
                    "cmd": "mkdir"
                },
                "Linux": {
                    "bash": "mkdir",
                    "zsh": "mkdir",
                    "fish": "mkdir"
                },
                "Darwin": {
                    "bash": "mkdir",
                    "zsh": "mkdir"
                }
            },
            "copy_file": {
                "Windows": {
                    "powershell": "Copy-Item",
                    "cmd": "copy"
                },
                "Linux": {
                    "bash": "cp",
                    "zsh": "cp",
                    "fish": "cp"
                },
                "Darwin": {
                    "bash": "cp",
                    "zsh": "cp"
                }
            },
            "show_processes": {
                "Windows": {
                    "powershell": "Get-Process",
                    "cmd": "tasklist"
                },
                "Linux": {
                    "bash": "ps aux",
                    "zsh": "ps aux",
                    "fish": "ps aux"
                },
                "Darwin": {
                    "bash": "ps aux",
                    "zsh": "ps aux"
                }
            },
            "check_port_availability": {
                "Windows": {
                    "powershell": "Get-NetTCPConnection -LocalPort",
                    "cmd": "netstat -an"
                },
                "Linux": {
                    "bash": "netstat -tuln | grep",
                    "zsh": "netstat -tuln | grep",
                    "fish": "netstat -tuln | grep"
                },
                "Darwin": {
                    "bash": "netstat -an | grep",
                    "zsh": "netstat -an | grep"
                }
            },
            "list_listening_ports": {
                "Windows": {
                    "powershell": "Get-NetTCPConnection -State Listen",
                    "cmd": "netstat -an | findstr LISTENING"
                },
                "Linux": {
                    "bash": "ss -tuln",
                    "zsh": "ss -tuln",
                    "fish": "ss -tuln"
                },
                "Darwin": {
                    "bash": "netstat -an | grep LISTEN",
                    "zsh": "netstat -an | grep LISTEN"
                }
            },
            "check_software_installed": {
                "Windows": {
                    "powershell": "Get-Command",
                    "cmd": "where"
                },
                "Linux": {
                    "bash": "which",
                    "zsh": "which",
                    "fish": "which"
                },
                "Darwin": {
                    "bash": "which",
                    "zsh": "which"
                }
            },
            "check_software_installed": {
                "Windows": {
                    "powershell": "Get-Command",
                    "cmd": "where"
                },
                "Linux": {
                    "bash": "which",
                    "zsh": "which",
                    "fish": "which"
                },
                "Darwin": {
                    "bash": "which",
                    "zsh": "which"
                }
            }
        }
    
    def get_supported_commands(self, os_type: str, shell: str) -> List[str]:
        """Get list of commands supported in the current environment."""
        supported = []
        for cmd, info in self.commands.items():
            if os_type in info["platforms"] and shell in info["shells"]:
                supported.append(cmd)
        return supported
    
    def get_command_examples(self, os_type: str, shell: str) -> Dict[str, str]:
        """Get command examples for the current environment."""
        examples = {}
        for intent, os_map in self.intent_map.items():
            if os_type in os_map and shell in os_map[os_type]:
                examples[intent] = os_map[os_type][shell]
        return examples
    
    def is_command_supported(self, command: str, os_type: str, shell: str) -> bool:
        """Check if a command is supported in the given environment."""
        if command not in self.commands:
            return False
        
        cmd_info = self.commands[command]
        return (os_type in cmd_info["platforms"] and 
                shell in cmd_info["shells"])
    
    def get_command_for_intent(self, intent: str, os_type: str, shell: str) -> Optional[str]:
        """Get the appropriate command for an intent in the given environment."""
        if intent not in self.intent_map:
            return None
        
        os_map = self.intent_map[intent]
        if os_type not in os_map:
            return None
        
        shell_map = os_map[os_type]
        if shell not in shell_map:
            return None
        
        return shell_map[shell]