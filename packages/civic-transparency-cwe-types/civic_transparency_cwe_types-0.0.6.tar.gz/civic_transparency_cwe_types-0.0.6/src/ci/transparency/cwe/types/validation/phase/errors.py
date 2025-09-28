"""Phase validation error types with rich context.

Domain-specific error hierarchy for phase validation operations. Extends base error
types to provide phase-specific context like phase names, validation stages, and
processing statistics.

Design principles:
    - Inherits consistent formatting from base error types
    - Adds phase-specific context (phase names, stages, processing counts)
    - Provides specific exception types for different phase failure scenarios
    - Maintains minimal memory overhead with __slots__

Core phase errors:
    - PhaseError: Base phase error with phase name context
    - PhaseAbortedError: Phase operation was aborted
    - PhaseTimeoutError: Phase operation timed out
    - PhaseResourceError: Phase ran out of resources

Typical usage:
    from ci.transparency.cwe.types.validation.phase import PhaseAbortedError

    try:
        run_validation_phase(phase_config)
    except PhaseAbortedError as e:
        # Rich context: "Phase aborted | Phase: field-validation | Stage: processing | Items: 150/500"
        logger.error(f"Phase validation failed: {e}")
"""

from ci.transparency.cwe.types.base.errors import BaseTransparencyError, BaseValidationError


class PhaseError(BaseValidationError):
    """Base exception for phase validation operations.

    Extends BaseValidationError to add phase-specific context like phase names
    and processing stages.
    """

    __slots__ = ("phase_name", "stage", "items_processed")

    def __init__(
        self,
        message: str,
        phase_name: str | None = None,
        stage: str | None = None,
        items_processed: int | None = None,
        validation_context: str | None = None,
    ):
        """Initialize phase error with phase-specific context.

        Args:
            message: The error message
            phase_name: Optional name of the validation phase
            stage: Optional processing stage (e.g., "setup", "processing", "cleanup")
            items_processed: Optional number of items processed before error
            validation_context: Optional validation context
        """
        super().__init__(message, validation_context)
        self.phase_name = phase_name
        self.stage = stage
        self.items_processed = items_processed

    def get_context_parts(self) -> list[str]:
        """Add phase context to error message."""
        parts = super().get_context_parts()

        # Add phase name first for prominence
        if self.phase_name:
            parts.insert(0, f"Phase: {self.phase_name}")

        if self.stage:
            parts.append(f"Stage: {self.stage}")

        if self.items_processed is not None:
            parts.append(f"Processed: {self.items_processed}")

        return parts


# ============================================================================
# Phase operation error types
# ============================================================================


class PhaseAbortedError(PhaseError):
    """Phase operation was aborted before completion."""

    __slots__ = ("abort_reason", "total_items")

    def __init__(
        self,
        message: str,
        abort_reason: str | None = None,
        phase_name: str | None = None,
        stage: str | None = None,
        items_processed: int | None = None,
        total_items: int | None = None,
    ):
        """Initialize phase aborted error.

        Args:
            message: The abort error message
            abort_reason: Optional reason why the phase was aborted
            phase_name: Optional name of the validation phase
            stage: Optional processing stage where abort occurred
            items_processed: Optional number of items processed before abort
            total_items: Optional total number of items expected
        """
        super().__init__(message, phase_name, stage, items_processed)
        self.abort_reason = abort_reason
        self.total_items = total_items

    def get_context_parts(self) -> list[str]:
        """Add abort context to error message."""
        parts = super().get_context_parts()

        if self.abort_reason:
            parts.append(f"Reason: {self.abort_reason}")

        if self.items_processed is not None and self.total_items is not None:
            # Override the simple "Processed: X" with progress format
            for i, part in enumerate(parts):
                if part.startswith("Processed: "):
                    parts[i] = f"Progress: {self.items_processed}/{self.total_items}"
                    break

        return parts


class PhaseTimeoutError(PhaseError):
    """Phase operation timed out."""

    __slots__ = ("timeout_seconds", "elapsed_seconds")

    def __init__(
        self,
        message: str,
        timeout_seconds: float | None = None,
        elapsed_seconds: float | None = None,
        phase_name: str | None = None,
        stage: str | None = None,
        items_processed: int | None = None,
    ):
        """Initialize phase timeout error.

        Args:
            message: The timeout error message
            timeout_seconds: Optional timeout limit that was exceeded
            elapsed_seconds: Optional actual time elapsed before timeout
            phase_name: Optional name of the validation phase
            stage: Optional processing stage where timeout occurred
            items_processed: Optional number of items processed before timeout
        """
        super().__init__(message, phase_name, stage, items_processed)
        self.timeout_seconds = timeout_seconds
        self.elapsed_seconds = elapsed_seconds

    def get_context_parts(self) -> list[str]:
        """Add timeout context to error message."""
        parts = super().get_context_parts()

        if self.timeout_seconds:
            parts.append(f"Timeout: {self.timeout_seconds}s")

        if self.elapsed_seconds:
            parts.append(f"Elapsed: {self.elapsed_seconds:.1f}s")

        return parts


