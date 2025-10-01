"""
Advanced logging formatters for AI operations.

Provides structured, JSON, and colored formatting with performance optimization.
"""

import json
import logging
import os
import threading
from datetime import datetime
from typing import Dict, Any, Optional


class StructuredFormatter(logging.Formatter):
    """
    Structured formatter for readable log output.

    Formats log records with structured data in a human-readable format
    while preserving machine parsability.
    """

    def __init__(self, include_caller: bool = True, include_thread: bool = False):
        """
        Initialize structured formatter.

        Args:
            include_caller: Include caller information (file, function, line)
            include_thread: Include thread information
        """
        super().__init__()
        self.include_caller = include_caller
        self.include_thread = include_thread

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with structured data."""
        # Get structured data if available
        structured_data = getattr(record, 'structured_data', None)

        if structured_data:
            # Use pre-formatted structured data
            timestamp = structured_data.get('timestamp', datetime.now().isoformat())
            level = structured_data.get('level', record.levelname)
            logger_name = structured_data.get('logger', record.name)
            message = structured_data.get('message', record.getMessage())

            # Build the formatted message
            parts = [f"[{timestamp}]", f"{level:8}", f"{logger_name:15}", message]

            # Add caller information if available and requested
            if self.include_caller and 'caller' in structured_data:
                caller = structured_data['caller']
                caller_info = f"{caller['file']}:{caller['function']}:{caller['line']}"
                parts.append(f"({caller_info})")

            # Add thread information if requested
            if self.include_thread and 'thread' in structured_data:
                parts.append(f"[{structured_data['thread']}]")

            formatted_msg = " ".join(parts)

            # Add structured data if present
            if 'data' in structured_data:
                data_str = self._format_data(structured_data['data'])
                if data_str:
                    formatted_msg += f" | {data_str}"

            return formatted_msg

        else:
            # Fallback to standard formatting
            timestamp = datetime.fromtimestamp(record.created).isoformat()
            return f"[{timestamp}] {record.levelname:8} {record.name:15} {record.getMessage()}"

    def _format_data(self, data: Dict[str, Any]) -> str:
        """Format structured data for display."""
        if not data:
            return ""

        formatted_pairs = []
        for key, value in data.items():
            if isinstance(value, dict):
                # Nested dict - format compactly
                nested = ", ".join(f"{k}={v}" for k, v in value.items() if v is not None)
                if nested:
                    formatted_pairs.append(f"{key}={{{nested}}}")
            elif isinstance(value, list):
                # List - show length and sample
                if len(value) <= 3:
                    formatted_pairs.append(f"{key}={value}")
                else:
                    formatted_pairs.append(f"{key}=[{len(value)} items: {value[:2]}...]")
            elif isinstance(value, str) and len(value) > 100:
                # Long string - truncate
                formatted_pairs.append(f"{key}='{value[:97]}...'")
            elif value is not None:
                formatted_pairs.append(f"{key}={value}")

        return ", ".join(formatted_pairs)


class JSONFormatter(logging.Formatter):
    """
    JSON formatter for machine-readable log output.

    Formats log records as JSON objects for easy parsing by log aggregators
    and monitoring systems.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        # Get structured data if available
        structured_data = getattr(record, 'structured_data', None)

        if structured_data:
            # Use pre-formatted structured data
            log_entry = structured_data.copy()
        else:
            # Create basic log entry
            log_entry = {
                'timestamp': datetime.fromtimestamp(record.created).isoformat(),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage()
            }

            # Add caller information
            if hasattr(record, 'pathname'):
                log_entry['caller'] = {
                    'file': os.path.basename(record.pathname),
                    'function': record.funcName,
                    'line': record.lineno
                }

            # Add thread information
            if hasattr(record, 'thread'):
                log_entry['thread'] = record.thread

        # Add standard fields
        log_entry['process'] = os.getpid()

        # Add exception information if present
        if record.exc_info:
            log_entry['exception'] = {
                'type': record.exc_info[0].__name__ if record.exc_info[0] else None,
                'message': str(record.exc_info[1]) if record.exc_info[1] else None,
                'traceback': self.formatException(record.exc_info) if record.exc_info else None
            }

        return json.dumps(log_entry, ensure_ascii=False, separators=(',', ':'))


