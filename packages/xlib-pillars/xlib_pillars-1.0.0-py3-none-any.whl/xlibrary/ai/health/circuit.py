"""
Circuit Breaker implementation for AI provider health management.

Implements the Circuit Breaker pattern to prevent cascading failures and
provide automatic recovery for failing AI providers.
"""

import logging
import time
import threading
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, Callable, Any
from dataclasses import dataclass


logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"        # Normal operation, requests allowed
    OPEN = "open"           # Circuit is open, requests blocked
    HALF_OPEN = "half_open"  # Testing mode, limited requests allowed


@dataclass
class CircuitBreakerConfig:
    """Configuration for circuit breaker behavior."""
    failure_threshold: int = 5          # Number of failures before opening
    recovery_timeout: int = 60          # Seconds before attempting recovery
    success_threshold: int = 3          # Successes needed to close circuit
    timeout: float = 30.0              # Request timeout in seconds

    # Advanced configuration
    half_open_max_calls: int = 3       # Max calls allowed in half-open state
    reset_timeout: int = 300           # Full reset after this many seconds
    failure_rate_threshold: float = 0.5  # Failure rate to trigger opening


class CircuitBreaker:
    """
    Circuit Breaker implementation for AI provider calls.

    Prevents cascading failures by monitoring call success/failure rates
    and automatically blocking requests when providers are unhealthy.
    """

    def __init__(
        self,
        name: str,
        config: Optional[CircuitBreakerConfig] = None
    ):
        """
        Initialize circuit breaker.

        Args:
            name: Unique name for this circuit breaker
            config: Configuration options
        """
        self.name = name
        self.config = config or CircuitBreakerConfig()

        # State management
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._success_count = 0
        self._last_failure_time: Optional[datetime] = None
        self._next_attempt_time: Optional[datetime] = None

        # Statistics
        self._total_calls = 0
        self._total_failures = 0
        self._total_successes = 0
        self._half_open_calls = 0

        # Thread safety
        self._lock = threading.RLock()

        logger.info(f"CircuitBreaker '{name}' initialized with {self.config.failure_threshold} failure threshold")

    @property
    def state(self) -> CircuitState:
        """Get current circuit state."""
        with self._lock:
            return self._state

    @property
    def is_available(self) -> bool:
        """Check if circuit is available for calls."""
        with self._lock:
            now = datetime.now()

            if self._state == CircuitState.CLOSED:
                return True
            elif self._state == CircuitState.HALF_OPEN:
                return self._half_open_calls < self.config.half_open_max_calls
            else:  # OPEN
                # Check if it's time to try recovery
                if self._next_attempt_time and now >= self._next_attempt_time:
                    self._transition_to_half_open()
                    return True
                return False

    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute a function call through the circuit breaker.

        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Function result

        Raises:
            CircuitBreakerOpenError: If circuit is open
            Exception: Any exception raised by the function
        """
        if not self.is_available:
            self._record_blocked_call()
            raise CircuitBreakerOpenError(f"Circuit breaker '{self.name}' is OPEN")

        with self._lock:
            self._total_calls += 1
            if self._state == CircuitState.HALF_OPEN:
                self._half_open_calls += 1

        start_time = time.time()

        try:
            # Execute the function with timeout
            result = func(*args, **kwargs)

            # Record success
            self._record_success()

            return result

        except Exception as e:
            # Record failure
            self._record_failure(e)
            raise

    def _record_success(self):
        """Record a successful call."""
        with self._lock:
            self._success_count += 1
            self._total_successes += 1
            self._failure_count = 0  # Reset failure count on success

            logger.debug(f"CircuitBreaker '{self.name}' recorded success")

            # State transitions
            if self._state == CircuitState.HALF_OPEN:
                if self._success_count >= self.config.success_threshold:
                    self._transition_to_closed()
            elif self._state == CircuitState.CLOSED:
                # Already closed, just continue
                pass

    def _record_failure(self, exception: Exception):
        """Record a failed call."""
        with self._lock:
            self._failure_count += 1
            self._total_failures += 1
            self._last_failure_time = datetime.now()

            logger.warning(f"CircuitBreaker '{self.name}' recorded failure: {type(exception).__name__}")

            # State transitions
            if self._state == CircuitState.CLOSED:
                if self._failure_count >= self.config.failure_threshold:
                    self._transition_to_open()
            elif self._state == CircuitState.HALF_OPEN:
                # Any failure in half-open immediately opens the circuit
                self._transition_to_open()

    def _record_blocked_call(self):
        """Record a call that was blocked by the circuit breaker."""
        with self._lock:
            logger.debug(f"CircuitBreaker '{self.name}' blocked call (state: {self._state.value})")

    def _transition_to_open(self):
        """Transition circuit to OPEN state."""
        with self._lock:
            old_state = self._state
            self._state = CircuitState.OPEN
            self._next_attempt_time = datetime.now() + timedelta(seconds=self.config.recovery_timeout)
            self._half_open_calls = 0

            logger.warning(f"CircuitBreaker '{self.name}' opened (failures: {self._failure_count})")

    def _transition_to_half_open(self):
        """Transition circuit to HALF_OPEN state."""
        with self._lock:
            old_state = self._state
            self._state = CircuitState.HALF_OPEN
            self._success_count = 0
            self._half_open_calls = 0

            logger.info(f"CircuitBreaker '{self.name}' entering half-open state")

    def _transition_to_closed(self):
        """Transition circuit to CLOSED state."""
        with self._lock:
            old_state = self._state
            self._state = CircuitState.CLOSED
            self._failure_count = 0
            self._success_count = 0
            self._next_attempt_time = None
            self._half_open_calls = 0

            logger.info(f"CircuitBreaker '{self.name}' closed (recovered)")

    def force_open(self):
        """Manually force circuit to OPEN state."""
        with self._lock:
            self._transition_to_open()
            logger.info(f"CircuitBreaker '{self.name}' manually opened")

    def force_close(self):
        """Manually force circuit to CLOSED state."""
        with self._lock:
            self._transition_to_closed()
            logger.info(f"CircuitBreaker '{self.name}' manually closed")

    def reset(self):
        """Reset circuit breaker to initial state."""
        with self._lock:
            self._state = CircuitState.CLOSED
            self._failure_count = 0
            self._success_count = 0
            self._last_failure_time = None
            self._next_attempt_time = None

            # Reset statistics
            self._total_calls = 0
            self._total_failures = 0
            self._total_successes = 0
            self._half_open_calls = 0

            logger.info(f"CircuitBreaker '{self.name}' reset")

    def get_stats(self) -> dict:
        """Get circuit breaker statistics."""
        with self._lock:
            failure_rate = (
                self._total_failures / self._total_calls
                if self._total_calls > 0 else 0.0
            )

            return {
                'name': self.name,
                'state': self._state.value,
                'is_available': self.is_available,
                'total_calls': self._total_calls,
                'total_successes': self._total_successes,
                'total_failures': self._total_failures,
                'failure_rate': failure_rate,
                'current_failure_count': self._failure_count,
                'current_success_count': self._success_count,
                'last_failure_time': self._last_failure_time.isoformat() if self._last_failure_time else None,
                'next_attempt_time': self._next_attempt_time.isoformat() if self._next_attempt_time else None,
                'config': {
                    'failure_threshold': self.config.failure_threshold,
                    'recovery_timeout': self.config.recovery_timeout,
                    'success_threshold': self.config.success_threshold,
                    'timeout': self.config.timeout
                }
            }

    def __repr__(self) -> str:
        """String representation."""
        with self._lock:
            return (f"CircuitBreaker(name='{self.name}', state={self._state.value}, "
                   f"failures={self._failure_count}, available={self.is_available})")


class CircuitBreakerOpenError(Exception):
    """Raised when circuit breaker is open and blocking calls."""
    pass