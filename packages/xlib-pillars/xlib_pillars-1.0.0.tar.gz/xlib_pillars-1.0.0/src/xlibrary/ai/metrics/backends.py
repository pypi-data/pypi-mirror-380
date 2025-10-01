"""
Backend implementations for metrics storage and export.

Provides multiple backend options for metric storage without external dependencies.
"""

import json
import logging
import os
import socket
import threading
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from collections import deque

# Import will be done inline to avoid circular imports


logger = logging.getLogger(__name__)


class BaseBackend(ABC):
    """Abstract base class for metric backends."""

    @abstractmethod
    def record(self, metric):
        """Record a metric point."""
        pass

    def reset(self):
        """Reset/clear all stored metrics."""
        pass

    def close(self):
        """Clean up resources."""
        pass


class NullBackend(BaseBackend):
    """Backend that discards all metrics (for disabling)."""

    def record(self, metric):
        """Discard the metric."""
        pass


class MemoryBackend(BaseBackend):
    """In-memory backend that stores metrics in memory only."""

    def __init__(self, max_points: int = 10000):
        """
        Initialize memory backend.

        Args:
            max_points: Maximum number of metric points to store
        """
        self.max_points = max_points
        self.metrics: deque = deque(maxlen=max_points)
        self._lock = threading.Lock()

    def record(self, metric):
        """Store metric in memory."""
        with self._lock:
            self.metrics.append(metric)

    def get_metrics(self) -> List:
        """Get all stored metrics."""
        with self._lock:
            return list(self.metrics)

    def reset(self):
        """Clear all stored metrics."""
        with self._lock:
            self.metrics.clear()

    def get_stats(self) -> Dict[str, Any]:
        """Get backend statistics."""
        with self._lock:
            return {
                "backend_type": "memory",
                "total_points": len(self.metrics),
                "max_points": self.max_points,
                "oldest_metric": self.metrics[0].timestamp.isoformat() if self.metrics else None,
                "newest_metric": self.metrics[-1].timestamp.isoformat() if self.metrics else None
            }


class FileBackend(BaseBackend):
    """File-based backend that appends metrics to a JSON file."""

    def __init__(
        self,
        file_path: str = "ai_metrics.jsonl",
        max_file_size_mb: int = 100,
        rotate_files: bool = True
    ):
        """
        Initialize file backend.

        Args:
            file_path: Path to metrics file
            max_file_size_mb: Maximum file size before rotation
            rotate_files: Whether to rotate files when max size reached
        """
        self.file_path = Path(file_path).resolve()
        self.max_file_size_bytes = max_file_size_mb * 1024 * 1024
        self.rotate_files = rotate_files
        self._lock = threading.Lock()

        # Ensure directory exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"FileBackend initialized: {self.file_path}")

    def record(self, metric):
        """Append metric to file in JSONL format."""
        try:
            with self._lock:
                # Check file size and rotate if needed
                if self.rotate_files and self.file_path.exists():
                    if self.file_path.stat().st_size > self.max_file_size_bytes:
                        self._rotate_file()

                # Append metric
                with open(self.file_path, 'a') as f:
                    json.dump(metric.to_dict(), f, separators=(',', ':'))
                    f.write('\n')

        except Exception as e:
            logger.error(f"Failed to write metric to file: {e}")

    def _rotate_file(self):
        """Rotate the current file."""
        if not self.file_path.exists():
            return

        # Find next rotation number
        base_name = self.file_path.stem
        suffix = self.file_path.suffix
        rotation_num = 1

        while True:
            rotated_path = self.file_path.parent / f"{base_name}.{rotation_num}{suffix}"
            if not rotated_path.exists():
                break
            rotation_num += 1

        # Rotate the file
        self.file_path.rename(rotated_path)
        logger.info(f"Rotated metrics file to {rotated_path}")

    def get_recent_metrics(self, lines: int = 1000) -> List[Dict[str, Any]]:
        """
        Get recent metrics from file.

        Args:
            lines: Number of recent lines to read

        Returns:
            List of metric dictionaries
        """
        metrics = []
        if not self.file_path.exists():
            return metrics

        try:
            with self._lock:
                with open(self.file_path, 'r') as f:
                    # Read last N lines efficiently
                    file_lines = deque(f, maxlen=lines)

                    for line in file_lines:
                        line = line.strip()
                        if line:
                            try:
                                metrics.append(json.loads(line))
                            except json.JSONDecodeError:
                                continue

        except Exception as e:
            logger.error(f"Failed to read metrics from file: {e}")

        return metrics

    def reset(self):
        """Clear the metrics file."""
        try:
            with self._lock:
                if self.file_path.exists():
                    self.file_path.unlink()
                    logger.info(f"Cleared metrics file: {self.file_path}")
        except Exception as e:
            logger.error(f"Failed to clear metrics file: {e}")

    def get_stats(self) -> Dict[str, Any]:
        """Get backend statistics."""
        stats = {
            "backend_type": "file",
            "file_path": str(self.file_path),
            "file_exists": self.file_path.exists(),
            "max_file_size_mb": self.max_file_size_bytes // (1024 * 1024),
            "rotate_files": self.rotate_files
        }

        if self.file_path.exists():
            try:
                file_stat = self.file_path.stat()
                stats.update({
                    "file_size_bytes": file_stat.st_size,
                    "file_size_mb": round(file_stat.st_size / (1024 * 1024), 2),
                    "last_modified": datetime.fromtimestamp(file_stat.st_mtime).isoformat()
                })
            except Exception as e:
                logger.warning(f"Failed to get file stats: {e}")

        return stats


