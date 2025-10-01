"""
xlibrary.media - Enterprise-grade media processing toolkit

This module provides comprehensive media processing capabilities including:
- Advanced video processing with frame-accurate trimming
- Smart PNG watermarking with resolution-adaptive scaling
- Image processing and format conversion
- Precise timestamp control with multiple format support
- Batch processing for large-scale operations
- FFmpeg integration for professional video workflows

Key Features:
- Single high-resolution master watermark approach
- Resolution-adaptive scaling (320p to 4K+)
- Multi-format timestamp support (2:30.5, f5400, 150.75, etc.)
- Batch operations with progress tracking
- Professional video/image processing pipeline
- macOS thumbnail integration

Usage:
    from xlibrary.media import MediaManager, WatermarkConfig, WatermarkPosition

    mm = MediaManager()

    # Video trimming with flexible timestamps
    result = mm.trim_video(
        "input.mp4",
        start_time="2:30.5",        # 2 minutes 30.5 seconds
        end_time="f5400",           # Frame 5400
        output_path="trimmed.mp4"
    )

    # Smart watermarking
    watermark_config = WatermarkConfig(
        watermark_path="logo.png",
        position=WatermarkPosition.BOTTOM_RIGHT,
        auto_scale=True,
        opacity=0.8
    )

    result = mm.watermark_video("video.mp4", watermark_config, "branded.mp4")
"""

from .core.manager import MediaManager
from .watermark import WatermarkEngine
from .animation import AnimationEngine
from .core.types import (
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
from .utils import (
    TimeStampParser,
    parse_timestamp,
    timestamp_to_frame,
    frame_to_timestamp,
    detect_timestamp_format,
    validate_timestamp,
    seconds_to_hms,
    normalize_timestamp
)

__version__ = "1.0.0"
__all__ = [
    # Main classes
    "MediaManager",
    "WatermarkEngine",
    "AnimationEngine",

    # Configuration classes
    "WatermarkConfig",
    "ProcessingConfig",

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
    "MediaResult",
    "VideoMetadata",
    "ImageMetadata",
    "TimeStamp",

    # Utility classes and functions
    "TimeStampParser",
    "parse_timestamp",
    "timestamp_to_frame",
    "frame_to_timestamp",
    "detect_timestamp_format",
    "validate_timestamp",
    "seconds_to_hms",
    "normalize_timestamp",

    # Exceptions
    "MediaError",
    "UnsupportedFormatError",
    "FFmpegNotFoundError",
    "ProcessingError",
    "WatermarkError",
    "TimestampError"
]