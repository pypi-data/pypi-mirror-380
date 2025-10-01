"""Email communication components."""

from .providers.gmail import GmailProvider, GmailMessage
from .core.query import EmailQuery
from .core.attachments import AttachmentManager, AttachmentInfo

__all__ = [
    "GmailProvider",
    "GmailMessage",
    "EmailQuery",
    "AttachmentManager",
    "AttachmentInfo"
]