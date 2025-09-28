"""Schema evolution (freeze/compatibility) types (neutral).

Toolkit of attribute-only types for schema-to-schema comparisons:
freeze rule violations, backward compatibility assessment, and diff/report
structures. Engines/validators provide behavior; these are context carriers.

Core result types:
    - SchemaDiff: Structural summary of added/removed/changed elements
    - SchemaEvolutionReport: Aggregated outcome across checks

Error types:
    - SchemaFreezeError: Base evolution error (versions + rule context)
    - SchemaFreezeViolationError: Freeze rule violation details
    - SchemaCompatibilityError: Backward-compatibility failure
    - SchemaBreakingChangeError: Breaking change identified

Example usage:
    from ci.transparency.cwe.types.schema_evolution import (
        SchemaEvolutionReport, SchemaCompatibilityError
    )
"""

from ci.transparency.cwe.types.schema_evolution.errors import (
    SchemaBreakingChangeError,
    SchemaCompatibilityError,
    # Base & specific evolution errors
    SchemaFreezeError,
    SchemaFreezeViolationError,
)
from ci.transparency.cwe.types.schema_evolution.results import (
    # Result types
    SchemaDiff,
    SchemaEvolutionReport,
)

__all__ = [
    # Result types
    "SchemaDiff",
    "SchemaEvolutionReport",
    # Error types
    "SchemaFreezeError",
    "SchemaFreezeViolationError",
    "SchemaCompatibilityError",
    "SchemaBreakingChangeError",
]
