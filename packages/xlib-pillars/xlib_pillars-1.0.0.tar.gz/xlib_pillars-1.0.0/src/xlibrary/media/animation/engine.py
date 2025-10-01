"""
Advanced animation engine for video watermarks using MoviePy.

Provides sophisticated animation capabilities including fades, scrolls, pulses,
and credits rolling effects with precise timing control.
"""

import logging
import numpy as np
from pathlib import Path
from typing import Optional, Tuple, Union, TYPE_CHECKING
from datetime import datetime

from ..core.types import (
    WatermarkConfig, WatermarkAnimation, Resolution, Position, Size,
    MediaResult, ProcessingError
)
from ..watermark import WatermarkEngine

# Optional MoviePy import
try:
    from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False
    # Stub for type checking
    if TYPE_CHECKING:
        from moviepy.editor import ImageClip


class AnimationEngine:
    """
    Advanced watermark animation engine using MoviePy.

    Handles complex animations like fades, scrolls, pulses, and credits
    with precise timing and positioning control.
    """

    def __init__(self, config: WatermarkConfig, logger: Optional[logging.Logger] = None):
        """
        Initialize animation engine.

        Args:
            config: Watermark configuration with animation settings
            logger: Optional logger instance
        """
        if not MOVIEPY_AVAILABLE:
            raise ProcessingError(
                "MoviePy not available for animations. Install with: pip install xlibrary[media]"
            )

        self.config = config
        self.logger = logger or logging.getLogger(__name__)

        # Validate animation settings
        self._validate_config()

    def _validate_config(self):
        """Validate animation configuration parameters."""
        if self.config.animation_duration < 0:
            raise ProcessingError("Animation duration cannot be negative")

        if self.config.animation_start_time < 0:
            raise ProcessingError("Animation start time cannot be negative")

        if (self.config.animation_end_time is not None and
            self.config.animation_end_time <= self.config.animation_start_time):
            raise ProcessingError("Animation end time must be after start time")

        # Validate animation-specific parameters
        if self.config.fade_duration <= 0:
            raise ProcessingError("Fade duration must be positive")

        if self.config.scroll_speed <= 0:
            raise ProcessingError("Scroll speed must be positive")

        if self.config.pulse_frequency <= 0:
            raise ProcessingError("Pulse frequency must be positive")

    def apply_animated_watermark(
        self,
        input_path: Path,
        output_path: Path,
        target_resolution: Resolution,
        video_duration: float,
        start_time: datetime
    ) -> MediaResult:
        """
        Apply animated watermark to video using MoviePy.

        Args:
            input_path: Path to input video
            output_path: Path to output video
            target_resolution: Target video resolution
            video_duration: Video duration in seconds
            start_time: Processing start time for timing

        Returns:
            Processing result
        """
        try:
            self.logger.info(f"Applying {self.config.animation.value} animation watermark")

            # Load video
            video = VideoFileClip(str(input_path))

            # Create watermark engine for smart scaling
            watermark_engine = WatermarkEngine(self.config, self.logger)

            # Get scaled watermark image
            watermark_pil = watermark_engine.get_scaled_watermark(target_resolution)

            # Convert PIL to numpy array for MoviePy
            watermark_array = np.array(watermark_pil)

            # Calculate animation timing
            anim_start = self.config.animation_start_time
            anim_end = self.config.animation_end_time or video_duration
            anim_duration = self.config.animation_duration or (anim_end - anim_start)

            # Ensure animation fits within video duration
            anim_end = min(anim_end, video_duration)
            anim_duration = min(anim_duration, anim_end - anim_start)

            # Create base ImageClip
            watermark_clip = ImageClip(
                watermark_array,
                transparent=True,
                duration=anim_duration
            ).set_start(anim_start)

            # Calculate base position
            base_position = watermark_engine.calculate_position(
                Size(watermark_pil.size[0], watermark_pil.size[1]),
                target_resolution
            )

            # Apply specific animation
            animated_clip = self._create_animation(
                watermark_clip,
                base_position,
                target_resolution,
                watermark_pil.size,
                video_duration
            )

            # Composite video with animated watermark
            final_video = CompositeVideoClip([video, animated_clip])

            # Write output with quality settings
            codec_params = self._get_codec_params()

            final_video.write_videofile(
                str(output_path),
                **codec_params
            )

            # Clean up MoviePy clips
            video.close()
            animated_clip.close()
            final_video.close()

            # Calculate results
            processing_time = (datetime.now() - start_time).total_seconds()

            # Get watermark cache performance
            cache_info = watermark_engine.get_cache_info()

            return MediaResult(
                success=True,
                input_path=input_path,
                output_path=output_path,
                operation_type="animated_watermark",
                processing_time=processing_time,
                file_size_before=input_path.stat().st_size,
                file_size_after=output_path.stat().st_size,
                metadata={
                    "animation_type": self.config.animation.value,
                    "animation_duration": anim_duration,
                    "animation_start": anim_start,
                    "animation_end": anim_end,
                    "watermark_size": f"{watermark_pil.size[0]}x{watermark_pil.size[1]}",
                    "base_position": f"{base_position.x},{base_position.y}",
                    "cache_hit_rate": f"{cache_info['hit_rate']:.1%}" if cache_info["total_requests"] > 0 else "0%"
                }
            )

        except Exception as e:
            return MediaResult(
                success=False,
                input_path=input_path,
                output_path=output_path,
                operation_type="animated_watermark",
                processing_time=(datetime.now() - start_time).total_seconds(),
                error_message=str(e)
            )

    def _create_animation(
        self,
        watermark_clip,  # ImageClip type when MoviePy available
        base_position: Position,
        target_resolution: Resolution,
        watermark_size: Tuple[int, int],
        video_duration: float
    ):
        """Create specific animation based on configuration."""

        animation = self.config.animation

        if animation == WatermarkAnimation.STATIC or animation == WatermarkAnimation.NONE:
            # Static watermark
            return watermark_clip.set_position((base_position.x, base_position.y))

        elif animation == WatermarkAnimation.FADE_IN:
            # Fade in animation
            fade_duration = min(self.config.fade_duration, watermark_clip.duration / 2)
            return watermark_clip.set_position((base_position.x, base_position.y)).crossfadein(fade_duration)

        elif animation == WatermarkAnimation.FADE_OUT:
            # Fade out animation
            fade_duration = min(self.config.fade_duration, watermark_clip.duration / 2)
            return watermark_clip.set_position((base_position.x, base_position.y)).crossfadeout(fade_duration)

        elif animation == WatermarkAnimation.FADE_IN_OUT:
            # Fade in and out
            fade_duration = min(self.config.fade_duration, watermark_clip.duration / 4)
            return (watermark_clip
                    .set_position((base_position.x, base_position.y))
                    .crossfadein(fade_duration)
                    .crossfadeout(fade_duration))

        elif animation in [
            WatermarkAnimation.SCROLL_LEFT,
            WatermarkAnimation.SCROLL_RIGHT,
            WatermarkAnimation.SCROLL_UP,
            WatermarkAnimation.SCROLL_DOWN
        ]:
            # Scrolling animations
            return self._create_scroll_animation(
                watermark_clip, base_position, target_resolution, watermark_size, animation
            )

        elif animation == WatermarkAnimation.CREDITS_ROLL:
            # Credits roll from bottom to top
            return self._create_credits_roll(
                watermark_clip, base_position, target_resolution, watermark_size
            )

        elif animation == WatermarkAnimation.PULSE:
            # Pulsing opacity
            return self._create_pulse_animation(
                watermark_clip, base_position
            )

        else:
            # Fallback to static
            self.logger.warning(f"Unknown animation type: {animation}, using static")
            return watermark_clip.set_position((base_position.x, base_position.y))

    def _create_scroll_animation(
        self,
        clip,  # ImageClip type when MoviePy available
        base_position: Position,
        target_resolution: Resolution,
        watermark_size: Tuple[int, int],
        animation: WatermarkAnimation
    ):
        """Create scrolling animation."""

        def scroll_position(t):
            progress = (t * self.config.scroll_speed) % (
                target_resolution.width + watermark_size[0]
            )

            if animation == WatermarkAnimation.SCROLL_LEFT:
                return (target_resolution.width - progress, base_position.y)
            elif animation == WatermarkAnimation.SCROLL_RIGHT:
                return (progress - watermark_size[0], base_position.y)
            elif animation == WatermarkAnimation.SCROLL_UP:
                progress = (t * self.config.scroll_speed) % (
                    target_resolution.height + watermark_size[1]
                )
                return (base_position.x, target_resolution.height - progress)
            else:  # SCROLL_DOWN
                progress = (t * self.config.scroll_speed) % (
                    target_resolution.height + watermark_size[1]
                )
                return (base_position.x, progress - watermark_size[1])

        return clip.set_position(scroll_position)

    def _create_credits_roll(
        self,
        clip,  # ImageClip type when MoviePy available
        base_position: Position,
        target_resolution: Resolution,
        watermark_size: Tuple[int, int]
    ):
        """Create credits roll animation (bottom to top)."""

        def credits_position(t):
            progress = t * self.config.scroll_speed
            y = target_resolution.height - progress
            return (base_position.x, y)

        return clip.set_position(credits_position)

    def _create_pulse_animation(
        self,
        clip,  # ImageClip type when MoviePy available
        base_position: Position
    ):
        """Create pulsing opacity animation."""

        def pulse_opacity(t):
            cycle = np.sin(2 * np.pi * self.config.pulse_frequency * t)
            return self.config.opacity * (0.5 + 0.5 * cycle)

        return (clip
                .set_position((base_position.x, base_position.y))
                .set_opacity(pulse_opacity))

    def _get_codec_params(self) -> dict:
        """Get codec parameters for video output."""
        return {
            'audio_codec': 'aac',
            'codec': 'libx264',
            'preset': 'medium',
            'temp_audiofile': 'temp-audio.m4a',
            'remove_temp': True,
            'verbose': False,
            'logger': None  # Suppress MoviePy logs
        }

    @staticmethod
    def is_animation_available() -> bool:
        """Check if animation features are available."""
        return MOVIEPY_AVAILABLE

    @staticmethod
    def get_supported_animations() -> list:
        """Get list of supported animation types."""
        return [
            WatermarkAnimation.STATIC,
            WatermarkAnimation.FADE_IN,
            WatermarkAnimation.FADE_OUT,
            WatermarkAnimation.FADE_IN_OUT,
            WatermarkAnimation.SCROLL_LEFT,
            WatermarkAnimation.SCROLL_RIGHT,
            WatermarkAnimation.SCROLL_UP,
            WatermarkAnimation.SCROLL_DOWN,
            WatermarkAnimation.CREDITS_ROLL,
            WatermarkAnimation.PULSE
        ]