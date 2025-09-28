"""Phase validation result types and operations.

Immutable, slotted dataclasses for tracking single-phase and multi-phase
validation operations. Built on base validation result types with phase-specific
functionality and aggregation capabilities.

Core types:
    - PhaseValidationResult: Single validation phase tracking
    - MultiPhaseValidationResult: Multi-phase aggregation with phase ordering

Key operations:
    - set_phase_info: Configure phase identification
    - add_processed_item: Track processed items in a phase
    - add_phase: Add a phase to multi-phase result
    - update_phase: Update an existing phase in multi-phase result

Design principles:
    - Immutable: uses dataclasses.replace for all modifications
    - Phase-aware: first-class phase identity and ordering
    - Aggregation-friendly: multi-phase results aggregate child phase data
    - Conversion-compatible: follows base result conversion patterns
"""

from collections.abc import Callable
from dataclasses import dataclass, field, replace
from typing import Any

from ci.transparency.cwe.types.base import (
    BaseValidationResult,
    add_error,
    add_info,
    add_warning,
)


# Default factory functions for type safety
def _new_phase_details() -> dict[str, Any]:
    """Typed default factory for phase details."""
    return {}


def _new_phases() -> dict[str, "PhaseValidationResult"]:
    """Typed default factory for phases dictionary."""
    return {}


# ============================================================================
# Single Phase Validation Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class PhaseValidationResult(BaseValidationResult):
    """Result from a single validation phase.

    Tracks validation results for a single phase with phase-specific
    metadata and processing details.
    """

    phase_name: str = ""
    validation_type: str = ""
    items_processed: tuple[str, ...] = ()
    phase_details: dict[str, Any] = field(default_factory=_new_phase_details)

    # ---- Derived properties ----

    @property
    def items_count(self) -> int:
        """Number of items processed in this phase."""
        return len(self.items_processed)

    @property
    def has_phase_details(self) -> bool:
        """True if phase has additional detail information."""
        return bool(self.phase_details)

    # ---- Simple access methods ----

    def get_detail(self, key: str, default: Any = None) -> Any:
        """Get a specific phase detail value."""
        return self.phase_details.get(key, default)


# ============================================================================
# Multi-Phase Validation Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class MultiPhaseValidationResult(BaseValidationResult):
    """Result from multi-phase validation operations.

    Aggregates multiple validation phases and maintains phase ordering
    and current phase tracking. Top-level counts reflect aggregated
    totals from all child phases.
    """

    phases: dict[str, PhaseValidationResult] = field(default_factory=_new_phases)
    phase_order: tuple[str, ...] = ()
    current_phase: str | None = None

    # ---- Derived properties ----

    @property
    def phase_count(self) -> int:
        """Number of phases tracked."""
        return len(self.phases)

    @property
    def items_processed_total(self) -> int:
        """Total items processed across all phases."""
        return sum(phase.items_count for phase in self.phases.values())

    @property
    def has_current_phase(self) -> bool:
        """True if a current phase is set."""
        return self.current_phase is not None

    @property
    def ordered_phases(self) -> list[PhaseValidationResult]:
        """Get phases in their defined order."""
        return [self.phases[name] for name in self.phase_order if name in self.phases]

    # ---- Simple access methods ----

    def get_phase(self, phase_name: str) -> PhaseValidationResult | None:
        """Get a specific phase by name."""
        return self.phases.get(phase_name)

    def has_phase(self, phase_name: str) -> bool:
        """Check if a phase exists."""
        return phase_name in self.phases


# ============================================================================
# Single phase operations
# ============================================================================


def set_phase_info(
    result: PhaseValidationResult,
    phase_name: str,
    validation_type: str = "",
) -> PhaseValidationResult:
    """Set phase identification information.

    Args:
        result: The phase result to update
        phase_name: Name of the validation phase
        validation_type: Optional type of validation performed

    Returns:
        New result with phase info updated
    """
    return replace(result, phase_name=phase_name, validation_type=validation_type)


def add_processed_item(result: PhaseValidationResult, item_id: str) -> PhaseValidationResult:
    """Add an item that was processed in this phase.

    Args:
        result: The phase result to update
        item_id: ID of the item that was processed

    Returns:
        New result with processed item added
    """
    return replace(result, items_processed=result.items_processed + (item_id,))


def update_phase_details(
    result: PhaseValidationResult, details: dict[str, Any]
) -> PhaseValidationResult:
    """Update phase-specific details with shallow merge.

    Args:
        result: The phase result to update
        details: Details to merge into phase details

    Returns:
        New result with details updated
    """
    new_details = {**result.phase_details, **details}
    return replace(result, phase_details=new_details)


def set_phase_detail(result: PhaseValidationResult, key: str, value: Any) -> PhaseValidationResult:
    """Set a specific phase detail.

    Args:
        result: The phase result to update
        key: Detail key to set
        value: Detail value to set

    Returns:
        New result with detail set
    """
    new_details = {**result.phase_details, key: value}
    return replace(result, phase_details=new_details)


