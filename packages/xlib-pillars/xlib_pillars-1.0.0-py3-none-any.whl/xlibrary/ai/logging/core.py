"""
Core logging system with performance-optimized structured logging.

Designed for zero performance impact when disabled and comprehensive
debugging information when enabled.
"""

import logging
import os
import threading
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, Any, Optional, List, Callable, Union
from contextlib import contextmanager

from .formatters import StructuredFormatter, JSONFormatter, ColoredFormatter
from .handlers import FileHandler, RotatingFileHandler, NullHandler


class LogLevel(Enum):
    """Extended log levels for AI operations."""
    TRACE = 5       # Most detailed tracing
    DEBUG = 10      # Debug information
    INFO = 20       # General information
    WARNING = 30    # Warning messages
    ERROR = 40      # Error messages
    CRITICAL = 50   # Critical failures

    # AI-specific levels
    REQUEST = 15    # AI request/response logging
    PERFORMANCE = 25  # Performance metrics


@dataclass
class LogConfig:
    """Configuration for AI logging system."""

    # Core settings
    enabled: bool = False
    level: LogLevel = LogLevel.INFO

    # File output settings
    file_enabled: bool = False
    file_path: Optional[Union[str, Path]] = None
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    backup_count: int = 5

    # Console output settings
    console_enabled: bool = True
    console_colored: bool = True

    # Structured logging
    structured: bool = True
    json_format: bool = False
    include_caller: bool = True
    include_thread: bool = False

    # Performance settings
    async_logging: bool = True
    buffer_size: int = 1000
    flush_interval: float = 5.0

    # Filtering
    include_modules: List[str] = field(default_factory=list)
    exclude_modules: List[str] = field(default_factory=list)

    # AI-specific settings
    log_requests: bool = True
    log_responses: bool = True
    log_tokens: bool = True
    log_costs: bool = True
    log_errors: bool = True
    log_performance: bool = True

    # Sensitive data handling
    mask_api_keys: bool = True
    truncate_large_content: bool = True
    max_content_length: int = 1000

    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return {
            'enabled': self.enabled,
            'level': self.level.name,
            'file_enabled': self.file_enabled,
            'file_path': str(self.file_path) if self.file_path else None,
            'console_enabled': self.console_enabled,
            'structured': self.structured,
            'json_format': self.json_format,
            'log_requests': self.log_requests,
            'log_responses': self.log_responses,
            'mask_api_keys': self.mask_api_keys
        }


class PerformanceTracker:
    """Track performance metrics for operations."""

    def __init__(self):
        self._timings: Dict[str, List[float]] = defaultdict(list)
        self._counters: Dict[str, int] = defaultdict(int)
        self._errors: Dict[str, int] = defaultdict(int)
        self._lock = threading.Lock()

    def time_operation(self, operation: str, duration: float):
        """Record operation timing."""
        with self._lock:
            self._timings[operation].append(duration)

    def count_operation(self, operation: str):
        """Count operation occurrence."""
        with self._lock:
            self._counters[operation] += 1

    def count_error(self, operation: str):
        """Count error occurrence."""
        with self._lock:
            self._errors[operation] += 1

    def get_stats(self) -> Dict[str, Any]:
        """Get performance statistics."""
        with self._lock:
            stats = {
                'timings': {},
                'counters': dict(self._counters),
                'errors': dict(self._errors)
            }

            for operation, times in self._timings.items():
                if times:
                    stats['timings'][operation] = {
                        'count': len(times),
                        'avg_ms': sum(times) * 1000 / len(times),
                        'min_ms': min(times) * 1000,
                        'max_ms': max(times) * 1000,
                        'total_ms': sum(times) * 1000
                    }

            return stats

    def reset(self):
        """Reset all statistics."""
        with self._lock:
            self._timings.clear()
            self._counters.clear()
            self._errors.clear()


