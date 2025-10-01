"""Base configuration loader interface."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Optional, Union
from datetime import datetime


@dataclass
class LoadResult:
    """Result of configuration loading operation."""
    success: bool
    data: Dict[str, Any]
    source_path: Optional[str]
    load_time: datetime
    file_size: Optional[int]
    errors: list
    warnings: list


class ConfigLoader(ABC):
    """Abstract base class for configuration loaders."""

    @abstractmethod
    def can_load(self, path: Union[str, Path]) -> bool:
        """
        Check if this loader can handle the given file.

        Args:
            path: Path to configuration file

        Returns:
            True if this loader can handle the file
        """
        pass

    @abstractmethod
    def load(self, path: Union[str, Path]) -> LoadResult:
        """
        Load configuration from file.

        Args:
            path: Path to configuration file

        Returns:
            LoadResult with configuration data and metadata
        """
        pass

    @abstractmethod
    def save(self, data: Dict[str, Any], path: Union[str, Path]) -> bool:
        """
        Save configuration to file.

        Args:
            data: Configuration data to save
            path: Path to save configuration file

        Returns:
            True if save was successful
        """
        pass

    @abstractmethod
    def get_supported_extensions(self) -> list[str]:
        """
        Get list of file extensions this loader supports.

        Returns:
            List of file extensions (with dots, e.g., ['.toml', '.tml'])
        """
        pass

    def _get_file_info(self, path: Union[str, Path]) -> tuple[Optional[int], bool]:
        """
        Get file information.

        Args:
            path: Path to file

        Returns:
            Tuple of (file_size, exists)
        """
        path_obj = Path(path)
        if path_obj.exists() and path_obj.is_file():
            return path_obj.stat().st_size, True
        return None, False