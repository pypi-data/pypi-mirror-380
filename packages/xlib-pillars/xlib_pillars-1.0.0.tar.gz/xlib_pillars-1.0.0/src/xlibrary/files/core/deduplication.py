"""
File deduplication capabilities for xlibrary.files.

Provides advanced duplicate detection using MD5 hashing with content verification.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any

from .types import (
    FileInfo, DuplicateGroup, PathLike, ProgressCallback,
    FileOperationResult, FileManagerError
)


class DuplicateFinder:
    """Handles duplicate file detection and removal operations."""
    
    def __init__(self, file_manager):
        """Initialize with reference to FileManager."""
        self.file_manager = file_manager
    
    def find_duplicates(self, path: PathLike, files: Optional[List[FileInfo]] = None,
                       progress_callback: Optional[ProgressCallback] = None) -> List[DuplicateGroup]:
        """
        Find duplicate files using MD5 hash + content verification.
        
        Args:
            path: Directory to search for duplicates
            files: Optional pre-scanned file list
            progress_callback: Optional callback for progress updates
            
        Returns:
            List of DuplicateGroup objects containing duplicate file groups
        """
        if files is None:
            files = self.file_manager.scan_directory(path, include_hidden=True)
        
        # Group files by size first (optimization)
        size_groups = {}
        for file_info in files:
            if file_info.size not in size_groups:
                size_groups[file_info.size] = []
            size_groups[file_info.size].append(file_info)
        
        # Only check files that have same-size companions
        candidates = []
        for size, file_list in size_groups.items():
            if len(file_list) > 1:
                candidates.extend(file_list)
        
        if not candidates:
            return []
        
        # Calculate MD5 hashes for candidates
        hash_groups = {}
        total_candidates = len(candidates)
        
        for i, file_info in enumerate(candidates):
            if progress_callback:
                progress_callback(i + 1, total_candidates, f"Hashing file: {file_info.name}")
            
            try:
                hash_value = self.file_manager.operations.calculate_hash(file_info.path, 'md5')
                file_info.md5_hash = hash_value
                
                if hash_value not in hash_groups:
                    hash_groups[hash_value] = []
                hash_groups[hash_value].append(file_info)
                
            except Exception:
                continue
        
        # Create duplicate groups and verify with content comparison
        duplicate_groups = []
        
        for hash_value, file_list in hash_groups.items():
            if len(file_list) > 1:
                # Verify duplicates with byte-by-byte comparison
                verified_duplicates = self._verify_duplicates_by_content(file_list)
                
                if len(verified_duplicates) > 1:
                    # Calculate total size
                    total_size = sum(f.size for f in verified_duplicates)
                    
                    duplicate_group = DuplicateGroup(
                        hash_value=hash_value,
                        hash_type='md5',
                        files=verified_duplicates,
                        total_size=total_size
                    )
                    
                    duplicate_groups.append(duplicate_group)
        
        return duplicate_groups
    
    def _verify_duplicates_by_content(self, files: List[FileInfo]) -> List[FileInfo]:
        """
        Verify that files are truly identical by comparing content byte-by-byte.
        
        Args:
            files: List of files with same hash to verify
            
        Returns:
            List of files that are truly identical
        """
        if len(files) <= 1:
            return files
        
        # Use first file as reference
        reference = files[0]
        verified = [reference]
        
        try:
            with open(reference.path, 'rb') as ref_file:
                ref_content = ref_file.read()
        except Exception:
            return []
        
        # Compare each other file with reference
        for file_info in files[1:]:
            try:
                with open(file_info.path, 'rb') as compare_file:
                    if compare_file.read() == ref_content:
                        verified.append(file_info)
            except Exception:
                continue
        
        return verified
    
    def remove_duplicates(self, duplicate_groups: List[DuplicateGroup], dry_run: bool = False,
                         progress_callback: Optional[ProgressCallback] = None) -> Dict[str, Any]:
        """
        Remove duplicate files based on duplicate group recommendations.
        
        Args:
            duplicate_groups: List of duplicate groups from find_duplicates
            dry_run: If True, only simulate the operation
            progress_callback: Optional callback for progress updates
            
        Returns:
            Dictionary with operation results and statistics
        """
        total_files_to_delete = sum(len(group.recommended_delete) for group in duplicate_groups)
        total_space_to_save = sum(
            sum(f.size for f in group.recommended_delete) 
            for group in duplicate_groups
        )
        
        stats = {
            'duplicate_groups': len(duplicate_groups),
            'files_to_delete': total_files_to_delete,
            'space_to_save': total_space_to_save,
            'files_deleted': 0,
            'space_saved': 0,
            'errors': []
        }
        
        if dry_run:
            stats['dry_run'] = True
            deletion_plan = []
            for group in duplicate_groups:
                group_plan = {
                    'hash': group.hash_value,
                    'keep': str(group.recommended_keep.path) if group.recommended_keep else None,
                    'delete': [str(f.path) for f in group.recommended_delete]
                }
                deletion_plan.append(group_plan)
            stats['deletion_plan'] = deletion_plan
            return stats
        
        # Delete files
        deleted_count = 0
        for group in duplicate_groups:
            for file_to_delete in group.recommended_delete:
                deleted_count += 1
                
                if progress_callback:
                    progress_callback(deleted_count, total_files_to_delete, 
                                    f"Deleting duplicate: {file_to_delete.name}")
                
                try:
                    os.remove(file_to_delete.path)
                    stats['files_deleted'] += 1
                    stats['space_saved'] += file_to_delete.size
                except Exception as e:
                    stats['errors'].append(f"Failed to delete {file_to_delete.path}: {e}")
        
        return stats
    
    def analyze_duplicates(self, duplicate_groups: List[DuplicateGroup]) -> Dict[str, Any]:
        """
        Analyze duplicate groups and provide detailed statistics.
        
        Args:
            duplicate_groups: List of duplicate groups to analyze
            
        Returns:
            Dictionary with analysis results
        """
        if not duplicate_groups:
            return {
                'total_groups': 0,
                'total_duplicates': 0,
                'total_wasted_space': 0,
                'largest_duplicate_group': None,
                'most_wasted_space_group': None
            }
        
        total_duplicates = sum(len(group.files) for group in duplicate_groups)
        total_wasted_space = sum(
            sum(f.size for f in group.recommended_delete) 
            for group in duplicate_groups
        )
        
        # Find largest duplicate group by file count
        largest_group = max(duplicate_groups, key=lambda g: len(g.files))
        
        # Find group with most wasted space
        most_wasteful_group = max(duplicate_groups, 
                                 key=lambda g: sum(f.size for f in g.recommended_delete))
        
        # Group by file type
        type_analysis = {}
        for group in duplicate_groups:
            if group.files:
                file_type = group.files[0].file_type.value
                if file_type not in type_analysis:
                    type_analysis[file_type] = {
                        'groups': 0,
                        'files': 0,
                        'wasted_space': 0
                    }
                
                type_analysis[file_type]['groups'] += 1
                type_analysis[file_type]['files'] += len(group.files)
                type_analysis[file_type]['wasted_space'] += sum(
                    f.size for f in group.recommended_delete
                )
        
        return {
            'total_groups': len(duplicate_groups),
            'total_duplicates': total_duplicates,
            'total_wasted_space': total_wasted_space,
            'average_group_size': total_duplicates / len(duplicate_groups),
            'largest_duplicate_group': {
                'hash': largest_group.hash_value,
                'file_count': len(largest_group.files),
                'total_size': largest_group.total_size
            },
            'most_wasted_space_group': {
                'hash': most_wasteful_group.hash_value,
                'wasted_space': sum(f.size for f in most_wasteful_group.recommended_delete),
                'file_count': len(most_wasteful_group.files)
            },
            'by_file_type': type_analysis
        }
    
    def find_similar_files(self, path: PathLike, similarity_threshold: float = 0.8,
                          file_filter: Optional[Callable[[FileInfo], bool]] = None,
                          progress_callback: Optional[ProgressCallback] = None) -> List[Dict[str, Any]]:
        """
        Find files with similar names or content (fuzzy matching).
        
        Args:
            path: Directory to search
            similarity_threshold: Minimum similarity score (0.0 to 1.0)
            file_filter: Optional filter for files to consider
            progress_callback: Optional progress callback
            
        Returns:
            List of similar file groups
        """
        import difflib
        
        files = self.file_manager.scan_directory(path, include_hidden=True)
        
        if file_filter:
            files = [f for f in files if file_filter(f)]
        
        similar_groups = []
        processed_files = set()
        
        for i, file1 in enumerate(files):
            if str(file1.path) in processed_files:
                continue
            
            if progress_callback:
                progress_callback(i + 1, len(files), f"Analyzing: {file1.name}")
            
            similar_files = [file1]
            processed_files.add(str(file1.path))
            
            for file2 in files[i+1:]:
                if str(file2.path) in processed_files:
                    continue
                
                # Calculate name similarity
                name_similarity = difflib.SequenceMatcher(
                    None, file1.name.lower(), file2.name.lower()
                ).ratio()
                
                if name_similarity >= similarity_threshold:
                    similar_files.append(file2)
                    processed_files.add(str(file2.path))
            
            if len(similar_files) > 1:
                similar_groups.append({
                    'files': similar_files,
                    'similarity_scores': [
                        difflib.SequenceMatcher(None, file1.name.lower(), f.name.lower()).ratio()
                        for f in similar_files
                    ],
                    'total_size': sum(f.size for f in similar_files)
                })
        
        # Sort by number of similar files (descending)
        similar_groups.sort(key=lambda g: len(g['files']), reverse=True)
        
        return similar_groups