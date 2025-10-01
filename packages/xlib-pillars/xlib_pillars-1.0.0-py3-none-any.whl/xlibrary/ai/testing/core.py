"""
Core testing framework components for AI provider validation.

Defines test types, result structures, and the main testing suite.
"""

import logging
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any, Union
import json
import os

from ..core.base import BaseAIProvider
from ..core.models import Message
from ..core.exceptions import AIError


logger = logging.getLogger(__name__)


class TestType(Enum):
    """Test execution types."""
    STATELESS = "stateless"
    STATEFUL = "stateful"
    BOTH = "both"


@dataclass
class TestResult:
    """Individual test result with comprehensive metadata."""

    # Core test identification
    test_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    model: str = ""
    provider: str = ""
    test_type: str = ""  # "stateless" or "stateful"

    # Test execution results
    success: bool = False
    duration_seconds: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

    # Error information
    error_message: Optional[str] = None
    error_type: Optional[str] = None

    # Rich metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert test result to dictionary for serialization."""
        return {
            'test_id': self.test_id,
            'model': self.model,
            'provider': self.provider,
            'test_type': self.test_type,
            'success': self.success,
            'duration_seconds': self.duration_seconds,
            'timestamp': self.timestamp.isoformat(),
            'error_message': self.error_message,
            'error_type': self.error_type,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TestResult':
        """Create test result from dictionary."""
        result = cls(
            test_id=data.get('test_id', str(uuid.uuid4())),
            model=data.get('model', ''),
            provider=data.get('provider', ''),
            test_type=data.get('test_type', ''),
            success=data.get('success', False),
            duration_seconds=data.get('duration_seconds', 0.0),
            error_message=data.get('error_message'),
            error_type=data.get('error_type'),
            metadata=data.get('metadata', {})
        )

        # Parse timestamp
        timestamp_str = data.get('timestamp')
        if timestamp_str:
            try:
                result.timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                pass

        return result


@dataclass
class TestSuiteResults:
    """Complete test suite results with analytics."""

    # Core results
    results: List[TestResult] = field(default_factory=list)
    total_tests: int = 0
    successful_tests: int = 0
    failed_tests: int = 0
    total_duration_seconds: float = 0.0

    # Execution metadata
    execution_mode: str = "sequential"  # "sequential" or "concurrent"
    timestamp: datetime = field(default_factory=datetime.now)

    # Analytics
    success_rate: float = 0.0
    average_duration: float = 0.0
    providers_tested: List[str] = field(default_factory=list)
    models_tested: List[str] = field(default_factory=list)

    def calculate_analytics(self):
        """Calculate analytics from test results."""
        if not self.results:
            return

        self.total_tests = len(self.results)
        self.successful_tests = sum(1 for r in self.results if r.success)
        self.failed_tests = self.total_tests - self.successful_tests
        self.total_duration_seconds = sum(r.duration_seconds for r in self.results)

        self.success_rate = self.successful_tests / self.total_tests if self.total_tests > 0 else 0.0
        self.average_duration = self.total_duration_seconds / self.total_tests if self.total_tests > 0 else 0.0

        self.providers_tested = list(set(r.provider for r in self.results))
        self.models_tested = list(set(r.model for r in self.results))

    def to_dict(self) -> Dict[str, Any]:
        """Convert results to dictionary."""
        return {
            'results': [r.to_dict() for r in self.results],
            'total_tests': self.total_tests,
            'successful_tests': self.successful_tests,
            'failed_tests': self.failed_tests,
            'total_duration_seconds': self.total_duration_seconds,
            'execution_mode': self.execution_mode,
            'timestamp': self.timestamp.isoformat(),
            'success_rate': self.success_rate,
            'average_duration': self.average_duration,
            'providers_tested': self.providers_tested,
            'models_tested': self.models_tested
        }


class TestingSuite:
    """
    Main testing suite for AI provider validation.

    Provides comprehensive testing capabilities including stateless/stateful
    tests, concurrent execution, and persistent result storage.
    """

    # Standard test prompts
    STATELESS_TEST_PROMPT = "Respond with exactly: 'Test successful'"
    STATEFUL_TEST_PROMPTS = [
        "Remember this number: 42",
        "What number did I ask you to remember?"
    ]

    def __init__(self, provider: BaseAIProvider, results_file: Optional[str] = None):
        """
        Initialize testing suite.

        Args:
            provider: AI provider instance to test
            results_file: Optional file path for persistent result storage
        """
        self.provider = provider
        self.results_file = results_file or os.path.expanduser("~/.xlibrary/test_results.json")

        # Ensure results directory exists
        os.makedirs(os.path.dirname(self.results_file), exist_ok=True)

    def _get_provider_name(self) -> str:
        """Get provider name from the provider instance."""
        class_name = self.provider.__class__.__name__
        # Convert MockProvider -> mock, ClaudeProvider -> claude, etc.
        if class_name.endswith('Provider'):
            return class_name[:-8].lower()
        return class_name.lower()

    def run_stateless_test(self, model: str, timeout: float = 30.0) -> TestResult:
        """
        Run a stateless test on a specific model.

        Args:
            model: Model name to test
            timeout: Test timeout in seconds

        Returns:
            TestResult with test outcome
        """
        result = TestResult(
            model=model,
            provider=self._get_provider_name(),
            test_type="stateless"
        )

        start_time = time.time()

        try:
            # Temporarily set model
            original_model = self.provider.model
            self.provider.model = model

            # Create test message
            messages = [Message(role="user", content=self.STATELESS_TEST_PROMPT)]

            # Make request with timeout
            response = self.provider.complete(messages=messages, timeout=timeout)

            # Validate response
            expected = "Test successful"
            success = expected.lower() in response.content.lower()

            result.success = success
            if not success:
                result.error_message = f"Expected '{expected}', got '{response.content[:100]}'"

            # Collect metadata
            result.metadata = {
                'tokens_used': response.tokens_used,
                'cost_estimate': response.cost_estimate,
                'latency_ms': response.latency_ms,
                'execution_mode': 'stateless',
                'response_length': len(response.content),
                'expected_response': expected,
                'actual_response': response.content[:200]  # Truncated for storage
            }

            # Restore original model
            self.provider.model = original_model

        except Exception as e:
            result.success = False
            result.error_message = str(e)
            result.error_type = type(e).__name__

            logger.error(f"Stateless test failed for {model}: {e}")

        result.duration_seconds = time.time() - start_time
        return result

    def run_stateful_test(self, model: str, timeout: float = 60.0) -> TestResult:
        """
        Run a stateful test on a specific model.

        Args:
            model: Model name to test
            timeout: Test timeout in seconds

        Returns:
            TestResult with test outcome
        """
        result = TestResult(
            model=model,
            provider=self._get_provider_name(),
            test_type="stateful"
        )

        start_time = time.time()

        try:
            # Temporarily set model
            original_model = self.provider.model
            self.provider.model = model

            # Create conversation with both messages
            messages = [
                Message(role="user", content=self.STATEFUL_TEST_PROMPTS[0]),
                Message(role="assistant", content="I'll remember the number 42."),
                Message(role="user", content=self.STATEFUL_TEST_PROMPTS[1])
            ]

            # Make request with conversation context
            response = self.provider.complete(messages=messages, timeout=timeout)

            # Validate that response contains the remembered number
            success = "42" in response.content

            result.success = success
            if not success:
                result.error_message = f"Failed to remember number 42, got: '{response.content[:100]}'"

            # Collect metadata
            result.metadata = {
                'tokens_used': response.tokens_used,
                'cost_estimate': response.cost_estimate,
                'latency_ms': response.latency_ms,
                'execution_mode': 'stateful',
                'response_length': len(response.content),
                'conversation_length': len(messages),
                'expected_content': '42',
                'actual_response': response.content[:200]  # Truncated for storage
            }

            # Restore original model
            self.provider.model = original_model

        except Exception as e:
            result.success = False
            result.error_message = str(e)
            result.error_type = type(e).__name__

            logger.error(f"Stateful test failed for {model}: {e}")

        result.duration_seconds = time.time() - start_time
        return result

    def run_tests(
        self,
        models: Optional[List[str]] = None,
        test_types: TestType = TestType.BOTH,
        timeout: float = 30.0,
        sequential: bool = True,
        save_results: bool = True
    ) -> TestSuiteResults:
        """
        Run comprehensive tests on specified models.

        Args:
            models: List of models to test (None for all available)
            test_types: Types of tests to run
            timeout: Test timeout in seconds
            sequential: Whether to run tests sequentially (safer) or concurrently
            save_results: Whether to append results to persistent storage

        Returns:
            TestSuiteResults with complete test outcomes
        """
        # Get models to test
        if models is None:
            available_models = self.provider.get_models(real=True, aliases=False)
            models = list(available_models.keys())

        if not models:
            logger.warning("No models available for testing")
            return TestSuiteResults()

        # Determine test types to run
        run_stateless = test_types in [TestType.STATELESS, TestType.BOTH]
        run_stateful = test_types in [TestType.STATEFUL, TestType.BOTH]

        # Create test plan
        test_plan = []
        for model in models:
            if run_stateless:
                test_plan.append(('stateless', model))
            if run_stateful:
                test_plan.append(('stateful', model))

        logger.info(f"Running {len(test_plan)} tests on {len(models)} models")

        # Execute tests
        results = TestSuiteResults(
            execution_mode="sequential" if sequential else "concurrent"
        )

        if sequential:
            results.results = self._run_tests_sequential(test_plan, timeout)
        else:
            results.results = self._run_tests_concurrent(test_plan, timeout)

        # Calculate analytics
        results.calculate_analytics()

        # Save results if requested
        if save_results:
            self._save_results(results.results)

        logger.info(f"Testing complete: {results.successful_tests}/{results.total_tests} passed "
                   f"({results.success_rate:.1%}) in {results.total_duration_seconds:.1f}s")

        return results

    def _run_tests_sequential(self, test_plan: List[tuple], timeout: float) -> List[TestResult]:
        """Run tests sequentially."""
        results = []

        for test_type, model in test_plan:
            if test_type == 'stateless':
                result = self.run_stateless_test(model, timeout)
            else:
                result = self.run_stateful_test(model, timeout)

            results.append(result)

            # Brief pause between tests to respect rate limits
            time.sleep(0.5)

        return results

    def _run_tests_concurrent(self, test_plan: List[tuple], timeout: float, max_workers: int = 3) -> List[TestResult]:
        """Run tests concurrently (use with caution for rate limits)."""
        results = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_test = {}

            for test_type, model in test_plan:
                if test_type == 'stateless':
                    future = executor.submit(self.run_stateless_test, model, timeout)
                else:
                    future = executor.submit(self.run_stateful_test, model, timeout)

                future_to_test[future] = (test_type, model)

            for future in as_completed(future_to_test):
                test_type, model = future_to_test[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    # Create failed result
                    failed_result = TestResult(
                        model=model,
                        provider=self._get_provider_name(),
                        test_type=test_type,
                        success=False,
                        error_message=str(e),
                        error_type=type(e).__name__
                    )
                    results.append(failed_result)
                    logger.error(f"Concurrent test execution failed: {e}")

        return results

    def _save_results(self, results: List[TestResult]):
        """Save test results to persistent storage."""
        try:
            # Load existing results
            existing_results = []
            if os.path.exists(self.results_file) and os.path.getsize(self.results_file) > 0:
                try:
                    with open(self.results_file, 'r') as f:
                        data = json.load(f)
                        existing_results = [TestResult.from_dict(r) for r in data.get('results', [])]
                except (json.JSONDecodeError, KeyError):
                    # File exists but is corrupted/empty, start fresh
                    logger.warning(f"Results file {self.results_file} corrupted, starting fresh")
                    existing_results = []

            # Append new results
            all_results = existing_results + results

            # Keep only last 1000 results to prevent unbounded growth
            if len(all_results) > 1000:
                all_results = all_results[-1000:]

            # Save back to file
            data = {
                'results': [r.to_dict() for r in all_results],
                'last_updated': datetime.now().isoformat(),
                'total_results': len(all_results)
            }

            with open(self.results_file, 'w') as f:
                json.dump(data, f, indent=2)

            logger.info(f"Saved {len(results)} new test results to {self.results_file}")

        except Exception as e:
            logger.error(f"Failed to save test results: {e}")

    def load_historical_results(self) -> List[TestResult]:
        """Load all historical test results."""
        try:
            if os.path.exists(self.results_file) and os.path.getsize(self.results_file) > 0:
                with open(self.results_file, 'r') as f:
                    data = json.load(f)
                    return [TestResult.from_dict(r) for r in data.get('results', [])]
        except (json.JSONDecodeError, KeyError, FileNotFoundError) as e:
            logger.error(f"Failed to load historical results: {e}")

        return []

    def clear_results(self, confirm: bool = False) -> bool:
        """
        Clear all historical test results.

        Args:
            confirm: Must be True to actually clear results

        Returns:
            bool: True if results were cleared
        """
        if not confirm:
            logger.warning("clear_results() requires confirm=True to actually clear results")
            return False

        try:
            if os.path.exists(self.results_file):
                os.remove(self.results_file)
                logger.info("Cleared all historical test results")
                return True
        except Exception as e:
            logger.error(f"Failed to clear results: {e}")

        return False