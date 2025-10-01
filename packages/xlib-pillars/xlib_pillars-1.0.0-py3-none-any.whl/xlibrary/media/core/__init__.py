"""
Core media processing functionality.
"""

from .manager import MediaManager
from .types import (
    MediaFormat,
    VideoFormat,
    ImageFormat,
    WatermarkPosition,
    WatermarkAnimation,
    Resolution,
    Position,
    Size,
    Margin,
    ShadowConfig,
    WatermarkConfig,
    ProcessingConfig,
    MediaResult,
    VideoMetadata,
    ImageMetadata,
    TimeStamp,
    MediaError,
    UnsupportedFormatError,
    FFmpegNotFoundError,
    ProcessingError,
    WatermarkError,
    TimestampError
)

__all__ = [
    # Main class
    "MediaManager",

    # Enums
    "MediaFormat",
    "VideoFormat",
    "ImageFormat",
    "WatermarkPosition",
    "WatermarkAnimation",

    # Data types
    "Resolution",
    "Position",
    "Size",
    "Margin",
    "ShadowConfig",
    "WatermarkConfig",
    "ProcessingConfig",
    "MediaResult",
    "VideoMetadata",
    "ImageMetadata",
    "TimeStamp",

    # Exceptions
    "MediaError",
    "UnsupportedFormatError",
    "FFmpegNotFoundError",
    "ProcessingError",
    "WatermarkError",
    "TimestampError"
]