# ============================================================================
# Multi-phase operations
# ============================================================================


def add_phase(
    result: MultiPhaseValidationResult,
    phase: PhaseValidationResult,
    *,
    set_current: bool = False,
) -> MultiPhaseValidationResult:
    """Add a new phase and re-aggregate totals.

    Args:
        result: The multi-phase result to update
        phase: Phase to add
        set_current: Whether to set this as the current phase

    Returns:
        New result with phase added and totals re-aggregated
    """
    name = phase.phase_name or f"phase-{len(result.phases) + 1}"

    # Add or replace phase
    new_phases = {**result.phases, name: phase}

    # Update ordering if new phase
    new_order = result.phase_order if name in result.phase_order else result.phase_order + (name,)

    # Set current if requested
    new_current = name if set_current else result.current_phase

    result = replace(
        result,
        phases=new_phases,
        phase_order=new_order,
        current_phase=new_current,
    )

    return _reaggregate_totals(result)


def update_phase(
    result: MultiPhaseValidationResult,
    phase_name: str,
    updater: Callable[[PhaseValidationResult], PhaseValidationResult],
) -> MultiPhaseValidationResult:
    """Update an existing phase and re-aggregate totals.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase to update
        updater: Function that takes and returns an updated phase

    Returns:
        New result with phase updated and totals re-aggregated
    """
    phase = result.phases.get(phase_name)
    if phase is None:
        return add_error(result, f"Phase '{phase_name}' not found for update")

    updated_phase = updater(phase)
    new_phases = {**result.phases, phase_name: updated_phase}
    result = replace(result, phases=new_phases)

    return _reaggregate_totals(result)


def set_current_phase(
    result: MultiPhaseValidationResult, phase_name: str | None
) -> MultiPhaseValidationResult:
    """Set the current active phase.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase to set as current, or None to clear

    Returns:
        New result with current phase updated
    """
    if phase_name is not None and phase_name not in result.phases:
        return add_warning(result, f"Phase '{phase_name}' not found; current not changed")

    return replace(result, current_phase=phase_name)


def merge_phases(
    primary: MultiPhaseValidationResult, *others: MultiPhaseValidationResult
) -> MultiPhaseValidationResult:
    """Merge multiple multi-phase results.

    Args:
        primary: The primary result (type is preserved)
        *others: Additional results to merge

    Returns:
        New result with all phases merged and totals re-aggregated
    """
    merged_phases = dict(primary.phases)
    merged_order = list(primary.phase_order)

    # Merge phases from other results
    for other in others:
        for name, phase in other.phases.items():
            merged_phases[name] = phase
            if name not in merged_order:
                merged_order.append(name)

    result = replace(
        primary,
        phases=merged_phases,
        phase_order=tuple(merged_order),
    )

    return _reaggregate_totals(result)


# ============================================================================
# Multi-phase convenience operations
# ============================================================================


def add_item_to_phase(
    result: MultiPhaseValidationResult, phase_name: str, item_id: str
) -> MultiPhaseValidationResult:
    """Add an item to a named phase's processed list.

    Creates the phase if it doesn't exist.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase
        item_id: ID of the item to add

    Returns:
        New result with item added to phase
    """

    def updater(phase: PhaseValidationResult) -> PhaseValidationResult:
        return add_processed_item(phase, item_id)

    if phase_name not in result.phases:
        # Create new phase
        new_phase = PhaseValidationResult(phase_name=phase_name)
        new_phase = add_processed_item(new_phase, item_id)
        return add_phase(result, new_phase)
    # Update existing phase
    return update_phase(result, phase_name, updater)


def annotate_phase(
    result: MultiPhaseValidationResult, phase_name: str, **details: Any
) -> MultiPhaseValidationResult:
    """Add details to a named phase.

    Creates the phase if it doesn't exist.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase
        **details: Details to add to the phase

    Returns:
        New result with phase annotated
    """

    def updater(phase: PhaseValidationResult) -> PhaseValidationResult:
        return update_phase_details(phase, details)

    if phase_name not in result.phases:
        # Create new phase
        new_phase = PhaseValidationResult(phase_name=phase_name)
        new_phase = update_phase_details(new_phase, details)
        return add_phase(result, new_phase)
    # Update existing phase
    return update_phase(result, phase_name, updater)


def phase_add_error(
    result: MultiPhaseValidationResult, phase_name: str, message: str
) -> MultiPhaseValidationResult:
    """Add an error message to a named phase.

    Creates the phase if it doesn't exist.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase
        message: Error message to add

    Returns:
        New result with error added to phase
    """

    def updater(phase: PhaseValidationResult) -> PhaseValidationResult:
        return add_error(phase, message)

    if phase_name not in result.phases:
        # Create new phase
        new_phase = PhaseValidationResult(phase_name=phase_name)
        new_phase = add_error(new_phase, message)
        return add_phase(result, new_phase)
    # Update existing phase
    return update_phase(result, phase_name, updater)


