"""CWE schema error types with rich schema context.

Domain-specific error hierarchy for CWE schema operations. Extends base error
types to provide CWE schema-specific context like schema names, versions,
validation paths, and freeze violation details.

Design principles:
    - Inherits consistent formatting from base error types
    - Adds CWE schema-specific context (schema names, versions, field paths)
    - Provides specific exception types for different schema failure scenarios
    - Maintains minimal memory overhead with __slots__

Core CWE schema errors:
    - CweSchemaError: Base CWE schema error with schema context
    - CweSchemaLoadingError: CWE schema loading/parsing failures
    - CweSchemaValidationError: CWE data validation against schema failures
    - CweSchemaFreezeError: CWE schema freeze/compatibility violations

Typical usage:
    from ci.transparency.cwe.types.cwe.schema import CweSchemaValidationError

    try:
        validate_cwe_against_schema(cwe_data, schema)
    except CweSchemaValidationError as e:
        # Rich context: "Validation failed | Schema: cwe-v2.0 | Field: relationships[0].id | CWE: CWE-A001"
        logger.error(f"CWE schema error: {e}")
"""

from pathlib import Path

from ci.transparency.cwe.types.base.errors import BaseLoadingError, BaseValidationError


class CweSchemaError(BaseLoadingError):
    """Base exception for CWE schema operations.

    Extends BaseLoadingError to add CWE schema-specific context like
    schema names, versions, and CWE identifiers.
    """

    __slots__ = ("schema_name", "schema_version", "cwe_id")

    def __init__(
        self,
        message: str,
        schema_name: str | None = None,
        schema_version: str | None = None,
        cwe_id: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE schema error.

        Args:
            message: The error message
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            cwe_id: Optional CWE ID being processed
            file_path: Optional file path where the error occurred
        """
        super().__init__(message, file_path)
        self.schema_name = schema_name
        self.schema_version = schema_version
        self.cwe_id = cwe_id

    def get_context_parts(self) -> list[str]:
        """Add CWE schema context to error message."""
        parts = super().get_context_parts()

        # Add schema info first for prominence
        if self.schema_name:
            if self.schema_version:
                parts.insert(0, f"Schema: {self.schema_name}-{self.schema_version}")
            else:
                parts.insert(0, f"Schema: {self.schema_name}")
        elif self.schema_version:
            parts.insert(0, f"Version: {self.schema_version}")

        # Add CWE ID if available
        if self.cwe_id:
            parts.insert(-1 if self.file_path else len(parts), f"CWE: {self.cwe_id}")

        return parts


# ============================================================================
# CWE schema loading error types
# ============================================================================


class CweSchemaLoadingError(CweSchemaError):
    """CWE schema loading operation failed."""


class CweSchemaNotFoundError(CweSchemaLoadingError):
    """CWE schema file could not be found."""


class CweSchemaParsingError(CweSchemaLoadingError):
    """CWE schema file could not be parsed as valid JSON."""

    __slots__ = ("parse_error",)

    def __init__(
        self,
        message: str,
        parse_error: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE schema parsing error.

        Args:
            message: The parsing error message
            parse_error: Optional details of the parsing error
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            file_path: Optional file path that failed to parse
        """
        super().__init__(message, schema_name, schema_version, None, file_path)
        self.parse_error = parse_error

    def get_context_parts(self) -> list[str]:
        """Add parsing error details to context."""
        parts = super().get_context_parts()
        if self.parse_error:
            parts.append(f"Parse Error: {self.parse_error}")
        return parts


class CweSchemaVersionError(CweSchemaLoadingError):
    """CWE schema version is not supported or invalid."""

    __slots__ = ("supported_versions",)

    def __init__(
        self,
        message: str,
        schema_version: str | None = None,
        supported_versions: list[str] | None = None,
        schema_name: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE schema version error.

        Args:
            message: The version error message
            schema_version: Optional version that was found
            supported_versions: Optional list of supported versions
            schema_name: Optional name of the schema
            file_path: Optional file path with version issue
        """
        super().__init__(message, schema_name, schema_version, None, file_path)
        self.supported_versions = supported_versions or []

    def get_context_parts(self) -> list[str]:
        """Add supported versions to context."""
        parts = super().get_context_parts()
        if self.supported_versions:
            supported = ", ".join(self.supported_versions)
            parts.append(f"Supported: {supported}")
        return parts


class CweSchemaFormatError(CweSchemaLoadingError):
    """CWE schema format is invalid or malformed."""

    __slots__ = ("format_issue",)

    def __init__(
        self,
        message: str,
        format_issue: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        file_path: Path | None = None,
    ):
        """Initialize CWE schema format error.

        Args:
            message: The format error message
            format_issue: Optional description of the format issue
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            file_path: Optional file path with format issue
        """
        super().__init__(message, schema_name, schema_version, None, file_path)
        self.format_issue = format_issue

    def get_context_parts(self) -> list[str]:
        """Add format issue details to context."""
        parts = super().get_context_parts()
        if self.format_issue:
            parts.append(f"Issue: {self.format_issue}")
        return parts


# ============================================================================
# CWE schema validation error types
# ============================================================================


class CweSchemaValidationError(CweSchemaError):
    """Base CWE schema validation error."""


class CweDataValidationError(CweSchemaValidationError):
    """CWE data validation against schema failed."""

    __slots__ = ("validation_path", "expected_type", "actual_value")

    def __init__(
        self,
        message: str,
        validation_path: str | None = None,
        expected_type: str | None = None,
        actual_value: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        cwe_id: str | None = None,
    ):
        """Initialize CWE data validation error.

        Args:
            message: The validation error message
            validation_path: Optional path to the field that failed validation
            expected_type: Optional expected type or format
            actual_value: Optional actual value that failed validation
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            cwe_id: Optional CWE ID being validated
        """
        super().__init__(message, schema_name, schema_version, cwe_id)
        self.validation_path = validation_path
        self.expected_type = expected_type
        self.actual_value = actual_value

    def get_context_parts(self) -> list[str]:
        """Add validation details to context."""
        parts = super().get_context_parts()

        if self.validation_path:
            parts.append(f"Field: {self.validation_path}")

        if self.expected_type:
            parts.append(f"Expected: {self.expected_type}")

        if self.actual_value:
            parts.append(f"Actual: {self.actual_value}")

        return parts


class CweFieldValidationError(CweSchemaValidationError):
    """CWE field-level validation against schema failed."""

    __slots__ = ("field_name", "field_path", "constraint_type")

    def __init__(
        self,
        message: str,
        field_name: str | None = None,
        field_path: str | None = None,
        constraint_type: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        cwe_id: str | None = None,
    ):
        """Initialize CWE field validation error.

        Args:
            message: The field validation error message
            field_name: Optional name of the field
            field_path: Optional full path to the field (e.g., "relationships[0].id")
            constraint_type: Optional type of constraint that failed (e.g., "required", "pattern")
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            cwe_id: Optional CWE ID being validated
        """
        super().__init__(message, schema_name, schema_version, cwe_id)
        self.field_name = field_name
        self.field_path = field_path
        self.constraint_type = constraint_type

    def get_context_parts(self) -> list[str]:
        """Add field validation details to context."""
        parts = super().get_context_parts()

        if self.field_path:
            parts.append(f"Field: {self.field_path}")
        elif self.field_name:
            parts.append(f"Field: {self.field_name}")

        if self.constraint_type:
            parts.append(f"Constraint: {self.constraint_type}")

        return parts


class CweSchemaConstraintError(CweSchemaValidationError):
    """CWE schema constraint validation failed."""

    __slots__ = ("constraint_name", "constraint_value", "violated_rule")

    def __init__(
        self,
        message: str,
        constraint_name: str | None = None,
        constraint_value: str | None = None,
        violated_rule: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        cwe_id: str | None = None,
    ):
        """Initialize CWE schema constraint error.

        Args:
            message: The constraint error message
            constraint_name: Optional name of the constraint
            constraint_value: Optional expected constraint value
            violated_rule: Optional description of the violated rule
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
            cwe_id: Optional CWE ID being validated
        """
        super().__init__(message, schema_name, schema_version, cwe_id)
        self.constraint_name = constraint_name
        self.constraint_value = constraint_value
        self.violated_rule = violated_rule

    def get_context_parts(self) -> list[str]:
        """Add constraint details to context."""
        parts = super().get_context_parts()

        if self.constraint_name:
            parts.append(f"Constraint: {self.constraint_name}")

        if self.constraint_value:
            parts.append(f"Expected: {self.constraint_value}")

        if self.violated_rule:
            parts.append(f"Rule: {self.violated_rule}")

        return parts


# ============================================================================
# CWE schema freeze and compatibility error types
# ============================================================================


class CweSchemaFreezeError(BaseValidationError):
    """Base CWE schema freeze violation error."""

    __slots__ = ("old_version", "new_version", "freeze_rule")

    def __init__(
        self,
        message: str,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
        validation_context: str | None = None,
    ):
        """Initialize CWE schema freeze error.

        Args:
            message: The freeze error message
            old_version: Optional old schema version
            new_version: Optional new schema version
            freeze_rule: Optional name of the freeze rule violated
            validation_context: Optional validation context
        """
        super().__init__(message, validation_context)
        self.old_version = old_version
        self.new_version = new_version
        self.freeze_rule = freeze_rule

    def get_context_parts(self) -> list[str]:
        """Add freeze violation details to context."""
        parts = super().get_context_parts()

        if self.old_version and self.new_version:
            parts.insert(0, f"Versions: {self.old_version} → {self.new_version}")
        elif self.old_version:
            parts.insert(0, f"Old Version: {self.old_version}")
        elif self.new_version:
            parts.insert(0, f"New Version: {self.new_version}")

        if self.freeze_rule:
            parts.append(f"Rule: {self.freeze_rule}")

        return parts


class CweFreezeViolationError(CweSchemaFreezeError):
    """CWE schema freeze rule violation detected."""

    __slots__ = ("violation_type", "affected_fields")

    def __init__(
        self,
        message: str,
        violation_type: str | None = None,
        affected_fields: list[str] | None = None,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
    ):
        """Initialize CWE freeze violation error.

        Args:
            message: The violation error message
            violation_type: Optional type of violation (e.g., "field_removed", "constraint_tightened")
            affected_fields: Optional list of fields affected by the violation
            old_version: Optional old schema version
            new_version: Optional new schema version
            freeze_rule: Optional name of the freeze rule violated
        """
        super().__init__(message, old_version, new_version, freeze_rule)
        self.violation_type = violation_type
        self.affected_fields = affected_fields or []

    def get_context_parts(self) -> list[str]:
        """Add violation details to context."""
        parts = super().get_context_parts()

        if self.violation_type:
            parts.append(f"Violation: {self.violation_type}")

        if self.affected_fields:
            fields = ", ".join(self.affected_fields)
            parts.append(f"Affected: {fields}")

        return parts


class CweSchemaCompatibilityError(CweSchemaFreezeError):
    """CWE schema compatibility check failed."""

    __slots__ = ("compatibility_issue", "backward_compatible")

    def __init__(
        self,
        message: str,
        compatibility_issue: str | None = None,
        backward_compatible: bool = False,
        old_version: str | None = None,
        new_version: str | None = None,
    ):
        """Initialize CWE schema compatibility error.

        Args:
            message: The compatibility error message
            compatibility_issue: Optional description of the compatibility issue
            backward_compatible: Whether the change is backward compatible
            old_version: Optional old schema version
            new_version: Optional new schema version
        """
        super().__init__(message, old_version, new_version)
        self.compatibility_issue = compatibility_issue
        self.backward_compatible = backward_compatible

    def get_context_parts(self) -> list[str]:
        """Add compatibility details to context."""
        parts = super().get_context_parts()

        if self.compatibility_issue:
            parts.append(f"Issue: {self.compatibility_issue}")

        parts.append(f"Backward Compatible: {'Yes' if self.backward_compatible else 'No'}")

        return parts


class CweBreakingChangeError(CweSchemaFreezeError):
    """CWE schema breaking change detected."""

    __slots__ = ("change_type", "change_description", "impact_level")

    def __init__(
        self,
        message: str,
        change_type: str | None = None,
        change_description: str | None = None,
        impact_level: str | None = None,
        old_version: str | None = None,
        new_version: str | None = None,
    ):
        """Initialize CWE breaking change error.

        Args:
            message: The breaking change error message
            change_type: Optional type of breaking change (e.g., "field_removed", "type_changed")
            change_description: Optional detailed description of the change
            impact_level: Optional impact level (e.g., "high", "medium", "low")
            old_version: Optional old schema version
            new_version: Optional new schema version
        """
        super().__init__(message, old_version, new_version)
        self.change_type = change_type
        self.change_description = change_description
        self.impact_level = impact_level

    def get_context_parts(self) -> list[str]:
        """Add breaking change details to context."""
        parts = super().get_context_parts()

        if self.change_type:
            parts.append(f"Change: {self.change_type}")

        if self.impact_level:
            parts.append(f"Impact: {self.impact_level}")

        if self.change_description:
            parts.append(f"Description: {self.change_description}")

        return parts


# ============================================================================
# Specialized CWE schema error types
# ============================================================================


class CweSchemaReferenceError(CweSchemaValidationError):
    """CWE schema reference could not be resolved."""

    __slots__ = ("reference_path", "reference_target")

    def __init__(
        self,
        message: str,
        reference_path: str | None = None,
        reference_target: str | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
    ):
        """Initialize CWE schema reference error.

        Args:
            message: The reference error message
            reference_path: Optional path to the unresolved reference
            reference_target: Optional target of the reference
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
        """
        super().__init__(message, schema_name, schema_version)
        self.reference_path = reference_path
        self.reference_target = reference_target

    def get_context_parts(self) -> list[str]:
        """Add reference details to context."""
        parts = super().get_context_parts()

        if self.reference_path:
            parts.append(f"Reference: {self.reference_path}")

        if self.reference_target:
            parts.append(f"Target: {self.reference_target}")

        return parts


class CweSchemaCircularReferenceError(CweSchemaValidationError):
    """CWE schema contains circular references."""

    __slots__ = ("reference_chain",)

    def __init__(
        self,
        message: str,
        reference_chain: list[str] | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
    ):
        """Initialize CWE schema circular reference error.

        Args:
            message: The circular reference error message
            reference_chain: Optional chain of references that form the cycle
            schema_name: Optional name of the schema
            schema_version: Optional version of the schema
        """
        super().__init__(message, schema_name, schema_version)
        self.reference_chain = reference_chain or []

    def get_context_parts(self) -> list[str]:
        """Add circular reference details to context."""
        parts = super().get_context_parts()

        if self.reference_chain:
            chain = " → ".join(self.reference_chain)
            parts.append(f"Chain: {chain}")

        return parts
