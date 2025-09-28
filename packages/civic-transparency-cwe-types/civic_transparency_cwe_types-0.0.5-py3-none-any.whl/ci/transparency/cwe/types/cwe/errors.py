"""CWE domain error types with rich context.

Domain-specific error hierarchy for CWE operations. Extends base error types
to provide CWE-specific context like CWE IDs, relationship information, and
validation details.

Design principles:
    - Inherits consistent formatting from base error types
    - Adds CWE-specific context (CWE IDs, relationships, categories)
    - Provides specific exception types for different CWE failure scenarios
    - Maintains minimal memory overhead with __slots__

Core CWE errors:
    - CweError: Base CWE error with CWE ID context
    - CweLoadingError: CWE definition loading failures
    - CweValidationError: CWE validation failures
    - CweRelationshipError: CWE relationship validation failures

Typical usage:
    from ci.transparency.cwe.types.cwe import CweValidationError

    try:
        validate_cwe_definition(cwe_data)
    except CweValidationError as e:
        # Rich context: "Validation failed | CWE: CWE-79 | Field: relationships[0] | File: cwe-79.yaml"
        logger.error(f"CWE validation failed: {e}")
"""

from pathlib import Path

from ci.transparency.cwe.types.base.errors import (
    BaseLoadingError,
    BaseTransparencyError,
)


