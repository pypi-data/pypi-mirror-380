"""Validation framework types and operations.

This package provides validation orchestration tools:
    - Phase-based validation workflows for complex multi-step processes
    - Single-phase validation tracking with detailed context
    - Multi-phase coordination and aggregation
    - Rich validation-specific error hierarchy
    - Analysis and reporting functions for validation outcomes

The validation framework is built around immutable operations and supports
both simple single-phase validation and complex multi-phase workflows with
detailed progress tracking, error handling, and contextual metadata.

Import examples:
    from ci.transparency.cwe.types.validation import (
        PhaseValidationResult,
        MultiPhaseValidationResult,
        add_phase,
        set_current_phase,
        get_multiphase_summary,
        PhaseError,
        PhaseAbortedError,
    )
"""

# Re-export the complete phase validation toolkit as the main validation API
from .phase import (
    # Result types
    MultiPhaseValidationResult,
    # Error types
    PhaseAbortedError,
    PhaseConfigurationError,
    PhaseError,
    PhaseIntegrityError,
    PhaseResourceError,
    PhaseTimeoutError,
    PhaseValidationResult,
    PhaseValidationRuleError,
    # Multi-phase convenience operations
    add_item_to_phase,
    # Multi-phase operations
    add_phase,
    # Single phase operations
    add_processed_item,
    annotate_phase,
    # Analysis and reporting functions
    get_failed_phases,
    get_multiphase_summary,
    get_phase_by_name,
    get_phase_completion_rate,
    get_phase_summary,
    get_phases_by_type,
    merge_phases,
    phase_add_error,
    phase_add_info,
    phase_add_warning,
    set_current_phase,
    set_phase_detail,
    set_phase_info,
    update_phase,
    update_phase_details,
)

__all__ = [
    # Result types
    "PhaseValidationResult",
    "MultiPhaseValidationResult",
    # Single phase operations
    "set_phase_info",
    "add_processed_item",
    "update_phase_details",
    "set_phase_detail",
    # Multi-phase operations
    "add_phase",
    "update_phase",
    "set_current_phase",
    "merge_phases",
    # Multi-phase convenience operations
    "add_item_to_phase",
    "annotate_phase",
    "phase_add_error",
    "phase_add_warning",
    "phase_add_info",
    # Analysis and reporting functions
    "get_phase_summary",
    "get_multiphase_summary",
    "get_phase_by_name",
    "get_phases_by_type",
    "get_failed_phases",
    "get_phase_completion_rate",
    # Error types
    "PhaseError",
    "PhaseAbortedError",
    "PhaseTimeoutError",
    "PhaseResourceError",
    "PhaseIntegrityError",
    "PhaseConfigurationError",
    "PhaseValidationRuleError",
]
