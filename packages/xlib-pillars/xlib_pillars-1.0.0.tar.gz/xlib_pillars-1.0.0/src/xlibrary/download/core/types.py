"""
Type definitions for download management.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union, Callable
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def extract_clean_domain(url: str) -> str:
    """
    Extract clean domain name from URL.

    Examples:
        https://www.youtube.com/watch?v=xyz -> "youtube"
        https://m.youtube.com/watch?v=xyz -> "youtube"
        https://vimeo.com/123456 -> "vimeo"
        https://soundcloud.com/user/track -> "soundcloud"

    Args:
        url: Full URL

    Returns:
        Clean domain name without subdomains and TLD
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        # Remove common subdomains
        domain = domain.replace('www.', '').replace('m.', '').replace('mobile.', '')

        # Extract main domain (remove TLD)
        parts = domain.split('.')
        if len(parts) >= 2:
            # Handle special cases
            if 'youtube' in parts:
                return 'youtube'
            elif 'youtu.be' in domain:
                return 'youtube'
            elif 'vimeo' in parts:
                return 'vimeo'
            elif 'soundcloud' in parts:
                return 'soundcloud'
            elif 'instagram' in parts:
                return 'instagram'
            elif 'tiktok' in parts:
                return 'tiktok'
            elif 'twitter' in parts or 'x.com' in domain:
                return 'twitter'
            else:
                return parts[0]  # First part is usually the main domain

        return domain
    except:
        return "unknown"


class DownloadStatus(Enum):
    """Status of a download operation."""
    PENDING = "pending"
    QUEUED = "queued"
    DOWNLOADING = "downloading"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    PAUSED = "paused"


class DownloadSource(Enum):
    """Supported download sources."""
    YOUTUBE = "youtube"
    GENERIC_HTTP = "generic_http"
    VIMEO = "vimeo"
    DAILYMOTION = "dailymotion"
    SOUNDCLOUD = "soundcloud"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    TWITTER = "twitter"
    UNKNOWN = "unknown"


class VideoQuality(Enum):
    """Video quality options."""
    BEST = "best"
    WORST = "worst"
    HD_1080P = "1080p"
    HD_720P = "720p"
    SD_480P = "480p"
    SD_360P = "360p"
    SD_240P = "240p"
    AUDIO_ONLY = "audio"


class DownloadMethod(Enum):
    """Download methods/tools available."""
    YT_DLP = "yt-dlp"
    YOUTUBE_DL = "youtube-dl"
    REQUESTS = "requests"
    WGET = "wget"
    CURL = "curl"
    ARIA2 = "aria2"


