"""
Download metrics tracker - records and analyzes download performance.
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List

from ..core.types import DownloadResult, extract_clean_domain
from .types import DownloadMetrics, DomainStats, MethodStats
from .domain_preferences import DomainPreferences


logger = logging.getLogger(__name__)


class DownloadMetricsTracker:
    """
    Tracks download performance metrics and learns optimal strategies.

    Features:
    - Records success/failure rates by domain and method
    - Tracks download speeds and timing
    - Learns from patterns to optimize future downloads
    - Exports metrics for analysis
    """

    def __init__(
        self,
        metrics_file: Optional[Path] = None,
        auto_save: bool = True,
        enable_learning: bool = True
    ):
        """
        Initialize metrics tracker.

        Args:
            metrics_file: Path to save metrics data (default: ~/.xlibrary/download_metrics.json)
            auto_save: Whether to auto-save after each update
            enable_learning: Whether to learn from patterns and update preferences
        """
        if metrics_file is None:
            cache_dir = Path.home() / ".xlibrary"
            cache_dir.mkdir(exist_ok=True)
            metrics_file = cache_dir / "download_metrics.json"

        self.metrics_file = Path(metrics_file)
        self.auto_save = auto_save
        self.enable_learning = enable_learning

        # Initialize components
        self.domain_preferences = DomainPreferences()
        self.metrics = DownloadMetrics()

        # Load existing metrics
        self._load_metrics()

        logger.info(f"Metrics tracker initialized: {self.metrics_file}")

    def record_attempt(
        self,
        url: str,
        method: str,
        result: DownloadResult,
        download_time: Optional[float] = None,
        error_message: Optional[str] = None
    ):
        """
        Record a download attempt with its results.

        Args:
            url: The URL that was attempted
            method: Download method used (yt-dlp, requests, etc.)
            result: The download result
            download_time: Time taken for download in seconds
            error_message: Error message if download failed
        """
        domain = extract_clean_domain(url)
        now = datetime.now()

        # Ensure domain exists in metrics
        if domain not in self.metrics.domains:
            self.metrics.domains[domain] = DomainStats(
                domain=domain,
                first_seen=now
            )

        domain_stats = self.metrics.domains[domain]

        # Ensure method exists for domain
        if method not in domain_stats.methods:
            domain_stats.methods[method] = MethodStats(
                method_name=method,
                domain=domain
            )

        method_stats = domain_stats.methods[method]

        # Update statistics
        method_stats.total_attempts += 1
        method_stats.last_attempt = now
        domain_stats.total_attempts += 1
        domain_stats.last_activity = now

        if result.success:
            method_stats.successful_attempts += 1
            method_stats.last_success = now

            # Record performance data
            if download_time:
                method_stats.total_download_time += download_time

            if result.file_size:
                method_stats.total_bytes_downloaded += result.file_size

        else:
            method_stats.failed_attempts += 1

            # Record error patterns
            if error_message and error_message not in method_stats.common_errors:
                method_stats.common_errors.append(error_message)

                # Keep only most recent 10 error types
                if len(method_stats.common_errors) > 10:
                    method_stats.common_errors = method_stats.common_errors[-10:]

        # Update global timestamp
        self.metrics.last_updated = now

        # Learn from patterns if enabled
        if self.enable_learning:
            self._update_learned_preferences(domain)

        # Auto-save if enabled
        if self.auto_save:
            self._save_metrics()

        logger.debug(f"Recorded {method} attempt for {domain}: {'success' if result.success else 'failure'}")

    def get_optimal_method_order(self, url: str) -> List[str]:
        """
        Get optimal method order for a URL based on learned statistics.

        Args:
            url: URL to get method order for

        Returns:
            List of methods in optimal order (best first)
        """
        domain = extract_clean_domain(url)

        # If we have learned statistics for this domain, use them
        if domain in self.metrics.domains:
            domain_stats = self.metrics.domains[domain]
            learned_ranking = domain_stats.get_method_ranking()

            if learned_ranking:
                logger.info(f"Using learned method order for {domain}: {learned_ranking}")
                return learned_ranking

        # Fall back to static preferences
        static_order = self.domain_preferences.get_preferred_methods(url)
        logger.info(f"Using static method order for {domain}: {static_order}")
        return static_order

    def get_domain_stats(self, domain: str) -> Optional[DomainStats]:
        """Get statistics for a specific domain."""
        return self.metrics.domains.get(domain)

    def get_method_stats(self, domain: str, method: str) -> Optional[MethodStats]:
        """Get statistics for a specific method on a domain."""
        domain_stats = self.get_domain_stats(domain)
        if domain_stats:
            return domain_stats.methods.get(method)
        return None

    def get_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report."""
        return {
            'summary': self.metrics.get_performance_summary(),
            'domains': {
                domain: {
                    'total_attempts': stats.total_attempts,
                    'best_method': stats.get_best_method(),
                    'method_ranking': stats.get_method_ranking(),
                    'first_seen': stats.first_seen.isoformat() if stats.first_seen else None,
                    'last_activity': stats.last_activity.isoformat() if stats.last_activity else None,
                    'methods': {
                        method: {
                            'success_rate': method_stats.success_rate,
                            'average_speed_mbps': method_stats.average_speed,
                            'total_attempts': method_stats.total_attempts,
                            'performance_rating': method_stats.performance_rating.value,
                            'common_errors': method_stats.common_errors[-3:]  # Last 3 errors
                        }
                        for method, method_stats in stats.methods.items()
                    }
                }
                for domain, stats in self.metrics.domains.items()
            },
            'recommendations': self._generate_recommendations()
        }

    def benchmark_url(self, url: str, available_methods: List[str] = None) -> Dict[str, Any]:
        """
        Generate benchmark recommendations for a URL.

        Args:
            url: URL to benchmark
            available_methods: List of available methods to consider

        Returns:
            Benchmark analysis with recommendations
        """
        domain = extract_clean_domain(url)
        domain_info = self.domain_preferences.get_domain_info(url)

        if available_methods is None:
            available_methods = ["yt-dlp", "youtube-dl", "requests", "wget", "curl"]

        # Get learned statistics
        learned_stats = {}
        if domain in self.metrics.domains:
            domain_stats = self.metrics.domains[domain]
            for method in available_methods:
                if method in domain_stats.methods:
                    method_stats = domain_stats.methods[method]
                    learned_stats[method] = {
                        'success_rate': method_stats.success_rate,
                        'average_speed': method_stats.average_speed,
                        'attempts': method_stats.total_attempts,
                        'rating': method_stats.performance_rating.value
                    }

        # Combine with static preferences
        recommendations = []
        for method in available_methods:
            expected_success = self.domain_preferences.get_expected_success_rate(url, method)
            expected_speed = self.domain_preferences.get_expected_speed(url, method)
            should_skip = self.domain_preferences.should_skip_method(url, method)

            learned_data = learned_stats.get(method, {})

            recommendations.append({
                'method': method,
                'expected_success_rate': expected_success,
                'expected_speed_mbps': expected_speed,
                'learned_success_rate': learned_data.get('success_rate'),
                'learned_speed_mbps': learned_data.get('average_speed'),
                'learned_attempts': learned_data.get('attempts', 0),
                'should_skip': should_skip,
                'confidence': 'high' if learned_data.get('attempts', 0) >= 10 else 'medium' if learned_data.get('attempts', 0) >= 3 else 'low'
            })

        # Sort recommendations by best combination of learned and expected performance
        def recommendation_score(rec):
            # Use learned data if available with high confidence, otherwise use expected
            if rec['confidence'] == 'high' and rec['learned_success_rate'] is not None:
                return rec['learned_success_rate']
            elif rec['confidence'] == 'medium' and rec['learned_success_rate'] is not None:
                # Weighted combination of learned and expected
                return (rec['learned_success_rate'] * 0.7) + (rec['expected_success_rate'] * 0.3)
            else:
                return rec['expected_success_rate']

        recommendations.sort(key=recommendation_score, reverse=True)

        return {
            'url': url,
            'domain': domain,
            'domain_info': domain_info,
            'recommendations': recommendations,
            'optimal_order': [rec['method'] for rec in recommendations if not rec['should_skip']],
            'data_quality': 'good' if sum(r['learned_attempts'] for r in recommendations) > 50 else 'limited'
        }

    def export_metrics(self, output_file: Optional[Path] = None) -> Path:
        """Export metrics to JSON file for analysis."""
        if output_file is None:
            output_file = self.metrics_file.parent / f"metrics_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        export_data = {
            'metrics': self._metrics_to_dict(),
            'preferences': self.domain_preferences.export_preferences(),
            'report': self.get_performance_report(),
            'exported_at': datetime.now().isoformat()
        }

        with open(output_file, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)

        logger.info(f"Metrics exported to {output_file}")
        return output_file

    def _load_metrics(self):
        """Load metrics from file if it exists."""
        if not self.metrics_file.exists():
            logger.info("No existing metrics file found, starting fresh")
            return

        try:
            with open(self.metrics_file, 'r') as f:
                data = json.load(f)

            # Reconstruct metrics object
            self.metrics = self._dict_to_metrics(data)
            logger.info(f"Loaded metrics with {len(self.metrics.domains)} domains")

        except Exception as e:
            logger.warning(f"Failed to load metrics file: {e}")
            logger.info("Starting with fresh metrics")

    def _save_metrics(self):
        """Save current metrics to file."""
        try:
            self.metrics_file.parent.mkdir(parents=True, exist_ok=True)

            data = self._metrics_to_dict()

            with open(self.metrics_file, 'w') as f:
                json.dump(data, f, indent=2, default=str)

            logger.debug(f"Metrics saved to {self.metrics_file}")

        except Exception as e:
            logger.error(f"Failed to save metrics: {e}")

    def _update_learned_preferences(self, domain: str):
        """Update domain preferences based on learned statistics."""
        if domain not in self.metrics.domains:
            return

        domain_stats = self.metrics.domains[domain]

        # Only update preferences if we have sufficient data
        total_attempts = sum(
            method_stats.total_attempts
            for method_stats in domain_stats.methods.values()
        )

        if total_attempts >= 20:  # Threshold for reliable learning
            new_ranking = domain_stats.get_method_ranking()
            if new_ranking:
                self.domain_preferences.update_preferences_from_metrics(domain, new_ranking)
                logger.info(f"Updated learned preferences for {domain}: {new_ranking}")

    def _generate_recommendations(self) -> List[Dict[str, Any]]:
        """Generate actionable recommendations based on metrics."""
        recommendations = []

        for domain, stats in self.metrics.domains.items():
            if stats.total_attempts < 5:
                continue

            best_method = stats.get_best_method()
            if not best_method:
                continue

            best_stats = stats.methods[best_method]

            # Recommend based on performance
            if best_stats.success_rate >= 0.95:
                recommendations.append({
                    'type': 'excellent_performance',
                    'domain': domain,
                    'message': f"Excellent performance: {best_method} has {best_stats.success_rate:.1%} success rate for {domain}",
                    'method': best_method,
                    'success_rate': best_stats.success_rate
                })
            elif best_stats.success_rate < 0.60:
                recommendations.append({
                    'type': 'poor_performance',
                    'domain': domain,
                    'message': f"Poor performance: Best method {best_method} only has {best_stats.success_rate:.1%} success rate for {domain}",
                    'method': best_method,
                    'success_rate': best_stats.success_rate
                })

            # Recommend method updates if YouTube-dl is performing poorly
            if 'youtube-dl' in stats.methods and 'yt-dlp' in stats.methods:
                ytdl_rate = stats.methods['youtube-dl'].success_rate
                ytdlp_rate = stats.methods['yt-dlp'].success_rate

                if ytdlp_rate - ytdl_rate > 0.20:  # 20% difference
                    recommendations.append({
                        'type': 'tool_recommendation',
                        'domain': domain,
                        'message': f"Consider using yt-dlp over youtube-dl for {domain} (success rates: {ytdlp_rate:.1%} vs {ytdl_rate:.1%})",
                        'preferred_method': 'yt-dlp',
                        'alternative_method': 'youtube-dl'
                    })

        return recommendations

    def _metrics_to_dict(self) -> Dict[str, Any]:
        """Convert metrics object to dictionary for JSON serialization."""
        return {
            'domains': {
                domain: {
                    'domain': stats.domain,
                    'total_attempts': stats.total_attempts,
                    'first_seen': stats.first_seen.isoformat() if stats.first_seen else None,
                    'last_activity': stats.last_activity.isoformat() if stats.last_activity else None,
                    'methods': {
                        method: {
                            'method_name': method_stats.method_name,
                            'domain': method_stats.domain,
                            'total_attempts': method_stats.total_attempts,
                            'successful_attempts': method_stats.successful_attempts,
                            'failed_attempts': method_stats.failed_attempts,
                            'total_download_time': method_stats.total_download_time,
                            'total_bytes_downloaded': method_stats.total_bytes_downloaded,
                            'last_attempt': method_stats.last_attempt.isoformat() if method_stats.last_attempt else None,
                            'last_success': method_stats.last_success.isoformat() if method_stats.last_success else None,
                            'common_errors': method_stats.common_errors
                        }
                        for method, method_stats in stats.methods.items()
                    }
                }
                for domain, stats in self.metrics.domains.items()
            },
            'global_stats': self.metrics.global_stats,
            'created_at': self.metrics.created_at.isoformat(),
            'last_updated': self.metrics.last_updated.isoformat(),
            'version': self.metrics.version
        }

    def _dict_to_metrics(self, data: Dict[str, Any]) -> DownloadMetrics:
        """Convert dictionary back to metrics object."""
        metrics = DownloadMetrics()

        # Reconstruct domain stats
        for domain_name, domain_data in data.get('domains', {}).items():
            domain_stats = DomainStats(
                domain=domain_data['domain'],
                total_attempts=domain_data['total_attempts'],
                first_seen=datetime.fromisoformat(domain_data['first_seen']) if domain_data.get('first_seen') else None,
                last_activity=datetime.fromisoformat(domain_data['last_activity']) if domain_data.get('last_activity') else None
            )

            # Reconstruct method stats
            for method_name, method_data in domain_data.get('methods', {}).items():
                method_stats = MethodStats(
                    method_name=method_data['method_name'],
                    domain=method_data['domain'],
                    total_attempts=method_data['total_attempts'],
                    successful_attempts=method_data['successful_attempts'],
                    failed_attempts=method_data['failed_attempts'],
                    total_download_time=method_data['total_download_time'],
                    total_bytes_downloaded=method_data['total_bytes_downloaded'],
                    last_attempt=datetime.fromisoformat(method_data['last_attempt']) if method_data.get('last_attempt') else None,
                    last_success=datetime.fromisoformat(method_data['last_success']) if method_data.get('last_success') else None,
                    common_errors=method_data.get('common_errors', [])
                )
                domain_stats.methods[method_name] = method_stats

            metrics.domains[domain_name] = domain_stats

        # Set other fields
        metrics.global_stats = data.get('global_stats', {})
        metrics.created_at = datetime.fromisoformat(data.get('created_at', datetime.now().isoformat()))
        metrics.last_updated = datetime.fromisoformat(data.get('last_updated', datetime.now().isoformat()))
        metrics.version = data.get('version', '1.0')

        return metrics