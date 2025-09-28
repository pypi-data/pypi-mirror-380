"""Standards domain error types with rich context.

Domain-specific error hierarchy for standards operations. Extends base error types
to provide standards-specific context like standard IDs, mapping information, and
validation details.

Design principles:
    - Inherits consistent formatting from base error types
    - Adds standards-specific context (standard IDs, mappings, formats)
    - Provides specific exception types for different standards failure scenarios
    - Maintains minimal memory overhead with __slots__

Core standards errors:
    - StandardsError: Base standards error with standard ID context
    - StandardsLoadingError: Standards definition loading failures
    - StandardsValidationError: Standards validation failures
    - StandardsMappingError: Standards mapping validation failures

Typical usage:
    from ci.transparency.cwe.types.standards import StandardsValidationError

    try:
        validate_standards_definition(standards_data)
    except StandardsValidationError as e:
        # Rich context: "Validation failed | Standard: NIST-SP-800-53 | Field: controls[0] | File: nist.yaml"
        logger.error(f"Standards validation failed: {e}")
"""

from pathlib import Path

from ci.transparency.cwe.types.base.errors import (
    BaseLoadingError,
    BaseTransparencyError,
)


class StandardsError(BaseLoadingError):
    """Base exception for standards operations.

    Extends BaseLoadingError to add standards-specific context like standard
    identifiers and framework information.
    """

    __slots__ = ("standard_id", "framework")

    def __init__(
        self,
        message: str,
        standard_id: str | None = None,
        framework: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards error with standards-specific context.

        Args:
            message: The error message
            standard_id: Optional standard identifier (e.g., "NIST-SP-800-53")
            framework: Optional framework name (e.g., "NIST", "ISO")
            file_path: Optional file path where the error occurred
        """
        super().__init__(message, file_path)
        self.standard_id = standard_id
        self.framework = framework

    def get_context_parts(self) -> list[str]:
        """Add standards context to error message."""
        parts = super().get_context_parts()

        # Add standard ID first for prominence
        if self.standard_id:
            parts.insert(0, f"Standard: {self.standard_id}")

        if self.framework:
            parts.append(f"Framework: {self.framework}")

        return parts


# ============================================================================
# Standards loading error types
# ============================================================================


class StandardsLoadingError(StandardsError):
    """Base standards loading error."""


class StandardsFileNotFoundError(StandardsLoadingError):
    """Standards definition file could not be found."""


class StandardsParsingError(StandardsLoadingError):
    """Standards definition file could not be parsed."""

    __slots__ = ("parser_type", "line_number", "parse_details")

    def __init__(
        self,
        message: str,
        parser_type: str | None = None,
        line_number: int | None = None,
        parse_details: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards parsing error.

        Args:
            message: The parsing error message
            parser_type: Optional type of parser (e.g., "YAML", "JSON")
            line_number: Optional line number where parsing failed
            parse_details: Optional detailed parsing error information
            standard_id: Optional standard identifier
            file_path: Optional file path that failed to parse
        """
        super().__init__(message, standard_id, None, file_path)
        self.parser_type = parser_type
        self.line_number = line_number
        self.parse_details = parse_details

    def get_context_parts(self) -> list[str]:
        """Add parsing context to error message."""
        parts = super().get_context_parts()

        if self.parser_type:
            parts.append(f"Parser: {self.parser_type}")

        if self.line_number is not None:
            parts.append(f"Line: {self.line_number}")

        if self.parse_details:
            parts.append(f"Details: {self.parse_details}")

        return parts


class StandardsInvalidFormatError(StandardsLoadingError):
    """Standards definition format is invalid or unsupported."""

    __slots__ = ("detected_format", "supported_formats", "format_issue")

    def __init__(
        self,
        message: str,
        detected_format: str | None = None,
        supported_formats: list[str] | None = None,
        format_issue: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards invalid format error.

        Args:
            message: The format error message
            detected_format: Optional detected format
            supported_formats: Optional list of supported formats
            format_issue: Optional description of the format issue
            standard_id: Optional standard identifier
            file_path: Optional file path with format issue
        """
        super().__init__(message, standard_id, None, file_path)
        self.detected_format = detected_format
        self.supported_formats = supported_formats or []
        self.format_issue = format_issue

    def get_context_parts(self) -> list[str]:
        """Add format context to error message."""
        parts = super().get_context_parts()

        if self.detected_format:
            parts.append(f"Detected: {self.detected_format}")

        if self.supported_formats:
            supported = ", ".join(self.supported_formats)
            parts.append(f"Supported: {supported}")

        if self.format_issue:
            parts.append(f"Issue: {self.format_issue}")

        return parts


class StandardsMissingFieldError(StandardsLoadingError):
    """Required standards field is missing from definition."""

    __slots__ = ("field_name", "required_fields")

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        required_fields: list[str] | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards missing field error.

        Args:
            message: The missing field error message
            field_name: Optional name of the missing field
            required_fields: Optional list of all required fields
            standard_id: Optional standard identifier
            file_path: Optional file path with missing field
        """
        super().__init__(message, standard_id, None, file_path)
        self.field_name = field_name
        self.required_fields = required_fields or []

    def get_context_parts(self) -> list[str]:
        """Add missing field context to error message."""
        parts = super().get_context_parts()

        if self.field_name:
            parts.append(f"Field: {self.field_name}")

        if self.required_fields:
            required = ", ".join(self.required_fields)
            parts.append(f"Required: {required}")

        return parts


# ============================================================================
# Standards validation error types
# ============================================================================


class StandardsValidationError(StandardsError):
    """Base standards validation error."""

    __slots__ = ("validation_type",)

    def __init__(
        self,
        message: str,
        validation_type: str | None = None,
        standard_id: str | None = None,
        framework: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards validation error.

        Args:
            message: The validation error message
            validation_type: Optional type of validation (e.g., "field", "mapping", "constraint")
            standard_id: Optional standard identifier
            framework: Optional framework name
            file_path: Optional file path being validated
        """
        super().__init__(message, standard_id, framework, file_path)
        self.validation_type = validation_type

    def get_context_parts(self) -> list[str]:
        """Add validation type to context."""
        parts = super().get_context_parts()

        if self.validation_type:
            parts.append(f"Validation: {self.validation_type}")

        return parts


class StandardsFieldValidationError(StandardsValidationError):
    """Standards field-level validation failed."""

    __slots__ = ("field_name", "field_value", "validation_rule", "expected_value")

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        field_value: str | None = None,
        validation_rule: str | None = None,
        expected_value: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards field validation error.

        Args:
            message: The field validation error message
            field_name: Optional name of the field that failed validation
            field_value: Optional actual value of the field
            validation_rule: Optional validation rule that was violated
            expected_value: Optional expected value for the field
            standard_id: Optional standard identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, "field", standard_id, None, file_path)
        self.field_name = field_name
        self.field_value = field_value
        self.validation_rule = validation_rule
        self.expected_value = expected_value

    def get_context_parts(self) -> list[str]:
        """Add field validation details to context."""
        parts = super().get_context_parts()

        if self.field_name:
            parts.append(f"Field: {self.field_name}")

        if self.field_value is not None:
            parts.append(f"Value: {self.field_value}")

        if self.expected_value:
            parts.append(f"Expected: {self.expected_value}")

        if self.validation_rule:
            parts.append(f"Rule: {self.validation_rule}")

        return parts


class StandardsConstraintViolationError(StandardsValidationError):
    """Standards constraint validation failed."""

    __slots__ = ("constraint_name", "expected", "actual")

    def __init__(
        self,
        message: str,
        constraint_name: str | None = None,
        expected: str | None = None,
        actual: str | None = None,
        standard_id: str | None = None,
        framework: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards constraint violation error.

        Args:
            message: The constraint violation error message
            constraint_name: Optional name of the constraint
            expected: Optional expected constraint value
            actual: Optional actual value that violated the constraint
            standard_id: Optional standard identifier
            framework: Optional framework name
            file_path: Optional file path being validated
        """
        super().__init__(message, "constraint", standard_id, framework, file_path)
        self.constraint_name = constraint_name
        self.expected = expected
        self.actual = actual

    def get_context_parts(self) -> list[str]:
        """Add constraint details to context."""
        parts = super().get_context_parts()

        if self.constraint_name:
            parts.append(f"Constraint: {self.constraint_name}")

        if self.expected:
            parts.append(f"Expected: {self.expected}")

        if self.actual:
            parts.append(f"Actual: {self.actual}")

        return parts


# ============================================================================
# Standards mapping error types
# ============================================================================


class StandardsMappingError(StandardsError):
    """Base standards mapping validation error."""

    __slots__ = ("mapping_key", "target_id", "mapping_type")

    def __init__(
        self,
        message: str,
        mapping_key: str | None = None,
        target_id: str | None = None,
        mapping_type: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards mapping error.

        Args:
            message: The mapping error message
            mapping_key: Optional mapping key or control ID
            target_id: Optional target ID being mapped to (e.g., CWE ID)
            mapping_type: Optional type of mapping (e.g., "cwe", "control")
            standard_id: Optional standard identifier
            file_path: Optional file path being processed
        """
        super().__init__(message, standard_id, None, file_path)
        self.mapping_key = mapping_key
        self.target_id = target_id
        self.mapping_type = mapping_type

    def get_context_parts(self) -> list[str]:
        """Add mapping context to error message."""
        parts = super().get_context_parts()

        if self.mapping_key:
            parts.append(f"Mapping: {self.mapping_key}")

        if self.target_id:
            parts.append(f"Target: {self.target_id}")

        if self.mapping_type:
            parts.append(f"Type: {self.mapping_type}")

        return parts


class StandardsInvalidMappingError(StandardsMappingError):
    """Standards mapping references unknown target ID."""

    __slots__ = ("reference_source",)

    def __init__(
        self,
        message: str,
        target_id: str | None = None,
        mapping_key: str | None = None,
        reference_source: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards invalid mapping error.

        Args:
            message: The invalid mapping error message
            target_id: Optional target ID that couldn't be found
            mapping_key: Optional mapping key that failed
            reference_source: Optional source of the reference (e.g., "cwe_mappings", "controls")
            standard_id: Optional standard identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, mapping_key, target_id, "invalid", standard_id, file_path)
        self.reference_source = reference_source

    def get_context_parts(self) -> list[str]:
        """Add reference source to context."""
        parts = super().get_context_parts()

        if self.reference_source:
            parts.append(f"Source: {self.reference_source}")

        return parts


class StandardsDuplicateMappingError(StandardsMappingError):
    """Duplicate standards mapping detected."""

    __slots__ = ("existing_target", "duplicate_target")

    def __init__(
        self,
        message: str,
        mapping_key: str | None = None,
        existing_target: str | None = None,
        duplicate_target: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards duplicate mapping error.

        Args:
            message: The duplicate mapping error message
            mapping_key: Optional mapping key that's duplicated
            existing_target: Optional existing target ID
            duplicate_target: Optional duplicate target ID
            standard_id: Optional standard identifier
            file_path: Optional file path being processed
        """
        super().__init__(
            message, mapping_key, duplicate_target, "duplicate", standard_id, file_path
        )
        self.existing_target = existing_target
        self.duplicate_target = duplicate_target

    def get_context_parts(self) -> list[str]:
        """Add duplicate mapping context to error message."""
        parts = super().get_context_parts()

        if self.existing_target:
            parts.append(f"Existing: {self.existing_target}")

        if self.duplicate_target:
            parts.append(f"Duplicate: {self.duplicate_target}")

        return parts


# ============================================================================
# Standards format error types
# ============================================================================


class StandardsFormatError(StandardsError):
    """Standards formatting/serialization problem."""

    __slots__ = ("format_type", "export_template")

    def __init__(
        self,
        message: str,
        format_type: str | None = None,
        export_template: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards format error.

        Args:
            message: The format error message
            format_type: Optional format type (e.g., "export", "template")
            export_template: Optional export template name
            standard_id: Optional standard identifier
            file_path: Optional file path with format issue
        """
        super().__init__(message, standard_id, None, file_path)
        self.format_type = format_type
        self.export_template = export_template

    def get_context_parts(self) -> list[str]:
        """Add format context to error message."""
        parts = super().get_context_parts()

        if self.format_type:
            parts.append(f"Format: {self.format_type}")

        if self.export_template:
            parts.append(f"Template: {self.export_template}")

        return parts


# ============================================================================
# Standards processing error types
# ============================================================================


class StandardsConfigurationError(BaseTransparencyError):
    """Standards configuration error."""

    __slots__ = ("config_key", "config_value", "valid_values")

    def __init__(
        self,
        message: str,
        config_key: str | None = None,
        config_value: str | None = None,
        valid_values: list[str] | None = None,
    ):
        """Initialize standards configuration error.

        Args:
            message: The configuration error message
            config_key: Optional configuration key that caused the error
            config_value: Optional invalid configuration value
            valid_values: Optional list of valid configuration values
        """
        super().__init__(message)
        self.config_key = config_key
        self.config_value = config_value
        self.valid_values = valid_values or []

    def get_context_parts(self) -> list[str]:
        """Add configuration context to error message."""
        parts = super().get_context_parts()

        if self.config_key:
            parts.append(f"Config: {self.config_key}")

        if self.config_value:
            parts.append(f"Value: {self.config_value}")

        if self.valid_values:
            valid_str = ", ".join(self.valid_values)
            parts.append(f"Valid: {valid_str}")

        return parts


class StandardsProcessingError(StandardsError):
    """Standards processing operation failed."""

    __slots__ = ("operation", "stage", "processed_count")

    def __init__(
        self,
        message: str,
        operation: str | None = None,
        stage: str | None = None,
        processed_count: int | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards processing error.

        Args:
            message: The processing error message
            operation: Optional name of the operation being performed
            stage: Optional processing stage (e.g., "loading", "validation", "mapping")
            processed_count: Optional number of items processed before failure
            standard_id: Optional standard identifier
            file_path: Optional file path being processed
        """
        super().__init__(message, standard_id, None, file_path)
        self.operation = operation
        self.stage = stage
        self.processed_count = processed_count

    def get_context_parts(self) -> list[str]:
        """Add processing context to error message."""
        parts = super().get_context_parts()

        if self.operation:
            parts.append(f"Operation: {self.operation}")

        if self.stage:
            parts.append(f"Stage: {self.stage}")

        if self.processed_count is not None:
            parts.append(f"Processed: {self.processed_count}")

        return parts


class StandardsIntegrityError(StandardsError):
    """Standards data integrity violation."""

    __slots__ = ("integrity_check", "expected_value", "actual_value")

    def __init__(
        self,
        message: str,
        integrity_check: str | None = None,
        expected_value: str | None = None,
        actual_value: str | None = None,
        standard_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize standards integrity error.

        Args:
            message: The integrity error message
            integrity_check: Optional name of the integrity check that failed
            expected_value: Optional expected value
            actual_value: Optional actual value found
            standard_id: Optional standard identifier
            file_path: Optional file path being checked
        """
        super().__init__(message, standard_id, None, file_path)
        self.integrity_check = integrity_check
        self.expected_value = expected_value
        self.actual_value = actual_value

    def get_context_parts(self) -> list[str]:
        """Add integrity check details to context."""
        parts = super().get_context_parts()

        if self.integrity_check:
            parts.append(f"Check: {self.integrity_check}")

        if self.expected_value:
            parts.append(f"Expected: {self.expected_value}")

        if self.actual_value:
            parts.append(f"Actual: {self.actual_value}")

        return parts