class AILogger:
    """
    High-performance AI logging system with zero-overhead when disabled.

    Provides structured logging for AI operations with comprehensive
    debugging capabilities when enabled.
    """

    _instances: Dict[str, 'AILogger'] = {}
    _lock = threading.Lock()

    def __init__(self, name: str, config: Optional[LogConfig] = None):
        """
        Initialize AI logger for a specific component.

        Args:
            name: Logger name (typically module or component name)
            config: Logging configuration
        """
        self.name = name
        self.config = config or LogConfig()

        # Performance tracking
        self.perf_tracker = PerformanceTracker()

        # Initialize Python logger
        self._logger = logging.getLogger(f"xlibrary.ai.{name}")

        # Configure handlers if enabled
        if self.config.enabled:
            self._setup_handlers()
        else:
            # Use null handler for zero performance impact
            self._logger.addHandler(NullHandler())
            self._logger.setLevel(logging.CRITICAL + 1)  # Disable all logging

        # Thread-safe operation tracking
        self._active_operations: Dict[str, datetime] = {}
        self._operation_lock = threading.Lock()

    @classmethod
    def get_logger(cls, name: str, config: Optional[LogConfig] = None) -> 'AILogger':
        """Get or create logger instance (singleton per name)."""
        with cls._lock:
            if name not in cls._instances:
                cls._instances[name] = cls(name, config)
            elif config is not None:
                # Update configuration if provided
                cls._instances[name].update_config(config)
            return cls._instances[name]

    def update_config(self, config: LogConfig):
        """Update logger configuration."""
        self.config = config

        # Clear existing handlers
        for handler in self._logger.handlers[:]:
            self._logger.removeHandler(handler)

        if config.enabled:
            self._setup_handlers()
            self._logger.setLevel(config.level.value)
        else:
            self._logger.addHandler(NullHandler())
            self._logger.setLevel(logging.CRITICAL + 1)

    def _setup_handlers(self):
        """Set up logging handlers based on configuration."""
        self._logger.setLevel(self.config.level.value)

        # Console handler
        if self.config.console_enabled:
            console_handler = logging.StreamHandler()
            if self.config.console_colored:
                formatter = ColoredFormatter(
                    structured=self.config.structured,
                    include_caller=self.config.include_caller,
                    include_thread=self.config.include_thread
                )
            elif self.config.json_format:
                formatter = JSONFormatter()
            else:
                formatter = StructuredFormatter(
                    include_caller=self.config.include_caller,
                    include_thread=self.config.include_thread
                )
            console_handler.setFormatter(formatter)
            self._logger.addHandler(console_handler)

        # File handler
        if self.config.file_enabled and self.config.file_path:
            file_path = Path(self.config.file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            if self.config.max_file_size > 0:
                file_handler = RotatingFileHandler(
                    filename=file_path,
                    max_bytes=self.config.max_file_size,
                    backup_count=self.config.backup_count
                )
            else:
                file_handler = FileHandler(filename=file_path)

            if self.config.json_format:
                formatter = JSONFormatter()
            else:
                formatter = StructuredFormatter(
                    include_caller=self.config.include_caller,
                    include_thread=self.config.include_thread
                )
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

    @property
    def enabled(self) -> bool:
        """Check if logging is enabled (for performance optimization)."""
        return self.config.enabled

    @property
    def file(self) -> Optional[Path]:
        """Get current log file path."""
        if self.config.file_enabled and self.config.file_path:
            return Path(self.config.file_path)
        return None

    def _should_log(self, level: LogLevel) -> bool:
        """Check if message should be logged (performance optimization)."""
        return self.config.enabled and level.value >= self.config.level.value

    def _mask_sensitive_data(self, data: Any) -> Any:
        """Mask sensitive data in log messages."""
        if not self.config.mask_api_keys:
            return data

        if isinstance(data, str):
            # Mask API keys
            if data.startswith(('sk-', 'claude-', 'gsk_')):
                return f"{data[:6]}...{data[-4:]}" if len(data) > 10 else "***masked***"
            return data
        elif isinstance(data, dict):
            masked = {}
            for key, value in data.items():
                if key.lower() in ['api_key', 'token', 'secret', 'password']:
                    masked[key] = "***masked***"
                else:
                    masked[key] = self._mask_sensitive_data(value)
            return masked
        elif isinstance(data, list):
            return [self._mask_sensitive_data(item) for item in data]
        else:
            return data

    def _truncate_content(self, content: str) -> str:
        """Truncate large content if configured."""
        if (self.config.truncate_large_content and
            len(content) > self.config.max_content_length):
            return f"{content[:self.config.max_content_length]}... [truncated]"
        return content

    def _create_log_record(self, level: LogLevel, message: str, **kwargs) -> Dict[str, Any]:
        """Create structured log record."""
        record = {
            'timestamp': datetime.now().isoformat(),
            'level': level.name,
            'logger': self.name,
            'message': message
        }

        # Add caller information if enabled
        if self.config.include_caller:
            import inspect
            frame = inspect.currentframe()
            try:
                # Go up the stack to find the actual caller
                caller_frame = frame.f_back.f_back.f_back
                if caller_frame:
                    record['caller'] = {
                        'file': os.path.basename(caller_frame.f_code.co_filename),
                        'function': caller_frame.f_code.co_name,
                        'line': caller_frame.f_lineno
                    }
            finally:
                del frame

        # Add thread information if enabled
        if self.config.include_thread:
            record['thread'] = threading.current_thread().name

        # Add extra data
        if kwargs:
            record['data'] = self._mask_sensitive_data(kwargs)

        return record

    def trace(self, message: str, **kwargs):
        """Log trace message (most detailed)."""
        if self._should_log(LogLevel.TRACE):
            record = self._create_log_record(LogLevel.TRACE, message, **kwargs)
            self._logger.log(LogLevel.TRACE.value, message, extra={'structured_data': record})

    def debug(self, message: str, **kwargs):
        """Log debug message."""
        if self._should_log(LogLevel.DEBUG):
            record = self._create_log_record(LogLevel.DEBUG, message, **kwargs)
            self._logger.log(LogLevel.DEBUG.value, message, extra={'structured_data': record})

    def info(self, message: str, **kwargs):
        """Log info message."""
        if self._should_log(LogLevel.INFO):
            record = self._create_log_record(LogLevel.INFO, message, **kwargs)
            self._logger.log(LogLevel.INFO.value, message, extra={'structured_data': record})

    def warning(self, message: str, **kwargs):
        """Log warning message."""
        if self._should_log(LogLevel.WARNING):
            record = self._create_log_record(LogLevel.WARNING, message, **kwargs)
            self._logger.log(LogLevel.WARNING.value, message, extra={'structured_data': record})

    def error(self, message: str, **kwargs):
        """Log error message."""
        if self._should_log(LogLevel.ERROR):
            record = self._create_log_record(LogLevel.ERROR, message, **kwargs)
            self._logger.log(LogLevel.ERROR.value, message, extra={'structured_data': record})

            # Track error for performance monitoring
            operation = kwargs.get('operation', 'unknown')
            self.perf_tracker.count_error(operation)

    def critical(self, message: str, **kwargs):
        """Log critical message."""
        if self._should_log(LogLevel.CRITICAL):
            record = self._create_log_record(LogLevel.CRITICAL, message, **kwargs)
            self._logger.log(LogLevel.CRITICAL.value, message, extra={'structured_data': record})

    def request(self, message: str, **kwargs):
        """Log AI request information."""
        if self._should_log(LogLevel.REQUEST) and self.config.log_requests:
            record = self._create_log_record(LogLevel.REQUEST, message, **kwargs)
            self._logger.log(LogLevel.REQUEST.value, message, extra={'structured_data': record})

    def performance(self, message: str, **kwargs):
        """Log performance information."""
        if self._should_log(LogLevel.PERFORMANCE) and self.config.log_performance:
            record = self._create_log_record(LogLevel.PERFORMANCE, message, **kwargs)
            self._logger.log(LogLevel.PERFORMANCE.value, message, extra={'structured_data': record})

    def log_ai_request(self, provider: str, model: str, prompt: str, **kwargs):
        """Log AI request with standardized format."""
        if not self.config.log_requests:
            return

        request_data = {
            'provider': provider,
            'model': model,
            'prompt_length': len(prompt),
            'prompt': self._truncate_content(prompt) if prompt else None,
            **kwargs
        }

        self.request(f"AI Request to {provider}:{model}", **request_data)

    def log_ai_response(self, provider: str, model: str, response_length: int,
                       tokens_used: int = 0, cost: float = 0.0, latency_ms: float = 0.0, **kwargs):
        """Log AI response with standardized format."""
        if not self.config.log_responses:
            return

        response_data = {
            'provider': provider,
            'model': model,
            'response_length': response_length,
            'latency_ms': latency_ms,
            **kwargs
        }

        if self.config.log_tokens and tokens_used > 0:
            response_data['tokens_used'] = tokens_used

        if self.config.log_costs and cost > 0:
            response_data['cost_usd'] = cost

        self.request(f"AI Response from {provider}:{model}", **response_data)

    def log_ai_error(self, provider: str, model: str, error: Exception, **kwargs):
        """Log AI error with standardized format."""
        if not self.config.log_errors:
            return

        error_data = {
            'provider': provider,
            'model': model,
            'error_type': type(error).__name__,
            'error_message': str(error),
            **kwargs
        }

        self.error(f"AI Error in {provider}:{model}", **error_data)

    @contextmanager
    def operation(self, operation_name: str, **context):
        """Context manager for tracking operations with timing."""
        operation_id = f"{operation_name}_{int(time.time() * 1000)}"
        start_time = time.time()

        # Track active operation
        with self._operation_lock:
            self._active_operations[operation_id] = datetime.now()

        try:
            self.trace(f"Starting operation: {operation_name}",
                      operation=operation_name, operation_id=operation_id, **context)

            yield operation_id

            # Success
            duration = time.time() - start_time
            self.perf_tracker.time_operation(operation_name, duration)
            self.perf_tracker.count_operation(operation_name)

            self.performance(f"Completed operation: {operation_name}",
                           operation=operation_name, operation_id=operation_id,
                           duration_ms=duration * 1000, success=True, **context)

        except Exception as e:
            # Error
            duration = time.time() - start_time
            self.perf_tracker.count_error(operation_name)

            self.error(f"Failed operation: {operation_name}",
                      operation=operation_name, operation_id=operation_id,
                      duration_ms=duration * 1000, error=str(e), success=False, **context)
            raise

        finally:
            # Clean up active operation
            with self._operation_lock:
                self._active_operations.pop(operation_id, None)

    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics."""
        return self.perf_tracker.get_stats()

    def reset_performance_stats(self):
        """Reset performance statistics."""
        self.perf_tracker.reset()

    def get_active_operations(self) -> Dict[str, datetime]:
        """Get currently active operations."""
        with self._operation_lock:
            return self._active_operations.copy()

    def flush(self):
        """Flush all log handlers."""
        if self.config.enabled:
            for handler in self._logger.handlers:
                if hasattr(handler, 'flush'):
                    handler.flush()

    def close(self):
        """Close all log handlers."""
        for handler in self._logger.handlers[:]:
            if hasattr(handler, 'close'):
                handler.close()
            self._logger.removeHandler(handler)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.flush()
        if exc_type:
            self.error(f"Exception in logger context: {exc_val}",
                      exception_type=exc_type.__name__)


# Module-level convenience functions for backward compatibility
def get_ai_logger(name: str, config: Optional[LogConfig] = None) -> AILogger:
    """Get AI logger instance."""
    return AILogger.get_logger(name, config)


# Global performance tracking
_global_performance = PerformanceTracker()

def get_global_performance_stats() -> Dict[str, Any]:
    """Get global performance statistics across all loggers."""
    return _global_performance.get_stats()

def reset_global_performance_stats():
    """Reset global performance statistics."""
    _global_performance.reset()