"""
Static convenience functions for one-off downloads.

These are simple wrappers around DownloadManager for quick, single-use downloads.
Perfect for scripts, notebooks, and simple automation.
"""

from typing import List, Optional, Dict, Any
from pathlib import Path

from .core.manager import DownloadManager
from .core.types import VideoInfo


def get_audio(url: str, output_dir: str = None, format: str = "mp3",
              quality: str = "best", timeout: int = 300) -> str:
    """
    Download audio from URL. One-off convenience function.

    Args:
        url: URL to download from
        output_dir: Where to save (defaults to ~/Downloads or current dir)
        format: Audio format (mp3, wav, flac, etc.)
        quality: Audio quality ("best", "worst", or specific)
        timeout: Maximum time to wait for download

    Returns:
        Full path to downloaded audio file

    Example:
        audio_file = get_audio("https://youtube.com/watch?v=xyz", "~/Music")
        print(f"Downloaded: {audio_file}")
    """
    with DownloadManager() as manager:
        return manager.get_audio(url, output_dir, format, quality, timeout)


def get_transcript(url: str, output_dir: str = None, languages: List[str] = None,
                   timeout: int = 300) -> str:
    """
    Download transcript/subtitles from URL.

    Args:
        url: URL to download from
        output_dir: Where to save (defaults to ~/Downloads or current dir)
        languages: List of subtitle languages (defaults to ["en"])
        timeout: Maximum time to wait for download

    Returns:
        Full path to downloaded transcript file

    Example:
        transcript = get_transcript("https://youtube.com/watch?v=xyz",
                                   "~/Documents",
                                   languages=["en", "es"])
    """
    if languages is None:
        languages = ["en"]

    with DownloadManager() as manager:
        return manager.get_transcript(url, output_dir, languages, timeout)


def get_video(url: str, output_dir: str = None, quality: str = "best",
              format: str = "mp4", timeout: int = 600) -> str:
    """
    Download video from URL.

    Args:
        url: URL to download from
        output_dir: Where to save (defaults to ~/Downloads or current dir)
        quality: Video quality ("best", "1080p", "720p", "480p", etc.)
        format: Video format (mp4, mkv, avi, etc.)
        timeout: Maximum time to wait for download

    Returns:
        Full path to downloaded video file

    Example:
        video_file = get_video("https://youtube.com/watch?v=xyz",
                              "~/Videos",
                              quality="720p")
    """
    with DownloadManager() as manager:
        return manager.get_video(url, output_dir, quality, format, timeout)


def get_content(url: str, output_dir: str = None,
                include_audio: bool = False, include_video: bool = False,
                include_transcript: bool = False,
                audio_format: str = "mp3", video_format: str = "mp4",
                video_quality: str = "best", transcript_languages: List[str] = None,
                timeout: int = 600) -> Dict[str, str]:
    """
    Download multiple content types from a single URL.

    Args:
        url: URL to download from
        output_dir: Where to save files
        include_audio: Whether to download audio
        include_video: Whether to download video
        include_transcript: Whether to download transcript
        audio_format: Audio format if downloading audio
        video_format: Video format if downloading video
        video_quality: Video quality if downloading video
        transcript_languages: Languages for transcript
        timeout: Maximum time to wait for downloads

    Returns:
        Dictionary with keys like "audio_file", "video_file", "transcript_file"

    Example:
        result = get_content(
            "https://youtube.com/watch?v=xyz",
            "~/Downloads",
            include_audio=True,
            include_transcript=True,
            transcript_languages=["en", "es"]
        )
        print(f"Audio: {result.get('audio_file')}")
        print(f"Transcript: {result.get('transcript_file')}")
    """
    if transcript_languages is None:
        transcript_languages = ["en"]

    result = {}

    with DownloadManager(default_output_dir=output_dir) as manager:
        if include_audio:
            try:
                result["audio_file"] = manager.get_audio(
                    url, output_dir, audio_format, "best", timeout
                )
            except Exception as e:
                result["audio_error"] = str(e)

        if include_video:
            try:
                result["video_file"] = manager.get_video(
                    url, output_dir, video_quality, video_format, timeout
                )
            except Exception as e:
                result["video_error"] = str(e)

        if include_transcript:
            try:
                result["transcript_file"] = manager.get_transcript(
                    url, output_dir, transcript_languages, timeout
                )
            except Exception as e:
                result["transcript_error"] = str(e)

    return result


def get_info(url: str) -> Optional[VideoInfo]:
    """
    Extract video/media information without downloading.

    Args:
        url: URL to extract info from

    Returns:
        VideoInfo object with metadata, or None if extraction fails

    Example:
        info = get_info("https://youtube.com/watch?v=xyz")
        if info:
            print(f"Title: {info.title}")
            print(f"Duration: {info.duration} seconds")
            print(f"Uploader: {info.uploader}")
    """
    with DownloadManager() as manager:
        return manager.get_info(url)


