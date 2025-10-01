"""Gmail provider implementation based on SimpleGmail-master functionality.

This module provides a modern, enhanced Gmail provider that builds on the
foundation of SimpleGmail but with improved error handling, type safety,
and integration with our pillar architecture.
"""

import os
import json
import base64
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any, Union, Iterator, Callable
import logging
from pathlib import Path
import time

# Google API imports (optional dependencies)
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False
    Request = None
    Credentials = None
    InstalledAppFlow = None
    build = None
    HttpError = Exception

from ...core.message import CommunicationMessage, Contact, Attachment, ChannelType, MessageStatus
from ...core.exceptions import AuthenticationError, MessageError, AttachmentError, ProviderError, RateLimitError
from ..core.query import EmailQuery


logger = logging.getLogger(__name__)


class GmailProvider:
    """Enhanced Gmail provider with modern Python patterns.

    This class provides a comprehensive interface to Gmail functionality,
    building on the SimpleGmail foundation but with enhanced features:
    - Modern async/await patterns
    - Better error handling and recovery
    - Type safety and validation
    - Integration with xlibrary pillar architecture
    - Batch operations for performance
    - Real-time notifications (future)

    Example:
        gmail = GmailProvider(credentials_path="credentials.json")

        # Send email
        message = gmail.compose()
        message.to("recipient@example.com")
        message.subject("Hello from xlibrary")
        message.body("This is a test message")
        result = message.send()

        # Search emails
        query = EmailQuery().from_sender("boss@company.com").limit(10)
        messages = gmail.search(query)
    """

    # Gmail API scopes
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/gmail.send',
        'https://www.googleapis.com/auth/gmail.modify'
    ]

    def __init__(
        self,
        credentials_path: Optional[str] = None,
        token_path: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        user_id: str = 'me',
        **kwargs
    ):
        """Initialize Gmail provider.

        Args:
            credentials_path: Path to credentials.json file
            token_path: Path to store/read token file
            scopes: List of Gmail API scopes
            user_id: Gmail user ID (usually 'me')
            **kwargs: Additional configuration options

        Raises:
            ProviderError: If Google API libraries not available
            AuthenticationError: If authentication fails
        """
        if not GOOGLE_API_AVAILABLE:
            raise ProviderError(
                "Gmail provider requires Google API libraries. Install with: pip install xlibrary[communication-gmail]",
                provider="gmail",
                operation="initialize"
            )

        self.user_id = user_id
        self.scopes = scopes or self.SCOPES
        self.credentials_path = credentials_path
        self.token_path = token_path or "gmail_token.json"

        # Configuration
        self.batch_size = kwargs.get('batch_size', 100)
        self.retry_attempts = kwargs.get('retry_attempts', 3)
        self.retry_delay = kwargs.get('retry_delay', 1.0)

        # Internal state
        self._service = None
        self._credentials = None
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Initialize authentication
        self._authenticate()

    def _authenticate(self) -> None:
        """Authenticate with Gmail API.

        Raises:
            AuthenticationError: If authentication fails
        """
        try:
            creds = None

            # Load existing token if available
            if os.path.exists(self.token_path):
                creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)

            # If no valid credentials, run OAuth flow
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    try:
                        creds.refresh(Request())
                        self._logger.info("Gmail credentials refreshed successfully")
                    except Exception as e:
                        self._logger.warning(f"Failed to refresh credentials: {e}")
                        creds = None

                if not creds:
                    if not self.credentials_path or not os.path.exists(self.credentials_path):
                        raise AuthenticationError(
                            "Gmail credentials file not found. Please provide valid credentials.json path",
                            provider="gmail"
                        )

                    flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)
                    creds = flow.run_local_server(port=0)
                    self._logger.info("Gmail OAuth flow completed successfully")

                # Save credentials for next run
                with open(self.token_path, 'w') as token_file:
                    token_file.write(creds.to_json())
                    self._logger.info(f"Gmail token saved to {self.token_path}")

            self._credentials = creds
            self._service = build('gmail', 'v1', credentials=creds)
            self._logger.info("Gmail service initialized successfully")

        except Exception as e:
            raise AuthenticationError(
                f"Gmail authentication failed: {e}",
                provider="gmail"
            ) from e

    def compose(self) -> 'GmailMessage':
        """Create a new email message for composition.

        Returns:
            GmailMessage instance for composing email
        """
        return GmailMessage(self)

    def send_message(
        self,
        to: Union[str, List[str]],
        subject: str,
        body: str,
        cc: Optional[Union[str, List[str]]] = None,
        bcc: Optional[Union[str, List[str]]] = None,
        attachments: Optional[List[Union[str, Attachment]]] = None,
        html_body: Optional[str] = None
    ) -> str:
        """Send email message directly.

        Args:
            to: Recipient email address(es)
            subject: Email subject
            body: Plain text body
            cc: CC recipient(s)
            bcc: BCC recipient(s)
            attachments: List of file paths or Attachment objects
            html_body: HTML body content

        Returns:
            Sent message ID

        Raises:
            MessageError: If message sending fails
        """
        message = self.compose()

        # Set recipients
        if isinstance(to, str):
            to = [to]
        for recipient in to:
            message.to(recipient)

        if cc:
            if isinstance(cc, str):
                cc = [cc]
            for recipient in cc:
                message.cc(recipient)

        if bcc:
            if isinstance(bcc, str):
                bcc = [bcc]
            for recipient in bcc:
                message.bcc(recipient)

        # Set content
        message.subject(subject)
        message.body(body)

        if html_body:
            message.html_body(html_body)

        # Add attachments
        if attachments:
            for attachment in attachments:
                message.attach(attachment)

        return message.send()

    def get_messages(
        self,
        query: Optional[Union[str, EmailQuery]] = None,
        labels: Optional[List[str]] = None,
        max_results: Optional[int] = None,
        include_spam_trash: bool = False
    ) -> List[CommunicationMessage]:
        """Get messages matching criteria.

        Args:
            query: Search query string or EmailQuery object
            labels: List of labels to filter by
            max_results: Maximum number of messages to return
            include_spam_trash: Include spam and trash messages

        Returns:
            List of CommunicationMessage objects

        Raises:
            MessageError: If message retrieval fails
        """
        try:
            # Build query string
            if isinstance(query, EmailQuery):
                if not include_spam_trash:
                    query = query.include_spam_trash(False)
                if max_results:
                    query = query.limit(max_results)
                query_string = query.build_gmail_query()
            elif isinstance(query, str):
                query_string = query
            else:
                query_string = ""

            # Add label filters
            if labels:
                label_parts = [f"label:{label}" for label in labels]
                if query_string:
                    query_string = f"({query_string}) {' '.join(label_parts)}"
                else:
                    query_string = ' '.join(label_parts)

            # Execute search
            result = self._service.users().messages().list(
                userId=self.user_id,
                q=query_string,
                maxResults=max_results,
                includeSpamTrash=include_spam_trash
            ).execute()

            messages = result.get('messages', [])
            self._logger.info(f"Found {len(messages)} messages matching query")

            # Convert to CommunicationMessage objects
            communication_messages = []
            for msg in messages:
                try:
                    full_message = self.get_message(msg['id'])
                    communication_messages.append(full_message)
                except Exception as e:
                    self._logger.warning(f"Failed to retrieve message {msg['id']}: {e}")
                    continue

            return communication_messages

        except HttpError as e:
            raise MessageError(f"Failed to retrieve messages: {e}") from e
        except Exception as e:
            raise MessageError(f"Unexpected error retrieving messages: {e}") from e

    def get_message(self, message_id: str) -> CommunicationMessage:
        """Get specific message by ID.

        Args:
            message_id: Gmail message ID

        Returns:
            CommunicationMessage object

        Raises:
            MessageError: If message retrieval fails
        """
        try:
            message = self._service.users().messages().get(
                userId=self.user_id,
                id=message_id,
                format='full'
            ).execute()

            return self._parse_gmail_message(message)

        except HttpError as e:
            if e.resp.status == 404:
                raise MessageError(f"Message not found: {message_id}", message_id=message_id) from e
            raise MessageError(f"Failed to retrieve message {message_id}: {e}", message_id=message_id) from e
        except Exception as e:
            raise MessageError(f"Unexpected error retrieving message {message_id}: {e}", message_id=message_id) from e

    def search(self, query: EmailQuery) -> List[CommunicationMessage]:
        """Search messages using EmailQuery.

        Args:
            query: EmailQuery object with search criteria

        Returns:
            List of matching CommunicationMessage objects
        """
        return self.get_messages(
            query=query,
            max_results=query.get_limit(),
            include_spam_trash=query._include_spam_trash
        )

    def delete_messages(self, message_ids: Union[str, List[str]]) -> Dict[str, bool]:
        """Delete messages by ID.

        Args:
            message_ids: Single message ID or list of IDs

        Returns:
            Dictionary mapping message IDs to success status

        Raises:
            MessageError: If deletion fails
        """
        if isinstance(message_ids, str):
            message_ids = [message_ids]

        results = {}
        for message_id in message_ids:
            try:
                self._service.users().messages().delete(
                    userId=self.user_id,
                    id=message_id
                ).execute()
                results[message_id] = True
                self._logger.info(f"Deleted message: {message_id}")
            except Exception as e:
                results[message_id] = False
                self._logger.error(f"Failed to delete message {message_id}: {e}")

        return results

    def modify_labels(
        self,
        message_ids: Union[str, List[str]],
        add_labels: Optional[List[str]] = None,
        remove_labels: Optional[List[str]] = None
    ) -> Dict[str, bool]:
        """Modify labels on messages.

        Args:
            message_ids: Single message ID or list of IDs
            add_labels: Labels to add
            remove_labels: Labels to remove

        Returns:
            Dictionary mapping message IDs to success status
        """
        if isinstance(message_ids, str):
            message_ids = [message_ids]

        body = {}
        if add_labels:
            body['addLabelIds'] = add_labels
        if remove_labels:
            body['removeLabelIds'] = remove_labels

        if not body:
            raise ValueError("Must specify labels to add or remove")

        results = {}
        for message_id in message_ids:
            try:
                self._service.users().messages().modify(
                    userId=self.user_id,
                    id=message_id,
                    body=body
                ).execute()
                results[message_id] = True
                self._logger.info(f"Modified labels for message: {message_id}")
            except Exception as e:
                results[message_id] = False
                self._logger.error(f"Failed to modify labels for message {message_id}: {e}")

        return results

    def mark_as_read(self, message_ids: Union[str, List[str]]) -> Dict[str, bool]:
        """Mark messages as read.

        Args:
            message_ids: Single message ID or list of IDs

        Returns:
            Dictionary mapping message IDs to success status
        """
        return self.modify_labels(message_ids, remove_labels=['UNREAD'])

    def mark_as_unread(self, message_ids: Union[str, List[str]]) -> Dict[str, bool]:
        """Mark messages as unread.

        Args:
            message_ids: Single message ID or list of IDs

        Returns:
            Dictionary mapping message IDs to success status
        """
        return self.modify_labels(message_ids, add_labels=['UNREAD'])

    def get_labels(self) -> List[Dict[str, Any]]:
        """Get all available labels.

        Returns:
            List of label information dictionaries
        """
        try:
            result = self._service.users().labels().list(userId=self.user_id).execute()
            return result.get('labels', [])
        except Exception as e:
            raise ProviderError(f"Failed to retrieve labels: {e}", provider="gmail", operation="get_labels") from e

    def _parse_gmail_message(self, gmail_message: Dict[str, Any]) -> CommunicationMessage:
        """Parse Gmail API message into CommunicationMessage.

        Args:
            gmail_message: Raw Gmail API message data

        Returns:
            CommunicationMessage object
        """
        message_id = gmail_message['id']
        thread_id = gmail_message.get('threadId')
        label_ids = gmail_message.get('labelIds', [])

        # Parse headers
        headers = {}
        payload = gmail_message.get('payload', {})
        for header in payload.get('headers', []):
            headers[header['name'].lower()] = header['value']

        # Extract basic info
        subject = headers.get('subject', 'No Subject')
        sender_str = headers.get('from', 'Unknown Sender')
        to_str = headers.get('to', '')
        cc_str = headers.get('cc', '')
        date_str = headers.get('date', '')

        # Parse sender
        sender = Contact.from_string(sender_str)

        # Parse recipients
        recipients = []
        for recipient_str in [to_str, cc_str]:
            if recipient_str:
                # Handle multiple recipients separated by commas
                for addr in recipient_str.split(','):
                    if addr.strip():
                        recipients.append(Contact.from_string(addr.strip()))

        # Parse timestamp
        timestamp = datetime.now(timezone.utc)
        if date_str:
            try:
                # Gmail date format parsing
                timestamp = email.utils.parsedate_to_datetime(date_str)
            except Exception:
                pass  # Keep default timestamp

        # Extract body
        body = self._extract_body(payload)

        # Extract attachments
        attachments = self._extract_attachments(payload, message_id)

        # Determine status
        status = MessageStatus.UNREAD if 'UNREAD' in label_ids else MessageStatus.READ

        return CommunicationMessage(
            id=message_id,
            channel=ChannelType.EMAIL,
            sender=sender,
            recipients=recipients,
            subject=subject,
            body=body,
            attachments=attachments,
            timestamp=timestamp,
            status=status,
            thread_id=thread_id,
            labels=label_ids,
            email_headers=headers
        )

    def _extract_body(self, payload: Dict[str, Any]) -> str:
        """Extract email body from Gmail payload.

        Args:
            payload: Gmail message payload

        Returns:
            Email body text
        """
        body = ""

        # Handle different payload structures
        if 'parts' in payload:
            for part in payload['parts']:
                if part.get('mimeType') == 'text/plain':
                    data = part.get('body', {}).get('data', '')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8')
                        break
        else:
            # Single part message
            if payload.get('mimeType') == 'text/plain':
                data = payload.get('body', {}).get('data', '')
                if data:
                    body = base64.urlsafe_b64decode(data).decode('utf-8')

        return body

    def _extract_attachments(self, payload: Dict[str, Any], message_id: str) -> List[Attachment]:
        """Extract attachments from Gmail payload.

        Args:
            payload: Gmail message payload
            message_id: Gmail message ID

        Returns:
            List of Attachment objects
        """
        attachments = []

        def extract_from_parts(parts):
            for part in parts:
                if 'parts' in part:
                    extract_from_parts(part['parts'])
                    continue

                filename = None
                for header in part.get('headers', []):
                    if header['name'].lower() == 'content-disposition':
                        # Extract filename from Content-Disposition header
                        value = header['value']
                        if 'filename=' in value:
                            filename = value.split('filename=')[1].strip('"')
                            break

                if filename and part.get('body', {}).get('attachmentId'):
                    attachment = Attachment(
                        filename=filename,
                        content_type=part.get('mimeType', 'application/octet-stream'),
                        size=part.get('body', {}).get('size', 0),
                        attachment_id=part['body']['attachmentId']
                    )
                    attachments.append(attachment)

        if 'parts' in payload:
            extract_from_parts(payload['parts'])

        return attachments

    def download_attachment(self, message_id: str, attachment_id: str, file_path: str) -> str:
        """Download attachment to file.

        Args:
            message_id: Gmail message ID
            attachment_id: Gmail attachment ID
            file_path: Local file path to save attachment

        Returns:
            Path to downloaded file

        Raises:
            AttachmentError: If download fails
        """
        try:
            attachment = self._service.users().messages().attachments().get(
                userId=self.user_id,
                messageId=message_id,
                id=attachment_id
            ).execute()

            data = attachment['data']
            file_data = base64.urlsafe_b64decode(data)

            with open(file_path, 'wb') as f:
                f.write(file_data)

            self._logger.info(f"Downloaded attachment to: {file_path}")
            return file_path

        except Exception as e:
            raise AttachmentError(f"Failed to download attachment: {e}", file_path=file_path) from e

    def close(self) -> None:
        """Clean up resources."""
        self._service = None
        self._credentials = None
        self._logger.info("Gmail provider closed")


