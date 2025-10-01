"""
AI Metrics Collection System

Provides lightweight, optional metrics collection for AI usage tracking.
Supports multiple backends and export formats without requiring external dependencies.
"""

from .core import AIMetrics, MetricType
from .backends import MemoryBackend, FileBackend, StatsDBackend, NullBackend

__all__ = [
    'AIMetrics',
    'MetricType',
    'MemoryBackend',
    'FileBackend',
    'StatsDBackend',
    'NullBackend'
]