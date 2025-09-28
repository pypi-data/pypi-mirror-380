"""Standards domain result types and operations.

Immutable, slotted dataclasses for tracking standards loading, validation, and
mapping analysis operations. Built on base result types with standards-specific
functionality and conversion protocols.

Core types:
    - StandardsLoadingResult: Tracks standards definition loading with framework detection
    - StandardsValidationResult: Tracks standards validation with field and constraint checks
    - StandardsMappingResult: Tracks standards mapping validation and analysis

Key operations:
    - add_standard: Add successfully loaded standards definition
    - validate_standard: Validate standards data with field checks
    - analyze_mappings: Analyze standards mappings for consistency

Design principles:
    - Immutable: uses dataclasses.replace for all modifications
    - Standards-specific: tailored for standards definition requirements and patterns
    - Conversion-friendly: integrates with batch processing via from_result
    - Mapping-aware: standards mapping tracking and validation
"""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, TypedDict

from ci.transparency.cwe.types.base import (
    BaseLoadingResult,
    BaseValidationResult,
    add_error,
    add_info,
    add_warning,
)
from ci.transparency.cwe.types.batch import BatchResult


# Type definitions for standards data structures
class StandardsMappingDict(TypedDict, total=False):
    """Typed structure for standards mapping data."""

    target_id: str
    mapping_type: str
    confidence: str


class StandardsControlDict(TypedDict, total=False):
    """Typed structure for standards control data."""

    id: str
    title: str
    description: str
    mappings: list[StandardsMappingDict]


class StandardsDataDict(TypedDict, total=False):
    """Typed structure for standards data."""

    id: str
    name: str
    framework: str
    version: str
    controls: list[StandardsControlDict]


# Default factory functions for type safety
def _new_standards() -> dict[str, StandardsDataDict]:
    """Typed default factory for standards dictionary."""
    return {}


def _new_frameworks() -> dict[str, int]:
    """Typed default factory for framework tracking."""
    return {}


def _new_validation_results() -> dict[str, bool]:
    """Typed default factory for validation results."""
    return {}


def _new_mapping_results() -> dict[str, list[str]]:
    """Typed default factory for mapping results."""
    return {}


def _new_mapping_types() -> dict[str, int]:
    """Typed default factory for mapping type counts."""
    return {}


# ============================================================================
# Standards Loading Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class StandardsLoadingResult(BaseLoadingResult):
    """Result from standards definition loading operations.

    Tracks loaded standards definitions, framework detection, file processing,
    and provides conversion from batch operations. Extends BaseLoadingResult
    with standards-specific tracking and analysis capabilities.
    """

    standards: dict[str, StandardsDataDict] = field(default_factory=_new_standards)
    frameworks: dict[str, int] = field(default_factory=_new_frameworks)  # framework -> count
    invalid_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()
    duplicate_standards: tuple[str, ...] = ()

    # ---- Derived properties ----

    @property
    def standards_count(self) -> int:
        """Number of standards successfully loaded."""
        return len(self.standards)

    @property
    def loaded_standard_ids(self) -> tuple[str, ...]:
        """All loaded standards IDs."""
        return tuple(self.standards.keys())

    @property
    def framework_count(self) -> int:
        """Number of different frameworks detected."""
        return len(self.frameworks)

    @property
    def invalid_file_count(self) -> int:
        """Number of invalid files encountered."""
        return len(self.invalid_files)

    @property
    def skipped_file_count(self) -> int:
        """Number of files that were skipped."""
        return len(self.skipped_files)

    @property
    def duplicate_count(self) -> int:
        """Number of duplicate standards found."""
        return len(self.duplicate_standards)

    @property
    def has_duplicates(self) -> bool:
        """True if duplicate standards were found."""
        return bool(self.duplicate_standards)

    # ---- Simple standards access methods ----

    def get_standard(self, standard_id: str) -> StandardsDataDict | None:
        """Get standards data by ID."""
        return self.standards.get(standard_id)

    def has_standard(self, standard_id: str) -> bool:
        """Check if a standards ID was loaded."""
        return standard_id in self.standards

    def get_frameworks(self) -> list[str]:
        """Get list of all detected frameworks."""
        return list(self.frameworks.keys())

    # ---- Conversion methods ----

    @classmethod
    def from_batch(cls, batch_result: BatchResult) -> "StandardsLoadingResult":
        """Create StandardsLoadingResult from BatchResult.

        Args:
            batch_result: Batch loading result to convert

        Returns:
            StandardsLoadingResult with batch data mapped to standards fields
        """
        return cls.from_result(
            batch_result,
            standards=batch_result.items,  # type: ignore[arg-type]
            skipped_files=batch_result.skipped_files,
        )


