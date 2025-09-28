"""Civic Transparency CWE types package.

Toolkit for CWE operations, standards processing, batch operations,
and validation workflows. Provides immutable result types, rich error handling,
and functional operations across all transparency-related domains.

Architecture:
    - base: Foundation types (BaseResult, BaseLoadingResult, BaseValidationResult)
    - batch: Batch file processing with statistics and error tracking
    - cwe: CWE-specific operations with relationship analysis
    - standards: Standards processing with mapping analysis
    - validation.phase: Phase-based validation with multi-phase aggregation

Example usage:
    from ci.transparency.cwe.types import (
        CweLoadingResult, StandardsLoadingResult, BatchResult,
        add_cwe, validate_standard, analyze_relationships
    )

    # Batch processing
    batch = BatchResult()
    batch = store_item(batch, "cwe-79", cwe_data, Path("cwe-79.yaml"))

    # Convert to domain-specific results
    cwe_result = CweLoadingResult.from_batch(batch)

    # Domain-specific operations
    cwe_result = add_cwe(cwe_result, "CWE-89", sql_injection_data)
    standards_result = validate_standard(StandardsValidationResult(), "NIST-SP-800-53", nist_data)
"""

# Base foundation types - commonly used across domains
from .base import (
    BaseLoadingError,
    BaseLoadingResult,
    # Base result types
    BaseResult,
    # Base error types
    BaseTransparencyError,
    BaseValidationResult,
    # Common helpers
    add_error,
    add_info,
    add_warning,
    merge_results,
    record_failed,
    record_loaded,
    record_passed,
)

# Batch processing - file operations
from .batch import (
    BatchAbortedError,
    # Batch errors
    BatchError,
    BatchResourceError,
    # Batch result type
    BatchResult,
    record_file_error,
    skip_file,
    # Core batch operations
    store_item,
    track_file_type,
)

# CWE domain - CWE definitions and relationships
from .cwe import (
    # CWE errors
    CweError,
    CweLoadingError,
    # CWE result types
    CweLoadingResult,
    CweRelationshipError,
    CweRelationshipResult,
    CweValidationError,
    CweValidationResult,
    # CWE operations
    add_cwe,
    analyze_relationships,
    validate_cwe,
)

# Standards domain - standards processing and mapping
from .standards import (
    # Standards errors
    StandardsError,
    StandardsLoadingError,
    # Standards result types
    StandardsLoadingResult,
    StandardsMappingError,
    StandardsMappingResult,
    StandardsValidationError,
    StandardsValidationResult,
    # Standards operations
    add_standard,
    analyze_mappings,
    validate_standard,
)

# Validation tools - structured validation workflows
from .validation.phase import (
    MultiPhaseValidationResult,
    PhaseAbortedError,
    # Phase errors
    PhaseError,
    PhaseTimeoutError,
    # Phase result types
    PhaseValidationResult,
    add_phase,
    get_multiphase_summary,
    get_phase_summary,
    phase_add_error,
    # Phase operations
    set_phase_info,
)

__all__ = [
    # Base foundation types
    "BaseResult",
    "BaseLoadingResult",
    "BaseValidationResult",
    "BaseTransparencyError",
    "BaseLoadingError",
    "add_error",
    "add_warning",
    "add_info",
    "record_loaded",
    "record_failed",
    "record_passed",
    "merge_results",
    # Batch processing
    "BatchResult",
    "store_item",
    "skip_file",
    "record_file_error",
    "track_file_type",
    "BatchError",
    "BatchAbortedError",
    "BatchResourceError",
    # CWE domain
    "CweLoadingResult",
    "CweValidationResult",
    "CweRelationshipResult",
    "add_cwe",
    "validate_cwe",
    "analyze_relationships",
    "CweError",
    "CweLoadingError",
    "CweValidationError",
    "CweRelationshipError",
    # Standards domain
    "StandardsLoadingResult",
    "StandardsValidationResult",
    "StandardsMappingResult",
    "add_standard",
    "validate_standard",
    "analyze_mappings",
    "StandardsError",
    "StandardsLoadingError",
    "StandardsValidationError",
    "StandardsMappingError",
    # Phase validation
    "PhaseValidationResult",
    "MultiPhaseValidationResult",
    "set_phase_info",
    "add_phase",
    "phase_add_error",
    "get_phase_summary",
    "get_multiphase_summary",
    "PhaseError",
    "PhaseAbortedError",
    "PhaseTimeoutError",
]
