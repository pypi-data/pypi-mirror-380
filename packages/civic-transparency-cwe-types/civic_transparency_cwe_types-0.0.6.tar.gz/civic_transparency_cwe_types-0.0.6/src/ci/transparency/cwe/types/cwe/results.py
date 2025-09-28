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

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field, replace
import re
from typing import TYPE_CHECKING, Any, TypedDict

if TYPE_CHECKING:
    from pathlib import Path

    from ci.transparency.cwe.types.batch import BatchResult

from ci.transparency.cwe.types.base import (
    BaseLoadingResult,
    BaseValidationResult,
    add_error,
    add_info,
    add_warning,
)

# ============================================================================
# Typed structures for CWE data
# ============================================================================


class CweRelationshipDict(TypedDict, total=False):
    """Typed structure for CWE relationship data."""

    cwe_id: str
    type: str
    description: str


class CweDataDict(TypedDict, total=False):
    """Typed structure for CWE data."""

    id: str
    name: str
    category: str
    description: str
    impact: str
    likelihood: str
    relationships: list[CweRelationshipDict]
    mitigation: str
    examples: list[str]
    references: list[str]


# ============================================================================
# Default factories (typed)
# ============================================================================


def _new_cwes() -> dict[str, CweDataDict]:
    """Typed default factory for CWE dictionary."""
    return {}


def _new_duplicate_ids() -> dict[str, list[Path]]:
    """Typed default factory for duplicate ID tracking."""
    return {}


def _new_validation_results() -> dict[str, bool]:
    """Typed default factory for validation results."""
    return {}


def _new_relationship_map() -> dict[str, list[str]]:
    """Typed default factory for relationship mapping."""
    return {}


def _new_relationship_types() -> dict[str, int]:
    """Typed default factory for relationship type counts (or severities)."""
    return {}


def _new_relationship_depths() -> dict[str, int]:
    """Typed default factory for relationship depths."""
    return {}


