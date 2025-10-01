"""
Custom logging handlers for AI operations.

Provides performance-optimized handlers for file, rotating file,
and null output with minimal overhead.
"""

import logging
import os
import threading
import time
from collections import deque
from logging.handlers import RotatingFileHandler as StdRotatingFileHandler
from pathlib import Path
from typing import Optional, Deque, TextIO


class NullHandler(logging.Handler):
    """
    Null handler that discards all log records.

    Provides zero-overhead logging when disabled.
    """

    def emit(self, record):
        """Discard the record silently."""
        pass

    def handle(self, record):
        """Handle record by doing nothing."""
        return True

    def createLock(self):
        """Override to avoid creating unnecessary lock."""
        self.lock = None


class FileHandler(logging.FileHandler):
    """
    Enhanced file handler with better error handling and performance.

    Provides robust file writing with automatic directory creation
    and error recovery.
    """

    def __init__(self, filename, mode='a', encoding='utf-8', delay=False):
        """
        Initialize file handler.

        Args:
            filename: Log file path
            mode: File open mode
            encoding: File encoding
            delay: Delay file opening until first emit
        """
        # Ensure directory exists
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        super().__init__(filename, mode, encoding, delay)
        self._error_count = 0
        self._max_errors = 10

    def emit(self, record):
        """Emit log record with error handling."""
        try:
            super().emit(record)
            self._error_count = 0  # Reset on success
        except Exception as e:
            self._error_count += 1
            if self._error_count <= self._max_errors:
                # Try to recover by reopening file
                try:
                    if self.stream:
                        self.stream.close()
                    self.stream = self._open()
                    super().emit(record)
                    self._error_count = 0
                except Exception:
                    pass  # Give up silently to avoid logging recursion


class RotatingFileHandler(StdRotatingFileHandler):
    """
    Enhanced rotating file handler with better performance and error handling.

    Provides log rotation with automatic directory creation, better error
    recovery, and performance optimizations.
    """

    def __init__(self, filename, max_bytes=0, backup_count=0, encoding='utf-8', delay=False):
        """
        Initialize rotating file handler.

        Args:
            filename: Log file path
            max_bytes: Maximum file size before rotation
            backup_count: Number of backup files to keep
            encoding: File encoding
            delay: Delay file opening until first emit
        """
        # Ensure directory exists
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        super().__init__(filename, 'a', max_bytes, backup_count, encoding, delay)
        self._error_count = 0
        self._max_errors = 10

    def doRollover(self):
        """Perform log rotation with better error handling."""
        try:
            super().doRollover()
        except Exception as e:
            # If rotation fails, try to continue with current file
            if self.stream:
                try:
                    self.stream.flush()
                except Exception:
                    pass

    def emit(self, record):
        """Emit log record with error handling."""
        try:
            super().emit(record)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count <= self._max_errors:
                # Try to recover
                try:
                    if self.stream:
                        self.stream.close()
                    self.stream = self._open()
                    super().emit(record)
                    self._error_count = 0
                except Exception:
                    pass


class BufferedHandler(logging.Handler):
    """
    Buffered handler for high-performance async logging.

    Buffers log records in memory and flushes them periodically
    to minimize I/O overhead.
    """

    def __init__(self, target_handler, buffer_size=1000, flush_interval=5.0):
        """
        Initialize buffered handler.

        Args:
            target_handler: Underlying handler to write to
            buffer_size: Maximum buffer size before auto-flush
            flush_interval: Time interval for automatic flushing
        """
        super().__init__()
        self.target_handler = target_handler
        self.buffer_size = buffer_size
        self.flush_interval = flush_interval

        self._buffer: Deque[logging.LogRecord] = deque()
        self._buffer_lock = threading.Lock()
        self._last_flush = time.time()

        # Start flush thread
        self._flush_thread = threading.Thread(target=self._flush_worker, daemon=True)
        self._flush_thread.start()
        self._shutdown = threading.Event()

    def emit(self, record):
        """Add record to buffer."""
        try:
            with self._buffer_lock:
                self._buffer.append(record)

                # Auto-flush if buffer is full
                if len(self._buffer) >= self.buffer_size:
                    self._flush_buffer()

        except Exception:
            # Fallback to direct emission
            try:
                self.target_handler.emit(record)
            except Exception:
                pass

    def flush(self):
        """Manually flush buffer."""
        with self._buffer_lock:
            self._flush_buffer()

    def _flush_buffer(self):
        """Flush buffer contents to target handler (called with lock held)."""
        if not self._buffer:
            return

        # Move records to local list for processing
        records_to_flush = list(self._buffer)
        self._buffer.clear()
        self._last_flush = time.time()

        # Process records (release lock first)
        for record in records_to_flush:
            try:
                self.target_handler.emit(record)
            except Exception:
                pass  # Ignore individual record failures

        # Flush target handler
        try:
            self.target_handler.flush()
        except Exception:
            pass

    def _flush_worker(self):
        """Background thread for periodic flushing."""
        while not self._shutdown.wait(self.flush_interval):
            try:
                current_time = time.time()
                if current_time - self._last_flush >= self.flush_interval:
                    with self._buffer_lock:
                        if self._buffer:  # Only flush if there's data
                            self._flush_buffer()
            except Exception:
                pass  # Continue running even if flush fails

    def close(self):
        """Close handler and cleanup resources."""
        # Shutdown flush thread
        self._shutdown.set()
        if self._flush_thread.is_alive():
            self._flush_thread.join(timeout=1.0)

        # Final flush
        self.flush()

        # Close target handler
        if hasattr(self.target_handler, 'close'):
            self.target_handler.close()

        super().close()


