"""Enhanced email query system based on SimpleGmail query functionality."""

from datetime import datetime, date
from typing import List, Optional, Union, Dict, Any
from enum import Enum
import re


class SortOrder(Enum):
    """Email sorting options."""
    NEWEST_FIRST = "newest_first"
    OLDEST_FIRST = "oldest_first"
    SENDER_ASC = "sender_asc"
    SENDER_DESC = "sender_desc"
    SUBJECT_ASC = "subject_asc"
    SUBJECT_DESC = "subject_desc"


class EmailQuery:
    """Enhanced email query builder with fluent interface.

    This class provides a modern, fluent interface for building complex
    email search queries, inspired by SimpleGmail but with enhanced
    capabilities and better error handling.

    Example:
        query = (EmailQuery()
            .from_sender("boss@company.com")
            .with_subject("urgent")
            .between_dates(start_date, end_date)
            .has_attachments()
            .limit(50))
    """

    def __init__(self):
        """Initialize empty query."""
        self._filters = {}
        self._sort_order = SortOrder.NEWEST_FIRST
        self._limit = None
        self._include_spam_trash = False

    def from_sender(self, sender: str) -> 'EmailQuery':
        """Filter by sender email address.

        Args:
            sender: Email address or partial match

        Returns:
            EmailQuery instance for chaining
        """
        if not sender:
            raise ValueError("Sender cannot be empty")
        self._filters['from'] = sender
        return self

    def to_recipient(self, recipient: str) -> 'EmailQuery':
        """Filter by recipient email address.

        Args:
            recipient: Email address or partial match

        Returns:
            EmailQuery instance for chaining
        """
        if not recipient:
            raise ValueError("Recipient cannot be empty")
        self._filters['to'] = recipient
        return self

    def with_subject(self, subject: str, exact: bool = False) -> 'EmailQuery':
        """Filter by email subject.

        Args:
            subject: Subject text to search for
            exact: Whether to match exact subject or partial

        Returns:
            EmailQuery instance for chaining
        """
        if not subject:
            raise ValueError("Subject cannot be empty")

        if exact:
            self._filters['subject'] = f'"{subject}"'
        else:
            self._filters['subject'] = subject
        return self

    def with_body_text(self, text: str) -> 'EmailQuery':
        """Filter by text in email body.

        Args:
            text: Text to search for in email body

        Returns:
            EmailQuery instance for chaining
        """
        if not text:
            raise ValueError("Body text cannot be empty")
        self._filters['body'] = text
        return self

    def has_attachments(self, file_types: Optional[List[str]] = None) -> 'EmailQuery':
        """Filter emails that have attachments.

        Args:
            file_types: Optional list of file extensions to filter by

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['has_attachment'] = True
        if file_types:
            # Convert to lowercase and ensure they start with dot
            normalized_types = []
            for ft in file_types:
                ft = ft.lower().strip()
                if not ft.startswith('.'):
                    ft = f'.{ft}'
                normalized_types.append(ft)
            self._filters['attachment_types'] = normalized_types
        return self

    def no_attachments(self) -> 'EmailQuery':
        """Filter emails that have no attachments.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['has_attachment'] = False
        return self

    def with_labels(self, labels: Union[str, List[str]]) -> 'EmailQuery':
        """Filter by Gmail labels.

        Args:
            labels: Single label or list of labels

        Returns:
            EmailQuery instance for chaining
        """
        if isinstance(labels, str):
            labels = [labels]

        if not labels:
            raise ValueError("Labels list cannot be empty")

        # Normalize label names (Gmail is case-insensitive)
        normalized_labels = [label.strip() for label in labels if label.strip()]
        if not normalized_labels:
            raise ValueError("No valid labels provided")

        self._filters['labels'] = normalized_labels
        return self

    def without_labels(self, labels: Union[str, List[str]]) -> 'EmailQuery':
        """Exclude emails with specific labels.

        Args:
            labels: Single label or list of labels to exclude

        Returns:
            EmailQuery instance for chaining
        """
        if isinstance(labels, str):
            labels = [labels]

        if not labels:
            raise ValueError("Labels list cannot be empty")

        normalized_labels = [label.strip() for label in labels if label.strip()]
        if not normalized_labels:
            raise ValueError("No valid labels provided")

        self._filters['exclude_labels'] = normalized_labels
        return self

    def is_unread(self) -> 'EmailQuery':
        """Filter unread emails only.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['is_unread'] = True
        return self

    def is_read(self) -> 'EmailQuery':
        """Filter read emails only.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['is_unread'] = False
        return self

    def is_important(self) -> 'EmailQuery':
        """Filter important emails only.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['is_important'] = True
        return self

    def is_starred(self) -> 'EmailQuery':
        """Filter starred emails only.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['is_starred'] = True
        return self

    def between_dates(self, start_date: Union[datetime, date], end_date: Union[datetime, date]) -> 'EmailQuery':
        """Filter emails between date range.

        Args:
            start_date: Start date (inclusive)
            end_date: End date (inclusive)

        Returns:
            EmailQuery instance for chaining
        """
        if start_date > end_date:
            raise ValueError("Start date must be before end date")

        self._filters['after'] = start_date
        self._filters['before'] = end_date
        return self

    def after_date(self, date_value: Union[datetime, date]) -> 'EmailQuery':
        """Filter emails after specific date.

        Args:
            date_value: Date after which to search

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['after'] = date_value
        return self

    def before_date(self, date_value: Union[datetime, date]) -> 'EmailQuery':
        """Filter emails before specific date.

        Args:
            date_value: Date before which to search

        Returns:
            EmailQuery instance for chaining
        """
        self._filters['before'] = date_value
        return self

    def larger_than(self, size_bytes: int) -> 'EmailQuery':
        """Filter emails larger than specified size.

        Args:
            size_bytes: Minimum size in bytes

        Returns:
            EmailQuery instance for chaining
        """
        if size_bytes <= 0:
            raise ValueError("Size must be positive")
        self._filters['larger_than'] = size_bytes
        return self

    def smaller_than(self, size_bytes: int) -> 'EmailQuery':
        """Filter emails smaller than specified size.

        Args:
            size_bytes: Maximum size in bytes

        Returns:
            EmailQuery instance for chaining
        """
        if size_bytes <= 0:
            raise ValueError("Size must be positive")
        self._filters['smaller_than'] = size_bytes
        return self

    def with_filename(self, filename: str) -> 'EmailQuery':
        """Filter by attachment filename.

        Args:
            filename: Filename to search for (supports wildcards)

        Returns:
            EmailQuery instance for chaining
        """
        if not filename:
            raise ValueError("Filename cannot be empty")
        self._filters['filename'] = filename
        return self

    def in_folder(self, folder: str) -> 'EmailQuery':
        """Filter by Gmail folder/label.

        Args:
            folder: Folder name (INBOX, SENT, DRAFT, etc.)

        Returns:
            EmailQuery instance for chaining
        """
        if not folder:
            raise ValueError("Folder cannot be empty")

        # Normalize common folder names
        folder_mapping = {
            'inbox': 'INBOX',
            'sent': 'SENT',
            'draft': 'DRAFT',
            'drafts': 'DRAFT',
            'spam': 'SPAM',
            'trash': 'TRASH',
            'all': 'ALL'
        }

        normalized_folder = folder_mapping.get(folder.lower(), folder.upper())
        self._filters['in'] = normalized_folder
        return self

    def custom_filter(self, gmail_query: str) -> 'EmailQuery':
        """Add custom Gmail search query string.

        Args:
            gmail_query: Raw Gmail search query

        Returns:
            EmailQuery instance for chaining
        """
        if not gmail_query:
            raise ValueError("Custom query cannot be empty")
        self._filters['custom'] = gmail_query
        return self

    def sort_by(self, order: SortOrder) -> 'EmailQuery':
        """Set sort order for results.

        Args:
            order: Sort order from SortOrder enum

        Returns:
            EmailQuery instance for chaining
        """
        self._sort_order = order
        return self

    def limit(self, count: int) -> 'EmailQuery':
        """Limit number of results.

        Args:
            count: Maximum number of messages to return

        Returns:
            EmailQuery instance for chaining
        """
        if count <= 0:
            raise ValueError("Limit must be positive")
        if count > 1000:
            raise ValueError("Limit cannot exceed 1000")
        self._limit = count
        return self

    def include_spam_trash(self, include: bool = True) -> 'EmailQuery':
        """Include spam and trash messages in results.

        Args:
            include: Whether to include spam/trash messages

        Returns:
            EmailQuery instance for chaining
        """
        self._include_spam_trash = include
        return self

    def build_gmail_query(self) -> str:
        """Build Gmail API query string from filters.

        Returns:
            Gmail search query string
        """
        query_parts = []

        # From/To filters
        if 'from' in self._filters:
            query_parts.append(f"from:{self._filters['from']}")

        if 'to' in self._filters:
            query_parts.append(f"to:{self._filters['to']}")

        # Subject filter
        if 'subject' in self._filters:
            subject = self._filters['subject']
            if subject.startswith('"') and subject.endswith('"'):
                query_parts.append(f"subject:{subject}")
            else:
                query_parts.append(f"subject:({subject})")

        # Body text filter
        if 'body' in self._filters:
            query_parts.append(f'"{self._filters["body"]}"')

        # Attachment filters
        if 'has_attachment' in self._filters:
            if self._filters['has_attachment']:
                query_parts.append("has:attachment")
            else:
                query_parts.append("-has:attachment")

        # Attachment types
        if 'attachment_types' in self._filters:
            for file_type in self._filters['attachment_types']:
                query_parts.append(f"filename:{file_type}")

        # Read/Unread status
        if 'is_unread' in self._filters:
            if self._filters['is_unread']:
                query_parts.append("is:unread")
            else:
                query_parts.append("is:read")

        # Important/Starred status
        if 'is_important' in self._filters:
            if self._filters['is_important']:
                query_parts.append("is:important")

        if 'is_starred' in self._filters:
            if self._filters['is_starred']:
                query_parts.append("is:starred")

        # Date filters
        if 'after' in self._filters:
            date_str = self._format_date(self._filters['after'])
            query_parts.append(f"after:{date_str}")

        if 'before' in self._filters:
            date_str = self._format_date(self._filters['before'])
            query_parts.append(f"before:{date_str}")

        # Size filters
        if 'larger_than' in self._filters:
            size = self._filters['larger_than']
            query_parts.append(f"larger:{size}")

        if 'smaller_than' in self._filters:
            size = self._filters['smaller_than']
            query_parts.append(f"smaller:{size}")

        # Filename filter
        if 'filename' in self._filters:
            filename = self._filters['filename']
            query_parts.append(f"filename:{filename}")

        # Labels
        if 'labels' in self._filters:
            for label in self._filters['labels']:
                query_parts.append(f"label:{label}")

        if 'exclude_labels' in self._filters:
            for label in self._filters['exclude_labels']:
                query_parts.append(f"-label:{label}")

        # Folder
        if 'in' in self._filters:
            query_parts.append(f"in:{self._filters['in']}")

        # Custom query
        if 'custom' in self._filters:
            query_parts.append(f"({self._filters['custom']})")

        # Build final query
        query = " ".join(query_parts)

        # Add spam/trash exclusion if needed
        if not self._include_spam_trash:
            query = f"({query}) -in:spam -in:trash"

        return query.strip()

    def get_filters(self) -> Dict[str, Any]:
        """Get copy of current filters.

        Returns:
            Dictionary of current filters
        """
        return self._filters.copy()

    def get_sort_order(self) -> SortOrder:
        """Get current sort order.

        Returns:
            Current sort order
        """
        return self._sort_order

    def get_limit(self) -> Optional[int]:
        """Get current result limit.

        Returns:
            Current limit or None if unlimited
        """
        return self._limit

    def clear(self) -> 'EmailQuery':
        """Clear all filters and reset to defaults.

        Returns:
            EmailQuery instance for chaining
        """
        self._filters.clear()
        self._sort_order = SortOrder.NEWEST_FIRST
        self._limit = None
        self._include_spam_trash = False
        return self

    def copy(self) -> 'EmailQuery':
        """Create a copy of this query.

        Returns:
            New EmailQuery instance with same filters
        """
        new_query = EmailQuery()
        new_query._filters = self._filters.copy()
        new_query._sort_order = self._sort_order
        new_query._limit = self._limit
        new_query._include_spam_trash = self._include_spam_trash
        return new_query

    def _format_date(self, date_value: Union[datetime, date]) -> str:
        """Format date for Gmail query.

        Args:
            date_value: Date to format

        Returns:
            Formatted date string
        """
        if isinstance(date_value, datetime):
            return date_value.strftime('%Y/%m/%d')
        else:
            return date_value.strftime('%Y/%m/%d')

    def __str__(self) -> str:
        """String representation of the query."""
        gmail_query = self.build_gmail_query()
        filters_count = len(self._filters)
        limit_str = f", limit={self._limit}" if self._limit else ""
        return f"EmailQuery({filters_count} filters{limit_str}): {gmail_query}"

    def __repr__(self) -> str:
        """Developer representation of the query."""
        return f"EmailQuery(filters={self._filters}, sort={self._sort_order}, limit={self._limit})"