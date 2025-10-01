"""
Central import management for xlibrary.

Provides standardized file import system with pattern matching, deduplication, 
and processing tracking. Supports watch folder scanning, provider/version-based 
file classification, and comprehensive management interface.
"""

import os
import re
import json
import shutil
import hashlib
import uuid
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from .types import (
    ImportPattern, ImportEntry, ImportIndex, ImportStats, ProcessingResult,
    IndexBackup, WatchFolderConfig, ImportConfig, FileStatus,
    ImportOperationResult, ImportManagerError, ImportPatternError,
    ImportIndexError, ImportDuplicateError, PathLike, ImportCallback,
    ProgressCallback
)
from .patterns import PatternManager
from .processor import ImportProcessor


class ImportManager:
    """
    Core Import Management system.
    
    Features:
    - Watch folder scanning with regex pattern matching
    - Provider/version-based file classification  
    - MD5+filesize duplicate detection and prevention
    - UUID-based filename generation for conflict avoidance
    - JSON index tracking with processing status management
    - Full rollback capability for testing and development
    - Comprehensive import management and status reporting
    """
    
    def __init__(self, config: ImportConfig):
        """
        Initialize Import Manager.
        
        Args:
            config: ImportConfig with all necessary configuration
        """
        self.config = config
        self._index_cache: Optional[ImportIndex] = None
        
        # Initialize components
        self.pattern_manager = PatternManager(config.patterns)
        self.processor = ImportProcessor(self)
        
        # Ensure directories exist
        self._ensure_directories()
    
    def _ensure_directories(self) -> None:
        """Ensure import directory and parent directories exist."""
        self.config.import_directory.mkdir(parents=True, exist_ok=True)
        self.config.index_file.parent.mkdir(parents=True, exist_ok=True)
    
    def _format_timestamp(self, dt: Optional[datetime] = None) -> str:
        """Format datetime to standard YYMMDD.HHMM format."""
        if dt is None:
            dt = datetime.now()
        return dt.strftime("%y%m%d.%H%M")
    
    def _parse_timestamp(self, timestamp: str) -> datetime:
        """Parse timestamp from YYMMDD.HHMM format."""
        return datetime.strptime(timestamp, "%y%m%d.%H%M")
    
    def _calculate_md5(self, file_path: PathLike) -> str:
        """Calculate MD5 hash of file."""
        hash_md5 = hashlib.md5()
        path_obj = Path(file_path)
        
        with open(path_obj, "rb") as f:
            while chunk := f.read(self.config.chunk_size):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _generate_import_filename(self, original_name: str, file_uuid: str, timestamp: str) -> str:
        """Generate unique import filename with timestamp and UUID."""
        path = Path(original_name)
        extension = path.suffix
        return f"{timestamp}_{file_uuid}{extension}"
    
    def _load_index(self) -> ImportIndex:
        """Load import index from JSON file."""
        if not self.config.index_file.exists():
            # Create new index
            return ImportIndex(
                imports=[],
                metadata={
                    "created": datetime.now().isoformat(),
                    "last_scan": self._format_timestamp(),
                    "total_imports": 0,
                    "script_version": "1.0.0"
                }
            )
        
        try:
            with open(self.config.index_file, 'r') as f:
                data = json.load(f)
            
            # Convert dict entries back to ImportEntry objects
            imports = []
            for entry_data in data.get('imports', []):
                # Convert path strings back to Path objects
                entry_data['original_path'] = Path(entry_data['original_path'])
                entry_data['import_path'] = Path(entry_data['import_path'])
                entry_data['watch_folder'] = Path(entry_data['watch_folder'])
                imports.append(ImportEntry(**entry_data))
            
            metadata = data.get('metadata', {})
            version = data.get('version', "1.0.0")
            
            return ImportIndex(imports=imports, metadata=metadata, version=version)
            
        except Exception as e:
            raise ImportIndexError(f"Failed to load import index: {e}")
    
    def _save_index(self, index: ImportIndex) -> None:
        """Save import index to JSON file."""
        try:
            # Convert ImportEntry objects to dictionaries for JSON serialization
            imports_data = []
            for entry in index.imports:
                entry_dict = {
                    'original_name': entry.original_name,
                    'imported_name': entry.imported_name,
                    'original_path': str(entry.original_path),
                    'import_path': str(entry.import_path),
                    'watch_folder': str(entry.watch_folder),
                    'file_size': entry.file_size,
                    'file_modified_date': entry.file_modified_date,
                    'import_timestamp': entry.import_timestamp,
                    'uuid': entry.uuid,
                    'md5_hash': entry.md5_hash,
                    'provider': entry.provider,
                    'version': entry.version,
                    'exists_in_watch': entry.exists_in_watch,
                    'exists_in_import': entry.exists_in_import,
                    'processed_timestamp': entry.processed_timestamp,
                    'processed_successfully': entry.processed_successfully,
                    'processing_index': entry.processing_index,
                    'metadata': entry.metadata
                }
                imports_data.append(entry_dict)
            
            # Create data structure for JSON
            data = {
                "version": index.version,
                "imports": imports_data,
                "metadata": index.metadata
            }
            
            # Update metadata
            data["metadata"]["last_scan"] = self._format_timestamp()
            data["metadata"]["total_imports"] = len(index.imports)
            
            with open(self.config.index_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            raise ImportIndexError(f"Failed to save import index: {e}")
    
    def _find_duplicate(self, index: ImportIndex, md5_hash: str, file_size: int) -> Optional[ImportEntry]:
        """Find duplicate entry by MD5 hash and file size."""
        if not self.config.enable_duplicate_detection:
            return None
            
        for entry in index.imports:
            if entry.md5_hash == md5_hash and entry.file_size == file_size:
                return entry
        return None
    
    def _update_file_existence(self, entry: ImportEntry) -> ImportEntry:
        """Update exists_in_watch and exists_in_import flags for entry."""
        entry.exists_in_watch = entry.original_path.exists()
        entry.exists_in_import = entry.import_path.exists()
        return entry
    
    # ============================================================================
    # WATCH FOLDER SCANNING
    # ============================================================================
    
    def scan_watch_folders(self, progress_callback: Optional[ProgressCallback] = None) -> List[str]:
        """
        Scan watch folders for files matching import patterns.
        
        Args:
            progress_callback: Optional progress callback
            
        Returns:
            List of file paths that match import patterns
        """
        matching_files = []
        total_folders = len(self.config.watch_folders)
        
        for i, watch_config in enumerate(self.config.watch_folders):
            if not watch_config.active:
                continue
                
            if progress_callback:
                progress_callback(i + 1, total_folders, f"Scanning: {watch_config.path.name}")
            
            if not watch_config.path.exists():
                continue
            
            # Get files from watch folder
            if watch_config.recursive:
                file_paths = watch_config.path.rglob("*")
            else:
                file_paths = watch_config.path.iterdir()
            
            for file_path in file_paths:
                if not file_path.is_file():
                    continue
                
                # Check exclude patterns first
                if self._matches_exclude_patterns(file_path.name, watch_config.exclude_patterns):
                    continue
                
                # Check include patterns if specified
                if watch_config.patterns:
                    if not self._matches_include_patterns(file_path.name, watch_config.patterns):
                        continue
                
                # Check against import patterns
                if self.pattern_manager.match_patterns(file_path.name):
                    matching_files.append(str(file_path))
        
        return matching_files
    
    def _matches_exclude_patterns(self, filename: str, patterns: List[str]) -> bool:
        """Check if filename matches any exclude patterns."""
        for pattern in patterns:
            if re.search(pattern, filename):
                return True
        return False
    
    def _matches_include_patterns(self, filename: str, patterns: List[str]) -> bool:
        """Check if filename matches any include patterns."""
        for pattern in patterns:
            if re.search(pattern, filename):
                return True
        return False
    
    # ============================================================================
    # IMPORT OPERATIONS
    # ============================================================================
    
    def import_file(self, file_path: PathLike, 
                   callback: Optional[ImportCallback] = None) -> ImportOperationResult:
        """
        Import a single file.
        
        Args:
            file_path: Path to file to import
            callback: Optional callback for successful imports
            
        Returns:
            ImportOperationResult indicating the result
        """
        file_path_obj = Path(file_path)
        
        if not file_path_obj.exists():
            raise ImportManagerError(f"File not found: {file_path}")
        
        # Calculate file properties
        file_size = file_path_obj.stat().st_size
        md5_hash = self._calculate_md5(file_path_obj)
        file_modified_date = self._format_timestamp(
            datetime.fromtimestamp(file_path_obj.stat().st_mtime)
        )
        
        # Load index and check for duplicates
        index = self._load_index()
        duplicate = self._find_duplicate(index, md5_hash, file_size)
        
        if duplicate:
            return ImportOperationResult.DUPLICATE
        
        # Match patterns
        pattern_match = self.pattern_manager.match_patterns(file_path_obj.name)
        if not pattern_match:
            return ImportOperationResult.NO_PATTERN_MATCH
        
        # Generate import details
        file_uuid = str(uuid.uuid4())
        import_timestamp = self._format_timestamp()
        imported_name = self._generate_import_filename(
            file_path_obj.name, file_uuid, import_timestamp
        )
        
        import_path = self.config.import_directory / imported_name
        
        # Determine watch folder
        watch_folder = file_path_obj.parent
        
        # Copy file to import directory
        try:
            shutil.copy2(file_path_obj, import_path)
        except Exception as e:
            raise ImportManagerError(f"Failed to copy file: {e}")
        
        # Create import entry
        entry = ImportEntry(
            original_name=file_path_obj.name,
            imported_name=imported_name,
            original_path=file_path_obj,
            import_path=import_path,
            watch_folder=watch_folder,
            file_size=file_size,
            file_modified_date=file_modified_date,
            import_timestamp=import_timestamp,
            uuid=file_uuid,
            md5_hash=md5_hash,
            provider=pattern_match.provider,
            version=pattern_match.version,
            exists_in_watch=True,
            exists_in_import=True
        )
        
        # Add to index and save
        index.imports.append(entry)
        self._save_index(index)
        
        # Clear cache
        self._index_cache = None
        
        # Call callback if provided
        if callback:
            callback(entry)
        
        return ImportOperationResult.SUCCESS
    
    def import_scan(self, progress_callback: Optional[ProgressCallback] = None) -> ImportStats:
        """
        Scan watch folders and import new files.
        
        Args:
            progress_callback: Optional progress callback
            
        Returns:
            ImportStats with operation results
        """
        start_time = time.time()
        stats = ImportStats()
        
        matching_files = self.scan_watch_folders()
        stats.total_scanned = len(matching_files)
        stats.pattern_matches = len(matching_files)
        
        for i, file_path in enumerate(matching_files):
            if progress_callback:
                progress_callback(i + 1, len(matching_files), f"Importing: {Path(file_path).name}")
            
            try:
                result = self.import_file(file_path)
                
                if result == ImportOperationResult.SUCCESS:
                    stats.add_imported(file_path)
                elif result == ImportOperationResult.DUPLICATE:
                    stats.add_duplicate(file_path)
                elif result == ImportOperationResult.NO_PATTERN_MATCH:
                    # This shouldn't happen since we pre-filtered, but handle it
                    continue
                    
            except ImportManagerError:
                stats.add_error(file_path)
        
        stats.processing_time = time.time() - start_time
        return stats
    
    # ============================================================================
    # INDEX MANAGEMENT
    # ============================================================================
    
    def get_index(self, refresh: bool = False) -> ImportIndex:
        """
        Get import index.
        
        Args:
            refresh: Force reload from file
            
        Returns:
            ImportIndex instance
        """
        if self._index_cache is None or refresh:
            self._index_cache = self._load_index()
        return self._index_cache
    
    def list_imports(self, limit: Optional[int] = None, 
                    start_date: Optional[str] = None, 
                    end_date: Optional[str] = None, 
                    update_status: bool = True,
                    provider: Optional[str] = None,
                    version: Optional[str] = None,
                    processed_only: Optional[bool] = None) -> List[ImportEntry]:
        """
        List imported files with optional filtering.
        
        Args:
            limit: Maximum number of entries to return
            start_date: Start date filter (YYMMDD format)
            end_date: End date filter (YYMMDD format)
            update_status: Update file existence status
            provider: Filter by provider
            version: Filter by version
            processed_only: Filter by processing status (True/False/None)
            
        Returns:
            List of ImportEntry objects
        """
        index = self.get_index(refresh=True)
        entries = index.imports.copy()
        
        # Update file existence status if requested
        if update_status:
            for i, entry in enumerate(entries):
                entries[i] = self._update_file_existence(entry)
            
            # Save updated index
            index.imports = entries
            self._save_index(index)
            self._index_cache = None
        
        # Apply filters
        filtered_entries = []
        for entry in entries:
            # Date filters
            if start_date or end_date:
                entry_date = entry.import_timestamp.split('.')[0]  # Get YYMMDD part
                
                if start_date and entry_date < start_date:
                    continue
                if end_date and entry_date > end_date:
                    continue
            
            # Provider filter
            if provider and entry.provider != provider:
                continue
            
            # Version filter
            if version and entry.version != version:
                continue
            
            # Processing status filter
            if processed_only is not None:
                is_processed = entry.processed_timestamp is not None
                if processed_only and not is_processed:
                    continue
                if not processed_only and is_processed:
                    continue
            
            filtered_entries.append(entry)
        
        # Sort by import timestamp (most recent first)
        filtered_entries.sort(key=lambda x: x.import_timestamp, reverse=True)
        
        # Apply limit
        if limit:
            filtered_entries = filtered_entries[:limit]
        
        return filtered_entries
    
    # ============================================================================
    # ROLLBACK AND DELETE OPERATIONS
    # ============================================================================
    
    def rollback_import(self, entry_uuid: str) -> bool:
        """
        Rollback an import by UUID.
        
        Args:
            entry_uuid: UUID of entry to rollback
            
        Returns:
            True if successful, False otherwise
        """
        index = self.get_index(refresh=True)
        
        # Find entry
        entry = None
        entry_index = None
        for i, import_entry in enumerate(index.imports):
            if import_entry.uuid == entry_uuid:
                entry = import_entry
                entry_index = i
                break
        
        if not entry:
            return False
        
        # Move file back to original location
        if entry.import_path.exists():
            try:
                # Handle name conflicts
                target_path = entry.original_path
                conflict_counter = 1
                
                while target_path.exists():
                    stem = entry.original_path.stem
                    suffix = entry.original_path.suffix
                    target_path = entry.original_path.parent / f"{stem}_conflict_{conflict_counter:03d}{suffix}"
                    conflict_counter += 1
                
                shutil.move(str(entry.import_path), str(target_path))
                
            except Exception as e:
                raise ImportManagerError(f"Failed to rollback file: {e}")
        
        # Remove from index
        index.imports.pop(entry_index)
        self._save_index(index)
        self._index_cache = None
        
        return True
    
    def delete_import(self, entry_uuid: str) -> bool:
        """
        Delete an import entry and file.
        
        Args:
            entry_uuid: UUID of entry to delete
            
        Returns:
            True if successful, False otherwise
        """
        index = self.get_index(refresh=True)
        
        # Find entry
        entry = None
        entry_index = None
        for i, import_entry in enumerate(index.imports):
            if import_entry.uuid == entry_uuid:
                entry = import_entry
                entry_index = i
                break
        
        if not entry:
            return False
        
        # Delete import file
        if entry.import_path.exists():
            try:
                entry.import_path.unlink()
            except Exception as e:
                raise ImportManagerError(f"Failed to delete import file: {e}")
        
        # Remove from index
        index.imports.pop(entry_index)
        self._save_index(index)
        self._index_cache = None
        
        return True
    
    # ============================================================================
    # BACKUP OPERATIONS
    # ============================================================================
    
    def backup_index(self) -> IndexBackup:
        """
        Create backup of index file.
        
        Returns:
            IndexBackup with backup information
        """
        if not self.config.index_file.exists():
            raise ImportManagerError("Index file does not exist")
        
        timestamp = self._format_timestamp()
        backup_path = self.config.index_file.parent / f"{self.config.index_file.stem}_backup_{timestamp}{self.config.index_file.suffix}"
        
        try:
            shutil.copy2(self.config.index_file, backup_path)
            
            # Get backup info
            backup_stat = backup_path.stat()
            index = self.get_index()
            
            return IndexBackup(
                backup_path=backup_path,
                original_path=self.config.index_file,
                timestamp=timestamp,
                size=backup_stat.st_size,
                entry_count=len(index.imports)
            )
            
        except Exception as e:
            raise ImportManagerError(f"Failed to create backup: {e}")
    
    # ============================================================================
    # STATUS AND UTILITY METHODS
    # ============================================================================
    
    def get_file_status(self, entry: ImportEntry) -> FileStatus:
        """Get file status for an entry."""
        entry = self._update_file_existence(entry)
        
        if entry.exists_in_watch and entry.exists_in_import:
            return FileStatus.BOTH
        elif entry.exists_in_watch and not entry.exists_in_import:
            return FileStatus.ORIGINAL
        elif not entry.exists_in_watch and entry.exists_in_import:
            return FileStatus.IMPORT
        else:
            return FileStatus.NEITHER
    
    def get_status_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive status summary.
        
        Returns:
            Dictionary with status information
        """
        index = self.get_index(refresh=True)
        
        # Update all entries
        for entry in index.imports:
            self._update_file_existence(entry)
        
        total_imports = len(index.imports)
        processed_count = len([e for e in index.imports if e.processed_timestamp])
        unprocessed_count = total_imports - processed_count
        
        missing_original = len([e for e in index.imports if not e.exists_in_watch])
        missing_import = len([e for e in index.imports if not e.exists_in_import])
        missing_both = len([e for e in index.imports if not e.exists_in_watch and not e.exists_in_import])
        
        # Critical: unprocessed AND missing from import folder
        critical_missing = len([
            e for e in index.imports 
            if e.processed_timestamp is None and not e.exists_in_import
        ])
        
        # Provider and version stats
        providers = {}
        versions = {}
        for entry in index.imports:
            providers[entry.provider] = providers.get(entry.provider, 0) + 1
            versions[entry.version] = versions.get(entry.version, 0) + 1
        
        return {
            "total_imports": total_imports,
            "processed_count": processed_count,
            "unprocessed_count": unprocessed_count,
            "missing_from_original": missing_original,
            "missing_from_import": missing_import,
            "missing_from_both": missing_both,
            "critical_missing": critical_missing,
            "watch_folders": [str(wf.path) for wf in self.config.watch_folders if wf.active],
            "import_directory": str(self.config.import_directory),
            "index_file": str(self.config.index_file),
            "providers": providers,
            "versions": versions,
            "pattern_count": len(self.config.patterns)
        }