class StatsDBackend(BaseBackend):
    """StatsD backend that sends metrics via UDP."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8125,
        prefix: str = "xlibrary.ai",
        timeout: float = 5.0
    ):
        """
        Initialize StatsD backend.

        Args:
            host: StatsD server host
            port: StatsD server port
            prefix: Metric name prefix
            timeout: Socket timeout in seconds
        """
        self.host = host
        self.port = port
        self.prefix = prefix
        self.timeout = timeout
        self._socket = None
        self._lock = threading.Lock()

        # Test connection
        self._ensure_socket()
        logger.info(f"StatsDBackend initialized: {host}:{port}")

    def _ensure_socket(self):
        """Ensure UDP socket is available."""
        if self._socket is None:
            try:
                self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self._socket.settimeout(self.timeout)
            except Exception as e:
                logger.error(f"Failed to create StatsD socket: {e}")
                raise

    def record(self, metric):
        """Send metric to StatsD server."""
        try:
            with self._lock:
                self._ensure_socket()

                # Build metric name with prefix
                metric_name = f"{self.prefix}.{metric.name}"

                # Add labels to metric name
                if metric.labels:
                    label_parts = []
                    for key, value in metric.labels.items():
                        # Sanitize labels for StatsD
                        clean_key = key.replace('.', '_').replace(':', '_')
                        clean_value = str(value).replace('.', '_').replace(':', '_')
                        label_parts.append(f"{clean_key}.{clean_value}")

                    if label_parts:
                        metric_name += "." + ".".join(label_parts)

                # Format based on metric type
                if metric.metric_type.value == "counter":
                    statsd_line = f"{metric_name}:{metric.value}|c"
                elif metric.metric_type.value == "gauge":
                    statsd_line = f"{metric_name}:{metric.value}|g"
                elif metric.metric_type.value in ["histogram", "timer"]:
                    # Convert to milliseconds for timing
                    value = metric.value * 1000 if metric.metric_type.value == "timer" else metric.value
                    statsd_line = f"{metric_name}:{value}|ms"
                else:
                    statsd_line = f"{metric_name}:{metric.value}|g"

                # Send via UDP
                self._socket.sendto(statsd_line.encode('utf-8'), (self.host, self.port))

        except Exception as e:
            logger.warning(f"Failed to send metric to StatsD: {e}")
            # Don't raise - we don't want metrics to break the application

    def close(self):
        """Close the socket connection."""
        with self._lock:
            if self._socket:
                try:
                    self._socket.close()
                except Exception as e:
                    logger.warning(f"Error closing StatsD socket: {e}")
                finally:
                    self._socket = None

    def get_stats(self) -> Dict[str, Any]:
        """Get backend statistics."""
        return {
            "backend_type": "statsd",
            "host": self.host,
            "port": self.port,
            "prefix": self.prefix,
            "timeout": self.timeout,
            "socket_connected": self._socket is not None
        }


class CompositeBackend(BaseBackend):
    """Backend that forwards metrics to multiple other backends."""

    def __init__(self, backends: List[BaseBackend]):
        """
        Initialize composite backend.

        Args:
            backends: List of backend instances to forward to
        """
        self.backends = backends
        logger.info(f"CompositeBackend initialized with {len(backends)} backends")

    def record(self, metric):
        """Record metric to all backends."""
        for backend in self.backends:
            try:
                backend.record(metric)
            except Exception as e:
                logger.warning(f"Failed to record to backend {backend.__class__.__name__}: {e}")

    def reset(self):
        """Reset all backends."""
        for backend in self.backends:
            try:
                backend.reset()
            except Exception as e:
                logger.warning(f"Failed to reset backend {backend.__class__.__name__}: {e}")

    def close(self):
        """Close all backends."""
        for backend in self.backends:
            try:
                backend.close()
            except Exception as e:
                logger.warning(f"Failed to close backend {backend.__class__.__name__}: {e}")

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics from all backends."""
        stats = {
            "backend_type": "composite",
            "num_backends": len(self.backends),
            "backends": []
        }

        for i, backend in enumerate(self.backends):
            try:
                backend_stats = backend.get_stats() if hasattr(backend, 'get_stats') else {}
                backend_stats["backend_index"] = i
                stats["backends"].append(backend_stats)
            except Exception as e:
                stats["backends"].append({
                    "backend_index": i,
                    "error": str(e),
                    "backend_class": backend.__class__.__name__
                })

        return stats