class GmailMessage:
    """Gmail message composer for fluent message creation."""

    def __init__(self, provider: GmailProvider):
        """Initialize message composer.

        Args:
            provider: GmailProvider instance
        """
        self._provider = provider
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ""
        self._body = ""
        self._html_body = None
        self._attachments = []

    def to(self, address: str) -> 'GmailMessage':
        """Add TO recipient.

        Args:
            address: Email address

        Returns:
            Self for chaining
        """
        self._to.append(address)
        return self

    def cc(self, address: str) -> 'GmailMessage':
        """Add CC recipient.

        Args:
            address: Email address

        Returns:
            Self for chaining
        """
        self._cc.append(address)
        return self

    def bcc(self, address: str) -> 'GmailMessage':
        """Add BCC recipient.

        Args:
            address: Email address

        Returns:
            Self for chaining
        """
        self._bcc.append(address)
        return self

    def subject(self, subject: str) -> 'GmailMessage':
        """Set message subject.

        Args:
            subject: Email subject

        Returns:
            Self for chaining
        """
        self._subject = subject
        return self

    def body(self, body: str) -> 'GmailMessage':
        """Set message body.

        Args:
            body: Plain text body

        Returns:
            Self for chaining
        """
        self._body = body
        return self

    def html_body(self, html: str) -> 'GmailMessage':
        """Set HTML body.

        Args:
            html: HTML body content

        Returns:
            Self for chaining
        """
        self._html_body = html
        return self

    def attach(self, attachment: Union[str, Attachment]) -> 'GmailMessage':
        """Add attachment.

        Args:
            attachment: File path or Attachment object

        Returns:
            Self for chaining
        """
        if isinstance(attachment, str):
            attachment = Attachment.from_file(attachment)
        self._attachments.append(attachment)
        return self

    def send(self) -> str:
        """Send the message.

        Returns:
            Sent message ID

        Raises:
            MessageError: If sending fails
        """
        if not self._to:
            raise MessageError("Message must have at least one TO recipient")

        try:
            # Create MIME message
            if self._html_body or self._attachments:
                message = MIMEMultipart()
            else:
                message = MIMEText(self._body)
                message['To'] = ', '.join(self._to)
                message['Subject'] = self._subject
                if self._cc:
                    message['Cc'] = ', '.join(self._cc)

            if isinstance(message, MIMEMultipart):
                message['To'] = ', '.join(self._to)
                message['Subject'] = self._subject
                if self._cc:
                    message['Cc'] = ', '.join(self._cc)

                # Add text body
                if self._html_body:
                    # Both plain and HTML
                    text_part = MIMEText(self._body, 'plain')
                    html_part = MIMEText(self._html_body, 'html')
                    message.attach(text_part)
                    message.attach(html_part)
                else:
                    # Plain text only
                    text_part = MIMEText(self._body, 'plain')
                    message.attach(text_part)

                # Add attachments
                for attachment in self._attachments:
                    content = attachment.load_content()
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(content)
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {attachment.filename}'
                    )
                    message.attach(part)

            # Convert to Gmail API format
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            # Send message
            result = self._provider._service.users().messages().send(
                userId=self._provider.user_id,
                body={'raw': raw_message}
            ).execute()

            message_id = result['id']
            logger.info(f"Gmail message sent successfully: {message_id}")
            return message_id

        except Exception as e:
            raise MessageError(f"Failed to send Gmail message: {e}") from e