"""TOML configuration file loader."""

import toml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Union

from .base import ConfigLoader, LoadResult
from ..core.exceptions import FileNotFoundError, InvalidFormatError


class TomlLoader(ConfigLoader):
    """Loader for TOML configuration files."""

    def can_load(self, path: Union[str, Path]) -> bool:
        """Check if file is a TOML file."""
        path_obj = Path(path)
        return path_obj.suffix.lower() in self.get_supported_extensions()

    def load(self, path: Union[str, Path]) -> LoadResult:
        """
        Load TOML configuration file.

        Args:
            path: Path to TOML file

        Returns:
            LoadResult with parsed TOML data
        """
        path_obj = Path(path)
        load_time = datetime.now()
        errors = []
        warnings = []

        # Check if file exists
        file_size, exists = self._get_file_info(path_obj)
        if not exists:
            return LoadResult(
                success=False,
                data={},
                source_path=str(path_obj),
                load_time=load_time,
                file_size=file_size,
                errors=[f"File not found: {path_obj}"],
                warnings=warnings
            )

        try:
            # Load and parse TOML file
            with open(path_obj, 'r', encoding='utf-8') as f:
                data = toml.load(f)

            return LoadResult(
                success=True,
                data=data,
                source_path=str(path_obj),
                load_time=load_time,
                file_size=file_size,
                errors=errors,
                warnings=warnings
            )

        except toml.TomlDecodeError as e:
            errors.append(f"TOML parsing error: {e}")
            return LoadResult(
                success=False,
                data={},
                source_path=str(path_obj),
                load_time=load_time,
                file_size=file_size,
                errors=errors,
                warnings=warnings
            )

        except IOError as e:
            errors.append(f"File read error: {e}")
            return LoadResult(
                success=False,
                data={},
                source_path=str(path_obj),
                load_time=load_time,
                file_size=file_size,
                errors=errors,
                warnings=warnings
            )

        except Exception as e:
            errors.append(f"Unexpected error loading TOML: {e}")
            return LoadResult(
                success=False,
                data={},
                source_path=str(path_obj),
                load_time=load_time,
                file_size=file_size,
                errors=errors,
                warnings=warnings
            )

    def save(self, data: Dict[str, Any], path: Union[str, Path]) -> bool:
        """
        Save configuration data as TOML file.

        Args:
            data: Configuration data to save
            path: Path to save TOML file

        Returns:
            True if save was successful
        """
        path_obj = Path(path)

        try:
            # Create parent directories if they don't exist
            path_obj.parent.mkdir(parents=True, exist_ok=True)

            # Save as TOML
            with open(path_obj, 'w', encoding='utf-8') as f:
                toml.dump(data, f)

            return True

        except Exception as e:
            # In a real implementation, you might want to log this error
            return False

    def get_supported_extensions(self) -> list[str]:
        """Get supported TOML file extensions."""
        return ['.toml', '.tml']

    def format_toml(self, data: Dict[str, Any], sort_keys: bool = True) -> str:
        """
        Format data as TOML string.

        Args:
            data: Data to format as TOML
            sort_keys: Whether to sort keys

        Returns:
            Formatted TOML string
        """
        try:
            return toml.dumps(data, sort_keys=sort_keys)
        except Exception:
            return ""

    def validate_toml_syntax(self, content: str) -> tuple[bool, str]:
        """
        Validate TOML syntax without loading into memory.

        Args:
            content: TOML content string

        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            toml.loads(content)
            return True, ""
        except toml.TomlDecodeError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Unexpected error: {e}"