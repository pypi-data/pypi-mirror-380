"""
Testing interface module providing the main API functions.

This module provides the primary testing functions that are accessed via ai.testing.
"""

import logging
from typing import Dict, List, Optional, Any

from .core import TestingSuite, TestType, TestResult, TestSuiteResults
from ..core.base import BaseAIProvider


logger = logging.getLogger(__name__)

# Global testing suite instance (set by AIManager)
_current_testing_suite: Optional[TestingSuite] = None


def _get_testing_suite() -> TestingSuite:
    """Get the current testing suite instance."""
    if _current_testing_suite is None:
        raise RuntimeError(
            "Testing suite not initialized. This should be called via AIManager.testing.perform()"
        )
    return _current_testing_suite


def _set_testing_suite(suite: TestingSuite):
    """Set the current testing suite instance (called by AIManager)."""
    global _current_testing_suite
    _current_testing_suite = suite


def perform(
    models: Optional[List[str]] = None,
    test_types: TestType = TestType.BOTH,
    timeout: float = 30.0,
    sequential: bool = True,
    save_results: bool = True
) -> TestSuiteResults:
    """
    Run comprehensive tests on AI provider.

    Args:
        models: List of specific models to test (None for all available real models)
        test_types: Types of tests to run (STATELESS, STATEFUL, or BOTH)
        timeout: Test timeout in seconds
        sequential: Whether to run tests sequentially (safer) or concurrently
        save_results: Whether to append results to persistent log

    Returns:
        TestSuiteResults with complete test outcomes

    Example:
        # Test all models with both test types
        results = ai.testing.perform()

        # Test specific models
        results = ai.testing.perform(
            models=["claude-3-opus-20240229", "claude-3-sonnet-20240229"]
        )

        # Test only stateless functionality
        results = ai.testing.perform(test_types=TestType.STATELESS)

        # Fast concurrent execution (use with caution for rate limits)
        results = ai.testing.perform(sequential=False)
    """
    suite = _get_testing_suite()
    return suite.run_tests(
        models=models,
        test_types=test_types,
        timeout=timeout,
        sequential=sequential,
        save_results=save_results
    )


def get_results() -> List[TestResult]:
    """
    Get all historical test results.

    Returns:
        List of all stored TestResult objects

    Example:
        history = ai.testing.get_results()
        for result in history:
            print(f"{result.model}: {result.success} ({result.duration_seconds:.2f}s)")
    """
    suite = _get_testing_suite()
    return suite.load_historical_results()


