"""
Type definitions for xlibrary.imports module.
"""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional, List, Dict, Any, Union, Callable
from datetime import datetime


class FileStatus(Enum):
    """File existence status in watch and import folders."""
    BOTH = "both"
    ORIGINAL = "original" 
    IMPORT = "import"
    NEITHER = "neither"


class ImportOperationResult(Enum):
    """Results of import operations."""
    SUCCESS = "success"
    FAILED = "failed"
    DUPLICATE = "duplicate"
    NO_PATTERN_MATCH = "no_pattern_match"
    SKIPPED = "skipped"


@dataclass
class ImportPattern:
    """Configuration for file import patterns."""
    regex: str
    provider: str
    version: str
    description: str = ""
    priority: int = 0
    active: bool = True
    
    def __post_init__(self):
        """Post-initialization validation."""
        if not self.regex:
            raise ValueError("Pattern regex cannot be empty")
        if not self.provider:
            raise ValueError("Pattern provider cannot be empty")
        if not self.version:
            raise ValueError("Pattern version cannot be empty")


@dataclass
class ImportEntry:
    """Represents a single file import entry in the index."""
    original_name: str
    imported_name: str
    original_path: Path
    import_path: Path
    watch_folder: Path
    file_size: int
    file_modified_date: str
    import_timestamp: str
    uuid: str
    md5_hash: str
    provider: str
    version: str
    exists_in_watch: bool = True
    exists_in_import: bool = True
    processed_timestamp: Optional[str] = None
    processed_successfully: Optional[bool] = None
    processing_index: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Post-initialization processing."""
        if not isinstance(self.original_path, Path):
            self.original_path = Path(self.original_path)
        if not isinstance(self.import_path, Path):
            self.import_path = Path(self.import_path)
        if not isinstance(self.watch_folder, Path):
            self.watch_folder = Path(self.watch_folder)


@dataclass
class ImportIndex:
    """Complete import index structure."""
    imports: List[ImportEntry] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    version: str = "1.0.0"
    
    def __post_init__(self):
        """Initialize default metadata."""
        if not self.metadata:
            self.metadata = {
                "created": datetime.now().isoformat(),
                "last_scan": "",
                "total_imports": 0,
                "script_version": self.version
            }


@dataclass
class ImportStats:
    """Import operation statistics."""
    total_scanned: int = 0
    total_imported: int = 0
    duplicates_found: int = 0
    pattern_matches: int = 0
    errors: int = 0
    processing_time: float = 0.0
    imported_files: List[str] = field(default_factory=list)
    duplicate_files: List[str] = field(default_factory=list)
    error_files: List[str] = field(default_factory=list)
    
    def add_imported(self, file_path: str):
        """Add a successfully imported file."""
        self.total_imported += 1
        self.imported_files.append(file_path)
    
    def add_duplicate(self, file_path: str):
        """Add a duplicate file."""
        self.duplicates_found += 1
        self.duplicate_files.append(file_path)
    
    def add_error(self, file_path: str):
        """Add an error file."""
        self.errors += 1
        self.error_files.append(file_path)


@dataclass
class ProcessingResult:
    """Result of a file processing operation."""
    success: bool
    entry_uuid: str
    processing_index: str
    error_message: Optional[str] = None
    processing_time: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class IndexBackup:
    """Information about an index backup."""
    backup_path: Path
    original_path: Path
    timestamp: str
    size: int
    entry_count: int
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Post-initialization processing."""
        if not isinstance(self.backup_path, Path):
            self.backup_path = Path(self.backup_path)
        if not isinstance(self.original_path, Path):
            self.original_path = Path(self.original_path)


@dataclass
class WatchFolderConfig:
    """Configuration for a watch folder."""
    path: Path
    recursive: bool = False
    active: bool = True
    patterns: List[str] = field(default_factory=list)
    exclude_patterns: List[str] = field(default_factory=list)
    auto_import: bool = True
    
    def __post_init__(self):
        """Post-initialization processing."""
        if not isinstance(self.path, Path):
            self.path = Path(self.path)


@dataclass
class ImportConfig:
    """Complete import manager configuration."""
    import_directory: Path
    index_file: Path
    watch_folders: List[WatchFolderConfig] = field(default_factory=list)
    patterns: List[ImportPattern] = field(default_factory=list)
    enable_duplicate_detection: bool = True
    enable_backup: bool = True
    max_backups: int = 10
    chunk_size: int = 8192
    
    def __post_init__(self):
        """Post-initialization processing."""
        if not isinstance(self.import_directory, Path):
            self.import_directory = Path(self.import_directory)
        if not isinstance(self.index_file, Path):
            self.index_file = Path(self.index_file)


# Exception classes

class ImportManagerError(Exception):
    """Base exception for import manager operations."""
    
    def __init__(self, message: str, code: Optional[str] = None, path: Optional[Path] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.path = path


class ImportPatternError(ImportManagerError):
    """Exception for import pattern errors."""
    pass


class ImportIndexError(ImportManagerError):
    """Exception for import index errors."""
    pass


class ImportDuplicateError(ImportManagerError):
    """Exception for duplicate handling errors."""
    pass


class ImportProcessingError(ImportManagerError):
    """Exception for processing errors."""
    pass


# Type aliases
PathLike = Union[str, Path]
ImportCallback = Callable[[ImportEntry], None]
ProgressCallback = Callable[[int, int, str], None]
PatternMatcher = Callable[[str], Optional[ImportPattern]]