"""Base error types for transparency operations.

Provides base exception classes with contextual information and consistent
formatting patterns. Domain-specific error hierarchies extend these base
types to provide rich error context and structured error handling.

Design principles:
    - Contextual: errors capture relevant context (file paths, IDs, frameworks)
    - Consistent: all errors follow the same __str__ formatting pattern
    - Slotted: minimal memory overhead with __slots__
    - Hierarchical: base classes allow generic error handling

Core error hierarchy:
    - BaseTransparencyError: Root exception for all transparency operations
    - BaseLoadingError: Loading operations (adds file_path context)
    - BaseValidationError: Validation operations (adds validation_context)

Common error types:
    - FileNotFoundError: File could not be found during loading
    - ParsingError: File could not be parsed (YAML, JSON, etc.)
    - ValidationError: File content failed validation checks
    - ConfigurationError: Configuration is invalid or incomplete

All errors use consistent formatting: "message | Context1: value | Context2: value"
"""

from pathlib import Path


class BaseTransparencyError(Exception):
    """Base exception for all transparency operations.

    Provides consistent error formatting and context tracking across all
    transparency-related exceptions.
    """

    __slots__ = ("message",)

    def __init__(self, message: str):
        """Initialize base transparency error.

        Args:
            message: The error message describing what went wrong
        """
        super().__init__(message)
        self.message = message

    def get_context_parts(self) -> list[str]:
        """Get contextual information parts for error formatting.

        Subclasses override this to add their own contextual information.

        Returns:
            List of context strings (e.g., ["File: path.yaml", "ID: CWE-123"])
        """
        return []

    def __str__(self) -> str:
        """Format error with message and context information.

        Returns:
            Formatted error string with message and context joined by " | "
        """
        parts = [self.message]
        parts.extend(self.get_context_parts())
        return " | ".join(parts)


class BaseLoadingError(BaseTransparencyError):
    """Base exception for loading operations.

    Adds file path context that's common to all loading operations.
    """

    __slots__ = ("file_path",)

    def __init__(self, message: str, file_path: Path | None = None):
        """Initialize loading error with optional file context.

        Args:
            message: The error message
            file_path: Optional path to the file being loaded
        """
        super().__init__(message)
        self.file_path = file_path

    def get_context_parts(self) -> list[str]:
        """Add file path to context if available."""
        parts = super().get_context_parts()
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return parts


class BaseValidationError(BaseTransparencyError):
    """Base exception for validation operations.

    Can be extended by domain-specific validation errors to add
    validation-specific context.
    """

    __slots__ = ("validation_context",)

    def __init__(self, message: str, validation_context: str | None = None):
        """Initialize validation error with optional context.

        Args:
            message: The validation error message
            validation_context: Optional context about what was being validated
        """
        super().__init__(message)
        self.validation_context = validation_context

    def get_context_parts(self) -> list[str]:
        """Add validation context if available."""
        parts = super().get_context_parts()
        if self.validation_context:
            parts.append(f"Context: {self.validation_context}")
        return parts


class BaseProcessingError(BaseTransparencyError):
    """Base exception for processing operations.

    Adds processing context for operations that transform or analyze data.
    """

    __slots__ = ("operation", "item_id")

    def __init__(self, message: str, operation: str | None = None, item_id: str | None = None):
        """Initialize processing error with optional context.

        Args:
            message: The error message
            operation: Optional name of the operation being performed
            item_id: Optional identifier of the item being processed
        """
        super().__init__(message)
        self.operation = operation
        self.item_id = item_id

    def get_context_parts(self) -> list[str]:
        """Add processing context if available."""
        parts = super().get_context_parts()
        if self.operation:
            parts.append(f"Operation: {self.operation}")
        if self.item_id:
            parts.append(f"Item: {self.item_id}")
        return parts


# ============================================================================
# Common error types that extend the base classes
# ============================================================================


class LoadingFileNotFoundError(BaseLoadingError):
    """File could not be found during loading operation."""


class LoadingParsingError(BaseLoadingError):
    """File could not be parsed (YAML, JSON, etc.)."""

    __slots__ = ("parser_type",)

    def __init__(self, message: str, file_path: Path | None = None, parser_type: str | None = None):
        """Initialize parsing error with parser context.

        Args:
            message: The parsing error message
            file_path: Optional path to the file that failed to parse
            parser_type: Optional type of parser used (e.g., "YAML", "JSON")
        """
        super().__init__(message, file_path)
        self.parser_type = parser_type

    def get_context_parts(self) -> list[str]:
        """Add parser type to context if available."""
        parts = super().get_context_parts()
        if self.parser_type:
            parts.append(f"Parser: {self.parser_type}")
        return parts


