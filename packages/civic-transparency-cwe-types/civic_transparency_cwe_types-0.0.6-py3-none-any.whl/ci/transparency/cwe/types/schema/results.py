"""Schema result types for loading and validation.

Domain-neutral result holders used by schema loading/parsing and instance
validation operations. These are lightweight data containers designed to
compose cleanly with higher-level workflows.

Design principles:
    - Attribute-only data holders (no external dependencies)
    - Consistent shape across loading and validation operations
    - Minimal memory footprint with __slots__
    - Friendly to functional updates and transformations

Core schema results:
    - SchemaLoadingResult: Outcome of loading/parsing a schema
    - SchemaValidationResult: Outcome of validating an instance against a schema
"""

from dataclasses import dataclass

from ci.transparency.cwe.types.base.results import BaseLoadingResult, BaseValidationResult


@dataclass(frozen=True, slots=True, init=False)
class SchemaLoadingResult(BaseLoadingResult):
    """Result of loading/parsing a schema."""

    schema_name: str | None = None
    schema_version: str | None = None

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
        """Initialize SchemaLoadingResult with schema metadata and result status.

        Args:
            ok (bool): Whether loading/parsing succeeded.
            errors (list[str] | tuple[str, ...] | None): Error messages.
            warnings (list[str] | tuple[str, ...] | None): Warning messages.
            infos (list[str] | tuple[str, ...] | None): Informational messages.
            schema_name (str | None): Name of the schema.
            schema_version (str | None): Version of the schema.
        """
        # Initialize the frozen BaseLoadingResult with normalized messages
        BaseLoadingResult.__init__(  # type: ignore[misc]
            self,
            loaded=1 if ok else 0,
            failed=0 if ok else 1,
            errors=tuple(errors) if errors is not None else (),
            warnings=tuple(warnings) if warnings is not None else (),
            infos=tuple(infos) if infos is not None else (),
        )
        # Assign our own slotted fields in a frozen dataclass
        object.__setattr__(self, "schema_name", schema_name)
        object.__setattr__(self, "schema_version", schema_version)


@dataclass(frozen=True, slots=True, init=False)
class SchemaValidationResult(BaseValidationResult):
    """Result of validating an instance against a schema."""

    schema_name: str | None = None
    schema_version: str | None = None
    instance_summary: str | None = None

    def __init__(
        self,
        *,
        ok: bool,
        errors: list[str] | tuple[str, ...] | None = None,
        warnings: list[str] | tuple[str, ...] | None = None,
        infos: list[str] | tuple[str, ...] | None = None,
        schema_name: str | None = None,
        schema_version: str | None = None,
        instance_summary: str | None = None,
    ) -> None:
        """Initialize SchemaValidationResult with schema and instance metadata and result status.

        Args:
            ok (bool): Whether validation succeeded.
            errors (list[str] | tuple[str, ...] | None): Error messages.
            warnings (list[str] | tuple[str, ...] | None): Warning messages.
            infos (list[str] | tuple[str, ...] | None): Informational messages.
            schema_name (str | None): Name of the schema.
            schema_version (str | None): Version of the schema.
            instance_summary (str | None): Summary of the validated instance.
        """
        # Initialize the frozen BaseValidationResult with normalized messages
        BaseValidationResult.__init__(  # type: ignore[misc]
            self,
            passed=1 if ok else 0,
            failed=0 if ok else 1,
            errors=tuple(errors) if errors is not None else (),
            warnings=tuple(warnings) if warnings is not None else (),
            infos=tuple(infos) if infos is not None else (),
        )
        # Assign our own slotted fields in a frozen dataclass
        object.__setattr__(self, "schema_name", schema_name)
        object.__setattr__(self, "schema_version", schema_version)
        object.__setattr__(self, "instance_summary", instance_summary)


__all__ = ["SchemaLoadingResult", "SchemaValidationResult"]
