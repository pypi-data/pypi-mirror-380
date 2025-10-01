"""
Rate limiting strategies and algorithms.

Implements token bucket algorithm, exponential backoff, request queuing,
and other rate limiting strategies for AI provider management.
"""

import logging
import random
import threading
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, Callable, Any, Deque
import math


logger = logging.getLogger(__name__)


class BackoffStrategy(Enum):
    """Backoff strategies for rate limiting."""
    NONE = "none"                # No backoff
    LINEAR = "linear"            # Linear backoff (1s, 2s, 3s, ...)
    EXPONENTIAL = "exponential"  # Exponential backoff (1s, 2s, 4s, 8s, ...)
    FIBONACCI = "fibonacci"      # Fibonacci backoff (1s, 1s, 2s, 3s, 5s, ...)


class TokenBucket:
    """
    Token bucket algorithm implementation for rate limiting.

    The token bucket algorithm allows for burst traffic while maintaining
    an average rate limit over time.
    """

    def __init__(
        self,
        capacity: int,
        refill_rate: float,
        refill_period: float = 1.0,
        initial_tokens: Optional[int] = None
    ):
        """
        Initialize token bucket.

        Args:
            capacity: Maximum number of tokens the bucket can hold
            refill_rate: Number of tokens added per refill period
            refill_period: Time in seconds between refills
            initial_tokens: Initial number of tokens (defaults to capacity)
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.refill_period = refill_period
        self.tokens = initial_tokens if initial_tokens is not None else capacity
        self.last_refill = time.time()
        self._lock = threading.Lock()

        logger.debug(f"TokenBucket initialized: capacity={capacity}, rate={refill_rate}/{refill_period}s")

    def consume(self, tokens: int = 1) -> bool:
        """
        Attempt to consume tokens from the bucket.

        Args:
            tokens: Number of tokens to consume

        Returns:
            bool: True if tokens were consumed, False if insufficient tokens
        """
        with self._lock:
            self._refill()

            if self.tokens >= tokens:
                self.tokens -= tokens
                logger.debug(f"Consumed {tokens} tokens, {self.tokens} remaining")
                return True
            else:
                logger.debug(f"Insufficient tokens: need {tokens}, have {self.tokens}")
                return False

    def peek(self, tokens: int = 1) -> bool:
        """
        Check if tokens are available without consuming them.

        Args:
            tokens: Number of tokens to check for

        Returns:
            bool: True if tokens are available
        """
        with self._lock:
            self._refill()
            return self.tokens >= tokens

    def time_until_available(self, tokens: int = 1) -> float:
        """
        Calculate time until specified tokens will be available.

        Args:
            tokens: Number of tokens needed

        Returns:
            float: Seconds until tokens will be available (0 if already available)
        """
        with self._lock:
            self._refill()

            if self.tokens >= tokens:
                return 0.0

            tokens_needed = tokens - self.tokens
            time_needed = (tokens_needed / self.refill_rate) * self.refill_period

            return time_needed

    def _refill(self):
        """Refill tokens based on elapsed time."""
        now = time.time()
        elapsed = now - self.last_refill

        if elapsed >= self.refill_period:
            # Calculate tokens to add
            refill_periods = elapsed / self.refill_period
            tokens_to_add = int(refill_periods * self.refill_rate)

            if tokens_to_add > 0:
                self.tokens = min(self.capacity, self.tokens + tokens_to_add)
                self.last_refill = now
                logger.debug(f"Refilled {tokens_to_add} tokens, total: {self.tokens}")

    def get_status(self) -> dict:
        """Get current bucket status."""
        with self._lock:
            self._refill()
            return {
                'capacity': self.capacity,
                'current_tokens': self.tokens,
                'refill_rate': self.refill_rate,
                'refill_period': self.refill_period,
                'utilization': 1.0 - (self.tokens / self.capacity)
            }

    def reset(self, tokens: Optional[int] = None):
        """Reset bucket to specified token count."""
        with self._lock:
            self.tokens = tokens if tokens is not None else self.capacity
            self.last_refill = time.time()
            logger.debug(f"TokenBucket reset to {self.tokens} tokens")


@dataclass
class QueuedRequest:
    """Represents a queued request waiting for rate limit clearance."""
    request_id: str
    tokens_required: int
    queued_at: datetime
    priority: int = 0  # Lower numbers = higher priority
    callback: Optional[Callable] = None
    timeout: Optional[float] = None


class RequestQueue:
    """
    Request queue for managing rate-limited requests.

    Implements priority queuing with timeout handling and fair scheduling.
    """

    def __init__(
        self,
        max_size: int = 1000,
        default_timeout: float = 300.0,  # 5 minutes
        enable_priorities: bool = True
    ):
        """
        Initialize request queue.

        Args:
            max_size: Maximum number of queued requests
            default_timeout: Default timeout for queued requests
            enable_priorities: Whether to enable priority scheduling
        """
        self.max_size = max_size
        self.default_timeout = default_timeout
        self.enable_priorities = enable_priorities

        self._queue: Deque[QueuedRequest] = deque()
        self._lock = threading.Lock()

        logger.debug(f"RequestQueue initialized: max_size={max_size}, timeout={default_timeout}s")

    def enqueue(
        self,
        request_id: str,
        tokens_required: int = 1,
        priority: int = 0,
        timeout: Optional[float] = None,
        callback: Optional[Callable] = None
    ) -> bool:
        """
        Add request to queue.

        Args:
            request_id: Unique identifier for the request
            tokens_required: Number of tokens required
            priority: Request priority (lower = higher priority)
            timeout: Request timeout in seconds
            callback: Optional callback for completion/timeout

        Returns:
            bool: True if queued successfully, False if queue is full
        """
        with self._lock:
            if len(self._queue) >= self.max_size:
                logger.warning(f"Request queue full, rejecting request {request_id}")
                return False

            request = QueuedRequest(
                request_id=request_id,
                tokens_required=tokens_required,
                queued_at=datetime.now(),
                priority=priority,
                callback=callback,
                timeout=timeout or self.default_timeout
            )

            # Insert based on priority if enabled
            if self.enable_priorities and priority > 0:
                # Find insertion point for priority
                insert_index = 0
                for i, queued_req in enumerate(self._queue):
                    if queued_req.priority > priority:
                        insert_index = i
                        break
                    insert_index = i + 1

                # Convert deque to list, insert, convert back
                queue_list = list(self._queue)
                queue_list.insert(insert_index, request)
                self._queue = deque(queue_list)
            else:
                # Simple FIFO
                self._queue.append(request)

            logger.debug(f"Queued request {request_id} (priority={priority}, tokens={tokens_required})")
            return True

    def dequeue(self) -> Optional[QueuedRequest]:
        """
        Remove and return next request from queue.

        Returns:
            QueuedRequest: Next request, or None if queue is empty
        """
        with self._lock:
            if not self._queue:
                return None

            # Remove expired requests from front
            self._cleanup_expired()

            if self._queue:
                request = self._queue.popleft()
                logger.debug(f"Dequeued request {request.request_id}")
                return request

            return None

    def peek(self) -> Optional[QueuedRequest]:
        """
        Look at next request without removing it.

        Returns:
            QueuedRequest: Next request, or None if queue is empty
        """
        with self._lock:
            self._cleanup_expired()
            return self._queue[0] if self._queue else None

    def remove(self, request_id: str) -> bool:
        """
        Remove specific request from queue.

        Args:
            request_id: ID of request to remove

        Returns:
            bool: True if request was found and removed
        """
        with self._lock:
            for i, request in enumerate(self._queue):
                if request.request_id == request_id:
                    del self._queue[i]
                    logger.debug(f"Removed request {request_id} from queue")
                    return True
            return False

    def _cleanup_expired(self):
        """Remove expired requests from queue."""
        now = datetime.now()
        expired_count = 0

        # Remove expired requests from front
        while self._queue:
            request = self._queue[0]
            elapsed = (now - request.queued_at).total_seconds()

            if elapsed > request.timeout:
                expired_request = self._queue.popleft()
                expired_count += 1

                # Call timeout callback if provided
                if expired_request.callback:
                    try:
                        expired_request.callback(expired_request, "timeout")
                    except Exception as e:
                        logger.error(f"Error in timeout callback: {e}")
            else:
                break  # Queue is ordered, so no more expired requests

        if expired_count > 0:
            logger.debug(f"Cleaned up {expired_count} expired requests")

    def size(self) -> int:
        """Get current queue size."""
        with self._lock:
            self._cleanup_expired()
            return len(self._queue)

    def is_full(self) -> bool:
        """Check if queue is full."""
        return self.size() >= self.max_size

    def clear(self):
        """Clear all queued requests."""
        with self._lock:
            cleared_count = len(self._queue)
            self._queue.clear()
            logger.info(f"Cleared {cleared_count} requests from queue")

    def get_stats(self) -> dict:
        """Get queue statistics."""
        with self._lock:
            self._cleanup_expired()

            if not self._queue:
                return {
                    'size': 0,
                    'max_size': self.max_size,
                    'utilization': 0.0,
                    'oldest_request_age': 0.0,
                    'average_priority': 0.0
                }

            now = datetime.now()
            ages = [(now - req.queued_at).total_seconds() for req in self._queue]
            priorities = [req.priority for req in self._queue]

            return {
                'size': len(self._queue),
                'max_size': self.max_size,
                'utilization': len(self._queue) / self.max_size,
                'oldest_request_age': max(ages) if ages else 0.0,
                'average_age': sum(ages) / len(ages) if ages else 0.0,
                'average_priority': sum(priorities) / len(priorities) if priorities else 0.0
            }


class BackoffCalculator:
    """
    Calculate backoff delays using various strategies.

    Implements multiple backoff algorithms with jitter support to prevent
    thundering herd problems.
    """

    def __init__(
        self,
        strategy: BackoffStrategy = BackoffStrategy.EXPONENTIAL,
        base_delay: float = 1.0,
        max_delay: float = 300.0,
        jitter: bool = True,
        jitter_factor: float = 0.1
    ):
        """
        Initialize backoff calculator.

        Args:
            strategy: Backoff strategy to use
            base_delay: Base delay in seconds
            max_delay: Maximum delay in seconds
            jitter: Whether to add random jitter
            jitter_factor: Jitter factor (0.0 to 1.0)
        """
        self.strategy = strategy
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter
        self.jitter_factor = jitter_factor

        # Fibonacci sequence cache
        self._fibonacci_cache = [1, 1]

        logger.debug(f"BackoffCalculator initialized: {strategy.value}, base={base_delay}s, max={max_delay}s")

    def calculate(self, attempt: int) -> float:
        """
        Calculate backoff delay for given attempt.

        Args:
            attempt: Attempt number (0-based)

        Returns:
            float: Delay in seconds
        """
        if self.strategy == BackoffStrategy.NONE:
            delay = 0.0
        elif self.strategy == BackoffStrategy.LINEAR:
            delay = self.base_delay * (attempt + 1)
        elif self.strategy == BackoffStrategy.EXPONENTIAL:
            delay = self.base_delay * (2 ** attempt)
        elif self.strategy == BackoffStrategy.FIBONACCI:
            delay = self.base_delay * self._get_fibonacci(attempt + 1)
        else:
            delay = self.base_delay

        # Apply maximum delay limit
        delay = min(delay, self.max_delay)

        # Add jitter if enabled
        if self.jitter and delay > 0:
            jitter_amount = delay * self.jitter_factor
            delay += random.uniform(-jitter_amount, jitter_amount)
            delay = max(0.0, delay)  # Ensure non-negative

        logger.debug(f"Calculated backoff for attempt {attempt}: {delay:.2f}s")
        return delay

    def _get_fibonacci(self, n: int) -> int:
        """Get nth Fibonacci number with caching."""
        while len(self._fibonacci_cache) <= n:
            next_fib = self._fibonacci_cache[-1] + self._fibonacci_cache[-2]
            self._fibonacci_cache.append(next_fib)

        return self._fibonacci_cache[n]

    def reset(self):
        """Reset any internal state."""
        # Nothing to reset for current strategies
        pass