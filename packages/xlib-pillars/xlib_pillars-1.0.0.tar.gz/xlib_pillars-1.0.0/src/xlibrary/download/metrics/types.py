"""
Type definitions for download metrics system.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum


class MethodPerformance(Enum):
    """Performance rating for download methods."""
    EXCELLENT = "excellent"  # >95% success
    GOOD = "good"           # 80-95% success
    FAIR = "fair"           # 60-80% success
    POOR = "poor"           # <60% success
    UNKNOWN = "unknown"     # Not enough data


@dataclass
class MethodStats:
    """Statistics for a download method on a specific domain."""
    method_name: str
    domain: str
    total_attempts: int = 0
    successful_attempts: int = 0
    failed_attempts: int = 0
    total_download_time: float = 0.0  # seconds
    total_bytes_downloaded: int = 0
    last_attempt: Optional[datetime] = None
    last_success: Optional[datetime] = None
    common_errors: List[str] = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        """Calculate success rate (0.0 to 1.0)."""
        if self.total_attempts == 0:
            return 0.0
        return self.successful_attempts / self.total_attempts

    @property
    def average_speed(self) -> float:
        """Average download speed in MB/s."""
        if self.total_download_time == 0 or self.total_bytes_downloaded == 0:
            return 0.0
        return (self.total_bytes_downloaded / (1024 * 1024)) / self.total_download_time

    @property
    def performance_rating(self) -> MethodPerformance:
        """Get performance rating based on success rate."""
        rate = self.success_rate
        if rate >= 0.95:
            return MethodPerformance.EXCELLENT
        elif rate >= 0.80:
            return MethodPerformance.GOOD
        elif rate >= 0.60:
            return MethodPerformance.FAIR
        elif rate > 0:
            return MethodPerformance.POOR
        else:
            return MethodPerformance.UNKNOWN


@dataclass
class DomainStats:
    """Statistics for all methods on a specific domain."""
    domain: str
    methods: Dict[str, MethodStats] = field(default_factory=dict)
    total_attempts: int = 0
    first_seen: Optional[datetime] = None
    last_activity: Optional[datetime] = None

    def get_best_method(self) -> Optional[str]:
        """Get the method with highest success rate."""
        if not self.methods:
            return None

        # Filter methods with at least 5 attempts for reliability
        reliable_methods = {
            name: stats for name, stats in self.methods.items()
            if stats.total_attempts >= 5
        }

        if not reliable_methods:
            # If no method has enough attempts, use the one with most attempts
            return max(self.methods.keys(), key=lambda m: self.methods[m].total_attempts)

        # Sort by success rate, then by speed
        best = max(
            reliable_methods.keys(),
            key=lambda m: (reliable_methods[m].success_rate, reliable_methods[m].average_speed)
        )
        return best

    def get_method_ranking(self) -> List[str]:
        """Get methods ranked by reliability and speed."""
        if not self.methods:
            return []

        # Sort by success rate (desc), then speed (desc), then total attempts (desc)
        return sorted(
            self.methods.keys(),
            key=lambda m: (
                self.methods[m].success_rate,
                self.methods[m].average_speed,
                self.methods[m].total_attempts
            ),
            reverse=True
        )


@dataclass
class DownloadMetrics:
    """Complete metrics data for the download system."""
    domains: Dict[str, DomainStats] = field(default_factory=dict)
    global_stats: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)
    version: str = "1.0"

    def get_domain_stats(self, domain: str) -> Optional[DomainStats]:
        """Get statistics for a specific domain."""
        return self.domains.get(domain)

    def get_global_best_methods(self) -> Dict[str, str]:
        """Get best method for each domain."""
        return {
            domain: stats.get_best_method() or "yt-dlp"
            for domain, stats in self.domains.items()
            if stats.get_best_method()
        }

    def get_performance_summary(self) -> Dict[str, Any]:
        """Get overall performance summary."""
        total_domains = len(self.domains)
        total_attempts = sum(domain.total_attempts for domain in self.domains.values())

        # Method performance across all domains
        method_totals = {}
        for domain_stats in self.domains.values():
            for method_name, method_stats in domain_stats.methods.items():
                if method_name not in method_totals:
                    method_totals[method_name] = {
                        'attempts': 0,
                        'successes': 0,
                        'total_time': 0.0,
                        'total_bytes': 0
                    }

                method_totals[method_name]['attempts'] += method_stats.total_attempts
                method_totals[method_name]['successes'] += method_stats.successful_attempts
                method_totals[method_name]['total_time'] += method_stats.total_download_time
                method_totals[method_name]['total_bytes'] += method_stats.total_bytes_downloaded

        # Calculate global success rates
        method_performance = {}
        for method, totals in method_totals.items():
            success_rate = totals['successes'] / totals['attempts'] if totals['attempts'] > 0 else 0
            avg_speed = (totals['total_bytes'] / (1024 * 1024)) / totals['total_time'] if totals['total_time'] > 0 else 0

            method_performance[method] = {
                'success_rate': success_rate,
                'average_speed_mbps': avg_speed,
                'total_attempts': totals['attempts'],
                'performance_rating': MethodPerformance.EXCELLENT.value if success_rate >= 0.95 else
                                    MethodPerformance.GOOD.value if success_rate >= 0.80 else
                                    MethodPerformance.FAIR.value if success_rate >= 0.60 else
                                    MethodPerformance.POOR.value if success_rate > 0 else
                                    MethodPerformance.UNKNOWN.value
            }

        return {
            'total_domains': total_domains,
            'total_attempts': total_attempts,
            'method_performance': method_performance,
            'last_updated': self.last_updated,
            'data_quality': 'good' if total_attempts > 100 else 'limited'
        }