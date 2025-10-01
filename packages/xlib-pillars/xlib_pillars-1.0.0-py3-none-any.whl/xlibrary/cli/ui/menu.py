"""
Interactive menu system with arrow key navigation and letter shortcuts.

Provides console-based interactive menus similar to text user interfaces
with support for navigation, submenus, and keyboard shortcuts.
"""

import sys
import os
from enum import Enum
from typing import List, Optional, Callable, Dict, Any, Union, Tuple
from dataclasses import dataclass, field
from pathlib import Path

from ..interactive.keyboard import KeyboardHandler, KeyEvent, KeyType

# Optional Rich import for enhanced display
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class MenuAction(Enum):
    """Types of menu actions."""
    FUNCTION = "function"     # Execute a function
    SUBMENU = "submenu"      # Navigate to submenu
    BACK = "back"            # Go back to parent menu
    EXIT = "exit"            # Exit application
    SHELL = "shell"          # Execute shell command


@dataclass
class MenuItem:
    """Individual menu item definition."""
    key: str                                    # Keyboard shortcut (single letter)
    label: str                                  # Display text
    action: MenuAction                          # Action type
    description: str = ""                       # Optional description
    target: Optional[Union[Callable, 'MenuSystem', str]] = None  # Action target
    enabled: bool = True                        # Whether item is enabled
    metadata: Dict[str, Any] = field(default_factory=dict)       # Additional data

    def __post_init__(self):
        """Validate menu item after initialization."""
        if self.action == MenuAction.FUNCTION and not callable(self.target):
            if self.target is not None:
                raise ValueError(f"Function action requires callable target, got {type(self.target)}")

        if self.action == MenuAction.SUBMENU and not isinstance(self.target, MenuSystem):
            if self.target is not None:
                raise ValueError(f"Submenu action requires MenuSystem target, got {type(self.target)}")


