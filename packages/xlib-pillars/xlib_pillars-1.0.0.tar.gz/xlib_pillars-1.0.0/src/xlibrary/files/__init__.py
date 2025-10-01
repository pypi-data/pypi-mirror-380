"""
xlibrary.files - Comprehensive file and directory management

This module provides enterprise-grade file management capabilities including:

Core Features:
- Advanced file type detection and analysis
- Folder structure management and cleanup
- File organization by extension or custom rules
- Compression and extraction utilities (ZIP, TAR, etc.)
- Deduplication with multiple verification methods
- Batch operations with progress tracking
- Empty folder cleanup and management

Folder Operations:
- Flatten folder structures (collapse all subfolders)
- Organize files by extension into subfolders
- Remove empty folders and directories
- Clear folder contents (including hidden files)
- Compress and decompress folders

Key Features:
- Hidden file support with configurable inclusion
- Progress callbacks for long operations
- Dry-run mode for safe testing
- Comprehensive error handling and logging
- Magic number detection for file type verification

Usage Examples:
    from xlibrary.files import FileManager

    fm = FileManager()

    # Flatten folder structure
    result = fm.collapse_folders("/path/to/folder")

    # Organize by file type
    result = fm.organize_by_file_type("/path/to/messy/folder")

    # Compress folder
    result = fm.compress_folder("/source", "/archive.zip")

    # Remove empty folders
    result = fm.remove_empty_folders("/path/to/clean")

    # Clear folder contents
    result = fm.clear_folder_contents("/path/to/empty")
"""

from .core.manager import FileManager
from .core.types import (
    FileInfo,
    FileOperationResult,
    FileType,
    FolderStats,
    CompressionFormat,
    FileFilter,
    ProgressCallback,
    PathLike,
    FileManagerError,
    CompressionError,
    BatchOperation,
    ProcessingResult
)

__version__ = "1.0.0"
__all__ = [
    # Main class
    "FileManager",

    # Data types
    "FileInfo",
    "FolderStats",
    "BatchOperation",
    "ProcessingResult",

    # Enums
    "FileOperationResult",
    "FileType",
    "CompressionFormat",

    # Type aliases
    "FileFilter",
    "ProgressCallback",
    "PathLike",

    # Exceptions
    "FileManagerError",
    "CompressionError"
]