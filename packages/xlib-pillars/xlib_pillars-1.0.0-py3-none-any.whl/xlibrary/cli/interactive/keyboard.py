"""
Keyboard input handling for interactive CLI features.

Provides cross-platform keyboard input handling for menu navigation
and interactive features.
"""

import sys
import select
import termios
import tty
from enum import Enum
from typing import Optional, Callable, Dict, Any
from dataclasses import dataclass


class KeyType(Enum):
    """Types of keyboard input."""
    CHAR = "char"           # Regular character
    ARROW_UP = "arrow_up"
    ARROW_DOWN = "arrow_down"
    ARROW_LEFT = "arrow_left"
    ARROW_RIGHT = "arrow_right"
    ENTER = "enter"
    ESCAPE = "escape"
    BACKSPACE = "backspace"
    DELETE = "delete"
    TAB = "tab"
    SPACE = "space"
    CTRL_C = "ctrl_c"
    UNKNOWN = "unknown"


@dataclass
class KeyEvent:
    """Keyboard event information."""
    key_type: KeyType
    char: Optional[str] = None
    raw_bytes: Optional[bytes] = None
    modifiers: Optional[Dict[str, bool]] = None


class KeyboardHandler:
    """
    Cross-platform keyboard input handler for interactive CLI.

    Handles raw keyboard input including arrow keys, special keys,
    and character input for menu navigation.
    """

    # Key mappings for special sequences
    ESCAPE_SEQUENCES = {
        b'\x1b[A': KeyType.ARROW_UP,
        b'\x1b[B': KeyType.ARROW_DOWN,
        b'\x1b[C': KeyType.ARROW_RIGHT,
        b'\x1b[D': KeyType.ARROW_LEFT,
        b'\x1b[3~': KeyType.DELETE,
        b'\x1b': KeyType.ESCAPE,
    }

    CHAR_MAPPINGS = {
        b'\r': KeyType.ENTER,
        b'\n': KeyType.ENTER,
        b'\x7f': KeyType.BACKSPACE,  # DEL character (often backspace)
        b'\x08': KeyType.BACKSPACE,  # BS character
        b'\t': KeyType.TAB,
        b' ': KeyType.SPACE,
        b'\x03': KeyType.CTRL_C,
    }

    def __init__(self):
        """Initialize keyboard handler."""
        self._original_settings = None
        self._raw_mode_active = False

    def enable_raw_mode(self):
        """Enable raw keyboard input mode."""
        if sys.platform == "win32":
            # Windows implementation would go here
            # For now, we'll use basic input
            return

        if not sys.stdin.isatty():
            return

        try:
            self._original_settings = termios.tcgetattr(sys.stdin.fileno())
            tty.setraw(sys.stdin.fileno())
            self._raw_mode_active = True
        except (termios.error, OSError):
            # Fallback for environments without termios
            pass

    def disable_raw_mode(self):
        """Disable raw keyboard input mode."""
        if sys.platform == "win32":
            return

        if self._original_settings is not None:
            try:
                termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._original_settings)
                self._raw_mode_active = False
            except (termios.error, OSError):
                pass

    def read_key(self, timeout: Optional[float] = None) -> Optional[KeyEvent]:
        """
        Read a single key event.

        Args:
            timeout: Timeout in seconds (None for blocking)

        Returns:
            KeyEvent or None if timeout occurred
        """
        if not self._raw_mode_active:
            # Fallback to basic input
            return self._read_key_fallback(timeout)

        try:
            # Check if input is available
            if timeout is not None:
                ready, _, _ = select.select([sys.stdin], [], [], timeout)
                if not ready:
                    return None

            # Read first byte
            first_byte = sys.stdin.buffer.read(1)
            if not first_byte:
                return None

            # Handle escape sequences
            if first_byte == b'\x1b':
                return self._read_escape_sequence()

            # Handle regular characters
            return self._process_char(first_byte)

        except (OSError, IOError, KeyboardInterrupt):
            return KeyEvent(KeyType.CTRL_C)

    def _read_escape_sequence(self) -> KeyEvent:
        """Read and process escape sequence."""
        try:
            # Try to read more characters for escape sequence
            sequence = b'\x1b'

            # Read next character with short timeout
            ready, _, _ = select.select([sys.stdin], [], [], 0.1)
            if ready:
                next_char = sys.stdin.buffer.read(1)
                if next_char:
                    sequence += next_char

                    # For arrow keys, we need one more character
                    if next_char == b'[':
                        ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                        if ready:
                            third_char = sys.stdin.buffer.read(1)
                            if third_char:
                                sequence += third_char

                                # Some sequences have a 4th character
                                if third_char == b'3':
                                    ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                                    if ready:
                                        fourth_char = sys.stdin.buffer.read(1)
                                        if fourth_char:
                                            sequence += fourth_char

            # Look up the sequence
            key_type = self.ESCAPE_SEQUENCES.get(sequence, KeyType.UNKNOWN)

            return KeyEvent(
                key_type=key_type,
                raw_bytes=sequence
            )

        except (OSError, IOError):
            return KeyEvent(KeyType.ESCAPE, raw_bytes=b'\x1b')

    def _process_char(self, char_byte: bytes) -> KeyEvent:
        """Process regular character input."""
        # Check for special characters
        key_type = self.CHAR_MAPPINGS.get(char_byte)

        if key_type:
            return KeyEvent(key_type=key_type, raw_bytes=char_byte)

        # Regular character
        try:
            char = char_byte.decode('utf-8')
            return KeyEvent(
                key_type=KeyType.CHAR,
                char=char,
                raw_bytes=char_byte
            )
        except UnicodeDecodeError:
            return KeyEvent(
                key_type=KeyType.UNKNOWN,
                raw_bytes=char_byte
            )

    def _read_key_fallback(self, timeout: Optional[float] = None) -> Optional[KeyEvent]:
        """Fallback key reading for systems without raw mode."""
        try:
            if timeout is not None:
                # Simple timeout using select
                ready, _, _ = select.select([sys.stdin], [], [], timeout)
                if not ready:
                    return None

            char = sys.stdin.read(1)
            if not char:
                return None

            if char == '\n' or char == '\r':
                return KeyEvent(KeyType.ENTER, char=char)
            elif ord(char) == 3:  # Ctrl+C
                return KeyEvent(KeyType.CTRL_C, char=char)
            else:
                return KeyEvent(KeyType.CHAR, char=char)

        except KeyboardInterrupt:
            return KeyEvent(KeyType.CTRL_C)
        except (OSError, IOError):
            return None

    def wait_for_key(self, valid_keys: Optional[set] = None) -> Optional[KeyEvent]:
        """
        Wait for a specific key input.

        Args:
            valid_keys: Set of valid KeyType values or characters

        Returns:
            KeyEvent for valid key, or None if interrupted
        """
        while True:
            event = self.read_key()
            if not event:
                continue

            if event.key_type == KeyType.CTRL_C:
                return event

            if valid_keys is None:
                return event

            # Check if key is valid
            if (event.key_type in valid_keys or
                (event.char and event.char.lower() in valid_keys)):
                return event

    def __enter__(self):
        """Context manager entry."""
        self.enable_raw_mode()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disable_raw_mode()


