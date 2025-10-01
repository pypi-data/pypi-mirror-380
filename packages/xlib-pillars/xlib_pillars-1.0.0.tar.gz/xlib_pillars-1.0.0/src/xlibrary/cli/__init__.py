"""
xlibrary.cli - Comprehensive CLI framework with rich terminal features

This module provides enterprise-grade command-line interface capabilities including:

Features:
- Docker-style multi-line progress bars with colors and ETA
- Interactive menu system with arrow key navigation
- Cisco-style command abbreviations (conf t → configure terminal)
- Rich formatted output with automatic fallbacks
- Live monitoring dashboards for long operations
- TUI-ready foundation for future interfaces

Core Components:
- CLIFramework: Main command-line interface system
- MenuSystem: Interactive navigation with keyboard shortcuts
- ProgressManager: Advanced progress tracking with multiple styles
- CommandRegistry: Smart command abbreviation resolution
- Dashboard: Live monitoring for system operations

Usage Examples:
    # Command-line with abbreviations
    xlibrary conf t           # configure terminal
    xlibrary m wat video.mp4  # media watermark video.mp4

    # Interactive menu system
    from xlibrary.cli import MenuSystem
    menu = MenuSystem()
    menu.show_main_menu()

    # Docker-style progress
    from xlibrary.cli import ProgressManager
    with ProgressManager.docker_style() as pm:
        task = pm.add_task("Processing...", total=100)
        pm.update(task, advance=10)
"""

from .core.framework import CLIFramework, CLICommand, CLIArgument, ArgumentType
from .core.commands import CommandRegistry, resolve_command
from .ui.progress import ProgressManager, ProgressStyle, DockerProgress
from .ui.menu import MenuSystem, MenuItem, MenuAction
from .ui.output import CLIOutput, OutputMode, Terminal
from .ui.dashboard import LiveDashboard, DashboardPanel
from .interactive.navigator import MenuNavigator, NavigationMode
from .interactive.keyboard import KeyboardHandler, KeyEvent

__version__ = "1.0.0"
__all__ = [
    # Core Framework
    "CLIFramework",
    "CLICommand",
    "CLIArgument",
    "ArgumentType",

    # Command System
    "CommandRegistry",
    "resolve_command",

    # Progress & UI
    "ProgressManager",
    "ProgressStyle",
    "DockerProgress",
    "CLIOutput",
    "OutputMode",
    "Terminal",

    # Interactive Menu
    "MenuSystem",
    "MenuItem",
    "MenuAction",
    "MenuNavigator",
    "NavigationMode",

    # Dashboard
    "LiveDashboard",
    "DashboardPanel",

    # Input Handling
    "KeyboardHandler",
    "KeyEvent",
]