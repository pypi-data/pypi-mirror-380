"""
Download Pillar - Universal download manager with multi-source support

Features:
- Universal downloader for YouTube, Vimeo, SoundCloud, Instagram, TikTok, Twitter, and HTTP
- Robust 5-tier fallback strategy (yt-dlp → youtube-dl → requests → wget → curl)
- Multi-threaded queue management with persistence
- Rich progress tracking and statistics
- Both enterprise queue system and simple convenience functions

Usage:
    # Simple one-off downloads
    from xlibrary.download import get_audio, get_transcript, get_video

    audio = get_audio("https://youtube.com/watch?v=xyz", output_dir="~/Music")
    transcript = get_transcript("https://youtube.com/watch?v=xyz", languages=["en"])

    # Enterprise queue system
    from xlibrary.download import DownloadManager

    dm = DownloadManager(default_output_dir="~/Downloads", max_concurrent=3)
    task_id = dm.add_download(url, config=DownloadConfig(audio_only=True))
"""

from .core.manager import DownloadManager
from .metrics import DownloadMetricsTracker, MetricsAnalyzer, DomainPreferences
from .core.types import (
    DownloadStatus,
    DownloadSource,
    VideoQuality,
    DownloadMethod,
    DownloadConfig,
    DownloadProgress,
    DownloadResult,
    DownloadTask,
    DownloadStatistics,
    VideoInfo
)
from .core.exceptions import (
    DownloadError,
    DownloadTimeoutError,
    UnsupportedSourceError,
    NetworkError,
    ConfigurationError
)

# Static convenience functions
from .convenience import (
    get_audio, get_transcript, get_video, get_content, get_info,
    get_audio_batch, list_supported_sites, check_dependencies,
    get_available_formats, get_optimal_format, get_transcript_markdown
)

# Transcript converter
from .transcript_converter import convert_transcript_to_markdown, TranscriptConverter

__version__ = "1.0.0"
__all__ = [
    # Main classes
    "DownloadManager",

    # Types
    "DownloadStatus",
    "DownloadSource",
    "VideoQuality",
    "DownloadMethod",
    "DownloadConfig",
    "DownloadProgress",
    "DownloadResult",
    "DownloadTask",
    "DownloadStatistics",
    "VideoInfo",

    # Exceptions
    "DownloadError",
    "DownloadTimeoutError",
    "UnsupportedSourceError",
    "NetworkError",
    "ConfigurationError",

    # Convenience functions
    "get_audio",
    "get_transcript",
    "get_video",
    "get_content",
    "get_info",
    "get_audio_batch",
    "list_supported_sites",
    "check_dependencies",
    "get_available_formats",
    "get_optimal_format",
    "get_transcript_markdown",

    # Transcript converter
    "convert_transcript_to_markdown",
    "TranscriptConverter"
]