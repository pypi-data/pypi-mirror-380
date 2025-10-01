"""Universal message format for all communication channels."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Dict, Any, Optional, Union
import json
from pathlib import Path


class ChannelType(Enum):
    """Communication channel types."""
    EMAIL = "email"
    SMS = "sms"
    SOCKET = "socket"


class MessageStatus(Enum):
    """Message status values."""
    DRAFT = "draft"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"
    READ = "read"
    UNREAD = "unread"


@dataclass
class Contact:
    """Contact information for senders and recipients."""
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    display_name: Optional[str] = None

    def __post_init__(self):
        """Generate display name if not provided."""
        if not self.display_name:
            if self.name:
                self.display_name = f"{self.name} <{self.email or self.phone or 'unknown'}>"
            else:
                self.display_name = self.email or self.phone or "Unknown Contact"

    @property
    def address(self) -> str:
        """Get primary contact address (email or phone)."""
        return self.email or self.phone or ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "email": self.email,
            "name": self.name,
            "phone": self.phone,
            "display_name": self.display_name
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Contact':
        """Create from dictionary."""
        return cls(**data)

    @classmethod
    def from_string(cls, contact_str: str) -> 'Contact':
        """Parse contact from string format 'Name <email>' or just 'email'."""
        contact_str = contact_str.strip()

        if '<' in contact_str and '>' in contact_str:
            # Format: "John Doe <john@example.com>"
            name = contact_str[:contact_str.find('<')].strip()
            email = contact_str[contact_str.find('<') + 1:contact_str.find('>')].strip()
            return cls(email=email, name=name)
        elif '@' in contact_str:
            # Format: "john@example.com"
            return cls(email=contact_str)
        elif contact_str.startswith('+') or contact_str.isdigit():
            # Format: "+1234567890" or "1234567890"
            return cls(phone=contact_str)
        else:
            # Assume it's a name
            return cls(name=contact_str)


@dataclass
class Attachment:
    """File attachment for messages."""
    filename: str
    content_type: str
    size: int
    file_path: Optional[str] = None
    content: Optional[bytes] = None
    attachment_id: Optional[str] = None

    def __post_init__(self):
        """Validate attachment data."""
        if not self.file_path and not self.content:
            raise ValueError("Either file_path or content must be provided")

        if self.file_path and not self.content:
            # Load file size if not provided
            if self.size == 0:
                path = Path(self.file_path)
                if path.exists():
                    self.size = path.stat().st_size

    def load_content(self) -> bytes:
        """Load attachment content from file if not already loaded."""
        if self.content:
            return self.content

        if self.file_path:
            with open(self.file_path, 'rb') as f:
                self.content = f.read()
            return self.content

        raise ValueError("No content or file path available")

    def save_to_file(self, file_path: str) -> str:
        """Save attachment content to file."""
        content = self.load_content()
        with open(file_path, 'wb') as f:
            f.write(content)
        return file_path

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary (excluding content for serialization)."""
        return {
            "filename": self.filename,
            "content_type": self.content_type,
            "size": self.size,
            "file_path": self.file_path,
            "attachment_id": self.attachment_id
        }

    @classmethod
    def from_file(cls, file_path: str, filename: Optional[str] = None) -> 'Attachment':
        """Create attachment from file path."""
        import mimetypes

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Attachment file not found: {file_path}")

        content_type, _ = mimetypes.guess_type(file_path)
        content_type = content_type or "application/octet-stream"

        return cls(
            filename=filename or path.name,
            content_type=content_type,
            size=path.stat().st_size,
            file_path=str(path.absolute())
        )


@dataclass
class CommunicationMessage:
    """Universal message format across all communication channels."""
    id: str
    channel: ChannelType
    sender: Contact
    recipients: List[Contact] = field(default_factory=list)
    subject: Optional[str] = None
    body: str = ""
    attachments: List[Attachment] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    status: MessageStatus = MessageStatus.DRAFT

    # Channel-specific metadata
    email_headers: Optional[Dict[str, str]] = None
    thread_id: Optional[str] = None
    labels: List[str] = field(default_factory=list)

    def add_recipient(self, recipient: Union[str, Contact]) -> None:
        """Add a recipient to the message."""
        if isinstance(recipient, str):
            recipient = Contact.from_string(recipient)
        self.recipients.append(recipient)

    def add_attachment(self, attachment: Union[str, Attachment]) -> None:
        """Add an attachment to the message."""
        if isinstance(attachment, str):
            attachment = Attachment.from_file(attachment)
        self.attachments.append(attachment)

    def get_recipient_addresses(self) -> List[str]:
        """Get list of recipient addresses."""
        return [contact.address for contact in self.recipients if contact.address]

    def has_attachments(self) -> bool:
        """Check if message has attachments."""
        return len(self.attachments) > 0

    def get_total_attachment_size(self) -> int:
        """Get total size of all attachments in bytes."""
        return sum(att.size for att in self.attachments)

    def is_sent(self) -> bool:
        """Check if message has been sent."""
        return self.status in (MessageStatus.SENT, MessageStatus.DELIVERED, MessageStatus.READ)

    def mark_as_read(self) -> None:
        """Mark message as read."""
        if self.status == MessageStatus.UNREAD:
            self.status = MessageStatus.READ

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary for serialization."""
        return {
            "id": self.id,
            "channel": self.channel.value,
            "sender": self.sender.to_dict(),
            "recipients": [r.to_dict() for r in self.recipients],
            "subject": self.subject,
            "body": self.body,
            "attachments": [a.to_dict() for a in self.attachments],
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status.value,
            "email_headers": self.email_headers,
            "thread_id": self.thread_id,
            "labels": self.labels
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CommunicationMessage':
        """Create message from dictionary."""
        # Parse timestamp
        timestamp = datetime.fromisoformat(data["timestamp"])

        # Parse contacts
        sender = Contact.from_dict(data["sender"])
        recipients = [Contact.from_dict(r) for r in data["recipients"]]

        # Parse attachments (without content for security)
        attachments = []
        for att_data in data.get("attachments", []):
            att = Attachment(
                filename=att_data["filename"],
                content_type=att_data["content_type"],
                size=att_data["size"],
                file_path=att_data.get("file_path"),
                attachment_id=att_data.get("attachment_id")
            )
            attachments.append(att)

        return cls(
            id=data["id"],
            channel=ChannelType(data["channel"]),
            sender=sender,
            recipients=recipients,
            subject=data.get("subject"),
            body=data.get("body", ""),
            attachments=attachments,
            metadata=data.get("metadata", {}),
            timestamp=timestamp,
            status=MessageStatus(data.get("status", "draft")),
            email_headers=data.get("email_headers"),
            thread_id=data.get("thread_id"),
            labels=data.get("labels", [])
        )

    def to_json(self) -> str:
        """Convert message to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'CommunicationMessage':
        """Create message from JSON string."""
        return cls.from_dict(json.loads(json_str))

    def __str__(self) -> str:
        """String representation of the message."""
        recipient_str = ", ".join(self.get_recipient_addresses())
        return f"Message({self.id}): {self.sender.display_name} → {recipient_str} | {self.subject or 'No Subject'}"