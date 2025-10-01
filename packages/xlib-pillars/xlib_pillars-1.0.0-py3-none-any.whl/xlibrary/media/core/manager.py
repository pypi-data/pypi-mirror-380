"""
Main MediaManager class that orchestrates all media processing operations.
"""

import os
import shutil
import logging
import tempfile
import time
from pathlib import Path
from typing import Optional, Union, List, Dict, Any, Callable
from datetime import datetime

from .types import (
    WatermarkConfig, ProcessingConfig, MediaResult, VideoMetadata, ImageMetadata,
    VideoFormat, ImageFormat, TimeStamp, Resolution, WatermarkPosition,
    MediaError, UnsupportedFormatError, FFmpegNotFoundError, ProcessingError,
    WatermarkError
)
from ..utils import parse_timestamp, TimeStampParser
from ..watermark import WatermarkEngine
from ..animation import AnimationEngine

# Standard library imports for real FFmpeg integration
import subprocess
import json
import tempfile

# Optional dependencies
try:
    import ffmpeg
    FFMPEG_AVAILABLE = True
except ImportError:
    FFMPEG_AVAILABLE = False

try:
    from PIL import Image, ImageEnhance, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class MediaManager:
    """
    Central manager for all media processing operations.

    This class provides a unified interface for:
    - PNG overlay watermarking with smart scaling
    - Video processing (clipping, watermarking, thumbnails)
    - Image processing (conversion, resizing, optimization)
    - Keyframe/thumbnail control for macOS

    Features:
    - Single high-resolution master watermark approach
    - Resolution-adaptive scaling (320p to 4K+)
    - Animation support for watermarks
    - FFmpeg-based video processing
    - Consistent API across all operations
    """

    def __init__(
        self,
        config: Optional[ProcessingConfig] = None,
        logger: Optional[logging.Logger] = None
    ):
        """
        Initialize MediaManager.

        Args:
            config: Processing configuration (uses defaults if None)
            logger: Optional logger instance
        """
        self.config = config or ProcessingConfig()
        self.logger = logger or logging.getLogger(__name__)

        # Initialize components
        self._initialize_dependencies()
        self._setup_temp_directory()

        # Processing statistics
        self.stats = {
            "operations_completed": 0,
            "total_processing_time": 0.0,
            "files_processed": 0,
            "errors": 0,
            "operations_by_type": {}
        }

        # Timestamp parser
        self.timestamp_parser = TimeStampParser()

    def _initialize_dependencies(self):
        """Check and initialize required dependencies."""
        if not FFMPEG_AVAILABLE and not PIL_AVAILABLE:
            raise MediaError(
                "No media processing libraries available. Install with: pip install xlibrary[media]"
            )

        # Check FFmpeg availability
        self.ffmpeg_path = self._find_ffmpeg()
        if not self.ffmpeg_path:
            self.logger.warning("FFmpeg not found. Video operations will not be available.")

    def _find_ffmpeg(self) -> Optional[Path]:
        """Find FFmpeg binary and verify it works."""
        if self.config.ffmpeg_path and self.config.ffmpeg_path.exists():
            ffmpeg_path = self.config.ffmpeg_path
        else:
            # Check common locations
            for path_str in [shutil.which("ffmpeg"), "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg"]:
                if path_str and Path(path_str).exists():
                    ffmpeg_path = Path(path_str)
                    break
            else:
                return None

        # Verify FFmpeg works
        try:
            result = subprocess.run(
                [str(ffmpeg_path), "-version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                self.logger.debug(f"FFmpeg verified: {ffmpeg_path}")
                return ffmpeg_path
            else:
                self.logger.warning(f"FFmpeg at {ffmpeg_path} not working properly")
                return None
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            self.logger.warning(f"FFmpeg verification failed: {e}")
            return None

    def _setup_temp_directory(self):
        """Setup temporary directory for processing."""
        if self.config.temp_dir:
            self.temp_dir = self.config.temp_dir
            self.temp_dir.mkdir(parents=True, exist_ok=True)
        else:
            self.temp_dir = Path(tempfile.gettempdir()) / "xlibrary_media"
            self.temp_dir.mkdir(parents=True, exist_ok=True)

    def create_watermark_config(
        self,
        watermark_path: Union[str, Path],
        position: WatermarkPosition = WatermarkPosition.BOTTOM_RIGHT,
        opacity: float = 0.8,
        margin: int = 50,
        max_width_percent: float = 0.25,
        **kwargs
    ) -> WatermarkConfig:
        """
        Create watermark configuration with sensible defaults.

        Args:
            watermark_path: Path to watermark image
            position: Watermark position
            opacity: Watermark opacity (0.0 to 1.0)
            margin: Margin from edges in pixels
            max_width_percent: Maximum width as percentage of video width
            **kwargs: Additional WatermarkConfig parameters

        Returns:
            WatermarkConfig object
        """
        return WatermarkConfig(
            watermark_path=Path(watermark_path),
            position=position,
            opacity=opacity,
            margin=margin,
            max_width_percent=max_width_percent,
            **kwargs
        )

    def _update_stats(self, operation_type: str, result: MediaResult):
        """Update processing statistics."""
        self.stats["operations_completed"] += 1

        if result.success:
            self.stats["files_processed"] += 1
            if result.processing_time:
                self.stats["total_processing_time"] += result.processing_time
        else:
            self.stats["errors"] += 1

        if operation_type not in self.stats["operations_by_type"]:
            self.stats["operations_by_type"][operation_type] = {"success": 0, "error": 0}

        if result.success:
            self.stats["operations_by_type"][operation_type]["success"] += 1
        else:
            self.stats["operations_by_type"][operation_type]["error"] += 1

    # Video Processing Methods

    def trim_video(
        self,
        input_path: Union[str, Path],
        start_time: Union[str, int, float],
        end_time: Union[str, int, float],
        output_path: Union[str, Path],
        preserve_audio: bool = True,
        preserve_metadata: bool = True,
        copy_streams: bool = False
    ) -> MediaResult:
        """
        Trim video with frame-accurate precision.

        Args:
            input_path: Path to input video
            start_time: Start timestamp (flexible format)
            end_time: End timestamp (flexible format)
            output_path: Path to output video
            preserve_audio: Whether to preserve audio streams
            preserve_metadata: Whether to preserve metadata
            copy_streams: Whether to copy streams without re-encoding

        Returns:
            MediaResult with operation details
        """
        start_timestamp = time.time()
        input_path = Path(input_path)
        output_path = Path(output_path)

        try:
            if not self.ffmpeg_path:
                raise FFmpegNotFoundError("FFmpeg not available for video operations")

            # Get video info for accurate timestamp parsing
            video_info = self._get_video_info_basic(input_path)
            fps = video_info["fps"]
            max_duration = video_info["duration"]

            # Parse timestamps with clamping
            start_ts = parse_timestamp(start_time, fps)
            end_ts = parse_timestamp(end_time, fps)

            # Clamp to video bounds
            start_seconds = max(0, min(start_ts.seconds, max_duration))
            end_seconds = max(start_seconds + 0.1, min(end_ts.seconds, max_duration))
            duration_seconds = end_seconds - start_seconds

            if duration_seconds <= 0:
                raise ProcessingError("End time must be after start time")

            # Get input file size
            file_size_before = input_path.stat().st_size

            # Create output directory if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Build FFmpeg command for precise video trimming
            cmd = [
                str(self.ffmpeg_path),
                "-y",  # Overwrite output
                "-ss", str(start_seconds),  # Seek to start
                "-i", str(input_path),  # Input file
                "-t", str(duration_seconds),  # Duration
            ]

            # Preserve streams based on parameters
            if copy_streams:
                cmd.extend(["-c", "copy"])  # Stream copy for speed
            else:
                cmd.extend(["-c:v", "libx264", "-preset", "medium"])

            if preserve_audio:
                if not copy_streams:
                    cmd.extend(["-c:a", "aac"])
            else:
                cmd.extend(["-an"])  # No audio

            # Preserve metadata
            if preserve_metadata:
                cmd.extend(["-map_metadata", "0"])

            # Handle timestamp issues
            cmd.extend(["-avoid_negative_ts", "make_zero"])

            # Output file
            cmd.append(str(output_path))

            self.logger.info(f"Trimming video from {start_seconds}s to {end_seconds}s (duration: {duration_seconds}s)")
            self.logger.debug(f"FFmpeg command: {' '.join(cmd)}")

            # Execute FFmpeg command
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                raise ProcessingError(f"Video trimming failed: {result.stderr}")

            processing_time = time.time() - start_timestamp

            # Get output video info
            try:
                output_info = self._get_video_info_basic(output_path)
                output_duration = output_info["duration"]
            except:
                output_duration = duration_seconds  # Fallback

            result = MediaResult(
                success=True,
                input_path=input_path,
                output_path=output_path,
                operation_type="video_trim",
                processing_time=processing_time,
                file_size_before=file_size_before,
                file_size_after=output_path.stat().st_size,
                metadata={
                    "start_time": start_seconds,
                    "end_time": end_seconds,
                    "duration": output_duration,
                    "preserve_audio": preserve_audio,
                    "copy_streams": copy_streams,
                    "original_duration": max_duration
                }
            )

            self._update_stats("video_trim", result)
            return result

        except Exception as e:
            processing_time = time.time() - start_timestamp
            result = MediaResult(
                success=False,
                input_path=input_path,
                output_path=output_path,
                operation_type="video_trim",
                processing_time=processing_time,
                error_message=str(e)
            )
            self._update_stats("video_trim", result)
            return result

    def watermark_video(
        self,
        video_path: Union[str, Path],
        watermark_config: WatermarkConfig,
        output_path: Union[str, Path],
        start_time: Optional[Union[str, float]] = None,
        end_time: Optional[Union[str, float]] = None
    ) -> MediaResult:
        """
        Add watermark to video with smart scaling.

        Args:
            video_path: Path to input video
            watermark_config: Watermark configuration
            output_path: Path to output video
            start_time: Optional start time for watermark
            end_time: Optional end time for watermark

        Returns:
            MediaResult with operation details
        """
        start_timestamp = time.time()
        video_path = Path(video_path)
        output_path = Path(output_path)

        try:
            if not self.ffmpeg_path:
                raise FFmpegNotFoundError("FFmpeg not available for video watermarking")

            if not watermark_config.watermark_path.exists():
                raise WatermarkError(f"Watermark file not found: {watermark_config.watermark_path}")

            # Get video info
            video_info = self._get_video_info_basic(video_path)
            target_resolution = video_info["resolution"]
            video_duration = video_info["duration"]

            file_size_before = video_path.stat().st_size

            # Create output directory
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Determine if animation is needed
            from ..core.types import WatermarkAnimation
            needs_animation = (
                watermark_config.animation != WatermarkAnimation.STATIC and
                watermark_config.animation != WatermarkAnimation.NONE
            )

            if needs_animation:
                # Use animation engine for complex animations
                try:
                    animation_engine = AnimationEngine(watermark_config, self.logger)
                    result = animation_engine.apply_animated_watermark(
                        video_path, output_path, target_resolution,
                        video_duration, datetime.fromtimestamp(start_timestamp)
                    )

                    # Update result with timing constraints if specified
                    if start_time is not None or end_time is not None:
                        if start_time is not None:
                            start_ts = parse_timestamp(start_time, video_info["fps"])
                            result.metadata["start_constraint"] = start_ts.seconds
                        if end_time is not None:
                            end_ts = parse_timestamp(end_time, video_info["fps"])
                            result.metadata["end_constraint"] = end_ts.seconds

                    return result

                except Exception as e:
                    self.logger.warning(f"Animation failed, falling back to static: {e}")
                    # Fall through to static watermark

            # Static watermark using FFmpeg overlay filter
            watermark_engine = WatermarkEngine(watermark_config, self.logger)

            # Get scaled watermark and position
            watermark_image = watermark_engine.get_scaled_watermark(target_resolution)
            position = watermark_engine.calculate_position(
                Size(watermark_image.size[0], watermark_image.size[1]),
                target_resolution
            )

            # Save scaled watermark to temporary file
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_wm:
                watermark_image.save(temp_wm.name)
                temp_watermark_path = temp_wm.name

            try:
                # Build FFmpeg command with overlay filter
                cmd = [
                    str(self.ffmpeg_path),
                    "-y",  # Overwrite output
                    "-i", str(video_path),  # Input video
                    "-i", temp_watermark_path,  # Watermark image
                ]

                # Time-based filtering if specified
                if start_time is not None or end_time is not None:
                    # Parse time constraints
                    start_seconds = 0.0
                    end_seconds = video_duration

                    if start_time is not None:
                        start_ts = parse_timestamp(start_time, video_info["fps"])
                        start_seconds = max(0, min(start_ts.seconds, video_duration))

                    if end_time is not None:
                        end_ts = parse_timestamp(end_time, video_info["fps"])
                        end_seconds = max(start_seconds, min(end_ts.seconds, video_duration))

                    # Apply time-based overlay
                    overlay_filter = f"[0:v][1:v] overlay={position.x}:{position.y}:enable='between(t,{start_seconds},{end_seconds})'"
                else:
                    # Apply watermark for entire duration
                    overlay_filter = f"[0:v][1:v] overlay={position.x}:{position.y}"

                cmd.extend([
                    "-filter_complex", overlay_filter,
                    "-c:a", "copy",  # Copy audio stream
                    "-preset", self.config.quality_preset,  # Quality preset
                    str(output_path)
                ])

                self.logger.info(f"Applying static watermark at position ({position.x}, {position.y}) with size {watermark_image.size}")
                self.logger.debug(f"FFmpeg command: {' '.join(cmd)}")

                # Execute FFmpeg command
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
                if result.returncode != 0:
                    raise ProcessingError(f"Video watermarking failed: {result.stderr}")

                processing_time = time.time() - start_timestamp

                # Get watermark cache performance info
                cache_info = watermark_engine.get_cache_info()

                result = MediaResult(
                    success=True,
                    input_path=video_path,
                    output_path=output_path,
                    operation_type="video_watermark",
                    processing_time=processing_time,
                    file_size_before=file_size_before,
                    file_size_after=output_path.stat().st_size,
                    metadata={
                        "watermark_path": str(watermark_config.watermark_path),
                        "position": watermark_config.position.value,
                        "animation": watermark_config.animation.value,
                        "watermark_size": f"{watermark_image.size[0]}x{watermark_image.size[1]}",
                        "position_coords": f"{position.x},{position.y}",
                        "opacity": watermark_config.opacity,
                        "video_duration": video_duration,
                        "cache_hit_rate": f"{cache_info['hit_rate']:.1%}" if cache_info["total_requests"] > 0 else "0%"
                    }
                )

            finally:
                # Clean up temporary watermark file
                Path(temp_watermark_path).unlink(missing_ok=True)

            self._update_stats("video_watermark", result)
            return result

        except Exception as e:
            processing_time = time.time() - start_timestamp
            result = MediaResult(
                success=False,
                input_path=video_path,
                output_path=output_path,
                operation_type="video_watermark",
                processing_time=processing_time,
                error_message=str(e)
            )
            self._update_stats("video_watermark", result)
            return result

    def extract_video_frame(
        self,
        video_path: Union[str, Path],
        timestamp: Union[str, int, float],
        output_path: Union[str, Path],
        format: str = "jpg",
        quality: int = 95
    ) -> MediaResult:
        """
        Extract single frame at precise timestamp.

        Args:
            video_path: Path to input video
            timestamp: Timestamp for frame extraction
            output_path: Path to output image
            format: Output image format
            quality: Image quality (1-100)

        Returns:
            MediaResult with operation details
        """
        start_timestamp = time.time()
        video_path = Path(video_path)
        output_path = Path(output_path)

        try:
            if not self.ffmpeg_path:
                raise FFmpegNotFoundError("FFmpeg not available for frame extraction")

            # Get video info for accurate timestamp parsing and clamping
            video_info = self._get_video_info_basic(video_path)
            fps = video_info["fps"]
            max_duration = video_info["duration"]

            # Parse timestamp with clamping
            ts = parse_timestamp(timestamp, fps)
            time_seconds = max(0, min(ts.seconds, max_duration))

            if time_seconds != ts.seconds:
                self.logger.warning(f"Timestamp clamped from {ts.seconds}s to {time_seconds}s")

            file_size_before = video_path.stat().st_size

            # Create output directory
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Build FFmpeg command for frame extraction
            cmd = [
                str(self.ffmpeg_path),
                "-y",  # Overwrite output
                "-ss", str(time_seconds),  # Seek to timestamp
                "-i", str(video_path),  # Input video
                "-frames:v", "1",  # Extract one frame
                "-q:v", str(min(31, max(1, 31 - quality // 3))),  # Quality scale (FFmpeg uses 1-31, lower = better)
            ]

            # Set output format
            if format.lower() in ['jpg', 'jpeg']:
                cmd.extend(["-f", "mjpeg"])
            elif format.lower() == 'png':
                cmd.extend(["-f", "image2", "-vcodec", "png"])
            else:
                cmd.extend(["-f", "image2"])

            cmd.append(str(output_path))

            self.logger.info(f"Extracting frame at {time_seconds}s (frame {int(time_seconds * fps)})")
            self.logger.debug(f"FFmpeg command: {' '.join(cmd)}")

            # Execute FFmpeg command
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                raise ProcessingError(f"Frame extraction failed: {result.stderr}")

            processing_time = time.time() - start_timestamp

            # Get extracted image dimensions using PIL
            try:
                with Image.open(output_path) as img:
                    image_resolution = img.size
            except Exception:
                image_resolution = (video_info["resolution"].width, video_info["resolution"].height)

            result = MediaResult(
                success=True,
                input_path=video_path,
                output_path=output_path,
                operation_type="frame_extraction",
                processing_time=processing_time,
                file_size_before=file_size_before,
                file_size_after=output_path.stat().st_size,
                metadata={
                    "timestamp": time_seconds,
                    "frame": int(time_seconds * fps),
                    "format": format,
                    "quality": quality,
                    "image_resolution": f"{image_resolution[0]}x{image_resolution[1]}",
                    "video_fps": fps,
                    "video_duration": max_duration
                }
            )

            self._update_stats("frame_extraction", result)
            return result

        except Exception as e:
            processing_time = time.time() - start_timestamp
            result = MediaResult(
                success=False,
                input_path=video_path,
                output_path=output_path,
                operation_type="frame_extraction",
                processing_time=processing_time,
                error_message=str(e)
            )
            self._update_stats("frame_extraction", result)
            return result

    def get_video_info(self, video_path: Union[str, Path]) -> VideoMetadata:
        """
        Get comprehensive video metadata and properties.

        Args:
            video_path: Path to video file

        Returns:
            VideoMetadata object
        """
        video_path = Path(video_path)

        try:
            # In production, this would use ffprobe
            info = self._get_video_info_basic(video_path)

            return VideoMetadata(
                duration=info["duration"],
                fps=info["fps"],
                resolution=info["resolution"],
                bitrate=info["bitrate"],
                codec=info["codec"],
                audio_codec=info.get("audio_codec"),
                file_size=video_path.stat().st_size,
                frame_count=int(info["duration"] * info["fps"]),
                metadata=info.get("metadata", {})
            )

        except Exception as e:
            raise ProcessingError(f"Failed to get video info: {e}")

    def _get_video_info_basic(self, video_path: Path) -> Dict[str, Any]:
        """Get video information using ffprobe."""
        if not self.ffmpeg_path:
            raise FFmpegNotFoundError("FFmpeg not available for video info")

        try:
            # Use ffprobe to get detailed video information
            ffprobe_path = self.ffmpeg_path.parent / "ffprobe"
            if not ffprobe_path.exists():
                ffprobe_path = shutil.which("ffprobe")
                if not ffprobe_path:
                    raise FFmpegNotFoundError("ffprobe not found")

            cmd = [
                str(ffprobe_path),
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(video_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                raise ProcessingError(f"ffprobe failed: {result.stderr}")

            info = json.loads(result.stdout)

            # Extract video stream info
            video_stream = None
            for stream in info.get("streams", []):
                if stream.get("codec_type") == "video":
                    video_stream = stream
                    break

            if not video_stream:
                raise ProcessingError("No video stream found")

            # Parse frame rate (can be a fraction like "30000/1001")
            fps_str = video_stream.get("r_frame_rate", "30/1")
            if "/" in fps_str:
                num, den = map(float, fps_str.split("/"))
                fps = num / den if den != 0 else 30.0
            else:
                fps = float(fps_str)

            return {
                "duration": float(info["format"].get("duration", 0)),
                "fps": fps,
                "resolution": Resolution(int(video_stream.get("width", 0)), int(video_stream.get("height", 0))),
                "bitrate": int(info["format"].get("bit_rate", 0)),
                "codec": video_stream.get("codec_name", "unknown"),
                "audio_codec": self._get_audio_codec(info.get("streams", [])),
                "metadata": info["format"].get("tags", {})
            }

        except json.JSONDecodeError as e:
            raise ProcessingError(f"Failed to parse video info: {e}")
        except Exception as e:
            raise ProcessingError(f"Failed to get video info: {e}")

    def _get_audio_codec(self, streams: List[Dict]) -> Optional[str]:
        """Extract audio codec from stream list."""
        for stream in streams:
            if stream.get("codec_type") == "audio":
                return stream.get("codec_name")
        return None

    def _calculate_watermark_scale(self, video_resolution: Resolution, config: WatermarkConfig) -> float:
        """Calculate appropriate watermark scale factor using enhanced engine."""
        try:
            # Create temporary watermark engine to calculate optimal scaling
            watermark_engine = WatermarkEngine(config, self.logger)

            # Get optimal size for resolution
            optimal_size = watermark_engine.calculate_optimal_size(video_resolution)

            # Calculate scale factor based on master watermark
            master_size = watermark_engine._master_watermark.size
            scale_factor = optimal_size.width / master_size[0]

            return scale_factor

        except Exception as e:
            self.logger.warning(f"Failed to calculate smart watermark scale: {e}, using fallback")

            # Fallback to simple scaling
            if not config.auto_scale:
                return config.scale_factor

            max_width = video_resolution.width * config.max_width_percent
            # Estimate based on typical watermark size
            estimated_watermark_width = 400

            scale_factor = max_width / estimated_watermark_width
            scale_factor = max(config.min_scale, min(config.max_scale, scale_factor))

            return scale_factor

    # Image Processing Methods

    def watermark_image(
        self,
        image_path: Union[str, Path],
        watermark_config: WatermarkConfig,
        output_path: Union[str, Path]
    ) -> MediaResult:
        """
        Add watermark to image with smart positioning and scaling.

        Args:
            image_path: Path to input image
            watermark_config: Watermark configuration
            output_path: Path to output image

        Returns:
            MediaResult with operation details
        """
        image_path = Path(image_path)
        output_path = Path(output_path)

        try:
            if not PIL_AVAILABLE:
                raise MediaError("PIL not available for image operations")

            # Create output directory
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Create watermark engine with advanced scaling
            watermark_engine = WatermarkEngine(watermark_config, self.logger)

            # Apply watermark using enhanced engine
            result = watermark_engine.apply_to_image_file(image_path, output_path)

            # Update statistics
            self._update_stats("image_watermark", result)

            # Log cache performance
            cache_info = watermark_engine.get_cache_info()
            self.logger.debug(f"Watermark cache performance: {cache_info['hit_rate']:.1%} hit rate")

            return result

        except Exception as e:
            result = MediaResult(
                success=False,
                input_path=image_path,
                output_path=output_path,
                operation_type="image_watermark",
                error_message=str(e)
            )
            self._update_stats("image_watermark", result)
            return result

    # Batch Operations

    def batch_watermark_videos(
        self,
        input_pattern: Union[str, List[str]],
        watermark_config: WatermarkConfig,
        output_dir: Union[str, Path],
        max_concurrent: int = 2,
        on_progress: Optional[Callable] = None,
        on_complete: Optional[Callable] = None,
        on_error: Optional[Callable] = None
    ) -> List[MediaResult]:
        """
        Batch watermark multiple videos efficiently.

        Args:
            input_pattern: Glob pattern or list of video paths
            watermark_config: Watermark configuration
            output_dir: Output directory
            max_concurrent: Maximum concurrent operations
            on_progress: Progress callback (current, total, filename)
            on_complete: Completion callback (result)
            on_error: Error callback (error, filename)

        Returns:
            List of MediaResult objects
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Get list of files
        if isinstance(input_pattern, str):
            files = list(Path().glob(input_pattern))
        else:
            files = [Path(p) for p in input_pattern]

        results = []
        total_files = len(files)

        for i, input_file in enumerate(files, 1):
            try:
                output_file = output_dir / f"{input_file.stem}_watermarked{input_file.suffix}"

                if on_progress:
                    on_progress(i, total_files, input_file.name)

                result = self.watermark_video(input_file, watermark_config, output_file)
                results.append(result)

                if on_complete:
                    on_complete(result)

            except Exception as e:
                result = MediaResult(
                    success=False,
                    input_path=input_file,
                    error_message=str(e),
                    operation_type="batch_video_watermark"
                )
                results.append(result)

                if on_error:
                    on_error(e, input_file.name)

        return results

    # Utility Methods

    def get_processing_stats(self) -> Dict[str, Any]:
        """Get processing statistics and performance metrics."""
        stats = self.stats.copy()

        if stats["operations_completed"] > 0:
            stats["average_processing_time"] = stats["total_processing_time"] / stats["files_processed"] if stats["files_processed"] > 0 else 0
            stats["success_rate"] = stats["files_processed"] / stats["operations_completed"]
        else:
            stats["average_processing_time"] = 0
            stats["success_rate"] = 0

        return stats

    def reset_stats(self):
        """Reset processing statistics."""
        self.stats = {
            "operations_completed": 0,
            "total_processing_time": 0.0,
            "files_processed": 0,
            "errors": 0,
            "operations_by_type": {}
        }

    def validate_media_file(self, media_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Validate media file and return detailed analysis.

        Args:
            media_path: Path to media file

        Returns:
            Validation results dictionary
        """
        media_path = Path(media_path)

        result = {
            "valid": False,
            "file_exists": media_path.exists(),
            "file_size": 0,
            "format": None,
            "errors": []
        }

        try:
            if not media_path.exists():
                result["errors"].append("File does not exist")
                return result

            result["file_size"] = media_path.stat().st_size

            # Determine file type from extension
            suffix = media_path.suffix.lower()
            if suffix in ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v']:
                result["format"] = "video"
                result["valid"] = True
            elif suffix in ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff']:
                result["format"] = "image"
                result["valid"] = True
            else:
                result["errors"].append(f"Unsupported format: {suffix}")

        except Exception as e:
            result["errors"].append(str(e))

        return result

    def cleanup_temp_files(self):
        """Clean up temporary files created during processing."""
        try:
            if self.temp_dir.exists():
                for temp_file in self.temp_dir.glob("*"):
                    if temp_file.is_file():
                        temp_file.unlink()
                self.logger.info("Temporary files cleaned up")
        except Exception as e:
            self.logger.warning(f"Failed to cleanup temp files: {e}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        self.cleanup_temp_files()