def analyze() -> Dict[str, Any]:
    """
    Analyze historical test results and provide insights.

    Returns:
        Dict containing analysis of test patterns and model reliability

    Example:
        analysis = ai.testing.analyze()
        print(f"Overall success rate: {analysis['overall_success_rate']:.1%}")
        print(f"Best performing model: {analysis['best_model']}")
    """
    suite = _get_testing_suite()
    results = suite.load_historical_results()

    if not results:
        return {
            'total_tests': 0,
            'overall_success_rate': 0.0,
            'message': 'No historical test results available'
        }

    # Calculate overall statistics
    total_tests = len(results)
    successful_tests = sum(1 for r in results if r.success)
    overall_success_rate = successful_tests / total_tests if total_tests > 0 else 0.0

    # Model-level analysis
    model_stats = {}
    for result in results:
        model = result.model
        if model not in model_stats:
            model_stats[model] = {
                'total_tests': 0,
                'successful_tests': 0,
                'total_duration': 0.0,
                'test_types': set()
            }

        stats = model_stats[model]
        stats['total_tests'] += 1
        stats['total_duration'] += result.duration_seconds
        stats['test_types'].add(result.test_type)
        if result.success:
            stats['successful_tests'] += 1

    # Calculate derived metrics for each model
    for model, stats in model_stats.items():
        stats['success_rate'] = stats['successful_tests'] / stats['total_tests']
        stats['average_duration'] = stats['total_duration'] / stats['total_tests']
        stats['test_types'] = list(stats['test_types'])

    # Find best and worst performing models
    best_model = max(model_stats.items(), key=lambda x: x[1]['success_rate']) if model_stats else None
    worst_model = min(model_stats.items(), key=lambda x: x[1]['success_rate']) if model_stats else None

    # Test type analysis
    stateless_results = [r for r in results if r.test_type == 'stateless']
    stateful_results = [r for r in results if r.test_type == 'stateful']

    stateless_success_rate = sum(1 for r in stateless_results if r.success) / len(stateless_results) if stateless_results else 0.0
    stateful_success_rate = sum(1 for r in stateful_results if r.success) / len(stateful_results) if stateful_results else 0.0

    # Recent performance (last 50 tests)
    recent_results = results[-50:] if len(results) > 50 else results
    recent_success_rate = sum(1 for r in recent_results if r.success) / len(recent_results) if recent_results else 0.0

    # Provider analysis
    provider_stats = {}
    for result in results:
        provider = result.provider
        if provider not in provider_stats:
            provider_stats[provider] = {'total_tests': 0, 'successful_tests': 0}

        provider_stats[provider]['total_tests'] += 1
        if result.success:
            provider_stats[provider]['successful_tests'] += 1

    for provider, stats in provider_stats.items():
        stats['success_rate'] = stats['successful_tests'] / stats['total_tests']

    return {
        # Overall statistics
        'total_tests': total_tests,
        'successful_tests': successful_tests,
        'overall_success_rate': overall_success_rate,
        'recent_success_rate': recent_success_rate,

        # Model analysis
        'model_stats': model_stats,
        'best_model': best_model[0] if best_model else None,
        'best_model_success_rate': best_model[1]['success_rate'] if best_model else 0.0,
        'worst_model': worst_model[0] if worst_model else None,
        'worst_model_success_rate': worst_model[1]['success_rate'] if worst_model else 0.0,

        # Test type analysis
        'stateless_tests': len(stateless_results),
        'stateless_success_rate': stateless_success_rate,
        'stateful_tests': len(stateful_results),
        'stateful_success_rate': stateful_success_rate,

        # Provider analysis
        'provider_stats': provider_stats,

        # Recommendations
        'recommendations': _generate_recommendations(model_stats, stateless_success_rate, stateful_success_rate)
    }


def clear_results(confirm: bool = False) -> bool:
    """
    Clear all historical test results.

    Args:
        confirm: Must be True to actually clear results (safety measure)

    Returns:
        bool: True if results were cleared successfully

    Example:
        # This will only log a warning
        ai.testing.clear_results()

        # This will actually clear the results
        success = ai.testing.clear_results(confirm=True)
    """
    suite = _get_testing_suite()
    return suite.clear_results(confirm=confirm)


def _generate_recommendations(
    model_stats: Dict[str, Dict[str, Any]],
    stateless_success_rate: float,
    stateful_success_rate: float
) -> List[str]:
    """Generate actionable recommendations based on test analysis."""
    recommendations = []

    if not model_stats:
        return ["Run tests first with ai.testing.perform() to get recommendations"]

    # Model reliability recommendations
    reliable_models = [
        model for model, stats in model_stats.items()
        if stats['success_rate'] >= 0.95 and stats['total_tests'] >= 3
    ]

    unreliable_models = [
        model for model, stats in model_stats.items()
        if stats['success_rate'] < 0.8 and stats['total_tests'] >= 3
    ]

    if reliable_models:
        recommendations.append(
            f"Recommended reliable models: {', '.join(reliable_models[:3])}"
        )

    if unreliable_models:
        recommendations.append(
            f"Consider avoiding: {', '.join(unreliable_models[:3])} (low success rate)"
        )

    # Test type recommendations
    if stateless_success_rate > 0 and stateful_success_rate > 0:
        if stateless_success_rate > stateful_success_rate + 0.1:
            recommendations.append(
                "Stateful tests have lower success rate - check conversation context handling"
            )
        elif stateful_success_rate > stateless_success_rate + 0.1:
            recommendations.append(
                "Stateless tests have lower success rate - check basic request handling"
            )

    # Performance recommendations
    fast_models = [
        model for model, stats in model_stats.items()
        if stats['average_duration'] < 2.0 and stats['success_rate'] > 0.8
    ]

    if fast_models:
        recommendations.append(
            f"Fastest reliable models: {', '.join(fast_models[:2])}"
        )

    # General recommendations
    total_tests = sum(stats['total_tests'] for stats in model_stats.values())
    if total_tests < 10:
        recommendations.append(
            "Run more tests for better reliability analysis (recommendation: 10+ tests per model)"
        )

    return recommendations