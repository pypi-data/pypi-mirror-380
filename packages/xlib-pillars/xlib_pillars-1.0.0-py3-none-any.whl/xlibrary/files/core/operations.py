"""
Basic file operations and folder management for xlibrary.files.

Provides core file operations, folder structure management, and batch processing.
"""

import os
import shutil
import hashlib
import time
from pathlib import Path
from typing import Dict, List, Optional, Union, Callable, Any

from .types import (
    FileOperationResult, FileInfo, PathLike, ProgressCallback,
    FileManagerError, BatchOperation, ProcessingResult
)


class FileOperations:
    """Handles basic file operations and folder management."""

    def __init__(self, file_manager):
        """Initialize with reference to FileManager."""
        self.file_manager = file_manager

    # ============================================================================
    # BASIC FILE OPERATIONS
    # ============================================================================

    def calculate_hash(self, file_path: PathLike, algorithm: str = 'md5') -> str:
        """
        Calculate hash of a file.

        Args:
            file_path: Path to the file
            algorithm: Hash algorithm ('md5', 'sha256', 'sha1')

        Returns:
            Hexadecimal hash string
        """
        hash_map = {
            'md5': hashlib.md5(),
            'sha256': hashlib.sha256(),
            'sha1': hashlib.sha1()
        }

        if algorithm not in hash_map:
            raise FileManagerError(f"Unsupported hash algorithm: {algorithm}")

        hasher = hash_map[algorithm]
        path_obj = Path(file_path)

        try:
            with open(path_obj, 'rb') as f:
                while chunk := f.read(self.file_manager.chunk_size):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            raise FileManagerError(f"Failed to calculate {algorithm} hash for {file_path}: {e}")

    def move_files(self, sources: Union[PathLike, List[PathLike]], destination: PathLike,
                   overwrite: bool = False, create_dirs: bool = True) -> Dict[str, FileOperationResult]:
        """
        Move one or more files to destination.

        Args:
            sources: Single file path or list of file paths
            destination: Destination directory or file path
            overwrite: Whether to overwrite existing files
            create_dirs: Whether to create destination directories

        Returns:
            Dictionary mapping source paths to operation results
        """
        if not isinstance(sources, list):
            sources = [sources]

        results = {}
        dest_path = Path(destination)

        # Create destination directory if needed
        if create_dirs and not dest_path.exists():
            dest_path.mkdir(parents=True, exist_ok=True)

        for source in sources:
            source_path = Path(source)
            source_str = str(source_path)

            if not source_path.exists():
                results[source_str] = FileOperationResult.FAILED
                continue

            # Determine final destination path
            if dest_path.is_dir():
                final_dest = dest_path / source_path.name
            else:
                final_dest = dest_path

            # Check for existing file
            if final_dest.exists() and not overwrite:
                results[source_str] = FileOperationResult.EXISTS
                continue

            try:
                shutil.move(str(source_path), str(final_dest))
                results[source_str] = FileOperationResult.SUCCESS
            except Exception:
                results[source_str] = FileOperationResult.FAILED

        return results

    def copy_files(self, sources: Union[PathLike, List[PathLike]], destination: PathLike,
                   overwrite: bool = False, create_dirs: bool = True) -> Dict[str, FileOperationResult]:
        """
        Copy one or more files to destination.

        Args:
            sources: Single file path or list of file paths
            destination: Destination directory or file path
            overwrite: Whether to overwrite existing files
            create_dirs: Whether to create destination directories

        Returns:
            Dictionary mapping source paths to operation results
        """
        if not isinstance(sources, list):
            sources = [sources]

        results = {}
        dest_path = Path(destination)

        # Create destination directory if needed
        if create_dirs and not dest_path.exists():
            dest_path.mkdir(parents=True, exist_ok=True)

        for source in sources:
            source_path = Path(source)
            source_str = str(source_path)

            if not source_path.exists():
                results[source_str] = FileOperationResult.FAILED
                continue

            # Determine final destination path
            if dest_path.is_dir():
                final_dest = dest_path / source_path.name
            else:
                final_dest = dest_path

            # Check for existing file
            if final_dest.exists() and not overwrite:
                results[source_str] = FileOperationResult.EXISTS
                continue

            try:
                if source_path.is_file():
                    shutil.copy2(str(source_path), str(final_dest))
                else:
                    shutil.copytree(str(source_path), str(final_dest))
                results[source_str] = FileOperationResult.SUCCESS
            except Exception:
                results[source_str] = FileOperationResult.FAILED

        return results

    # ============================================================================
    # FOLDER STRUCTURE MANAGEMENT
    # ============================================================================

    def collapse_folders(self, target_folder: PathLike, dry_run: bool = False,
                        progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Collapse all subfolders by moving their files to the target folder.

        This recursively moves all files from subfolders to the specified target folder,
        handling name collisions by adding suffixes like "(1)", "(2)", etc.

        Args:
            target_folder: Folder to collapse into
            dry_run: If True, only simulate the operation
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with operation results and statistics
        """
        target_path = Path(target_folder)

        if not target_path.exists():
            raise FileManagerError(f"Target folder not found: {target_folder}")

        if not target_path.is_dir():
            raise FileManagerError(f"Target path is not a directory: {target_folder}")

        # Collect all files in subfolders
        files_to_move = []
        for root, dirs, files in os.walk(target_folder):
            # Skip the target folder itself
            if root == str(target_folder):
                continue

            for filename in files:
                source_path = Path(root) / filename
                files_to_move.append(source_path)

        # Statistics
        stats = {
            'files_found': len(files_to_move),
            'files_moved': 0,
            'files_skipped': 0,
            'naming_conflicts': 0,
            'errors': []
        }

        if dry_run:
            stats['dry_run'] = True
            stats['would_move'] = [str(f) for f in files_to_move]
            return stats

        # Move files
        for i, source_path in enumerate(files_to_move):
            if progress_callback:
                progress_callback(i + 1, len(files_to_move), f"Moving file: {source_path.name}")

            # Determine destination filename
            dest_filename = self._get_unique_filename(target_path, source_path.name)
            dest_path = target_path / dest_filename

            # Track naming conflicts
            if dest_filename != source_path.name:
                stats['naming_conflicts'] += 1

            try:
                shutil.move(str(source_path), str(dest_path))
                stats['files_moved'] += 1
            except Exception as e:
                stats['errors'].append(f"Failed to move {source_path}: {e}")
                stats['files_skipped'] += 1

        return stats

    def _get_unique_filename(self, directory: Path, filename: str) -> str:
        """
        Get a unique filename in the directory by adding suffixes if needed.

        Args:
            directory: Target directory
            filename: Desired filename

        Returns:
            Unique filename that doesn't exist in the directory
        """
        base_path = directory / filename

        if not base_path.exists():
            return filename

        # Split filename and extension
        name_part = Path(filename).stem
        ext_part = Path(filename).suffix

        # Try adding numbers
        counter = 1
        while True:
            new_filename = f"{name_part} ({counter}){ext_part}"
            new_path = directory / new_filename

            if not new_path.exists():
                return new_filename

            counter += 1

            # Prevent infinite loop
            if counter > 9999:
                raise FileManagerError(f"Too many naming conflicts for {filename}")

    def remove_empty_folders(self, path: PathLike, dry_run: bool = False,
                           progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Remove all empty folders within the specified path.

        Args:
            path: Root path to search for empty folders
            dry_run: If True, only simulate the operation
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with operation results and statistics
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileManagerError(f"Path not found: {path}")

        empty_folders = []

        # Walk bottom-up to handle nested empty folders
        for root, dirs, files in os.walk(path, topdown=False):
            # Skip the root directory itself
            if root == str(path):
                continue

            root_path = Path(root)

            # Check if folder is empty (no files and no non-empty subdirectories)
            try:
                if not any(root_path.iterdir()):
                    empty_folders.append(root_path)
            except (OSError, PermissionError):
                continue

        stats = {
            'empty_folders_found': len(empty_folders),
            'folders_removed': 0,
            'errors': []
        }

        if dry_run:
            stats['dry_run'] = True
            stats['would_remove'] = [str(f) for f in empty_folders]
            return stats

        # Remove empty folders
        for i, folder_path in enumerate(empty_folders):
            if progress_callback:
                progress_callback(i + 1, len(empty_folders), f"Removing empty folder: {folder_path}")

            try:
                folder_path.rmdir()
                stats['folders_removed'] += 1
            except Exception as e:
                stats['errors'].append(f"Failed to remove {folder_path}: {e}")

        return stats

    def clear_folder_contents(self, path: PathLike, include_hidden: bool = False,
                             dry_run: bool = False,
                             progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Clear all contents from a folder, optionally including hidden files.

        Args:
            path: Path to folder to clear
            include_hidden: Whether to include hidden files and folders
            dry_run: If True, only simulate the operation
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with operation results and statistics
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileManagerError(f"Folder not found: {path}")

        if not path_obj.is_dir():
            raise FileManagerError(f"Path is not a directory: {path}")

        # Collect all items to remove
        items_to_remove = []

        for item in path_obj.iterdir():
            # Skip hidden items if not included
            if not include_hidden and item.name.startswith('.'):
                continue
            items_to_remove.append(item)

        stats = {
            'items_found': len(items_to_remove),
            'items_removed': 0,
            'files_removed': 0,
            'folders_removed': 0,
            'errors': []
        }

        if dry_run:
            stats['dry_run'] = True
            stats['would_remove'] = [str(item) for item in items_to_remove]
            return stats

        # Remove items
        for i, item in enumerate(items_to_remove):
            if progress_callback:
                progress_callback(i + 1, len(items_to_remove), f"Removing: {item.name}")

            try:
                if item.is_file():
                    item.unlink()
                    stats['files_removed'] += 1
                elif item.is_dir():
                    shutil.rmtree(str(item))
                    stats['folders_removed'] += 1
                stats['items_removed'] += 1
            except Exception as e:
                stats['errors'].append(f"Failed to remove {item}: {e}")

        return stats

    def organize_by_file_type(self, path: PathLike, dry_run: bool = False,
                             custom_mapping: Optional[Dict[str, str]] = None,
                             progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Organize files into subfolders based on their file type/extension.

        Args:
            path: Directory to organize
            dry_run: If True, only simulate the operation
            custom_mapping: Custom extension to folder name mapping
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with operation results and statistics
        """
        path_obj = Path(path)

        if not path_obj.exists():
            raise FileManagerError(f"Directory not found: {path}")

        # Default extension to folder mapping
        default_mapping = {
            # Documents
            '.pdf': 'Documents',
            '.docx': 'Documents',
            '.doc': 'Documents',
            '.txt': 'Documents',
            '.rtf': 'Documents',
            '.odt': 'Documents',
            '.md': 'Documents',

            # Images
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.png': 'Images',
            '.gif': 'Images',
            '.bmp': 'Images',
            '.tiff': 'Images',
            '.svg': 'Images',
            '.webp': 'Images',

            # Videos
            '.mp4': 'Videos',
            '.avi': 'Videos',
            '.mkv': 'Videos',
            '.mov': 'Videos',
            '.wmv': 'Videos',
            '.webm': 'Videos',
            '.m4v': 'Videos',

            # Audio
            '.mp3': 'Audio',
            '.flac': 'Audio',
            '.wav': 'Audio',
            '.aac': 'Audio',
            '.ogg': 'Audio',
            '.m4a': 'Audio',

            # Archives
            '.zip': 'Archives',
            '.rar': 'Archives',
            '.7z': 'Archives',
            '.tar': 'Archives',
            '.gz': 'Archives',
            '.bz2': 'Archives',

            # Code
            '.py': 'Code',
            '.js': 'Code',
            '.html': 'Code',
            '.css': 'Code',
            '.cpp': 'Code',
            '.java': 'Code',
            '.php': 'Code',

            # Executables
            '.exe': 'Executables',
            '.msi': 'Executables',
            '.app': 'Executables',
            '.deb': 'Executables',
            '.dmg': 'Executables',
        }

        # Use custom mapping if provided, otherwise use default
        mapping = custom_mapping if custom_mapping else default_mapping

        # Get all files in the directory (not recursive)
        files_to_organize = [
            file for file in path_obj.iterdir()
            if file.is_file() and not file.name.startswith('.')
        ]

        # Group files by their target folders
        file_groups = {}
        for file_path in files_to_organize:
            extension = file_path.suffix.lower()
            target_folder = mapping.get(extension, 'Other')

            if target_folder not in file_groups:
                file_groups[target_folder] = []
            file_groups[target_folder].append(file_path)

        stats = {
            'files_found': len(files_to_organize),
            'files_moved': 0,
            'folders_created': 0,
            'file_groups': {k: len(v) for k, v in file_groups.items()},
            'errors': []
        }

        if dry_run:
            stats['dry_run'] = True
            stats['organization_plan'] = {
                folder: [str(f) for f in files]
                for folder, files in file_groups.items()
            }
            return stats

        # Create folders and move files
        total_files = len(files_to_organize)
        processed = 0

        for folder_name, files in file_groups.items():
            # Create target folder
            target_folder = path_obj / folder_name

            if not target_folder.exists():
                target_folder.mkdir(parents=True, exist_ok=True)
                stats['folders_created'] += 1

            # Move files to target folder
            for file_path in files:
                processed += 1
                if progress_callback:
                    progress_callback(processed, total_files, f"Moving {file_path.name} to {folder_name}")

                try:
                    # Handle naming conflicts
                    dest_filename = self._get_unique_filename(target_folder, file_path.name)
                    dest_path = target_folder / dest_filename

                    shutil.move(str(file_path), str(dest_path))
                    stats['files_moved'] += 1
                except Exception as e:
                    stats['errors'].append(f"Failed to move {file_path}: {e}")

        return stats

    # ============================================================================
    # BATCH OPERATIONS
    # ============================================================================

    def execute_batch_operation(self, operation: BatchOperation) -> ProcessingResult:
        """
        Execute a batch file operation.

        Args:
            operation: BatchOperation configuration

        Returns:
            ProcessingResult with operation results
        """
        start_time = time.time()

        # Find source files
        import glob
        source_files = glob.glob(operation.source_pattern, recursive=operation.recursive)

        if not source_files:
            return ProcessingResult(
                success=False,
                operation=operation.operation,
                error_message="No files found matching pattern"
            )

        result = ProcessingResult(
            success=True,
            operation=operation.operation,
            source_path=Path('.') if not operation.source_pattern.startswith('/') else None
        )

        if operation.dry_run:
            result.details['dry_run'] = True
            result.details['matched_files'] = source_files
            result.files_processed = len(source_files)
            return result

        # Process each file
        for i, source_file in enumerate(source_files):
            source_path = Path(source_file)

            # Apply size filters
            if operation.min_size > 0 and source_path.stat().st_size < operation.min_size:
                result.add_file_result(source_path, FileOperationResult.SKIPPED, "Below minimum size")
                continue

            if operation.max_size and source_path.stat().st_size > operation.max_size:
                result.add_file_result(source_path, FileOperationResult.SKIPPED, "Above maximum size")
                continue

            # Apply extension filters
            if operation.include_extensions and source_path.suffix.lower() not in operation.include_extensions:
                result.add_file_result(source_path, FileOperationResult.SKIPPED, "Extension not included")
                continue

            if operation.exclude_extensions and source_path.suffix.lower() in operation.exclude_extensions:
                result.add_file_result(source_path, FileOperationResult.SKIPPED, "Extension excluded")
                continue

            # Execute operation
            try:
                if operation.operation == 'copy':
                    if operation.target_directory:
                        target_path = operation.target_directory / source_path.name
                        if operation.overwrite or not target_path.exists():
                            shutil.copy2(source_path, target_path)
                            result.add_file_result(source_path, FileOperationResult.SUCCESS)
                        else:
                            result.add_file_result(source_path, FileOperationResult.EXISTS)
                    else:
                        result.add_file_result(source_path, FileOperationResult.FAILED, "No target directory")

                elif operation.operation == 'move':
                    if operation.target_directory:
                        target_path = operation.target_directory / source_path.name
                        if operation.overwrite or not target_path.exists():
                            shutil.move(str(source_path), str(target_path))
                            result.add_file_result(source_path, FileOperationResult.SUCCESS)
                        else:
                            result.add_file_result(source_path, FileOperationResult.EXISTS)
                    else:
                        result.add_file_result(source_path, FileOperationResult.FAILED, "No target directory")

                elif operation.operation == 'delete':
                    source_path.unlink()
                    result.add_file_result(source_path, FileOperationResult.SUCCESS)

                else:
                    result.add_file_result(source_path, FileOperationResult.FAILED, f"Unknown operation: {operation.operation}")

                result.bytes_processed += source_path.stat().st_size

            except Exception as e:
                result.add_file_result(source_path, FileOperationResult.FAILED, str(e))

            # Progress callback
            if operation.progress_callback:
                operation.progress_callback(i + 1, len(source_files), f"Processing {source_path.name}")

        result.processing_time = time.time() - start_time
        result.success = result.files_failed == 0

        return result