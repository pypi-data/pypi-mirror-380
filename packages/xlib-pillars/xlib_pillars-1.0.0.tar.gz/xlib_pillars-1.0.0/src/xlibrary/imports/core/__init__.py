"""
xlibrary.imports - Advanced file import management

This module provides comprehensive file import capabilities including:
- Watch folder scanning with configurable patterns
- Provider/version-based file classification and organization
- MD5+filesize duplicate detection and prevention
- UUID-based filename generation for conflict avoidance
- JSON index tracking with processing status management
- Full rollback capability for testing and development
- Batch processing with progress tracking and filtering
- Comprehensive import management and status reporting

Key Features:
- Regex pattern matching with priority-based selection
- Automatic file deduplication using MD5 hash + file size
- Watch folder monitoring with include/exclude pattern support
- Processing workflow management with status tracking
- Index backup and recovery capabilities
- Comprehensive statistics and reporting
- Flexible configuration with multiple watch folders
- Rollback and deletion operations for import management
"""

from .manager import ImportManager
from .patterns import PatternManager
from .processor import ImportProcessor
from .types import (
    # Core data classes
    ImportPattern, ImportEntry, ImportIndex, ImportStats, ProcessingResult,
    IndexBackup, WatchFolderConfig, ImportConfig,
    
    # Enums
    FileStatus, ImportOperationResult,
    
    # Exceptions
    ImportManagerError, ImportPatternError, ImportIndexError,
    ImportDuplicateError, ImportProcessingError,
    
    # Type aliases
    PathLike, ImportCallback, ProgressCallback, PatternMatcher
)

__version__ = "1.0.0"
__all__ = [
    # Core classes
    'ImportManager',
    'PatternManager',
    'ImportProcessor',
    
    # Core data classes
    'ImportPattern',
    'ImportEntry',
    'ImportIndex',
    'ImportStats',
    'ProcessingResult',
    'IndexBackup',
    'WatchFolderConfig',
    'ImportConfig',
    
    # Enums
    'FileStatus',
    'ImportOperationResult',
    
    # Exceptions
    'ImportManagerError',
    'ImportPatternError',
    'ImportIndexError',
    'ImportDuplicateError',
    'ImportProcessingError',
    
    # Type aliases
    'PathLike',
    'ImportCallback',
    'ProgressCallback',
    'PatternMatcher'
]