class FilteredHandler(logging.Handler):
    """
    Handler that applies filtering based on module patterns.

    Allows fine-grained control over which modules/components
    should have their logs emitted.
    """

    def __init__(self, target_handler, include_patterns=None, exclude_patterns=None):
        """
        Initialize filtered handler.

        Args:
            target_handler: Underlying handler to write to
            include_patterns: List of patterns to include (None = include all)
            exclude_patterns: List of patterns to exclude (None = exclude none)
        """
        super().__init__()
        self.target_handler = target_handler
        self.include_patterns = include_patterns or []
        self.exclude_patterns = exclude_patterns or []

    def emit(self, record):
        """Emit record if it passes filters."""
        if not self._should_emit(record):
            return

        try:
            self.target_handler.emit(record)
        except Exception:
            pass

    def _should_emit(self, record) -> bool:
        """Check if record should be emitted based on filters."""
        logger_name = record.name

        # Check exclude patterns first (more restrictive)
        if self.exclude_patterns:
            for pattern in self.exclude_patterns:
                if pattern in logger_name:
                    return False

        # Check include patterns
        if self.include_patterns:
            for pattern in self.include_patterns:
                if pattern in logger_name:
                    return True
            return False  # Didn't match any include pattern

        return True  # No patterns or passed all checks

    def flush(self):
        """Flush target handler."""
        if hasattr(self.target_handler, 'flush'):
            self.target_handler.flush()

    def close(self):
        """Close target handler."""
        if hasattr(self.target_handler, 'close'):
            self.target_handler.close()
        super().close()


class PerformanceHandler(logging.Handler):
    """
    High-performance handler for minimal overhead logging.

    Optimized for maximum throughput with minimal memory allocation
    and processing overhead.
    """

    def __init__(self, target_handler):
        """
        Initialize performance handler.

        Args:
            target_handler: Underlying handler to write to
        """
        super().__init__()
        self.target_handler = target_handler

        # Performance tracking
        self._emit_count = 0
        self._error_count = 0
        self._last_error_time = 0

    def emit(self, record):
        """Emit record with minimal overhead."""
        self._emit_count += 1

        try:
            self.target_handler.emit(record)
        except Exception:
            self._error_count += 1
            self._last_error_time = time.time()

            # If too many errors, stop trying for a while
            if self._error_count > 10:
                current_time = time.time()
                if current_time - self._last_error_time < 60:  # 1 minute cooldown
                    return

                self._error_count = 0  # Reset after cooldown

    def get_stats(self):
        """Get performance statistics."""
        return {
            'emit_count': self._emit_count,
            'error_count': self._error_count,
            'last_error_time': self._last_error_time
        }

    def flush(self):
        """Flush target handler."""
        try:
            if hasattr(self.target_handler, 'flush'):
                self.target_handler.flush()
        except Exception:
            pass

    def close(self):
        """Close target handler."""
        try:
            if hasattr(self.target_handler, 'close'):
                self.target_handler.close()
        except Exception:
            pass
        super().close()


class MultiHandler(logging.Handler):
    """
    Handler that broadcasts to multiple target handlers.

    Allows sending the same log record to multiple destinations
    (e.g., both file and console) with individual error handling.
    """

    def __init__(self, handlers):
        """
        Initialize multi-handler.

        Args:
            handlers: List of handlers to broadcast to
        """
        super().__init__()
        self.handlers = list(handlers) if handlers else []

    def emit(self, record):
        """Emit record to all handlers."""
        for handler in self.handlers:
            try:
                handler.emit(record)
            except Exception:
                # Continue with other handlers even if one fails
                pass

    def flush(self):
        """Flush all handlers."""
        for handler in self.handlers:
            try:
                if hasattr(handler, 'flush'):
                    handler.flush()
            except Exception:
                pass

    def close(self):
        """Close all handlers."""
        for handler in self.handlers:
            try:
                if hasattr(handler, 'close'):
                    handler.close()
            except Exception:
                pass
        super().close()

    def add_handler(self, handler):
        """Add a handler to the broadcast list."""
        if handler not in self.handlers:
            self.handlers.append(handler)

    def remove_handler(self, handler):
        """Remove a handler from the broadcast list."""
        if handler in self.handlers:
            self.handlers.remove(handler)


class SamplingHandler(logging.Handler):
    """
    Handler that samples log records to reduce volume.

    Useful for high-frequency logging where you only want
    a representative sample rather than every record.
    """

    def __init__(self, target_handler, sample_rate=0.1):
        """
        Initialize sampling handler.

        Args:
            target_handler: Underlying handler to write to
            sample_rate: Fraction of records to emit (0.0 to 1.0)
        """
        super().__init__()
        self.target_handler = target_handler
        self.sample_rate = max(0.0, min(1.0, sample_rate))
        self._counter = 0
        self._emit_threshold = int(1.0 / self.sample_rate) if self.sample_rate > 0 else 0

    def emit(self, record):
        """Emit record based on sampling rate."""
        if self.sample_rate <= 0:
            return

        if self.sample_rate >= 1.0:
            # Emit all records
            try:
                self.target_handler.emit(record)
            except Exception:
                pass
            return

        # Sample based on counter
        self._counter += 1
        if self._counter >= self._emit_threshold:
            self._counter = 0
            try:
                self.target_handler.emit(record)
            except Exception:
                pass

    def flush(self):
        """Flush target handler."""
        if hasattr(self.target_handler, 'flush'):
            self.target_handler.flush()

    def close(self):
        """Close target handler."""
        if hasattr(self.target_handler, 'close'):
            self.target_handler.close()
        super().close()