"""
Metrics analyzer - provides insights and recommendations from download metrics.
"""

import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple

from .types import DownloadMetrics, MethodPerformance
from .tracker import DownloadMetricsTracker


logger = logging.getLogger(__name__)


class MetricsAnalyzer:
    """
    Analyzes download metrics to provide insights and recommendations.

    Features:
    - Performance analysis across domains and methods
    - Trend analysis over time
    - Bottleneck identification
    - Optimization recommendations
    """

    def __init__(self, tracker: DownloadMetricsTracker):
        """
        Initialize analyzer with metrics tracker.

        Args:
            tracker: DownloadMetricsTracker instance
        """
        self.tracker = tracker

    def analyze_domain_performance(self, domain: str) -> Dict[str, Any]:
        """
        Analyze performance for a specific domain.

        Args:
            domain: Domain to analyze

        Returns:
            Comprehensive domain analysis
        """
        domain_stats = self.tracker.get_domain_stats(domain)
        if not domain_stats:
            return {
                'domain': domain,
                'status': 'no_data',
                'message': f'No metrics available for domain: {domain}'
            }

        # Calculate overall statistics
        total_attempts = domain_stats.total_attempts
        methods = domain_stats.methods

        # Method performance analysis
        method_analysis = {}
        for method_name, method_stats in methods.items():
            method_analysis[method_name] = {
                'success_rate': method_stats.success_rate,
                'average_speed_mbps': method_stats.average_speed,
                'total_attempts': method_stats.total_attempts,
                'performance_rating': method_stats.performance_rating.value,
                'reliability': self._assess_reliability(method_stats),
                'last_success': method_stats.last_success.isoformat() if method_stats.last_success else None,
                'common_errors': method_stats.common_errors[-5:],  # Last 5 errors
                'recommendation': self._get_method_recommendation(method_stats)
            }

        # Find best and worst methods
        best_method = domain_stats.get_best_method()
        worst_method = min(methods.keys(), key=lambda m: methods[m].success_rate) if methods else None

        # Performance trends
        performance_trend = self._analyze_performance_trend(domain_stats)

        return {
            'domain': domain,
            'status': 'analyzed',
            'overview': {
                'total_attempts': total_attempts,
                'methods_tested': len(methods),
                'best_method': best_method,
                'worst_method': worst_method,
                'first_seen': domain_stats.first_seen.isoformat() if domain_stats.first_seen else None,
                'last_activity': domain_stats.last_activity.isoformat() if domain_stats.last_activity else None
            },
            'methods': method_analysis,
            'trends': performance_trend,
            'recommendations': self._get_domain_recommendations(domain_stats),
            'optimization_score': self._calculate_optimization_score(domain_stats)
        }

    def analyze_global_performance(self) -> Dict[str, Any]:
        """Analyze overall system performance across all domains."""
        metrics = self.tracker.metrics

        if not metrics.domains:
            return {
                'status': 'no_data',
                'message': 'No metrics available for analysis'
            }

        # Global statistics
        total_domains = len(metrics.domains)
        total_attempts = sum(domain.total_attempts for domain in metrics.domains.values())

        # Method performance across all domains
        global_method_stats = {}
        for domain_stats in metrics.domains.values():
            for method_name, method_stats in domain_stats.methods.items():
                if method_name not in global_method_stats:
                    global_method_stats[method_name] = {
                        'total_attempts': 0,
                        'successful_attempts': 0,
                        'total_time': 0.0,
                        'total_bytes': 0,
                        'domains_used': 0
                    }

                stats = global_method_stats[method_name]
                stats['total_attempts'] += method_stats.total_attempts
                stats['successful_attempts'] += method_stats.successful_attempts
                stats['total_time'] += method_stats.total_download_time
                stats['total_bytes'] += method_stats.total_bytes_downloaded
                stats['domains_used'] += 1

        # Calculate global method performance
        method_performance = {}
        for method, stats in global_method_stats.items():
            success_rate = stats['successful_attempts'] / stats['total_attempts'] if stats['total_attempts'] > 0 else 0
            avg_speed = (stats['total_bytes'] / (1024 * 1024)) / stats['total_time'] if stats['total_time'] > 0 else 0

            method_performance[method] = {
                'global_success_rate': success_rate,
                'average_speed_mbps': avg_speed,
                'total_attempts': stats['total_attempts'],
                'domains_supported': stats['domains_used'],
                'performance_rating': self._rate_global_performance(success_rate, stats['total_attempts']),
                'reliability_score': self._calculate_reliability_score(success_rate, stats['total_attempts'])
            }

        # Domain analysis
        domain_performance = {}
        for domain, stats in metrics.domains.items():
            best_method = stats.get_best_method()
            domain_performance[domain] = {
                'attempts': stats.total_attempts,
                'best_method': best_method,
                'best_success_rate': stats.methods[best_method].success_rate if best_method else 0,
                'methods_count': len(stats.methods),
                'health_score': self._calculate_domain_health_score(stats)
            }

        # System recommendations
        system_recommendations = self._get_system_recommendations(metrics, method_performance)

        return {
            'status': 'analyzed',
            'overview': {
                'total_domains': total_domains,
                'total_attempts': total_attempts,
                'analysis_date': datetime.now().isoformat(),
                'data_quality': self._assess_data_quality(total_attempts, total_domains)
            },
            'method_performance': method_performance,
            'domain_performance': domain_performance,
            'system_health': self._calculate_system_health(method_performance),
            'recommendations': system_recommendations,
            'trends': self._analyze_global_trends(metrics)
        }

    def generate_optimization_report(self) -> Dict[str, Any]:
        """Generate comprehensive optimization report."""
        global_analysis = self.analyze_global_performance()

        if global_analysis['status'] == 'no_data':
            return global_analysis

        # Find optimization opportunities
        optimization_opportunities = []

        method_performance = global_analysis['method_performance']
        domain_performance = global_analysis['domain_performance']

        # Method optimization opportunities
        for method, perf in method_performance.items():
            if perf['total_attempts'] >= 10:  # Only analyze methods with sufficient data
                if perf['global_success_rate'] < 0.60:
                    optimization_opportunities.append({
                        'type': 'poor_method_performance',
                        'severity': 'high',
                        'method': method,
                        'success_rate': perf['global_success_rate'],
                        'recommendation': f"Consider reducing reliance on {method} (success rate: {perf['global_success_rate']:.1%})"
                    })
                elif perf['global_success_rate'] > 0.90 and perf['domains_supported'] >= 5:
                    optimization_opportunities.append({
                        'type': 'excellent_method_performance',
                        'severity': 'info',
                        'method': method,
                        'success_rate': perf['global_success_rate'],
                        'recommendation': f"Prioritize {method} - excellent performance across {perf['domains_supported']} domains"
                    })

        # Domain optimization opportunities
        for domain, perf in domain_performance.items():
            if perf['attempts'] >= 10:
                if perf['best_success_rate'] < 0.70:
                    optimization_opportunities.append({
                        'type': 'domain_issues',
                        'severity': 'medium',
                        'domain': domain,
                        'best_success_rate': perf['best_success_rate'],
                        'recommendation': f"Investigate {domain} downloads - best method only achieves {perf['best_success_rate']:.1%} success"
                    })

        # Performance benchmarks
        benchmarks = self._generate_performance_benchmarks(method_performance)

        return {
            'status': 'optimized',
            'generated_at': datetime.now().isoformat(),
            'global_analysis': global_analysis,
            'optimization_opportunities': sorted(optimization_opportunities, key=lambda x: x['severity']),
            'benchmarks': benchmarks,
            'action_items': self._generate_action_items(optimization_opportunities),
            'performance_score': self._calculate_overall_performance_score(method_performance)
        }

    def benchmark_methods_for_domain(self, domain: str) -> Dict[str, Any]:
        """
        Generate method benchmark for a specific domain.

        Args:
            domain: Domain to benchmark

        Returns:
            Method comparison and recommendations
        """
        domain_stats = self.tracker.get_domain_stats(domain)
        if not domain_stats:
            return {
                'domain': domain,
                'status': 'no_data',
                'message': f'No data available for domain: {domain}'
            }

        methods = domain_stats.methods

        # Create benchmark comparison
        benchmark_results = []
        for method_name, method_stats in methods.items():
            if method_stats.total_attempts >= 3:  # Only include methods with sufficient attempts
                benchmark_results.append({
                    'method': method_name,
                    'success_rate': method_stats.success_rate,
                    'average_speed_mbps': method_stats.average_speed,
                    'total_attempts': method_stats.total_attempts,
                    'reliability_score': self._calculate_reliability_score(
                        method_stats.success_rate,
                        method_stats.total_attempts
                    ),
                    'performance_rating': method_stats.performance_rating.value,
                    'last_success': method_stats.last_success.isoformat() if method_stats.last_success else None,
                    'recommendation': self._get_method_recommendation(method_stats)
                })

        # Sort by reliability score (combination of success rate and confidence)
        benchmark_results.sort(key=lambda x: x['reliability_score'], reverse=True)

        # Generate recommendations
        if benchmark_results:
            best_method = benchmark_results[0]
            recommendations = [
                f"Primary recommendation: Use {best_method['method']} for {domain} (success rate: {best_method['success_rate']:.1%})"
            ]

            if len(benchmark_results) > 1:
                second_best = benchmark_results[1]
                recommendations.append(
                    f"Fallback recommendation: {second_best['method']} (success rate: {second_best['success_rate']:.1%})"
                )

            # Add specific recommendations based on performance
            for result in benchmark_results:
                if result['success_rate'] < 0.30 and result['total_attempts'] >= 5:
                    recommendations.append(f"Avoid {result['method']} for {domain} - consistently poor performance")

        else:
            recommendations = ["Insufficient data for reliable recommendations"]

        return {
            'domain': domain,
            'status': 'benchmarked',
            'benchmark_results': benchmark_results,
            'recommendations': recommendations,
            'optimal_order': [r['method'] for r in benchmark_results],
            'confidence_level': self._assess_benchmark_confidence(benchmark_results)
        }

    def _assess_reliability(self, method_stats) -> str:
        """Assess method reliability based on stats."""
        if method_stats.total_attempts < 5:
            return "insufficient_data"
        elif method_stats.success_rate >= 0.90:
            return "excellent"
        elif method_stats.success_rate >= 0.75:
            return "good"
        elif method_stats.success_rate >= 0.50:
            return "fair"
        else:
            return "poor"

    def _get_method_recommendation(self, method_stats) -> str:
        """Get recommendation for a method based on its stats."""
        reliability = self._assess_reliability(method_stats)

        if reliability == "insufficient_data":
            return "Need more data to assess"
        elif reliability == "excellent":
            return "Highly recommended - excellent performance"
        elif reliability == "good":
            return "Recommended - reliable performance"
        elif reliability == "fair":
            return "Use with caution - moderate success rate"
        else:
            return "Not recommended - poor performance"

    def _analyze_performance_trend(self, domain_stats) -> Dict[str, Any]:
        """Analyze performance trends for a domain."""
        # This is a simplified trend analysis
        # In a full implementation, you'd track metrics over time bins

        methods = domain_stats.methods
        if not methods:
            return {"status": "no_data"}

        # Check if we have recent activity
        recent_cutoff = datetime.now() - timedelta(days=7)
        recent_activity = any(
            method.last_attempt and method.last_attempt > recent_cutoff
            for method in methods.values()
        )

        # Find dominant method
        best_method = domain_stats.get_best_method()
        if best_method:
            best_stats = methods[best_method]
            dominance = best_stats.total_attempts / domain_stats.total_attempts
        else:
            dominance = 0

        return {
            "status": "analyzed",
            "recent_activity": recent_activity,
            "dominant_method": best_method,
            "method_dominance": dominance,
            "trend_direction": "stable"  # Would be calculated from time-series data
        }

    def _get_domain_recommendations(self, domain_stats) -> List[str]:
        """Generate recommendations for a domain."""
        recommendations = []

        best_method = domain_stats.get_best_method()
        if best_method:
            best_stats = domain_stats.methods[best_method]
            recommendations.append(
                f"Use {best_method} as primary method (success rate: {best_stats.success_rate:.1%})"
            )

            if best_stats.success_rate < 0.80:
                recommendations.append(
                    f"Consider investigating why {best_method} has relatively low success rate"
                )

        method_ranking = domain_stats.get_method_ranking()
        if len(method_ranking) > 1:
            recommendations.append(
                f"Fallback order: {' → '.join(method_ranking[1:3])}"
            )

        return recommendations

    def _calculate_optimization_score(self, domain_stats) -> float:
        """Calculate optimization score for a domain (0-100)."""
        if not domain_stats.methods:
            return 0.0

        best_method = domain_stats.get_best_method()
        if not best_method:
            return 0.0

        best_success_rate = domain_stats.methods[best_method].success_rate
        total_attempts = domain_stats.total_attempts

        # Score based on success rate and data quality
        success_score = best_success_rate * 70  # 70 points for success rate
        data_score = min(total_attempts / 50, 1.0) * 30  # 30 points for data quality

        return success_score + data_score

    def _rate_global_performance(self, success_rate: float, attempts: int) -> str:
        """Rate global performance of a method."""
        if attempts < 10:
            return "insufficient_data"
        elif success_rate >= 0.90:
            return "excellent"
        elif success_rate >= 0.75:
            return "good"
        elif success_rate >= 0.50:
            return "fair"
        else:
            return "poor"

    def _calculate_reliability_score(self, success_rate: float, attempts: int) -> float:
        """Calculate reliability score combining success rate and confidence."""
        if attempts == 0:
            return 0.0

        # Base score from success rate
        base_score = success_rate

        # Confidence multiplier based on number of attempts
        confidence = min(attempts / 20, 1.0)  # Max confidence at 20+ attempts

        return base_score * (0.5 + 0.5 * confidence)  # Scale by confidence

    def _calculate_domain_health_score(self, domain_stats) -> float:
        """Calculate health score for a domain."""
        if not domain_stats.methods:
            return 0.0

        best_method = domain_stats.get_best_method()
        if not best_method:
            return 0.0

        best_success_rate = domain_stats.methods[best_method].success_rate
        return best_success_rate * 100

    def _get_system_recommendations(self, metrics, method_performance) -> List[Dict[str, Any]]:
        """Generate system-wide recommendations."""
        recommendations = []

        # Method recommendations
        best_methods = sorted(
            method_performance.items(),
            key=lambda x: x[1]['reliability_score'],
            reverse=True
        )

        if best_methods:
            best_method, best_perf = best_methods[0]
            if best_perf['total_attempts'] >= 50 and best_perf['global_success_rate'] >= 0.90:
                recommendations.append({
                    'type': 'primary_method',
                    'priority': 'high',
                    'message': f"Prioritize {best_method} system-wide - excellent global performance",
                    'method': best_method,
                    'success_rate': best_perf['global_success_rate']
                })

        # Poor performance warnings
        for method, perf in method_performance.items():
            if perf['total_attempts'] >= 20 and perf['global_success_rate'] < 0.40:
                recommendations.append({
                    'type': 'performance_warning',
                    'priority': 'medium',
                    'message': f"Consider reducing reliance on {method} - poor global performance",
                    'method': method,
                    'success_rate': perf['global_success_rate']
                })

        return recommendations

    def _calculate_system_health(self, method_performance) -> Dict[str, Any]:
        """Calculate overall system health metrics."""
        if not method_performance:
            return {"status": "no_data", "score": 0}

        # Calculate weighted average success rate
        total_attempts = sum(perf['total_attempts'] for perf in method_performance.values())
        if total_attempts == 0:
            return {"status": "no_data", "score": 0}

        weighted_success_rate = sum(
            perf['global_success_rate'] * perf['total_attempts']
            for perf in method_performance.values()
        ) / total_attempts

        # System health score
        health_score = weighted_success_rate * 100

        # Health status
        if health_score >= 85:
            status = "excellent"
        elif health_score >= 70:
            status = "good"
        elif health_score >= 50:
            status = "fair"
        else:
            status = "poor"

        return {
            "status": status,
            "score": health_score,
            "weighted_success_rate": weighted_success_rate,
            "methods_analyzed": len(method_performance)
        }

    def _analyze_global_trends(self, metrics) -> Dict[str, Any]:
        """Analyze global trends across the system."""
        # Simplified trend analysis
        total_domains = len(metrics.domains)
        recent_domains = sum(
            1 for stats in metrics.domains.values()
            if stats.last_activity and stats.last_activity > datetime.now() - timedelta(days=30)
        )

        return {
            "total_domains": total_domains,
            "recently_active_domains": recent_domains,
            "activity_rate": recent_domains / total_domains if total_domains > 0 else 0,
            "trend": "growing" if recent_domains > total_domains * 0.5 else "stable"
        }

    def _assess_data_quality(self, total_attempts: int, total_domains: int) -> str:
        """Assess overall data quality."""
        if total_attempts < 50:
            return "insufficient"
        elif total_attempts < 200:
            return "limited"
        elif total_domains >= 10 and total_attempts >= 500:
            return "excellent"
        else:
            return "good"

    def _generate_performance_benchmarks(self, method_performance) -> Dict[str, Any]:
        """Generate performance benchmarks for comparison."""
        benchmarks = {}

        for method, perf in method_performance.items():
            if perf['total_attempts'] >= 10:
                benchmarks[method] = {
                    'success_rate_benchmark': perf['global_success_rate'],
                    'speed_benchmark_mbps': perf['average_speed_mbps'],
                    'reliability_tier': self._get_reliability_tier(perf['global_success_rate'])
                }

        return benchmarks

    def _get_reliability_tier(self, success_rate: float) -> str:
        """Get reliability tier for benchmarking."""
        if success_rate >= 0.95:
            return "tier_1_excellent"
        elif success_rate >= 0.85:
            return "tier_2_good"
        elif success_rate >= 0.70:
            return "tier_3_acceptable"
        else:
            return "tier_4_problematic"

    def _generate_action_items(self, opportunities) -> List[Dict[str, Any]]:
        """Generate actionable items from optimization opportunities."""
        action_items = []

        high_severity = [opp for opp in opportunities if opp['severity'] == 'high']
        if high_severity:
            action_items.append({
                'priority': 'immediate',
                'action': 'Address high-severity performance issues',
                'details': f"{len(high_severity)} critical issues requiring attention",
                'estimated_impact': 'high'
            })

        medium_severity = [opp for opp in opportunities if opp['severity'] == 'medium']
        if medium_severity:
            action_items.append({
                'priority': 'short_term',
                'action': 'Investigate moderate performance issues',
                'details': f"{len(medium_severity)} issues affecting reliability",
                'estimated_impact': 'medium'
            })

        return action_items

    def _calculate_overall_performance_score(self, method_performance) -> float:
        """Calculate overall performance score for the system."""
        if not method_performance:
            return 0.0

        # Weighted score based on method usage and performance
        total_weight = sum(perf['total_attempts'] for perf in method_performance.values())
        if total_weight == 0:
            return 0.0

        weighted_score = sum(
            perf['global_success_rate'] * perf['total_attempts']
            for perf in method_performance.values()
        ) / total_weight

        return weighted_score * 100

    def _assess_benchmark_confidence(self, benchmark_results) -> str:
        """Assess confidence level in benchmark results."""
        if not benchmark_results:
            return "no_data"

        total_attempts = sum(result['total_attempts'] for result in benchmark_results)

        if total_attempts >= 100:
            return "high"
        elif total_attempts >= 20:
            return "medium"
        else:
            return "low"