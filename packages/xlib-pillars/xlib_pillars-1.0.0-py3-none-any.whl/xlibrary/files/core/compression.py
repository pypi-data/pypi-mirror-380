"""
Archive compression and extraction capabilities for xlibrary.files.

Provides comprehensive compression and extraction utilities for various archive formats.
"""

import os
import zipfile
import tarfile
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any

from .types import (
    CompressionFormat, PathLike, ProgressCallback,
    FileManagerError, CompressionError
)


class CompressionManager:
    """Handles archive compression and extraction operations."""
    
    def __init__(self, file_manager):
        """Initialize with reference to FileManager."""
        self.file_manager = file_manager
    
    def compress_folder(self, source_path: PathLike, archive_path: PathLike, 
                       format: str = "zip",
                       exclude_patterns: Optional[List[str]] = None,
                       progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Compress a folder into an archive.
        
        Args:
            source_path: Path to folder to compress
            archive_path: Path for the output archive
            format: Compression format ("zip", "tar", "tar.gz", "tar.bz2", "tar.xz")
            exclude_patterns: List of patterns to exclude (glob style)
            progress_callback: Optional callback for progress updates
            
        Returns:
            Dictionary with compression results and statistics
        """
        source = Path(source_path)
        archive = Path(archive_path)
        
        if not source.exists():
            raise CompressionError(f"Source path not found: {source_path}")
        
        if not source.is_dir():
            raise CompressionError(f"Source path is not a directory: {source_path}")
        
        # Validate format
        format_enum = self._get_compression_format(format)
        
        # Create parent directory for archive if needed
        archive.parent.mkdir(parents=True, exist_ok=True)
        
        # Collect files to compress
        files_to_compress = []
        for root, dirs, files in os.walk(source):
            for filename in files:
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(source)
                
                # Check exclusion patterns
                if exclude_patterns:
                    should_exclude = False
                    for pattern in exclude_patterns:
                        if file_path.match(pattern) or str(rel_path).find(pattern) != -1:
                            should_exclude = True
                            break
                    if should_exclude:
                        continue
                
                files_to_compress.append((file_path, rel_path))
        
        stats = {
            'source_path': str(source),
            'archive_path': str(archive),
            'format': format,
            'files_found': len(files_to_compress),
            'files_compressed': 0,
            'original_size': 0,
            'compressed_size': 0,
            'errors': []
        }
        
        try:
            if format_enum == CompressionFormat.ZIP:
                self._compress_zip(archive, files_to_compress, stats, progress_callback)
            elif format_enum in [CompressionFormat.TAR, CompressionFormat.TAR_GZ, 
                                CompressionFormat.TAR_BZ2, CompressionFormat.TAR_XZ]:
                self._compress_tar(archive, files_to_compress, format_enum, stats, progress_callback)
            else:
                raise CompressionError(f"Unsupported compression format: {format}")
            
            # Get final archive size
            if archive.exists():
                stats['compressed_size'] = archive.stat().st_size
                if stats['original_size'] > 0:
                    stats['compression_ratio'] = (1 - stats['compressed_size'] / stats['original_size']) * 100
                else:
                    stats['compression_ratio'] = 0
            
        except Exception as e:
            raise CompressionError(f"Compression failed: {e}")
        
        return stats
    
    def _compress_zip(self, archive_path: Path, files_to_compress: List, 
                     stats: Dict, progress_callback: Optional[ProgressCallback]):
        """Compress files to ZIP format."""
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, (file_path, rel_path) in enumerate(files_to_compress):
                if progress_callback:
                    progress_callback(i + 1, len(files_to_compress), 
                                    f"Compressing: {rel_path}")
                
                try:
                    zf.write(file_path, rel_path)
                    stats['files_compressed'] += 1
                    stats['original_size'] += file_path.stat().st_size
                except Exception as e:
                    stats['errors'].append(f"Failed to compress {file_path}: {e}")
    
    def _compress_tar(self, archive_path: Path, files_to_compress: List,
                     format_enum: CompressionFormat, stats: Dict, 
                     progress_callback: Optional[ProgressCallback]):
        """Compress files to TAR format."""
        mode_map = {
            CompressionFormat.TAR: 'w',
            CompressionFormat.TAR_GZ: 'w:gz',
            CompressionFormat.TAR_BZ2: 'w:bz2',
            CompressionFormat.TAR_XZ: 'w:xz'
        }
        
        with tarfile.open(archive_path, mode_map[format_enum]) as tf:
            for i, (file_path, rel_path) in enumerate(files_to_compress):
                if progress_callback:
                    progress_callback(i + 1, len(files_to_compress),
                                    f"Compressing: {rel_path}")
                
                try:
                    tf.add(file_path, rel_path)
                    stats['files_compressed'] += 1
                    stats['original_size'] += file_path.stat().st_size
                except Exception as e:
                    stats['errors'].append(f"Failed to compress {file_path}: {e}")
    
    def extract_archive(self, archive_path: PathLike, destination_path: PathLike,
                       overwrite: bool = False, 
                       progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Extract an archive to a destination folder.
        
        Args:
            archive_path: Path to the archive file
            destination_path: Path to extract files to
            overwrite: Whether to overwrite existing files
            progress_callback: Optional callback for progress updates
            
        Returns:
            Dictionary with extraction results and statistics
        """
        archive = Path(archive_path)
        destination = Path(destination_path)
        
        if not archive.exists():
            raise CompressionError(f"Archive not found: {archive_path}")
        
        # Create destination directory
        destination.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'archive_path': str(archive),
            'destination_path': str(destination),
            'files_extracted': 0,
            'total_size': 0,
            'errors': []
        }
        
        try:
            # Detect archive type and extract
            if archive.suffix.lower() == '.zip':
                self._extract_zip(archive, destination, overwrite, stats, progress_callback)
            elif self._is_tar_archive(archive):
                self._extract_tar(archive, destination, overwrite, stats, progress_callback)
            else:
                raise CompressionError(f"Unsupported archive format: {archive.suffix}")
                
        except Exception as e:
            raise CompressionError(f"Extraction failed: {e}")
        
        return stats
    
    def _extract_zip(self, archive_path: Path, destination: Path, overwrite: bool,
                    stats: Dict, progress_callback: Optional[ProgressCallback]):
        """Extract ZIP archive."""
        with zipfile.ZipFile(archive_path, 'r') as zf:
            members = zf.namelist()
            stats['total_files'] = len(members)
            
            for i, member in enumerate(members):
                if progress_callback:
                    progress_callback(i + 1, len(members), f"Extracting: {member}")
                
                try:
                    member_path = destination / member
                    
                    # Check for overwrite
                    if member_path.exists() and not overwrite:
                        continue
                    
                    # Security check - prevent directory traversal
                    if not str(member_path.resolve()).startswith(str(destination.resolve())):
                        stats['errors'].append(f"Security: Skipped {member} (path traversal attempt)")
                        continue
                    
                    zf.extract(member, destination)
                    stats['files_extracted'] += 1
                    
                    if member_path.exists():
                        stats['total_size'] += member_path.stat().st_size
                        
                except Exception as e:
                    stats['errors'].append(f"Failed to extract {member}: {e}")
    
    def _extract_tar(self, archive_path: Path, destination: Path, overwrite: bool,
                    stats: Dict, progress_callback: Optional[ProgressCallback]):
        """Extract TAR archive."""
        with tarfile.open(archive_path, 'r:*') as tf:
            members = tf.getnames()
            stats['total_files'] = len(members)
            
            for i, member in enumerate(members):
                if progress_callback:
                    progress_callback(i + 1, len(members), f"Extracting: {member}")
                
                try:
                    member_path = destination / member
                    
                    # Check for overwrite
                    if member_path.exists() and not overwrite:
                        continue
                    
                    # Security check - prevent directory traversal
                    if not str(member_path.resolve()).startswith(str(destination.resolve())):
                        stats['errors'].append(f"Security: Skipped {member} (path traversal attempt)")
                        continue
                    
                    tf.extract(member, destination)
                    stats['files_extracted'] += 1
                    
                    if member_path.exists():
                        stats['total_size'] += member_path.stat().st_size
                        
                except Exception as e:
                    stats['errors'].append(f"Failed to extract {member}: {e}")
    
    def _get_compression_format(self, format_str: str) -> CompressionFormat:
        """Convert string format to CompressionFormat enum."""
        format_map = {
            'zip': CompressionFormat.ZIP,
            'tar': CompressionFormat.TAR,
            'tar.gz': CompressionFormat.TAR_GZ,
            'tar.bz2': CompressionFormat.TAR_BZ2,
            'tar.xz': CompressionFormat.TAR_XZ
        }
        
        if format_str.lower() not in format_map:
            raise CompressionError(f"Unsupported format: {format_str}")
        
        return format_map[format_str.lower()]
    
    def _is_tar_archive(self, archive_path: Path) -> bool:
        """Check if file is a TAR archive."""
        tar_extensions = ['.tar', '.tar.gz', '.tar.bz2', '.tar.xz', '.tgz', '.tbz2', '.txz']
        return any(str(archive_path).endswith(ext) for ext in tar_extensions)
    
    def list_archive_contents(self, archive_path: PathLike) -> Dict[str, Any]:
        """
        List contents of an archive without extracting.
        
        Args:
            archive_path: Path to the archive file
            
        Returns:
            Dictionary with archive information and file list
        """
        archive = Path(archive_path)
        
        if not archive.exists():
            raise CompressionError(f"Archive not found: {archive_path}")
        
        contents = {
            'archive_path': str(archive),
            'archive_size': archive.stat().st_size,
            'files': [],
            'directories': [],
            'total_files': 0,
            'total_directories': 0,
            'uncompressed_size': 0
        }
        
        try:
            if archive.suffix.lower() == '.zip':
                with zipfile.ZipFile(archive, 'r') as zf:
                    for info in zf.infolist():
                        if info.is_dir():
                            contents['directories'].append({
                                'name': info.filename,
                                'date_time': info.date_time
                            })
                            contents['total_directories'] += 1
                        else:
                            contents['files'].append({
                                'name': info.filename,
                                'size': info.file_size,
                                'compressed_size': info.compress_size,
                                'date_time': info.date_time,
                                'crc': info.CRC
                            })
                            contents['total_files'] += 1
                            contents['uncompressed_size'] += info.file_size
            
            elif self._is_tar_archive(archive):
                with tarfile.open(archive, 'r:*') as tf:
                    for member in tf.getmembers():
                        if member.isdir():
                            contents['directories'].append({
                                'name': member.name,
                                'mode': oct(member.mode),
                                'mtime': member.mtime
                            })
                            contents['total_directories'] += 1
                        elif member.isfile():
                            contents['files'].append({
                                'name': member.name,
                                'size': member.size,
                                'mode': oct(member.mode),
                                'mtime': member.mtime,
                                'uid': member.uid,
                                'gid': member.gid
                            })
                            contents['total_files'] += 1
                            contents['uncompressed_size'] += member.size
            
            else:
                raise CompressionError(f"Unsupported archive format: {archive.suffix}")
        
        except Exception as e:
            raise CompressionError(f"Failed to read archive contents: {e}")
        
        return contents
    
    def verify_archive(self, archive_path: PathLike) -> Dict[str, Any]:
        """
        Verify the integrity of an archive.
        
        Args:
            archive_path: Path to the archive file
            
        Returns:
            Dictionary with verification results
        """
        archive = Path(archive_path)
        
        if not archive.exists():
            raise CompressionError(f"Archive not found: {archive_path}")
        
        result = {
            'archive_path': str(archive),
            'is_valid': False,
            'errors': [],
            'warnings': []
        }
        
        try:
            if archive.suffix.lower() == '.zip':
                with zipfile.ZipFile(archive, 'r') as zf:
                    # Test all files in the archive
                    bad_file = zf.testzip()
                    if bad_file:
                        result['errors'].append(f"Corrupted file in archive: {bad_file}")
                    else:
                        result['is_valid'] = True
            
            elif self._is_tar_archive(archive):
                with tarfile.open(archive, 'r:*') as tf:
                    # Try to list all members
                    members = tf.getmembers()
                    result['is_valid'] = True
                    result['warnings'].append(f"TAR verification limited - found {len(members)} members")
            
            else:
                result['errors'].append(f"Unsupported archive format: {archive.suffix}")
        
        except Exception as e:
            result['errors'].append(f"Archive verification failed: {e}")
        
        return result