"""Central communication manager for all communication channels."""

from typing import Optional, Dict, Any, Type, Union
import logging
from pathlib import Path

from .exceptions import CommunicationError, ProviderError
from .message import ChannelType


logger = logging.getLogger(__name__)


class CommManager:
    """Central communication manager supporting multiple channels.

    The CommManager provides a unified interface for accessing different
    communication channels including email, SMS, and socket communications.

    Example:
        comm = CommManager()
        gmail = comm.gmail(credentials_path="credentials.json")
        sms = comm.sms(provider="twilio", account_sid="...", auth_token="...")
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize communication manager.

        Args:
            config: Optional configuration dictionary for default settings
        """
        self.config = config or {}
        self._providers = {}
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def gmail(self, credentials_path: Optional[str] = None, **kwargs) -> 'GmailProvider':
        """Create Gmail provider instance.

        Args:
            credentials_path: Path to Gmail API credentials JSON file
            **kwargs: Additional provider configuration

        Returns:
            Configured Gmail provider instance

        Raises:
            ProviderError: If Gmail provider cannot be initialized
        """
        try:
            from ..email.providers.gmail import GmailProvider

            # Merge configuration
            gmail_config = self.config.get("gmail", {})
            gmail_config.update(kwargs)

            if credentials_path:
                gmail_config["credentials_path"] = credentials_path

            provider = GmailProvider(**gmail_config)
            provider_id = f"gmail_{id(provider)}"
            self._providers[provider_id] = provider

            self._logger.info(f"Created Gmail provider: {provider_id}")
            return provider

        except ImportError as e:
            raise ProviderError(
                "Gmail provider dependencies not available. Install with: pip install xlibrary[communication-gmail]",
                provider="gmail",
                operation="initialize"
            ) from e
        except Exception as e:
            raise ProviderError(
                f"Failed to initialize Gmail provider: {e}",
                provider="gmail",
                operation="initialize"
            ) from e

    def email(self, smtp_config: Dict[str, Any], **kwargs) -> 'SMTPProvider':
        """Create generic SMTP/IMAP email provider.

        Args:
            smtp_config: SMTP server configuration
            **kwargs: Additional provider configuration

        Returns:
            Configured SMTP provider instance

        Raises:
            ProviderError: If SMTP provider cannot be initialized
        """
        try:
            from ..email.providers.smtp import SMTPProvider

            # Merge configuration
            email_config = self.config.get("email", {})
            email_config.update(kwargs)
            email_config["smtp_config"] = smtp_config

            provider = SMTPProvider(**email_config)
            provider_id = f"smtp_{id(provider)}"
            self._providers[provider_id] = provider

            self._logger.info(f"Created SMTP provider: {provider_id}")
            return provider

        except ImportError as e:
            raise ProviderError(
                "SMTP provider dependencies not available. Install with: pip install xlibrary[communication-email]",
                provider="smtp",
                operation="initialize"
            ) from e
        except Exception as e:
            raise ProviderError(
                f"Failed to initialize SMTP provider: {e}",
                provider="smtp",
                operation="initialize"
            ) from e

    def sms(self, provider: str, **kwargs) -> 'BaseSMSProvider':
        """Create SMS provider instance.

        Args:
            provider: SMS provider name ("twilio", "aws_sns")
            **kwargs: Provider-specific configuration

        Returns:
            Configured SMS provider instance

        Raises:
            ProviderError: If SMS provider cannot be initialized
        """
        try:
            if provider.lower() == "twilio":
                from ..sms.providers.twilio import TwilioProvider
                provider_class = TwilioProvider
            elif provider.lower() == "aws_sns":
                from ..sms.providers.aws_sns import AWSSNSProvider
                provider_class = AWSSNSProvider
            else:
                raise ValueError(f"Unknown SMS provider: {provider}")

            # Merge configuration
            sms_config = self.config.get("sms", {}).get(provider.lower(), {})
            sms_config.update(kwargs)

            provider_instance = provider_class(**sms_config)
            provider_id = f"sms_{provider.lower()}_{id(provider_instance)}"
            self._providers[provider_id] = provider_instance

            self._logger.info(f"Created SMS provider: {provider_id}")
            return provider_instance

        except ImportError as e:
            raise ProviderError(
                f"SMS provider '{provider}' dependencies not available. Install with: pip install xlibrary[communication-sms]",
                provider=provider,
                operation="initialize"
            ) from e
        except Exception as e:
            raise ProviderError(
                f"Failed to initialize SMS provider '{provider}': {e}",
                provider=provider,
                operation="initialize"
            ) from e

    def socket(self, socket_type: str = "tcp", **kwargs) -> 'BaseSocketProvider':
        """Create socket communication provider.

        Args:
            socket_type: Type of socket ("tcp", "udp", "websocket")
            **kwargs: Socket-specific configuration

        Returns:
            Configured socket provider instance

        Raises:
            ProviderError: If socket provider cannot be initialized
        """
        try:
            if socket_type.lower() == "tcp":
                from ..sockets.tcp.client import TCPClient
                provider_class = TCPClient
            elif socket_type.lower() == "websocket":
                from ..sockets.websocket.client import WebSocketClient
                provider_class = WebSocketClient
            else:
                raise ValueError(f"Unknown socket type: {socket_type}")

            # Merge configuration
            socket_config = self.config.get("sockets", {}).get(socket_type.lower(), {})
            socket_config.update(kwargs)

            provider_instance = provider_class(**socket_config)
            provider_id = f"socket_{socket_type.lower()}_{id(provider_instance)}"
            self._providers[provider_id] = provider_instance

            self._logger.info(f"Created socket provider: {provider_id}")
            return provider_instance

        except ImportError as e:
            raise ProviderError(
                f"Socket provider '{socket_type}' dependencies not available. Install with: pip install xlibrary[communication-sockets]",
                provider=socket_type,
                operation="initialize"
            ) from e
        except Exception as e:
            raise ProviderError(
                f"Failed to initialize socket provider '{socket_type}': {e}",
                provider=socket_type,
                operation="initialize"
            ) from e

    def get_provider(self, provider_id: str):
        """Get provider instance by ID.

        Args:
            provider_id: Provider identifier

        Returns:
            Provider instance

        Raises:
            ProviderError: If provider not found
        """
        if provider_id not in self._providers:
            raise ProviderError(
                f"Provider '{provider_id}' not found",
                provider=provider_id,
                operation="get_provider"
            )
        return self._providers[provider_id]

    def list_providers(self) -> Dict[str, str]:
        """List all active providers.

        Returns:
            Dictionary mapping provider IDs to their types
        """
        return {
            pid: type(provider).__name__
            for pid, provider in self._providers.items()
        }

    def close_all_providers(self) -> None:
        """Close all active providers and clean up resources."""
        for provider_id, provider in self._providers.items():
            try:
                if hasattr(provider, 'close'):
                    provider.close()
                self._logger.info(f"Closed provider: {provider_id}")
            except Exception as e:
                self._logger.warning(f"Error closing provider {provider_id}: {e}")

        self._providers.clear()
        self._logger.info("All providers closed")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        self.close_all_providers()

    @classmethod
    def from_config_file(cls, config_path: Union[str, Path]) -> 'CommManager':
        """Create CommManager from configuration file.

        Args:
            config_path: Path to configuration file (JSON or TOML)

        Returns:
            Configured CommManager instance

        Raises:
            CommunicationError: If configuration cannot be loaded
        """
        import json
        from pathlib import Path

        config_path = Path(config_path)
        if not config_path.exists():
            raise CommunicationError(f"Configuration file not found: {config_path}")

        try:
            if config_path.suffix.lower() == '.json':
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            elif config_path.suffix.lower() in ['.toml', '.tml']:
                try:
                    import tomli
                    with open(config_path, 'rb') as f:
                        config = tomli.load(f)
                except ImportError:
                    raise CommunicationError(
                        "TOML support not available. Install with: pip install tomli"
                    )
            else:
                raise CommunicationError(f"Unsupported config file format: {config_path.suffix}")

            return cls(config)

        except Exception as e:
            raise CommunicationError(f"Failed to load configuration from {config_path}: {e}") from e