# ============================================================================
# Standards Validation Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class StandardsValidationResult(BaseValidationResult):
    """Result from standards validation operations.

    Tracks standards validation results including field validation, constraint checks,
    and validation metadata. Provides detailed tracking of validation outcomes.
    """

    validation_results: dict[str, bool] = field(default_factory=_new_validation_results)
    field_errors: tuple[str, ...] = ()
    validated_standards: tuple[str, ...] = ()
    control_validation_count: int = 0
    constraint_violations: tuple[str, ...] = ()

    # ---- Derived properties ----

    @property
    def validated_count(self) -> int:
        """Number of standards that were validated."""
        return len(self.validation_results)

    @property
    def field_error_count(self) -> int:
        """Number of field-level validation errors."""
        return len(self.field_errors)

    @property
    def constraint_violation_count(self) -> int:
        """Number of constraint violations detected."""
        return len(self.constraint_violations)

    @property
    def has_field_errors(self) -> bool:
        """True if any field-level validation errors occurred."""
        return bool(self.field_errors)

    @property
    def has_constraint_violations(self) -> bool:
        """True if any constraint violations occurred."""
        return bool(self.constraint_violations)

    # ---- Simple analysis methods ----

    def get_failed_standards(self) -> list[str]:
        """Get list of standards IDs that failed validation."""
        return [std_id for std_id, result in self.validation_results.items() if not result]

    def get_passed_standards(self) -> list[str]:
        """Get list of standards IDs that passed validation."""
        return [std_id for std_id, result in self.validation_results.items() if result]


# ============================================================================
# Standards Mapping Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class StandardsMappingResult(BaseValidationResult):
    """Result from standards mapping validation and analysis.

    Tracks standards mapping consistency, invalid references detection,
    and mapping statistics analysis.
    """

    mapping_results: dict[str, list[str]] = field(
        default_factory=_new_mapping_results
    )  # standard_id -> targets
    invalid_mappings: tuple[str, ...] = ()
    duplicate_mappings: tuple[str, ...] = ()
    orphaned_controls: tuple[str, ...] = ()
    mapping_types: dict[str, int] = field(default_factory=_new_mapping_types)

    # ---- Derived properties ----

    @property
    def total_mappings(self) -> int:
        """Total number of mappings tracked."""
        return sum(len(targets) for targets in self.mapping_results.values())

    @property
    def invalid_mapping_count(self) -> int:
        """Number of invalid mappings detected."""
        return len(self.invalid_mappings)

    @property
    def duplicate_mapping_count(self) -> int:
        """Number of duplicate mappings detected."""
        return len(self.duplicate_mappings)

    @property
    def orphaned_control_count(self) -> int:
        """Number of orphaned controls (no mappings)."""
        return len(self.orphaned_controls)

    @property
    def has_invalid_mappings(self) -> bool:
        """True if invalid mappings were detected."""
        return bool(self.invalid_mappings)

    @property
    def has_orphaned_controls(self) -> bool:
        """True if orphaned controls were found."""
        return bool(self.orphaned_controls)

    # ---- Simple mapping access ----

    def get_mappings(self, standard_id: str) -> list[str]:
        """Get all mappings for a specific standard."""
        return self.mapping_results.get(standard_id, [])


# ============================================================================
# Standards loading operations
# ============================================================================


def add_standard(
    result: StandardsLoadingResult,
    standard_id: str,
    standards_data: StandardsDataDict,
    *,
    file_path: Path | None = None,
) -> StandardsLoadingResult:
    """Add successfully loaded standards to the result.

    Args:
        result: The standards loading result to update
        standard_id: Standards identifier
        standards_data: Standards definition data
        file_path: Optional source file path

    Returns:
        New result with standards added
    """
    # Check for duplicates
    if standard_id in result.standards:
        new_duplicates = result.duplicate_standards + (standard_id,)
        result = add_warning(result, f"Duplicate standards ID found: {standard_id}")
        return replace(
            result,
            duplicate_standards=new_duplicates,
            failed=result.failed + 1,
        )

    # Track framework
    framework = standards_data.get("framework", "unknown")
    new_frameworks = {**result.frameworks}
    new_frameworks[framework] = new_frameworks.get(framework, 0) + 1

    # Add the standards
    new_standards = {**result.standards, standard_id: standards_data}
    return replace(
        result,
        standards=new_standards,
        frameworks=new_frameworks,
        loaded=result.loaded + 1,
    )


