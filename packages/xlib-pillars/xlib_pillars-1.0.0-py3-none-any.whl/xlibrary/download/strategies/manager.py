"""
Strategy Manager for Download Operations

Manages the 5-tier fallback system:
1. yt-dlp (best for video platforms)
2. youtube-dl (fallback for video platforms)
3. requests (for direct HTTP downloads)
4. wget (system tool fallback)
5. curl (final system tool fallback)
"""

import subprocess
import shutil
from pathlib import Path
from typing import Optional, List, Callable
from urllib.parse import urlparse

from ..core.types import (
    DownloadConfig, DownloadResult, DownloadProgress, VideoInfo,
    DownloadSource, DownloadMethod
)
from ..core.exceptions import DownloadError, UnsupportedSourceError


class StrategyManager:
    """
    Manages download strategies with intelligent fallback system.

    Automatically detects the best strategy based on URL and available tools,
    then falls back through the hierarchy if needed.
    """

    def __init__(self):
        """Initialize strategy manager and detect available tools."""
        self.available_strategies = []
        self._detect_available_tools()

    def _detect_available_tools(self) -> None:
        """Detect which download tools are available on the system."""
        tools_to_check = [
            ("yt-dlp", DownloadMethod.YT_DLP),
            ("youtube-dl", DownloadMethod.YOUTUBE_DL),
            ("wget", DownloadMethod.WGET),
            ("curl", DownloadMethod.CURL)
        ]

        for tool_name, method in tools_to_check:
            if shutil.which(tool_name):
                self.available_strategies.append(method)

        # requests is always available (Python built-in)
        if DownloadMethod.REQUESTS not in self.available_strategies:
            self.available_strategies.append(DownloadMethod.REQUESTS)

    def detect_source(self, url: str) -> DownloadSource:
        """Detect the source platform from URL."""
        domain = urlparse(url).netloc.lower()

        if "youtube.com" in domain or "youtu.be" in domain:
            return DownloadSource.YOUTUBE
        elif "vimeo.com" in domain:
            return DownloadSource.VIMEO
        elif "soundcloud.com" in domain:
            return DownloadSource.SOUNDCLOUD
        elif "instagram.com" in domain:
            return DownloadSource.INSTAGRAM
        elif "tiktok.com" in domain:
            return DownloadSource.TIKTOK
        elif "twitter.com" in domain or "x.com" in domain:
            return DownloadSource.TWITTER
        elif "dailymotion.com" in domain:
            return DownloadSource.DAILYMOTION
        else:
            return DownloadSource.GENERIC_HTTP

    def extract_info(self, url: str) -> Optional[VideoInfo]:
        """Extract video information without downloading."""
        # Try yt-dlp first for info extraction
        if DownloadMethod.YT_DLP in self.available_strategies:
            return self._extract_info_ytdlp(url)
        elif DownloadMethod.YOUTUBE_DL in self.available_strategies:
            return self._extract_info_youtube_dl(url)

        return None

    def download_with_fallback(
        self,
        url: str,
        output_path: Path,
        config: DownloadConfig,
        progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    ) -> DownloadResult:
        """
        Download using fallback strategy chain.

        Tries strategies in order of preference, falling back if one fails.
        """
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)

        source = self.detect_source(url)
        last_error = None

        # Determine strategy order based on source
        strategy_order = self._get_strategy_order(source)

        for method in strategy_order:
            if method not in self.available_strategies:
                continue

            try:
                if progress_callback:
                    progress_callback(DownloadProgress(
                        status=f"Trying {method.value}..."
                    ))

                result = self._download_with_method(url, output_path, config, method, progress_callback)

                if result.success:
                    result.method_used = method
                    return result

                last_error = result.error_message

            except Exception as e:
                last_error = str(e)
                continue

        # All strategies failed
        return DownloadResult(
            success=False,
            error_message=f"All download strategies failed. Last error: {last_error}"
        )

    def _get_strategy_order(self, source: DownloadSource) -> List[DownloadMethod]:
        """Get preferred strategy order based on source type."""
        if source in [DownloadSource.YOUTUBE, DownloadSource.VIMEO, DownloadSource.SOUNDCLOUD,
                      DownloadSource.INSTAGRAM, DownloadSource.TIKTOK, DownloadSource.TWITTER]:
            # Video platforms: prioritize yt-dlp/youtube-dl
            return [
                DownloadMethod.YT_DLP,
                DownloadMethod.YOUTUBE_DL,
                DownloadMethod.REQUESTS,
                DownloadMethod.WGET,
                DownloadMethod.CURL
            ]
        else:
            # Generic HTTP: prioritize direct download methods
            return [
                DownloadMethod.REQUESTS,
                DownloadMethod.WGET,
                DownloadMethod.CURL,
                DownloadMethod.YT_DLP,
                DownloadMethod.YOUTUBE_DL
            ]

    def _download_with_method(
        self,
        url: str,
        output_path: Path,
        config: DownloadConfig,
        method: DownloadMethod,
        progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    ) -> DownloadResult:
        """Download using a specific method."""

        if method == DownloadMethod.YT_DLP:
            return self._download_ytdlp(url, output_path, config, progress_callback)
        elif method == DownloadMethod.YOUTUBE_DL:
            return self._download_youtube_dl(url, output_path, config, progress_callback)
        elif method == DownloadMethod.REQUESTS:
            return self._download_requests(url, output_path, config, progress_callback)
        elif method == DownloadMethod.WGET:
            return self._download_wget(url, output_path, config, progress_callback)
        elif method == DownloadMethod.CURL:
            return self._download_curl(url, output_path, config, progress_callback)
        else:
            raise DownloadError(f"Unknown download method: {method}")

    def _download_ytdlp(
        self,
        url: str,
        output_path: Path,
        config: DownloadConfig,
        progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    ) -> DownloadResult:
        """Download using yt-dlp."""
        try:
            cmd = ["yt-dlp", "--no-warnings", "--output", f"{output_path}/%(title)s.%(ext)s"]

            if config.audio_only or config.extract_audio:
                cmd.extend(["--extract-audio", "--audio-format", config.audio_format])

            if config.quality.value != "best":
                if config.quality.value == "audio":
                    cmd.extend(["--format", "bestaudio"])
                else:
                    cmd.extend(["--format", f"best[height<={config.quality.value[:-1]}]"])

            if config.subtitle_languages:
                cmd.extend(["--write-subs", "--sub-langs", ",".join(config.subtitle_languages)])
                if config.embed_subs:
                    cmd.append("--embed-subs")

            if config.write_thumbnail:
                cmd.append("--write-thumbnail")

            if config.write_info_json:
                cmd.append("--write-info-json")

            cmd.append(url)

            # Execute command
            process = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout)

            if process.returncode == 0:
                # Find the downloaded file
                downloaded_files = list(output_path.glob("*"))
                if downloaded_files:
                    main_file = max(downloaded_files, key=lambda f: f.stat().st_size)
                    return DownloadResult(
                        success=True,
                        downloaded_file=main_file,
                        file_size=main_file.stat().st_size
                    )

            return DownloadResult(
                success=False,
                error_message=f"yt-dlp failed: {process.stderr}"
            )

        except subprocess.TimeoutExpired:
            return DownloadResult(
                success=False,
                error_message=f"yt-dlp timed out after {config.timeout} seconds"
            )
        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"yt-dlp error: {str(e)}"
            )

    def _download_youtube_dl(
        self,
        url: str,
        output_path: Path,
        config: DownloadConfig,
        progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    ) -> DownloadResult:
        """Download using youtube-dl (fallback for yt-dlp)."""
        # Similar to yt-dlp but with youtube-dl command
        try:
            cmd = ["youtube-dl", "--no-warnings", "--output", f"{output_path}/%(title)s.%(ext)s"]

            if config.audio_only or config.extract_audio:
                cmd.extend(["--extract-audio", "--audio-format", config.audio_format])

            cmd.append(url)

            process = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout)

            if process.returncode == 0:
                downloaded_files = list(output_path.glob("*"))
                if downloaded_files:
                    main_file = max(downloaded_files, key=lambda f: f.stat().st_size)
                    return DownloadResult(
                        success=True,
                        downloaded_file=main_file,
                        file_size=main_file.stat().st_size
                    )

            return DownloadResult(
                success=False,
                error_message=f"youtube-dl failed: {process.stderr}"
            )

        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"youtube-dl error: {str(e)}"
            )

    def _download_requests(
        self,
        url: str,
        output_path: Path,
        config: DownloadConfig,
        progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    ) -> DownloadResult:
        """Download using Python requests library."""
        try:
            import requests

            # Simple filename from URL
            filename = Path(urlparse(url).path).name or "download"
            output_file = output_path / filename

            with requests.get(url, stream=True, timeout=config.timeout) as response:
                response.raise_for_status()

                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0

                with open(output_file, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                            if progress_callback and total_size > 0:
                                progress = DownloadProgress(
                                    downloaded_bytes=downloaded,
                                    total_bytes=total_size,
                                    percentage=(downloaded / total_size) * 100
                                )
                                progress_callback(progress)

            return DownloadResult(
                success=True,
                downloaded_file=output_file,
                file_size=output_file.stat().st_size
            )

        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"requests error: {str(e)}"
            )

    def _download_wget(self, url: str, output_path: Path, config: DownloadConfig,
                      progress_callback: Optional[Callable[[DownloadProgress], None]] = None) -> DownloadResult:
        """Download using wget."""
        try:
            cmd = ["wget", "-P", str(output_path), "--timeout", str(config.timeout), url]

            process = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout + 10)

            if process.returncode == 0:
                # Find the downloaded file (wget creates files based on URL)
                downloaded_files = [f for f in output_path.iterdir() if f.is_file()]
                if downloaded_files:
                    main_file = max(downloaded_files, key=lambda f: f.stat().st_mtime)
                    return DownloadResult(
                        success=True,
                        downloaded_file=main_file,
                        file_size=main_file.stat().st_size
                    )

            return DownloadResult(
                success=False,
                error_message=f"wget failed: {process.stderr}"
            )

        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"wget error: {str(e)}"
            )

    def _download_curl(self, url: str, output_path: Path, config: DownloadConfig,
                      progress_callback: Optional[Callable[[DownloadProgress], None]] = None) -> DownloadResult:
        """Download using curl."""
        try:
            filename = Path(urlparse(url).path).name or "download"
            output_file = output_path / filename

            cmd = ["curl", "-L", "--max-time", str(config.timeout), "-o", str(output_file), url]

            process = subprocess.run(cmd, capture_output=True, text=True, timeout=config.timeout + 10)

            if process.returncode == 0 and output_file.exists():
                return DownloadResult(
                    success=True,
                    downloaded_file=output_file,
                    file_size=output_file.stat().st_size
                )

            return DownloadResult(
                success=False,
                error_message=f"curl failed: {process.stderr}"
            )

        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"curl error: {str(e)}"
            )

    def _extract_info_ytdlp(self, url: str) -> Optional[VideoInfo]:
        """Extract video info using yt-dlp."""
        try:
            import json

            cmd = ["yt-dlp", "--dump-json", "--no-download", url]
            process = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if process.returncode == 0:
                info_data = json.loads(process.stdout)
                return VideoInfo(
                    id=info_data.get("id", ""),
                    title=info_data.get("title", ""),
                    description=info_data.get("description"),
                    uploader=info_data.get("uploader"),
                    duration=info_data.get("duration"),
                    view_count=info_data.get("view_count"),
                    thumbnail=info_data.get("thumbnail"),
                    webpage_url=info_data.get("webpage_url")
                )

        except Exception:
            pass

        return None

    def _extract_info_youtube_dl(self, url: str) -> Optional[VideoInfo]:
        """Extract video info using youtube-dl."""
        # Similar implementation for youtube-dl
        return None  # Simplified for now