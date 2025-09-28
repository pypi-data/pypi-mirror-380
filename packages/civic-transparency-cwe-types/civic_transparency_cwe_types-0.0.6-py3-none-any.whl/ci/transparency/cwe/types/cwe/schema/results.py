"""CWE schema result types for loading and validation.

Domain-specific result holders used by CWE schema loading/parsing and
CWE instance-vs-schema validation. Lightweight data containers that
compose cleanly with higher-level workflows.

Design principles:
    - Attribute-only data holders (no external dependencies)
    - Consistent shape across loading and validation operations
    - Minimal memory footprint with __slots__
    - Friendly to functional updates and transformations

Core CWE schema results:
    - CweSchemaLoadingResult: Outcome of loading/parsing a CWE schema
    - CweSchemaValidationResult: Outcome of validating CWE data against a schema
"""

from dataclasses import dataclass

from ci.transparency.cwe.types.schema.results import SchemaLoadingResult, SchemaValidationResult


@dataclass(frozen=True, slots=True, init=False)
class CweSchemaLoadingResult(SchemaLoadingResult):
    """Result of loading/parsing a CWE schema."""

    # Inherits schema_name/schema_version from base; no extra fields

    def __init__(
        self,
        *,
        ok: bool,
        errors: list[str] | tuple[str, ...] | None = None,
        warnings: list[str] | tuple[str, ...] | None = None,
        infos: list[str] | tuple[str, ...] | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
    ) -> None:
        """Initialize a CweSchemaLoadingResult with loading outcome details.

        Args:
            ok (bool): Whether loading was successful.
            errors (list[str] | tuple[str, ...] | None): List of error messages.
            warnings (list[str] | tuple[str, ...] | None): List of warning messages.
            infos (list[str] | tuple[str, ...] | None): List of informational messages.
            schema_name (str | None): Name of the schema.
            schema_version (str | None): Version of the schema.
        """
        SchemaLoadingResult.__init__(
            self,
            ok=ok,
            errors=errors,
            warnings=warnings,
            infos=infos,
            schema_name=schema_name,
            schema_version=schema_version,
        )


@dataclass(frozen=True, slots=True, init=False)
class CweSchemaValidationResult(SchemaValidationResult):
    """Result of validating CWE data against a schema."""

    cwe_id: str | None = None
    field_path: str | None = None

    def __init__(
        self,
        *,
        ok: bool,
        errors: list[str] | tuple[str, ...] | None = None,
        warnings: list[str] | tuple[str, ...] | None = None,
        infos: list[str] | tuple[str, ...] | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        cwe_id: str | None = None,
        field_path: str | None = None,
    ) -> None:
        """Initialize a CweSchemaValidationResult with validation outcome details.

        Args:
            ok (bool): Whether validation was successful.
            errors (list[str] | tuple[str, ...] | None): List of error messages.
            warnings (list[str] | tuple[str, ...] | None): List of warning messages.
            infos (list[str] | tuple[str, ...] | None): List of informational messages.
            schema_name (str | None): Name of the schema.
            schema_version (str | None): Version of the schema.
            cwe_id (str | None): CWE identifier.
            field_path (str | None): Path to the field being validated.
        """
        SchemaValidationResult.__init__(
            self,
            ok=ok,
            errors=errors,
            warnings=warnings,
            infos=infos,
            schema_name=schema_name,
            schema_version=schema_version,
            instance_summary=None,
        )
        object.__setattr__(self, "cwe_id", cwe_id)
        object.__setattr__(self, "field_path", field_path)


__all__ = ["CweSchemaLoadingResult", "CweSchemaValidationResult"]