def track_duplicate_standard(
    result: StandardsLoadingResult, standard_id: str, reason: str
) -> StandardsLoadingResult:
    """Track a duplicate standards ID.

    Args:
        result: The standards loading result to update
        standard_id: Duplicate standards ID
        reason: Reason for the duplicate

    Returns:
        New result with duplicate tracked
    """
    new_duplicates = result.duplicate_standards + (standard_id,)
    result = add_warning(result, f"Duplicate standards: {standard_id} - {reason}")

    return replace(
        result,
        duplicate_standards=new_duplicates,
        failed=result.failed + 1,
    )


def track_invalid_standards_file(
    result: StandardsLoadingResult, file_path: Path, reason: str
) -> StandardsLoadingResult:
    """Track an invalid standards file.

    Args:
        result: The standards loading result to update
        file_path: Path to the invalid file
        reason: Reason the file is invalid

    Returns:
        New result with invalid file tracked
    """
    result = add_error(result, f"Invalid standards file {file_path}: {reason}")
    new_invalid = result.invalid_files + (file_path,)

    return replace(
        result,
        invalid_files=new_invalid,
        failed=result.failed + 1,
    )


def track_skipped_standards_file(
    result: StandardsLoadingResult, file_path: Path, reason: str
) -> StandardsLoadingResult:
    """Track a skipped standards file.

    Args:
        result: The standards loading result to update
        file_path: Path to the skipped file
        reason: Reason the file was skipped

    Returns:
        New result with skipped file tracked
    """
    result = add_info(result, f"Skipped standards file {file_path}: {reason}")
    new_skipped = result.skipped_files + (file_path,)

    return replace(result, skipped_files=new_skipped)


# ============================================================================
# Standards validation operations
# ============================================================================


def validate_standard(
    result: StandardsValidationResult,
    standard_id: str,
    standards_data: StandardsDataDict,
) -> StandardsValidationResult:
    """Validate a standards definition with basic field validation.

    Args:
        result: The validation result to update
        standard_id: Standards ID being validated
        standards_data: Standards data to validate

    Returns:
        New result with validation performed
    """
    is_valid = True

    # Basic standards validation
    if not standards_data.get("id"):
        result = add_error(result, f"Missing ID in standards data for {standard_id}")
        is_valid = False

    if not standards_data.get("name"):
        result = add_error(result, f"Missing name in standards data for {standard_id}")
        is_valid = False

    if not standards_data.get("framework"):
        result = add_warning(result, f"Missing framework in standards data for {standard_id}")

    # Validate controls if present
    controls = standards_data.get("controls", [])
    control_count = 0
    for control in controls:
        if not control.get("id"):
            result = add_error(result, f"Control missing ID in {standard_id}")
            is_valid = False
        else:
            control_count += 1

    # Record validation result
    new_results = {**result.validation_results, standard_id: is_valid}
    new_validated = result.validated_standards + (standard_id,)

    result = replace(
        result,
        validation_results=new_results,
        validated_standards=new_validated,
        control_validation_count=result.control_validation_count + control_count,
    )

    if is_valid:
        return replace(result, passed=result.passed + 1)
    return replace(result, failed=result.failed + 1)


def validate_standards_field(
    result: StandardsValidationResult,
    standard_id: str,
    field_path: str,
    field_value: Any,
    validation_rule: str,
) -> StandardsValidationResult:
    """Validate a specific standards field.

    Args:
        result: The validation result to update
        standard_id: Standards ID being validated
        field_path: Path to the field being validated
        field_value: Value of the field
        validation_rule: Description of the validation rule

    Returns:
        New result with field validation recorded
    """
    # Basic field validation
    is_valid = field_value is not None

    if not is_valid:
        error_msg = f"Field validation failed for {standard_id}.{field_path}: {validation_rule}"
        result = add_error(result, error_msg)
        new_field_errors = result.field_errors + (f"{standard_id}.{field_path}",)
        result = replace(result, field_errors=new_field_errors)
        return replace(result, failed=result.failed + 1)

    return replace(result, passed=result.passed + 1)


def batch_validate_standards(
    result: StandardsValidationResult,
    standards_dict: dict[str, StandardsDataDict],
) -> StandardsValidationResult:
    """Validate multiple standards in batch.

    Args:
        result: The validation result to update
        standards_dict: Dictionary of standards ID -> standards data

    Returns:
        New result with all standards validated
    """
    for standard_id, standards_data in standards_dict.items():
        result = validate_standard(result, standard_id, standards_data)

    return result


# ============================================================================
# Helper classes and functions for mapping analysis
# ============================================================================