@dataclass
class DownloadConfig:
    """Configuration for download operations with format prioritization."""
    quality: VideoQuality = VideoQuality.BEST
    audio_only: bool = False
    extract_audio: bool = False
    audio_format: str = "mp3"
    video_format: str = "mp4"
    output_template: str = "%(title)s.%(ext)s"
    max_filesize: Optional[int] = None  # MB
    min_filesize: Optional[int] = None  # MB
    subtitle_languages: List[str] = field(default_factory=list)
    embed_subs: bool = False
    write_thumbnail: bool = False
    write_info_json: bool = False
    concurrent_fragments: int = 1
    retries: int = 3
    retry_sleep: int = 5
    timeout: int = 300
    user_agent: Optional[str] = None
    cookies_file: Optional[Path] = None
    proxy: Optional[str] = None
    rate_limit: Optional[int] = None  # KB/s
    prefer_free_formats: bool = False
    merge_output_format: Optional[str] = None

    # Format prioritization - your requested feature!
    preferred_video_formats: List[str] = field(default_factory=lambda: ["mp4", "mkv", "webm", "avi"])
    preferred_audio_formats: List[str] = field(default_factory=lambda: ["mp3", "m4a", "wav", "flac"])
    preferred_transcript_formats: List[str] = field(default_factory=lambda: ["srt", "vtt", "ass", "txt"])

    # Codec preferences
    preferred_video_codecs: List[str] = field(default_factory=lambda: ["h264", "h265", "vp9", "av1"])
    preferred_audio_codecs: List[str] = field(default_factory=lambda: ["aac", "mp3", "opus", "vorbis"])

    # Quality preferences with fallbacks
    preferred_resolutions: List[str] = field(default_factory=lambda: ["1080p", "720p", "480p", "360p"])
    preferred_audio_quality: List[str] = field(default_factory=lambda: ["320k", "256k", "192k", "128k"])

    # Platform-specific optimizations
    optimize_for_platform: Optional[str] = None  # "mac", "windows", "linux", "mobile"

    @classmethod
    def mac_optimized(cls) -> 'DownloadConfig':
        """Create Mac-optimized download configuration."""
        return cls(
            video_format="mp4",
            audio_format="mp3",
            preferred_video_formats=["mp4", "mov", "mkv"],  # MP4 works best on Mac
            preferred_audio_formats=["mp3", "m4a", "aac"],  # Native Mac formats
            preferred_transcript_formats=["srt", "vtt"],     # Standard subtitle formats
            preferred_video_codecs=["h264", "h265"],         # Hardware accelerated on Mac
            preferred_audio_codecs=["aac", "mp3"],           # Native Mac codecs
            optimize_for_platform="mac"
        )

    @classmethod
    def windows_optimized(cls) -> 'DownloadConfig':
        """Create Windows-optimized download configuration."""
        return cls(
            video_format="mp4",
            audio_format="mp3",
            preferred_video_formats=["mp4", "avi", "mkv"],
            preferred_audio_formats=["mp3", "wav", "wma"],
            preferred_transcript_formats=["srt", "ass"],
            optimize_for_platform="windows"
        )

    @classmethod
    def linux_optimized(cls) -> 'DownloadConfig':
        """Create Linux-optimized download configuration."""
        return cls(
            video_format="mkv",
            audio_format="flac",
            preferred_video_formats=["mkv", "webm", "mp4"],
            preferred_audio_formats=["flac", "ogg", "mp3"],
            preferred_transcript_formats=["srt", "ass"],
            optimize_for_platform="linux"
        )


@dataclass
class DownloadProgress:
    """Progress information for a download."""
    downloaded_bytes: int = 0
    total_bytes: Optional[int] = None
    speed: Optional[float] = None  # bytes/sec
    eta: Optional[int] = None  # seconds
    percentage: Optional[float] = None
    status: str = ""
    fragment_index: Optional[int] = None
    fragment_count: Optional[int] = None
    elapsed_time: float = 0.0

    @property
    def download_rate_mbps(self) -> Optional[float]:
        """Get download rate in MB/s."""
        if self.speed:
            return self.speed / (1024 * 1024)
        return None

    @property
    def downloaded_mb(self) -> float:
        """Get downloaded size in MB."""
        return self.downloaded_bytes / (1024 * 1024)

    @property
    def total_mb(self) -> Optional[float]:
        """Get total size in MB."""
        if self.total_bytes:
            return self.total_bytes / (1024 * 1024)
        return None


@dataclass
class VideoInfo:
    """Information about a video/media file."""
    id: str
    title: str
    description: Optional[str] = None
    uploader: Optional[str] = None
    duration: Optional[int] = None  # seconds
    view_count: Optional[int] = None
    like_count: Optional[int] = None
    upload_date: Optional[str] = None
    thumbnail: Optional[str] = None
    webpage_url: Optional[str] = None
    formats: List[Dict[str, Any]] = field(default_factory=list)
    subtitles: Dict[str, List[Dict]] = field(default_factory=dict)
    automatic_captions: Dict[str, List[Dict]] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    categories: List[str] = field(default_factory=list)
    age_limit: Optional[int] = None
    availability: Optional[str] = None
    filesize: Optional[int] = None
    format_id: Optional[str] = None
    format_note: Optional[str] = None
    fps: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    vcodec: Optional[str] = None
    acodec: Optional[str] = None
    abr: Optional[float] = None  # audio bitrate
    vbr: Optional[float] = None  # video bitrate


