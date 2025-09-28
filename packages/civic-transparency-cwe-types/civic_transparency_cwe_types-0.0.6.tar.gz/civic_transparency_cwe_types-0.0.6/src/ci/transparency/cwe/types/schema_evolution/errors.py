"""Schema evolution (freeze/compatibility) error types with rich context.

Domain-neutral error hierarchy for comparing schemas across versions.
Extends base validation error types to provide evolution-specific context
like old/new versions, violated rules, affected fields, and compatibility
assessment details.

Design principles:
    - Inherits consistent formatting from base error types
    - Adds evolution-specific context (versions, rules, affected paths)
    - Provides specific exception types for different evolution scenarios
    - Maintains minimal memory overhead with __slots__

Core schema evolution errors:
    - SchemaFreezeError: Base evolution error with version/rule context
    - SchemaFreezeViolationError: Rule violation detected during comparison
    - SchemaCompatibilityError: Backward-compatibility check failed
    - SchemaBreakingChangeError: Breaking change identified

Typical usage:
    from ci.transparency.cwe.types.schema_evolution.errors import SchemaCompatibilityError

    try:
        compare_schemas(old_schema, new_schema)
    except SchemaCompatibilityError as e:
        # Example: "Versions: 2.0 → 2.1 | Issue: enum narrowed | Backward Compatible: No"
        logger.error(f"Schema compatibility failed: {e}")
"""

from ci.transparency.cwe.types.base.errors import BaseValidationError


class SchemaFreezeError(BaseValidationError):
    """Base schema evolution error comparing old vs new versions."""

    __slots__ = ("old_version", "new_version", "freeze_rule")

    def __init__(
        self,
        message: str,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
        validation_context: str | None = None,
    ):
        """Initialize schema evolution error with optional version/rule context.

        Args:
            message: The error message
            old_version: Optional old schema version identifier
            new_version: Optional new schema version identifier
            freeze_rule: Optional name of the freeze/compatibility rule
            validation_context: Optional validation context (scope/category)
        """
        super().__init__(message, validation_context)
        self.old_version = old_version
        self.new_version = new_version
        self.freeze_rule = freeze_rule

    def get_context_parts(self) -> list[str]:
        """Add version/rule context to error message."""
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


class SchemaFreezeViolationError(SchemaFreezeError):
    """Schema freeze rule violation detected (may or may not be breaking)."""

    __slots__ = ("violation_type", "affected_fields")

    def __init__(
        self,
        message: str,
        violation_type: str | None = None,
        affected_fields: list[str] | None = None,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
        validation_context: str | None = None,
    ):
        """Initialize freeze violation with optional type/affected fields.

        Args:
            message: The violation message
            violation_type: Optional violation type (e.g., "enum_narrowed")
            affected_fields: Optional list of affected field paths
            old_version: Optional old schema version identifier
            new_version: Optional new schema version identifier
            freeze_rule: Optional name of the violated rule
            validation_context: Optional validation context (scope/category)
        """
        super().__init__(message, old_version, new_version, freeze_rule, validation_context)
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


class SchemaCompatibilityError(SchemaFreezeError):
    """Backward-compatibility check failed."""

    __slots__ = ("compatibility_issue", "backward_compatible")

    def __init__(
        self,
        message: str,
        compatibility_issue: str | None = None,
        backward_compatible: bool = False,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
        validation_context: str | None = None,
    ):
        """Initialize compatibility error with optional issue/flag.

        Args:
            message: The compatibility error message
            compatibility_issue: Optional description of the issue
            backward_compatible: Whether the change is backward compatible
            old_version: Optional old schema version identifier
            new_version: Optional new schema version identifier
            freeze_rule: Optional name of the related rule
            validation_context: Optional validation context (scope/category)
        """
        super().__init__(message, old_version, new_version, freeze_rule, validation_context)
        self.compatibility_issue = compatibility_issue
        self.backward_compatible = backward_compatible

    def get_context_parts(self) -> list[str]:
        """Add compatibility details to context."""
        parts = super().get_context_parts()

        if self.compatibility_issue:
            parts.append(f"Issue: {self.compatibility_issue}")

        parts.append(f"Backward Compatible: {'Yes' if self.backward_compatible else 'No'}")

        return parts


class SchemaBreakingChangeError(SchemaFreezeError):
    """Breaking change detected between schema versions."""

    __slots__ = ("change_type", "change_description", "impact_level")

    def __init__(
        self,
        message: str,
        change_type: str | None = None,
        change_description: str | None = None,
        impact_level: str | None = None,
        old_version: str | None = None,
        new_version: str | None = None,
        freeze_rule: str | None = None,
        validation_context: str | None = None,
    ):
        """Initialize breaking change with optional type/impact/details.

        Args:
            message: The breaking change message
            change_type: Optional type (e.g., "field_removed", "type_changed")
            change_description: Optional description of the change
            impact_level: Optional impact level (e.g., "high", "medium", "low")
            old_version: Optional old schema version identifier
            new_version: Optional new schema version identifier
            freeze_rule: Optional name of the related rule
            validation_context: Optional validation context (scope/category)
        """
        super().__init__(message, old_version, new_version, freeze_rule, validation_context)
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


# Public API (alphabetical)
__all__ = [
    "SchemaBreakingChangeError",
    "SchemaCompatibilityError",
    "SchemaFreezeError",
    "SchemaFreezeViolationError",
]
