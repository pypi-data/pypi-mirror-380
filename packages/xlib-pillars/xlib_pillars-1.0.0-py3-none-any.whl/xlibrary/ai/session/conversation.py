"""Conversation class for stateful AI interactions."""

import uuid
import logging
from typing import List, Optional, Dict, Any
from datetime import datetime
from pathlib import Path

from ..core.base import BaseAIProvider
from ..core.config import AIConfig
from ..core.models import Message, AIResponse, Artifact


logger = logging.getLogger(__name__)


class ChainableRequest:
    """
    Chainable request builder for fluent conversation API.

    Allows patterns like:
    conversation.request("prompt").with_temperature(0.8).send()
    conversation.request("prompt").attach_file("doc.txt").send()
    """

    def __init__(self, conversation: 'Conversation', prompt: str):
        """Initialize chainable request."""
        self.conversation = conversation
        self.prompt = prompt
        self.parameters: Dict[str, Any] = {}
        self.attachments: List[str] = []

    def with_temperature(self, temperature: float) -> 'ChainableRequest':
        """Set temperature for this request."""
        self.parameters['temperature'] = temperature
        return self

    def with_max_tokens(self, max_tokens: int) -> 'ChainableRequest':
        """Set max tokens for this request."""
        self.parameters['max_tokens'] = max_tokens
        return self

    def with_reasoning(self, enable: bool = True) -> 'ChainableRequest':
        """Enable reasoning mode for this request."""
        self.parameters['enable_reasoning'] = enable
        return self

    def attach_file(self, file_path: str, description: Optional[str] = None) -> 'ChainableRequest':
        """Attach a file to this request."""
        # Add file to conversation context first
        self.conversation.add_file(file_path, description)
        self.attachments.append(file_path)
        return self

    def attach_files(self, file_paths: List[str]) -> 'ChainableRequest':
        """Attach multiple files to this request."""
        for file_path in file_paths:
            self.attach_file(file_path)
        return self

    def with_param(self, key: str, value: Any) -> 'ChainableRequest':
        """Add custom parameter to this request."""
        self.parameters[key] = value
        return self

    def send(self) -> AIResponse:
        """Execute the request with all configured parameters."""
        # Extract enable_reasoning from parameters since it's a direct argument
        enable_reasoning = self.parameters.get('enable_reasoning', False)

        # Create a copy of parameters without enable_reasoning
        params = {k: v for k, v in self.parameters.items() if k != 'enable_reasoning'}

        return self.conversation._execute_request(
            prompt=self.prompt,
            enable_reasoning=enable_reasoning,
            **params
        )


