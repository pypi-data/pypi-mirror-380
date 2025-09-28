"""Tests for domain-neutral schema evolution error types and result operations.

Covers SchemaDiff / SchemaEvolutionReport plus basic construction and behavior
of schema-evolution error types (freeze/compat/ breaking-change).
"""


import pytest

from ci.transparency.cwe.types.schema_evolution.errors import (
    SchemaBreakingChangeError,
    SchemaCompatibilityError,
    SchemaFreezeError,
    SchemaFreezeViolationError,
)

from ci.transparency.cwe.types.schema_evolution.results import (
    SchemaDiff,
    SchemaEvolutionReport,
)


# --------------------------------------------------------------------------------------
# Results: SchemaDiff
# --------------------------------------------------------------------------------------


def test_schema_diff_init_and_attributes() -> None:
    diff = SchemaDiff(
        added=["/properties/name", "/definitions/id"],
        removed=["/properties/legacy"],
        changed=["/properties/type"],
    )

    assert isinstance(diff, SchemaDiff)
    assert diff.added == ["/properties/name", "/definitions/id"]
    assert diff.removed == ["/properties/legacy"]
    assert diff.changed == ["/properties/type"]


def test_schema_diff_defaults_are_independent_lists() -> None:
    d1 = SchemaDiff()
    d2 = SchemaDiff()
    # Mutate one and ensure the other is untouched (defensive defaulting)
    d1.added.append("/x")
    assert d1.added == ["/x"]
    assert d2.added == []


# --------------------------------------------------------------------------------------
# Results: SchemaEvolutionReport (BaseValidationResult semantics)
# --------------------------------------------------------------------------------------


def test_schema_evolution_report_success_ok_true() -> None:
    rep = SchemaEvolutionReport(
        ok=True,
        errors=None,
        warnings=None,
        diff=SchemaDiff(added=["/a"]),
        old_version="1.0",
        new_version="1.1",
    )

    assert isinstance(rep, SchemaEvolutionReport)
    # Passed/failed wiring mirrors BaseValidationResult semantics
    assert rep.passed == 1
    assert rep.failed == 0
    assert rep.success_rate == 1.0
    assert rep.errors == ()
    assert rep.warnings == ()
    assert rep.infos == ()
    assert isinstance(rep.diff, SchemaDiff)
    assert rep.old_version == "1.0"
    assert rep.new_version == "1.1"


def test_schema_evolution_report_failure_ok_false_with_messages() -> None:
    rep = SchemaEvolutionReport(
        ok=False,
        errors=["breaking: removed /id"],
        warnings=["renamed /title -> /name"],
        diff=SchemaDiff(removed=["/id"], changed=["/title"]),
        old_version="2.0",
        new_version="3.0",
    )

    assert rep.passed == 0
    assert rep.failed == 1
    assert rep.success_rate == 0.0
    # Inputs normalized to tuples
    assert rep.errors == ("breaking: removed /id",)
    assert rep.warnings == ("renamed /title -> /name",)
    assert isinstance(rep.diff, SchemaDiff)
    assert rep.old_version == "2.0"
    assert rep.new_version == "3.0"


# --------------------------------------------------------------------------------------
# Errors: basic construction and context
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "err_cls",
    [
        SchemaFreezeError,
        SchemaFreezeViolationError,
        SchemaCompatibilityError,
        SchemaBreakingChangeError,
    ],
)
def test_errors_construct_and_stringify(err_cls: type) -> None:
    # Only rely on the required "message" parameter to avoid coupling to
    # optional kwargs that may evolve. All our error types are Exception subclasses.
    e = err_cls("boom")
    assert isinstance(e, Exception)

    # __str__ should include the message
    s = str(e)
    assert "boom" in s

    # If the error type implements context parts, it should return a list
    get_ctx = getattr(e, "get_context_parts", None)
    if callable(get_ctx):
        parts = get_ctx()
        assert isinstance(parts, list)
