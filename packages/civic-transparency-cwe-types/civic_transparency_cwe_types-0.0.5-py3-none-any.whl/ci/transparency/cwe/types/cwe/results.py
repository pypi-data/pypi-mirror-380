"""CWE domain result types and operations.

Immutable, slotted dataclasses for tracking CWE loading, validation, and
relationship analysis operations. Built on base result types with CWE-specific
functionality and conversion protocols.

Core types:
    - CweLoadingResult: Tracks CWE definition loading with duplicate detection
    - CweValidationResult: Tracks CWE validation with field and schema checks
    - CweRelationshipResult: Tracks CWE relationship validation and analysis

Key operations:
    - add_cwe: Add successfully loaded CWE definition
    - validate_cwe: Validate CWE data with field checks
    - analyze_relationships: Analyze CWE relationships for consistency

Design principles:
    - Immutable: uses dataclasses.replace for all modifications
    - CWE-specific: tailored for CWE definition requirements and patterns
    - Conversion-friendly: integrates with batch processing via from_result
    - Relationship-aware: CWE relationship tracking and validation
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


# Type definitions for CWE data structures
class CweRelationshipDict(TypedDict, total=False):
    """Typed structure for CWE relationship data."""

    cwe_id: str
    type: str


class CweDataDict(TypedDict, total=False):
    """Typed structure for CWE data."""

    id: str
    name: str
    category: str
    relationships: list[CweRelationshipDict]


# Default factory functions for type safety
def _new_cwes() -> dict[str, CweDataDict]:
    """Typed default factory for CWE dictionary."""
    return {}


def _new_duplicate_ids() -> dict[str, Path]:
    """Typed default factory for duplicate ID tracking."""
    return {}


def _new_validation_results() -> dict[str, bool]:
    """Typed default factory for validation results."""
    return {}


def _new_relationship_map() -> dict[str, list[str]]:
    """Typed default factory for relationship mapping."""
    return {}


def _new_relationship_types() -> dict[str, int]:
    """Typed default factory for relationship type counts."""
    return {}


# ============================================================================
# CWE Loading Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class CweLoadingResult(BaseLoadingResult):
    """Result from CWE definition loading operations.

    Tracks loaded CWE definitions, duplicate detection, file processing,
    and provides conversion from batch operations. Extends BaseLoadingResult
    with CWE-specific tracking and analysis capabilities.
    """

    cwes: dict[str, CweDataDict] = field(default_factory=_new_cwes)
    duplicate_ids: dict[str, Path] = field(default_factory=_new_duplicate_ids)
    invalid_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()

    # ---- Derived properties ----

    @property
    def cwe_count(self) -> int:
        """Number of CWEs successfully loaded."""
        return len(self.cwes)

    @property
    def loaded_cwe_ids(self) -> tuple[str, ...]:
        """All loaded CWE IDs."""
        return tuple(self.cwes.keys())

    @property
    def duplicate_count(self) -> int:
        """Number of duplicate CWE IDs found."""
        return len(self.duplicate_ids)

    @property
    def invalid_file_count(self) -> int:
        """Number of invalid files encountered."""
        return len(self.invalid_files)

    @property
    def skipped_file_count(self) -> int:
        """Number of files that were skipped."""
        return len(self.skipped_files)

    @property
    def has_duplicates(self) -> bool:
        """True if duplicate CWE IDs were found."""
        return bool(self.duplicate_ids)

    # ---- Simple CWE access methods ----

    def get_cwe(self, cwe_id: str) -> CweDataDict | None:
        """Get CWE data by ID."""
        return self.cwes.get(cwe_id)

    def has_cwe(self, cwe_id: str) -> bool:
        """Check if a CWE ID was loaded."""
        return cwe_id in self.cwes

    # ---- Conversion methods ----

    @classmethod
    def from_batch(cls, batch_result: BatchResult) -> "CweLoadingResult":
        """Create CweLoadingResult from BatchResult.

        Args:
            batch_result: Batch loading result to convert

        Returns:
            CweLoadingResult with batch data mapped to CWE fields
        """
        return cls.from_result(
            batch_result,
            cwes=batch_result.items,  # type: ignore[arg-type]
            skipped_files=batch_result.skipped_files,
        )


# ============================================================================
# CWE Validation Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class CweValidationResult(BaseValidationResult):
    """Result from CWE validation operations.

    Tracks CWE validation results including field validation, schema validation,
    and validation metadata. Provides detailed tracking of validation outcomes.
    """

    validation_results: dict[str, bool] = field(default_factory=_new_validation_results)
    field_errors: tuple[str, ...] = ()
    validated_cwes: tuple[str, ...] = ()
    schema_validation_used: bool = False
    schema_version: str = ""

    # ---- Derived properties ----

    @property
    def validated_count(self) -> int:
        """Number of CWEs that were validated."""
        return len(self.validation_results)

    @property
    def field_error_count(self) -> int:
        """Number of field-level validation errors."""
        return len(self.field_errors)

    @property
    def has_field_errors(self) -> bool:
        """True if any field-level validation errors occurred."""
        return bool(self.field_errors)

    # ---- Simple analysis methods ----

    def get_failed_cwes(self) -> list[str]:
        """Get list of CWE IDs that failed validation."""
        return [cwe_id for cwe_id, result in self.validation_results.items() if not result]

    def get_passed_cwes(self) -> list[str]:
        """Get list of CWE IDs that passed validation."""
        return [cwe_id for cwe_id, result in self.validation_results.items() if result]


# ============================================================================
# CWE Relationship Result
# ============================================================================


@dataclass(frozen=True, slots=True)
class CweRelationshipResult(BaseValidationResult):
    """Result from CWE relationship validation and analysis.

    Tracks CWE relationship consistency, circular dependency detection,
    and relationship graph analysis.
    """

    relationship_map: dict[str, list[str]] = field(default_factory=_new_relationship_map)
    circular_dependencies: tuple[str, ...] = ()
    orphaned_cwes: tuple[str, ...] = ()
    invalid_references: tuple[str, ...] = ()
    relationship_types: dict[str, int] = field(default_factory=_new_relationship_types)

    # ---- Derived properties ----

    @property
    def total_relationships(self) -> int:
        """Total number of relationships tracked."""
        return sum(len(refs) for refs in self.relationship_map.values())

    @property
    def circular_dependency_count(self) -> int:
        """Number of circular dependencies detected."""
        return len(self.circular_dependencies)

    @property
    def orphaned_cwe_count(self) -> int:
        """Number of orphaned CWEs (no relationships)."""
        return len(self.orphaned_cwes)

    @property
    def invalid_reference_count(self) -> int:
        """Number of invalid relationship references."""
        return len(self.invalid_references)

    @property
    def has_circular_dependencies(self) -> bool:
        """True if circular dependencies were detected."""
        return bool(self.circular_dependencies)

    @property
    def has_orphaned_cwes(self) -> bool:
        """True if orphaned CWEs were found."""
        return bool(self.orphaned_cwes)

    # ---- Simple relationship access ----

    def get_relationships(self, cwe_id: str) -> list[str]:
        """Get all relationships for a specific CWE."""
        return self.relationship_map.get(cwe_id, [])


# ============================================================================
# CWE loading operations
# ============================================================================


def add_cwe(
    result: CweLoadingResult,
    cwe_id: str,
    cwe_data: CweDataDict,
    *,
    file_path: Path | None = None,
) -> CweLoadingResult:
    """Add successfully loaded CWE to the result.

    Args:
        result: The CWE loading result to update
        cwe_id: CWE identifier
        cwe_data: CWE definition data
        file_path: Optional source file path

    Returns:
        New result with CWE added
    """
    # Check for duplicates
    if cwe_id in result.cwes:
        if file_path:
            new_duplicates = {**result.duplicate_ids, cwe_id: file_path}
            result = replace(result, duplicate_ids=new_duplicates)
        result = add_warning(result, f"Duplicate CWE ID found: {cwe_id}")
        return replace(result, failed=result.failed + 1)

    # Add the CWE
    new_cwes = {**result.cwes, cwe_id: cwe_data}
    return replace(
        result,
        cwes=new_cwes,
        loaded=result.loaded + 1,
    )


def track_duplicate_cwe(result: CweLoadingResult, cwe_id: str, file_path: Path) -> CweLoadingResult:
    """Track a duplicate CWE ID.

    Args:
        result: The CWE loading result to update
        cwe_id: Duplicate CWE ID
        file_path: File where duplicate was found

    Returns:
        New result with duplicate tracked
    """
    new_duplicates = {**result.duplicate_ids, cwe_id: file_path}
    result = add_warning(result, f"Duplicate CWE ID: {cwe_id} in {file_path}")

    return replace(
        result,
        duplicate_ids=new_duplicates,
        failed=result.failed + 1,
    )


def track_invalid_file(result: CweLoadingResult, file_path: Path, reason: str) -> CweLoadingResult:
    """Track an invalid CWE file.

    Args:
        result: The CWE loading result to update
        file_path: Path to the invalid file
        reason: Reason the file is invalid

    Returns:
        New result with invalid file tracked
    """
    result = add_error(result, f"Invalid CWE file {file_path}: {reason}")
    new_invalid = result.invalid_files + (file_path,)

    return replace(
        result,
        invalid_files=new_invalid,
        failed=result.failed + 1,
    )


def track_skipped_cwe_file(
    result: CweLoadingResult, file_path: Path, reason: str
) -> CweLoadingResult:
    """Track a skipped CWE file.

    Args:
        result: The CWE loading result to update
        file_path: Path to the skipped file
        reason: Reason the file was skipped

    Returns:
        New result with skipped file tracked
    """
    result = add_info(result, f"Skipped CWE file {file_path}: {reason}")
    new_skipped = result.skipped_files + (file_path,)

    return replace(result, skipped_files=new_skipped)


# ============================================================================
# CWE validation operations
# ============================================================================


def validate_cwe(
    result: CweValidationResult,
    cwe_id: str,
    cwe_data: CweDataDict,
) -> CweValidationResult:
    """Validate a CWE definition with basic field validation.

    Args:
        result: The validation result to update
        cwe_id: CWE ID being validated
        cwe_data: CWE data to validate

    Returns:
        New result with validation performed
    """
    is_valid = True

    # Basic CWE validation
    if not cwe_data.get("id"):
        result = add_error(result, f"Missing ID in CWE data for {cwe_id}")
        is_valid = False

    if not cwe_data.get("name"):
        result = add_error(result, f"Missing name in CWE data for {cwe_id}")
        is_valid = False

    if not cwe_data.get("category"):
        result = add_warning(result, f"Missing category in CWE data for {cwe_id}")

    # Record validation result
    new_results = {**result.validation_results, cwe_id: is_valid}
    new_validated = result.validated_cwes + (cwe_id,)

    result = replace(
        result,
        validation_results=new_results,
        validated_cwes=new_validated,
    )

    if is_valid:
        return replace(result, passed=result.passed + 1)
    return replace(result, failed=result.failed + 1)


def validate_cwe_field(
    result: CweValidationResult,
    cwe_id: str,
    field_path: str,
    field_value: Any,
    validation_rule: str,
) -> CweValidationResult:
    """Validate a specific CWE field.

    Args:
        result: The validation result to update
        cwe_id: CWE ID being validated
        field_path: Path to the field being validated
        field_value: Value of the field
        validation_rule: Description of the validation rule

    Returns:
        New result with field validation recorded
    """
    # Basic field validation
    is_valid = field_value is not None

    if not is_valid:
        error_msg = f"Field validation failed for {cwe_id}.{field_path}: {validation_rule}"
        result = add_error(result, error_msg)
        new_field_errors = result.field_errors + (f"{cwe_id}.{field_path}",)
        result = replace(result, field_errors=new_field_errors)
        return replace(result, failed=result.failed + 1)

    return replace(result, passed=result.passed + 1)


def batch_validate_cwes(
    result: CweValidationResult,
    cwe_dict: dict[str, CweDataDict],
) -> CweValidationResult:
    """Validate multiple CWEs in batch.

    Args:
        result: The validation result to update
        cwe_dict: Dictionary of CWE ID -> CWE data

    Returns:
        New result with all CWEs validated
    """
    for cwe_id, cwe_data in cwe_dict.items():
        result = validate_cwe(result, cwe_id, cwe_data)

    return result


# ============================================================================
# CWE relationship operations
# ============================================================================


def analyze_relationships(
    result: CweRelationshipResult,
    cwe_dict: dict[str, CweDataDict],
) -> CweRelationshipResult:
    """Analyze CWE relationships for consistency and detect issues.

    Args:
        result: The relationship result to update
        cwe_dict: Dictionary of CWE ID -> CWE data

    Returns:
        New result with relationship analysis performed
    """
    relationship_map: dict[str, list[str]] = {}
    relationship_types: dict[str, int] = {}
    invalid_references: list[str] = []
    orphaned_cwes: list[str] = []

    # Build relationship map
    for cwe_id, cwe_data in cwe_dict.items():
        relationships = cwe_data.get("relationships", [])
        related_ids: list[str] = []

        for relationship in relationships:
            related_id: str | None = relationship.get("cwe_id")
            rel_type: str = relationship.get("type", "unknown")

            if related_id:
                related_ids.append(related_id)
                relationship_types[rel_type] = relationship_types.get(rel_type, 0) + 1

                # Check if reference is valid
                if related_id not in cwe_dict:
                    invalid_references.append(f"{cwe_id} → {related_id}")

        if related_ids:
            relationship_map[cwe_id] = related_ids
        else:
            orphaned_cwes.append(cwe_id)

    # Detect circular dependencies
    circular_deps = _detect_circular_dependencies(relationship_map)

    return replace(
        result,
        relationship_map=relationship_map,
        relationship_types=relationship_types,
        circular_dependencies=tuple(circular_deps),
        orphaned_cwes=tuple(orphaned_cwes),
        invalid_references=tuple(invalid_references),
        passed=result.passed + (len(cwe_dict) - len(invalid_references)),
        failed=result.failed + len(invalid_references),
    )


def add_relationship(
    result: CweRelationshipResult,
    from_cwe: str,
    to_cwe: str,
    relationship_type: str = "related",
) -> CweRelationshipResult:
    """Add a relationship between two CWEs.

    Args:
        result: The relationship result to update
        from_cwe: Source CWE ID
        to_cwe: Target CWE ID
        relationship_type: Type of relationship

    Returns:
        New result with relationship added
    """
    current_relationships = result.relationship_map.get(from_cwe, [])
    new_relationships = current_relationships + [to_cwe]

    new_map = {**result.relationship_map, from_cwe: new_relationships}
    new_types = {**result.relationship_types}
    new_types[relationship_type] = new_types.get(relationship_type, 0) + 1

    return replace(
        result,
        relationship_map=new_map,
        relationship_types=new_types,
    )


# ============================================================================
# Analysis and reporting functions
# ============================================================================


def get_cwe_loading_summary(result: CweLoadingResult) -> dict[str, Any]:
    """Generate CWE loading summary.

    Args:
        result: The CWE loading result to summarize

    Returns:
        Dictionary with detailed CWE loading statistics
    """
    return {
        "cwes_loaded": result.cwe_count,
        "successful_loads": result.loaded,
        "failed_loads": result.failed,
        "duplicate_ids": result.duplicate_count,
        "invalid_files": result.invalid_file_count,
        "skipped_files": result.skipped_file_count,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "loaded_cwe_ids": list(result.loaded_cwe_ids),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
    }


def get_cwe_validation_summary(result: CweValidationResult) -> dict[str, Any]:
    """Generate CWE validation summary.

    Args:
        result: The CWE validation result to summarize

    Returns:
        Dictionary with detailed validation statistics
    """
    return {
        "cwes_validated": result.validated_count,
        "validation_passed": result.passed,
        "validation_failed": result.failed,
        "field_errors": result.field_error_count,
        "schema_validation_used": result.schema_validation_used,
        "schema_version": result.schema_version,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "failed_cwes": result.get_failed_cwes(),
        "passed_cwes": result.get_passed_cwes(),
    }


def get_relationship_summary(result: CweRelationshipResult) -> dict[str, Any]:
    """Generate CWE relationship summary.

    Args:
        result: The CWE relationship result to summarize

    Returns:
        Dictionary with detailed relationship analysis
    """
    return {
        "total_relationships": result.total_relationships,
        "connected_cwes": len(result.relationship_map),
        "relationship_types": dict(result.relationship_types),
        "circular_dependencies": list(result.circular_dependencies),
        "orphaned_cwes": list(result.orphaned_cwes),
        "invalid_references": list(result.invalid_references),
        "has_circular_dependencies": result.has_circular_dependencies,
        "has_orphaned_cwes": result.has_orphaned_cwes,
        "invalid_reference_rate": (
            result.invalid_reference_count / result.total_relationships
            if result.total_relationships > 0
            else 0
        ),
    }


# ============================================================================
# Helper functions
# ============================================================================


def _detect_circular_dependencies(relationship_map: dict[str, list[str]]) -> list[str]:
    """Detect circular dependencies in relationship map.

    Args:
        relationship_map: Dictionary mapping CWE ID to list of related CWE IDs

    Returns:
        List of CWE IDs involved in circular dependencies
    """
    circular_deps: list[str] = []
    visited: set[str] = set()

    def dfs(cwe_id: str, path: list[str]) -> None:
        if cwe_id in path:
            # Found a cycle
            cycle_start = path.index(cwe_id)
            cycle = path[cycle_start:] + [cwe_id]
            circular_deps.extend(cycle)
            return

        if cwe_id in visited:
            return

        visited.add(cwe_id)
        path.append(cwe_id)

        for related_id in relationship_map.get(cwe_id, []):
            dfs(related_id, path)

        path.pop()

    for cwe_id in relationship_map:
        if cwe_id not in visited:
            dfs(cwe_id, [])

    return list(set(circular_deps))


# ============================================================================
# CWE-specific analysis functions
# ============================================================================


def get_cwes_by_category(result: CweLoadingResult, category: str) -> dict[str, CweDataDict]:
    """Get CWEs filtered by category.

    Args:
        result: The CWE loading result containing CWE data
        category: Category to filter by

    Returns:
        Dictionary of CWE ID -> CWE data for matching category
    """
    return {
        cwe_id: cwe_data
        for cwe_id, cwe_data in result.cwes.items()
        if cwe_data.get("category") == category
    }


def get_relationship_depth(result: CweRelationshipResult, cwe_id: str) -> int:
    """Get maximum relationship depth for a CWE.

    Args:
        result: The relationship result containing relationship data
        cwe_id: CWE ID to analyze

    Returns:
        Maximum depth in the relationship graph
    """
    return _calculate_relationship_depth(result.relationship_map, cwe_id, set())


def _calculate_relationship_depth(
    relationship_map: dict[str, list[str]], cwe_id: str, visited: set[str]
) -> int:
    """Calculate relationship depth recursively."""
    if cwe_id in visited:
        return 0  # Circular dependency

    visited.add(cwe_id)
    relationships = relationship_map.get(cwe_id, [])

    if not relationships:
        return 1

    max_depth = 0
    for related_id in relationships:
        depth = _calculate_relationship_depth(relationship_map, related_id, visited.copy())
        max_depth = max(max_depth, depth)

    return max_depth + 1
