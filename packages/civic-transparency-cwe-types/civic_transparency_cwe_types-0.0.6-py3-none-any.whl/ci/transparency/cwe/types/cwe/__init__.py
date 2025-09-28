"""CWE operations and validation.

Toolkit for CWE operations including loading, validation, relationship
analysis, and schema operations. Handles CWE-specific requirements including
duplicate detection, relationship consistency, and schema compatibility checking.

Core result types:
    - CweLoadingResult: CWE definition loading with duplicate detection
    - CweValidationResult: CWE validation with field checks
    - CweRelationshipResult: CWE relationship validation and analysis

Error types:
    - CweError: Base CWE error with CWE ID context
    - CweLoadingError: CWE loading/parsing failures
    - CweValidationError: CWE validation failures
    - CweRelationshipError: CWE relationship validation failures

Key operations:
    - add_cwe: Add successfully loaded CWE definition
    - validate_cwe: Validate CWE data with field validation
    - analyze_relationships: Analyze CWE relationships for consistency
    - batch_validate_cwes: Validate multiple CWEs efficiently

Example usage:
    from ci.transparency.cwe.types.cwe import (
        CweLoadingResult, CweValidationError, add_cwe
    )

    result = CweLoadingResult()

    try:
        result = add_cwe(result, "CWE-79", cwe_data, file_path=path)
        validation_result = validate_cwe(CweValidationResult(), "CWE-79", cwe_data)
    except CweValidationError as e:
        # Rich context: "Validation failed | CWE: CWE-79 | Field: name"
        logger.error(f"CWE validation error: {e}")

    # Analyze relationships
    rel_result = analyze_relationships(CweRelationshipResult(), result.cwes)
    if rel_result.has_circular_dependencies:
        logger.warning("Circular dependencies detected")
"""

from .errors import (
    CweCircularRelationshipError,
    CweConfigurationError,
    CweConstraintViolationError,
    CweDuplicateError,
    # Base CWE error
    CweError,
    CweFieldValidationError,
    CweFileNotFoundError,
    CweIntegrityError,
    CweInvalidFormatError,
    CweInvalidReferenceError,
    # CWE loading error types
    CweLoadingError,
    CweMissingFieldError,
    CweOrphanedError,
    CweParsingError,
    # CWE processing and system errors
    CweProcessingError,
    # CWE relationship error types
    CweRelationshipError,
    CweSchemaValidationError,
    # CWE validation error types
    CweValidationError,
)
from .results import (
    # Result types
    CweLoadingResult,
    CweRelationshipResult,
    CweValidationResult,
    # CWE loading operations
    add_cwe,
    add_relationship,
    # CWE relationship operations
    analyze_relationships,
    batch_validate_cwes,
    # Analysis and reporting functions
    get_cwe_loading_summary,
    get_cwe_validation_summary,
    # CWE-specific analysis functions
    get_relationship_summary,
    track_duplicate_cwe,
    track_invalid_file,
    track_skipped_cwe_file,
    # CWE validation operations
    validate_cwe,
    validate_cwe_field,
)

__all__ = [
    # Result types
    "CweLoadingResult",
    "CweValidationResult",
    "CweRelationshipResult",
    # CWE loading operations
    "add_cwe",
    "track_duplicate_cwe",
    "track_invalid_file",
    "track_skipped_cwe_file",
    # CWE validation operations
    "validate_cwe",
    "validate_cwe_field",
    "batch_validate_cwes",
    # CWE relationship operations
    "analyze_relationships",
    "add_relationship",
    # Analysis and reporting functions
    "get_cwe_loading_summary",
    "get_cwe_validation_summary",
    "get_relationship_summary",
    # Base CWE error
    "CweError",
    # CWE loading error types
    "CweLoadingError",
    "CweFileNotFoundError",
    "CweParsingError",
    "CweDuplicateError",
    "CweInvalidFormatError",
    "CweMissingFieldError",
    # CWE validation error types
    "CweValidationError",
    "CweFieldValidationError",
    "CweSchemaValidationError",
    "CweConstraintViolationError",
    # CWE relationship error types
    "CweRelationshipError",
    "CweCircularRelationshipError",
    "CweOrphanedError",
    "CweInvalidReferenceError",
    # CWE processing and system errors
    "CweProcessingError",
    "CweIntegrityError",
    "CweConfigurationError",
]
