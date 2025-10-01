"""
Type definitions for file operations.
"""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional, Dict, Any, Union, List, Callable
from datetime import datetime


# Type aliases
PathLike = Union[str, Path]
ProgressCallback = Callable[[int, int, str], None]  # (current, total, message)
FileFilter = Callable[['FileInfo'], bool]


class FileOperationResult(Enum):
    """Results of file operations."""
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"
    EXISTS = "exists"


class FileType(Enum):
    """Broad categories of file types."""
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    ARCHIVE = "archive"
    EXECUTABLE = "executable"
    BINARY = "binary"
    UNKNOWN = "unknown"


class CompressionFormat(Enum):
    """Supported compression formats."""
    ZIP = "zip"
    TAR = "tar"
    TAR_GZ = "tar.gz"
    TAR_BZ2 = "tar.bz2"
    TAR_XZ = "tar.xz"


@dataclass
class FileInfo:
    """Comprehensive file information."""
    path: Path
    name: str
    extension: str
    size: int
    modified_time: datetime
    created_time: datetime
    is_hidden: bool
    is_readable: bool
    is_writable: bool
    is_executable: bool
    permissions: str
    declared_type: str
    actual_type: str
    mime_type: str
    file_type: FileType
    is_type_mismatch: bool
    hash_md5: Optional[str] = None
    hash_sha256: Optional[str] = None


@dataclass
class DuplicateGroup:
    """Group of duplicate files."""
    hash_key: str
    size: int
    files: List[FileInfo] = field(default_factory=list)

    @property
    def total_size(self) -> int:
        """Total size of all files in group."""
        return len(self.files) * self.size

    @property
    def wasted_space(self) -> int:
        """Space wasted by duplicates (total - one original)."""
        return max(0, self.total_size - self.size)


@dataclass
class FolderStats:
    """Statistics about a folder."""
    path: Path
    total_files: int = 0
    total_directories: int = 0
    total_size: int = 0
    file_type_counts: Dict[FileType, int] = field(default_factory=dict)
    extension_counts: Dict[str, int] = field(default_factory=dict)
    hidden_files_count: int = 0
    empty_files_count: int = 0
    large_files_count: int = 0
    old_files_count: int = 0
    largest_files: List[FileInfo] = field(default_factory=list)
    smallest_files: List[FileInfo] = field(default_factory=list)
    newest_files: List[FileInfo] = field(default_factory=list)
    oldest_files: List[FileInfo] = field(default_factory=list)
    duplicate_groups: List[DuplicateGroup] = field(default_factory=list)
    duplicate_files_count: int = 0
    duplicate_size_wasted: int = 0
    type_mismatches: List[FileInfo] = field(default_factory=list)

    def add_file(self, file_info: FileInfo):
        """Add a file to the statistics."""
        self.total_files += 1
        self.total_size += file_info.size

        # Count by type
        if file_info.file_type in self.file_type_counts:
            self.file_type_counts[file_info.file_type] += 1
        else:
            self.file_type_counts[file_info.file_type] = 1

        # Count by extension
        ext = file_info.extension or 'no_extension'
        if ext in self.extension_counts:
            self.extension_counts[ext] += 1
        else:
            self.extension_counts[ext] = 1

        # Special categories
        if file_info.is_hidden:
            self.hidden_files_count += 1

        if file_info.size == 0:
            self.empty_files_count += 1

        if file_info.size > 100 * 1024 * 1024:  # 100MB
            self.large_files_count += 1

        # Check age (older than 365 days)
        age_days = (datetime.now() - file_info.modified_time).days
        if age_days > 365:
            self.old_files_count += 1

        if file_info.is_type_mismatch:
            self.type_mismatches.append(file_info)


@dataclass
class BatchOperation:
    """Configuration for batch file operations."""
    operation: str  # 'copy', 'move', 'delete', 'analyze'
    source_pattern: str  # glob pattern for source files
    target_directory: Optional[Path] = None
    recursive: bool = True
    include_hidden: bool = False
    overwrite: bool = False
    dry_run: bool = False
    min_size: int = 0
    max_size: Optional[int] = None
    include_extensions: Optional[List[str]] = None
    exclude_extensions: Optional[List[str]] = None
    progress_callback: Optional[ProgressCallback] = None


@dataclass
class ProcessingResult:
    """Result of batch processing operation."""
    success: bool
    operation: str
    files_processed: int = 0
    files_failed: int = 0
    files_skipped: int = 0
    bytes_processed: int = 0
    processing_time: float = 0.0
    source_path: Optional[Path] = None
    target_path: Optional[Path] = None
    details: Dict[str, Any] = field(default_factory=dict)
    file_results: Dict[str, FileOperationResult] = field(default_factory=dict)

    def add_file_result(self, file_path: Path, result: FileOperationResult, message: str = ""):
        """Add result for a specific file."""
        self.file_results[str(file_path)] = result

        if result == FileOperationResult.SUCCESS:
            self.files_processed += 1
        elif result == FileOperationResult.FAILED:
            self.files_failed += 1
        elif result == FileOperationResult.SKIPPED:
            self.files_skipped += 1

        if message:
            if 'messages' not in self.details:
                self.details['messages'] = []
            self.details['messages'].append(f"{file_path}: {message}")


# Exceptions
class FileManagerError(Exception):
    """Base exception for file manager operations."""
    pass


class CompressionError(FileManagerError):
    """Exception raised during compression/extraction operations."""
    pass