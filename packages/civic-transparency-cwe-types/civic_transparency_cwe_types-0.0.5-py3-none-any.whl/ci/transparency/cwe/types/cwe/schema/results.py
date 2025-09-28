"""CWE schema result types and operations.

Immutable, slotted dataclasses for tracking CWE schema loading, validation,
and freeze detection operations. Built on base result types for consistent
count tracking and error handling.

Core types:
    - CweSchemaLoadingResult: Tracks CWE schema loading with version info
    - CweSchemaValidationResult: Tracks CWE data validation against schemas
    - CweSchemaFreezeResult: Tracks schema freeze violations and compatibility

Key operations:
    - load_cwe_schema: Load CWE schema with version detection
    - validate_cwe_data: Validate CWE data against loaded schemas
    - detect_schema_freeze: Detect breaking changes in schema updates

Design principles:
    - Immutable: uses dataclasses.replace for all modifications
    - CWE-specific: tailored for CWE schema requirements and patterns
    - Version-aware: tracks schema versions and compatibility
    - Validation-focused: CWE data validation tracking
"""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base import (
    BaseLoadingResult,
    BaseValidationResult,
    add_error,
    add_info,
    add_warning,
)


def _new_schemas() -> dict[str, dict[str, Any]]:
    """Typed default factory for schemas dictionary."""
    return {}


def _new_validation_results() -> dict[str, bool]:
    """Typed default factory for validation results."""
    return {}


def _new_freeze_violations() -> tuple[str, ...]:
    """Typed default factory for freeze violations."""
    return ()


def _new_schema_versions() -> dict[str, str]:
    """Typed default factory for schema versions."""
    return {}


@dataclass(frozen=True, slots=True)
class CweSchemaLoadingResult(BaseLoadingResult):
    """Result from CWE schema loading operations.

    Tracks loaded CWE schemas, version information, and schema-specific
    metadata. Extends BaseLoadingResult to provide loaded/failed counts
    and conversion protocol.
    """

    schemas: dict[str, dict[str, Any]] = field(default_factory=_new_schemas)
    schema_versions: dict[str, str] = field(default_factory=_new_schema_versions)
    schema_files: tuple[Path, ...] = ()
    unsupported_versions: tuple[str, ...] = ()

    # ---- Derived metrics for schema loading ----

    @property
    def schema_count(self) -> int:
        """Number of schemas successfully loaded."""
        return len(self.schemas)

    @property
    def version_count(self) -> int:
        """Number of distinct schema versions loaded."""
        return len(set(self.schema_versions.values()))

    @property
    def has_schemas(self) -> bool:
        """True if any schemas were successfully loaded."""
        return bool(self.schemas)

    @property
    def has_unsupported_versions(self) -> bool:
        """True if any unsupported schema versions were encountered."""
        return bool(self.unsupported_versions)

    # ---- Schema analysis ----

    def get_schemas_by_version(self, version: str) -> list[str]:
        """Get schema names for a specific version.

        Args:
            version: Schema version to filter by

        Returns:
            List of schema names using the specified version
        """
        return [name for name, ver in self.schema_versions.items() if ver == version]

    def get_latest_version(self) -> str | None:
        """Get the latest schema version loaded.

        Returns:
            Latest schema version string, or None if no schemas loaded
        """
        if not self.schema_versions:
            return None
        return max(self.schema_versions.values())

    def has_schema(self, schema_name: str) -> bool:
        """Check if a specific schema was loaded.

        Args:
            schema_name: Name of the schema to check

        Returns:
            True if the schema was successfully loaded
        """
        return schema_name in self.schemas


@dataclass(frozen=True, slots=True)
class CweSchemaValidationResult(BaseValidationResult):
    """Result from CWE data validation against schemas.

    Tracks CWE validation results, field-level errors, and validation
    statistics. Extends BaseValidationResult for passed/failed counts.
    """

    validation_results: dict[str, bool] = field(default_factory=_new_validation_results)
    field_errors: tuple[str, ...] = ()
    validated_cwes: tuple[str, ...] = ()
    schema_name: str = ""

    # ---- Derived metrics for validation ----

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

    # ---- Validation analysis ----

    def get_failed_cwes(self) -> list[str]:
        """Get list of CWE IDs that failed validation.

        Returns:
            List of CWE IDs that failed schema validation
        """
        return [cwe_id for cwe_id, result in self.validation_results.items() if not result]

    def get_passed_cwes(self) -> list[str]:
        """Get list of CWE IDs that passed validation.

        Returns:
            List of CWE IDs that passed schema validation
        """
        return [cwe_id for cwe_id, result in self.validation_results.items() if result]

    def get_validation_rate_by_schema(self) -> float:
        """Get validation success rate for this schema.

        Returns:
            Float in [0, 1] representing validation success rate
        """
        if not self.validation_results:
            return 1.0
        passed = sum(self.validation_results.values())
        return passed / len(self.validation_results)