# Convenience functions
def get_key(timeout: Optional[float] = None) -> Optional[KeyEvent]:
    """Get a single key press."""
    with KeyboardHandler() as handler:
        return handler.read_key(timeout)


def wait_for_enter():
    """Wait for Enter key press."""
    with KeyboardHandler() as handler:
        while True:
            event = handler.read_key()
            if event and event.key_type in (KeyType.ENTER, KeyType.CTRL_C):
                return event.key_type == KeyType.ENTER


def confirm(prompt: str = "Continue? (y/n): ") -> bool:
    """Get yes/no confirmation from user."""
    print(prompt, end="", flush=True)

    with KeyboardHandler() as handler:
        valid_keys = {'y', 'n', 'yes', 'no'}
        event = handler.wait_for_key(valid_keys)

        if event and event.char:
            response = event.char.lower()
            print(response)  # Echo the response
            return response in ('y', 'yes')

        return False


# Example usage
if __name__ == "__main__":
    print("Keyboard Handler Test")
    print("Press keys (ESC or Ctrl+C to exit):")

    with KeyboardHandler() as handler:
        while True:
            event = handler.read_key()
            if not event:
                continue

            if event.key_type in (KeyType.ESCAPE, KeyType.CTRL_C):
                print("\nExiting...")
                break

            if event.key_type == KeyType.CHAR:
                print(f"Character: '{event.char}'")
            else:
                print(f"Special key: {event.key_type.value}")

            if event.key_type == KeyType.ENTER:
                print("Enter pressed!")