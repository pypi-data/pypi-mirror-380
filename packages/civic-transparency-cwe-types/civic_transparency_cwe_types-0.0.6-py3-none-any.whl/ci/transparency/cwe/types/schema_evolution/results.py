"""Schema evolution (freeze/compatibility) result types.

Domain-neutral result holders for comparing two schemas across versions.
Provide a compact diff representation and an aggregate evolution report.

Design principles:
    - Attribute-only data holders (engines add behavior)
    - Consistent shape for consumption by higher-level workflows
    - Minimal memory footprint with __slots__
    - Compatible with functional transformations

Core schema evolution results:
    - SchemaDiff: Structural summary of added/removed/changed elements
    - SchemaEvolutionReport: Aggregated outcome (ok/errors/warnings/diff/versions)

Typical usage:
    from ci.transparency.cwe.types.schema_evolution.results import SchemaEvolutionReport

    report = SchemaEvolutionReport(
        ok=False,
        errors=[...],
        warnings=[],
        diff=SchemaDiff(added=["/items/description"], changed=["/id:type"]),
        old_version="2.0",
        new_version="2.1",
    )
"""

from dataclasses import dataclass

from ci.transparency.cwe.types.base.results import BaseValidationResult


class SchemaDiff:
    """Structural diff between two schema versions."""

    __slots__ = ("added", "removed", "changed")

    # Explicit annotations for pyright strict
    added: list[str]
    removed: list[str]
    changed: list[str]

    def __init__(
        self,
        added: list[str] | None = None,
        removed: list[str] | None = None,
        changed: list[str] | None = None,
    ) -> None:
        """Initialize a schema diff.

        Args:
            added: Optional list of added schema paths/keys
            removed: Optional list of removed schema paths/keys
            changed: Optional list of changed schema paths/keys
        """
        self.added = added or []
        self.removed = removed or []
        self.changed = changed or []


@dataclass(frozen=True, slots=True, init=False)
class SchemaEvolutionReport(BaseValidationResult):
    """Aggregate result of a schema evolution (freeze/compatibility) check."""

    diff: SchemaDiff | None = None
    old_version: str | None = None
    new_version: str | None = None

    def __init__(
        self,
        *,
        ok: bool,
        errors: list[str] | tuple[str, ...] | None = None,
        warnings: list[str] | tuple[str, ...] | None = None,
        infos: list[str] | tuple[str, ...] | None = None,
        diff: SchemaDiff | None = None,
        old_version: str | None = None,
        new_version: str | None = None,
    ) -> None:
        """Initialize a schema evolution report.

        Args:
            ok: Whether evolution checks passed
            errors: Optional list/tuple of evolution errors
            warnings: Optional list/tuple of non-fatal issues
            infos: Optional list/tuple of informational messages
            diff: Optional structural diff summary
            old_version: Optional identifier for the old schema version
            new_version: Optional identifier for the new schema version
        """
        # Map `ok` ➜ BaseValidationResult's (passed, failed) and normalize messages
        BaseValidationResult.__init__(  # type: ignore[misc]
            self,
            passed=1 if ok else 0,
            failed=0 if ok else 1,
            errors=tuple(errors) if errors is not None else (),
            warnings=tuple(warnings) if warnings is not None else (),
            infos=tuple(infos) if infos is not None else (),
        )
        # Assign our own slotted fields in a frozen dataclass
        object.__setattr__(self, "diff", diff)
        object.__setattr__(self, "old_version", old_version)
        object.__setattr__(self, "new_version", new_version)


# Public API (alphabetical)
__all__ = [
    "SchemaDiff",
    "SchemaEvolutionReport",
]