@dataclass(frozen=True, slots=True)
class _MappingAnalysis:
    """Internal dataclass for mapping analysis results."""

    mapping_results: dict[str, list[str]]
    mapping_types: dict[str, int]
    invalid_mappings: list[str]
    orphaned_controls: list[str]
    target_to_sources: dict[str, list[str]]


def _build_mapping_analysis(
    standards_dict: dict[str, StandardsDataDict], valid_targets: set[str] | None
) -> _MappingAnalysis:
    """Build initial mapping analysis from standards data."""
    mapping_results: dict[str, list[str]] = {}
    mapping_types: dict[str, int] = {}
    invalid_mappings: list[str] = []
    orphaned_controls: list[str] = []
    target_to_sources: dict[str, list[str]] = {}

    for standard_id, standards_data in standards_dict.items():
        standard_mappings = _process_standard_mappings(
            standard_id,
            standards_data,
            valid_targets,
            mapping_types,
            invalid_mappings,
            orphaned_controls,
            target_to_sources,
        )
        if standard_mappings:
            mapping_results[standard_id] = standard_mappings

    return _MappingAnalysis(
        mapping_results=mapping_results,
        mapping_types=mapping_types,
        invalid_mappings=invalid_mappings,
        orphaned_controls=orphaned_controls,
        target_to_sources=target_to_sources,
    )


def _process_standard_mappings(
    standard_id: str,
    standards_data: StandardsDataDict,
    valid_targets: set[str] | None,
    mapping_types: dict[str, int],
    invalid_mappings: list[str],
    orphaned_controls: list[str],
    target_to_sources: dict[str, list[str]],
) -> list[str]:
    """Process mappings for a single standard."""
    controls = standards_data.get("controls", [])
    standard_mappings: list[str] = []

    for control in controls:
        control_id = control.get("id", f"unknown-{len(orphaned_controls)}")
        mappings = control.get("mappings", [])

        if not mappings:
            orphaned_controls.append(f"{standard_id}:{control_id}")
            continue

        for mapping in mappings:
            target_id = mapping.get("target_id")
            mapping_type = mapping.get("mapping_type", "unknown")

            if target_id:
                _process_single_mapping(
                    standard_id,
                    control_id,
                    target_id,
                    mapping_type,
                    valid_targets,
                    standard_mappings,
                    mapping_types,
                    invalid_mappings,
                    target_to_sources,
                )

    return standard_mappings


def _process_single_mapping(
    standard_id: str,
    control_id: str,
    target_id: str,
    mapping_type: str,
    valid_targets: set[str] | None,
    standard_mappings: list[str],
    mapping_types: dict[str, int],
    invalid_mappings: list[str],
    target_to_sources: dict[str, list[str]],
) -> None:
    """Process a single mapping entry."""
    standard_mappings.append(target_id)
    mapping_types[mapping_type] = mapping_types.get(mapping_type, 0) + 1

    # Check for validity if valid_targets provided
    if valid_targets and target_id not in valid_targets:
        invalid_mappings.append(f"{standard_id}:{control_id} → {target_id}")

    # Track for duplicate detection
    if target_id not in target_to_sources:
        target_to_sources[target_id] = []
    target_to_sources[target_id].append(f"{standard_id}:{control_id}")


def _detect_duplicate_mappings(target_to_sources: dict[str, list[str]]) -> list[str]:
    """Detect duplicate mappings from target-to-sources mapping."""
    duplicate_mappings: list[str] = []
    for target_id, sources in target_to_sources.items():
        if len(sources) > 1:
            duplicate_mappings.append(f"{target_id} ← {', '.join(sources)}")
    return duplicate_mappings


# ============================================================================
# Standards mapping operations
# ============================================================================


def analyze_mappings(
    result: StandardsMappingResult,
    standards_dict: dict[str, StandardsDataDict],
    valid_targets: set[str] | None = None,
) -> StandardsMappingResult:
    """Analyze standards mappings for consistency and detect issues.

    Args:
        result: The mapping result to update
        standards_dict: Dictionary of standards ID -> standards data
        valid_targets: Optional set of valid target IDs for validation

    Returns:
        New result with mapping analysis performed
    """
    mapping_analysis = _build_mapping_analysis(standards_dict, valid_targets)
    duplicate_mappings = _detect_duplicate_mappings(mapping_analysis.target_to_sources)

    return replace(
        result,
        mapping_results=mapping_analysis.mapping_results,
        mapping_types=mapping_analysis.mapping_types,
        invalid_mappings=tuple(mapping_analysis.invalid_mappings),
        orphaned_controls=tuple(mapping_analysis.orphaned_controls),
        duplicate_mappings=tuple(duplicate_mappings),
        passed=result.passed
        + (len(mapping_analysis.mapping_results) - len(mapping_analysis.invalid_mappings)),
        failed=result.failed + len(mapping_analysis.invalid_mappings),
    )


