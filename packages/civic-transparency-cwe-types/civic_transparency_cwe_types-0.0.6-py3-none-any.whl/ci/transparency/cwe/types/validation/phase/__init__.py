"""Phase validation types and errors.

This package provides:
    - Single- and multi-phase validation result dataclasses
    - Immutable helper operations for building and aggregating results
    - Rich phase-specific error hierarchy for error handling

Import examples:
    from ci.transparency.cwe.types.validation.phase import (
        PhaseValidationResult,
        MultiPhaseValidationResult,
        get_phase_summary,
        get_multiphase_summary,
        PhaseError,
        PhaseAbortedError,
        PhaseTimeoutError,
        PhaseConfigurationError,
        PhaseResourceError,
        PhaseIntegrityError,
        PhaseValidationRuleError,
    )
"""

from .errors import (
    # Phase operation errors
    PhaseAbortedError,
    # Phase configuration and rule errors
    PhaseConfigurationError,
    # Base phase error
    PhaseError,
    PhaseIntegrityError,
    PhaseResourceError,
    PhaseTimeoutError,
    PhaseValidationRuleError,
)
from .results import (
    MultiPhaseValidationResult,
    # Result types
    PhaseValidationResult,
    # Multi-phase convenience operations
    add_item_to_phase,
    # Multi-phase operations
    add_phase,
    add_processed_item,
    annotate_phase,
    get_failed_phases,
    get_multiphase_summary,
    # Phase-specific analysis functions
    get_phase_by_name,
    get_phase_completion_rate,
    # Analysis and reporting functions
    get_phase_summary,
    get_phases_by_type,
    merge_phases,
    phase_add_error,
    phase_add_info,
    phase_add_warning,
    set_current_phase,
    set_phase_detail,
    # Single phase operations
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
    # Base phase error
    "PhaseError",
    # Phase operation errors
    "PhaseAbortedError",
    "PhaseTimeoutError",
    "PhaseResourceError",
    "PhaseIntegrityError",
    # Phase configuration and rule errors
    "PhaseConfigurationError",
    "PhaseValidationRuleError",
]
