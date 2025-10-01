"""
Central file and directory management for xlibrary.

Provides comprehensive file management capabilities including:
- Advanced file type detection and analysis
- Folder structure management and cleanup
- Deduplication with multiple verification methods
- Batch operations with progress tracking
- Compression and extraction utilities
- Text file processing and chunking
"""

import os
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Union, Callable, Any
from datetime import datetime, timedelta

try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

import mimetypes

from .types import (
    FileInfo, FileOperationResult, FileType, FolderStats,
    FileManagerError, PathLike, FileFilter, ProgressCallback
)
from .operations import FileOperations
from .deduplication import DuplicateFinder
from .compression import CompressionManager


class FileManager:
    """
    Central file and directory management for xlibrary scripts.

    Features:
    - Advanced file type detection and analysis
    - Folder structure management and cleanup
    - Deduplication with multiple verification methods
    - Batch operations with progress tracking
    - Compression and extraction utilities
    - Text file processing and chunking
    """

    def __init__(self, temp_dir: Optional[PathLike] = None,
                 chunk_size: int = 8192,
                 large_file_threshold: int = 100 * 1024 * 1024,
                 old_file_days: int = 365):
        """
        Initialize file manager.

        Args:
            temp_dir: Temporary directory for operations
            chunk_size: Default chunk size for file operations
            large_file_threshold: Size threshold for large files (bytes)
            old_file_days: Age threshold for old files (days)
        """
        self.temp_dir = Path(temp_dir) if temp_dir else Path(tempfile.gettempdir())
        self.chunk_size = chunk_size
        self.large_file_threshold = large_file_threshold
        self.old_file_days = old_file_days

        # Initialize components
        self.operations = FileOperations(self)
        self.deduplicator = DuplicateFinder(self)
        self.compressor = CompressionManager(self)

        # Initialize magic library for file type detection
        self.magic_instance = None
        self.magic_type_instance = None

        if MAGIC_AVAILABLE:
            try:
                self.magic_instance = magic.Magic(mime=True)
                self.magic_type_instance = magic.Magic()
            except Exception:
                pass

    # ============================================================================
    # FILE TYPE DETECTION AND ANALYSIS
    # ============================================================================

    def detect_file_type(self, file_path: PathLike) -> FileInfo:
        """
        Detect comprehensive file type information.

        Args:
            file_path: Path to the file to analyze

        Returns:
            FileInfo object with comprehensive file details
        """
        path_obj = Path(file_path)

        if not path_obj.exists():
            raise FileManagerError(f"File not found: {file_path}")

        if not path_obj.is_file():
            raise FileManagerError(f"Path is not a file: {file_path}")

        # Basic file information
        stat = path_obj.stat()

        # Extension and declared type
        extension = path_obj.suffix.lower()
        declared_type = self._get_declared_type(extension)

        # Magic number detection
        actual_type = "unknown"
        mime_type = "application/octet-stream"

        try:
            if self.magic_instance:
                mime_type = self.magic_instance.from_file(str(path_obj))
                actual_type = self.magic_type_instance.from_file(str(path_obj))
            else:
                # Fallback to mimetypes
                mime_guess, _ = mimetypes.guess_type(str(path_obj))
                if mime_guess:
                    mime_type = mime_guess
        except Exception:
            pass

        # Determine file type category
        file_type = self._categorize_file_type(mime_type, extension)

        # Check for type mismatch
        is_mismatch = self._is_type_mismatch(declared_type, actual_type, mime_type)

        # Check permissions
        is_readable = os.access(path_obj, os.R_OK)
        is_writable = os.access(path_obj, os.W_OK)
        is_executable = os.access(path_obj, os.X_OK)

        return FileInfo(
            path=path_obj,
            name=path_obj.name,
            extension=extension,
            size=stat.st_size,
            modified_time=datetime.fromtimestamp(stat.st_mtime),
            created_time=datetime.fromtimestamp(stat.st_ctime),
            is_hidden=path_obj.name.startswith('.'),
            is_readable=is_readable,
            is_writable=is_writable,
            is_executable=is_executable,
            permissions=oct(stat.st_mode)[-3:],
            declared_type=declared_type,
            actual_type=actual_type,
            mime_type=mime_type,
            file_type=file_type,
            is_type_mismatch=is_mismatch
        )

    def _get_declared_type(self, extension: str) -> str:
        """Get declared file type based on extension."""
        type_map = {
            '.txt': 'Text Document',
            '.docx': 'Word Document',
            '.pdf': 'PDF Document',
            '.jpg': 'JPEG Image',
            '.jpeg': 'JPEG Image',
            '.png': 'PNG Image',
            '.gif': 'GIF Image',
            '.bmp': 'BMP Image',
            '.svg': 'SVG Image',
            '.mp4': 'MP4 Video',
            '.avi': 'AVI Video',
            '.mov': 'MOV Video',
            '.mkv': 'MKV Video',
            '.mp3': 'MP3 Audio',
            '.wav': 'WAV Audio',
            '.flac': 'FLAC Audio',
            '.zip': 'ZIP Archive',
            '.tar': 'TAR Archive',
            '.gz': 'GZIP Archive',
            '.7z': '7-Zip Archive',
            '.exe': 'Executable',
            '.app': 'Application',
            '.py': 'Python Script',
            '.js': 'JavaScript',
            '.html': 'HTML Document',
            '.css': 'CSS Stylesheet',
            '.json': 'JSON Data',
            '.xml': 'XML Document',
            '.md': 'Markdown Document'
        }
        return type_map.get(extension, f'{extension.upper()} File' if extension else 'Unknown')

    def _categorize_file_type(self, mime_type: str, extension: str) -> FileType:
        """Categorize file into broad type categories."""
        if mime_type.startswith('text/'):
            return FileType.TEXT
        elif mime_type.startswith('image/'):
            return FileType.IMAGE
        elif mime_type.startswith('video/'):
            return FileType.VIDEO
        elif mime_type.startswith('audio/'):
            return FileType.AUDIO
        elif 'zip' in mime_type or 'tar' in mime_type or 'archive' in mime_type:
            return FileType.ARCHIVE
        elif 'executable' in mime_type or extension in ['.exe', '.app', '.deb', '.rpm']:
            return FileType.EXECUTABLE
        elif mime_type.startswith('application/') and any(x in mime_type for x in ['document', 'pdf', 'office']):
            return FileType.DOCUMENT
        elif mime_type == 'application/octet-stream':
            return FileType.BINARY
        else:
            return FileType.UNKNOWN

    def _is_type_mismatch(self, declared_type: str, actual_type: str, mime_type: str) -> bool:
        """Check if there's a mismatch between declared and actual file type."""
        # Simple heuristics for common mismatches
        if 'Word Document' in declared_type and 'zip' in mime_type.lower():
            return False  # .docx files are ZIP archives, this is expected

        # Check for obvious mismatches
        if 'executable' in actual_type.lower() and not any(x in declared_type.lower() for x in ['exe', 'executable']):
            return True

        if 'text' in mime_type and 'image' in declared_type.lower():
            return True

        return False

    # ============================================================================
    # DIRECTORY SCANNING AND ANALYSIS
    # ============================================================================

    def scan_directory(self, path: PathLike,
                      include_hidden: bool = False,
                      max_depth: Optional[int] = None,
                      file_filter: Optional[FileFilter] = None,
                      progress_callback: Optional[ProgressCallback] = None) -> List[FileInfo]:
        """
        Scan directory with advanced filtering capabilities.

        Args:
            path: Directory path to scan
            include_hidden: Include hidden files
            max_depth: Maximum recursion depth (None for unlimited)
            file_filter: Optional filter function
            progress_callback: Optional progress callback function

        Returns:
            List of FileInfo objects matching the criteria
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileManagerError(f"Directory not found: {path}")

        if not path_obj.is_dir():
            raise FileManagerError(f"Path is not a directory: {path}")

        results = []
        processed = 0

        # Walk directory tree
        for root, dirs, files in os.walk(path):
            current_depth = root[len(str(path)):].count(os.sep)

            # Check depth limit
            if max_depth is not None and current_depth > max_depth:
                dirs[:] = []  # Don't recurse deeper
                continue

            # Filter out hidden directories if not included
            if not include_hidden:
                dirs[:] = [d for d in dirs if not d.startswith('.')]

            for filename in files:
                # Skip hidden files if not included
                if not include_hidden and filename.startswith('.'):
                    continue

                file_path = Path(root) / filename

                try:
                    file_info = self.detect_file_type(file_path)

                    # Apply custom filter if provided
                    if file_filter is None or file_filter(file_info):
                        results.append(file_info)

                    processed += 1
                    if progress_callback and processed % 100 == 0:
                        progress_callback(processed, 0, f"Processed {processed} files")

                except Exception:
                    # Skip files we can't process
                    continue

        return results

    def get_folder_stats(self, path: PathLike, include_hidden: bool = False) -> FolderStats:
        """
        Get comprehensive statistics about a folder.

        Args:
            path: Directory path to analyze
            include_hidden: Include hidden files in analysis

        Returns:
            FolderStats object with detailed folder information
        """
        path_obj = Path(path)
        files = self.scan_directory(path_obj, include_hidden=include_hidden)

        # Initialize stats
        stats = FolderStats(path=path_obj)

        # Calculate basic statistics
        for file_info in files:
            stats.add_file(file_info)

        # Count directories
        for item in path_obj.rglob("*"):
            if item.is_dir() and (include_hidden or not item.name.startswith('.')):
                stats.total_directories += 1

        # Find large files (top 10)
        all_files_sorted = sorted(files, key=lambda x: x.size, reverse=True)
        stats.largest_files = all_files_sorted[:10]

        # Find small files (bottom 10, excluding 0-byte files)
        non_empty_files = [f for f in files if f.size > 0]
        small_files_sorted = sorted(non_empty_files, key=lambda x: x.size)
        stats.smallest_files = small_files_sorted[:10]

        # Find newest files (top 10)
        newest_sorted = sorted(files, key=lambda x: x.modified_time, reverse=True)
        stats.newest_files = newest_sorted[:10]

        # Find oldest files (bottom 10)
        oldest_sorted = sorted(files, key=lambda x: x.modified_time)
        stats.oldest_files = oldest_sorted[:10]

        # Find duplicate groups
        stats.duplicate_groups = self.deduplicator.find_duplicates(path_obj, files)
        stats.duplicate_files_count = sum(len(group.files) for group in stats.duplicate_groups)
        stats.duplicate_size_wasted = sum(
            group.total_size - max(f.size for f in group.files)
            for group in stats.duplicate_groups
        )

        return stats

    # ============================================================================
    # DELEGATE METHODS TO COMPONENTS
    # ============================================================================

    # File operations
    def calculate_hash(self, file_path: PathLike, algorithm: str = 'md5') -> str:
        """Calculate hash of a file."""
        return self.operations.calculate_hash(file_path, algorithm)

    def move_files(self, sources: Union[PathLike, List[PathLike]], destination: PathLike,
                   overwrite: bool = False, create_dirs: bool = True) -> Dict[str, FileOperationResult]:
        """Move one or more files to destination."""
        return self.operations.move_files(sources, destination, overwrite, create_dirs)

    def copy_files(self, sources: Union[PathLike, List[PathLike]], destination: PathLike,
                   overwrite: bool = False, create_dirs: bool = True) -> Dict[str, FileOperationResult]:
        """Copy one or more files to destination."""
        return self.operations.copy_files(sources, destination, overwrite, create_dirs)

    # Folder operations
    def collapse_folders(self, target_folder: PathLike, dry_run: bool = False,
                        progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Collapse all subfolders by moving their files to the target folder."""
        return self.operations.collapse_folders(target_folder, dry_run, progress_callback)

    def remove_empty_folders(self, path: PathLike, dry_run: bool = False,
                           progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Remove all empty folders within the specified path."""
        return self.operations.remove_empty_folders(path, dry_run, progress_callback)

    def organize_by_file_type(self, path: PathLike, dry_run: bool = False,
                             custom_mapping: Optional[Dict[str, str]] = None,
                             progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Organize files into subfolders based on their file type/extension."""
        return self.operations.organize_by_file_type(path, dry_run, custom_mapping, progress_callback)

    def clear_folder_contents(self, path: PathLike, include_hidden: bool = False,
                             dry_run: bool = False,
                             progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Clear all contents from a folder, optionally including hidden files."""
        return self.operations.clear_folder_contents(path, include_hidden, dry_run, progress_callback)

    # Deduplication
    def find_duplicates(self, path: PathLike, files: Optional[List[FileInfo]] = None,
                       progress_callback: Optional[ProgressCallback] = None):
        """Find duplicate files using MD5 hash + content verification."""
        return self.deduplicator.find_duplicates(path, files, progress_callback)

    def remove_duplicates(self, duplicate_groups, dry_run: bool = False,
                         progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Remove duplicate files based on duplicate group recommendations."""
        return self.deduplicator.remove_duplicates(duplicate_groups, dry_run, progress_callback)

    # Compression
    def compress_folder(self, source_path: PathLike, archive_path: PathLike,
                       format: str = "zip", exclude_patterns: Optional[List[str]] = None,
                       progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Compress a folder into an archive."""
        return self.compressor.compress_folder(source_path, archive_path, format, exclude_patterns, progress_callback)

    def extract_archive(self, archive_path: PathLike, destination_path: PathLike,
                       overwrite: bool = False, progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """Extract an archive to a destination folder."""
        return self.compressor.extract_archive(archive_path, destination_path, overwrite, progress_callback)

    # ============================================================================
    # UTILITY METHODS
    # ============================================================================

    def get_file_info_summary(self, file_infos: List[FileInfo]) -> Dict[str, Any]:
        """
        Get a summary of a list of FileInfo objects.

        Args:
            file_infos: List of FileInfo objects to summarize

        Returns:
            Dictionary with summary statistics
        """
        if not file_infos:
            return {'total_files': 0, 'total_size': 0}

        total_size = sum(f.size for f in file_infos)
        file_types = {}
        extensions = {}
        largest_file = max(file_infos, key=lambda x: x.size)
        oldest_file = min(file_infos, key=lambda x: x.modified_time)
        newest_file = max(file_infos, key=lambda x: x.modified_time)

        for file_info in file_infos:
            # Count file types
            file_type = file_info.file_type.value
            file_types[file_type] = file_types.get(file_type, 0) + 1

            # Count extensions
            ext = file_info.extension or 'no_extension'
            extensions[ext] = extensions.get(ext, 0) + 1

        return {
            'total_files': len(file_infos),
            'total_size': total_size,
            'average_size': total_size // len(file_infos),
            'file_types': file_types,
            'extensions': extensions,
            'largest_file': {'name': largest_file.name, 'size': largest_file.size},
            'oldest_file': {'name': oldest_file.name, 'modified': oldest_file.modified_time.isoformat()},
            'newest_file': {'name': newest_file.name, 'modified': newest_file.modified_time.isoformat()}
        }