class MenuSystem:
    """
    Interactive menu system with keyboard navigation.

    Features:
    - Arrow key navigation (up/down)
    - Letter shortcuts for quick access
    - Submenus and navigation breadcrumbs
    - Rich formatting with fallback to plain text
    - Customizable styling and layout
    """

    def __init__(
        self,
        title: str,
        items: Optional[List[MenuItem]] = None,
        console: Optional[Console] = None,
        parent: Optional['MenuSystem'] = None,
        auto_width: bool = True,
        show_shortcuts: bool = True,
        show_descriptions: bool = True
    ):
        """
        Initialize menu system.

        Args:
            title: Menu title
            items: List of menu items
            console: Rich console (created if None)
            parent: Parent menu for navigation
            auto_width: Auto-size menu width
            show_shortcuts: Show keyboard shortcuts
            show_descriptions: Show item descriptions
        """
        self.title = title
        self.items = items or []
        self.parent = parent
        self.auto_width = auto_width
        self.show_shortcuts = show_shortcuts
        self.show_descriptions = show_descriptions

        # Display settings
        self.use_rich = RICH_AVAILABLE
        if self.use_rich and console is None:
            console = Console()
        self.console = console

        # Navigation state
        self.selected_index = 0
        self.running = False
        self._item_map: Dict[str, int] = {}  # Key -> index mapping

        # Build key mapping
        self._build_key_map()

    def _build_key_map(self):
        """Build keyboard shortcut mapping."""
        self._item_map.clear()
        for i, item in enumerate(self.items):
            if item.key:
                self._item_map[item.key.lower()] = i

    def add_item(self, item: MenuItem) -> 'MenuSystem':
        """Add menu item and return self for chaining."""
        self.items.append(item)
        self._build_key_map()
        return self

    def add_function_item(
        self,
        key: str,
        label: str,
        function: Callable,
        description: str = ""
    ) -> 'MenuSystem':
        """Add function menu item."""
        item = MenuItem(
            key=key,
            label=label,
            action=MenuAction.FUNCTION,
            target=function,
            description=description
        )
        return self.add_item(item)

    def add_submenu_item(
        self,
        key: str,
        label: str,
        submenu: 'MenuSystem',
        description: str = ""
    ) -> 'MenuSystem':
        """Add submenu item."""
        submenu.parent = self
        item = MenuItem(
            key=key,
            label=label,
            action=MenuAction.SUBMENU,
            target=submenu,
            description=description
        )
        return self.add_item(item)

    def add_separator(self) -> 'MenuSystem':
        """Add visual separator."""
        item = MenuItem(
            key="",
            label="─" * 40,
            action=MenuAction.FUNCTION,
            target=lambda: None,
            enabled=False
        )
        return self.add_item(item)

    def add_exit_item(self, key: str = "q", label: str = "Quit") -> 'MenuSystem':
        """Add exit menu item."""
        item = MenuItem(
            key=key,
            label=label,
            action=MenuAction.EXIT,
            description="Exit the application"
        )
        return self.add_item(item)

    def add_back_item(self, key: str = "b", label: str = "Back") -> 'MenuSystem':
        """Add back navigation item."""
        if self.parent:
            item = MenuItem(
                key=key,
                label=label,
                action=MenuAction.BACK,
                description="Return to previous menu"
            )
            return self.add_item(item)
        return self

    def show(self) -> bool:
        """
        Display and run the menu.

        Returns:
            True if menu should continue, False to exit
        """
        self.running = True

        with KeyboardHandler() as keyboard:
            while self.running:
                # Clear screen and display menu
                self._display_menu()

                # Get user input
                event = keyboard.read_key()
                if not event:
                    continue

                # Handle input
                result = self._handle_input(event)
                if result is False:
                    return False  # Exit requested

        return True

    def _display_menu(self):
        """Display the menu interface."""
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')

        if self.use_rich:
            self._display_rich_menu()
        else:
            self._display_basic_menu()

    def _display_rich_menu(self):
        """Display menu using Rich formatting."""
        # Create menu table
        table = Table(show_header=False, show_lines=False, pad_edge=False)
        table.add_column("Key", style="cyan", width=4)
        table.add_column("Item", style="white")

        if self.show_descriptions:
            table.add_column("Description", style="dim")

        # Add breadcrumb navigation
        breadcrumb = self._get_breadcrumb()
        if breadcrumb:
            self.console.print(f"📍 {breadcrumb}", style="dim")
            self.console.print()

        # Add menu items
        for i, item in enumerate(self.items):
            if not item.enabled:
                # Separator or disabled item
                if item.label.startswith("─"):
                    table.add_row("", item.label)
                else:
                    table.add_row(item.key, f"[dim]{item.label}[/dim]")
                continue

            # Highlight selected item
            key_style = "cyan bold" if i == self.selected_index else "cyan"
            label_style = "white bold" if i == self.selected_index else "white"

            # Selection indicator
            indicator = "→ " if i == self.selected_index else "  "

            key_text = f"[{item.key.upper()}]" if item.key else ""
            label_text = f"{indicator}{item.label}"

            if self.show_descriptions and item.description:
                table.add_row(
                    f"[{key_style}]{key_text}[/{key_style}]",
                    f"[{label_style}]{label_text}[/{label_style}]",
                    f"[dim]{item.description}[/dim]"
                )
            else:
                table.add_row(
                    f"[{key_style}]{key_text}[/{key_style}]",
                    f"[{label_style}]{label_text}[/{label_style}]"
                )

        # Wrap in panel
        panel = Panel(
            table,
            title=f"🎛️ {self.title}",
            border_style="blue",
            title_align="left"
        )

        self.console.print(panel)

        # Instructions
        instructions = []
        if any(item.enabled for item in self.items):
            instructions.append("[cyan]↑↓[/cyan] Navigate")
            instructions.append("[cyan]Enter[/cyan] Select")
            instructions.append("[cyan]Letter[/cyan] Quick access")

        if self.parent:
            instructions.append("[cyan]Esc[/cyan] Back")

        instructions.append("[cyan]Ctrl+C[/cyan] Exit")

        instruction_text = " • ".join(instructions)
        self.console.print(f"\n{instruction_text}", style="dim")

    def _display_basic_menu(self):
        """Display menu using basic text formatting."""
        # Title and breadcrumb
        breadcrumb = self._get_breadcrumb()
        if breadcrumb:
            print(f"📍 {breadcrumb}")
            print()

        print(f"🎛️ {self.title}")
        print("=" * (len(self.title) + 4))
        print()

        # Menu items
        for i, item in enumerate(self.items):
            if not item.enabled:
                if item.label.startswith("─"):
                    print(f"   {item.label}")
                else:
                    print(f"   {item.label} (disabled)")
                continue

            # Selection indicator
            indicator = "→ " if i == self.selected_index else "  "

            # Format item
            key_part = f"[{item.key.upper()}]" if item.key else "   "
            label_part = f"{indicator}{item.label}"

            if self.show_descriptions and item.description:
                print(f" {key_part} {label_part:<30} {item.description}")
            else:
                print(f" {key_part} {label_part}")

        # Instructions
        print("\n" + "─" * 50)
        instructions = ["↑↓ Navigate", "Enter Select", "Letter Quick access"]

        if self.parent:
            instructions.append("Esc Back")

        instructions.append("Ctrl+C Exit")
        print("💡 " + " • ".join(instructions))

    def _get_breadcrumb(self) -> str:
        """Get navigation breadcrumb trail."""
        breadcrumbs = []
        current = self

        while current:
            breadcrumbs.insert(0, current.title)
            current = current.parent

        return " → ".join(breadcrumbs) if len(breadcrumbs) > 1 else ""

    def _handle_input(self, event: KeyEvent) -> Optional[bool]:
        """
        Handle keyboard input.

        Returns:
            None to continue, False to exit, True for handled
        """
        # Exit on Ctrl+C
        if event.key_type == KeyType.CTRL_C:
            return False

        # Navigation
        if event.key_type == KeyType.ARROW_UP:
            self._navigate(-1)
            return True

        if event.key_type == KeyType.ARROW_DOWN:
            self._navigate(1)
            return True

        # Selection
        if event.key_type == KeyType.ENTER:
            return self._execute_selected()

        # Back navigation
        if event.key_type == KeyType.ESCAPE and self.parent:
            self.running = False
            return True

        # Letter shortcuts
        if event.key_type == KeyType.CHAR and event.char:
            char = event.char.lower()
            if char in self._item_map:
                index = self._item_map[char]
                self.selected_index = index
                return self._execute_selected()

        return True

    def _navigate(self, direction: int):
        """Navigate menu selection."""
        enabled_indices = [
            i for i, item in enumerate(self.items)
            if item.enabled
        ]

        if not enabled_indices:
            return

        # Find current position in enabled items
        try:
            current_pos = enabled_indices.index(self.selected_index)
        except ValueError:
            # Current selection is not enabled, go to first enabled
            self.selected_index = enabled_indices[0]
            return

        # Move to next/previous enabled item
        new_pos = (current_pos + direction) % len(enabled_indices)
        self.selected_index = enabled_indices[new_pos]

    def _execute_selected(self) -> Optional[bool]:
        """Execute the currently selected menu item."""
        if not (0 <= self.selected_index < len(self.items)):
            return True

        item = self.items[self.selected_index]
        if not item.enabled:
            return True

        try:
            if item.action == MenuAction.FUNCTION:
                if item.target:
                    result = item.target()
                    if result is False:
                        return False  # Function requested exit

            elif item.action == MenuAction.SUBMENU:
                if item.target:
                    # Show submenu
                    result = item.target.show()
                    if result is False:
                        return False  # Submenu requested exit

            elif item.action == MenuAction.BACK:
                self.running = False

            elif item.action == MenuAction.EXIT:
                return False

            elif item.action == MenuAction.SHELL:
                if item.target:
                    os.system(str(item.target))
                    input("\nPress Enter to continue...")

        except Exception as e:
            if self.use_rich:
                self.console.print(f"\n[red]Error: {e}[/red]")
            else:
                print(f"\nError: {e}")

            input("Press Enter to continue...")

        return True