def _new_validation_details() -> dict[str, list[str]]:
    """Typed default factory for validation error details."""
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
    duplicate_ids: dict[str, list[Path]] = field(default_factory=_new_duplicate_ids)
    invalid_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()
    category_stats: dict[str, int] = field(default_factory=lambda: {})

    # ---- Derived properties ----

    @property
    def cwe_count(self) -> int:
        """Number of CWEs successfully loaded."""
        return len(self.cwes)

    @property
    def loaded_cwe_ids(self) -> tuple[str, ...]:
        """All loaded CWE IDs (sorted for stable output)."""
        return tuple(sorted(self.cwes.keys()))

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

    @property
    def category_count(self) -> int:
        """Number of distinct CWE categories."""
        return len(self.category_stats)

    # ---- Domain-neutral aliases (optional convenience) ----

    @property
    def definitions(self) -> dict[str, CweDataDict]:
        """CWE definitions loaded (alias for generic access)."""
        return self.cwes

    @property
    def cwe_definitions(self) -> dict[str, CweDataDict]:
        """CWE definitions loaded (explicit domain name)."""
        return self.cwes

    # ---- CWE access methods ----

    def get_cwe(self, cwe_id: str) -> CweDataDict | None:
        """Get CWE data by ID."""
        return self.cwes.get(cwe_id)

    def has_cwe(self, cwe_id: str) -> bool:
        """Check if a CWE ID was loaded."""
        return cwe_id in self.cwes

    def get_definition(self, cwe_id: str) -> CweDataDict | None:
        """Get CWE definition by ID (domain-specific alias)."""
        return self.get_cwe(cwe_id)

    def has_definition(self, cwe_id: str) -> bool:
        """Check if a CWE definition exists (domain-specific alias)."""
        return self.has_cwe(cwe_id)

    def get_cwe_ids(self) -> list[str]:
        """Get all CWE IDs."""
        return list(self.loaded_cwe_ids)

    def get_cwes_by_category(self, category: str) -> dict[str, CweDataDict]:
        """Get CWEs filtered by category."""
        return {
            cwe_id: cwe_data
            for cwe_id, cwe_data in self.cwes.items()
            if cwe_data.get("category") == category
        }

    def get_cwes_by_impact(self, impact: str) -> dict[str, CweDataDict]:
        """Get CWEs filtered by impact level."""
        return {
            cwe_id: cwe_data
            for cwe_id, cwe_data in self.cwes.items()
            if cwe_data.get("impact") == impact
        }

    def get_categories(self) -> list[str]:
        """Get all unique CWE categories."""
        return list(self.category_stats.keys())

    def get_most_common_category(self) -> str | None:
        """Get the category with the most CWEs."""
        if not self.category_stats:
            return None
        return max(self.category_stats, key=lambda k: self.category_stats[k])

    def search_cwes(self, search_term: str) -> dict[str, CweDataDict]:
        """Search CWEs by name or description."""
        search_lower = search_term.lower()
        return {
            cwe_id: cwe_data
            for cwe_id, cwe_data in self.cwes.items()
            if (
                search_lower in cwe_data.get("name", "").lower()
                or search_lower in cwe_data.get("description", "").lower()
            )
        }

    # ---- Conversion methods ----

    @classmethod
    def from_batch(cls, batch_result: BatchResult) -> CweLoadingResult:
        """Create CweLoadingResult from BatchResult.

        Args:
            batch_result: Batch loading result to convert

        Returns:
            CweLoadingResult with batch data mapped to CWE fields
        """
        # Calculate category statistics from loaded items
        category_stats: dict[str, int] = {}
        for item_data in batch_result.items.values():
            category = str(item_data.get("category", "unknown"))
            category_stats[category] = category_stats.get(category, 0) + 1

        return cls.from_result(
            batch_result,
            cwes=batch_result.items,  # type: ignore[arg-type]
            skipped_files=batch_result.skipped_files,
            category_stats=category_stats,
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
    validation_details: dict[str, list[str]] = field(default_factory=_new_validation_details)
    severity_counts: dict[str, int] = field(default_factory=_new_relationship_types)

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

    @property
    def validation_rate(self) -> float:
        """Validation success rate (0.0 to 1.0)."""
        if not self.validation_results:
            return 1.0
        passed = sum(self.validation_results.values())
        return passed / len(self.validation_results)

    # ---- Analysis methods ----

    def get_failed_cwes(self) -> list[str]:
        """Get list of CWE IDs that failed validation."""
        return [cwe_id for cwe_id, result in self.validation_results.items() if not result]

    def get_passed_cwes(self) -> list[str]:
        """Get list of CWE IDs that passed validation."""
        return [cwe_id for cwe_id, result in self.validation_results.items() if result]

    def get_validation_errors(self, cwe_id: str) -> list[str]:
        """Get validation errors for a specific CWE."""
        return self.validation_details.get(cwe_id, [])

    def get_most_common_errors(self, limit: int = 5) -> list[tuple[str, int]]:
        """Get most common validation errors."""
        error_counts: dict[str, int] = {}
        for errors in self.validation_details.values():
            for error in errors:
                error_counts[error] = error_counts.get(error, 0) + 1

        sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_errors[:limit]

    def get_error_summary(self) -> dict[str, Any]:
        """Get comprehensive error summary."""
        return {
            "total_errors": sum(len(errors) for errors in self.validation_details.values()),
            "cwes_with_errors": len([
                cwe for cwe, errors in self.validation_details.items() if errors
            ]),
            "most_common_errors": self.get_most_common_errors(),
            "severity_distribution": dict(self.severity_counts),
        }


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
    relationship_depths: dict[str, int] = field(default_factory=_new_relationship_depths)
    orphaned_cwes: tuple[str, ...] = ()
    invalid_references: tuple[str, ...] = ()
    relationship_types: dict[str, int] = field(default_factory=_new_relationship_types)
    circular_dependencies: tuple[str, ...] = ()

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

    @property
    def connected_cwe_count(self) -> int:
        """Number of CWEs with at least one relationship."""
        return len(self.relationship_map)

    @property
    def max_relationship_depth(self) -> int:
        """Maximum relationship depth in the graph."""
        return max(self.relationship_depths.values()) if self.relationship_depths else 0

    # ---- Relationship access ----

    def get_relationships(self, cwe_id: str) -> list[str]:
        """Get all relationships for a specific CWE."""
        return self.relationship_map.get(cwe_id, [])

    def get_relationship_depth(self, cwe_id: str) -> int:
        """Get relationship depth for a specific CWE."""
        return self.relationship_depths.get(cwe_id, 0)

    def get_related_cwes(self, cwe_id: str, max_depth: int = 1) -> set[str]:
        """Get all CWEs related to a given CWE up to max_depth."""
        related: set[str] = set()
        current_level: set[str] = {cwe_id}

        for _depth in range(max_depth):
            next_level: set[str] = set()
            for current_cwe in current_level:
                for related_cwe in self.get_relationships(current_cwe):
                    if related_cwe not in related and related_cwe != cwe_id:
                        related.add(related_cwe)
                        next_level.add(related_cwe)
            current_level = next_level
            if not current_level:
                break

        return related

    def find_relationship_path(self, from_cwe: str, to_cwe: str) -> list[str] | None:
        """Find shortest path between two CWEs."""
        return _find_shortest_path(self.relationship_map, from_cwe, to_cwe)

    def get_relationship_statistics(self) -> dict[str, Any]:
        """Get comprehensive relationship statistics."""
        return {
            "total_relationships": self.total_relationships,
            "connected_cwes": self.connected_cwe_count,
            "orphaned_cwes": self.orphaned_cwe_count,
            "circular_dependencies": self.circular_dependency_count,
            "invalid_references": self.invalid_reference_count,
            "relationship_types": dict(self.relationship_types),
            "max_depth": self.max_relationship_depth,
            "avg_relationships_per_cwe": (
                self.total_relationships / self.connected_cwe_count
                if self.connected_cwe_count > 0
                else 0
            ),
        }


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
    """Add successfully loaded CWE to the result."""
    # Check for duplicates
    if cwe_id in result.cwes:
        if file_path is not None:
            new_dup: dict[str, list[Path]] = dict(result.duplicate_ids)
            prev = new_dup.get(cwe_id, [])
            new_dup[cwe_id] = [*prev, file_path]
            result = replace(result, duplicate_ids=new_dup)
        result = add_warning(result, f"Duplicate CWE ID found: {cwe_id}")
        return replace(result, failed=result.failed + 1)

    # Update category statistics
    category = str(cwe_data.get("category", "unknown"))
    new_category_stats = {**result.category_stats}
    new_category_stats[category] = new_category_stats.get(category, 0) + 1

    # Add the CWE
    new_cwes = {**result.cwes, cwe_id: cwe_data}
    result = add_info(result, f"Loaded CWE {cwe_id}: {cwe_data.get('name', 'unnamed')}")

    return replace(
        result,
        cwes=new_cwes,
        category_stats=new_category_stats,
        loaded=result.loaded + 1,
    )


def track_duplicate_cwe(result: CweLoadingResult, cwe_id: str, file_path: Path) -> CweLoadingResult:
    """Track a duplicate CWE ID found in a file."""
    dup: dict[str, list[Path]] = dict(result.duplicate_ids)
    dup[cwe_id] = [*dup.get(cwe_id, []), file_path]
    return replace(
        add_warning(result, f"Duplicate CWE ID {cwe_id} in {file_path}"),
        duplicate_ids=dup,
        failed=result.failed + 1,
    )


def track_invalid_file(result: CweLoadingResult, file_path: Path, reason: str) -> CweLoadingResult:
    """Track an invalid CWE file."""
    result = add_error(result, f"Invalid CWE file {file_path}: {reason}")
    new_invalid = result.invalid_files + (file_path,)
    return replace(result, invalid_files=new_invalid, failed=result.failed + 1)


def track_skipped_cwe_file(
    result: CweLoadingResult,
    file_path: Path,
    reason: str,
) -> CweLoadingResult:
    """Track a skipped CWE file."""
    result = add_info(result, f"Skipped CWE file {file_path}: {reason}")
    new_skipped = result.skipped_files + (file_path,)
    return replace(result, skipped_files=new_skipped)


# ============================================================================
# CWE validation operations
# ============================================================================


def _raise_severity(current: str, candidate: str) -> str:
    """Return the higher-severity label according to _severity_order()."""
    return max(current, candidate, key=_severity_order)


def _validate_required_fields(cwe_data: CweDataDict) -> tuple[list[str], str]:
    """Validate required CWE fields: id, name, description (recommended)."""
    errors: list[str] = []
    severity: str = "info"

    cid = cwe_data.get("id")
    if not cid:
        errors.append("Missing required field: id")
        severity = "error"
    elif not _is_valid_cwe_id(str(cid)):
        errors.append(f"Invalid CWE ID format: {cid}")
        severity = "error"

    name = cwe_data.get("name")
    if not name:
        errors.append("Missing required field: name")
        severity = "error"
    elif len(str(name)) < 3:
        errors.append("CWE name too short (minimum 3 characters)")
        severity = _raise_severity(severity, "warning")

    desc = cwe_data.get("description")
    if not desc:
        errors.append("Missing recommended field: description")
        severity = _raise_severity(severity, "warning")
    elif len(str(desc)) < 10:
        errors.append("Description too short (minimum 10 characters)")
        severity = _raise_severity(severity, "warning")

    return errors, severity


def _validate_optional_fields(cwe_data: CweDataDict) -> tuple[list[str], str]:
    """Validate optional-but-constrained fields: category, impact."""
    errors: list[str] = []
    severity: str = "info"

    category = cwe_data.get("category")
    if category and not _is_valid_category(str(category)):
        errors.append(f"Invalid category: {category}")
        severity = _raise_severity(severity, "warning")

    impact = cwe_data.get("impact")
    if impact and not _is_valid_impact(str(impact)):
        errors.append(f"Invalid impact level: {impact}")
        severity = _raise_severity(severity, "warning")

    return errors, severity


def _validate_relationships(cwe_data: CweDataDict) -> tuple[list[str], str]:
    """Validate relationships: presence of cwe_id and its format."""
    errors: list[str] = []
    severity: str = "info"

    relationships = cwe_data.get("relationships", [])
    if relationships:
        for i, rel in enumerate(relationships):
            rel_id = rel.get("cwe_id")
            if not rel_id:
                errors.append(f"Relationship {i}: missing cwe_id")
                severity = _raise_severity(severity, "warning")
            elif not _is_valid_cwe_id(str(rel_id)):
                errors.append(f"Relationship {i}: invalid cwe_id format")
                severity = _raise_severity(severity, "warning")

    return errors, severity


def _max_severity(*labels: str) -> str:
    """Return the highest-severity label among the provided ones."""
    highest = "info"
    for lab in labels:
        highest = _raise_severity(highest, lab)
    return highest


def validate_cwe(
    result: CweValidationResult,
    cwe_id: str,
    cwe_data: CweDataDict,
) -> CweValidationResult:
    """Validate a CWE definition with comprehensive field validation."""
    req_errors, req_sev = _validate_required_fields(cwe_data)
    opt_errors, opt_sev = _validate_optional_fields(cwe_data)
    rel_errors, rel_sev = _validate_relationships(cwe_data)

    errors = req_errors + opt_errors + rel_errors
    severity = _max_severity(req_sev, opt_sev, rel_sev)
    is_valid = not errors

    # Record validation result
    new_results = {**result.validation_results, cwe_id: is_valid}
    new_validated = result.validated_cwes + (cwe_id,)
    new_details = {**result.validation_details}
    new_severity_counts = {**result.severity_counts}

    if errors:
        new_details[cwe_id] = errors
        new_severity_counts[severity] = new_severity_counts.get(severity, 0) + 1
        result = add_error(result, f"Validation failed for {cwe_id}: {len(errors)} issues")

    result = replace(
        result,
        validation_results=new_results,
        validated_cwes=new_validated,
        validation_details=new_details,
        severity_counts=new_severity_counts,
    )

    return (
        replace(result, passed=result.passed + 1)
        if is_valid
        else replace(result, failed=result.failed + 1)
    )


def validate_cwe_field(
    result: CweValidationResult,
    cwe_id: str,
    field_path: str,
    field_value: Any,
    validation_rule: str,
) -> CweValidationResult:
    """Validate a specific CWE field."""
    is_valid = True
    error_msg = ""

    if field_value is None:
        is_valid = False
        error_msg = f"Field {field_path} is required but missing"
    elif isinstance(field_value, str) and len(field_value.strip()) == 0:
        is_valid = False
        error_msg = f"Field {field_path} cannot be empty"
    elif field_path == "id" and (
        not isinstance(field_value, str) or not _is_valid_cwe_id(field_value)
    ):
        is_valid = False
        error_msg = f"Field {field_path} has invalid CWE ID format"

    if not is_valid:
        full_error_msg = (
            f"Field validation failed for {cwe_id}.{field_path}: {error_msg} ({validation_rule})"
        )
        result = add_error(result, full_error_msg)
        new_field_errors = result.field_errors + (f"{cwe_id}.{field_path}",)
        result = replace(result, field_errors=new_field_errors)
        return replace(result, failed=result.failed + 1)

    return replace(result, passed=result.passed + 1)


def batch_validate_cwes(
    result: CweValidationResult,
    cwe_dict: dict[str, CweDataDict],
) -> CweValidationResult:
    """Validate multiple CWEs in batch."""
    for cwe_id, cwe_data in cwe_dict.items():
        result = validate_cwe(result, cwe_id, cwe_data)
    return add_info(result, f"Batch validated {len(cwe_dict)} CWEs")


# ============================================================================
# CWE relationship operations
# ============================================================================


def analyze_relationships(
    result: CweRelationshipResult,
    cwe_dict: dict[str, CweDataDict],
) -> CweRelationshipResult:
    """Analyze CWE relationships for consistency and detect issues."""
    relationship_map: dict[str, list[str]] = {}
    relationship_types: dict[str, int] = {}
    invalid_references: list[str] = []
    orphaned_cwes: list[str] = []

    # Build relationship map
    for cwe_id, cwe_data in cwe_dict.items():
        relationships = cwe_data.get("relationships", [])
        related_ids: list[str] = []

        for relationship in relationships:
            related_id = relationship.get("cwe_id")
            rel_type = relationship.get("type", "unknown")

            if related_id:
                related_ids.append(str(related_id))
                relationship_types[rel_type] = relationship_types.get(rel_type, 0) + 1

                # Check if reference is valid
                if str(related_id) not in cwe_dict:
                    invalid_references.append(f"{cwe_id} → {related_id}")

        if related_ids:
            relationship_map[cwe_id] = related_ids
        else:
            orphaned_cwes.append(cwe_id)

    # Detect circular dependencies
    circular_deps = _detect_circular_dependencies(relationship_map)

    # Calculate relationship depths
    relationship_depths: dict[str, int] = {}
    for cid in cwe_dict:
        relationship_depths[cid] = _calculate_relationship_depth(relationship_map, cid, set())

    result = add_info(result, f"Analyzed relationships for {len(cwe_dict)} CWEs")
    if circular_deps:
        result = add_warning(result, f"Found {len(circular_deps)} CWEs in circular dependencies")
    if invalid_references:
        result = add_error(
            result, f"Found {len(invalid_references)} invalid relationship references"
        )

    return replace(
        result,
        relationship_map=relationship_map,
        relationship_types=relationship_types,
        relationship_depths=relationship_depths,
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
    """Add a relationship between two CWEs."""
    current_relationships = result.relationship_map.get(from_cwe, [])
    if to_cwe not in current_relationships:
        new_relationships = current_relationships + [to_cwe]
        new_map = {**result.relationship_map, from_cwe: new_relationships}
        new_types = {**result.relationship_types}
        new_types[relationship_type] = new_types.get(relationship_type, 0) + 1
        return replace(result, relationship_map=new_map, relationship_types=new_types)
    return result


# ============================================================================
# Analysis and reporting
# ============================================================================


def get_cwe_loading_summary(result: CweLoadingResult) -> dict[str, Any]:
    """Generate CWE loading summary."""
    return {
        "cwes_loaded": result.cwe_count,
        "successful_loads": result.loaded,
        "failed_loads": result.failed,
        "duplicate_ids": result.duplicate_count,
        "invalid_files": result.invalid_file_count,
        "skipped_files": result.skipped_file_count,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "loaded_cwe_ids": list(result.loaded_cwe_ids),
        "categories": result.get_categories(),
        "category_distribution": dict(result.category_stats),
        "most_common_category": result.get_most_common_category(),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
    }


def get_cwe_validation_summary(result: CweValidationResult) -> dict[str, Any]:
    """Generate CWE validation summary."""
    return {
        "cwes_validated": result.validated_count,
        "validation_passed": result.passed,
        "validation_failed": result.failed,
        "field_errors": result.field_error_count,
        "schema_validation_used": result.schema_validation_used,
        "schema_version": result.schema_version,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "validation_rate": round(result.validation_rate * 100, 2),
        "failed_cwes": result.get_failed_cwes(),
        "passed_cwes": result.get_passed_cwes(),
        "error_summary": result.get_error_summary(),
        "most_common_errors": result.get_most_common_errors(),
    }


def get_relationship_summary(result: CweRelationshipResult) -> dict[str, Any]:
    """Generate CWE relationship summary."""
    stats = result.get_relationship_statistics()
    return {
        "total_relationships": result.total_relationships,
        "connected_cwes": len(result.relationship_map),
        "relationship_types": dict(result.relationship_types),
        "circular_dependencies": list(result.circular_dependencies),
        "orphaned_cwes": list(result.orphaned_cwes),
        "invalid_references": list(result.invalid_references),
        "has_circular_dependencies": result.has_circular_dependencies,
        "has_orphaned_cwes": result.has_orphaned_cwes,
        "max_relationship_depth": result.max_relationship_depth,
        "relationship_statistics": stats,
        "invalid_reference_rate": (
            result.invalid_reference_count / result.total_relationships
            if result.total_relationships > 0
            else 0
        ),
    }


# ============================================================================
# Helpers (internal)
# ============================================================================


def _detect_circular_dependencies(relationship_map: dict[str, list[str]]) -> list[str]:
    """Detect circular dependencies in relationship map using DFS."""
    white, gray, black = 0, 1, 2
    color: dict[str, int] = defaultdict(lambda: white)
    circular_deps: set[str] = set()

    def dfs(node: str) -> bool:
        if color[node] == gray:
            # Back edge found - circular dependency
            return True
        if color[node] == black:
            return False

        color[node] = gray
        for neighbor in relationship_map.get(node, []):
            if dfs(neighbor):
                circular_deps.add(node)
                circular_deps.add(neighbor)
        color[node] = black
        return False

    for cwe_id in relationship_map:
        if color[cwe_id] == white:
            dfs(cwe_id)

    return list(circular_deps)


def _calculate_relationship_depth(
    relationship_map: dict[str, list[str]],
    cwe_id: str,
    visited: set[str],
) -> int:
    """Calculate relationship depth recursively with cycle detection."""
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


def _find_shortest_path(
    relationship_map: dict[str, list[str]],
    start: str,
    end: str,
) -> list[str] | None:
    """Find shortest path between two CWEs using BFS."""
    if start == end:
        return [start]

    queue: list[tuple[str, list[str]]] = [(start, [start])]
    visited: set[str] = {start}

    while queue:
        current, path = queue.pop(0)
        for neighbor in relationship_map.get(current, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def _is_valid_cwe_id(cwe_id: str) -> bool:
    """Validate CWE ID format."""
    # Pattern: CWE-[Letter][Number] (e.g., CWE-A001, CWE-B1234)
    pattern = r"^CWE-[A-Z]\d{3,4}$"
    return bool(re.match(pattern, cwe_id))


def _is_valid_category(category: str) -> bool:
    """Validate CWE category."""
    valid_categories = {
        "input_validation",
        "authentication",
        "authorization",
        "session_management",
        "cryptography",
        "error_handling",
        "code_quality",
        "race_conditions",
        "resource_management",
        "information_exposure",
        "injection",
        "path_traversal",
        "cross_site_scripting",
        "buffer_errors",
        "numeric_errors",
        "other",
    }
    return category.lower() in valid_categories


def _is_valid_impact(impact: str) -> bool:
    """Validate impact level."""
    valid_impacts = {"low", "medium", "high", "critical"}
    return impact.lower() in valid_impacts


def _severity_order(severity: str) -> int:
    """Get severity order for comparison."""
    order = {"info": 0, "warning": 1, "error": 2}
    return order.get(severity, 0)


# ============================================================================
# Public API
# ============================================================================

__all__ = [
    "CweLoadingResult",
    "CweValidationResult",
    "CweRelationshipResult",
    "CweRelationshipDict",
    "CweDataDict",
    # Loading ops
    "add_cwe",
    "track_duplicate_cwe",
    "track_invalid_file",
    "track_skipped_cwe_file",
    # Validation ops
    "validate_cwe",
    "validate_cwe_field",
    "batch_validate_cwes",
    # Relationship ops
    "analyze_relationships",
    "add_relationship",
    # Summaries
    "get_cwe_loading_summary",
    "get_cwe_validation_summary",
    "get_relationship_summary",
]
