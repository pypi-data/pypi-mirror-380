# Organization

```text
ci/transparency/cwe/types/
├── __init__.py            # Main entry point (convenience imports)
├── py.typed               # Type marker (unchanged)
├── _version.py            # Version info (SCM-managed)
│
├── base/                  # Foundation types
│   ├── __init__.py        # Base toolkit
│   ├── results.py         # BaseResult + BaseLoadingResult + BaseValidationResult + helpers
│   └── errors.py          # BaseTransparencyError + BaseLoadingError + BaseValidationError
│
├── batch/                 # Batch file processing
│   ├── __init__.py        # Batch toolkit (BatchResult + operations + errors)
│   ├── results.py         # BatchResult + batch operations
│   └── errors.py          # BatchError + BatchAbortedError + BatchResourceError + etc.
│
├── cwe/                   # CWE domain (includes CWE schema subdomain)
│   ├── __init__.py        # CWE toolkit
│   ├── results.py         # CweLoadingResult + CweValidationResult + CweRelationshipResult + operations
│   ├── errors.py          # CweError + CweLoadingError + CweValidationError + CweRelationshipError + etc.
│   └── schema/            # CWE Schema subdomain
│       ├── __init__.py    # CWE schema toolkit
│       ├── results.py     # CweSchemaLoadingResult + CweSchemaValidationResult + CweSchemaFreezeResult + operations
│       └── errors.py      # CweSchemaError + CweSchemaLoadingError + CweSchemaValidationError + CweSchemaFreezeError + etc.
│
├── standards/             # Standards domain
│   ├── __init__.py        # Standards toolkit
│   ├── results.py         # StandardsLoadingResult + StandardsValidationResult + StandardsMappingResult + operations
│   └── errors.py          # StandardsError + StandardsLoadingError + StandardsValidationError + StandardsMappingError + etc.
│
└── validation/            # Validation tools
    ├── __init__.py        # Validation toolkit (re-exports phase tools)
    └── phase/             # Phase-based validation
        ├── __init__.py    # Phase validation toolkit
        ├── results.py     # PhaseValidationResult + MultiPhaseValidationResult + operations
        └── errors.py      # PhaseError + PhaseAbortedError + PhaseTimeoutError + etc.
```

## User Import Patterns

```
# Domain-focused (most common)
from ci.transparency.cwe.types.cwe import CweLoadingResult, CweError, add_cwe
from ci.transparency.cwe.types.cwe.schema import CweSchemaLoadingResult, CweFreezeViolationError, load_cwe_schema
from ci.transparency.cwe.types.standards import StandardsLoadingResult, StandardsMappingError, analyze_mappings
from ci.transparency.cwe.types.batch import BatchResult, skip_file, store_item

# Foundation (for extending)
from ci.transparency.cwe.types.base import BaseResult, BaseLoadingError, add_error

# Validation workflows
from ci.transparency.cwe.types.validation.phase import PhaseValidationResult, MultiPhaseValidationResult, add_phase

# Convenience (top-level) - most common operations
from ci.transparency.cwe.types import (
    BatchResult, CweLoadingResult, StandardsLoadingResult,
    PhaseValidationResult, add_cwe, validate_standard
)

# Specialized validation tools
from ci.transparency.cwe.types.validation import PhaseValidationResult, get_multiphase_summary
```

## Key Design Principles

- Immutable operations throughout using dataclasses.replace
- Rich error context with domain-specific information
- Functional helpers for building and transforming results
- Clean conversion protocols between generic and domain-specific types
- Consistent patterns across all domains
- Namespace organization that matches usage patterns:
  - batch/ - File loading infrastructure (used across domains)
  - validation/ - Validation workflows and orchestration
  - Domain modules - Toolkits for domain-specific functionality
- SCM-compatible versioning (no hardcoded versions)

## Architecture Benefits

- Clear conceptual boundaries between loading, validation, and domain operations
- Scalable structure - easy to add new domains or validation tools
- Type-safe operations with error handling
- Conversion-friendly - transitions between generic and specialized types
- Import flexibility - supports both convenience and precision import patterns
