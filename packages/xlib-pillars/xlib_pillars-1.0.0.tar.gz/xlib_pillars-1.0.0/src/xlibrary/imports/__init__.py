"""
xlibrary.imports - Advanced file import management system

This module provides enterprise-grade file import capabilities including:

Core Features:
- Watch folder scanning with regex pattern matching
- Provider/version-based file classification
- MD5+filesize duplicate detection and prevention
- UUID-based filename generation for conflict avoidance
- JSON index tracking with processing status management
- Full rollback capability for testing and development
- Comprehensive import management and status reporting

Usage Examples:
    from xlibrary.imports import ImportManager, ImportConfig

    config = ImportConfig(
        watch_folder="/watch",
        output_folder="/output",
        index_file="imports.json"
    )

    manager = ImportManager(config)

    # Scan for new files
    results = manager.scan_watch_folder()

    # Process imports
    results = manager.process_pending_imports()
"""

from .core.manager import ImportManager
from .core.types import (
    ImportConfig,
    ImportPattern,
    ImportEntry,
    ImportIndex,
    ImportStats,
    ProcessingResult,
    WatchFolderConfig,
    FileStatus,
    ImportOperationResult,
    ImportManagerError,
    ImportPatternError,
    ImportIndexError,
    ImportDuplicateError,
    PathLike,
    ImportCallback,
    ProgressCallback
)

__version__ = "1.0.0"
__all__ = [
    # Main class
    "ImportManager",

    # Configuration
    "ImportConfig",
    "WatchFolderConfig",
    "ImportPattern",

    # Data types
    "ImportEntry",
    "ImportIndex",
    "ImportStats",
    "ProcessingResult",

    # Enums
    "FileStatus",
    "ImportOperationResult",

    # Type aliases
    "PathLike",
    "ImportCallback",
    "ProgressCallback",

    # Exceptions
    "ImportManagerError",
    "ImportPatternError",
    "ImportIndexError",
    "ImportDuplicateError"
]