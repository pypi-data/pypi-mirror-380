"""Email core components."""

from .query import EmailQuery
from .attachments import AttachmentManager, AttachmentInfo

__all__ = ["EmailQuery", "AttachmentManager", "AttachmentInfo"]