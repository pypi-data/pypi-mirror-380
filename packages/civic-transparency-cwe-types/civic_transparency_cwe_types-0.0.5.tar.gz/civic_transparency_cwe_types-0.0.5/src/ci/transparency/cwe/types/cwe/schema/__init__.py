"""CWE schema operations and validation.

Toolkit for CWE JSON schema operations including schema loading,
CWE data validation against schemas, freeze detection, and schema versioning.
Handles CWE-specific schema requirements and compatibility checking.

Core result types:
    - CweSchemaLoadingResult: CWE schema file loading with version tracking
    - CweSchemaValidationResult: CWE data validation against schemas
    - CweSchemaFreezeResult: CWE schema freeze detection and compatibility analysis

Error types (with CWE schema context):
    - CweSchemaLoadingError: Base CWE schema error (includes schema name + file path)
    - CweSchemaParsingError: CWE JSON schema parsing error
    - CweSchemaVersionError: CWE schema version compatibility error
    - CweSchemaFreezeError: CWE schema freeze validation error
    - CweSchemaValidationError: CWE data validation against schema failed

Key operations:
    - load_cwe_schema: Load CWE schema with version detection
    - validate_cwe_data: Validate CWE data against schema
    - detect_schema_freeze: Detect schema freeze violations
    - check_schema_compatibility: Check schema version compatibility

Example usage:
    from ci.transparency.cwe.types.cwe.schema import (
        CweSchemaLoadingResult, CweSchemaValidationError, load_cwe_schema
    )

    result = CweSchemaLoadingResult()

    try:
        result = load_cwe_schema(result, "cwe-schema-v2.0", schema_data, file_path=path)
        validation_result = validate_cwe_data(cwe_data, schema_data)
    except CweSchemaValidationError as e:
        # Rich context: "Validation failed | Schema: cwe-v2.0 | Field: relationships[0].id | CWE: CWE-A001"
        logger.error(f"CWE schema error: {e}")

    # Detect breaking changes
    freeze_result = detect_schema_freeze(old_schema, new_schema)
    if freeze_result.has_violations:
        logger.warning("Schema freeze violations detected")
"""

from .errors import (
    CweBreakingChangeError,
    # Schema validation errors
    CweDataValidationError,
    CweFieldValidationError,
    CweFreezeViolationError,
    CweSchemaCompatibilityError,
    CweSchemaConstraintError,
    # Base CWE schema errors
    CweSchemaError,
    CweSchemaFormatError,
    # Schema freeze errors
    CweSchemaFreezeError,
    CweSchemaLoadingError,
    # Schema loading errors
    CweSchemaNotFoundError,
    CweSchemaParsingError,
    CweSchemaValidationError,
    CweSchemaVersionError,
)
from .results import (
    CweSchemaFreezeResult,
    # Result types
    CweSchemaLoadingResult,
    CweSchemaValidationResult,
    add_schema_version,
    analyze_schema_changes,
    batch_validate_cwes,
    check_schema_compatibility,
    # Freeze detection operations
    detect_schema_freeze,
    get_freeze_analysis,
    # Analysis and reporting
    get_schema_loading_summary,
    get_validation_summary,
    # Schema loading operations
    load_cwe_schema,
    track_schema_usage,
    # Schema validation operations
    validate_cwe_data,
    validate_cwe_field,
)

__all__ = [
    # Result types
    "CweSchemaLoadingResult",
    "CweSchemaValidationResult",
    "CweSchemaFreezeResult",
    # Schema loading operations
    "load_cwe_schema",
    "add_schema_version",
    "track_schema_usage",
    # Schema validation operations
    "validate_cwe_data",
    "validate_cwe_field",
    "batch_validate_cwes",
    # Freeze detection operations
    "detect_schema_freeze",
    "check_schema_compatibility",
    "analyze_schema_changes",
    # Analysis and reporting
    "get_schema_loading_summary",
    "get_validation_summary",
    "get_freeze_analysis",
    # Base CWE schema errors
    "CweSchemaError",
    "CweSchemaLoadingError",
    "CweSchemaValidationError",
    # Schema loading errors
    "CweSchemaNotFoundError",
    "CweSchemaParsingError",
    "CweSchemaVersionError",
    "CweSchemaFormatError",
    # Schema validation errors
    "CweDataValidationError",
    "CweFieldValidationError",
    "CweSchemaConstraintError",
    # Schema freeze errors
    "CweSchemaFreezeError",
    "CweFreezeViolationError",
    "CweSchemaCompatibilityError",
    "CweBreakingChangeError",
]