# Convenience functions for common menu patterns
def create_main_menu() -> MenuSystem:
    """Create main xlibrary menu."""
    menu = MenuSystem("xlibrary Main Menu")

    # Add pillar menus
    menu.add_function_item("m", "Media Processing", lambda: media_menu().show(), "Video and image processing")
    menu.add_function_item("e", "Encryption & Security", lambda: encryption_menu().show(), "Encryption and cryptographic operations")
    menu.add_function_item("a", "AI & LLM Integration", lambda: ai_menu().show(), "AI provider management and chat")
    menu.add_function_item("c", "Configuration", lambda: config_menu().show(), "System configuration and settings")
    menu.add_function_item("t", "Tools & Utilities", lambda: tools_menu().show(), "Additional tools and utilities")

    menu.add_separator()
    menu.add_exit_item()

    return menu


def media_menu() -> MenuSystem:
    """Create media processing menu."""
    menu = MenuSystem("Media Processing")

    menu.add_function_item("w", "Watermark Videos", lambda: print("Watermark feature coming soon!"), "Add watermarks to video files")
    menu.add_function_item("t", "Trim Videos", lambda: print("Trim feature coming soon!"), "Cut video segments with precise timing")
    menu.add_function_item("c", "Convert Formats", lambda: print("Convert feature coming soon!"), "Convert between video/image formats")
    menu.add_function_item("b", "Batch Operations", lambda: print("Batch processing coming soon!"), "Process multiple files at once")

    menu.add_separator()
    menu.add_back_item()

    return menu


