"""
Core health checking system for AI providers.

Provides comprehensive health monitoring, automatic failover, and integration
with testing and metrics systems.
"""

import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Any, Callable, Union
from collections import defaultdict, deque

from ..core.base import BaseAIProvider
from ..core.exceptions import AIError
from ..testing.core import TestingSuite, TestType, TestResult
from .circuit import CircuitBreaker, CircuitBreakerConfig, CircuitState, CircuitBreakerOpenError


logger = logging.getLogger(__name__)


class HealthState(Enum):
    """Health states for providers."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


@dataclass
class ProviderHealth:
    """Health status for a specific provider."""
    provider_name: str
    state: HealthState = HealthState.UNKNOWN
    last_check: Optional[datetime] = None
    response_time_ms: float = 0.0
    success_rate: float = 0.0
    error_count: int = 0
    consecutive_failures: int = 0
    last_error: Optional[str] = None
    circuit_breaker_state: CircuitState = CircuitState.CLOSED
    available: bool = True

    # Historical data
    recent_checks: List[bool] = field(default_factory=list)  # Last N check results
    avg_response_time: float = 0.0

    def update_from_test_result(self, result: TestResult):
        """Update health status from a test result."""
        self.last_check = result.timestamp
        self.response_time_ms = result.duration_seconds * 1000

        # Update recent checks (keep last 10)
        if len(self.recent_checks) >= 10:
            self.recent_checks.pop(0)
        self.recent_checks.append(result.success)

        # Calculate success rate
        if self.recent_checks:
            self.success_rate = sum(self.recent_checks) / len(self.recent_checks)

        # Update consecutive failures
        if result.success:
            self.consecutive_failures = 0
        else:
            self.consecutive_failures += 1
            self.error_count += 1
            self.last_error = result.error_message

        # Update health state based on metrics
        self._update_health_state()

    def _update_health_state(self):
        """Update health state based on current metrics."""
        if self.consecutive_failures >= 5:
            self.state = HealthState.UNHEALTHY
        elif self.consecutive_failures >= 3 or self.success_rate < 0.8:
            self.state = HealthState.DEGRADED
        elif self.success_rate >= 0.9:
            self.state = HealthState.HEALTHY
        else:
            self.state = HealthState.UNKNOWN

        # Update availability
        self.available = self.state in [HealthState.HEALTHY, HealthState.DEGRADED]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'provider_name': self.provider_name,
            'state': self.state.value,
            'available': self.available,
            'last_check': self.last_check.isoformat() if self.last_check else None,
            'response_time_ms': self.response_time_ms,
            'avg_response_time': self.avg_response_time,
            'success_rate': self.success_rate,
            'error_count': self.error_count,
            'consecutive_failures': self.consecutive_failures,
            'last_error': self.last_error,
            'circuit_breaker_state': self.circuit_breaker_state.value,
            'recent_checks_count': len(self.recent_checks)
        }


@dataclass
class HealthStatus:
    """Overall health status for all monitored providers."""
    overall_healthy: bool = True
    healthy_providers: List[str] = field(default_factory=list)
    unhealthy_providers: List[str] = field(default_factory=list)
    degraded_providers: List[str] = field(default_factory=list)
    provider_details: Dict[str, ProviderHealth] = field(default_factory=dict)
    last_check: Optional[datetime] = None
    total_providers: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            'overall_healthy': self.overall_healthy,
            'healthy_providers': self.healthy_providers,
            'unhealthy_providers': self.unhealthy_providers,
            'degraded_providers': self.degraded_providers,
            'last_check': self.last_check.isoformat() if self.last_check else None,
            'total_providers': self.total_providers,
            'details': {name: health.to_dict() for name, health in self.provider_details.items()}
        }


class HealthChecker:
    """
    Comprehensive health checker for AI providers.

    Monitors provider health using the testing subsystem, implements circuit breaker
    patterns, and provides automatic failover capabilities.
    """

    def __init__(
        self,
        providers: Optional[List[str]] = None,
        check_interval_seconds: int = 30,
        timeout_seconds: int = 10,
        enable_circuit_breakers: bool = True,
        circuit_breaker_config: Optional[CircuitBreakerConfig] = None,
        max_workers: int = 3
    ):
        """
        Initialize health checker.

        Args:
            providers: List of provider names to monitor
            check_interval_seconds: Time between health checks
            timeout_seconds: Timeout for individual health checks
            enable_circuit_breakers: Whether to use circuit breakers
            circuit_breaker_config: Configuration for circuit breakers
            max_workers: Maximum concurrent health check threads
        """
        self.providers = providers or []
        self.check_interval = check_interval_seconds
        self.timeout = timeout_seconds
        self.enable_circuit_breakers = enable_circuit_breakers
        self.max_workers = max_workers

        # Health tracking
        self._provider_health: Dict[str, ProviderHealth] = {}
        self._circuit_breakers: Dict[str, CircuitBreaker] = {}

        # Provider instances for testing
        self._provider_instances: Dict[str, BaseAIProvider] = {}
        self._testing_suites: Dict[str, TestingSuite] = {}

        # Monitoring state
        self._monitoring_active = False
        self._monitoring_thread: Optional[threading.Thread] = None
        self._lock = threading.RLock()

        # Initialize components
        self._initialize_circuit_breakers(circuit_breaker_config)
        self._initialize_provider_health()

        logger.info(f"HealthChecker initialized for providers: {self.providers}")

    def _initialize_circuit_breakers(self, config: Optional[CircuitBreakerConfig]):
        """Initialize circuit breakers for each provider."""
        if not self.enable_circuit_breakers:
            return

        config = config or CircuitBreakerConfig()

        for provider in self.providers:
            self._circuit_breakers[provider] = CircuitBreaker(
                name=f"{provider}_circuit",
                config=config
            )

    def _initialize_provider_health(self):
        """Initialize health tracking for each provider."""
        for provider in self.providers:
            self._provider_health[provider] = ProviderHealth(provider_name=provider)

    def register_provider(self, provider_name: str, provider_instance: BaseAIProvider):
        """
        Register a provider instance for health monitoring.

        Args:
            provider_name: Name of the provider
            provider_instance: Provider instance to monitor
        """
        with self._lock:
            self._provider_instances[provider_name] = provider_instance
            self._testing_suites[provider_name] = TestingSuite(provider_instance)

            if provider_name not in self.providers:
                self.providers.append(provider_name)
                self._provider_health[provider_name] = ProviderHealth(provider_name=provider_name)

                if self.enable_circuit_breakers:
                    self._circuit_breakers[provider_name] = CircuitBreaker(
                        name=f"{provider_name}_circuit"
                    )

            logger.info(f"Registered provider for health monitoring: {provider_name}")

    def start_monitoring(self):
        """Start background health monitoring."""
        with self._lock:
            if self._monitoring_active:
                logger.warning("Health monitoring already active")
                return

            self._monitoring_active = True
            self._monitoring_thread = threading.Thread(
                target=self._monitoring_loop,
                name="HealthMonitor",
                daemon=True
            )
            self._monitoring_thread.start()

            logger.info("Health monitoring started")

    def stop_monitoring(self):
        """Stop background health monitoring."""
        with self._lock:
            if not self._monitoring_active:
                return

            self._monitoring_active = False

            if self._monitoring_thread and self._monitoring_thread.is_alive():
                self._monitoring_thread.join(timeout=5.0)

            logger.info("Health monitoring stopped")

    def _monitoring_loop(self):
        """Background monitoring loop."""
        logger.info("Health monitoring loop started")

        while self._monitoring_active:
            try:
                self.check_all_providers()
                time.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"Health monitoring loop error: {e}")
                time.sleep(min(self.check_interval, 10))  # Shorter retry on errors

        logger.info("Health monitoring loop stopped")

    def check_all_providers(self) -> HealthStatus:
        """
        Check health of all registered providers.

        Returns:
            HealthStatus with overall health information
        """
        if not self._provider_instances:
            logger.warning("No provider instances registered for health checking")
            return HealthStatus()

        logger.debug(f"Starting health check for {len(self._provider_instances)} providers")

        # Run health checks concurrently
        health_results = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_provider = {
                executor.submit(self.check_provider, provider_name): provider_name
                for provider_name in self._provider_instances.keys()
            }

            for future in as_completed(future_to_provider):
                provider_name = future_to_provider[future]
                try:
                    health_results[provider_name] = future.result()
                except Exception as e:
                    logger.error(f"Health check failed for {provider_name}: {e}")
                    # Create failed health result
                    health_results[provider_name] = self._create_failed_health_result(provider_name, str(e))

        # Update overall status
        return self._build_health_status(health_results)

    def check_provider(self, provider_name: str) -> ProviderHealth:
        """
        Check health of a specific provider.

        Args:
            provider_name: Name of provider to check

        Returns:
            ProviderHealth with current status
        """
        if provider_name not in self._provider_instances:
            raise ValueError(f"Provider {provider_name} not registered")

        logger.debug(f"Checking health for provider: {provider_name}")

        # Get or create health tracking
        if provider_name not in self._provider_health:
            self._provider_health[provider_name] = ProviderHealth(provider_name=provider_name)

        health = self._provider_health[provider_name]
        testing_suite = self._testing_suites[provider_name]

        try:
            # Use circuit breaker if enabled
            if self.enable_circuit_breakers and provider_name in self._circuit_breakers:
                circuit_breaker = self._circuit_breakers[provider_name]
                health.circuit_breaker_state = circuit_breaker.state

                if not circuit_breaker.is_available:
                    logger.debug(f"Circuit breaker open for {provider_name}, skipping health check")
                    health.available = False
                    return health

                # Run health check through circuit breaker
                def health_check():
                    return testing_suite.run_stateless_test("latest", timeout=self.timeout)

                result = circuit_breaker.call(health_check)
            else:
                # Direct health check
                result = testing_suite.run_stateless_test("latest", timeout=self.timeout)

            # Update health from test result
            health.update_from_test_result(result)

            logger.debug(f"Health check completed for {provider_name}: {health.state.value}")

        except CircuitBreakerOpenError:
            # Circuit breaker blocked the call
            health.available = False
            health.state = HealthState.UNHEALTHY
            logger.debug(f"Circuit breaker blocked health check for {provider_name}")

        except Exception as e:
            # Health check failed
            logger.warning(f"Health check failed for {provider_name}: {e}")

            # Create fake failed result
            failed_result = TestResult(
                model="latest",
                provider=provider_name,
                test_type="stateless",
                success=False,
                error_message=str(e),
                error_type=type(e).__name__,
                timestamp=datetime.now()
            )

            health.update_from_test_result(failed_result)

        return health

    def _create_failed_health_result(self, provider_name: str, error_message: str) -> ProviderHealth:
        """Create a failed health result."""
        health = self._provider_health.get(provider_name, ProviderHealth(provider_name=provider_name))
        health.state = HealthState.UNHEALTHY
        health.available = False
        health.last_error = error_message
        health.consecutive_failures += 1
        health.error_count += 1
        health.last_check = datetime.now()
        return health

    def _build_health_status(self, health_results: Dict[str, ProviderHealth]) -> HealthStatus:
        """Build overall health status from individual results."""
        with self._lock:
            # Update stored health results
            self._provider_health.update(health_results)

            # Categorize providers
            healthy = []
            unhealthy = []
            degraded = []

            for provider_name, health in health_results.items():
                if health.state == HealthState.HEALTHY:
                    healthy.append(provider_name)
                elif health.state == HealthState.UNHEALTHY:
                    unhealthy.append(provider_name)
                elif health.state == HealthState.DEGRADED:
                    degraded.append(provider_name)

            # Overall health is good if at least one provider is healthy
            overall_healthy = len(healthy) > 0 and len(unhealthy) == 0

            status = HealthStatus(
                overall_healthy=overall_healthy,
                healthy_providers=healthy,
                unhealthy_providers=unhealthy,
                degraded_providers=degraded,
                provider_details=dict(self._provider_health),
                last_check=datetime.now(),
                total_providers=len(health_results)
            )

            return status

    def get_status(self) -> HealthStatus:
        """
        Get current health status without running new checks.

        Returns:
            HealthStatus with last known health information
        """
        with self._lock:
            return self._build_health_status(self._provider_health)

    def get_healthy_providers(self) -> List[str]:
        """Get list of currently healthy providers."""
        status = self.get_status()
        return status.healthy_providers

    def get_circuit_breaker_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get circuit breaker statistics for all providers."""
        if not self.enable_circuit_breakers:
            return {}

        with self._lock:
            return {
                provider: breaker.get_stats()
                for provider, breaker in self._circuit_breakers.items()
            }

    def reset_circuit_breaker(self, provider_name: str):
        """Reset circuit breaker for a specific provider."""
        if not self.enable_circuit_breakers or provider_name not in self._circuit_breakers:
            return

        with self._lock:
            self._circuit_breakers[provider_name].reset()
            logger.info(f"Reset circuit breaker for provider: {provider_name}")

    def reset_all_circuit_breakers(self):
        """Reset all circuit breakers."""
        if not self.enable_circuit_breakers:
            return

        with self._lock:
            for provider_name, breaker in self._circuit_breakers.items():
                breaker.reset()

            logger.info("Reset all circuit breakers")

    def __enter__(self):
        """Context manager entry."""
        self.start_monitoring()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_monitoring()

    def __repr__(self) -> str:
        """String representation."""
        return f"HealthChecker(providers={len(self.providers)}, monitoring={self._monitoring_active})"