@dataclass(frozen=True, slots=True)
class CweSchemaFreezeResult(BaseValidationResult):
    """Result from CWE schema freeze detection.

    Tracks schema freeze violations, breaking changes, and compatibility
    analysis between schema versions.
    """

    freeze_violations: tuple[str, ...] = field(default_factory=_new_freeze_violations)
    breaking_changes: tuple[str, ...] = ()
    compatible_changes: tuple[str, ...] = ()
    old_schema_version: str = ""
    new_schema_version: str = ""

    # ---- Derived metrics for freeze analysis ----

    @property
    def violation_count(self) -> int:
        """Number of schema freeze violations detected."""
        return len(self.freeze_violations)

    @property
    def breaking_change_count(self) -> int:
        """Number of breaking changes detected."""
        return len(self.breaking_changes)

    @property
    def compatible_change_count(self) -> int:
        """Number of compatible changes detected."""
        return len(self.compatible_changes)

    @property
    def has_violations(self) -> bool:
        """True if any schema freeze violations were detected."""
        return bool(self.freeze_violations)

    @property
    def has_breaking_changes(self) -> bool:
        """True if any breaking changes were detected."""
        return bool(self.breaking_changes)

    @property
    def is_compatible(self) -> bool:
        """True if schema changes are backward compatible."""
        return not self.has_breaking_changes

    # ---- Compatibility analysis ----

    def get_compatibility_summary(self) -> dict[str, Any]:
        """Get summary of schema compatibility analysis.

        Returns:
            Dictionary with compatibility analysis results
        """
        return {
            "is_compatible": self.is_compatible,
            "freeze_violations": self.violation_count,
            "breaking_changes": self.breaking_change_count,
            "compatible_changes": self.compatible_change_count,
            "old_version": self.old_schema_version,
            "new_version": self.new_schema_version,
            "overall_assessment": self.get_overall_assessment(),
        }

    def get_overall_assessment(self) -> str:
        """Get overall assessment of schema changes."""
        if self.has_violations:
            return "freeze_violated"
        if self.has_breaking_changes:
            return "breaking_changes"
        if self.compatible_change_count > 0:
            return "compatible_changes"
        return "no_changes"


# ============================================================================
# Schema loading operations
# ============================================================================


def load_cwe_schema[R: CweSchemaLoadingResult](
    result: R,
    schema_name: str,
    schema_data: dict[str, Any],
    *,
    file_path: Path,
    version: str | None = None,
) -> R:
    """Load a CWE schema with version detection.

    Args:
        result: The schema loading result to update
        schema_name: Name/identifier for the schema
        schema_data: The parsed schema data
        file_path: Path to the schema file
        version: Optional explicit version (detected if not provided)

    Returns:
        New result with schema loaded and metadata updated
    """
    # Detect version if not provided
    if version is None:
        version = _detect_schema_version(schema_data)

    new_schemas = {**result.schemas, schema_name: schema_data}
    new_versions = {**result.schema_versions, schema_name: version}
    new_files = result.schema_files + (file_path,)

    return replace(
        result,
        schemas=new_schemas,
        schema_versions=new_versions,
        schema_files=new_files,
        loaded=result.loaded + 1,
    )


def add_schema_version[R: CweSchemaLoadingResult](result: R, schema_name: str, version: str) -> R:
    """Add or update schema version information.

    Args:
        result: The schema loading result to update
        schema_name: Name of the schema
        version: Version string to associate with the schema

    Returns:
        New result with version information updated
    """
    new_versions = {**result.schema_versions, schema_name: version}
    return replace(result, schema_versions=new_versions)


def track_unsupported_version[R: CweSchemaLoadingResult](result: R, version: str, reason: str) -> R:
    """Track an unsupported schema version.

    Args:
        result: The schema loading result to update
        version: The unsupported version
        reason: Reason why the version is unsupported

    Returns:
        New result with unsupported version tracked and warning added
    """
    result = add_warning(result, f"Unsupported schema version {version}: {reason}")
    new_unsupported = result.unsupported_versions + (version,)

    return replace(
        result,
        unsupported_versions=new_unsupported,
        failed=result.failed + 1,
    )


