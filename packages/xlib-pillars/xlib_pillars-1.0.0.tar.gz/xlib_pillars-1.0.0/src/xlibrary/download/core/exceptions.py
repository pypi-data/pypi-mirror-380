"""Exception hierarchy for download operations."""


class DownloadError(Exception):
    """Base exception for download operations."""
    pass


class DownloadTimeoutError(DownloadError):
    """Download operation timed out."""
    pass


class UnsupportedSourceError(DownloadError):
    """URL source is not supported by any available strategy."""
    pass


class NetworkError(DownloadError):
    """Network-related download error."""
    pass


class ConfigurationError(DownloadError):
    """Configuration or setup error."""
    pass


class StrategyError(DownloadError):
    """Error with download strategy execution."""
    pass


class QueueError(DownloadError):
    """Error with download queue management."""
    pass


class PermissionError(DownloadError):
    """File system permission error."""
    pass