def phase_add_warning(
    result: MultiPhaseValidationResult, phase_name: str, message: str
) -> MultiPhaseValidationResult:
    """Add a warning message to a named phase.

    Creates the phase if it doesn't exist.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase
        message: Warning message to add

    Returns:
        New result with warning added to phase
    """

    def updater(phase: PhaseValidationResult) -> PhaseValidationResult:
        return add_warning(phase, message)

    if phase_name not in result.phases:
        # Create new phase
        new_phase = PhaseValidationResult(phase_name=phase_name)
        new_phase = add_warning(new_phase, message)
        return add_phase(result, new_phase)
    # Update existing phase
    return update_phase(result, phase_name, updater)


def phase_add_info(
    result: MultiPhaseValidationResult, phase_name: str, message: str
) -> MultiPhaseValidationResult:
    """Add an info message to a named phase.

    Creates the phase if it doesn't exist.

    Args:
        result: The multi-phase result to update
        phase_name: Name of the phase
        message: Info message to add

    Returns:
        New result with info added to phase
    """

    def updater(phase: PhaseValidationResult) -> PhaseValidationResult:
        return add_info(phase, message)

    if phase_name not in result.phases:
        # Create new phase
        new_phase = PhaseValidationResult(phase_name=phase_name)
        new_phase = add_info(new_phase, message)
        return add_phase(result, new_phase)
    # Update existing phase
    return update_phase(result, phase_name, updater)


# ============================================================================
# Analysis and reporting functions
# ============================================================================


def get_phase_summary(result: PhaseValidationResult) -> dict[str, Any]:
    """Generate single-phase validation summary.

    Args:
        result: The phase result to summarize

    Returns:
        Dictionary with detailed phase statistics
    """
    return {
        "phase_name": result.phase_name,
        "validation_type": result.validation_type,
        "items_processed": result.items_count,
        "validation_passed": result.passed,
        "validation_failed": result.failed,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "has_infos": result.has_infos,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
        "info_count": result.info_count,
        "phase_details": dict(result.phase_details),
    }


def get_multiphase_summary(result: MultiPhaseValidationResult) -> dict[str, Any]:
    """Generate multi-phase validation summary.

    Args:
        result: The multi-phase result to summarize

    Returns:
        Dictionary with detailed multi-phase statistics
    """
    phase_summaries = {name: get_phase_summary(phase) for name, phase in result.phases.items()}

    return {
        # Phase organization
        "phase_count": result.phase_count,
        "phase_order": list(result.phase_order),
        "current_phase": result.current_phase,
        # Aggregated totals
        "items_processed_total": result.items_processed_total,
        "validation_passed_total": result.passed,
        "validation_failed_total": result.failed,
        # Message totals
        "errors_total": result.error_count,
        "warnings_total": result.warning_count,
        "infos_total": result.info_count,
        # Overall metrics
        "success_rate_percent": round(result.success_rate * 100, 2),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "has_infos": result.has_infos,
        # Per-phase details
        "phases": phase_summaries,
    }


# ============================================================================
# Helper functions
# ============================================================================


def _reaggregate_totals(result: MultiPhaseValidationResult) -> MultiPhaseValidationResult:
    """Re-aggregate top-level totals from child phases.

    This ensures that the top-level BaseValidationResult fields reflect
    the sum of all child phases, maintaining consistency.

    Args:
        result: The multi-phase result to re-aggregate

    Returns:
        New result with totals re-aggregated from child phases
    """
    # Aggregate all messages and counts from child phases
    all_errors: tuple[str, ...] = ()
    all_warnings: tuple[str, ...] = ()
    all_infos: tuple[str, ...] = ()
    total_passed = 0
    total_failed = 0

    for phase in result.phases.values():
        all_errors += phase.errors
        all_warnings += phase.warnings
        all_infos += phase.infos
        total_passed += phase.passed
        total_failed += phase.failed

    return replace(
        result,
        errors=all_errors,
        warnings=all_warnings,
        infos=all_infos,
        passed=total_passed,
        failed=total_failed,
    )


# ============================================================================
# Phase-specific analysis functions
# ============================================================================


def get_phase_by_name(
    result: MultiPhaseValidationResult, phase_name: str
) -> PhaseValidationResult | None:
    """Get a phase by name with None if not found."""
    return result.phases.get(phase_name)


def get_phases_by_type(
    result: MultiPhaseValidationResult, validation_type: str
) -> list[PhaseValidationResult]:
    """Get all phases of a specific validation type."""
    return [phase for phase in result.phases.values() if phase.validation_type == validation_type]


def get_failed_phases(result: MultiPhaseValidationResult) -> list[PhaseValidationResult]:
    """Get all phases that have failures."""
    return [phase for phase in result.phases.values() if phase.failed > 0]


def get_phase_completion_rate(result: MultiPhaseValidationResult) -> float:
    """Calculate overall phase completion rate."""
    if not result.phases:
        return 1.0

    completed_phases = sum(1 for phase in result.phases.values() if not phase.has_errors)
    return completed_phases / len(result.phases)