def encryption_menu() -> MenuSystem:
    """Create encryption menu."""
    menu = MenuSystem("Encryption & Security")

    menu.add_function_item("e", "Encrypt Files", lambda: print("Encryption coming soon!"), "Encrypt files and folders")
    menu.add_function_item("d", "Decrypt Files", lambda: print("Decryption coming soon!"), "Decrypt encrypted files")
    menu.add_function_item("g", "Generate Keys", lambda: print("Key generation coming soon!"), "Generate encryption keys and certificates")
    menu.add_function_item("h", "Hash Files", lambda: print("Hashing coming soon!"), "Generate secure hashes")

    menu.add_separator()
    menu.add_back_item()

    return menu


def ai_menu() -> MenuSystem:
    """Create AI menu."""
    menu = MenuSystem("AI & LLM Integration")

    menu.add_function_item("c", "Chat Session", lambda: print("AI chat coming soon!"), "Interactive AI conversation")
    menu.add_function_item("s", "Stream Responses", lambda: print("Streaming coming soon!"), "Real-time AI responses")
    menu.add_function_item("p", "Provider Settings", lambda: print("Provider config coming soon!"), "Configure AI providers")

    menu.add_separator()
    menu.add_back_item()

    return menu


def config_menu() -> MenuSystem:
    """Create configuration menu."""
    menu = MenuSystem("Configuration")

    menu.add_function_item("v", "View Settings", lambda: print("View config coming soon!"), "Display current configuration")
    menu.add_function_item("e", "Edit Settings", lambda: print("Edit config coming soon!"), "Modify configuration values")
    menu.add_function_item("r", "Reset to Defaults", lambda: print("Reset coming soon!"), "Reset all settings to defaults")

    menu.add_separator()
    menu.add_back_item()

    return menu


def tools_menu() -> MenuSystem:
    """Create tools menu."""
    menu = MenuSystem("Tools & Utilities")

    menu.add_function_item("s", "System Info", lambda: print("System info coming soon!"), "Display system information")
    menu.add_function_item("l", "Logs Viewer", lambda: print("Log viewer coming soon!"), "View application logs")
    menu.add_function_item("t", "Run Tests", lambda: print("Tests coming soon!"), "Run system diagnostics")

    menu.add_separator()
    menu.add_back_item()

    return menu


# Example usage
if __name__ == "__main__":
    try:
        main_menu = create_main_menu()
        main_menu.show()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")