def track_schema_usage[R: CweSchemaLoadingResult](result: R, schema_name: str) -> R:
    """Track usage of a loaded schema.

    Args:
        result: The schema loading result to update
        schema_name: Name of the schema being used

    Returns:
        New result with usage information updated (could track usage counts in future)
    """
    # For now, just add info message about schema usage
    return add_info(result, f"Schema {schema_name} used for validation")


# ============================================================================
# Schema validation operations
# ============================================================================


def validate_cwe_data[R: CweSchemaValidationResult](
    result: R, cwe_id: str, cwe_data: dict[str, Any], schema: dict[str, Any], schema_name: str = ""
) -> R:
    """Validate CWE data against a schema.

    Args:
        result: The validation result to update
        cwe_id: ID of the CWE being validated
        cwe_data: CWE data to validate
        schema: JSON schema to validate against
        schema_name: Optional name of the schema being used

    Returns:
        New result with validation outcome recorded
    """
    # Perform validation (simplified - real implementation would use jsonschema)
    is_valid = _validate_against_schema(cwe_data, schema)

    new_results = {**result.validation_results, cwe_id: is_valid}
    new_validated = result.validated_cwes + (cwe_id,)

    result_with_data = replace(
        result,
        validation_results=new_results,
        validated_cwes=new_validated,
        schema_name=schema_name or result.schema_name,
    )

    if is_valid:
        return replace(result_with_data, passed=result_with_data.passed + 1)
    return replace(result_with_data, failed=result_with_data.failed + 1)


def validate_cwe_field[R: CweSchemaValidationResult](
    result: R, field_path: str, field_value: Any, field_schema: dict[str, Any]
) -> R:
    """Validate a specific CWE field against its schema.

    Args:
        result: The validation result to update
        field_path: Path to the field (e.g., "relationships[0].id")
        field_value: Value of the field
        field_schema: Schema for the specific field

    Returns:
        New result with field validation outcome recorded
    """
    # Perform field-level validation
    is_valid = _validate_field_against_schema(field_value, field_schema)

    if not is_valid:
        error_msg = f"Field validation failed: {field_path}"
        result = add_error(result, error_msg)
        new_field_errors = result.field_errors + (field_path,)
        result = replace(result, field_errors=new_field_errors)

    return result


def batch_validate_cwes[R: CweSchemaValidationResult](
    result: R,
    cwe_data_dict: dict[str, dict[str, Any]],
    schema: dict[str, Any],
    schema_name: str = "",
) -> R:
    """Validate multiple CWEs against a schema in batch.

    Args:
        result: The validation result to update
        cwe_data_dict: Dictionary of CWE ID -> CWE data
        schema: JSON schema to validate against
        schema_name: Optional name of the schema being used

    Returns:
        New result with all validation outcomes recorded
    """
    for cwe_id, cwe_data in cwe_data_dict.items():
        result = validate_cwe_data(result, cwe_id, cwe_data, schema, schema_name)

    return result


# ============================================================================
# Schema freeze detection operations
# ============================================================================


def detect_schema_freeze[R: CweSchemaFreezeResult](
    result: R,
    old_schema: dict[str, Any],
    new_schema: dict[str, Any],
    old_version: str = "",
    new_version: str = "",
) -> R:
    """Detect schema freeze violations between two schema versions.

    Args:
        result: The freeze result to update
        old_schema: Previous schema version
        new_schema: New schema version
        old_version: Optional version string for old schema
        new_version: Optional version string for new schema

    Returns:
        New result with freeze analysis performed
    """
    # Analyze schema changes
    violations = _detect_freeze_violations(old_schema, new_schema)
    breaking_changes = _detect_breaking_changes(old_schema, new_schema)
    compatible_changes = _detect_compatible_changes(old_schema, new_schema)

    return replace(
        result,
        freeze_violations=violations,
        breaking_changes=breaking_changes,
        compatible_changes=compatible_changes,
        old_schema_version=old_version,
        new_schema_version=new_version,
        passed=result.passed + (1 if not violations else 0),
        failed=result.failed + (1 if violations else 0),
    )


def check_schema_compatibility[R: CweSchemaFreezeResult](
    result: R, schema1: dict[str, Any], schema2: dict[str, Any]
) -> R:
    """Check compatibility between two schemas.

    Args:
        result: The freeze result to update
        schema1: First schema to compare
        schema2: Second schema to compare

    Returns:
        New result with compatibility analysis performed
    """
    return detect_schema_freeze(result, schema1, schema2)


