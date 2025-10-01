"""Configuration-related exceptions."""

from typing import List, Optional, Dict, Any


class ConfigError(Exception):
    """Base exception for configuration errors."""

    def __init__(self, message: str, path: Optional[str] = None, **kwargs):
        self.message = message
        self.path = path
        self.metadata = kwargs
        super().__init__(self.format_message())

    def format_message(self) -> str:
        """Format error message with path information."""
        if self.path:
            return f"Configuration error in '{self.path}': {self.message}"
        return f"Configuration error: {self.message}"


class ValidationError(ConfigError):
    """Exception raised when configuration validation fails."""

    def __init__(self, message: str, path: Optional[str] = None, errors: Optional[List[str]] = None, **kwargs):
        self.errors = errors or []
        super().__init__(message, path, **kwargs)

    def format_message(self) -> str:
        """Format validation error with detailed error list."""
        base_msg = super().format_message()
        if self.errors:
            error_details = "\n".join(f"  - {error}" for error in self.errors)
            return f"{base_msg}\nValidation errors:\n{error_details}"
        return base_msg


class FileNotFoundError(ConfigError):
    """Exception raised when configuration file is not found."""

    def __init__(self, path: str, **kwargs):
        super().__init__(f"Configuration file not found: {path}", path, **kwargs)


class InterpolationError(ConfigError):
    """Exception raised when variable interpolation fails."""

    def __init__(self, message: str, variable: Optional[str] = None, path: Optional[str] = None, **kwargs):
        self.variable = variable
        if variable:
            message = f"Interpolation error for variable '{variable}': {message}"
        super().__init__(message, path, **kwargs)


class InvalidFormatError(ConfigError):
    """Exception raised when configuration file format is invalid."""

    def __init__(self, path: str, format_error: str, **kwargs):
        message = f"Invalid configuration format: {format_error}"
        super().__init__(message, path, **kwargs)


class CircularReferenceError(ConfigError):
    """Exception raised when circular references are detected in interpolation."""

    def __init__(self, variable: str, path: Optional[str] = None, **kwargs):
        message = f"Circular reference detected for variable '{variable}'"
        super().__init__(message, path, **kwargs)