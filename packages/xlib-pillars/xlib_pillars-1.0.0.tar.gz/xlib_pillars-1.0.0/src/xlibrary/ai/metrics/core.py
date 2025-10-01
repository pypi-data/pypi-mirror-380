"""
Core metrics collection system for AI provider usage tracking.

Provides lightweight, thread-safe metrics collection with multiple backend options.
"""

import logging
import time
import threading
from datetime import datetime, timezone
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any, Union
from collections import defaultdict, deque

from .backends import BaseBackend, MemoryBackend


logger = logging.getLogger(__name__)


class MetricType(Enum):
    """Types of metrics that can be collected."""
    COUNTER = "counter"        # Monotonic increasing values (requests, tokens)
    GAUGE = "gauge"           # Current value that can go up/down (active conversations)
    HISTOGRAM = "histogram"   # Distribution of values (response times, costs)
    TIMER = "timer"          # Alias for histogram focused on durations


@dataclass
class MetricPoint:
    """Individual metric measurement point."""
    name: str
    value: float
    metric_type: MetricType
    labels: Dict[str, str] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'name': self.name,
            'value': self.value,
            'type': self.metric_type.value,
            'labels': self.labels,
            'timestamp': self.timestamp.isoformat()
        }


@dataclass
class MetricSummary:
    """Summary statistics for a metric over time."""
    name: str
    count: int = 0
    sum: float = 0.0
    min: float = float('inf')
    max: float = float('-inf')
    avg: float = 0.0
    last_value: float = 0.0
    last_updated: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def update(self, value: float, timestamp: Optional[datetime] = None):
        """Update summary with new value."""
        self.count += 1
        self.sum += value
        self.min = min(self.min, value)
        self.max = max(self.max, value)
        self.avg = self.sum / self.count
        self.last_value = value
        self.last_updated = timestamp or datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'name': self.name,
            'count': self.count,
            'sum': self.sum,
            'min': self.min if self.min != float('inf') else 0.0,
            'max': self.max if self.max != float('-inf') else 0.0,
            'avg': self.avg,
            'last_value': self.last_value,
            'last_updated': self.last_updated.isoformat()
        }


