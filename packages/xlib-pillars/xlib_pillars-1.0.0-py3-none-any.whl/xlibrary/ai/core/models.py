"""Core data models for AI provider system."""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union
from enum import Enum
from pathlib import Path
from datetime import datetime
import json
import re
import uuid
import ast


class AIErrorCodes:
    """Standard error codes for AI responses."""
    # API and provider errors
    API_ERROR = "api_error"
    RATE_LIMIT = "rate_limit"
    AUTHENTICATION = "authentication"
    TIMEOUT = "timeout"
    SERVICE_UNAVAILABLE = "service_unavailable"

    # Content and input errors
    INVALID_INPUT = "invalid_input"
    CONTENT_FILTER = "content_filter"
    TOKEN_LIMIT = "token_limit"
    CONTEXT_LENGTH = "context_length"

    # Model and capability errors
    MODEL_UNAVAILABLE = "model_unavailable"
    UNSUPPORTED_FEATURE = "unsupported_feature"

    # Network and connectivity errors
    NETWORK_ERROR = "network_error"
    CONNECTION_ERROR = "connection_error"

    # Generic errors
    UNKNOWN_ERROR = "unknown_error"
    INTERNAL_ERROR = "internal_error"


class ArtifactType(Enum):
    """Types of artifacts that can be extracted from AI responses."""
    CODE = "code"                         # Source code files
    SCRIPT = "script"                     # Executable scripts
    DOCUMENT = "document"                 # Text documents
    CONFIG = "config"                     # Configuration files
    DATA = "data"                         # Data files (JSON, CSV, etc.)
    MARKUP = "markup"                     # HTML, Markdown, etc.
    QUERY = "query"                       # SQL queries, etc.
    SCHEMA = "schema"                     # Database schemas, API specs
    TEST = "test"                         # Test files
    DOCUMENTATION = "documentation"        # Documentation files

    # Legacy aliases for backward compatibility
    JSON = "data"
    MARKDOWN = "markup"
    TEXT = "document"
    XML = "markup"
    YAML = "data"
    HTML = "markup"


@dataclass
class Message:
    """A single message in a conversation."""
    role: str  # "user", "assistant", "system"
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        if self.role not in ["user", "assistant", "system"]:
            raise ValueError(f"Invalid role: {self.role}")
        if self.timestamp is None:
            self.timestamp = datetime.now()