class Conversation:
    """
    Manages a stateful conversation with an AI provider.

    Maintains message history and provides context for multi-turn interactions.
    """

    def __init__(
        self,
        provider: BaseAIProvider,
        config: AIConfig,
        conversation_id: Optional[str] = None,
        system_message: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize a new conversation.

        Args:
            provider: AI provider instance to use
            config: Configuration for the conversation
            conversation_id: Optional unique ID (generated if not provided)
            system_message: Optional system message to set context
            **kwargs: Additional conversation parameters
        """
        self.provider = provider
        self.config = config
        self.conversation_id = conversation_id or str(uuid.uuid4())
        self.created_at = datetime.now()
        self.last_activity = self.created_at

        # Message history
        self.messages: List[Message] = []

        # Add system message if provided
        if system_message:
            self.messages.append(Message(
                role="system",
                content=system_message,
                metadata={"conversation_id": self.conversation_id}
            ))

        # Conversation metadata
        self.metadata = kwargs
        self.total_tokens_used = 0
        self.total_cost = 0.0

        # Artifact collection
        self.artifacts: List[Artifact] = []

        logger.info(f"Conversation created: {self.conversation_id}")

    def request(
        self,
        prompt: str,
        enable_reasoning: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> ChainableRequest:
        """
        Create a chainable request for this conversation.

        Args:
            prompt: The user message
            enable_reasoning: Enable thinking trace if supported
            temperature: Override default temperature
            max_tokens: Override default max tokens
            **kwargs: Additional provider-specific parameters

        Returns:
            ChainableRequest object that can be chained or sent immediately

        Examples:
            # Simple usage (backward compatible)
            response = conversation.request("Hello").send()

            # Chained usage
            response = conversation.request("Hello")\\
                .with_temperature(0.8)\\
                .attach_file("doc.txt")\\
                .send()
        """
        # Create chainable request with initial parameters
        chainable = ChainableRequest(self, prompt)

        # Set initial parameters if provided
        if enable_reasoning:
            chainable.with_reasoning(enable_reasoning)
        if temperature is not None:
            chainable.with_temperature(temperature)
        if max_tokens is not None:
            chainable.with_max_tokens(max_tokens)
        for key, value in kwargs.items():
            chainable.with_param(key, value)

        return chainable

    def _execute_request(
        self,
        prompt: str,
        enable_reasoning: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> AIResponse:
        """
        Internal method to execute a request with the AI provider.

        This contains the actual request logic that was moved from the original request() method.
        """
        # Add user message to history
        user_message = Message(
            role="user",
            content=prompt,
            metadata={"conversation_id": self.conversation_id}
        )
        self.messages.append(user_message)

        # Prepare request parameters
        request_params = {}
        if temperature is not None:
            request_params['temperature'] = temperature
        elif self.config.temperature is not None:
            request_params['temperature'] = self.config.temperature

        if max_tokens is not None:
            request_params['max_tokens'] = max_tokens
        elif self.config.max_tokens is not None:
            request_params['max_tokens'] = self.config.max_tokens

        request_params.update(kwargs)

        # Manage conversation history length
        messages_to_send = self._get_context_messages()

        # Make request
        start_time = datetime.now()
        response = self.provider.complete(
            messages=messages_to_send,
            enable_reasoning=enable_reasoning,
            **request_params
        )
        end_time = datetime.now()

        # Add timing information
        response.latency_ms = (end_time - start_time).total_seconds() * 1000
        response.conversation_context = self.conversation_id

        # Add assistant message to history
        assistant_message = Message(
            role="assistant",
            content=response.content,
            metadata={
                "conversation_id": self.conversation_id,
                "tokens_used": response.tokens_used,
                "cost": response.cost_estimate,
                "thinking_trace": response.thinking_trace
            }
        )
        self.messages.append(assistant_message)

        # Update conversation statistics
        self.total_tokens_used += response.tokens_used
        self.total_cost += response.cost_estimate
        self.last_activity = datetime.now()

        # Extract artifacts if enabled
        if self.config.auto_extract_artifacts:
            new_artifacts = response.extract_artifacts()
            # Add to conversation's artifact collection
            for artifact in new_artifacts:
                artifact.parent_conversation_id = self.conversation_id
            self.artifacts.extend(new_artifacts)

        logger.info(f"Conversation {self.conversation_id}: "
                   f"{len(response.content)} chars, {response.tokens_used} tokens")

        return response

    def add_file(
        self,
        file_path: str,
        description: Optional[str] = None,
        file_type: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add a file to the conversation context.

        Args:
            file_path: Path to the file
            description: Optional description of the file
            file_type: Optional file type hint
            **kwargs: Additional file metadata

        Returns:
            Dict with file attachment information
        """
        file_path_obj = Path(file_path)

        if not file_path_obj.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read file content
        try:
            with open(file_path_obj, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Handle binary files
            with open(file_path_obj, 'rb') as f:
                content = f"[Binary file: {file_path_obj.name}]"

        # Create file message
        file_description = description or f"File: {file_path_obj.name}"
        file_content = f"{file_description}\n\n```{file_type or ''}\n{content}\n```"

        file_message = Message(
            role="user",
            content=file_content,
            metadata={
                "conversation_id": self.conversation_id,
                "file_path": str(file_path_obj),
                "file_type": file_type or file_path_obj.suffix,
                "file_size": file_path_obj.stat().st_size,
                "is_file_attachment": True,
                **kwargs
            }
        )

        self.messages.append(file_message)
        self.last_activity = datetime.now()

        attachment_info = {
            "file_path": str(file_path_obj),
            "description": file_description,
            "file_type": file_type or file_path_obj.suffix,
            "size_bytes": file_path_obj.stat().st_size,
            "added_at": datetime.now()
        }

        logger.info(f"Added file to conversation {self.conversation_id}: {file_path_obj.name}")
        return attachment_info

    def get_history(self, include_system: bool = True, include_files: bool = True) -> List[Dict[str, Any]]:
        """
        Get conversation message history.

        Args:
            include_system: Include system messages
            include_files: Include file attachments

        Returns:
            List of message dictionaries
        """
        history = []

        for msg in self.messages:
            # Filter based on parameters
            if not include_system and msg.role == "system":
                continue
            if not include_files and msg.metadata.get("is_file_attachment"):
                continue

            history.append({
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp,
                "metadata": msg.metadata
            })

        return history

    def clear_history(self, keep_system: bool = True):
        """
        Clear conversation history.

        Args:
            keep_system: Keep system messages
        """
        if keep_system:
            # Keep only system messages
            self.messages = [msg for msg in self.messages if msg.role == "system"]
        else:
            self.messages = []

        self.total_tokens_used = 0
        self.total_cost = 0.0
        self.last_activity = datetime.now()

        logger.info(f"Cleared history for conversation {self.conversation_id}")

    def get_stats(self) -> Dict[str, Any]:
        """Get conversation statistics."""
        return {
            "conversation_id": self.conversation_id,
            "created_at": self.created_at,
            "last_activity": self.last_activity,
            "message_count": len(self.messages),
            "total_tokens_used": self.total_tokens_used,
            "total_cost": self.total_cost,
            "provider": self.provider.__class__.__name__,
            "model": self.provider.model,
            "artifact_count": len(self.artifacts),
            "artifacts_by_type": self._get_artifacts_by_type_count()
        }

    def get_artifacts(self, artifact_type=None, language=None) -> List[Artifact]:
        """
        Get artifacts from the conversation, optionally filtered.

        Args:
            artifact_type: Filter by ArtifactType (e.g., ArtifactType.CODE)
            language: Filter by programming language

        Returns:
            List of matching artifacts
        """
        artifacts = self.artifacts

        if artifact_type:
            artifacts = [a for a in artifacts if a.type == artifact_type]

        if language:
            artifacts = [a for a in artifacts if a.language == language.lower()]

        return artifacts

    def save_all_artifacts(self, directory: str, overwrite: bool = False) -> List[Path]:
        """
        Save all conversation artifacts to a directory.

        Args:
            directory: Directory to save artifacts to
            overwrite: Whether to overwrite existing files

        Returns:
            List of paths where artifacts were saved
        """
        directory_path = Path(directory)
        directory_path.mkdir(parents=True, exist_ok=True)

        saved_paths = []
        for artifact in self.artifacts:
            try:
                saved_path = artifact.save(directory_path, overwrite=overwrite)
                saved_paths.append(saved_path)
                logger.info(f"Saved artifact {artifact.artifact_id} to {saved_path}")
            except Exception as e:
                logger.error(f"Failed to save artifact {artifact.artifact_id}: {e}")

        return saved_paths

    def validate_all_artifacts(self) -> Dict[str, Any]:
        """
        Validate all artifacts in the conversation.

        Returns:
            Summary of validation results
        """
        results = {
            "total_artifacts": len(self.artifacts),
            "valid_artifacts": 0,
            "invalid_artifacts": 0,
            "artifacts_with_warnings": 0,
            "validation_details": []
        }

        for artifact in self.artifacts:
            validation = artifact.validate()

            if validation["is_valid"]:
                results["valid_artifacts"] += 1
            else:
                results["invalid_artifacts"] += 1

            if validation["warnings"]:
                results["artifacts_with_warnings"] += 1

            results["validation_details"].append({
                "artifact_id": artifact.artifact_id,
                "filename": artifact.filename,
                "type": artifact.type.value,
                "validation": validation
            })

        return results

    def find_artifact(self, artifact_id: str) -> Optional[Artifact]:
        """Find an artifact by its ID."""
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                return artifact
        return None

    def remove_artifact(self, artifact_id: str) -> bool:
        """
        Remove an artifact from the conversation.

        Args:
            artifact_id: ID of the artifact to remove

        Returns:
            bool: True if artifact was removed, False if not found
        """
        for i, artifact in enumerate(self.artifacts):
            if artifact.artifact_id == artifact_id:
                del self.artifacts[i]
                logger.info(f"Removed artifact {artifact_id} from conversation {self.conversation_id}")
                return True
        return False

    def _get_artifacts_by_type_count(self) -> Dict[str, int]:
        """Get count of artifacts by type."""
        type_counts = {}
        for artifact in self.artifacts:
            type_name = artifact.type.value
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
        return type_counts

    def _get_context_messages(self) -> List[Message]:
        """Get messages to send as context, respecting history limits."""
        max_history = self.config.max_history_length

        if len(self.messages) <= max_history:
            return self.messages

        # Keep system messages and most recent messages
        system_messages = [msg for msg in self.messages if msg.role == "system"]
        recent_messages = [msg for msg in self.messages if msg.role != "system"][-max_history:]

        return system_messages + recent_messages

    def __repr__(self) -> str:
        """String representation of the conversation."""
        return (f"Conversation(id={self.conversation_id[:8]}..., "
                f"messages={len(self.messages)}, "
                f"tokens={self.total_tokens_used})")

    def __len__(self) -> int:
        """Return number of messages in conversation."""
        return len(self.messages)