class AIMetrics:
    """
    Main metrics collection system for AI provider usage.

    Provides lightweight, thread-safe metrics collection with multiple backend options.
    Automatically tracks AI usage patterns, performance, and costs.
    """

    # Standard metric names
    REQUESTS_TOTAL = "xlibrary_ai_requests_total"
    REQUEST_DURATION = "xlibrary_ai_request_duration_seconds"
    TOKENS_USED_TOTAL = "xlibrary_ai_tokens_used_total"
    COST_TOTAL = "xlibrary_ai_cost_total"
    ERRORS_TOTAL = "xlibrary_ai_errors_total"
    CONVERSATIONS_ACTIVE = "xlibrary_ai_conversations_active"
    STREAMING_CHUNKS_TOTAL = "xlibrary_ai_streaming_chunks_total"
    ARTIFACTS_GENERATED_TOTAL = "xlibrary_ai_artifacts_generated_total"

    def __init__(
        self,
        backend: Optional[Union[str, BaseBackend]] = None,
        enabled: bool = True,
        max_history_size: int = 10000,
        **backend_kwargs
    ):
        """
        Initialize AI metrics collection.

        Args:
            backend: Backend for metric storage ("memory", "file", "statsd", or backend instance)
            enabled: Whether metrics collection is enabled
            max_history_size: Maximum number of metric points to keep in history
            **backend_kwargs: Additional arguments for backend initialization
        """
        self.enabled = enabled
        self.max_history_size = max_history_size

        # Thread safety
        self._lock = threading.RLock()

        # Initialize backend
        if isinstance(backend, BaseBackend):
            self.backend = backend
        elif backend == "file":
            from .backends import FileBackend
            self.backend = FileBackend(**backend_kwargs)
        elif backend == "statsd":
            from .backends import StatsDBackend
            self.backend = StatsDBackend(**backend_kwargs)
        elif backend == "null":
            from .backends import NullBackend
            self.backend = NullBackend()
        else:
            # Default to memory backend
            self.backend = MemoryBackend(**backend_kwargs)

        # Internal metric storage
        self._counters: Dict[str, float] = defaultdict(float)
        self._gauges: Dict[str, float] = defaultdict(float)
        self._histograms: Dict[str, deque] = defaultdict(lambda: deque(maxlen=self.max_history_size))
        self._summaries: Dict[str, MetricSummary] = defaultdict(lambda: MetricSummary(""))

        # Metric metadata for labels
        self._labels: Dict[str, Dict[str, str]] = defaultdict(dict)

        logger.info(f"AIMetrics initialized with {self.backend.__class__.__name__} backend")

    def _get_metric_key(self, name: str, labels: Optional[Dict[str, str]] = None) -> str:
        """Generate unique key for metric with labels."""
        if not labels:
            return name

        label_str = ",".join(f"{k}={v}" for k, v in sorted(labels.items()))
        return f"{name}{{{label_str}}}"

    def record(
        self,
        name: str,
        value: float,
        metric_type: MetricType,
        labels: Optional[Dict[str, str]] = None,
        timestamp: Optional[datetime] = None
    ):
        """
        Record a metric value.

        Args:
            name: Metric name
            value: Metric value
            metric_type: Type of metric (counter, gauge, histogram, timer)
            labels: Optional labels for the metric
            timestamp: Optional timestamp (defaults to now)
        """
        if not self.enabled:
            return

        labels = labels or {}
        timestamp = timestamp or datetime.now(timezone.utc)
        metric_key = self._get_metric_key(name, labels)

        with self._lock:
            # Store labels for this metric
            if labels:
                self._labels[metric_key] = labels

            # Update internal storage based on type
            if metric_type == MetricType.COUNTER:
                self._counters[metric_key] += value
            elif metric_type == MetricType.GAUGE:
                self._gauges[metric_key] = value
            elif metric_type in [MetricType.HISTOGRAM, MetricType.TIMER]:
                self._histograms[metric_key].append((value, timestamp))
                # Update summary statistics
                if metric_key not in self._summaries:
                    self._summaries[metric_key] = MetricSummary(name)
                self._summaries[metric_key].update(value, timestamp)

            # Send to backend
            metric_point = MetricPoint(
                name=name,
                value=value,
                metric_type=metric_type,
                labels=labels,
                timestamp=timestamp
            )

            try:
                self.backend.record(metric_point)
            except Exception as e:
                logger.warning(f"Failed to record metric to backend: {e}")

    def increment(self, name: str, value: float = 1.0, labels: Optional[Dict[str, str]] = None):
        """Increment a counter metric."""
        self.record(name, value, MetricType.COUNTER, labels)

    def set_gauge(self, name: str, value: float, labels: Optional[Dict[str, str]] = None):
        """Set a gauge metric value."""
        self.record(name, value, MetricType.GAUGE, labels)

    def time_histogram(self, name: str, duration: float, labels: Optional[Dict[str, str]] = None):
        """Record a timing measurement in a histogram."""
        self.record(name, duration, MetricType.HISTOGRAM, labels)

    def record_request(
        self,
        provider: str,
        model: str,
        duration_seconds: float,
        tokens_used: int = 0,
        cost_estimate: float = 0.0,
        success: bool = True,
        error_type: Optional[str] = None
    ):
        """
        Record a complete AI request with all standard metrics.

        Args:
            provider: AI provider name
            model: Model name used
            duration_seconds: Request duration in seconds
            tokens_used: Number of tokens consumed
            cost_estimate: Estimated cost in USD
            success: Whether the request succeeded
            error_type: Type of error if request failed
        """
        labels = {"provider": provider, "model": model}

        # Request count
        self.increment(self.REQUESTS_TOTAL, 1.0, labels)

        # Request duration
        self.time_histogram(self.REQUEST_DURATION, duration_seconds, labels)

        # Token usage
        if tokens_used > 0:
            self.increment(self.TOKENS_USED_TOTAL, float(tokens_used), labels)

        # Cost tracking
        if cost_estimate > 0:
            self.increment(self.COST_TOTAL, cost_estimate, labels)

        # Error tracking
        if not success and error_type:
            error_labels = {**labels, "error_type": error_type}
            self.increment(self.ERRORS_TOTAL, 1.0, error_labels)

    def record_conversation(self, provider: str, active_count: int):
        """Record active conversation count."""
        labels = {"provider": provider}
        self.set_gauge(self.CONVERSATIONS_ACTIVE, float(active_count), labels)

    def record_streaming(self, provider: str, model: str, chunks_count: int):
        """Record streaming response metrics."""
        labels = {"provider": provider, "model": model}
        self.increment(self.STREAMING_CHUNKS_TOTAL, float(chunks_count), labels)

    def record_artifact(self, provider: str, model: str, artifact_type: str):
        """Record artifact generation."""
        labels = {"provider": provider, "model": model, "type": artifact_type}
        self.increment(self.ARTIFACTS_GENERATED_TOTAL, 1.0, labels)

    def get_stats(self) -> Dict[str, Any]:
        """
        Get current metrics summary.

        Returns:
            Dict containing current metric values and summaries
        """
        with self._lock:
            stats = {
                "counters": dict(self._counters),
                "gauges": dict(self._gauges),
                "summaries": {k: v.to_dict() for k, v in self._summaries.items()},
                "collection_time": datetime.now(timezone.utc).isoformat(),
                "backend": self.backend.__class__.__name__,
                "enabled": self.enabled
            }

            # Add derived statistics
            if self._counters:
                stats["totals"] = {
                    "total_requests": sum(v for k, v in self._counters.items()
                                        if k.startswith(self.REQUESTS_TOTAL)),
                    "total_tokens": sum(v for k, v in self._counters.items()
                                      if k.startswith(self.TOKENS_USED_TOTAL)),
                    "total_cost": sum(v for k, v in self._counters.items()
                                    if k.startswith(self.COST_TOTAL)),
                    "total_errors": sum(v for k, v in self._counters.items()
                                      if k.startswith(self.ERRORS_TOTAL))
                }

            return stats

    def export_prometheus_format(self) -> str:
        """
        Export metrics in Prometheus text format.

        Returns:
            String in Prometheus exposition format
        """
        lines = []
        timestamp = int(time.time() * 1000)  # Prometheus expects milliseconds

        with self._lock:
            # Export counters
            for metric_key, value in self._counters.items():
                base_name = metric_key.split('{')[0]  # Remove label part
                labels_dict = self._labels.get(metric_key, {})

                if labels_dict:
                    labels_str = ','.join(f'{k}="{v}"' for k, v in labels_dict.items())
                    line = f'{base_name}{{{labels_str}}} {value} {timestamp}'
                else:
                    line = f'{base_name} {value} {timestamp}'
                lines.append(line)

            # Export gauges
            for metric_key, value in self._gauges.items():
                base_name = metric_key.split('{')[0]
                labels_dict = self._labels.get(metric_key, {})

                if labels_dict:
                    labels_str = ','.join(f'{k}="{v}"' for k, v in labels_dict.items())
                    line = f'{base_name}{{{labels_str}}} {value} {timestamp}'
                else:
                    line = f'{base_name} {value} {timestamp}'
                lines.append(line)

            # Export histogram summaries
            for metric_key, summary in self._summaries.items():
                base_name = summary.name
                labels_dict = self._labels.get(metric_key, {})

                label_prefix = ""
                if labels_dict:
                    label_prefix = ','.join(f'{k}="{v}"' for k, v in labels_dict.items())
                    label_prefix = f'{{{label_prefix}}}'

                # Summary statistics
                lines.extend([
                    f'{base_name}_count{label_prefix} {summary.count} {timestamp}',
                    f'{base_name}_sum{label_prefix} {summary.sum} {timestamp}',
                    f'{base_name}_avg{label_prefix} {summary.avg} {timestamp}'
                ])

        return '\n'.join(lines) + '\n' if lines else ""

    def export_json_format(self) -> Dict[str, Any]:
        """Export metrics in JSON format."""
        return self.get_stats()

    def reset(self):
        """Reset all metrics to zero/empty."""
        if not self.enabled:
            return

        with self._lock:
            self._counters.clear()
            self._gauges.clear()
            self._histograms.clear()
            self._summaries.clear()
            self._labels.clear()

            try:
                if hasattr(self.backend, 'reset'):
                    self.backend.reset()
            except Exception as e:
                logger.warning(f"Failed to reset backend: {e}")

        logger.info("AIMetrics reset completed")

    def enable(self):
        """Enable metrics collection."""
        self.enabled = True
        logger.info("AIMetrics collection enabled")

    def disable(self):
        """Disable metrics collection."""
        self.enabled = False
        logger.info("AIMetrics collection disabled")

    def __repr__(self) -> str:
        """String representation of metrics system."""
        with self._lock:
            total_metrics = len(self._counters) + len(self._gauges) + len(self._summaries)
            return (f"AIMetrics(backend={self.backend.__class__.__name__}, "
                   f"enabled={self.enabled}, metrics={total_metrics})")