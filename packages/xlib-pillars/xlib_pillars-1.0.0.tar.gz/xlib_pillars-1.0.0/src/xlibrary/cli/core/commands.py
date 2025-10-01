"""
Cisco-style command abbreviation system.

Provides smart command resolution similar to Cisco routers where 'conf t'
resolves to 'configure terminal' based on unique prefixes.
"""

from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass
from enum import Enum


class CommandCategory(Enum):
    """Command categories for organization."""
    MAIN = "main"
    MEDIA = "media"
    ENCRYPTION = "encryption"
    AI = "ai"
    CONFIG = "config"
    TOOLS = "tools"


@dataclass
class CommandDefinition:
    """Definition of a CLI command with abbreviations."""
    name: str
    category: CommandCategory
    description: str
    aliases: List[str]
    min_chars: int = 1  # Minimum characters needed for abbreviation
    subcommands: Optional[Dict[str, 'CommandDefinition']] = None


class CommandRegistry:
    """
    Registry for CLI commands with smart abbreviation resolution.

    Supports Cisco-style command abbreviation where commands are resolved
    by unique prefixes. For example:
    - 'conf' → 'configure' (if unique)
    - 'config' → 'configure'
    - 'conf t' → 'configure terminal'
    """

    def __init__(self):
        """Initialize command registry."""
        self._commands: Dict[str, CommandDefinition] = {}
        self._setup_default_commands()

    def _setup_default_commands(self):
        """Setup default xlibrary commands."""

        # Main commands
        self.register(CommandDefinition(
            name="configure",
            category=CommandCategory.MAIN,
            description="Configure xlibrary settings",
            aliases=["conf", "config", "configure"],
            min_chars=4,
            subcommands={
                "terminal": CommandDefinition(
                    name="terminal",
                    category=CommandCategory.MAIN,
                    description="Configure terminal settings",
                    aliases=["t", "term", "terminal"],
                    min_chars=1
                )
            }
        ))

        # Media commands
        self.register(CommandDefinition(
            name="media",
            category=CommandCategory.MEDIA,
            description="Media processing operations",
            aliases=["m", "med", "media"],
            min_chars=1,
            subcommands={
                "watermark": CommandDefinition(
                    name="watermark",
                    category=CommandCategory.MEDIA,
                    description="Add watermarks to media files",
                    aliases=["w", "wat", "water", "watermark"],
                    min_chars=1
                ),
                "trim": CommandDefinition(
                    name="trim",
                    category=CommandCategory.MEDIA,
                    description="Trim video files",
                    aliases=["t", "tr", "trim"],
                    min_chars=2  # Avoid conflict with 'terminal'
                ),
                "convert": CommandDefinition(
                    name="convert",
                    category=CommandCategory.MEDIA,
                    description="Convert media formats",
                    aliases=["c", "conv", "convert"],
                    min_chars=1
                )
            }
        ))

        # Encryption commands
        self.register(CommandDefinition(
            name="encryption",
            category=CommandCategory.ENCRYPTION,
            description="Encryption and security operations",
            aliases=["e", "enc", "encrypt", "encryption"],
            min_chars=1,
            subcommands={
                "encrypt": CommandDefinition(
                    name="encrypt",
                    category=CommandCategory.ENCRYPTION,
                    description="Encrypt files or strings",
                    aliases=["e", "enc", "encrypt"],
                    min_chars=3  # Avoid conflict with parent
                ),
                "decrypt": CommandDefinition(
                    name="decrypt",
                    category=CommandCategory.ENCRYPTION,
                    description="Decrypt files or strings",
                    aliases=["d", "dec", "decrypt"],
                    min_chars=1
                ),
                "generate": CommandDefinition(
                    name="generate",
                    category=CommandCategory.ENCRYPTION,
                    description="Generate keys and certificates",
                    aliases=["g", "gen", "generate"],
                    min_chars=1
                )
            }
        ))

        # AI commands
        self.register(CommandDefinition(
            name="ai",
            category=CommandCategory.AI,
            description="AI and LLM operations",
            aliases=["ai", "llm"],
            min_chars=2,
            subcommands={
                "chat": CommandDefinition(
                    name="chat",
                    category=CommandCategory.AI,
                    description="Interactive AI chat session",
                    aliases=["c", "chat"],
                    min_chars=1
                ),
                "stream": CommandDefinition(
                    name="stream",
                    category=CommandCategory.AI,
                    description="Streaming AI responses",
                    aliases=["s", "str", "stream"],
                    min_chars=1
                )
            }
        ))

    def register(self, command: CommandDefinition):
        """Register a command definition."""
        self._commands[command.name] = command

    def resolve_command(self, input_args: List[str]) -> Tuple[Optional[List[str]], List[str]]:
        """
        Resolve command abbreviations to full commands.

        Args:
            input_args: List of command arguments

        Returns:
            Tuple of (resolved_command_path, remaining_args)
            Returns (None, original_args) if resolution fails
        """
        if not input_args:
            return None, input_args

        resolved_path = []
        current_commands = self._commands
        remaining_args = input_args.copy()

        while remaining_args and isinstance(current_commands, dict):
            arg = remaining_args[0]

            # Try exact match first
            exact_match = None
            for cmd_name, cmd_def in current_commands.items():
                if cmd_name == arg or arg in cmd_def.aliases:
                    exact_match = cmd_def
                    break

            if exact_match:
                resolved_path.append(exact_match.name)
                remaining_args = remaining_args[1:]
                current_commands = exact_match.subcommands or {}
                continue

            # Try abbreviation matching
            matches = self._find_abbreviation_matches(arg, current_commands)

            if len(matches) == 1:
                # Unique match found
                cmd_def = matches[0]
                resolved_path.append(cmd_def.name)
                remaining_args = remaining_args[1:]
                current_commands = cmd_def.subcommands or {}
            elif len(matches) > 1:
                # Ambiguous abbreviation
                return None, input_args
            else:
                # No matches - remaining args are parameters
                break

        return resolved_path if resolved_path else None, remaining_args

    def _find_abbreviation_matches(self, abbrev: str, commands: Dict[str, CommandDefinition]) -> List[CommandDefinition]:
        """Find commands that match the given abbreviation."""
        matches = []

        for cmd_name, cmd_def in commands.items():
            # Check if abbreviation is a valid prefix
            if (len(abbrev) >= cmd_def.min_chars and
                cmd_name.startswith(abbrev)):
                matches.append(cmd_def)
            else:
                # Check aliases
                for alias in cmd_def.aliases:
                    if (len(abbrev) >= cmd_def.min_chars and
                        alias.startswith(abbrev) and alias != abbrev):
                        matches.append(cmd_def)
                        break

        return matches

    def get_suggestions(self, partial_command: str, category: Optional[CommandCategory] = None) -> List[str]:
        """Get command suggestions for partial input."""
        suggestions = []

        for cmd_name, cmd_def in self._commands.items():
            if category and cmd_def.category != category:
                continue

            if cmd_name.startswith(partial_command):
                suggestions.append(cmd_name)

            # Check aliases
            for alias in cmd_def.aliases:
                if alias.startswith(partial_command) and alias not in suggestions:
                    suggestions.append(f"{alias} → {cmd_name}")

        return sorted(suggestions)

    def get_command_help(self, command_path: List[str]) -> Optional[str]:
        """Get help text for a command path."""
        current_commands = self._commands

        for cmd_name in command_path:
            if cmd_name in current_commands:
                cmd_def = current_commands[cmd_name]
                if len(command_path) == 1:
                    # Return help for this command
                    help_text = f"{cmd_def.name}: {cmd_def.description}\n"
                    help_text += f"Aliases: {', '.join(cmd_def.aliases)}\n"

                    if cmd_def.subcommands:
                        help_text += "\nSubcommands:\n"
                        for sub_name, sub_def in cmd_def.subcommands.items():
                            help_text += f"  {sub_name}: {sub_def.description}\n"

                    return help_text
                else:
                    # Continue to subcommand
                    current_commands = cmd_def.subcommands or {}
                    command_path = command_path[1:]
            else:
                return None

        return None

    def list_commands(self, category: Optional[CommandCategory] = None) -> Dict[str, CommandDefinition]:
        """List all commands, optionally filtered by category."""
        if category is None:
            return self._commands.copy()

        return {
            name: cmd_def for name, cmd_def in self._commands.items()
            if cmd_def.category == category
        }