class PhaseResourceError(PhaseError):
    """Phase operation ran out of system resources."""

    __slots__ = ("resource_type", "limit_reached", "resource_usage")

    def __init__(
        self,
        message: str,
        resource_type: str | None = None,
        limit_reached: str | None = None,
        resource_usage: str | None = None,
        phase_name: str | None = None,
        stage: str | None = None,
        items_processed: int | None = None,
    ):
        """Initialize phase resource error.

        Args:
            message: The resource error message
            resource_type: Optional type of resource (e.g., "memory", "disk", "threads")
            limit_reached: Optional description of the limit that was reached
            resource_usage: Optional description of current resource usage
            phase_name: Optional name of the validation phase
            stage: Optional processing stage where resource exhaustion occurred
            items_processed: Optional number of items processed before exhaustion
        """
        super().__init__(message, phase_name, stage, items_processed)
        self.resource_type = resource_type
        self.limit_reached = limit_reached
        self.resource_usage = resource_usage

    def get_context_parts(self) -> list[str]:
        """Add resource context to error message."""
        parts = super().get_context_parts()

        if self.resource_type:
            parts.append(f"Resource: {self.resource_type}")

        if self.limit_reached:
            parts.append(f"Limit: {self.limit_reached}")

        if self.resource_usage:
            parts.append(f"Usage: {self.resource_usage}")

        return parts


class PhaseIntegrityError(PhaseError):
    """Phase data integrity violation."""

    __slots__ = ("integrity_check", "expected_value", "actual_value")

    def __init__(
        self,
        message: str,
        integrity_check: str | None = None,
        expected_value: str | None = None,
        actual_value: str | None = None,
        phase_name: str | None = None,
        stage: str | None = None,
    ):
        """Initialize phase integrity error.

        Args:
            message: The integrity error message
            integrity_check: Optional name of the integrity check that failed
            expected_value: Optional expected value
            actual_value: Optional actual value found
            phase_name: Optional name of the validation phase
            stage: Optional processing stage where integrity issue was detected
        """
        super().__init__(message, phase_name, stage)
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


class PhaseConfigurationError(BaseTransparencyError):
    """Phase configuration is invalid or incomplete."""

    __slots__ = ("config_parameter", "config_value", "valid_values", "phase_name")

    def __init__(
        self,
        message: str,
        config_parameter: str | None = None,
        config_value: str | None = None,
        valid_values: list[str] | None = None,
        phase_name: str | None = None,
    ):
        """Initialize phase configuration error.

        Args:
            message: The configuration error message
            config_parameter: Optional name of the invalid configuration parameter
            config_value: Optional value that was provided
            valid_values: Optional list of valid values for the parameter
            phase_name: Optional name of the validation phase
        """
        super().__init__(message)
        self.config_parameter = config_parameter
        self.config_value = config_value
        self.valid_values = valid_values or []
        self.phase_name = phase_name

    def get_context_parts(self) -> list[str]:
        """Add configuration context to error message."""
        parts = super().get_context_parts()

        if self.phase_name:
            parts.insert(0, f"Phase: {self.phase_name}")

        if self.config_parameter:
            parts.append(f"Parameter: {self.config_parameter}")

        if self.config_value:
            parts.append(f"Value: {self.config_value}")

        if self.valid_values:
            valid_str = ", ".join(self.valid_values)
            parts.append(f"Valid: {valid_str}")

        return parts


class PhaseValidationRuleError(PhaseError):
    """Phase validation rule failed."""

    __slots__ = ("rule_name", "rule_type", "field_path", "field_value")

    def __init__(
        self,
        message: str,
        rule_name: str | None = None,
        rule_type: str | None = None,
        field_path: str | None = None,
        field_value: str | None = None,
        phase_name: str | None = None,
        stage: str | None = None,
    ):
        """Initialize phase validation rule error.

        Args:
            message: The validation rule error message
            rule_name: Optional name of the validation rule that failed
            rule_type: Optional type of rule (e.g., "format", "constraint", "reference")
            field_path: Optional path to the field that failed
            field_value: Optional value that failed validation
            phase_name: Optional name of the validation phase
            stage: Optional processing stage where rule failed
        """
        super().__init__(message, phase_name, stage)
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.field_path = field_path
        self.field_value = field_value

    def get_context_parts(self) -> list[str]:
        """Add validation rule details to context."""
        parts = super().get_context_parts()

        if self.rule_name:
            parts.append(f"Rule: {self.rule_name}")

        if self.rule_type:
            parts.append(f"Type: {self.rule_type}")

        if self.field_path:
            parts.append(f"Field: {self.field_path}")

        if self.field_value is not None:
            parts.append(f"Value: {self.field_value}")

        return parts
