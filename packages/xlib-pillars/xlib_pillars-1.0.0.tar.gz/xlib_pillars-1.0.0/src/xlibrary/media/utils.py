"""
Utilities for media processing operations.
"""

import re
from typing import Union, Optional
from .core.types import TimeStamp, TimestampError


class TimeStampParser:
    """
    Flexible timestamp parser supporting multiple formats.

    Supported formats:
    - "2:30.5" - Minutes:seconds.fraction
    - "f5400" - Frame number (f prefix)
    - "150.75" - Seconds (decimal)
    - "2:30:45.250" - Hours:minutes:seconds.milliseconds
    """

    def __init__(self, default_fps: float = 30.0):
        """
        Initialize parser with default FPS.

        Args:
            default_fps: Default frames per second for frame calculations
        """
        self.default_fps = default_fps

    def parse(self, timestamp: Union[str, int, float], fps: Optional[float] = None) -> TimeStamp:
        """
        Parse timestamp from various formats.

        Args:
            timestamp: Timestamp in supported format
            fps: Frames per second (uses default if None)

        Returns:
            TimeStamp object

        Raises:
            TimestampError: If timestamp format is invalid
        """
        if fps is None:
            fps = self.default_fps

        if isinstance(timestamp, (int, float)):
            return TimeStamp.from_seconds(float(timestamp), fps)

        if not isinstance(timestamp, str):
            raise TimestampError(f"Invalid timestamp type: {type(timestamp)}")

        timestamp = timestamp.strip()

        try:
            # Frame number format (f5400)
            if timestamp.startswith('f'):
                frame_num = int(timestamp[1:])
                return TimeStamp.from_frame(frame_num, fps)

            # Time format with colons (2:30.5 or 2:30:45.250)
            elif ':' in timestamp:
                return self._parse_time_format(timestamp, fps)

            # Direct seconds (150.75)
            else:
                seconds = float(timestamp)
                return TimeStamp.from_seconds(seconds, fps)

        except (ValueError, IndexError) as e:
            raise TimestampError(f"Invalid timestamp format '{timestamp}': {e}")

    def _parse_time_format(self, time_str: str, fps: float) -> TimeStamp:
        """Parse time format like MM:SS.fraction or HH:MM:SS.fraction."""
        parts = time_str.split(':')

        if len(parts) == 2:
            # MM:SS.fraction
            minutes_str, seconds_str = parts
            minutes = int(minutes_str)
            seconds = float(seconds_str)
            total_seconds = minutes * 60 + seconds

        elif len(parts) == 3:
            # HH:MM:SS.fraction
            hours_str, minutes_str, seconds_str = parts
            hours = int(hours_str)
            minutes = int(minutes_str)
            seconds = float(seconds_str)
            total_seconds = hours * 3600 + minutes * 60 + seconds

        else:
            raise ValueError(f"Invalid time format: {time_str}")

        return TimeStamp.from_seconds(total_seconds, fps)


def parse_timestamp(timestamp: Union[str, int, float], fps: float = 30.0) -> TimeStamp:
    """
    Convenience function to parse timestamp.

    Args:
        timestamp: Timestamp in supported format
        fps: Frames per second

    Returns:
        TimeStamp object
    """
    parser = TimeStampParser(fps)
    return parser.parse(timestamp, fps)


def timestamp_to_frame(timestamp: Union[str, int, float], fps: float = 30.0) -> int:
    """
    Convert timestamp to frame number.

    Args:
        timestamp: Timestamp in supported format
        fps: Frames per second

    Returns:
        Frame number
    """
    ts = parse_timestamp(timestamp, fps)
    return ts.frame


def frame_to_timestamp(frame: int, fps: float = 30.0) -> str:
    """
    Convert frame number to timestamp string.

    Args:
        frame: Frame number
        fps: Frames per second

    Returns:
        Timestamp string in MM:SS.fraction format
    """
    seconds = frame / fps
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:06.3f}"


def detect_timestamp_format(timestamp: str) -> str:
    """
    Detect the format of a timestamp string.

    Args:
        timestamp: Timestamp string

    Returns:
        Format description
    """
    timestamp = timestamp.strip()

    if timestamp.startswith('f'):
        return "frame_number"
    elif ':' in timestamp:
        parts = timestamp.split(':')
        if len(parts) == 2:
            return "minutes_seconds"
        elif len(parts) == 3:
            return "hours_minutes_seconds"
        else:
            return "unknown_time_format"
    else:
        try:
            float(timestamp)
            return "decimal_seconds"
        except ValueError:
            return "unknown_format"


def validate_timestamp(timestamp: str, fps: float = 30.0) -> bool:
    """
    Validate if timestamp string is in supported format.

    Args:
        timestamp: Timestamp string to validate
        fps: Frames per second for validation

    Returns:
        True if valid, False otherwise
    """
    try:
        parse_timestamp(timestamp, fps)
        return True
    except TimestampError:
        return False


def seconds_to_hms(seconds: float) -> str:
    """
    Convert seconds to HH:MM:SS.mmm format.

    Args:
        seconds: Time in seconds

    Returns:
        Formatted time string
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{remaining_seconds:06.3f}"
    else:
        return f"{minutes:02d}:{remaining_seconds:06.3f}"


def normalize_timestamp(timestamp: Union[str, int, float], fps: float = 30.0) -> str:
    """
    Normalize timestamp to standard MM:SS.mmm format.

    Args:
        timestamp: Timestamp in any supported format
        fps: Frames per second

    Returns:
        Normalized timestamp string
    """
    ts = parse_timestamp(timestamp, fps)
    return seconds_to_hms(ts.seconds)