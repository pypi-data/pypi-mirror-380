"""
Download Manager Core

Universal download manager for handling media downloads from multiple sources
with robust fallback mechanisms, progress tracking, and queue management.
"""

import json
import os
import threading
import time
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor, Future

from .types import (
    DownloadTask, DownloadConfig, DownloadStatus, DownloadProgress,
    DownloadResult, DownloadStatistics, VideoInfo, DownloadSource,
    ProgressCallback, CompletionCallback, ErrorCallback, VideoQuality
)
from .exceptions import DownloadError, DownloadTimeoutError, ConfigurationError
from ..strategies.manager import StrategyManager
from ..metrics.tracker import DownloadMetricsTracker
from ..metrics.analyzer import MetricsAnalyzer


class DownloadManager:
    """
    Universal download manager with multi-source support and robust fallbacks.

    Features:
    - Multi-threaded download queue with persistence
    - Progress tracking and callbacks
    - Automatic retry with exponential backoff
    - Multiple download strategies with 5-tier fallback
    - Rich statistics and reporting
    - Both enterprise queue API and simple convenience methods
    """

    def __init__(
        self,
        queue_file: Union[str, Path] = None,
        default_output_dir: Union[str, Path] = None,
        max_concurrent: int = 3,
        default_config: Optional[DownloadConfig] = None,
        enable_metrics: bool = False,
        metrics_file: Union[str, Path] = None
    ):
        """
        Initialize download manager with flexible defaults.

        Args:
            queue_file: Path to JSON file for persistent queue state
                       (defaults to ~/.xlibrary/downloads.json)
            default_output_dir: Default download directory
            max_concurrent: Maximum concurrent downloads
            default_config: Default configuration for downloads
            enable_metrics: Enable statistical tracking and optimization
            metrics_file: Path to metrics file (defaults to ~/.xlibrary/download_metrics.json)
        """
        # Set up queue file with smart default
        if queue_file is None:
            cache_dir = Path.home() / ".xlibrary"
            cache_dir.mkdir(exist_ok=True)
            queue_file = cache_dir / "downloads.json"

        self.queue_file = Path(queue_file)
        self.queue_file.parent.mkdir(parents=True, exist_ok=True)

        # Set up default output directory
        self.default_output_dir = default_output_dir
        self.system_downloads = self._get_system_downloads_dir()

        # Configuration
        self.max_concurrent = max_concurrent
        self.default_config = default_config or DownloadConfig()

        # Task management
        self.tasks: Dict[str, DownloadTask] = {}
        self.download_queue = PriorityQueue()
        self.active_downloads: Dict[str, Future] = {}

        # Strategy manager for handling different download methods
        self.strategy_manager = StrategyManager()

        # Thread pool for concurrent downloads
        self.executor = ThreadPoolExecutor(max_workers=max_concurrent, thread_name_prefix="download")

        # Callbacks
        self.progress_callbacks: List[ProgressCallback] = []
        self.completion_callbacks: List[CompletionCallback] = []
        self.error_callbacks: List[ErrorCallback] = []

        # State management
        self.running = False
        self.worker_thread: Optional[threading.Thread] = None
        self.lock = threading.RLock()

        # Statistics
        self.total_downloaded_bytes = 0
        self.total_download_time = 0.0

        # Metrics system
        self.enable_metrics = enable_metrics
        self.metrics_tracker = None
        self.metrics_analyzer = None

        if enable_metrics:
            self.metrics_tracker = DownloadMetricsTracker(
                metrics_file=Path(metrics_file) if metrics_file else None,
                auto_save=True,
                enable_learning=True
            )
            self.metrics_analyzer = MetricsAnalyzer(self.metrics_tracker)
            logger.info("Metrics tracking enabled")

        # Load existing queue and auto-start
        self._load_queue()
        self.start()

    def _get_system_downloads_dir(self) -> str:
        """Get user's Downloads folder from system."""
        downloads_dir = Path.home() / "Downloads"
        if downloads_dir.exists():
            return str(downloads_dir)
        return "."  # Current directory fallback

    def _resolve_output_dir(self, method_output_dir: str = None) -> str:
        """
        Resolve final output directory using priority system.

        Priority: method parameter → constructor default → system Downloads → current dir
        """
        if method_output_dir:
            return method_output_dir

        if self.default_output_dir:
            return str(self.default_output_dir)

        if self.system_downloads != ".":
            return self.system_downloads

        return "."

    def _load_queue(self) -> None:
        """Load existing queue from file."""
        if not self.queue_file.exists():
            return

        try:
            with open(self.queue_file, 'r') as f:
                data = json.load(f)

            # Load tasks
            for task_id, task_data in data.get("tasks", {}).items():
                task = self._task_from_dict(task_data)
                self.tasks[task_id] = task

                # Re-queue pending/failed tasks
                if task.status in [DownloadStatus.PENDING, DownloadStatus.QUEUED]:
                    self.download_queue.put((-task.priority, task.task_id))
                elif task.status == DownloadStatus.FAILED and task.retry_count < task.max_retries:
                    self.download_queue.put((-task.priority, task.task_id))

            # Load statistics
            stats_data = data.get("statistics", {})
            self.total_downloaded_bytes = stats_data.get("total_downloaded_bytes", 0)
            self.total_download_time = stats_data.get("total_download_time", 0.0)

        except Exception as e:
            raise DownloadError(f"Failed to load queue from {self.queue_file}: {e}")

    def _save_queue(self) -> None:
        """Save current queue state to file."""
        try:
            with self.lock:
                data = {
                    "tasks": {
                        task_id: self._task_to_dict(task)
                        for task_id, task in self.tasks.items()
                    },
                    "statistics": {
                        "total_downloaded_bytes": self.total_downloaded_bytes,
                        "total_download_time": self.total_download_time,
                        "last_updated": datetime.now().isoformat()
                    },
                    "metadata": {
                        "version": "1.0",
                        "max_concurrent": self.max_concurrent,
                        "strategy_count": len(self.strategy_manager.available_strategies)
                    }
                }

            with open(self.queue_file, 'w') as f:
                json.dump(data, f, indent=2, default=str)

        except Exception as e:
            raise DownloadError(f"Failed to save queue to {self.queue_file}: {e}")

    def _task_to_dict(self, task: DownloadTask) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization."""
        return {
            "task_id": task.task_id,
            "url": task.url,
            "output_path": str(task.output_path),
            "config": {
                "quality": task.config.quality.value,
                "audio_only": task.config.audio_only,
                "extract_audio": task.config.extract_audio,
                "audio_format": task.config.audio_format,
                "video_format": task.config.video_format,
                "output_template": task.config.output_template,
                "subtitle_languages": task.config.subtitle_languages,
                "embed_subs": task.config.embed_subs,
                "timeout": task.config.timeout,
                "retries": task.config.retries
            },
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat(),
            "status": task.status.value,
            "source": task.source.value,
            "priority": task.priority,
            "retry_count": task.retry_count,
            "max_retries": task.max_retries,
            "metadata": task.metadata,
            "error_history": task.error_history
        }

    def _task_from_dict(self, data: Dict[str, Any]) -> DownloadTask:
        """Create task from dictionary."""
        config_data = data["config"]
        config = DownloadConfig(
            quality=VideoQuality(config_data["quality"]),
            audio_only=config_data["audio_only"],
            extract_audio=config_data["extract_audio"],
            audio_format=config_data["audio_format"],
            video_format=config_data["video_format"],
            output_template=config_data["output_template"],
            subtitle_languages=config_data["subtitle_languages"],
            embed_subs=config_data["embed_subs"],
            timeout=config_data["timeout"],
            retries=config_data["retries"]
        )

        task = DownloadTask(
            task_id=data["task_id"],
            url=data["url"],
            output_path=Path(data["output_path"]),
            config=config,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            status=DownloadStatus(data["status"]),
            source=DownloadSource(data["source"]),
            priority=data["priority"],
            retry_count=data["retry_count"],
            max_retries=data["max_retries"],
            metadata=data["metadata"],
            error_history=data["error_history"]
        )

        return task

    # Enterprise Queue API
    def add_download(
        self,
        url: str,
        output_path: Union[str, Path] = None,
        config: Optional[DownloadConfig] = None,
        priority: int = 0,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add a download task to the queue.

        Args:
            url: URL to download
            output_path: Output directory path (uses defaults if None)
            config: Download configuration (uses default if None)
            priority: Download priority (higher = processed first)
            metadata: Additional metadata

        Returns:
            Task ID for tracking the download
        """
        task_id = str(uuid.uuid4())
        resolved_output_path = Path(self._resolve_output_dir(output_path))
        config = config or self.default_config

        # Detect source
        source = self.strategy_manager.detect_source(url)

        # Get optimal method order from metrics if enabled
        if self.metrics_tracker:
            try:
                optimal_methods = self.metrics_tracker.get_optimal_method_order(url)
                # Update strategy manager with learned preferences
                self.strategy_manager.set_method_order(optimal_methods)
            except Exception as e:
                logger.warning(f"Failed to get optimal method order: {e}")

        task = DownloadTask(
            task_id=task_id,
            url=url,
            output_path=resolved_output_path,
            config=config,
            source=source,
            priority=priority,
            metadata=metadata or {}
        )

        with self.lock:
            self.tasks[task_id] = task
            task.status = DownloadStatus.QUEUED
            self.download_queue.put((-priority, task_id))
            self._save_queue()

        return task_id

    # Simple Convenience API
    def get_audio(self, url: str, output_dir: str = None, format: str = "mp3",
                  quality: str = "best", timeout: int = 300) -> str:
        """
        Download audio and return file path.

        Args:
            url: URL to download from
            output_dir: Where to save (uses defaults if None)
            format: Audio format (mp3, wav, etc.)
            quality: Audio quality
            timeout: Maximum time to wait for download

        Returns:
            Full path to downloaded audio file
        """
        config = DownloadConfig(
            audio_only=True,
            audio_format=format,
            quality=VideoQuality.AUDIO_ONLY if quality == "audio" else VideoQuality.BEST,
            timeout=timeout
        )

        task_id = self.add_download(url, output_dir, config, priority=10)
        return self._wait_for_task_completion(task_id, timeout)

    def get_transcript(self, url: str, output_dir: str = None,
                      languages: List[str] = ["en"], timeout: int = 300) -> str:
        """
        Download transcript/subtitles and return file path.

        Args:
            url: URL to download from
            output_dir: Where to save (uses defaults if None)
            languages: List of subtitle languages to download
            timeout: Maximum time to wait for download

        Returns:
            Full path to downloaded transcript file
        """
        config = DownloadConfig(
            subtitle_languages=languages,
            audio_only=False,  # Need video info to get subtitles
            timeout=timeout
        )

        task_id = self.add_download(url, output_dir, config, priority=10)
        return self._wait_for_task_completion(task_id, timeout)

    def get_video(self, url: str, output_dir: str = None, quality: str = "best",
                  format: str = "mp4", timeout: int = 600) -> str:
        """
        Download video and return file path.

        Args:
            url: URL to download from
            output_dir: Where to save (uses defaults if None)
            quality: Video quality (best, 1080p, 720p, etc.)
            format: Video format
            timeout: Maximum time to wait for download

        Returns:
            Full path to downloaded video file
        """
        quality_enum = VideoQuality.BEST
        if quality in ["1080p", "720p", "480p", "360p", "240p"]:
            quality_enum = VideoQuality(quality)

        config = DownloadConfig(
            quality=quality_enum,
            video_format=format,
            timeout=timeout
        )

        task_id = self.add_download(url, output_dir, config, priority=10)
        return self._wait_for_task_completion(task_id, timeout)

    def get_info(self, url: str) -> Optional[VideoInfo]:
        """Extract video/media information without downloading."""
        return self.strategy_manager.extract_info(url)

    def _wait_for_task_completion(self, task_id: str, timeout: int) -> str:
        """Wait for a task to complete and return the downloaded file path."""
        start_time = time.time()

        while time.time() - start_time < timeout:
            task = self.get_task(task_id)
            if not task:
                raise DownloadError(f"Task {task_id} not found")

            if task.status == DownloadStatus.COMPLETED:
                if task.result and task.result.downloaded_file:
                    return str(task.result.downloaded_file)
                else:
                    raise DownloadError(f"Task completed but no file found")

            elif task.status == DownloadStatus.FAILED:
                error_msg = "Download failed"
                if task.result and task.result.error_message:
                    error_msg = task.result.error_message
                raise DownloadError(error_msg)

            elif task.status == DownloadStatus.CANCELLED:
                raise DownloadError("Download was cancelled")

            time.sleep(0.5)

        raise DownloadTimeoutError(f"Download timed out after {timeout} seconds")

    # Task Management
    def get_task(self, task_id: str) -> Optional[DownloadTask]:
        """Get a task by ID."""
        return self.tasks.get(task_id)

    def get_tasks_by_status(self, status: DownloadStatus) -> List[DownloadTask]:
        """Get all tasks with a specific status."""
        return [task for task in self.tasks.values() if task.status == status]

    def cancel_download(self, task_id: str) -> bool:
        """Cancel a download."""
        task = self.get_task(task_id)
        if not task:
            return False

        with self.lock:
            if task.status in [DownloadStatus.PENDING, DownloadStatus.QUEUED]:
                task.status = DownloadStatus.CANCELLED
                task.updated_at = datetime.now()
                self._save_queue()
                return True
            elif task.status == DownloadStatus.DOWNLOADING:
                if task_id in self.active_downloads:
                    future = self.active_downloads[task_id]
                    future.cancel()
                    task.status = DownloadStatus.CANCELLED
                    task.updated_at = datetime.now()
                    self._save_queue()
                    return True

        return False

    # Worker Management
    def start(self) -> None:
        """Start the download manager worker thread."""
        if self.running:
            return

        self.running = True
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()

    def stop(self) -> None:
        """Stop the download manager."""
        self.running = False

        if self.worker_thread:
            self.worker_thread.join(timeout=5.0)

        with self.lock:
            for future in self.active_downloads.values():
                future.cancel()
            self.active_downloads.clear()

        self.executor.shutdown(wait=True)

    def _worker_loop(self) -> None:
        """Main worker loop for processing download queue."""
        while self.running:
            try:
                if len(self.active_downloads) >= self.max_concurrent:
                    time.sleep(0.1)
                    continue

                if self.download_queue.empty():
                    time.sleep(0.5)
                    continue

                try:
                    priority, task_id = self.download_queue.get_nowait()
                except:
                    time.sleep(0.1)
                    continue

                task = self.get_task(task_id)
                if not task or task.status not in [DownloadStatus.QUEUED, DownloadStatus.FAILED]:
                    continue

                if task.status == DownloadStatus.FAILED and task.retry_count >= task.max_retries:
                    continue

                # Start download
                task.status = DownloadStatus.DOWNLOADING
                task.updated_at = datetime.now()

                future = self.executor.submit(self._download_task, task)
                self.active_downloads[task_id] = future

                future.add_done_callback(lambda f, tid=task_id: self._on_download_complete(tid, f))

            except Exception as e:
                print(f"Worker loop error: {e}")
                time.sleep(1.0)

    def _download_task(self, task: DownloadTask) -> DownloadResult:
        """Execute a download task."""
        def progress_callback(progress: DownloadProgress):
            task.progress = progress
            for callback in self.progress_callbacks:
                try:
                    callback(task.task_id, progress)
                except Exception as e:
                    print(f"Progress callback error: {e}")

        try:
            result = self.strategy_manager.download_with_fallback(
                task.url,
                task.output_path,
                task.config,
                progress_callback
            )
            return result

        except Exception as e:
            return DownloadResult(
                success=False,
                error_message=f"Download task error: {str(e)}"
            )

    def _on_download_complete(self, task_id: str, future: Future) -> None:
        """Handle download completion."""
        with self.lock:
            if task_id in self.active_downloads:
                del self.active_downloads[task_id]

        task = self.get_task(task_id)
        if not task:
            return

        try:
            result = future.result()
            task.result = result
            task.updated_at = datetime.now()

            # Record metrics if enabled
            if self.metrics_tracker:
                try:
                    download_time = result.download_time if result.download_time else 0
                    error_msg = result.error_message if not result.success else None

                    self.metrics_tracker.record_attempt(
                        url=task.url,
                        method=result.method_used.value if result.method_used else "unknown",
                        result=result,
                        download_time=download_time,
                        error_message=error_msg
                    )
                except Exception as e:
                    logger.warning(f"Failed to record metrics: {e}")

            if result.success:
                task.status = DownloadStatus.COMPLETED

                if result.file_size:
                    self.total_downloaded_bytes += result.file_size
                if result.download_time:
                    self.total_download_time += result.download_time

                for callback in self.completion_callbacks:
                    try:
                        callback(task_id, result)
                    except Exception as e:
                        print(f"Completion callback error: {e}")
            else:
                task.status = DownloadStatus.FAILED
                if result.error_message:
                    task.error_history.append(f"{datetime.now().isoformat()}: {result.error_message}")

                if task.retry_count < task.max_retries:
                    task.retry_count += 1
                    threading.Timer(task.config.retry_sleep,
                                  lambda: self.download_queue.put((-task.priority, task_id))).start()

                for callback in self.error_callbacks:
                    try:
                        callback(task_id, task.url, Exception(result.error_message or "Download failed"))
                    except Exception as e:
                        print(f"Error callback error: {e}")

            self._save_queue()

        except Exception as e:
            task.status = DownloadStatus.FAILED
            task.error_history.append(f"{datetime.now().isoformat()}: Future error: {str(e)}")
            task.updated_at = datetime.now()
            self._save_queue()

    # Callback Management
    def add_progress_callback(self, callback: ProgressCallback) -> None:
        """Add a progress callback function."""
        self.progress_callbacks.append(callback)

    def add_completion_callback(self, callback: CompletionCallback) -> None:
        """Add a completion callback function."""
        self.completion_callbacks.append(callback)

    def add_error_callback(self, callback: ErrorCallback) -> None:
        """Add an error callback function."""
        self.error_callbacks.append(callback)

    # Statistics
    # Metrics Methods
    def get_metrics_report(self) -> Optional[Dict[str, Any]]:
        """Get comprehensive metrics report."""
        if not self.metrics_analyzer:
            return None
        return self.metrics_analyzer.analyze_global_performance()

    def get_domain_metrics(self, domain: str) -> Optional[Dict[str, Any]]:
        """Get metrics for a specific domain."""
        if not self.metrics_analyzer:
            return None
        return self.metrics_analyzer.analyze_domain_performance(domain)

    def get_optimization_report(self) -> Optional[Dict[str, Any]]:
        """Get optimization recommendations."""
        if not self.metrics_analyzer:
            return None
        return self.metrics_analyzer.generate_optimization_report()

    def benchmark_url(self, url: str, test_all_methods: bool = False) -> Optional[Dict[str, Any]]:
        """
        Benchmark a URL to get optimal method recommendations.

        Args:
            url: URL to benchmark
            test_all_methods: If True, tests all available methods (for learning)

        Returns:
            Benchmark results and recommendations
        """
        if not self.metrics_tracker:
            return None

        if test_all_methods:
            # This would implement your requested "test all methods" feature
            logger.info(f"Benchmarking all methods for {url}")
            # In a full implementation, this would test yt-dlp, youtube-dl, requests, etc.
            # and record the results for learning

        return self.metrics_tracker.benchmark_url(url)

    def export_metrics(self, output_file: Optional[Path] = None) -> Optional[Path]:
        """Export metrics to file for analysis."""
        if not self.metrics_tracker:
            return None
        return self.metrics_tracker.export_metrics(output_file)

    def get_statistics(self) -> DownloadStatistics:
        """Get comprehensive download statistics."""
        status_counts = {}
        for status in DownloadStatus:
            status_counts[status.value] = len(self.get_tasks_by_status(status))

        source_counts = {}
        for task in self.tasks.values():
            source_counts[task.source.value] = source_counts.get(task.source.value, 0) + 1

        completed_tasks = self.get_tasks_by_status(DownloadStatus.COMPLETED)
        success_rate = len(completed_tasks) / len(self.tasks) if self.tasks else 0.0
        average_speed = self.total_downloaded_bytes / self.total_download_time if self.total_download_time > 0 else 0.0

        return DownloadStatistics(
            total_tasks=len(self.tasks),
            by_status=status_counts,
            by_source=source_counts,
            total_downloaded=self.total_downloaded_bytes,
            total_files=len(completed_tasks),
            average_speed=average_speed,
            total_time=self.total_download_time,
            success_rate=success_rate,
            error_summary=[],  # Simplified for now
            active_downloads=len(self.active_downloads),
            queue_size=self.download_queue.qsize()
        )

    # Context Manager
    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()
        self._save_queue()