"""Public API for CWE schema operations.

This package provides:
    • High-level result types for loading and validating CWE JSON schemas.
    • Rich error hierarchy for CWE-specific schema failures.
    • Functional helpers to load schemas and validate CWE data.

Import from here for stable, top-level access to all CWE schema capabilities:

    from ci.transparency.cwe.types.cwe.schema import (
        CweSchemaLoadingResult,
        CweSchemaValidationResult,
        CweSchemaError,
        CweSchemaLoadingError,
        CweSchemaValidationError,
        ...
    )
"""

from ci.transparency.cwe.types.cwe.schema.errors import (
    CweSchemaCircularReferenceError,
    CweSchemaConstraintError,
    CweSchemaDataValidationError,
    CweSchemaError,
    CweSchemaFieldValidationError,
    CweSchemaFormatError,
    CweSchemaLoadingError,
    CweSchemaNotFoundError,
    CweSchemaParsingError,
    CweSchemaReferenceError,
    CweSchemaValidationError,
    CweSchemaVersionError,
)
from ci.transparency.cwe.types.cwe.schema.results import (
    CweSchemaLoadingResult,
    CweSchemaValidationResult,
)

__all__ = [
    # Result types
    "CweSchemaLoadingResult",
    "CweSchemaValidationResult",
    # Base error and categories
    "CweSchemaError",
    "CweSchemaLoadingError",
    "CweSchemaValidationError",
    # Loading errors
    "CweSchemaNotFoundError",
    "CweSchemaParsingError",
    "CweSchemaVersionError",
    "CweSchemaFormatError",
    # Validation errors
    "CweSchemaDataValidationError",
    "CweSchemaFieldValidationError",
    "CweSchemaConstraintError",
    "CweSchemaReferenceError",
    "CweSchemaCircularReferenceError",
]