class ColoredFormatter(StructuredFormatter):
    """
    Colored formatter for enhanced console output.

    Extends StructuredFormatter with color coding for different log levels
    and components.
    """

    # ANSI color codes
    COLORS = {
        'TRACE': '\033[90m',      # Bright black (dark gray)
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'REQUEST': '\033[94m',    # Bright blue
        'WARNING': '\033[33m',    # Yellow
        'PERFORMANCE': '\033[35m', # Magenta
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[41m',   # Red background
        'RESET': '\033[0m'        # Reset
    }

    # Component colors
    COMPONENT_COLORS = {
        'manager': '\033[96m',    # Bright cyan
        'provider': '\033[92m',   # Bright green
        'session': '\033[93m',    # Bright yellow
        'health': '\033[95m',     # Bright magenta
        'metrics': '\033[94m',    # Bright blue
        'testing': '\033[91m',    # Bright red
        'limits': '\033[90m'      # Bright black
    }

    def __init__(self, structured: bool = True, include_caller: bool = True, include_thread: bool = False):
        """
        Initialize colored formatter.

        Args:
            structured: Use structured formatting
            include_caller: Include caller information
            include_thread: Include thread information
        """
        super().__init__(include_caller=include_caller, include_thread=include_thread)
        self.structured = structured

        # Detect color support
        self.use_colors = self._supports_color()

    def _supports_color(self) -> bool:
        """Check if terminal supports colors."""
        # Check common environment variables
        if os.getenv('NO_COLOR'):
            return False
        if os.getenv('FORCE_COLOR'):
            return True

        # Check if we're in a terminal
        if not hasattr(os.sys.stdout, 'isatty') or not os.sys.stdout.isatty():
            return False

        # Check TERM variable
        term = os.getenv('TERM', '')
        if 'color' in term or term in ['xterm', 'xterm-256color', 'screen']:
            return True

        return False

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with colors."""
        if not self.use_colors:
            return super().format(record)

        # Get base formatted message
        formatted = super().format(record)

        # Get structured data
        structured_data = getattr(record, 'structured_data', None)
        if not structured_data:
            return formatted

        level = structured_data.get('level', record.levelname)
        logger_name = structured_data.get('logger', record.name)

        # Apply level color
        level_color = self.COLORS.get(level, self.COLORS['RESET'])
        formatted = formatted.replace(f"{level:8}", f"{level_color}{level:8}{self.COLORS['RESET']}")

        # Apply component color to logger name
        component_color = self._get_component_color(logger_name)
        if component_color:
            formatted = formatted.replace(f"{logger_name:15}",
                                        f"{component_color}{logger_name:15}{self.COLORS['RESET']}")

        # Color specific data fields
        if 'data' in structured_data:
            formatted = self._colorize_data(formatted, structured_data['data'])

        return formatted

    def _get_component_color(self, logger_name: str) -> Optional[str]:
        """Get color for logger component."""
        for component, color in self.COMPONENT_COLORS.items():
            if component in logger_name.lower():
                return color
        return None

    def _colorize_data(self, formatted: str, data: Dict[str, Any]) -> str:
        """Add colors to specific data fields."""
        # Color error-related fields
        for error_field in ['error', 'error_type', 'error_message', 'exception']:
            if error_field in data:
                field_str = f"{error_field}={data[error_field]}"
                if field_str in formatted:
                    colored_str = f"{self.COLORS['ERROR']}{field_str}{self.COLORS['RESET']}"
                    formatted = formatted.replace(field_str, colored_str)

        # Color performance fields
        for perf_field in ['duration_ms', 'latency_ms', 'tokens_used', 'cost_usd']:
            if perf_field in data:
                field_str = f"{perf_field}={data[perf_field]}"
                if field_str in formatted:
                    colored_str = f"{self.COLORS['PERFORMANCE']}{field_str}{self.COLORS['RESET']}"
                    formatted = formatted.replace(field_str, colored_str)

        # Color provider/model fields
        for provider_field in ['provider', 'model']:
            if provider_field in data:
                field_str = f"{provider_field}={data[provider_field]}"
                if field_str in formatted:
                    colored_str = f"{self.COLORS['INFO']}{field_str}{self.COLORS['RESET']}"
                    formatted = formatted.replace(field_str, colored_str)

        return formatted


class CompactFormatter(logging.Formatter):
    """
    Compact formatter for high-volume logging scenarios.

    Provides minimal formatting for maximum performance when logging
    large volumes of data.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format record compactly."""
        timestamp = datetime.fromtimestamp(record.created).strftime("%H:%M:%S")
        level_short = record.levelname[0]  # Just first letter
        name_short = record.name.split('.')[-1][:8]  # Last component, max 8 chars

        return f"{timestamp} {level_short} {name_short:8} {record.getMessage()}"


class PerformanceFormatter(logging.Formatter):
    """
    Performance-optimized formatter for minimal overhead.

    Provides basic formatting with maximum performance for high-frequency
    logging scenarios.
    """

    def __init__(self):
        """Initialize performance formatter."""
        super().__init__()
        self._format_cache = {}
        self._cache_lock = threading.Lock()

    def format(self, record: logging.LogRecord) -> str:
        """Format record with caching for performance."""
        # Create cache key from record essentials
        cache_key = (record.levelname, record.name)

        with self._cache_lock:
            if cache_key in self._format_cache:
                prefix = self._format_cache[cache_key]
            else:
                timestamp = datetime.fromtimestamp(record.created).strftime("%H:%M:%S.%f")[:-3]
                prefix = f"{timestamp} {record.levelname:5} {record.name}"
                self._format_cache[cache_key] = prefix

                # Limit cache size
                if len(self._format_cache) > 100:
                    # Remove oldest entries (simple cleanup)
                    keys_to_remove = list(self._format_cache.keys())[:20]
                    for key in keys_to_remove:
                        del self._format_cache[key]

        return f"{prefix} {record.getMessage()}"