def add_mapping(
    result: StandardsMappingResult,
    standard_id: str,
    target_id: str,
    mapping_type: str = "mapped",
) -> StandardsMappingResult:
    """Add a mapping between a standard and target.

    Args:
        result: The mapping result to update
        standard_id: Source standards ID
        target_id: Target ID (e.g., CWE ID)
        mapping_type: Type of mapping

    Returns:
        New result with mapping added
    """
    current_mappings = result.mapping_results.get(standard_id, [])
    new_items = current_mappings + [target_id]

    new_results = {**result.mapping_results, standard_id: new_items}
    new_types = {**result.mapping_types}
    new_types[mapping_type] = new_types.get(mapping_type, 0) + 1

    return replace(
        result,
        mapping_results=new_results,
        mapping_types=new_types,
    )


# ============================================================================
# Analysis and reporting functions
# ============================================================================


def get_standards_loading_summary(result: StandardsLoadingResult) -> dict[str, Any]:
    """Generate standards loading summary.

    Args:
        result: The standards loading result to summarize

    Returns:
        Dictionary with detailed standards loading statistics
    """
    return {
        "standards_loaded": result.standards_count,
        "successful_loads": result.loaded,
        "failed_loads": result.failed,
        "frameworks_detected": result.framework_count,
        "frameworks": dict(result.frameworks),
        "duplicate_standards": result.duplicate_count,
        "invalid_files": result.invalid_file_count,
        "skipped_files": result.skipped_file_count,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "loaded_standard_ids": list(result.loaded_standard_ids),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
    }


def get_standards_validation_summary(result: StandardsValidationResult) -> dict[str, Any]:
    """Generate standards validation summary.

    Args:
        result: The standards validation result to summarize

    Returns:
        Dictionary with detailed validation statistics
    """
    return {
        "standards_validated": result.validated_count,
        "validation_passed": result.passed,
        "validation_failed": result.failed,
        "field_errors": result.field_error_count,
        "constraint_violations": result.constraint_violation_count,
        "controls_validated": result.control_validation_count,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "failed_standards": result.get_failed_standards(),
        "passed_standards": result.get_passed_standards(),
    }


def get_mapping_summary(result: StandardsMappingResult) -> dict[str, Any]:
    """Generate standards mapping summary.

    Args:
        result: The standards mapping result to summarize

    Returns:
        Dictionary with detailed mapping analysis
    """
    return {
        "total_mappings": result.total_mappings,
        "mapped_standards": len(result.mapping_results),
        "mapping_types": dict(result.mapping_types),
        "invalid_mappings": list(result.invalid_mappings),
        "duplicate_mappings": list(result.duplicate_mappings),
        "orphaned_controls": list(result.orphaned_controls),
        "has_invalid_mappings": result.has_invalid_mappings,
        "has_orphaned_controls": result.has_orphaned_controls,
        "mapping_coverage_rate": (
            len(result.mapping_results)
            / (len(result.mapping_results) + result.orphaned_control_count)
            if (len(result.mapping_results) + result.orphaned_control_count) > 0
            else 0
        ),
    }


# ============================================================================
# Standards-specific analysis functions
# ============================================================================


def get_standards_by_framework(
    result: StandardsLoadingResult, framework: str
) -> dict[str, StandardsDataDict]:
    """Get standards filtered by framework.

    Args:
        result: The standards loading result containing standards data
        framework: Framework to filter by

    Returns:
        Dictionary of standards ID -> standards data for matching framework
    """
    return {
        standard_id: standards_data
        for standard_id, standards_data in result.standards.items()
        if standards_data.get("framework") == framework
    }


def get_control_count(result: StandardsLoadingResult) -> int:
    """Get total number of controls across all standards.

    Args:
        result: The standards loading result containing standards data

    Returns:
        Total count of controls
    """
    total_controls = 0
    for standards_data in result.standards.values():
        controls = standards_data.get("controls", [])
        total_controls += len(controls)
    return total_controls


def get_mapping_coverage(result: StandardsMappingResult) -> float:
    """Calculate mapping coverage rate.

    Args:
        result: The mapping result containing mapping analysis

    Returns:
        Coverage rate as float in [0, 1]
    """
    total_items = len(result.mapping_results) + result.orphaned_control_count
    if total_items == 0:
        return 1.0
    return len(result.mapping_results) / total_items
