"""
Utility functions for Amvka CLI.
"""

import os
import sys
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()


def print_error(message):
    """Print error message in red."""
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}", file=sys.stderr)


def print_success(message):
    """Print success message in green."""
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def print_info(message):
    """Print info message in blue."""
    print(f"{Fore.BLUE}ℹ️  {message}{Style.RESET_ALL}")


def print_warning(message):
    """Print warning message in yellow."""
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def ensure_dir_exists(directory):
    """Ensure directory exists, create if it doesn't."""
    os.makedirs(directory, exist_ok=True)


def get_home_config_dir():
    """Get the home config directory for amvka."""
    home = os.path.expanduser("~")
    config_dir = os.path.join(home, ".amvka")
    ensure_dir_exists(config_dir)
    return config_dir


def safe_input(prompt, default=None):
    """Safe input with default value."""
    try:
        value = input(prompt).strip()
        return value if value else default
    except (EOFError, KeyboardInterrupt):
        print_info("\nOperation cancelled.")
        sys.exit(1)