@dataclass
class DownloadResult:
    """Result of a download operation with comprehensive metadata."""
    success: bool
    downloaded_file: Optional[Path] = None
    info: Optional[VideoInfo] = None
    error_message: Optional[str] = None
    method_used: Optional[DownloadMethod] = None
    download_time: Optional[float] = None
    file_size: Optional[int] = None
    final_progress: Optional[DownloadProgress] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Enhanced metadata fields
    source_domain: Optional[str] = None  # e.g., "youtube", "vimeo" (clean domain name)
    original_url: Optional[str] = None
    final_filename: Optional[str] = None
    file_extension: Optional[str] = None
    actual_format: Optional[str] = None  # The format actually downloaded
    available_formats: List[Dict[str, Any]] = field(default_factory=list)  # All available formats
    quality_selected: Optional[str] = None  # The quality that was actually selected
    available_qualities: List[str] = field(default_factory=list)  # All available qualities
    codec_info: Dict[str, Optional[str]] = field(default_factory=dict)  # video/audio codecs
    resolution: Optional[str] = None  # e.g., "1920x1080"
    duration: Optional[float] = None  # Duration in seconds
    bitrate: Optional[int] = None  # Overall bitrate
    audio_bitrate: Optional[int] = None  # Audio bitrate
    video_bitrate: Optional[int] = None  # Video bitrate
    fps: Optional[float] = None  # Frames per second
    download_speed_mbps: Optional[float] = None  # Average download speed
    fallback_attempts: List[str] = field(default_factory=list)  # Methods that failed before success
    content_type: Optional[str] = None  # "video", "audio", "transcript"
    subtitle_languages: List[str] = field(default_factory=list)  # Available subtitle languages
    thumbnail_url: Optional[str] = None
    upload_date: Optional[str] = None
    uploader: Optional[str] = None
    view_count: Optional[int] = None

    @property
    def file_size_mb(self) -> Optional[float]:
        """Get file size in MB."""
        if self.file_size:
            return self.file_size / (1024 * 1024)
        return None

    @property
    def duration_formatted(self) -> Optional[str]:
        """Get duration as formatted string (HH:MM:SS)."""
        if not self.duration:
            return None

        hours = int(self.duration // 3600)
        minutes = int((self.duration % 3600) // 60)
        seconds = int(self.duration % 60)

        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"

    @property
    def download_summary(self) -> Dict[str, Any]:
        """Get a comprehensive summary of the download."""
        return {
            "success": self.success,
            "source": self.source_domain,
            "method": self.method_used.value if self.method_used else None,
            "format": self.actual_format,
            "quality": self.quality_selected,
            "file_size_mb": self.file_size_mb,
            "duration": self.duration_formatted,
            "download_time": f"{self.download_time:.2f}s" if self.download_time else None,
            "speed_mbps": f"{self.download_speed_mbps:.2f}" if self.download_speed_mbps else None,
            "filename": self.final_filename,
            "uploader": self.uploader,
            "fallback_attempts": len(self.fallback_attempts)
        }


@dataclass
class DownloadTask:
    """A download task with all its information."""
    task_id: str
    url: str
    output_path: Path
    config: DownloadConfig
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    status: DownloadStatus = DownloadStatus.PENDING
    progress: DownloadProgress = field(default_factory=DownloadProgress)
    result: Optional[DownloadResult] = None
    source: DownloadSource = DownloadSource.UNKNOWN
    priority: int = 0  # Higher numbers = higher priority
    retry_count: int = 0
    max_retries: int = 3
    metadata: Dict[str, Any] = field(default_factory=dict)
    error_history: List[str] = field(default_factory=list)


@dataclass
class DownloadStatistics:
    """Statistics about download operations."""
    total_tasks: int
    by_status: Dict[str, int]
    by_source: Dict[str, int]
    total_downloaded: int  # bytes
    total_files: int
    average_speed: float  # bytes/sec
    total_time: float  # seconds
    success_rate: float
    error_summary: List[Dict[str, Any]]
    active_downloads: int
    queue_size: int


# Type aliases for callbacks
ProgressCallback = Callable[[str, DownloadProgress], None]  # task_id, progress
CompletionCallback = Callable[[str, DownloadResult], None]  # task_id, result
ErrorCallback = Callable[[str, str, Exception], None]  # task_id, url, error