class LoadingValidationError(BaseLoadingError):
    """File content failed validation checks."""

    __slots__ = ("validation_rule",)

    def __init__(
        self, message: str, file_path: Path | None = None, validation_rule: str | None = None
    ):
        """Initialize validation error with rule context.

        Args:
            message: The validation error message
            file_path: Optional path to the file that failed validation
            validation_rule: Optional name of the validation rule that failed
        """
        super().__init__(message, file_path)
        self.validation_rule = validation_rule

    def get_context_parts(self) -> list[str]:
        """Add validation rule to context if available."""
        parts = super().get_context_parts()
        if self.validation_rule:
            parts.append(f"Rule: {self.validation_rule}")
        return parts


class ConfigurationError(BaseTransparencyError):
    """Configuration is invalid or incomplete."""

    __slots__ = ("config_key", "config_file")

    def __init__(
        self, message: str, config_key: str | None = None, config_file: Path | None = None
    ):
        """Initialize configuration error with config context.

        Args:
            message: The configuration error message
            config_key: Optional configuration key that caused the error
            config_file: Optional path to the configuration file
        """
        super().__init__(message)
        self.config_key = config_key
        self.config_file = config_file

    def get_context_parts(self) -> list[str]:
        """Add configuration context if available."""
        parts = super().get_context_parts()
        if self.config_key:
            parts.append(f"Config: {self.config_key}")
        if self.config_file:
            parts.append(f"File: {self.config_file}")
        return parts


class VersionError(BaseTransparencyError):
    """Version compatibility or format error."""

    __slots__ = ("version_found", "version_expected")

    def __init__(
        self, message: str, version_found: str | None = None, version_expected: str | None = None
    ):
        """Initialize version error with version context.

        Args:
            message: The version error message
            version_found: Optional version that was found
            version_expected: Optional version that was expected
        """
        super().__init__(message)
        self.version_found = version_found
        self.version_expected = version_expected

    def get_context_parts(self) -> list[str]:
        """Add version information to context if available."""
        parts = super().get_context_parts()
        if self.version_found:
            parts.append(f"Found: {self.version_found}")
        if self.version_expected:
            parts.append(f"Expected: {self.version_expected}")
        return parts


class SchemaError(BaseValidationError):
    """Schema validation failed."""

    __slots__ = ("schema_name", "field_path")

    def __init__(
        self,
        message: str,
        validation_context: str | None = None,
        schema_name: str | None = None,
        field_path: str | None = None,
    ):
        """Initialize schema error with schema context.

        Args:
            message: The schema validation error message
            validation_context: Optional validation context
            schema_name: Optional name of the schema
            field_path: Optional path to the field that failed (e.g., "data.items[0].id")
        """
        super().__init__(message, validation_context)
        self.schema_name = schema_name
        self.field_path = field_path

    def get_context_parts(self) -> list[str]:
        """Add schema context if available."""
        parts = super().get_context_parts()
        if self.schema_name:
            parts.append(f"Schema: {self.schema_name}")
        if self.field_path:
            parts.append(f"Field: {self.field_path}")
        return parts


class NetworkError(BaseTransparencyError):
    """Network operation failed."""

    __slots__ = ("url", "status_code")

    def __init__(self, message: str, url: str | None = None, status_code: int | None = None):
        """Initialize network error with network context.

        Args:
            message: The network error message
            url: Optional URL that was being accessed
            status_code: Optional HTTP status code
        """
        super().__init__(message)
        self.url = url
        self.status_code = status_code

    def get_context_parts(self) -> list[str]:
        """Add network context if available."""
        parts = super().get_context_parts()
        if self.url:
            parts.append(f"URL: {self.url}")
        if self.status_code:
            parts.append(f"Status: {self.status_code}")
        return parts


class TransparencyTimeoutError(BaseTransparencyError):
    """Operation timed out."""

    __slots__ = ("timeout_seconds", "operation")

    def __init__(
        self, message: str, timeout_seconds: float | None = None, operation: str | None = None
    ):
        """Initialize timeout error with timing context.

        Args:
            message: The timeout error message
            timeout_seconds: Optional timeout duration that was exceeded
            operation: Optional name of the operation that timed out
        """
        super().__init__(message)
        self.timeout_seconds = timeout_seconds
        self.operation = operation

    def get_context_parts(self) -> list[str]:
        """Add timeout context if available."""
        parts = super().get_context_parts()
        if self.operation:
            parts.append(f"Operation: {self.operation}")
        if self.timeout_seconds:
            parts.append(f"Timeout: {self.timeout_seconds}s")
        return parts


class AbortedError(BaseTransparencyError):
    """Operation was aborted before completion."""

    __slots__ = ("abort_reason",)

    def __init__(self, message: str, abort_reason: str | None = None):
        """Initialize aborted error with reason.

        Args:
            message: The abort error message
            abort_reason: Optional reason why the operation was aborted
        """
        super().__init__(message)
        self.abort_reason = abort_reason

    def get_context_parts(self) -> list[str]:
        """Add abort reason to context if available."""
        parts = super().get_context_parts()
        if self.abort_reason:
            parts.append(f"Reason: {self.abort_reason}")
        return parts
