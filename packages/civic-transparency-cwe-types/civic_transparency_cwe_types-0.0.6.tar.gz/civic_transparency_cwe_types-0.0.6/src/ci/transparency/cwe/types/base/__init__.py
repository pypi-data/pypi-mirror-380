"""Foundation types for transparency operations.

Base result types and error classes that provide the foundation for all
domain-specific operations. Use these when building new domain types
or when you need the core functionality without domain-specific features.

Core result types:
    - BaseResult: Abstract base for all operation results
    - BaseLoadingResult: Base for loading operations (tracks loaded/failed counts)
    - BaseValidationResult: Base for validation operations (tracks passed/failed counts)

Core error types:
    - BaseTransparencyError: Abstract base for all transparency errors
    - BaseLoadingError: Base for loading errors (includes file path context)
    - BaseValidationError: Base for validation errors (includes validation context)

Essential helpers:
    - Message helpers: add_error, add_warning, add_info
    - Count helpers: record_loaded, record_failed, record_passed
    - Merge helpers: merge_results, merge_loading, merge_validation

Example usage:
    from ci.transparency.cwe.types.base import BaseResult, add_error

    class MyResult(BaseResult):
        @property
        def success_rate(self) -> float:
            return 1.0 if not self.errors else 0.0

    result = MyResult.ok()
    result = add_error(result, "Something failed")
"""

# Import everything from the implementation files
from .errors import (
    BaseLoadingError,
    # Base error types
    BaseTransparencyError,
    BaseValidationError,
    ConfigurationError,
    # Common error types (renamed to avoid builtin shadowing)
    LoadingFileNotFoundError,
    LoadingParsingError,
    LoadingValidationError,
    TransparencyTimeoutError,
)
from .results import (
    BaseLoadingResult,
    # Base result types
    BaseResult,
    BaseValidationResult,
    add_counts,
    # Message helpers
    add_error,
    add_info,
    add_validation_counts,
    add_warning,
    extend_errors,
    extend_infos,
    extend_warnings,
    merge_loading,
    merge_many,
    merge_many_loading,
    merge_many_validation,
    merge_results,
    merge_validation,
    process_validation_batch,
    record_exception,
    record_fail,
    record_failed,
    record_failure,
    # Loading helpers
    record_loaded,
    record_pass,
    # Validation helpers
    record_passed,
    record_skip,
    record_success,
    record_validation_error,
    record_validation_warning,
    with_exception,
)

__all__ = [
    # Base result types
    "BaseResult",
    "BaseLoadingResult",
    "BaseValidationResult",
    # Base error types
    "BaseTransparencyError",
    "BaseLoadingError",
    "BaseValidationError",
    # Message helpers
    "add_error",
    "add_warning",
    "add_info",
    "extend_errors",
    "extend_warnings",
    "extend_infos",
    "with_exception",
    "merge_results",
    "merge_many",
    # Loading helpers
    "record_loaded",
    "record_failed",
    "add_counts",
    "record_exception",
    "record_skip",
    "record_success",
    "record_failure",
    "merge_loading",
    "merge_many_loading",
    # Validation helpers
    "record_passed",
    "add_validation_counts",
    "record_validation_error",
    "record_validation_warning",
    "process_validation_batch",
    "record_pass",
    "record_fail",
    "merge_validation",
    "merge_many_validation",
    # Common error types (renamed to avoid builtin shadowing)
    "LoadingFileNotFoundError",
    "LoadingParsingError",
    "LoadingValidationError",
    "ConfigurationError",
    "TransparencyTimeoutError",
]