class CweError(BaseLoadingError):
    """Base exception for CWE operations.

    Extends BaseLoadingError to add CWE-specific context like CWE identifiers
    and categories.
    """

    __slots__ = ("cwe_id", "category")

    def __init__(
        self,
        message: str,
        cwe_id: str | None = None,
        category: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE error with CWE-specific context.

        Args:
            message: The error message
            cwe_id: Optional CWE identifier (e.g., "CWE-79")
            category: Optional CWE category
            file_path: Optional file path where the error occurred
        """
        super().__init__(message, file_path)
        self.cwe_id = cwe_id
        self.category = category

    def get_context_parts(self) -> list[str]:
        """Add CWE context to error message."""
        parts = super().get_context_parts()

        # Add CWE ID first for prominence
        if self.cwe_id:
            parts.insert(0, f"CWE: {self.cwe_id}")

        if self.category:
            parts.append(f"Category: {self.category}")

        return parts


# ============================================================================
# CWE loading error types
# ============================================================================


class CweLoadingError(CweError):
    """Base CWE loading error."""


class CweFileNotFoundError(CweLoadingError):
    """CWE definition file could not be found."""


class CweParsingError(CweLoadingError):
    """CWE definition file could not be parsed."""

    __slots__ = ("parser_type", "line_number", "parse_details")

    def __init__(
        self,
        message: str,
        parser_type: str | None = None,
        line_number: int | None = None,
        parse_details: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE parsing error.

        Args:
            message: The parsing error message
            parser_type: Optional type of parser (e.g., "YAML", "JSON")
            line_number: Optional line number where parsing failed
            parse_details: Optional detailed parsing error information
            cwe_id: Optional CWE identifier
            file_path: Optional file path that failed to parse
        """
        super().__init__(message, cwe_id, None, file_path)
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


class CweDuplicateError(CweLoadingError):
    """Duplicate CWE ID detected during loading."""

    __slots__ = ("existing_file", "duplicate_file")

    def __init__(
        self,
        message: str,
        cwe_id: str | None = None,
        existing_file: Path | None = None,
        duplicate_file: Path | None = None,
    ):
        """Initialize CWE duplicate error.

        Args:
            message: The duplicate error message
            cwe_id: Optional CWE identifier that's duplicated
            existing_file: Optional path to the existing CWE file
            duplicate_file: Optional path to the duplicate CWE file
        """
        super().__init__(message, cwe_id, None, duplicate_file)
        self.existing_file = existing_file
        self.duplicate_file = duplicate_file

    def get_context_parts(self) -> list[str]:
        """Add duplicate file context to error message."""
        parts = super().get_context_parts()

        if self.existing_file:
            parts.append(f"Existing: {self.existing_file}")

        if self.duplicate_file:
            parts.append(f"Duplicate: {self.duplicate_file}")

        return parts


class CweInvalidFormatError(CweLoadingError):
    """CWE definition format is invalid or unsupported."""

    __slots__ = ("expected_format", "detected_format", "format_issue")

    def __init__(
        self,
        message: str,
        expected_format: str | None = None,
        detected_format: str | None = None,
        format_issue: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE invalid format error.

        Args:
            message: The format error message
            expected_format: Optional expected format (e.g., "YAML")
            detected_format: Optional detected format
            format_issue: Optional description of the format issue
            cwe_id: Optional CWE identifier
            file_path: Optional file path with format issue
        """
        super().__init__(message, cwe_id, None, file_path)
        self.expected_format = expected_format
        self.detected_format = detected_format
        self.format_issue = format_issue

    def get_context_parts(self) -> list[str]:
        """Add format context to error message."""
        parts = super().get_context_parts()

        if self.expected_format:
            parts.append(f"Expected: {self.expected_format}")

        if self.detected_format:
            parts.append(f"Detected: {self.detected_format}")

        if self.format_issue:
            parts.append(f"Issue: {self.format_issue}")

        return parts


class CweMissingFieldError(CweLoadingError):
    """Required CWE field is missing from definition."""

    __slots__ = ("field_name", "required_fields")

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        required_fields: list[str] | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE missing field error.

        Args:
            message: The missing field error message
            field_name: Optional name of the missing field
            required_fields: Optional list of all required fields
            cwe_id: Optional CWE identifier
            file_path: Optional file path with missing field
        """
        super().__init__(message, cwe_id, None, file_path)
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
# CWE validation error types
# ============================================================================


class CweValidationError(CweError):
    """Base CWE validation error."""

    __slots__ = ("validation_type",)

    def __init__(
        self,
        message: str,
        validation_type: str | None = None,
        cwe_id: str | None = None,
        category: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE validation error.

        Args:
            message: The validation error message
            validation_type: Optional type of validation (e.g., "field", "schema", "relationship")
            cwe_id: Optional CWE identifier
            category: Optional CWE category
            file_path: Optional file path being validated
        """
        super().__init__(message, cwe_id, category, file_path)
        self.validation_type = validation_type

    def get_context_parts(self) -> list[str]:
        """Add validation type to context."""
        parts = super().get_context_parts()

        if self.validation_type:
            parts.append(f"Validation: {self.validation_type}")

        return parts


class CweFieldValidationError(CweValidationError):
    """CWE field-level validation failed."""

    __slots__ = ("field_name", "field_value", "validation_rule", "expected_value")

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        field_value: str | None = None,
        validation_rule: str | None = None,
        expected_value: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE field validation error.

        Args:
            message: The field validation error message
            field_name: Optional name of the field that failed validation
            field_value: Optional actual value of the field
            validation_rule: Optional validation rule that was violated
            expected_value: Optional expected value for the field
            cwe_id: Optional CWE identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, "field", cwe_id, None, file_path)
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


class CweSchemaValidationError(CweValidationError):
    """CWE schema validation failed."""

    __slots__ = ("schema_name", "schema_version", "field_path")

    def __init__(
        self,
        message: str,
        schema_name: str | None = None,
        schema_version: str | None = None,
        field_path: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE schema validation error.

        Args:
            message: The schema validation error message
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            field_path: Optional path to the field that failed (e.g., "relationships[0].id")
            cwe_id: Optional CWE identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, "schema", cwe_id, None, file_path)
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.field_path = field_path

    def get_context_parts(self) -> list[str]:
        """Add schema validation context to error message."""
        parts = super().get_context_parts()

        if self.schema_name:
            if self.schema_version:
                parts.insert(-1, f"Schema: {self.schema_name}-{self.schema_version}")
            else:
                parts.insert(-1, f"Schema: {self.schema_name}")

        if self.field_path:
            parts.append(f"Field: {self.field_path}")

        return parts


class CweConstraintViolationError(CweValidationError):
    """CWE constraint validation failed."""

    __slots__ = ("constraint_name", "constraint_value", "actual_value")

    def __init__(
        self,
        message: str,
        constraint_name: str | None = None,
        constraint_value: str | None = None,
        actual_value: str | None = None,
        cwe_id: str | None = None,
        category: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE constraint violation error.

        Args:
            message: The constraint violation error message
            constraint_name: Optional name of the constraint
            constraint_value: Optional expected constraint value
            actual_value: Optional actual value that violated the constraint
            cwe_id: Optional CWE identifier
            category: Optional CWE category
            file_path: Optional file path being validated
        """
        super().__init__(message, "constraint", cwe_id, category, file_path)
        self.constraint_name = constraint_name
        self.constraint_value = constraint_value
        self.actual_value = actual_value

    def get_context_parts(self) -> list[str]:
        """Add constraint details to context."""
        parts = super().get_context_parts()

        if self.constraint_name:
            parts.append(f"Constraint: {self.constraint_name}")

        if self.constraint_value:
            parts.append(f"Expected: {self.constraint_value}")

        if self.actual_value:
            parts.append(f"Actual: {self.actual_value}")

        return parts


# ============================================================================
# CWE relationship error types
# ============================================================================


class CweRelationshipError(CweValidationError):
    """CWE relationship validation failed."""

    __slots__ = ("related_cwe_id", "relationship_type", "relationship_direction")

    def __init__(
        self,
        message: str,
        related_cwe_id: str | None = None,
        relationship_type: str | None = None,
        relationship_direction: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE relationship error.

        Args:
            message: The relationship error message
            related_cwe_id: Optional ID of the related CWE
            relationship_type: Optional type of relationship (e.g., "ChildOf", "ParentOf")
            relationship_direction: Optional direction (e.g., "outbound", "inbound")
            cwe_id: Optional source CWE identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, "relationship", cwe_id, None, file_path)
        self.related_cwe_id = related_cwe_id
        self.relationship_type = relationship_type
        self.relationship_direction = relationship_direction

    def get_context_parts(self) -> list[str]:
        """Add relationship context to error message."""
        parts = super().get_context_parts()

        if self.related_cwe_id:
            parts.append(f"Related: {self.related_cwe_id}")

        if self.relationship_type:
            parts.append(f"Type: {self.relationship_type}")

        if self.relationship_direction:
            parts.append(f"Direction: {self.relationship_direction}")

        return parts


class CweCircularRelationshipError(CweRelationshipError):
    """Circular CWE relationship detected."""

    __slots__ = ("relationship_chain",)

    def __init__(
        self,
        message: str,
        relationship_chain: list[str] | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE circular relationship error.

        Args:
            message: The circular relationship error message
            relationship_chain: Optional chain of CWE IDs that form the cycle
            cwe_id: Optional source CWE identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, None, "circular", None, cwe_id, file_path)
        self.relationship_chain = relationship_chain or []

    def get_context_parts(self) -> list[str]:
        """Add relationship chain to context."""
        parts = super().get_context_parts()

        if self.relationship_chain:
            chain = " → ".join(self.relationship_chain)
            parts.append(f"Chain: {chain}")

        return parts


class CweOrphanedError(CweRelationshipError):
    """CWE has no valid relationships."""

    def __init__(
        self,
        message: str,
        cwe_id: str | None = None,
        category: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE orphaned error.

        Args:
            message: The orphaned error message
            cwe_id: Optional CWE identifier that's orphaned
            category: Optional CWE category
            file_path: Optional file path being validated
        """
        super().__init__(message, None, "orphaned", None, cwe_id, file_path)
        self.category = category

    def get_context_parts(self) -> list[str]:
        """Add category to context for orphaned CWEs."""
        parts = super().get_context_parts()

        if self.category:
            parts.append(f"Category: {self.category}")

        return parts


class CweInvalidReferenceError(CweRelationshipError):
    """CWE relationship references unknown CWE ID."""

    __slots__ = ("reference_source",)

    def __init__(
        self,
        message: str,
        related_cwe_id: str | None = None,
        reference_source: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE invalid reference error.

        Args:
            message: The invalid reference error message
            related_cwe_id: Optional ID that couldn't be found
            reference_source: Optional source of the reference (e.g., "relationships", "taxonomy")
            cwe_id: Optional source CWE identifier
            file_path: Optional file path being validated
        """
        super().__init__(message, related_cwe_id, "invalid_reference", None, cwe_id, file_path)
        self.reference_source = reference_source

    def get_context_parts(self) -> list[str]:
        """Add reference source to context."""
        parts = super().get_context_parts()

        if self.reference_source:
            parts.append(f"Source: {self.reference_source}")

        return parts


# ============================================================================
# CWE processing error types
# ============================================================================


class CweProcessingError(BaseTransparencyError):
    """CWE processing operation failed."""

    __slots__ = ("operation", "processed_count", "total_count")

    def __init__(
        self,
        message: str,
        operation: str | None = None,
        processed_count: int | None = None,
        total_count: int | None = None,
    ):
        """Initialize CWE processing error.

        Args:
            message: The processing error message
            operation: Optional name of the operation being performed
            processed_count: Optional number of items processed before failure
            total_count: Optional total number of items to process
        """
        super().__init__(message)
        self.operation = operation
        self.processed_count = processed_count
        self.total_count = total_count

    def get_context_parts(self) -> list[str]:
        """Add processing context to error message."""
        parts = super().get_context_parts()

        if self.operation:
            parts.append(f"Operation: {self.operation}")

        if self.processed_count is not None and self.total_count is not None:
            parts.append(f"Progress: {self.processed_count}/{self.total_count}")
        elif self.processed_count is not None:
            parts.append(f"Processed: {self.processed_count}")

        return parts


class CweIntegrityError(CweError):
    """CWE data integrity violation."""

    __slots__ = ("integrity_check", "expected_value", "actual_value")

    def __init__(
        self,
        message: str,
        integrity_check: str | None = None,
        expected_value: str | None = None,
        actual_value: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE integrity error.

        Args:
            message: The integrity error message
            integrity_check: Optional name of the integrity check that failed
            expected_value: Optional expected value
            actual_value: Optional actual value found
            cwe_id: Optional CWE identifier
            file_path: Optional file path being checked
        """
        super().__init__(message, cwe_id, None, file_path)
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


class CweConfigurationError(BaseTransparencyError):
    """CWE configuration error."""

    __slots__ = ("config_key", "config_value", "valid_values")

    def __init__(
        self,
        message: str,
        config_key: str | None = None,
        config_value: str | None = None,
        valid_values: list[str] | None = None,
    ):
        """Initialize CWE configuration error.

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
