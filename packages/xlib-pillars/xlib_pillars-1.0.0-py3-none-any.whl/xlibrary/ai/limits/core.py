"""
Core rate limiting implementation for AI providers.

Combines token bucket algorithms, request queuing, exponential backoff,
and provider-specific limits into a unified rate limiting system.
"""

import logging
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional, List, Callable, Any

from .strategies import TokenBucket, RequestQueue, BackoffCalculator, BackoffStrategy
from .providers import get_provider_limits, ProviderLimits


logger = logging.getLogger(__name__)


class RateLimitResult(Enum):
    """Results of rate limit checking."""
    ALLOWED = "allowed"          # Request can proceed immediately
    QUEUED = "queued"           # Request was queued for later processing
    REJECTED = "rejected"       # Request was rejected (queue full, etc.)
    BACKOFF = "backoff"         # Request should be retried with backoff


@dataclass
class RateLimitConfig:
    """Configuration for rate limiting behavior."""

    # Token bucket settings
    enabled: bool = True
    requests_per_minute: Optional[int] = None
    tokens_per_minute: Optional[int] = None
    concurrent_requests: Optional[int] = None
    burst_allowance: Optional[int] = None

    # Request queuing
    enable_queuing: bool = True
    max_queue_size: int = 1000
    queue_timeout: float = 300.0  # 5 minutes
    enable_priorities: bool = True

    # Backoff strategy
    backoff_strategy: BackoffStrategy = BackoffStrategy.EXPONENTIAL
    base_delay: float = 1.0
    max_delay: float = 300.0
    enable_jitter: bool = True
    jitter_factor: float = 0.1

    # Provider integration
    use_provider_defaults: bool = True
    provider_tier: Optional[str] = None

    # Advanced features
    adaptive_limits: bool = False
    failure_threshold: int = 5
    success_reset_threshold: int = 10

    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return {
            'enabled': self.enabled,
            'requests_per_minute': self.requests_per_minute,
            'tokens_per_minute': self.tokens_per_minute,
            'concurrent_requests': self.concurrent_requests,
            'burst_allowance': self.burst_allowance,
            'enable_queuing': self.enable_queuing,
            'max_queue_size': self.max_queue_size,
            'queue_timeout': self.queue_timeout,
            'enable_priorities': self.enable_priorities,
            'backoff_strategy': self.backoff_strategy.value,
            'base_delay': self.base_delay,
            'max_delay': self.max_delay,
            'enable_jitter': self.enable_jitter,
            'jitter_factor': self.jitter_factor,
            'use_provider_defaults': self.use_provider_defaults,
            'provider_tier': self.provider_tier,
            'adaptive_limits': self.adaptive_limits,
            'failure_threshold': self.failure_threshold,
            'success_reset_threshold': self.success_reset_threshold
        }


