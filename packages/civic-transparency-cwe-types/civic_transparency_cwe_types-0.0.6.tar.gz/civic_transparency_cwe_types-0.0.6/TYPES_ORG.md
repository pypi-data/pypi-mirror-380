# Organization

```text
ci/transparency/cwe/types/
├── __init__.py            # Main entry point (convenience re-exports)
├── py.typed               # Type marker
├── _version.py            # Version info (SCM-managed)
│
├── base/                  # Foundation types (neutral)
│   ├── __init__.py
│   ├── results.py         # BaseResult + BaseLoadingResult + BaseValidationResult + helpers
│   └── errors.py          # BaseTransparencyError + BaseLoadingError + BaseValidationError
│
├── batch/                 # Batch file processing (neutral)
│   ├── __init__.py
│   ├── results.py         # BatchResult + batch operations results
│   └── errors.py          # BatchError + BatchAbortedError + BatchResourceError + etc.
│
├── schema/                # JSON Schema (instance to schema, neutral)
│   ├── __init__.py
│   ├── results.py         # SchemaLoadingResult + SchemaValidationResult
│   └── errors.py          # SchemaError + SchemaLoadingError + SchemaValidationError + etc.
│
├── schema_evolution/      # Schema to schema (freeze/compat/diff, neutral)
│   ├── __init__.py
│   ├── results.py         # SchemaDiff + SchemaEvolutionReport
│   └── errors.py          # SchemaFreezeError + SchemaCompatibilityError + etc.
│
├── cwe/                   # CWE domain (types only or thin re-exports)
│   ├── __init__.py        # Re-export neutral types under CWE-prefixed names if desired
│   ├── results.py         # CweLoadingResult + CweValidationResult + domain result holders
│   ├── errors.py          # CweError + CweLoadingError + CweValidationError (attributes only)
│   └── schema/            # OPTIONAL: Thin adapters/re-exports of neutral schema types
│       ├── __init__.py
│       ├── results.py     # CweSchemaLoadingResult = SchemaLoadingResult (alias)
│       └── errors.py      # CweSchema*Error = Schema*Error (alias)
│
├── standards/             # Standards domain (types only or thin re-exports)
│   ├── __init__.py
│   ├── results.py         # StandardsLoadingResult + StandardsValidationResult
│   └── errors.py          # StandardsError + StandardsLoadingError + etc.
│
└── validation/            # Validation workflow types (neutral orchestration)
    ├── __init__.py
    └── phase/
        ├── __init__.py
        ├── results.py     # PhaseValidationResult + MultiPhaseValidationResult
        └── errors.py      # PhaseError + PhaseAbortedError + PhaseTimeoutError + etc.

```

## User Import Patterns

```
# Neutral schema (preferred for engines/tools)
from ci.transparency.cwe.types.schema import (
    SchemaLoadingResult, SchemaValidationResult,
    SchemaError, SchemaValidationError,
)

from ci.transparency.cwe.types.schema_evolution import (
    SchemaFreezeError, SchemaCompatibilityError,
    SchemaEvolutionReport, SchemaDiff,
)

# Domain-focused (re-exports / aliases; optional ergonomics)
from ci.transparency.cwe.types.cwe import CweError, CweValidationError
from ci.transparency.cwe.types.cwe.schema import CweSchemaValidationResult, CweSchemaValidationError
from ci.transparency.cwe.types.standards import StandardsLoadingResult, StandardsValidationError

# Foundation (to extend)
from ci.transparency.cwe.types.base import BaseResult, BaseLoadingError

# Validation workflow types
from ci.transparency.cwe.types.validation.phase import (
    PhaseValidationResult, MultiPhaseValidationResult
)

# Convenience (top-level) – curated re-exports
from ci.transparency.cwe.types import (
    BatchResult, SchemaValidationResult, SchemaEvolutionReport,
    PhaseValidationResult,
)

```

## Key Design Principles

- Immutable operations throughout using dataclasses.replace
- Rich error context with domain-specific information
- Functional helpers for building and transforming results
- Clean conversion protocols between generic and domain-specific types
- Consistent patterns across all domains
- Namespace organization that matches usage patterns:
  - batch/ - File loading infrastructure (used across domains)
  - schema/ - all schemas
  - schema_evolution/ - all schema evolution
  - validation/ - Validation workflows and orchestration
  - Domain modules - Toolkits for domain-specific functionality
- SCM-compatible versioning (no hardcoded versions)

## Architecture Benefits

- Clear conceptual boundaries between loading, validation, and domain operations
- Scalable structure - easy to add new domains or validation tools
- Type-safe operations with error handling
- Conversion-friendly - transitions between generic and specialized types
- Import flexibility - supports both convenience and precision import patterns
