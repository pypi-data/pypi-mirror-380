"""Base result types and helpers for transparency operations.

This module contains all foundational result types and their functional helpers.
Combines BaseResult, BaseLoadingResult, and BaseValidationResult with their
combined set of immutable operations.

Core types:
    - BaseResult: Abstract base for all operation results
    - BaseLoadingResult: Base for loading operations (loaded/failed tracking)
    - BaseValidationResult: Base for validation operations (passed/failed tracking)

All helpers follow functional, immutable patterns with type preservation.
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass, replace
from typing import Any, Self, TypeVar

# Type variables for conversion methods
T = TypeVar("T", bound="BaseLoadingResult")
V = TypeVar("V", bound="BaseValidationResult")


# ============================================================================
# BaseResult - Foundation for all result types
# ============================================================================


@dataclass(frozen=True, slots=True)
class BaseResult(ABC):
    """Immutable base result for operations.

    All operations return results that track errors, warnings, and informational
    messages. Results are immutable and provide boolean properties for easy
    condition checking.

    Notes:
        - total_issues = errors + warnings (infos excluded)
        - Truthiness: bool(result) is True iff no errors
    """

    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    infos: tuple[str, ...] = ()

    # ---- Boolean properties for easy condition checking ----

    @property
    def has_errors(self) -> bool:
        """True if any errors are present."""
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        """True if any warnings are present."""
        return bool(self.warnings)

    @property
    def has_infos(self) -> bool:
        """True if any informational messages are present."""
        return bool(self.infos)

    @property
    def success(self) -> bool:
        """True if no errors occurred."""
        return not self.has_errors

    # ---- Abstract property for domain-specific success metrics ----

    @property
    @abstractmethod
    def success_rate(self) -> float:
        """Ratio in [0, 1] indicating operation success.

        Defined by subclasses based on their specific success criteria.
        For example, loading operations might use loaded/(loaded+failed),
        while validation operations might use passed/(passed+failed).
        """

    # ---- Message counts for reporting and analysis ----

    @property
    def error_count(self) -> int:
        """Number of error messages."""
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        """Number of warning messages."""
        return len(self.warnings)

    @property
    def info_count(self) -> int:
        """Number of informational messages."""
        return len(self.infos)

    @property
    def total_issues(self) -> int:
        """Total number of issues (errors + warnings).

        Note: Informational messages are not considered issues.
        """
        return self.error_count + self.warning_count

    @property
    def total_messages(self) -> int:
        """Total number of all messages (errors + warnings + infos)."""
        return self.error_count + self.warning_count + self.info_count

    # ---- Construction ----

    @classmethod
    def ok(cls) -> Self:
        """Return a successful result with no messages."""
        return cls()

    @classmethod
    def from_exception(cls, exc: Exception, context: str = "") -> Self:
        """Create a result from an exception.

        Args:
            exc: The exception to convert to a result
            context: Optional context string (e.g., "File processing")

        Returns:
            New result with the exception recorded as an error
        """
        error_msg = f"{context}: {exc}" if context else str(exc)
        return cls(errors=(error_msg,))

    # ---- Truthiness based on success ----

    def __bool__(self) -> bool:
        """Truthiness reflects success (True iff no errors)."""
        return self.success


# ============================================================================
# BaseLoadingResult - Foundation for loading operations
# ============================================================================


@dataclass(frozen=True, slots=True)
class BaseLoadingResult(BaseResult):
    """Base result for all loading operations.

    Tracks counts of successfully loaded items versus failed attempts.
    Provides conversion methods for creating domain-specific result types
    from generic loading results.
    """

    loaded: int = 0
    failed: int = 0
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    infos: tuple[str, ...] = ()

    # ---- Derived metrics ----

    @property
    def total_processed(self) -> int:
        """Total number of items processed (loaded + failed)."""
        return self.loaded + self.failed

    @property
    def has_attempts(self) -> bool:
        """True if any loading attempts were made."""
        return self.total_processed > 0

    @property
    def success_rate(self) -> float:
        """Ratio of successful loads to total attempts.

        Returns:
            Float in [0, 1]. With zero attempts, returns 1.0 (vacuous success).
        """
        total = self.total_processed
        return self.loaded / total if total else 1.0

    @property
    def failure_rate(self) -> float:
        """Ratio of failed loads to total attempts.

        Returns:
            Float in [0, 1]. With zero attempts, returns 0.0 (vacuous success).
        """
        total = self.total_processed
        return self.failed / total if total else 0.0

    # ---- Construction and validation ----

    @classmethod
    def from_counts(cls, loaded: int = 0, failed: int = 0) -> Self:
        """Create a result from explicit counts.

        Args:
            loaded: Number of successfully loaded items
            failed: Number of failed loading attempts

        Returns:
            New loading result with the specified counts

        Raises:
            ValueError: If either count is negative
        """
        if loaded < 0 or failed < 0:
            raise ValueError("Counts must be non-negative")
        return cls(loaded=loaded, failed=failed)

    @classmethod
    def from_result(cls: type[T], base: "BaseLoadingResult", **extra_fields: Any) -> T:
        """Convert any BaseLoadingResult to a specific subtype.

        This is the general conversion protocol that all domain-specific
        loading results can use to convert from generic batch results
        to their specialized types.

        Args:
            base: The base loading result to convert from
            **extra_fields: Additional fields specific to the target type

        Returns:
            New instance of the target type with base fields copied

        Example:
            batch_result = BatchResult()
            cwe_result = CweLoadingResult.from_result(
                batch_result,
                cwes=batch_result.mappings,
                duplicate_ids=()
            )
        """
        return cls(
            # Copy all BaseResult fields
            errors=base.errors,
            warnings=base.warnings,
            infos=base.infos,
            # Copy all BaseLoadingResult fields
            loaded=base.loaded,
            failed=base.failed,
            # Add any extra fields passed by the subclass
            **extra_fields,
        )

    def to_subtype(self, target_class: type[T], **extra_fields: Any) -> T:
        """Convert this result to a specific subtype.

        Args:
            target_class: The target result type
            **extra_fields: Additional fields for the target type

        Returns:
            New instance of target_class with this result's data
        """
        return target_class.from_result(self, **extra_fields)

    def __post_init__(self) -> None:
        """Validate that counts are non-negative after initialization."""
        if self.loaded < 0 or self.failed < 0:
            raise ValueError("Counts must be non-negative")


# ============================================================================
# BaseValidationResult - Foundation for validation operations
# ============================================================================


@dataclass(frozen=True, slots=True)
class BaseValidationResult(BaseResult):
    """Base result for all validation operations.

    Tracks counts of validation passes versus failures. Provides conversion
    methods for creating domain-specific validation result types from
    generic validation results.
    """

    passed: int = 0
    failed: int = 0

    # ---- Derived metrics ----

    @property
    def total_processed(self) -> int:
        """Total number of items validated (passed + failed)."""
        return self.passed + self.failed

    @property
    def has_validations(self) -> bool:
        """True if any validation attempts were made."""
        return self.total_processed > 0

    @property
    def success_rate(self) -> float:
        """Ratio of validation passes to total validations.

        Returns:
            Float in [0, 1]. With zero validations, returns 1.0 (vacuous success).
        """
        total = self.total_processed
        return self.passed / total if total else 1.0

    @property
    def pass_rate(self) -> float:
        """Alias for success_rate - ratio of passed validations.

        Returns:
            Float in [0, 1]. Identical to success_rate.
        """
        return self.success_rate

    @property
    def failure_rate(self) -> float:
        """Ratio of validation failures to total validations.

        Returns:
            Float in [0, 1]. With zero validations, returns 0.0 (vacuous success).
        """
        total = self.total_processed
        return self.failed / total if total else 0.0

    # ---- Construction and conversion ----

    @classmethod
    def from_counts(cls, passed: int = 0, failed: int = 0) -> Self:
        """Create a result from explicit counts.

        Args:
            passed: Number of validations that passed
            failed: Number of validations that failed

        Returns:
            New validation result with the specified counts

        Raises:
            ValueError: If either count is negative
        """
        if passed < 0 or failed < 0:
            raise ValueError("Counts must be non-negative")
        return cls(passed=passed, failed=failed)

    @classmethod
    def from_bools(cls, outcomes: Sequence[bool]) -> Self:
        """Create a result from a sequence of boolean validation outcomes.

        Args:
            outcomes: Sequence of validation results (True=passed, False=failed)

        Returns:
            New validation result with counts derived from the boolean outcomes

        Example:
            results = [True, True, False, True]
            validation_result = BaseValidationResult.from_bools(results)
            # validation_result.passed == 3, validation_result.failed == 1
        """
        passed = sum(outcomes)  # Efficient counting of True values
        failed = len(outcomes) - passed
        return cls(passed=passed, failed=failed)

    @classmethod
    def from_result(cls: type[V], base: "BaseValidationResult", **extra_fields: Any) -> V:
        """Convert any BaseValidationResult to a specific subtype.

        This is the general conversion protocol that all domain-specific
        validation results can use to convert from generic validation results
        to their specialized types.

        Args:
            base: The base validation result to convert from
            **extra_fields: Additional fields specific to the target type

        Returns:
            New instance of the target type with base fields copied

        Example:
            generic_result = BaseValidationResult(passed=5, failed=2)
            cwe_result = CweValidationResult.from_result(
                generic_result,
                invalid_relationships=(),
                schema_errors=()
            )
        """
        return cls(
            # Copy all BaseResult fields
            errors=base.errors,
            warnings=base.warnings,
            infos=base.infos,
            # Copy all BaseValidationResult fields
            passed=base.passed,
            failed=base.failed,
            # Add any extra fields passed by the subclass
            **extra_fields,
        )

    def to_subtype(self, target_class: type[V], **extra_fields: Any) -> V:
        """Convert this result to a specific subtype.

        Args:
            target_class: The target result type
            **extra_fields: Additional fields for the target type

        Returns:
            New instance of target_class with this result's data
        """
        return target_class.from_result(self, **extra_fields)

    def __post_init__(self) -> None:
        """Validate that counts are non-negative after initialization."""
        if self.passed < 0 or self.failed < 0:
            raise ValueError("Counts must be non-negative")


# ============================================================================
# Message manipulation helpers (for BaseResult)
# ============================================================================


def add_error[R: BaseResult](result: R, error: str) -> R:
    """Return a copy of result with error appended.

    Args:
        result: The result to add an error to
        error: The error message to append

    Returns:
        New result with error appended to errors tuple
    """
    return replace(result, errors=result.errors + (error,))


def add_warning[R: BaseResult](result: R, warning: str) -> R:
    """Return a copy of result with warning appended.

    Args:
        result: The result to add a warning to
        warning: The warning message to append

    Returns:
        New result with warning appended to warnings tuple
    """
    return replace(result, warnings=result.warnings + (warning,))


def add_info[R: BaseResult](result: R, info: str) -> R:
    """Return a copy of result with info appended.

    Args:
        result: The result to add an info message to
        info: The informational message to append

    Returns:
        New result with info appended to infos tuple
    """
    return replace(result, infos=result.infos + (info,))


def extend_errors[R: BaseResult](result: R, *errors: str) -> R:
    """Return a copy with all errors appended.

    Args:
        result: The result to extend
        *errors: Variable number of error messages to append

    Returns:
        New result with all error messages appended
    """
    return replace(result, errors=result.errors + tuple(errors))


def extend_warnings[R: BaseResult](result: R, *warnings: str) -> R:
    """Return a copy with all warnings appended.

    Args:
        result: The result to extend
        *warnings: Variable number of warning messages to append

    Returns:
        New result with all warning messages appended
    """
    return replace(result, warnings=result.warnings + tuple(warnings))


def extend_infos[R: BaseResult](result: R, *infos: str) -> R:
    """Return a copy with all infos appended.

    Args:
        result: The result to extend
        *infos: Variable number of info messages to append

    Returns:
        New result with all info messages appended
    """
    return replace(result, infos=result.infos + tuple(infos))


def with_exception[R: BaseResult](result: R, exc: Exception, context: str = "") -> R:
    """Return a copy with exception added as error.

    Args:
        result: The result to add exception to
        exc: The exception to record
        context: Optional context string for the error

    Returns:
        New result with exception recorded as an error message
    """
    error_msg = f"{context}: {exc}" if context else str(exc)
    return add_error(result, error_msg)


def merge_results[R: BaseResult](r1: R, r2: R) -> R:
    """Return r1 with all messages merged from r2.

    Args:
        r1: The primary result (type is preserved)
        r2: The result to merge messages from

    Returns:
        New result of r1's type with messages from both results
    """
    return replace(
        r1,
        errors=r1.errors + r2.errors,
        warnings=r1.warnings + r2.warnings,
        infos=r1.infos + r2.infos,
    )


def merge_many[R: BaseResult](first: R, *rest: R) -> R:
    """Merge multiple results into one.

    Args:
        first: The first result (determines return type)
        *rest: Additional results to merge

    Returns:
        Single result of first's type with all messages merged
    """
    result = first
    for r in rest:
        result = merge_results(result, r)
    return result


# ============================================================================
# Loading operation helpers (for BaseLoadingResult)
# ============================================================================


def record_loaded[R: BaseLoadingResult](result: R) -> R:
    """Record a successful load by incrementing the loaded count.

    Args:
        result: The loading result to update

    Returns:
        New result with loaded count incremented by 1
    """
    return replace(result, loaded=result.loaded + 1)


def record_failed[R: BaseLoadingResult](result: R) -> R:
    """Record a failed load by incrementing the failed count.

    Args:
        result: The loading result to update

    Returns:
        New result with failed count incremented by 1
    """
    return replace(result, failed=result.failed + 1)


def add_counts[R: BaseLoadingResult](result: R, loaded: int, failed: int) -> R:
    """Add multiple counts to the result.

    Args:
        result: The loading result to update
        loaded: Number of successful loads to add
        failed: Number of failed loads to add

    Returns:
        New result with counts increased by the specified amounts

    Raises:
        ValueError: If either count is negative
    """
    if loaded < 0 or failed < 0:
        raise ValueError("Counts must be non-negative")
    return replace(
        result,
        loaded=result.loaded + loaded,
        failed=result.failed + failed,
    )


def record_exception[R: BaseLoadingResult](result: R, exc: Exception, context: str = "") -> R:
    """Record an exception as an error and increment failed count.

    Args:
        result: The loading result to update
        exc: The exception to record
        context: Optional context string (e.g., file path)

    Returns:
        New result with exception recorded as error and failed count incremented
    """
    error_msg = f"{context}: {exc}" if context else str(exc)
    result = add_error(result, error_msg)
    return record_failed(result)


def record_skip[R: BaseLoadingResult](result: R, reason: str) -> R:
    """Record a skip with warning and increment failed count.

    Args:
        result: The loading result to update
        reason: Reason for skipping (recorded as warning)

    Returns:
        New result with warning added and failed count incremented
    """
    result = add_warning(result, reason)
    return record_failed(result)


def record_success[R: BaseLoadingResult](result: R) -> R:
    """Alias for record_loaded - records a successful operation.

    Args:
        result: The loading result to update

    Returns:
        New result with loaded count incremented
    """
    return record_loaded(result)


def record_failure[R: BaseLoadingResult](result: R, reason: str = "") -> R:
    """Record a failure with optional reason.

    Args:
        result: The loading result to update
        reason: Optional reason for failure (recorded as error if provided)

    Returns:
        New result with failed count incremented and optional error message
    """
    if reason:
        result = add_error(result, reason)
    return record_failed(result)


def merge_loading[R: BaseLoadingResult](a: R, b: R) -> R:
    """Merge two loading results of the same type.

    Combines counts and messages from both results while preserving
    the concrete type of the first result.

    Args:
        a: The primary result (type is preserved)
        b: The result to merge from

    Returns:
        New result of type R with combined counts and messages
    """
    merged_msgs = merge_results(a, b)  # Handles errors/warnings/infos
    return replace(
        merged_msgs,
        loaded=a.loaded + b.loaded,
        failed=a.failed + b.failed,
    )


def merge_many_loading[R: BaseLoadingResult](first: R, *rest: R) -> R:
    """Merge multiple loading results into one.

    Args:
        first: The first result (determines return type)
        *rest: Additional results to merge

    Returns:
        Single result of first's type with all counts and messages combined
    """
    result = first
    for r in rest:
        result = merge_loading(result, r)
    return result


# ============================================================================
# Validation operation helpers (for BaseValidationResult)
# ============================================================================


def record_passed[R: BaseValidationResult](result: R) -> R:
    """Record a validation pass by incrementing the passed count.

    Args:
        result: The validation result to update

    Returns:
        New result with passed count incremented by 1
    """
    return replace(result, passed=result.passed + 1)


def record_validation_failed[R: BaseValidationResult](result: R) -> R:
    """Record a validation failure by incrementing the failed count.

    Args:
        result: The validation result to update

    Returns:
        New result with failed count incremented by 1
    """
    return replace(result, failed=result.failed + 1)


def add_validation_counts[R: BaseValidationResult](result: R, passed: int, failed: int) -> R:
    """Add multiple validation counts to the result.

    Args:
        result: The validation result to update
        passed: Number of validation passes to add
        failed: Number of validation failures to add

    Returns:
        New result with counts increased by the specified amounts

    Raises:
        ValueError: If either count is negative
    """
    if passed < 0 or failed < 0:
        raise ValueError("Counts must be non-negative")
    return replace(
        result,
        passed=result.passed + passed,
        failed=result.failed + failed,
    )


def record_validation_error[R: BaseValidationResult](
    result: R, error_msg: str, increment_failed: bool = True
) -> R:
    """Record a validation error with optional failure count increment.

    Args:
        result: The validation result to update
        error_msg: The validation error message
        increment_failed: Whether to increment the failed count (default: True)

    Returns:
        New result with error recorded and optionally failed count incremented
    """
    result = add_error(result, error_msg)
    if increment_failed:
        result = record_validation_failed(result)
    return result


def record_validation_warning[R: BaseValidationResult](
    result: R, warning_msg: str, increment_failed: bool = False
) -> R:
    """Record a validation warning with optional failure count increment.

    Args:
        result: The validation result to update
        warning_msg: The validation warning message
        increment_failed: Whether to increment the failed count (default: False)

    Returns:
        New result with warning recorded and optionally failed count incremented
    """
    result = add_warning(result, warning_msg)
    if increment_failed:
        result = record_validation_failed(result)
    return result


def process_validation_batch[R: BaseValidationResult](result: R, outcomes: Sequence[bool]) -> R:
    """Process a batch of validation outcomes.

    Args:
        result: The validation result to update
        outcomes: Sequence of validation results (True=passed, False=failed)

    Returns:
        New result with counts updated based on the outcomes
    """
    passed_count = sum(outcomes)
    failed_count = len(outcomes) - passed_count
    return add_validation_counts(result, passed_count, failed_count)


def record_pass[R: BaseValidationResult](result: R) -> R:
    """Alias for record_passed - records a validation success.

    Args:
        result: The validation result to update

    Returns:
        New result with passed count incremented
    """
    return record_passed(result)


def record_fail[R: BaseValidationResult](result: R) -> R:
    """Alias for record_validation_failed - records a validation failure.

    Args:
        result: The validation result to update

    Returns:
        New result with failed count incremented
    """
    return record_validation_failed(result)


def merge_validation[R: BaseValidationResult](a: R, b: R) -> R:
    """Merge two validation results of the same type.

    Combines counts and messages from both results while preserving
    the concrete type of the first result.

    Args:
        a: The primary result (type is preserved)
        b: The result to merge from

    Returns:
        New result of type R with combined counts and messages
    """
    merged_msgs = merge_results(a, b)  # Handles errors/warnings/infos
    return replace(
        merged_msgs,
        passed=a.passed + b.passed,
        failed=a.failed + b.failed,
    )


def merge_many_validation[R: BaseValidationResult](first: R, *rest: R) -> R:
    """Merge multiple validation results into one.

    Args:
        first: The first result (determines return type)
        *rest: Additional results to merge

    Returns:
        Single result of first's type with all counts and messages combined
    """
    result = first
    for r in rest:
        result = merge_validation(result, r)
    return result