def get_available_formats(url: str) -> Dict[str, List[str]]:
    """
    Query available formats for a URL without downloading.

    Args:
        url: URL to query

    Returns:
        Dictionary with available video formats, audio formats, and qualities

    Example:
        formats = get_available_formats("https://youtube.com/watch?v=xyz")
        print(f"Video formats: {formats['video_formats']}")
        print(f"Audio formats: {formats['audio_formats']}")
        print(f"Available qualities: {formats['qualities']}")
        print(f"Subtitle languages: {formats['subtitle_languages']}")
    """
    info = get_info(url)
    if not info:
        return {
            "video_formats": [],
            "audio_formats": [],
            "qualities": [],
            "subtitle_languages": [],
            "codecs": {"video": [], "audio": []}
        }

    video_formats = set()
    audio_formats = set()
    qualities = set()
    video_codecs = set()
    audio_codecs = set()

    # Extract format information
    for format_info in info.formats:
        # Video formats
        if format_info.get('vcodec') and format_info.get('vcodec') != 'none':
            if format_info.get('ext'):
                video_formats.add(format_info['ext'])
            if format_info.get('vcodec'):
                video_codecs.add(format_info['vcodec'])

            # Quality/resolution
            if format_info.get('height'):
                qualities.add(f"{format_info['height']}p")
            elif format_info.get('format_note'):
                qualities.add(format_info['format_note'])

        # Audio formats
        if format_info.get('acodec') and format_info.get('acodec') != 'none':
            if format_info.get('ext'):
                audio_formats.add(format_info['ext'])
            if format_info.get('acodec'):
                audio_codecs.add(format_info['acodec'])

    # Get subtitle languages
    subtitle_languages = list(info.subtitles.keys()) + list(info.automatic_captions.keys())

    return {
        "video_formats": sorted(list(video_formats)),
        "audio_formats": sorted(list(audio_formats)),
        "qualities": sorted(list(qualities), key=lambda x: int(x.rstrip('p')) if x.rstrip('p').isdigit() else 0, reverse=True),
        "subtitle_languages": sorted(list(set(subtitle_languages))),
        "codecs": {
            "video": sorted(list(video_codecs)),
            "audio": sorted(list(audio_codecs))
        }
    }


def get_optimal_format(url: str, content_type: str = "video", platform: str = "mac") -> Dict[str, str]:
    """
    Get optimal format recommendations for a URL based on platform.

    Args:
        url: URL to analyze
        content_type: "video", "audio", or "transcript"
        platform: "mac", "windows", or "linux"

    Returns:
        Dictionary with recommended format, quality, and codec

    Example:
        optimal = get_optimal_format("https://youtube.com/watch?v=xyz", "video", "mac")
        print(f"Recommended format: {optimal['format']}")
        print(f"Recommended quality: {optimal['quality']}")
        print(f"Recommended codec: {optimal['codec']}")
    """
    available = get_available_formats(url)

    if platform.lower() == "mac":
        from .core.types import DownloadConfig
        config = DownloadConfig.mac_optimized()
    elif platform.lower() == "windows":
        from .core.types import DownloadConfig
        config = DownloadConfig.windows_optimized()
    else:
        from .core.types import DownloadConfig
        config = DownloadConfig.linux_optimized()

    if content_type == "video":
        # Find best video format available
        for preferred_format in config.preferred_video_formats:
            if preferred_format in available["video_formats"]:
                recommended_format = preferred_format
                break
        else:
            recommended_format = available["video_formats"][0] if available["video_formats"] else "mp4"

        # Find best quality
        for preferred_quality in config.preferred_resolutions:
            if preferred_quality in available["qualities"]:
                recommended_quality = preferred_quality
                break
        else:
            recommended_quality = available["qualities"][0] if available["qualities"] else "720p"

        # Find best codec
        for preferred_codec in config.preferred_video_codecs:
            if preferred_codec in available["codecs"]["video"]:
                recommended_codec = preferred_codec
                break
        else:
            recommended_codec = available["codecs"]["video"][0] if available["codecs"]["video"] else "h264"

    elif content_type == "audio":
        # Find best audio format
        for preferred_format in config.preferred_audio_formats:
            if preferred_format in available["audio_formats"]:
                recommended_format = preferred_format
                break
        else:
            recommended_format = available["audio_formats"][0] if available["audio_formats"] else "mp3"

        recommended_quality = "320k"  # Default high quality

        # Find best codec
        for preferred_codec in config.preferred_audio_codecs:
            if preferred_codec in available["codecs"]["audio"]:
                recommended_codec = preferred_codec
                break
        else:
            recommended_codec = available["codecs"]["audio"][0] if available["codecs"]["audio"] else "mp3"

    else:  # transcript
        recommended_format = "srt"  # Most compatible
        recommended_quality = "auto"
        recommended_codec = "utf-8"

    return {
        "format": recommended_format,
        "quality": recommended_quality,
        "codec": recommended_codec,
        "platform_optimized": platform,
        "available_formats": available
    }