@dataclass
class Artifact:
    """
    Comprehensive artifact extracted from AI responses.

    Matches the design document specification with full metadata,
    validation, and file system integration.
    """
    # Identification
    artifact_id: str
    type: ArtifactType
    filename: str

    # Content
    content: str
    language: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None

    # Metadata
    size_bytes: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    created_from_provider: str = "unknown"
    created_from_model: str = "unknown"

    # Validation and processing
    is_executable: bool = False
    mime_type: str = "text/plain"
    encoding: str = "utf-8"

    # Relationships
    parent_conversation_id: Optional[str] = None
    derived_from_artifact: Optional[str] = None

    # Additional metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Initialize computed fields."""
        if not self.artifact_id:
            self.artifact_id = str(uuid.uuid4())

        if not self.size_bytes:
            self.size_bytes = len(self.content.encode(self.encoding))

        # Set MIME type based on artifact type and language
        self._update_mime_type()

        # Determine if executable
        self._check_executable()

    def save(self, path: Union[str, Path], overwrite: bool = False) -> Path:
        """
        Save artifact to file system.

        Args:
            path: File path or directory to save to
            overwrite: Whether to overwrite existing files

        Returns:
            Path: Actual path where file was saved

        Raises:
            FileExistsError: If file exists and overwrite=False
        """
        file_path = Path(path)

        # If path is a directory, use the artifact's filename
        if file_path.is_dir():
            file_path = file_path / self.filename

        # Create parent directories if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Check for existing file
        if file_path.exists() and not overwrite:
            raise FileExistsError(f"File already exists: {file_path}")

        # Write content to file
        with open(file_path, 'w', encoding=self.encoding) as f:
            f.write(self.content)

        # Update metadata
        self.metadata['saved_at'] = datetime.now()
        self.metadata['saved_path'] = str(file_path)

        return file_path

    def validate(self) -> Dict[str, Any]:
        """
        Validate artifact content and return validation results.

        Returns:
            Dict with validation results including errors and warnings
        """
        result = {
            "is_valid": True,
            "errors": [],
            "warnings": [],
            "checks_performed": []
        }

        # Basic content validation
        if not self.content.strip():
            result["is_valid"] = False
            result["errors"].append("Artifact content is empty")
        result["checks_performed"].append("content_not_empty")

        # Type-specific validation
        if self.type in [ArtifactType.DATA, ArtifactType.JSON]:
            self._validate_json(result)
        elif self.type == ArtifactType.CODE:
            self._validate_code(result)
        elif self.type == ArtifactType.MARKUP:
            self._validate_markup(result)
        elif self.type == ArtifactType.QUERY:
            self._validate_query(result)
        elif self.type == ArtifactType.CONFIG:
            self._validate_config(result)

        # Size validation
        if self.size_bytes > 10 * 1024 * 1024:  # 10MB
            result["warnings"].append("Artifact is very large (>10MB)")
        result["checks_performed"].append("size_check")

        # Encoding validation
        try:
            self.content.encode(self.encoding)
        except UnicodeEncodeError as e:
            result["errors"].append(f"Content cannot be encoded as {self.encoding}: {e}")
            result["is_valid"] = False
        result["checks_performed"].append("encoding_check")

        return result

    def _update_mime_type(self):
        """Update MIME type based on type and language."""
        mime_mappings = {
            ArtifactType.CODE: {
                'python': 'text/x-python',
                'javascript': 'application/javascript',
                'typescript': 'application/typescript',
                'java': 'text/x-java-source',
                'cpp': 'text/x-c++src',
                'c': 'text/x-csrc',
                'go': 'text/x-go',
                'rust': 'text/x-rust',
                'default': 'text/x-script'
            },
            ArtifactType.DATA: {
                'json': 'application/json',
                'yaml': 'application/x-yaml',
                'csv': 'text/csv',
                'xml': 'application/xml',
                'default': 'application/json'
            },
            ArtifactType.MARKUP: {
                'html': 'text/html',
                'markdown': 'text/markdown',
                'xml': 'application/xml',
                'default': 'text/html'
            },
            ArtifactType.SCRIPT: 'application/x-shellscript',
            ArtifactType.DOCUMENT: 'text/plain',
            ArtifactType.CONFIG: 'text/plain',
            ArtifactType.QUERY: 'application/sql',
            ArtifactType.SCHEMA: 'application/json',
            ArtifactType.TEST: 'text/x-script',
            ArtifactType.DOCUMENTATION: 'text/markdown'
        }

        if self.type in mime_mappings:
            type_mapping = mime_mappings[self.type]
            if isinstance(type_mapping, dict):
                self.mime_type = type_mapping.get(self.language, type_mapping['default'])
            else:
                self.mime_type = type_mapping

    def _check_executable(self):
        """Determine if the artifact is executable."""
        executable_types = {ArtifactType.SCRIPT, ArtifactType.CODE}
        executable_languages = {'python', 'bash', 'sh', 'javascript', 'node'}

        self.is_executable = (
            self.type in executable_types or
            self.language in executable_languages or
            self.content.startswith('#!')
        )

    def _validate_json(self, result: Dict[str, Any]):
        """Validate JSON content."""
        try:
            json.loads(self.content)
            result["checks_performed"].append("json_syntax")
        except json.JSONDecodeError as e:
            result["is_valid"] = False
            result["errors"].append(f"Invalid JSON: {e}")

    def _validate_code(self, result: Dict[str, Any]):
        """Validate code content."""
        if self.language == 'python':
            try:
                ast.parse(self.content)
                result["checks_performed"].append("python_syntax")
            except SyntaxError as e:
                result["warnings"].append(f"Python syntax issue: {e}")

        # Check for common code issues
        if len(self.content.splitlines()) > 1000:
            result["warnings"].append("Code artifact is very long (>1000 lines)")

        result["checks_performed"].append("code_structure")

    def _validate_markup(self, result: Dict[str, Any]):
        """Validate markup content."""
        if self.language in ['html', 'xml']:
            # Basic tag matching
            open_tags = re.findall(r'<([^/][^>]*)>', self.content)
            close_tags = re.findall(r'</([^>]*)>', self.content)

            if len(open_tags) != len(close_tags):
                result["warnings"].append("HTML/XML may have mismatched tags")

        result["checks_performed"].append("markup_structure")

    def _validate_query(self, result: Dict[str, Any]):
        """Validate query content."""
        # Basic SQL validation
        sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP']
        content_upper = self.content.upper()

        if not any(keyword in content_upper for keyword in sql_keywords):
            result["warnings"].append("Query doesn't contain common SQL keywords")

        result["checks_performed"].append("query_keywords")

    def _validate_config(self, result: Dict[str, Any]):
        """Validate configuration content."""
        # Try to parse as various config formats
        formats_tried = []

        # Try JSON
        try:
            json.loads(self.content)
            formats_tried.append("json")
        except:
            pass

        # Try basic key=value
        if '=' in self.content:
            formats_tried.append("key_value")

        if not formats_tried:
            result["warnings"].append("Configuration format not recognized")

        result["checks_performed"].append("config_format")


