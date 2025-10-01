"""
Import processing management for xlibrary.imports.

Handles processing status, batch operations, and processing workflows.
"""

import time
from datetime import datetime
from typing import List, Optional, Dict, Any, Callable

from .types import (
    ImportEntry, ImportIndex, ProcessingResult, ImportStats,
    ImportProcessingError, ProgressCallback
)


class ImportProcessor:
    """Handles import processing operations and status management."""
    
    def __init__(self, import_manager):
        """
        Initialize processor.
        
        Args:
            import_manager: Reference to ImportManager instance
        """
        self.import_manager = import_manager
    
    def mark_processed(self, entry_uuid: str, success: bool, 
                      processing_index: str, error_message: Optional[str] = None) -> bool:
        """
        Mark an entry as processed.
        
        Args:
            entry_uuid: UUID of entry to mark
            success: Whether processing was successful
            processing_index: Script-specific processing identifier
            error_message: Optional error message for failed processing
            
        Returns:
            True if successful, False otherwise
        """
        index = self.import_manager.get_index(refresh=True)
        
        # Find entry
        for entry in index.imports:
            if entry.uuid == entry_uuid:
                entry.processed_timestamp = self.import_manager._format_timestamp()
                entry.processed_successfully = success
                entry.processing_index = processing_index
                
                # Add error to metadata if provided
                if error_message:
                    if 'processing_errors' not in entry.metadata:
                        entry.metadata['processing_errors'] = []
                    entry.metadata['processing_errors'].append({
                        'timestamp': entry.processed_timestamp,
                        'message': error_message
                    })
                
                self.import_manager._save_index(index)
                self.import_manager._index_cache = None
                return True
        
        return False
    
    def clear_processing(self, entry_uuid: str) -> bool:
        """
        Clear processing information for an entry.
        
        Args:
            entry_uuid: UUID of entry to clear
            
        Returns:
            True if successful, False otherwise
        """
        index = self.import_manager.get_index(refresh=True)
        
        # Find entry
        for entry in index.imports:
            if entry.uuid == entry_uuid:
                entry.processed_timestamp = None
                entry.processed_successfully = None  
                entry.processing_index = None
                
                # Clear processing errors from metadata
                if 'processing_errors' in entry.metadata:
                    del entry.metadata['processing_errors']
                
                self.import_manager._save_index(index)
                self.import_manager._index_cache = None
                return True
        
        return False
    
    def get_unprocessed(self, limit: Optional[int] = None) -> List[ImportEntry]:
        """
        Get list of unprocessed entries.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of unprocessed ImportEntry objects
        """
        index = self.import_manager.get_index(refresh=True)
        unprocessed = [
            entry for entry in index.imports 
            if entry.processed_timestamp is None
        ]
        
        # Sort by import timestamp (oldest first for processing order)
        unprocessed.sort(key=lambda x: x.import_timestamp)
        
        if limit:
            unprocessed = unprocessed[:limit]
        
        return unprocessed
    
    def get_failed_processing(self, limit: Optional[int] = None) -> List[ImportEntry]:
        """
        Get list of entries that failed processing.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of failed ImportEntry objects
        """
        index = self.import_manager.get_index(refresh=True)
        failed = [
            entry for entry in index.imports 
            if entry.processed_successfully is False
        ]
        
        # Sort by processing timestamp (most recent first)
        failed.sort(key=lambda x: x.processed_timestamp or "", reverse=True)
        
        if limit:
            failed = failed[:limit]
        
        return failed
    
    def get_processing_queue(self, provider: Optional[str] = None, 
                           version: Optional[str] = None) -> List[ImportEntry]:
        """
        Get processing queue with optional filtering.
        
        Args:
            provider: Optional provider filter
            version: Optional version filter
            
        Returns:
            List of ImportEntry objects ready for processing
        """
        unprocessed = self.get_unprocessed()
        
        if provider or version:
            filtered = []
            for entry in unprocessed:
                if provider and entry.provider != provider:
                    continue
                if version and entry.version != version:
                    continue
                filtered.append(entry)
            return filtered
        
        return unprocessed
    
    def batch_process(self, processor_func: Callable[[ImportEntry], ProcessingResult],
                     max_entries: Optional[int] = None,
                     provider: Optional[str] = None,
                     version: Optional[str] = None,
                     progress_callback: Optional[ProgressCallback] = None) -> ImportStats:
        """
        Process multiple entries in batch.
        
        Args:
            processor_func: Function that processes an ImportEntry and returns ProcessingResult
            max_entries: Maximum number of entries to process
            provider: Optional provider filter
            version: Optional version filter
            progress_callback: Optional progress callback
            
        Returns:
            ImportStats with batch processing results
        """
        start_time = time.time()
        stats = ImportStats()
        
        # Get entries to process
        queue = self.get_processing_queue(provider, version)
        
        if max_entries:
            queue = queue[:max_entries]
        
        stats.total_scanned = len(queue)
        
        for i, entry in enumerate(queue):
            if progress_callback:
                progress_callback(i + 1, len(queue), f"Processing: {entry.original_name}")
            
            try:
                # Process the entry
                result = processor_func(entry)
                
                # Mark as processed
                self.mark_processed(
                    entry.uuid,
                    result.success,
                    result.processing_index,
                    result.error_message
                )
                
                if result.success:
                    stats.add_imported(entry.original_name)
                else:
                    stats.add_error(entry.original_name)
                
            except Exception as e:
                # Mark as failed
                self.mark_processed(
                    entry.uuid,
                    False,
                    "batch_process_error",
                    str(e)
                )
                stats.add_error(entry.original_name)
        
        stats.processing_time = time.time() - start_time
        return stats
    
    def retry_failed(self, processor_func: Callable[[ImportEntry], ProcessingResult],
                    max_entries: Optional[int] = None,
                    progress_callback: Optional[ProgressCallback] = None) -> ImportStats:
        """
        Retry processing failed entries.
        
        Args:
            processor_func: Function that processes an ImportEntry and returns ProcessingResult
            max_entries: Maximum number of entries to retry
            progress_callback: Optional progress callback
            
        Returns:
            ImportStats with retry results
        """
        start_time = time.time()
        stats = ImportStats()
        
        # Get failed entries
        failed_entries = self.get_failed_processing(max_entries)
        stats.total_scanned = len(failed_entries)
        
        for i, entry in enumerate(failed_entries):
            if progress_callback:
                progress_callback(i + 1, len(failed_entries), f"Retrying: {entry.original_name}")
            
            try:
                # Clear previous processing status
                self.clear_processing(entry.uuid)
                
                # Process the entry
                result = processor_func(entry)
                
                # Mark as processed
                self.mark_processed(
                    entry.uuid,
                    result.success,
                    result.processing_index,
                    result.error_message
                )
                
                if result.success:
                    stats.add_imported(entry.original_name)
                else:
                    stats.add_error(entry.original_name)
                
            except Exception as e:
                # Mark as failed again
                self.mark_processed(
                    entry.uuid,
                    False,
                    "retry_error",
                    str(e)
                )
                stats.add_error(entry.original_name)
        
        stats.processing_time = time.time() - start_time
        return stats
    
    def get_processing_stats(self) -> Dict[str, Any]:
        """
        Get detailed processing statistics.
        
        Returns:
            Dictionary with processing statistics
        """
        index = self.import_manager.get_index(refresh=True)
        
        total_entries = len(index.imports)
        processed_entries = [e for e in index.imports if e.processed_timestamp is not None]
        successful_entries = [e for e in index.imports if e.processed_successfully is True]
        failed_entries = [e for e in index.imports if e.processed_successfully is False]
        unprocessed_entries = [e for e in index.imports if e.processed_timestamp is None]
        
        # Processing by provider/version
        provider_stats = {}
        version_stats = {}
        
        for entry in index.imports:
            # Provider stats
            if entry.provider not in provider_stats:
                provider_stats[entry.provider] = {
                    'total': 0, 'processed': 0, 'successful': 0, 'failed': 0
                }
            
            provider_stats[entry.provider]['total'] += 1
            if entry.processed_timestamp:
                provider_stats[entry.provider]['processed'] += 1
                if entry.processed_successfully is True:
                    provider_stats[entry.provider]['successful'] += 1
                elif entry.processed_successfully is False:
                    provider_stats[entry.provider]['failed'] += 1
            
            # Version stats
            if entry.version not in version_stats:
                version_stats[entry.version] = {
                    'total': 0, 'processed': 0, 'successful': 0, 'failed': 0
                }
            
            version_stats[entry.version]['total'] += 1
            if entry.processed_timestamp:
                version_stats[entry.version]['processed'] += 1
                if entry.processed_successfully is True:
                    version_stats[entry.version]['successful'] += 1
                elif entry.processed_successfully is False:
                    version_stats[entry.version]['failed'] += 1
        
        # Processing timeline (last 24 hours)
        recent_processed = []
        current_time = datetime.now()
        
        for entry in processed_entries:
            if entry.processed_timestamp:
                try:
                    processed_time = self.import_manager._parse_timestamp(entry.processed_timestamp)
                    hours_ago = (current_time - processed_time).total_seconds() / 3600
                    if hours_ago <= 24:
                        recent_processed.append(entry)
                except ValueError:
                    continue
        
        return {
            'total_entries': total_entries,
            'processed_count': len(processed_entries),
            'successful_count': len(successful_entries),
            'failed_count': len(failed_entries),
            'unprocessed_count': len(unprocessed_entries),
            'processing_rate': len(processed_entries) / max(total_entries, 1) * 100,
            'success_rate': len(successful_entries) / max(len(processed_entries), 1) * 100,
            'recent_processed_24h': len(recent_processed),
            'provider_stats': provider_stats,
            'version_stats': version_stats
        }
    
    def get_next_batch(self, batch_size: int = 10, 
                      provider: Optional[str] = None,
                      version: Optional[str] = None) -> List[ImportEntry]:
        """
        Get the next batch of entries to process.
        
        Args:
            batch_size: Number of entries to return
            provider: Optional provider filter
            version: Optional version filter
            
        Returns:
            List of ImportEntry objects ready for processing
        """
        return self.get_processing_queue(provider, version)[:batch_size]
    
    def schedule_processing(self, entry_uuid: str, processing_index: str) -> bool:
        """
        Schedule an entry for processing (mark it as being processed).
        
        Args:
            entry_uuid: UUID of entry to schedule
            processing_index: Processing identifier
            
        Returns:
            True if scheduled successfully
        """
        index = self.import_manager.get_index(refresh=True)
        
        for entry in index.imports:
            if entry.uuid == entry_uuid:
                # Add scheduling info to metadata
                if 'processing_schedule' not in entry.metadata:
                    entry.metadata['processing_schedule'] = {}
                
                entry.metadata['processing_schedule'] = {
                    'scheduled_at': self.import_manager._format_timestamp(),
                    'processing_index': processing_index,
                    'status': 'scheduled'
                }
                
                self.import_manager._save_index(index)
                self.import_manager._index_cache = None
                return True
        
        return False
    
    def get_scheduled_entries(self) -> List[ImportEntry]:
        """
        Get entries that are scheduled for processing.
        
        Returns:
            List of scheduled ImportEntry objects
        """
        index = self.import_manager.get_index(refresh=True)
        scheduled = []
        
        for entry in index.imports:
            if (entry.processed_timestamp is None and 
                'processing_schedule' in entry.metadata and
                entry.metadata['processing_schedule'].get('status') == 'scheduled'):
                scheduled.append(entry)
        
        return scheduled