class RateLimiter:
    """
    Comprehensive rate limiting system for AI providers.

    Combines token bucket algorithm, request queuing, exponential backoff,
    and provider-specific limits into a unified system with optional
    adaptive behavior based on success/failure rates.
    """

    def __init__(
        self,
        provider: str,
        config: Optional[RateLimitConfig] = None,
        provider_tier: Optional[str] = None,
        metrics=None,
        health_checker=None
    ):
        """
        Initialize rate limiter for a specific provider.

        Args:
            provider: Provider name (claude, openai, deepseek, mock)
            config: Rate limiting configuration (uses defaults if None)
            provider_tier: Specific provider tier (free, pro, team, etc.)
            metrics: Optional metrics instance for recording rate limit events
            health_checker: Optional health checker for rate limit health status
        """
        self.provider = provider
        self.config = config or RateLimitConfig()
        self.provider_tier = provider_tier or self.config.provider_tier
        self.metrics = metrics
        self.health_checker = health_checker

        # Get provider-specific limits
        self.provider_limits: Optional[ProviderLimits] = None
        if self.config.use_provider_defaults:
            self.provider_limits = get_provider_limits(provider, self.provider_tier)
            if self.provider_limits:
                logger.info(f"Using provider limits for {provider}/{self.provider_tier}")
            else:
                logger.warning(f"No provider limits found for {provider}/{self.provider_tier}")

        # Initialize rate limiting components
        self._initialize_components()

        # Tracking state
        self._consecutive_failures = 0
        self._consecutive_successes = 0
        self._last_failure_time: Optional[datetime] = None
        self._request_count = 0
        self._lock = threading.Lock()

        # Active requests tracking
        self._active_requests: Dict[str, datetime] = {}

        logger.info(f"RateLimiter initialized for {provider} (enabled: {self.config.enabled})")

    def _initialize_components(self):
        """Initialize token buckets, queues, and backoff calculator."""
        if not self.config.enabled:
            self._request_bucket = None
            self._token_bucket = None
            self._request_queue = None
            self._backoff_calculator = None
            return

        # Determine limits (config overrides provider defaults)
        requests_per_min = self.config.requests_per_minute
        tokens_per_min = self.config.tokens_per_minute
        concurrent_requests = self.config.concurrent_requests
        burst_allowance = self.config.burst_allowance

        if self.provider_limits and self.config.use_provider_defaults:
            requests_per_min = requests_per_min or self.provider_limits.requests_per_minute
            tokens_per_min = tokens_per_min or self.provider_limits.tokens_per_minute
            concurrent_requests = concurrent_requests or self.provider_limits.concurrent_requests
            burst_allowance = burst_allowance or self.provider_limits.burst_allowance

        # Default fallbacks
        requests_per_min = requests_per_min or 60
        tokens_per_min = tokens_per_min or 60000
        concurrent_requests = concurrent_requests or 10
        burst_allowance = burst_allowance or 10

        # Request rate limiting (requests per minute)
        self._request_bucket = TokenBucket(
            capacity=requests_per_min + burst_allowance,
            refill_rate=requests_per_min / 60,  # Convert to per-second
            refill_period=1.0,
            initial_tokens=requests_per_min
        )

        # Token rate limiting (tokens per minute)
        self._token_bucket = TokenBucket(
            capacity=tokens_per_min + (burst_allowance * 100),  # Allow some token burst
            refill_rate=tokens_per_min / 60,  # Convert to per-second
            refill_period=1.0,
            initial_tokens=tokens_per_min
        )

        # Request queuing
        if self.config.enable_queuing:
            self._request_queue = RequestQueue(
                max_size=self.config.max_queue_size,
                default_timeout=self.config.queue_timeout,
                enable_priorities=self.config.enable_priorities
            )
        else:
            self._request_queue = None

        # Backoff calculator
        self._backoff_calculator = BackoffCalculator(
            strategy=self.config.backoff_strategy,
            base_delay=self.config.base_delay,
            max_delay=self.config.max_delay,
            jitter=self.config.enable_jitter,
            jitter_factor=self.config.jitter_factor
        )

        logger.debug(f"Rate limiter components initialized: "
                    f"{requests_per_min} req/min, {tokens_per_min} tokens/min, "
                    f"{concurrent_requests} concurrent")

    def check_rate_limit(
        self,
        request_id: str,
        tokens_required: int = 1,
        priority: int = 0
    ) -> RateLimitResult:
        """
        Check if a request can proceed based on rate limits.

        Args:
            request_id: Unique identifier for the request
            tokens_required: Number of tokens the request will consume
            priority: Request priority (lower = higher priority)

        Returns:
            RateLimitResult indicating if request is allowed, queued, or rejected
        """
        if not self.config.enabled:
            return RateLimitResult.ALLOWED

        # Record rate limit check attempt
        if self.metrics:
            self.metrics.record_custom_metric(
                name="rate_limit_check",
                value=1,
                labels={"provider": self.provider, "result": "checking"}
            )

        with self._lock:
            # Check if we're in backoff period due to failures
            if self._should_backoff():
                if self.metrics:
                    self.metrics.record_custom_metric(
                        name="rate_limit_check",
                        value=1,
                        labels={"provider": self.provider, "result": "backoff"}
                    )
                return RateLimitResult.BACKOFF

            # Check concurrent request limit
            if not self._check_concurrent_limit():
                if self.config.enable_queuing and self._request_queue:
                    if self._request_queue.enqueue(request_id, tokens_required, priority):
                        return RateLimitResult.QUEUED
                    else:
                        return RateLimitResult.REJECTED
                else:
                    return RateLimitResult.REJECTED

            # Check token bucket (if tokens are required)
            if tokens_required > 0 and self._token_bucket:
                if not self._token_bucket.peek(tokens_required):
                    if self.config.enable_queuing and self._request_queue:
                        if self._request_queue.enqueue(request_id, tokens_required, priority):
                            return RateLimitResult.QUEUED
                        else:
                            return RateLimitResult.REJECTED
                    else:
                        return RateLimitResult.REJECTED

            # Check request bucket
            if self._request_bucket and not self._request_bucket.peek(1):
                if self.config.enable_queuing and self._request_queue:
                    if self._request_queue.enqueue(request_id, tokens_required, priority):
                        return RateLimitResult.QUEUED
                    else:
                        return RateLimitResult.REJECTED
                else:
                    return RateLimitResult.REJECTED

            # Record allowed result
            if self.metrics:
                self.metrics.record_custom_metric(
                    name="rate_limit_check",
                    value=1,
                    labels={"provider": self.provider, "result": "allowed"}
                )

            return RateLimitResult.ALLOWED

    def consume_tokens(
        self,
        request_id: str,
        tokens_used: int = 1
    ) -> bool:
        """
        Consume tokens for a request that's been approved.

        Args:
            request_id: Request identifier
            tokens_used: Number of tokens to consume

        Returns:
            bool: True if tokens were consumed successfully
        """
        if not self.config.enabled:
            return True

        with self._lock:
            # Consume from request bucket
            request_consumed = True
            if self._request_bucket:
                request_consumed = self._request_bucket.consume(1)

            # Consume from token bucket
            token_consumed = True
            if tokens_used > 0 and self._token_bucket:
                token_consumed = self._token_bucket.consume(tokens_used)

            if request_consumed and token_consumed:
                # Track active request
                self._active_requests[request_id] = datetime.now()
                self._request_count += 1
                logger.debug(f"Tokens consumed for {request_id}: {tokens_used}")
                return True
            else:
                logger.warning(f"Failed to consume tokens for {request_id}")
                return False

    def release_request(self, request_id: str, success: bool = True):
        """
        Release a completed request and update success/failure tracking.

        Args:
            request_id: Request identifier
            success: Whether the request completed successfully
        """
        with self._lock:
            # Remove from active requests
            if request_id in self._active_requests:
                del self._active_requests[request_id]

            # Update success/failure tracking for adaptive behavior
            if self.config.adaptive_limits:
                if success:
                    self._consecutive_successes += 1
                    self._consecutive_failures = 0

                    # Consider relaxing limits after sustained success
                    if self._consecutive_successes >= self.config.success_reset_threshold:
                        self._maybe_relax_limits()
                else:
                    self._consecutive_failures += 1
                    self._consecutive_successes = 0
                    self._last_failure_time = datetime.now()

                    # Consider tightening limits after failures
                    if self._consecutive_failures >= self.config.failure_threshold:
                        self._maybe_tighten_limits()

            logger.debug(f"Released request {request_id} (success: {success})")

    def process_queue(self, max_items: int = 10) -> List[str]:
        """
        Process queued requests that can now proceed.

        Args:
            max_items: Maximum number of items to process

        Returns:
            List of request IDs that can now proceed
        """
        if not self.config.enabled or not self.config.enable_queuing or not self._request_queue:
            return []

        processed_requests = []

        with self._lock:
            for _ in range(max_items):
                request = self._request_queue.peek()
                if not request:
                    break

                # Check if this request can now proceed
                result = self.check_rate_limit(
                    request.request_id,
                    request.tokens_required,
                    request.priority
                )

                if result == RateLimitResult.ALLOWED:
                    # Remove from queue and allow to proceed
                    self._request_queue.dequeue()
                    processed_requests.append(request.request_id)
                else:
                    # Can't process this request yet, stop processing
                    break

        if processed_requests:
            logger.debug(f"Processed {len(processed_requests)} queued requests")

        return processed_requests

    def get_backoff_delay(self) -> float:
        """
        Get the current backoff delay based on failure count.

        Returns:
            float: Delay in seconds (0 if no backoff needed)
        """
        if not self.config.enabled or not self._backoff_calculator:
            return 0.0

        with self._lock:
            if self._consecutive_failures > 0:
                return self._backoff_calculator.calculate(self._consecutive_failures - 1)
            return 0.0

    def _should_backoff(self) -> bool:
        """Check if we should be in backoff mode due to failures."""
        if not self.config.adaptive_limits or self._consecutive_failures == 0:
            return False

        if not self._last_failure_time:
            return False

        backoff_delay = self.get_backoff_delay()
        if backoff_delay == 0:
            return False

        elapsed = (datetime.now() - self._last_failure_time).total_seconds()
        return elapsed < backoff_delay

    def _check_concurrent_limit(self) -> bool:
        """Check if we're under the concurrent request limit."""
        if not self.provider_limits:
            return True

        concurrent_limit = self.provider_limits.concurrent_requests
        current_concurrent = len(self._active_requests)

        return current_concurrent < concurrent_limit

    def _maybe_relax_limits(self):
        """Adaptively relax rate limits after sustained success."""
        if not self.config.adaptive_limits:
            return

        # Could increase bucket capacity or refill rates here
        # For now, just reset the success counter
        self._consecutive_successes = 0
        logger.debug("Considering limit relaxation after sustained success")

    def _maybe_tighten_limits(self):
        """Adaptively tighten rate limits after repeated failures."""
        if not self.config.adaptive_limits:
            return

        # Could decrease bucket capacity or refill rates here
        # For now, just log the event
        logger.debug("Considering limit tightening after repeated failures")

    def get_status(self) -> Dict[str, Any]:
        """
        Get current rate limiter status.

        Returns:
            Dict with current status information
        """
        if not self.config.enabled:
            return {
                'enabled': False,
                'provider': self.provider,
                'provider_tier': self.provider_tier
            }

        with self._lock:
            status = {
                'enabled': True,
                'provider': self.provider,
                'provider_tier': self.provider_tier,
                'request_count': self._request_count,
                'consecutive_failures': self._consecutive_failures,
                'consecutive_successes': self._consecutive_successes,
                'active_requests': len(self._active_requests),
                'backoff_delay': self.get_backoff_delay(),
                'in_backoff': self._should_backoff()
            }

            # Token bucket status
            if self._request_bucket:
                bucket_status = self._request_bucket.get_status()
                status['request_bucket'] = bucket_status

            if self._token_bucket:
                bucket_status = self._token_bucket.get_status()
                status['token_bucket'] = bucket_status

            # Queue status
            if self._request_queue:
                queue_stats = self._request_queue.get_stats()
                status['queue'] = queue_stats

            return status

    def reset(self):
        """Reset rate limiter state."""
        with self._lock:
            self._consecutive_failures = 0
            self._consecutive_successes = 0
            self._last_failure_time = None
            self._request_count = 0
            self._active_requests.clear()

            if self._request_bucket:
                self._request_bucket.reset()

            if self._token_bucket:
                self._token_bucket.reset()

            if self._request_queue:
                self._request_queue.clear()

            if self._backoff_calculator:
                self._backoff_calculator.reset()

            logger.info(f"Rate limiter reset for {self.provider}")

    def update_config(self, config: RateLimitConfig):
        """
        Update rate limiter configuration.

        Args:
            config: New configuration to apply
        """
        with self._lock:
            self.config = config

            # Re-initialize components with new config
            self._initialize_components()

            logger.info(f"Rate limiter configuration updated for {self.provider}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - cleanup resources."""
        if self._request_queue:
            self._request_queue.clear()

        with self._lock:
            self._active_requests.clear()