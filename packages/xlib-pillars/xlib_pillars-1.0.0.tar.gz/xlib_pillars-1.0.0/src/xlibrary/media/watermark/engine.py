"""
Advanced PNG overlay watermark engine with smart resolution scaling.

This engine uses a single high-resolution master watermark approach
with intelligent scaling to handle videos from 320p to 4K+ without
quality loss. Supports transparency, animations, and precise positioning.
"""

import logging
from pathlib import Path
from typing import Optional, Tuple, Union, Dict, Any
from datetime import datetime

from ..core.types import (
    WatermarkConfig, WatermarkPosition, WatermarkAnimation,
    Resolution, Position, Size, WatermarkError, MediaResult
)

# Optional PIL import
try:
    from PIL import Image, ImageEnhance, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class WatermarkEngine:
    """
    Advanced PNG overlay watermarking with smart resolution scaling.

    This engine uses a single high-resolution master watermark approach
    with intelligent scaling to handle videos from 320p to 4K+ without
    quality loss. Supports transparency, animations, and precise positioning.
    """

    def __init__(self, config: WatermarkConfig, logger: Optional[logging.Logger] = None):
        """
        Initialize watermark engine.

        Args:
            config: Watermark configuration
            logger: Optional logger instance
        """
        if not PIL_AVAILABLE:
            raise WatermarkError(
                "PIL not available for watermarking. Install with: pip install xlibrary[media]"
            )

        self.config = config
        self.logger = logger or logging.getLogger(__name__)

        # Validate watermark file
        if not config.watermark_path.exists():
            raise WatermarkError(f"Watermark file not found: {config.watermark_path}")

        # Load master watermark
        self._master_watermark = None
        self._load_master_watermark()

        # Cached scaled versions for performance
        self._watermark_cache: Dict[str, Image.Image] = {}

        # Cache statistics
        self._cache_stats = {
            "hits": 0,
            "misses": 0,
            "entries": 0
        }

    def _load_master_watermark(self):
        """Load the master watermark PNG with transparency."""
        try:
            # Load with transparency support
            image = Image.open(self.config.watermark_path).convert("RGBA")

            # Validate it's a proper PNG with alpha channel
            if image.mode != "RGBA":
                self.logger.warning(f"Watermark {self.config.watermark_path} doesn't have alpha channel, converting...")
                image = image.convert("RGBA")

            self._master_watermark = image
            self.logger.debug(f"Loaded master watermark: {image.size[0]}x{image.size[1]}")

        except Exception as e:
            raise WatermarkError(f"Failed to load watermark: {e}")

    def calculate_optimal_size(self, target_resolution: Resolution) -> Size:
        """
        Calculate optimal watermark size for target resolution.

        Uses smart scaling algorithm that considers:
        - Target resolution
        - Master watermark dimensions
        - Configuration limits
        - Quality preservation thresholds

        Args:
            target_resolution: Target media resolution

        Returns:
            Optimal watermark size (width, height)
        """
        if isinstance(target_resolution, tuple):
            target_width, target_height = target_resolution
        else:
            target_width, target_height = target_resolution.width, target_resolution.height

        master_width, master_height = self._master_watermark.size

        # Calculate maximum allowed dimensions based on percentages
        max_width = int(target_width * self.config.max_width_percent)
        max_height = int(target_height * self.config.max_height_percent)

        if self.config.auto_scale:
            # Smart scaling based on target resolution
            if target_height >= self.config.quality_threshold:
                # High resolution target - can scale up for quality
                base_scale = target_height / 1080.0  # Reference: 1080p
            else:
                # Lower resolution target - be more conservative
                base_scale = target_height / 720.0   # Reference: 720p

            # Apply base scale with configuration factor
            scale = base_scale * self.config.scale_factor

            # Clamp to configured limits
            scale = max(self.config.min_scale, min(self.config.max_scale, scale))

            # Calculate scaled dimensions
            scaled_width = int(master_width * scale)
            scaled_height = int(master_height * scale)
        else:
            # Manual scaling using scale factor only
            scaled_width = int(master_width * self.config.scale_factor)
            scaled_height = int(master_height * self.config.scale_factor)

        # Ensure we don't exceed maximum dimensions
        if scaled_width > max_width or scaled_height > max_height:
            # Scale down to fit within limits while maintaining aspect ratio
            width_ratio = max_width / scaled_width
            height_ratio = max_height / scaled_height
            final_ratio = min(width_ratio, height_ratio)

            scaled_width = int(scaled_width * final_ratio)
            scaled_height = int(scaled_height * final_ratio)

        # Ensure minimum size (at least 16x16 pixels)
        scaled_width = max(16, scaled_width)
        scaled_height = max(16, scaled_height)

        self.logger.debug(
            f"Calculated watermark size for {target_width}x{target_height}: "
            f"{scaled_width}x{scaled_height} (scale: {scaled_width/master_width:.3f})"
        )

        return Size(scaled_width, scaled_height)

    def calculate_position(self, watermark_size: Size, target_resolution: Resolution) -> Position:
        """
        Calculate watermark position based on configuration.

        Args:
            watermark_size: Size of the watermark
            target_resolution: Target media resolution

        Returns:
            Position coordinates (x, y) for top-left corner of watermark
        """
        if isinstance(watermark_size, tuple):
            wm_width, wm_height = watermark_size
        else:
            wm_width, wm_height = watermark_size.width, watermark_size.height

        if isinstance(target_resolution, tuple):
            target_width, target_height = target_resolution
        else:
            target_width, target_height = target_resolution.width, target_resolution.height

        # Base positions for each location
        position_map = {
            WatermarkPosition.TOP_LEFT: (self.config.offset_x, self.config.offset_y),
            WatermarkPosition.TOP_CENTER: (
                (target_width - wm_width) // 2,
                self.config.offset_y
            ),
            WatermarkPosition.TOP_RIGHT: (
                target_width - wm_width - self.config.offset_x,
                self.config.offset_y
            ),
            WatermarkPosition.CENTER_LEFT: (
                self.config.offset_x,
                (target_height - wm_height) // 2
            ),
            WatermarkPosition.CENTER: (
                (target_width - wm_width) // 2,
                (target_height - wm_height) // 2
            ),
            WatermarkPosition.CENTER_RIGHT: (
                target_width - wm_width - self.config.offset_x,
                (target_height - wm_height) // 2
            ),
            WatermarkPosition.BOTTOM_LEFT: (
                self.config.offset_x,
                target_height - wm_height - self.config.offset_y
            ),
            WatermarkPosition.BOTTOM_CENTER: (
                (target_width - wm_width) // 2,
                target_height - wm_height - self.config.offset_y
            ),
            WatermarkPosition.BOTTOM_RIGHT: (
                target_width - wm_width - self.config.offset_x,
                target_height - wm_height - self.config.offset_y
            )
        }

        x, y = position_map.get(self.config.position, position_map[WatermarkPosition.BOTTOM_RIGHT])

        # Ensure position is within bounds
        x = max(0, min(x, target_width - wm_width))
        y = max(0, min(y, target_height - wm_height))

        return Position(x, y)

    def get_scaled_watermark(self, target_resolution: Resolution, use_cache: bool = True) -> Image.Image:
        """
        Get scaled watermark for target resolution with caching.

        Args:
            target_resolution: Target media resolution
            use_cache: Whether to use cached versions

        Returns:
            Scaled watermark image
        """
        if isinstance(target_resolution, tuple):
            cache_key = f"{target_resolution[0]}x{target_resolution[1]}"
            resolution_obj = Resolution(target_resolution[0], target_resolution[1])
        else:
            cache_key = f"{target_resolution.width}x{target_resolution.height}"
            resolution_obj = target_resolution

        # Check cache first
        if use_cache and cache_key in self._watermark_cache:
            self._cache_stats["hits"] += 1
            return self._watermark_cache[cache_key]

        self._cache_stats["misses"] += 1

        # Calculate optimal size
        optimal_size = self.calculate_optimal_size(resolution_obj)

        # Scale the master watermark
        scaled_watermark = self._master_watermark.resize(
            (optimal_size.width, optimal_size.height),
            Image.LANCZOS  # High-quality resampling
        )

        # Apply opacity if needed
        if self.config.opacity < 1.0:
            # Create alpha mask for opacity
            alpha = scaled_watermark.split()[-1]  # Get alpha channel
            alpha = ImageEnhance.Brightness(alpha).enhance(self.config.opacity)
            scaled_watermark.putalpha(alpha)

        # Cache the scaled version
        if use_cache:
            self._watermark_cache[cache_key] = scaled_watermark
            self._cache_stats["entries"] = len(self._watermark_cache)

        self.logger.debug(f"Generated scaled watermark: {optimal_size.width}x{optimal_size.height}")

        return scaled_watermark

    def apply_to_image(self, image: Image.Image, target_resolution: Optional[Resolution] = None) -> Tuple[Image.Image, MediaResult]:
        """
        Apply watermark to a PIL Image.

        Args:
            image: Input PIL Image
            target_resolution: Optional override for resolution (uses image size if None)

        Returns:
            Tuple of (watermarked image, processing result)
        """
        start_time = datetime.now()

        try:
            if target_resolution is None:
                target_resolution = Resolution(image.width, image.height)
            elif isinstance(target_resolution, tuple):
                target_resolution = Resolution(target_resolution[0], target_resolution[1])

            # Get scaled watermark
            watermark = self.get_scaled_watermark(target_resolution)

            # Calculate position
            position = self.calculate_position(
                Size(watermark.width, watermark.height),
                target_resolution
            )

            # Create composite image
            if image.mode != "RGBA":
                image = image.convert("RGBA")

            # Paste watermark onto image
            composite = image.copy()
            composite.paste(watermark, (position.x, position.y), watermark)

            processing_time = (datetime.now() - start_time).total_seconds()

            result = MediaResult(
                success=True,
                operation_type="image_watermark",
                processing_time=processing_time,
                metadata={
                    "watermark_size": f"{watermark.width}x{watermark.height}",
                    "position": f"{position.x},{position.y}",
                    "opacity": self.config.opacity,
                    "cache_hit": self._cache_stats["hits"] > 0
                }
            )

            return composite, result

        except Exception as e:
            processing_time = (datetime.now() - start_time).total_seconds()
            result = MediaResult(
                success=False,
                operation_type="image_watermark",
                processing_time=processing_time,
                error_message=str(e)
            )
            return image, result

    def apply_to_image_file(self, input_path: Path, output_path: Path) -> MediaResult:
        """
        Apply watermark to image file.

        Args:
            input_path: Path to input image file
            output_path: Path to output image file

        Returns:
            Processing result
        """
        start_time = datetime.now()

        try:
            with Image.open(input_path) as image:
                file_size_before = input_path.stat().st_size

                # Apply watermark
                watermarked_image, watermark_result = self.apply_to_image(image)

                # Determine output format
                output_format = output_path.suffix.upper().lstrip('.')
                if output_format == 'JPG':
                    output_format = 'JPEG'

                # Convert to RGB if saving as JPEG
                if output_format == 'JPEG' and watermarked_image.mode == 'RGBA':
                    background = Image.new('RGB', watermarked_image.size, (255, 255, 255))
                    background.paste(watermarked_image, mask=watermarked_image.split()[-1])
                    watermarked_image = background

                # Save watermarked image
                save_kwargs = {'format': output_format}
                if output_format == 'JPEG':
                    save_kwargs['quality'] = 95
                elif output_format == 'PNG':
                    save_kwargs['optimize'] = True

                watermarked_image.save(output_path, **save_kwargs)

                processing_time = (datetime.now() - start_time).total_seconds()
                file_size_after = output_path.stat().st_size

                result = MediaResult(
                    success=True,
                    input_path=input_path,
                    output_path=output_path,
                    operation_type="file_watermark",
                    processing_time=processing_time,
                    file_size_before=file_size_before,
                    file_size_after=file_size_after,
                    metadata=watermark_result.metadata
                )

                return result

        except Exception as e:
            processing_time = (datetime.now() - start_time).total_seconds()
            return MediaResult(
                success=False,
                input_path=input_path,
                output_path=output_path,
                operation_type="file_watermark",
                processing_time=processing_time,
                error_message=str(e)
            )

    def clear_cache(self):
        """Clear the watermark cache."""
        self._watermark_cache.clear()
        self._cache_stats = {
            "hits": 0,
            "misses": 0,
            "entries": 0
        }
        self.logger.debug("Watermark cache cleared")

    def get_cache_info(self) -> Dict[str, Any]:
        """
        Get cache performance information.

        Returns:
            Dictionary with cache statistics
        """
        total_requests = self._cache_stats["hits"] + self._cache_stats["misses"]
        hit_rate = (self._cache_stats["hits"] / total_requests) if total_requests > 0 else 0.0

        return {
            "hits": self._cache_stats["hits"],
            "misses": self._cache_stats["misses"],
            "entries": self._cache_stats["entries"],
            "total_requests": total_requests,
            "hit_rate": hit_rate,
            "cache_size_mb": len(self._watermark_cache) * 0.1  # Rough estimate
        }