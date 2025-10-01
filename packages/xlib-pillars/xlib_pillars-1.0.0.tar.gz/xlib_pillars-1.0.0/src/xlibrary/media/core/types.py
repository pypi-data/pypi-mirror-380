"""
Type definitions for xlibrary.media module.
"""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional, Tuple, Dict, Any, Union, List
from datetime import datetime


class MediaFormat(Enum):
    """Base media formats."""
    IMAGE = "image"
    VIDEO = "video"


class VideoFormat(Enum):
    """Supported video formats."""
    MP4 = "mp4"
    MOV = "mov"
    AVI = "avi"
    MKV = "mkv"
    WEBM = "webm"
    M4V = "m4v"


class ImageFormat(Enum):
    """Supported image formats."""
    JPEG = "jpeg"
    PNG = "png"
    WEBP = "webp"
    BMP = "bmp"
    TIFF = "tiff"


class WatermarkPosition(Enum):
    """Watermark positioning options."""
    TOP_LEFT = "top_left"
    TOP_CENTER = "top_center"
    TOP_RIGHT = "top_right"
    CENTER_LEFT = "center_left"
    CENTER = "center"
    CENTER_RIGHT = "center_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_CENTER = "bottom_center"
    BOTTOM_RIGHT = "bottom_right"


class WatermarkAnimation(Enum):
    """Watermark animation types."""
    NONE = "none"          # Legacy alias for STATIC
    STATIC = "static"      # No animation (default)
    FADE_IN = "fade_in"
    FADE_OUT = "fade_out"
    FADE_IN_OUT = "fade_in_out"
    SCROLL_LEFT = "scroll_left"
    SCROLL_RIGHT = "scroll_right"
    SCROLL_UP = "scroll_up"
    SCROLL_DOWN = "scroll_down"
    CREDITS_ROLL = "credits_roll"
    PULSE = "pulse"
    BOUNCE = "bounce"      # Legacy support


@dataclass
class Resolution:
    """Video/image resolution."""
    width: int
    height: int

    def __str__(self):
        return f"{self.width}x{self.height}"

    @property
    def aspect_ratio(self) -> float:
        return self.width / self.height if self.height > 0 else 0

    @classmethod
    def from_string(cls, resolution_str: str) -> 'Resolution':
        """Parse resolution from string like '1920x1080'."""
        width, height = map(int, resolution_str.split('x'))
        return cls(width, height)


@dataclass
class Position:
    """2D position coordinates."""
    x: int
    y: int


@dataclass
class Size:
    """2D size dimensions."""
    width: int
    height: int


@dataclass
class Margin:
    """Margin specification."""
    top: int = 0
    right: int = 0
    bottom: int = 0
    left: int = 0

    def __init__(self, top: int = 0, right: int = None, bottom: int = None, left: int = None):
        self.top = top
        self.right = right if right is not None else top
        self.bottom = bottom if bottom is not None else top
        self.left = left if left is not None else self.right


@dataclass
class ShadowConfig:
    """Shadow effect configuration."""
    enabled: bool = False
    blur: int = 3
    offset: Tuple[int, int] = (2, 2)
    color: str = "black"
    opacity: float = 0.5


@dataclass
class WatermarkConfig:
    """Advanced watermark configuration with professional features."""
    # Source watermark (PNG with transparency)
    watermark_path: Path

    # Positioning
    position: WatermarkPosition = WatermarkPosition.BOTTOM_RIGHT
    offset_x: int = 20  # Pixels from edge
    offset_y: int = 20  # Pixels from edge

    # Scaling and sizing
    scale_factor: float = 1.0  # Base scale factor
    max_width_percent: float = 0.25  # Max 25% of video width
    max_height_percent: float = 0.25  # Max 25% of video height
    maintain_aspect_ratio: bool = True

    # Transparency and blending
    opacity: float = 0.8  # 0.0 to 1.0
    blend_mode: str = "normal"  # "normal", "multiply", "overlay", etc.

    # Animation settings
    animation: WatermarkAnimation = WatermarkAnimation.NONE
    animation_duration: float = 0.0  # Seconds (0 = entire duration)
    animation_start_time: float = 0.0  # Start time in seconds
    animation_end_time: Optional[float] = None  # End time (None = end of video)

    # Animation-specific parameters
    scroll_speed: int = 50  # Pixels per second for scroll animations
    fade_duration: float = 1.0  # Seconds for fade effects
    pulse_frequency: float = 1.0  # Hz for pulse effect

    # Resolution adaptation
    auto_scale: bool = True  # Enable smart resolution scaling
    min_scale: float = 0.1  # Minimum scale factor
    max_scale: float = 3.0   # Maximum scale factor
    quality_threshold: int = 720  # Above this height, use high-quality scaling

    # Legacy support
    margin: Union[int, Margin] = field(default_factory=lambda: Margin(50))
    min_scale_factor: float = 0.1  # Alias for min_scale
    max_scale_factor: float = 2.0  # Alias for max_scale
    scale_strategy: str = "maintain_quality"  # preserve|fit|crop|maintain_quality
    shadow: Optional[ShadowConfig] = None

    def __post_init__(self):
        """Validate configuration after initialization."""
        if isinstance(self.watermark_path, str):
            self.watermark_path = Path(self.watermark_path)
        if isinstance(self.margin, int):
            self.margin = Margin(self.margin)

        # Sync legacy parameters
        if hasattr(self, 'min_scale_factor'):
            self.min_scale = self.min_scale_factor
        if hasattr(self, 'max_scale_factor'):
            self.max_scale = self.max_scale_factor

        # Clamp values to valid ranges
        self.opacity = max(0.0, min(1.0, self.opacity))
        self.scale_factor = max(0.0, self.scale_factor)
        self.max_width_percent = max(0.01, min(1.0, self.max_width_percent))
        self.max_height_percent = max(0.01, min(1.0, self.max_height_percent))


