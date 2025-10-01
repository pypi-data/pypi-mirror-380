"""
Static domain preferences and default method rankings.

This file contains curated preferences based on community knowledge and testing.
It gets updated with new releases and can be overridden by learned metrics.
"""

from typing import Dict, List
from ..core.types import extract_clean_domain

# Static domain preferences - updated with each release
# Format: domain -> [primary_method, fallback_methods...]
DEFAULT_DOMAIN_PREFERENCES: Dict[str, List[str]] = {
    # Video platforms
    "youtube": ["yt-dlp", "youtube-dl", "requests"],
    "vimeo": ["yt-dlp", "requests", "youtube-dl"],
    "dailymotion": ["yt-dlp", "youtube-dl"],
    "twitch": ["yt-dlp", "youtube-dl"],

    # Social media
    "instagram": ["yt-dlp", "requests"],
    "tiktok": ["yt-dlp", "youtube-dl"],
    "twitter": ["yt-dlp", "youtube-dl"],
    "facebook": ["yt-dlp", "youtube-dl"],

    # Audio platforms
    "soundcloud": ["yt-dlp", "youtube-dl"],
    "bandcamp": ["yt-dlp", "youtube-dl"],
    "spotify": ["yt-dlp"],  # Limited support

    # Generic/HTTP
    "generic": ["requests", "wget", "curl"],
    "unknown": ["yt-dlp", "youtube-dl", "requests", "wget", "curl"]
}

# Known reliability ratings based on community feedback and testing
METHOD_RELIABILITY_MATRIX: Dict[str, Dict[str, float]] = {
    "youtube": {
        "yt-dlp": 0.95,      # Excellent - actively maintained
        "youtube-dl": 0.85,   # Good - stable but slower updates
        "requests": 0.10,     # Poor - YouTube blocks direct requests
        "wget": 0.05,         # Very poor
        "curl": 0.05          # Very poor
    },
    "vimeo": {
        "yt-dlp": 0.90,
        "requests": 0.75,     # Sometimes works for direct URLs
        "youtube-dl": 0.80,
        "wget": 0.60,
        "curl": 0.60
    },
    "instagram": {
        "yt-dlp": 0.80,       # Good but requires updates for API changes
        "requests": 0.30,     # Limited - requires headers/auth
        "youtube-dl": 0.60,   # Fair but often outdated
        "wget": 0.15,
        "curl": 0.15
    },
    "tiktok": {
        "yt-dlp": 0.85,
        "youtube-dl": 0.70,
        "requests": 0.20,
        "wget": 0.10,
        "curl": 0.10
    },
    "soundcloud": {
        "yt-dlp": 0.90,
        "youtube-dl": 0.85,
        "requests": 0.40,     # Some tracks are direct
        "wget": 0.30,
        "curl": 0.30
    },
    "generic": {
        "requests": 0.90,     # Best for generic HTTP
        "wget": 0.85,
        "curl": 0.85,
        "yt-dlp": 0.20,       # Overkill for simple files
        "youtube-dl": 0.15
    }
}

# Common error patterns that indicate method won't work
ERROR_PATTERNS: Dict[str, Dict[str, List[str]]] = {
    "youtube": {
        "requests": ["403", "blocked", "access denied"],
        "wget": ["403", "not found", "forbidden"],
        "curl": ["403", "not found", "forbidden"]
    },
    "instagram": {
        "requests": ["login required", "403", "rate limit"],
        "youtube-dl": ["extractor outdated", "api changed"]
    },
    "tiktok": {
        "requests": ["403", "cloudflare", "rate limit"],
        "wget": ["403", "blocked", "javascript required"]
    }
}

# Speed expectations (MB/s) for different methods on different domains
EXPECTED_SPEEDS: Dict[str, Dict[str, float]] = {
    "youtube": {
        "yt-dlp": 2.5,
        "youtube-dl": 2.0,
        "requests": 1.0  # If it works
    },
    "vimeo": {
        "yt-dlp": 3.0,
        "requests": 4.0,  # Direct downloads are fast
        "youtube-dl": 2.2
    },
    "generic": {
        "requests": 5.0,
        "wget": 4.5,
        "curl": 4.5,
        "yt-dlp": 1.5
    }
}


class DomainPreferences:
    """Manages domain-specific download method preferences."""

    def __init__(self):
        self.preferences = DEFAULT_DOMAIN_PREFERENCES.copy()
        self.reliability_matrix = METHOD_RELIABILITY_MATRIX.copy()
        self.error_patterns = ERROR_PATTERNS.copy()
        self.expected_speeds = EXPECTED_SPEEDS.copy()

    def get_preferred_methods(self, url: str) -> List[str]:
        """Get preferred methods for a URL in order of preference."""
        domain = extract_clean_domain(url)

        # Try exact domain match first
        if domain in self.preferences:
            return self.preferences[domain].copy()

        # Try partial matches for subdomains
        for known_domain in self.preferences:
            if known_domain in domain:
                return self.preferences[known_domain].copy()

        # Default fallback
        return self.preferences["unknown"].copy()

    def get_expected_success_rate(self, url: str, method: str) -> float:
        """Get expected success rate for method on domain."""
        domain = extract_clean_domain(url)

        if domain in self.reliability_matrix:
            return self.reliability_matrix[domain].get(method, 0.0)

        # Try partial match
        for known_domain in self.reliability_matrix:
            if known_domain in domain:
                return self.reliability_matrix[known_domain].get(method, 0.0)

        # Default conservative estimate
        return 0.5

    def get_expected_speed(self, url: str, method: str) -> float:
        """Get expected download speed for method on domain."""
        domain = extract_clean_domain(url)

        if domain in self.expected_speeds:
            return self.expected_speeds[domain].get(method, 1.0)

        # Default speed estimate
        return 2.0

    def is_error_pattern_known(self, url: str, method: str, error_message: str) -> bool:
        """Check if error message matches known failure patterns."""
        domain = extract_clean_domain(url)

        if domain not in self.error_patterns:
            return False

        if method not in self.error_patterns[domain]:
            return False

        error_lower = error_message.lower()
        patterns = self.error_patterns[domain][method]

        return any(pattern in error_lower for pattern in patterns)

    def should_skip_method(self, url: str, method: str) -> bool:
        """Check if method should be skipped based on known patterns."""
        expected_rate = self.get_expected_success_rate(url, method)

        # Skip methods with very low expected success rate
        return expected_rate < 0.15

    def update_preferences_from_metrics(self, domain: str, method_ranking: List[str]):
        """Update preferences based on learned metrics."""
        if method_ranking and len(method_ranking) > 0:
            self.preferences[domain] = method_ranking

    def get_domain_info(self, url: str) -> Dict[str, any]:
        """Get comprehensive domain information."""
        domain = extract_clean_domain(url)
        preferred_methods = self.get_preferred_methods(url)

        method_info = {}
        for method in preferred_methods:
            method_info[method] = {
                'expected_success_rate': self.get_expected_success_rate(url, method),
                'expected_speed': self.get_expected_speed(url, method),
                'should_skip': self.should_skip_method(url, method)
            }

        return {
            'domain': domain,
            'preferred_methods': preferred_methods,
            'method_details': method_info,
            'has_custom_patterns': domain in self.error_patterns
        }

    def export_preferences(self) -> Dict[str, any]:
        """Export current preferences for saving/analysis."""
        return {
            'domain_preferences': self.preferences,
            'reliability_matrix': self.reliability_matrix,
            'error_patterns': self.error_patterns,
            'expected_speeds': self.expected_speeds,
            'version': '1.0',
            'last_updated': '2025-01-15'
        }