# Batch convenience functions
def get_audio_batch(urls: List[str], output_dir: str = None,
                   format: str = "mp3", max_concurrent: int = 3) -> List[str]:
    """
    Download audio from multiple URLs efficiently.

    Args:
        urls: List of URLs to download
        output_dir: Where to save files
        format: Audio format
        max_concurrent: Maximum concurrent downloads

    Returns:
        List of downloaded file paths

    Example:
        urls = ["https://youtube.com/watch?v=1", "https://youtube.com/watch?v=2"]
        files = get_audio_batch(urls, "~/Music", max_concurrent=2)
    """
    results = []

    with DownloadManager(default_output_dir=output_dir, max_concurrent=max_concurrent) as manager:
        # Add all downloads to queue
        task_ids = []
        for url in urls:
            try:
                task_id = manager.add_download(url, output_dir, config=None)
                task_ids.append(task_id)
            except Exception as e:
                results.append(f"Error: {e}")

        # Wait for all to complete (simplified)
        import time
        while True:
            active = len(manager.get_tasks_by_status(manager.DownloadStatus.DOWNLOADING))
            queued = len(manager.get_tasks_by_status(manager.DownloadStatus.QUEUED))

            if active == 0 and queued == 0:
                break

            time.sleep(1)

        # Collect results
        for task_id in task_ids:
            task = manager.get_task(task_id)
            if task and task.result and task.result.success:
                results.append(str(task.result.downloaded_file))
            else:
                results.append(f"Failed: {task.result.error_message if task.result else 'Unknown error'}")

    return results


# Utility functions
def list_supported_sites() -> List[str]:
    """
    List supported video/media sites.

    Returns:
        List of supported site names
    """
    return [
        "YouTube",
        "Vimeo",
        "SoundCloud",
        "Instagram",
        "TikTok",
        "Twitter/X",
        "Dailymotion",
        "Generic HTTP URLs"
    ]


def check_dependencies() -> Dict[str, bool]:
    """
    Check which download tools are available on the system.

    Returns:
        Dictionary mapping tool names to availability status

    Example:
        deps = check_dependencies()
        if deps["yt-dlp"]:
            print("yt-dlp is available")
        else:
            print("Consider installing yt-dlp for better video support")
    """
    import shutil

    tools = {
        "yt-dlp": bool(shutil.which("yt-dlp")),
        "youtube-dl": bool(shutil.which("youtube-dl")),
        "wget": bool(shutil.which("wget")),
        "curl": bool(shutil.which("curl")),
        "requests": True,  # Python built-in
    }

    return tools


def get_transcript_markdown(url: str, output_dir: str = None, languages: List[str] = None,
                           paragraph_min_words: int = 15, preserve_speaker_labels: bool = True,
                           timeout: int = 300) -> Dict[str, str]:
    """
    Download transcript and convert to clean markdown format in one step.

    Args:
        url: URL to download from
        output_dir: Where to save files (defaults to ~/Downloads or current dir)
        languages: List of subtitle languages (defaults to ["en"])
        paragraph_min_words: Minimum words per paragraph
        preserve_speaker_labels: Whether to preserve speaker labels if found
        timeout: Maximum time to wait for download

    Returns:
        Dictionary with both original transcript path and markdown path

    Example:
        result = get_transcript_markdown("https://youtube.com/watch?v=xyz",
                                       "~/Documents",
                                       languages=["en"])
        print(f"Original: {result['transcript_file']}")
        print(f"Markdown: {result['markdown_file']}")
    """
    if languages is None:
        languages = ["en"]

    # First download the transcript
    transcript_path = get_transcript(url, output_dir, languages, timeout)

    # Convert to markdown
    from .transcript_converter import convert_transcript_to_markdown

    conversion_result = convert_transcript_to_markdown(
        transcript_path,
        paragraph_min_words=paragraph_min_words,
        preserve_speaker_labels=preserve_speaker_labels
    )

    return {
        'transcript_file': transcript_path,
        'markdown_file': conversion_result['output_file'],
        'word_count': conversion_result['word_count'],
        'paragraph_count': conversion_result['paragraph_count'],
        'conversion_stats': conversion_result
    }