def analyze_schema_changes[R: CweSchemaFreezeResult](
    result: R, old_schema: dict[str, Any], new_schema: dict[str, Any]
) -> R:
    """Perform analysis of schema changes.

    Args:
        result: The freeze result to update
        old_schema: Previous schema version
        new_schema: New schema version

    Returns:
        New result with change analysis
    """
    result = detect_schema_freeze(result, old_schema, new_schema)

    # Add informational messages about the analysis
    if result.compatible_change_count > 0:
        result = add_info(result, f"Found {result.compatible_change_count} compatible changes")

    if result.breaking_change_count > 0:
        result = add_warning(result, f"Found {result.breaking_change_count} breaking changes")

    return result


# ============================================================================
# Analysis and reporting functions
# ============================================================================


def get_schema_loading_summary(result: CweSchemaLoadingResult) -> dict[str, Any]:
    """Generate schema loading summary.

    Args:
        result: The schema loading result to summarize

    Returns:
        Dictionary with detailed schema loading statistics
    """
    return {
        "schemas_loaded": result.schema_count,
        "files_processed": len(result.schema_files),
        "schema_versions": dict(result.schema_versions),
        "unique_versions": result.version_count,
        "unsupported_versions": list(result.unsupported_versions),
        "latest_version": result.get_latest_version(),
        "success_rate_percent": round(result.success_rate * 100, 2),
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
    }


def get_validation_summary(result: CweSchemaValidationResult) -> dict[str, Any]:
    """Generate validation summary.

    Args:
        result: The validation result to summarize

    Returns:
        Dictionary with detailed validation statistics
    """
    return {
        "cwes_validated": result.validated_count,
        "validation_passed": result.passed,
        "validation_failed": result.failed,
        "field_errors": result.field_error_count,
        "schema_used": result.schema_name,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "failed_cwes": result.get_failed_cwes(),
        "passed_cwes": result.get_passed_cwes(),
        "has_field_errors": result.has_field_errors,
    }


def get_freeze_analysis(result: CweSchemaFreezeResult) -> dict[str, Any]:
    """Generate freeze analysis summary.

    Args:
        result: The freeze result to summarize

    Returns:
        Dictionary with detailed freeze analysis
    """
    return {
        "freeze_status": result.get_overall_assessment(),
        "is_compatible": result.is_compatible,
        "freeze_violations": list(result.freeze_violations),
        "breaking_changes": list(result.breaking_changes),
        "compatible_changes": list(result.compatible_changes),
        "violation_count": result.violation_count,
        "breaking_change_count": result.breaking_change_count,
        "compatible_change_count": result.compatible_change_count,
        "version_comparison": {
            "old": result.old_schema_version,
            "new": result.new_schema_version,
        },
        "compatibility_summary": result.get_compatibility_summary(),
    }


# ============================================================================
# Internal helper functions
# ============================================================================


def _detect_schema_version(schema_data: dict[str, Any]) -> str:
    """Detect schema version from schema data."""
    # Look for common version indicators
    if "$id" in schema_data and "v" in schema_data["$id"]:
        return schema_data["$id"].split("v")[-1]
    if "version" in schema_data:
        return str(schema_data["version"])
    return "unknown"


def _validate_against_schema(data: dict[str, Any], schema: dict[str, Any]) -> bool:
    """Validate data against schema (simplified implementation)."""
    # In a real implementation, this would use jsonschema library
    # For now, return True as placeholder
    return True


def _validate_field_against_schema(field_value: Any, field_schema: dict[str, Any]) -> bool:
    """Validate field value against field schema (simplified implementation)."""
    # In a real implementation, this would perform detailed field validation
    # For now, return True as placeholder
    return True


def _detect_freeze_violations(
    old_schema: dict[str, Any], new_schema: dict[str, Any]
) -> tuple[str, ...]:
    """Detect schema freeze violations (simplified implementation)."""
    # In a real implementation, this would analyze schema changes for freeze violations
    return ()


def _detect_breaking_changes(
    old_schema: dict[str, Any], new_schema: dict[str, Any]
) -> tuple[str, ...]:
    """Detect breaking changes between schemas (simplified implementation)."""
    # In a real implementation, this would identify breaking changes
    return ()


def _detect_compatible_changes(
    old_schema: dict[str, Any], new_schema: dict[str, Any]
) -> tuple[str, ...]:
    """Detect compatible changes between schemas (simplified implementation)."""
    # In a real implementation, this would identify non-breaking changes
    return ()