@dataclass
class AIResponse:
    """
    Complete response from an AI provider.

    Contains all metadata, performance info, and optional artifacts.
    """
    # Core response data
    content: str
    provider: str
    model: str
    timestamp: Optional[datetime] = None

    # Token usage and cost
    tokens_used: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cached_tokens: int = 0
    reasoning_tokens: int = 0
    cost_estimate: float = 0.0

    # Performance metadata
    latency_ms: float = 0.0
    finish_reason: str = "stop"
    request_id: Optional[str] = None

    # Advanced features
    thinking_trace: Optional[str] = None
    artifacts: List[Artifact] = field(default_factory=list)

    # Rate limiting info
    rate_limit_remaining: Optional[int] = None
    rate_limit_reset: Optional[datetime] = None
    daily_usage: Optional[int] = None

    # Context and metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    conversation_context: Optional[str] = None
    safety_scores: Optional[Dict[str, float]] = None

    # Streaming specific
    is_streaming: bool = False
    chunk_index: Optional[int] = None
    is_final_chunk: bool = True

    # Success and error handling
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    is_error: bool = False

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

        # Calculate total tokens if not provided
        if self.tokens_used == 0:
            self.tokens_used = self.input_tokens + self.output_tokens + self.reasoning_tokens

    @property
    def success(self) -> bool:
        """
        Determine if the AI response was successful.

        A response is considered successful if:
        1. It's not marked as an error
        2. It has content (not empty)
        3. The finish_reason indicates successful completion

        Returns:
            bool: True if the response was successful, False otherwise
        """
        # Explicit error flag takes precedence
        if self.is_error:
            return False

        # Check if we have content
        if not self.content or not self.content.strip():
            return False

        # Check finish_reason for success indicators
        success_reasons = {"stop", "length", "max_tokens"}
        error_reasons = {"error", "content_filter", "function_call"}

        if self.finish_reason in error_reasons:
            return False

        return True

    @classmethod
    def create_error(cls,
                    error_message: str,
                    error_code: str = AIErrorCodes.UNKNOWN_ERROR,
                    provider: str = "unknown",
                    model: str = "unknown",
                    **kwargs) -> 'AIResponse':
        """
        Create an AIResponse object representing an error.

        Args:
            error_message: Human-readable error message
            error_code: Machine-readable error code (e.g., "rate_limit", "api_error", "timeout")
            provider: AI provider name
            model: Model name
            **kwargs: Additional fields to set on the response

        Returns:
            AIResponse: Error response object with success=False
        """
        return cls(
            content="",  # Empty content for error responses
            provider=provider,
            model=model,
            error_code=error_code,
            error_message=error_message,
            is_error=True,
            finish_reason="error",
            **kwargs
        )

    def extract_artifacts(self) -> List[Artifact]:
        """
        Extract artifacts from response content using comprehensive pattern matching.

        Supports multiple formats:
        - Code blocks (```language)
        - Inline code spans
        - SQL queries
        - Configuration files
        - JSON/YAML data
        - Documentation sections
        """
        artifacts = []

        # Extract fenced code blocks
        artifacts.extend(self._extract_fenced_code_blocks())

        # Extract inline code artifacts
        artifacts.extend(self._extract_inline_artifacts())

        # Extract structured data
        artifacts.extend(self._extract_structured_data())

        # Extract queries
        artifacts.extend(self._extract_queries())

        # Store artifacts and return
        self.artifacts.extend(artifacts)
        return artifacts

    def _extract_fenced_code_blocks(self) -> List[Artifact]:
        """Extract artifacts from fenced code blocks (```language)."""
        artifacts = []

        # Enhanced regex to capture optional titles and metadata
        pattern = r'```(?:(\w+)(?:\s+(.+?))?)?\n(.*?)\n```'
        matches = re.findall(pattern, self.content, re.DOTALL)

        for i, (lang, metadata, code) in enumerate(matches):
            if not code.strip():
                continue

            # Determine artifact type from language
            artifact_type = self._determine_artifact_type(lang, code)

            # Parse metadata if present (title, filename, etc.)
            title = None
            filename = None
            description = None

            if metadata:
                # Look for common patterns: filename="...", title="..."
                if filename_match := re.search(r'filename[=:]"?([^"\s]+)"?', metadata):
                    filename = filename_match.group(1)
                if title_match := re.search(r'title[=:]"?([^"]+)"?', metadata):
                    title = title_match.group(1)
                else:
                    # Use the whole metadata as title if no explicit title
                    title = metadata.strip()

            # Generate filename if not provided
            if not filename:
                extensions = self._get_extensions_for_type(artifact_type, lang)
                filename = f"extracted_{artifact_type.value}_{i}{extensions[0]}"

            artifact = Artifact(
                artifact_id=str(uuid.uuid4()),
                content=code.strip(),
                type=artifact_type,
                filename=filename,
                language=lang.lower() if lang else None,
                title=title,
                description=description,
                created_from_provider=self.provider,
                created_from_model=self.model,
                parent_conversation_id=self.conversation_context,
                metadata={
                    'extraction_method': 'fenced_code_block',
                    'block_index': i,
                    'raw_metadata': metadata
                }
            )
            artifacts.append(artifact)

        return artifacts

    def _extract_inline_artifacts(self) -> List[Artifact]:
        """Extract artifacts from inline code and text patterns."""
        artifacts = []

        # Look for SQL queries in text
        sql_patterns = [
            r'(?i)(SELECT\s+.*?(?:;|$))',
            r'(?i)(INSERT\s+INTO\s+.*?(?:;|$))',
            r'(?i)(UPDATE\s+.*?(?:;|$))',
            r'(?i)(DELETE\s+FROM\s+.*?(?:;|$))',
            r'(?i)(CREATE\s+(?:TABLE|INDEX|VIEW)\s+.*?(?:;|$))'
        ]

        for i, pattern in enumerate(sql_patterns):
            matches = re.findall(pattern, self.content, re.MULTILINE | re.DOTALL)
            for j, query in enumerate(matches):
                if len(query.strip()) > 20:  # Filter out very short matches
                    artifact = Artifact(
                        artifact_id=str(uuid.uuid4()),
                        content=query.strip(),
                        type=ArtifactType.QUERY,
                        filename=f"query_{i}_{j}.sql",
                        language='sql',
                        title=f"SQL Query {i}-{j}",
                        created_from_provider=self.provider,
                        created_from_model=self.model,
                        parent_conversation_id=self.conversation_context,
                        metadata={'extraction_method': 'inline_sql_pattern'}
                    )
                    artifacts.append(artifact)

        return artifacts

    def _extract_structured_data(self) -> List[Artifact]:
        """Extract JSON, YAML, and other structured data."""
        artifacts = []

        # JSON objects (look for {...} patterns with simple nesting support)
        json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
        potential_json = re.findall(json_pattern, self.content)

        for i, json_str in enumerate(potential_json):
            if len(json_str) > 50:  # Filter out small objects
                try:
                    json.loads(json_str)  # Validate JSON
                    artifact = Artifact(
                        artifact_id=str(uuid.uuid4()),
                        content=json_str,
                        type=ArtifactType.DATA,
                        filename=f"data_{i}.json",
                        language='json',
                        title=f"JSON Data {i}",
                        created_from_provider=self.provider,
                        created_from_model=self.model,
                        parent_conversation_id=self.conversation_context,
                        metadata={'extraction_method': 'json_pattern'}
                    )
                    artifacts.append(artifact)
                except json.JSONDecodeError:
                    continue

        return artifacts

    def _extract_queries(self) -> List[Artifact]:
        """Extract database queries and API calls."""
        artifacts = []

        # More sophisticated SQL detection
        sql_indicators = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP']
        lines = self.content.split('\n')

        current_query = []
        in_query = False

        for line in lines:
            line_upper = line.upper().strip()

            # Start of query
            if any(line_upper.startswith(kw) for kw in sql_indicators):
                if current_query:  # Save previous query
                    self._save_query_artifact(artifacts, '\n'.join(current_query))
                current_query = [line]
                in_query = True
            elif in_query:
                current_query.append(line)
                # End of query (semicolon or empty line)
                if line.strip().endswith(';') or line.strip() == '':
                    self._save_query_artifact(artifacts, '\n'.join(current_query))
                    current_query = []
                    in_query = False

        # Save final query if exists
        if current_query:
            self._save_query_artifact(artifacts, '\n'.join(current_query))

        return artifacts

    def _save_query_artifact(self, artifacts: List[Artifact], query_content: str):
        """Helper to create query artifact."""
        if len(query_content.strip()) > 20:
            artifact = Artifact(
                artifact_id=str(uuid.uuid4()),
                content=query_content.strip(),
                type=ArtifactType.QUERY,
                filename=f"query_{len(artifacts)}.sql",
                language='sql',
                title=f"SQL Query {len(artifacts)}",
                created_from_provider=self.provider,
                created_from_model=self.model,
                parent_conversation_id=self.conversation_context,
                metadata={'extraction_method': 'multiline_sql'}
            )
            artifacts.append(artifact)

    def _determine_artifact_type(self, language: str, content: str) -> ArtifactType:
        """Determine artifact type from language and content."""
        if not language:
            # Guess from content
            if content.strip().startswith('{') or content.strip().startswith('['):
                return ArtifactType.DATA
            elif any(kw in content.upper() for kw in ['SELECT', 'INSERT', 'UPDATE', 'DELETE']):
                return ArtifactType.QUERY
            elif content.strip().startswith('<'):
                return ArtifactType.MARKUP
            else:
                return ArtifactType.CODE

        language = language.lower()

        # Language-based type mapping
        type_mappings = {
            # Data formats
            'json': ArtifactType.DATA,
            'yaml': ArtifactType.DATA,
            'yml': ArtifactType.DATA,
            'csv': ArtifactType.DATA,
            'toml': ArtifactType.DATA,

            # Markup
            'html': ArtifactType.MARKUP,
            'xml': ArtifactType.MARKUP,
            'markdown': ArtifactType.MARKUP,
            'md': ArtifactType.MARKUP,

            # Scripts
            'bash': ArtifactType.SCRIPT,
            'sh': ArtifactType.SCRIPT,
            'shell': ArtifactType.SCRIPT,
            'powershell': ArtifactType.SCRIPT,
            'ps1': ArtifactType.SCRIPT,

            # Queries
            'sql': ArtifactType.QUERY,
            'mysql': ArtifactType.QUERY,
            'postgresql': ArtifactType.QUERY,
            'sqlite': ArtifactType.QUERY,

            # Configuration
            'conf': ArtifactType.CONFIG,
            'config': ArtifactType.CONFIG,
            'ini': ArtifactType.CONFIG,
            'cfg': ArtifactType.CONFIG,

            # Tests
            'test': ArtifactType.TEST,
            'spec': ArtifactType.TEST,

            # Schema
            'schema': ArtifactType.SCHEMA,
            'openapi': ArtifactType.SCHEMA,
            'swagger': ArtifactType.SCHEMA,
        }

        return type_mappings.get(language, ArtifactType.CODE)

    def _get_extensions_for_type(self, artifact_type: ArtifactType, language: str = None) -> List[str]:
        """Get appropriate file extensions for artifact type."""
        if language:
            language_extensions = {
                'python': ['.py'],
                'javascript': ['.js'],
                'typescript': ['.ts'],
                'java': ['.java'],
                'cpp': ['.cpp', '.cxx'],
                'c': ['.c'],
                'go': ['.go'],
                'rust': ['.rs'],
                'sql': ['.sql'],
                'json': ['.json'],
                'yaml': ['.yaml', '.yml'],
                'xml': ['.xml'],
                'html': ['.html'],
                'css': ['.css'],
                'bash': ['.sh'],
                'shell': ['.sh'],
                'powershell': ['.ps1'],
            }
            if language.lower() in language_extensions:
                return language_extensions[language.lower()]

        type_extensions = {
            ArtifactType.CODE: ['.py', '.js', '.java'],
            ArtifactType.SCRIPT: ['.sh', '.bat'],
            ArtifactType.DATA: ['.json', '.yaml'],
            ArtifactType.MARKUP: ['.html', '.md'],
            ArtifactType.QUERY: ['.sql'],
            ArtifactType.CONFIG: ['.conf', '.ini'],
            ArtifactType.SCHEMA: ['.json', '.yaml'],
            ArtifactType.TEST: ['.test.py', '.spec.js'],
            ArtifactType.DOCUMENT: ['.txt', '.md'],
            ArtifactType.DOCUMENTATION: ['.md']
        }

        return type_extensions.get(artifact_type, ['.txt'])