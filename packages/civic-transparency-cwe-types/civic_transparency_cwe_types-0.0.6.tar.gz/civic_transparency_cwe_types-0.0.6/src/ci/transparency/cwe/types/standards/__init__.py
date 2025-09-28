"""Standards operations and validation.

Toolkit for standards operations including loading, validation, mapping
analysis, and format operations. Handles standards-specific requirements including
framework detection, control validation, and mapping consistency checking.

Core result types:
    - StandardsLoadingResult: Standards definition loading with framework detection
    - StandardsValidationResult: Standards validation with field and constraint checks
    - StandardsMappingResult: Standards mapping validation and analysis

Error types:
    - StandardsError: Base standards error with standard ID context
    - StandardsLoadingError: Standards loading/parsing failures
    - StandardsValidationError: Standards validation failures
    - StandardsMappingError: Standards mapping validation failures

Key operations:
    - add_standard: Add successfully loaded standards definition
    - validate_standard: Validate standards data with field validation
    - analyze_mappings: Analyze standards mappings for consistency
    - batch_validate_standards: Validate multiple standards efficiently

Example usage:
    from ci.transparency.cwe.types.standards import (
        StandardsLoadingResult, StandardsValidationError, add_standard
    )

    result = StandardsLoadingResult()

    try:
        result = add_standard(result, "NIST-SP-800-53", standards_data, file_path=path)
        validation_result = validate_standard(StandardsValidationResult(), "NIST-SP-800-53", standards_data)
    except StandardsValidationError as e:
        # Rich context: "Validation failed | Standard: NIST-SP-800-53 | Field: controls[0].id"
        logger.error(f"Standards validation error: {e}")

    # Analyze mappings
    mapping_result = analyze_mappings(StandardsMappingResult(), result.standards, valid_cwe_ids)
    if mapping_result.has_invalid_mappings:
        logger.warning("Invalid mappings detected")
"""

from .errors import (
    StandardsConfigurationError,
    StandardsConstraintViolationError,
    StandardsDuplicateMappingError,
    # Base standards error
    StandardsError,
    StandardsFieldValidationError,
    StandardsFileNotFoundError,
    # Standards format and processing error types
    StandardsFormatError,
    StandardsIntegrityError,
    StandardsInvalidFormatError,
    StandardsInvalidMappingError,
    # Standards loading error types
    StandardsLoadingError,
    # Standards mapping error types
    StandardsMappingError,
    StandardsMissingFieldError,
    StandardsParsingError,
    StandardsProcessingError,
    # Standards validation error types
    StandardsValidationError,
)
from .results import (
    # Result types
    StandardsLoadingResult,
    StandardsMappingResult,
    StandardsValidationResult,
    add_mapping,
    # Standards loading operations
    add_standard,
    # Standards mapping operations
    analyze_mappings,
    batch_validate_standards,
    get_control_count,
    get_mapping_coverage,
    get_mapping_summary,
    # Standards-specific analysis functions
    get_standards_by_framework,
    # Analysis and reporting functions
    get_standards_loading_summary,
    get_standards_validation_summary,
    track_duplicate_standard,
    track_invalid_standards_file,
    track_skipped_standards_file,
    # Standards validation operations
    validate_standard,
    validate_standards_field,
)

__all__ = [
    # Result types
    "StandardsLoadingResult",
    "StandardsValidationResult",
    "StandardsMappingResult",
    # Standards loading operations
    "add_standard",
    "track_duplicate_standard",
    "track_invalid_standards_file",
    "track_skipped_standards_file",
    # Standards validation operations
    "validate_standard",
    "validate_standards_field",
    "batch_validate_standards",
    # Standards mapping operations
    "analyze_mappings",
    "add_mapping",
    # Analysis and reporting functions
    "get_standards_loading_summary",
    "get_standards_validation_summary",
    "get_mapping_summary",
    "get_standards_by_framework",
    "get_control_count",
    "get_mapping_coverage",
    # Base standards error
    "StandardsError",
    # Standards loading error types
    "StandardsLoadingError",
    "StandardsFileNotFoundError",
    "StandardsParsingError",
    "StandardsInvalidFormatError",
    "StandardsMissingFieldError",
    # Standards validation error types
    "StandardsValidationError",
    "StandardsFieldValidationError",
    "StandardsConstraintViolationError",
    # Standards mapping error types
    "StandardsMappingError",
    "StandardsInvalidMappingError",
    "StandardsDuplicateMappingError",
    # Standards format and processing error types
    "StandardsFormatError",
    "StandardsConfigurationError",
    "StandardsProcessingError",
    "StandardsIntegrityError",
]