# Global command registry instance
_command_registry = CommandRegistry()


def resolve_command(args: List[str]) -> Tuple[Optional[List[str]], List[str]]:
    """
    Convenience function to resolve command abbreviations.

    Args:
        args: Command arguments to resolve

    Returns:
        Tuple of (resolved_command_path, remaining_args)
    """
    return _command_registry.resolve_command(args)


def get_suggestions(partial: str, category: Optional[CommandCategory] = None) -> List[str]:
    """Get command suggestions for partial input."""
    return _command_registry.get_suggestions(partial, category)


def get_command_help(command_path: List[str]) -> Optional[str]:
    """Get help text for a command."""
    return _command_registry.get_command_help(command_path)


# Example usage and testing
if __name__ == "__main__":
    # Test command resolution
    test_cases = [
        ["conf", "t"],           # → ["configure", "terminal"]
        ["m", "wat", "video.mp4"], # → ["media", "watermark"]
        ["e", "enc", "file.txt"], # → ["encryption", "encrypt"]
        ["ai", "c"],             # → ["ai", "chat"]
        ["config"],              # → ["configure"]
    ]

    registry = CommandRegistry()

    for test_args in test_cases:
        resolved, remaining = registry.resolve_command(test_args)
        print(f"Input: {test_args}")
        print(f"Resolved: {resolved}")
        print(f"Remaining: {remaining}")
        print("---")