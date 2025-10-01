"""Communication Pillar - Unified communication across email, SMS, and sockets.

This pillar provides a unified interface for multiple communication channels:
- Email (Gmail, SMTP/IMAP, Exchange)
- SMS (Twilio, AWS SNS)
- Socket Communication (TCP, UDP, WebSocket)

IMPORTANT: This pillar is independent and does not depend on other pillars.
Applications can integrate it with CLI, encryption, or other pillars as needed.

Example:
    from xlibrary.communication import CommManager, EmailQuery

    comm = CommManager()
    gmail = comm.gmail(credentials_path="credentials.json")

    # Send email
    message = gmail.compose()
    message.to("user@example.com")
    message.subject("Hello from xlibrary")
    message.body("This is a test message")
    result = message.send()

    # Advanced search
    messages = gmail.search(
        EmailQuery()
        .from_sender("boss@company.com")
        .is_unread()
        .limit(10)
    )
"""

from .core.manager import CommManager
from .core.message import CommunicationMessage, Contact, Attachment
from .core.exceptions import (
    CommunicationError,
    AuthenticationError,
    MessageError,
    AttachmentError,
    ProviderError
)

# Email components
from .email.core.query import EmailQuery, SortOrder
from .email.providers.gmail import GmailProvider, GmailMessage
from .email.core.attachments import AttachmentManager, AttachmentInfo

__version__ = "1.0.0"

__all__ = [
    # Core classes
    "CommManager",
    "CommunicationMessage",
    "Contact",
    "Attachment",

    # Email components
    "EmailQuery",
    "SortOrder",
    "GmailProvider",
    "GmailMessage",
    "AttachmentManager",
    "AttachmentInfo",

    # Exceptions
    "CommunicationError",
    "AuthenticationError",
    "MessageError",
    "AttachmentError",
    "ProviderError"
]


def get_version() -> str:
    """Get the communication pillar version."""
    return __version__