@dataclass
class ProcessingConfig:
    """Media processing configuration."""
    temp_dir: Optional[Path] = None
    ffmpeg_path: Optional[Path] = None
    quality_preset: str = "medium"  # fast|medium|high|ultra
    enable_hardware_acceleration: bool = False
    max_concurrent_operations: int = 2
    chunk_size: int = 64 * 1024
    preserve_metadata: bool = True

    def __post_init__(self):
        if self.temp_dir and isinstance(self.temp_dir, str):
            self.temp_dir = Path(self.temp_dir)
        if self.ffmpeg_path and isinstance(self.ffmpeg_path, str):
            self.ffmpeg_path = Path(self.ffmpeg_path)


@dataclass
class MediaResult:
    """Result of media processing operations."""
    success: bool
    input_path: Optional[Path] = None
    output_path: Optional[Path] = None
    operation_type: Optional[str] = None
    processing_time: Optional[float] = None
    file_size_before: Optional[int] = None
    file_size_after: Optional[int] = None
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class VideoMetadata:
    """Video file metadata."""
    duration: float
    fps: float
    resolution: Resolution
    bitrate: int
    codec: str
    audio_codec: Optional[str] = None
    file_size: Optional[int] = None
    frame_count: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ImageMetadata:
    """Image file metadata."""
    resolution: Resolution
    format: str
    color_mode: str
    has_alpha: bool = False
    dpi: Optional[Tuple[float, float]] = None
    file_size: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class TimeStamp:
    """Represents a timestamp with multiple format support."""
    seconds: float
    frame: int
    original_format: str
    fps: float

    def __str__(self):
        return f"{self.seconds:.3f}s (frame {self.frame})"

    @classmethod
    def from_seconds(cls, seconds: float, fps: float = 30.0) -> 'TimeStamp':
        """Create from seconds."""
        return cls(
            seconds=seconds,
            frame=int(seconds * fps),
            original_format=f"{seconds}s",
            fps=fps
        )

    @classmethod
    def from_frame(cls, frame: int, fps: float = 30.0) -> 'TimeStamp':
        """Create from frame number."""
        return cls(
            seconds=frame / fps,
            frame=frame,
            original_format=f"f{frame}",
            fps=fps
        )

    @classmethod
    def from_time_string(cls, time_str: str, fps: float = 30.0) -> 'TimeStamp':
        """Create from time string like '2:30.5' or 'f5400'."""
        if time_str.startswith('f'):
            # Frame number format
            frame = int(time_str[1:])
            return cls.from_frame(frame, fps)
        elif ':' in time_str:
            # Time format (MM:SS.fraction or HH:MM:SS.fraction)
            parts = time_str.split(':')
            if len(parts) == 2:
                # MM:SS.fraction
                minutes, seconds = parts
                total_seconds = int(minutes) * 60 + float(seconds)
            elif len(parts) == 3:
                # HH:MM:SS.fraction
                hours, minutes, seconds = parts
                total_seconds = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
            else:
                raise ValueError(f"Invalid time format: {time_str}")
            return cls.from_seconds(total_seconds, fps)
        else:
            # Direct seconds
            return cls.from_seconds(float(time_str), fps)


class MediaError(Exception):
    """Base exception for media processing operations."""
    pass


class UnsupportedFormatError(MediaError):
    """Exception for unsupported media formats."""
    pass


class FFmpegNotFoundError(MediaError):
    """Exception when FFmpeg is not available."""
    pass


class ProcessingError(MediaError):
    """Exception during media processing."""
    pass


class WatermarkError(MediaError):
    """Exception during watermarking operations."""
    pass


class TimestampError(MediaError):
    """Exception for timestamp parsing/processing."""
    pass