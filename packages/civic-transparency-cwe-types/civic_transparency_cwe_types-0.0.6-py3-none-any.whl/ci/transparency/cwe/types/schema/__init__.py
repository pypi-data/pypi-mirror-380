"""JSON Schema operations and validation (neutral types).

Toolkit for JSON Schema work including schema loading/parsing and
instance-vs-schema validation. These are attribute-only *types* intended
for use by higher-level engines; no external dependencies.

Core result types:
    - SchemaLoadingResult: Schema file/resource loading with version context
    - SchemaValidationResult: Instance validation against a schema

Error types (with schema context):
    - SchemaError: Base schema error (includes schema name/version and file path)
    - SchemaLoadingError: Generic schema loading failure
    - SchemaNotFoundError: Schema file/resource not found
    - SchemaParsingError: Schema parsing failure (e.g., JSON/YAML)
    - SchemaVersionError: Unsupported/invalid schema version
    - SchemaFormatError: Malformed/invalid schema structure
    - SchemaValidationError: Base instance-vs-schema validation failure
    - SchemaDataValidationError: Value/type/format mismatch at a path
    - SchemaFieldValidationError: Field-level constraint failure
    - SchemaConstraintError: Declarative constraint violation
    - SchemaReferenceError: Unresolvable $ref
    - SchemaCircularReferenceError: Circular reference chain detected

Example usage:
    from ci.transparency.cwe.types.schema import (
        SchemaLoadingResult, SchemaValidationError
    )
"""

# Re-export errors and results as the public package surface.
from ci.transparency.cwe.types.schema.errors import (
    SchemaCircularReferenceError,
    SchemaConstraintError,
    SchemaDataValidationError,
    # Base schema errors
    SchemaError,
    SchemaFieldValidationError,
    SchemaFormatError,
    SchemaLoadingError,
    # Loading/format errors
    SchemaNotFoundError,
    SchemaParsingError,
    # Reference errors
    SchemaReferenceError,
    # Validation errors
    SchemaValidationError,
    SchemaVersionError,
)
from ci.transparency.cwe.types.schema.results import (
    # Result types
    SchemaLoadingResult,
    SchemaValidationResult,
)

__all__ = [
    # Result types
    "SchemaLoadingResult",
    "SchemaValidationResult",
    # Base schema errors
    "SchemaError",
    "SchemaLoadingError",
    # Loading/format errors
    "SchemaNotFoundError",
    "SchemaParsingError",
    "SchemaVersionError",
    "SchemaFormatError",
    # Validation errors
    "SchemaValidationError",
    "SchemaDataValidationError",
    "SchemaFieldValidationError",
    "SchemaConstraintError",
    # Reference errors
    "SchemaReferenceError",
    "SchemaCircularReferenceError",
]
