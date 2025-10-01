"""
Import pattern management for xlibrary.imports.

Provides pattern matching, validation, and management for file import operations.
"""

import re
from typing import Dict, List, Optional, Tuple
from .types import ImportPattern, ImportPatternError


class PatternManager:
    """Manages import patterns and pattern matching operations."""
    
    def __init__(self, patterns: List[ImportPattern]):
        """
        Initialize pattern manager.
        
        Args:
            patterns: List of ImportPattern objects
        """
        self.patterns = patterns
        self._compiled_patterns: Dict[str, re.Pattern] = {}
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for efficient matching."""
        self._compiled_patterns.clear()
        
        for pattern in self.patterns:
            if not pattern.active:
                continue
                
            try:
                compiled_pattern = re.compile(pattern.regex)
                self._compiled_patterns[pattern.regex] = compiled_pattern
            except re.error as e:
                raise ImportPatternError(
                    f"Invalid regex pattern '{pattern.regex}' for provider '{pattern.provider}': {e}"
                )
    
    def match_patterns(self, filename: str) -> Optional[ImportPattern]:
        """
        Check if filename matches any import patterns.
        
        Args:
            filename: Filename to check
            
        Returns:
            ImportPattern if match found, None otherwise
        """
        # Sort patterns by priority (higher priority first)
        sorted_patterns = sorted(
            [p for p in self.patterns if p.active], 
            key=lambda x: x.priority, 
            reverse=True
        )
        
        for pattern in sorted_patterns:
            compiled_pattern = self._compiled_patterns.get(pattern.regex)
            if compiled_pattern and compiled_pattern.match(filename):
                return pattern
        
        return None
    
    def match_all_patterns(self, filename: str) -> List[ImportPattern]:
        """
        Get all patterns that match the filename.
        
        Args:
            filename: Filename to check
            
        Returns:
            List of matching ImportPattern objects
        """
        matching_patterns = []
        
        for pattern in self.patterns:
            if not pattern.active:
                continue
                
            compiled_pattern = self._compiled_patterns.get(pattern.regex)
            if compiled_pattern and compiled_pattern.match(filename):
                matching_patterns.append(pattern)
        
        # Sort by priority (higher first)
        matching_patterns.sort(key=lambda x: x.priority, reverse=True)
        return matching_patterns
    
    def add_pattern(self, pattern: ImportPattern) -> bool:
        """
        Add a new import pattern.
        
        Args:
            pattern: ImportPattern to add
            
        Returns:
            True if added successfully
        """
        # Validate pattern
        try:
            re.compile(pattern.regex)
        except re.error as e:
            raise ImportPatternError(f"Invalid regex pattern: {e}")
        
        # Check for duplicate regex
        for existing_pattern in self.patterns:
            if existing_pattern.regex == pattern.regex:
                raise ImportPatternError(f"Pattern already exists: {pattern.regex}")
        
        self.patterns.append(pattern)
        self._compile_patterns()
        return True
    
    def remove_pattern(self, regex: str) -> bool:
        """
        Remove a pattern by regex.
        
        Args:
            regex: Regex pattern to remove
            
        Returns:
            True if removed, False if not found
        """
        for i, pattern in enumerate(self.patterns):
            if pattern.regex == regex:
                self.patterns.pop(i)
                self._compile_patterns()
                return True
        return False
    
    def update_pattern(self, regex: str, **kwargs) -> bool:
        """
        Update an existing pattern.
        
        Args:
            regex: Regex of pattern to update
            **kwargs: Fields to update
            
        Returns:
            True if updated, False if not found
        """
        for pattern in self.patterns:
            if pattern.regex == regex:
                # Update allowed fields
                for key, value in kwargs.items():
                    if hasattr(pattern, key):
                        setattr(pattern, key, value)
                
                # Recompile patterns if regex or active status changed
                if 'regex' in kwargs or 'active' in kwargs:
                    self._compile_patterns()
                
                return True
        return False
    
    def get_pattern(self, regex: str) -> Optional[ImportPattern]:
        """
        Get a pattern by regex.
        
        Args:
            regex: Regex pattern to find
            
        Returns:
            ImportPattern if found, None otherwise
        """
        for pattern in self.patterns:
            if pattern.regex == regex:
                return pattern
        return None
    
    def list_patterns(self, active_only: bool = False) -> List[ImportPattern]:
        """
        List all patterns.
        
        Args:
            active_only: Only return active patterns
            
        Returns:
            List of ImportPattern objects
        """
        if active_only:
            return [p for p in self.patterns if p.active]
        return self.patterns.copy()
    
    def validate_pattern(self, pattern: ImportPattern) -> List[str]:
        """
        Validate a pattern and return any issues.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            List of validation error messages (empty if valid)
        """
        issues = []
        
        # Check regex validity
        try:
            re.compile(pattern.regex)
        except re.error as e:
            issues.append(f"Invalid regex: {e}")
        
        # Check required fields
        if not pattern.provider.strip():
            issues.append("Provider cannot be empty")
        
        if not pattern.version.strip():
            issues.append("Version cannot be empty")
        
        # Check priority range
        if not isinstance(pattern.priority, int):
            issues.append("Priority must be an integer")
        elif pattern.priority < 0:
            issues.append("Priority cannot be negative")
        
        return issues
    
    def test_pattern(self, pattern: ImportPattern, test_filenames: List[str]) -> Dict[str, bool]:
        """
        Test a pattern against multiple filenames.
        
        Args:
            pattern: Pattern to test
            test_filenames: List of filenames to test against
            
        Returns:
            Dictionary mapping filename to match result
        """
        try:
            compiled_pattern = re.compile(pattern.regex)
        except re.error as e:
            raise ImportPatternError(f"Invalid pattern: {e}")
        
        results = {}
        for filename in test_filenames:
            results[filename] = bool(compiled_pattern.match(filename))
        
        return results
    
    def get_providers(self) -> List[str]:
        """
        Get list of unique providers.
        
        Returns:
            List of provider names
        """
        providers = set(pattern.provider for pattern in self.patterns if pattern.active)
        return sorted(providers)
    
    def get_versions(self, provider: Optional[str] = None) -> List[str]:
        """
        Get list of unique versions, optionally filtered by provider.
        
        Args:
            provider: Optional provider to filter by
            
        Returns:
            List of version names
        """
        versions = set()
        for pattern in self.patterns:
            if not pattern.active:
                continue
            if provider and pattern.provider != provider:
                continue
            versions.add(pattern.version)
        
        return sorted(versions)
    
    def get_patterns_by_provider(self, provider: str) -> List[ImportPattern]:
        """
        Get all patterns for a specific provider.
        
        Args:
            provider: Provider name
            
        Returns:
            List of ImportPattern objects
        """
        return [p for p in self.patterns if p.provider == provider and p.active]
    
    def get_patterns_by_version(self, version: str) -> List[ImportPattern]:
        """
        Get all patterns for a specific version.
        
        Args:
            version: Version name
            
        Returns:
            List of ImportPattern objects
        """
        return [p for p in self.patterns if p.version == version and p.active]
    
    def export_patterns(self) -> List[Dict]:
        """
        Export patterns to a list of dictionaries.
        
        Returns:
            List of pattern dictionaries
        """
        return [
            {
                'regex': p.regex,
                'provider': p.provider,
                'version': p.version,
                'description': p.description,
                'priority': p.priority,
                'active': p.active
            }
            for p in self.patterns
        ]
    
    def import_patterns(self, pattern_dicts: List[Dict], replace: bool = False) -> int:
        """
        Import patterns from a list of dictionaries.
        
        Args:
            pattern_dicts: List of pattern dictionaries
            replace: If True, replace existing patterns
            
        Returns:
            Number of patterns imported
        """
        if replace:
            self.patterns.clear()
        
        imported_count = 0
        for pattern_dict in pattern_dicts:
            try:
                pattern = ImportPattern(**pattern_dict)
                
                # Check for duplicates if not replacing
                if not replace:
                    existing = self.get_pattern(pattern.regex)
                    if existing:
                        continue  # Skip duplicates
                
                self.patterns.append(pattern)
                imported_count += 1
                
            except (TypeError, ValueError) as e:
                # Skip invalid patterns
                continue
        
        self._compile_patterns()
        return imported_count
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get pattern statistics.
        
        Returns:
            Dictionary with pattern statistics
        """
        total_patterns = len(self.patterns)
        active_patterns = len([p for p in self.patterns if p.active])
        unique_providers = len(self.get_providers())
        unique_versions = len(self.get_versions())
        
        return {
            'total_patterns': total_patterns,
            'active_patterns': active_patterns,
            'inactive_patterns': total_patterns - active_patterns,
            'unique_providers': unique_providers,
            'unique_versions': unique_versions
        }