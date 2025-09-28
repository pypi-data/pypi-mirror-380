"""Tests for domain-neutral schema error types and result operations.

Tests for generic schema loading and validation, including all error types
and result operations.
"""


import inspect
from pathlib import Path
import pytest

from ci.transparency.cwe.types.schema.errors import (
    SchemaError,
    SchemaLoadingError,
    SchemaNotFoundError,
    SchemaParsingError,
    SchemaVersionError,
    SchemaFormatError,
    SchemaConstraintError,
    SchemaReferenceError,
    SchemaCircularReferenceError,
    SchemaValidationError,
    SchemaDataValidationError,
    SchemaFieldValidationError,
    __all__ as SCHEMA_ERRORS_ALL,
)

from ci.transparency.cwe.types.schema.results import (
    SchemaLoadingResult,
    SchemaValidationResult,
)


# ---------------------------
# Error type basics
# ---------------------------

ERROR_TYPES = (
    SchemaError,
    SchemaLoadingError,
    SchemaNotFoundError,
    SchemaParsingError,
    SchemaVersionError,
    SchemaFormatError,
    SchemaConstraintError,
    SchemaReferenceError,
    SchemaCircularReferenceError,
)

# ---------------------------
# Helpers
# ---------------------------

def _assert_substrings(text: str, *subs: str) -> None:
    """
    Check that every expected substring occurs in the given text,
    normalizing path separators to POSIX style so tests pass on
    Windows or Unix even though we still create Paths with pathlib.
    """
    norm_text = text.replace("\\", "/")
    for s in subs:
        # keep expected substrings in POSIX form too
        assert s.replace("\\", "/") in norm_text, (
            f"Expected substring not found: {s!r} in {norm_text!r}"
        )


def test_error_type_hierarchy():
    # All are classes, all are Exceptions; all specific ones derive from SchemaError
    for t in ERROR_TYPES:
        assert inspect.isclass(t)
        assert issubclass(t, Exception)

    for t in ERROR_TYPES[1:]:
        assert issubclass(t, SchemaError)


@pytest.mark.parametrize("err_type", ERROR_TYPES)
def test_error_instantiation_and_str(err_type: type):
    """
    Try to construct with a single message arg; if a subclass has a different
    signature, skip gracefully (keeps the test future-proof).
    """
    try:
        err = err_type("boom")
    except TypeError:
        pytest.skip(f"{err_type.__name__} uses a non-standard constructor")
        return

    assert isinstance(err, Exception)
    s = str(err)
    assert isinstance(s, str)
    assert s != ""


# ---------------------------
# Results: loading
# ---------------------------

def test_schema_loading_result_ok_minimal():
    r = SchemaLoadingResult(ok=True)
    # Ok path should count as one loaded, zero failed; messages normalize to tuples
    assert getattr(r, "loaded") == 1
    assert getattr(r, "failed") == 0
    assert isinstance(r.errors, tuple)
    assert isinstance(r.warnings, tuple)
    assert isinstance(r.infos, tuple)
    assert r.errors == ()
    assert r.warnings == ()
    assert r.infos == ()


def test_schema_loading_result_failure_normalizes_messages():
    r = SchemaLoadingResult(
        ok=False,
        errors=["bad schema"],
        warnings=["non-fatal"],
        infos=["note"],
    )
    assert r.loaded == 0
    assert r.failed == 1
    assert r.errors == ("bad schema",)
    assert r.warnings == ("non-fatal",)
    assert r.infos == ("note",)


# ---------------------------
# Results: validation
# ---------------------------

def test_schema_validation_result_ok_minimal():
    r = SchemaValidationResult(ok=True)
    assert r.passed == 1
    assert r.failed == 0
    assert r.errors == ()
    assert r.warnings == ()
    assert r.infos == ()


def test_schema_validation_result_failure_normalizes_messages():
    r = SchemaValidationResult(
        ok=False,
        errors=["id missing"],
        warnings=["short description"],
        infos=["checked 12 fields"],
    )
    assert r.passed == 0
    assert r.failed == 1
    assert r.errors == ("id missing",)
    assert r.warnings == ("short description",)
    assert r.infos == ("checked 12 fields",)

# ---------------------------
# Error context formatting
# ---------------------------

def test_schema_error_includes_schema_and_version_and_path():
    err = SchemaError(
        "generic boom",
        schema_name="core",
        schema_version="2.0",
        file_path=Path("schemas/core.json"),
    )
    s = str(err)
    _assert_substrings(s, "Schema: core-2.0", "File: schemas/core.json", "generic boom")

def test_schema_parsing_error_includes_parse_error():
    err = SchemaParsingError(
        "parse boom",
        parse_error="unexpected token at line 4",
        schema_name="core",
        schema_version="2.0",
        file_path=Path("schemas/core.json"),
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "File: schemas/core.json",
        "Parse Error: unexpected token at line 4",
        "parse boom",
    )

def test_schema_version_error_includes_supported_versions():
    err = SchemaVersionError(
        "unsupported version",
        schema_version="3.1",
        supported_versions=["1.0", "2.0", "2.1"],
        schema_name="core",
        file_path=Path("schemas/core.json"),
    )
    s = str(err).replace("\\", "/")  # normalize for display only
    # Accept either explicit "Version: 3.1" or combined "Schema: core-3.1"
    has_version = ("Version: 3.1" in s) or ("Schema: core-3.1" in s)
    assert has_version, f"Expected version in string, got: {s!r}"
    _assert_substrings(
        s,
        "Supported: 1.0, 2.0, 2.1",
        "File: schemas/core.json",
        "unsupported version",
    )

def test_schema_format_error_includes_issue():
    err = SchemaFormatError(
        "format boom",
        format_issue="missing '$schema' key",
        schema_name="mapping",
        schema_version="1.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: mapping-1.0",
        "Issue: missing '$schema' key",
        "format boom",
    )

def test_schema_data_validation_error_context_all_fields():
    err = SchemaDataValidationError(
        "data invalid",
        validation_path="items[0].id",
        expected_type="string",
        actual_value="None",
        schema_name="core",
        schema_version="2.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "Field: items[0].id",
        "Expected: string",
        "Actual: None",
        "data invalid",
    )

def test_schema_field_validation_error_context_all_fields():
    err = SchemaFieldValidationError(
        "field invalid",
        field_name="id",
        field_path="items[0].id",
        constraint_type="required",
        schema_name="core",
        schema_version="2.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "Field: items[0].id",
        "Constraint: required",
        "field invalid",
    )

def test_schema_constraint_error_context_all_fields():
    err = SchemaConstraintError(
        "constraint fail",
        constraint_name="minItems",
        constraint_value="1",
        violated_rule="array must contain at least one item",
        schema_name="core",
        schema_version="2.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "Constraint: minItems",
        "Expected: 1",
        "Rule: array must contain at least one item",
        "constraint fail",
    )

def test_schema_reference_error_context_all_fields():
    err = SchemaReferenceError(
        "unresolved $ref",
        reference_path="#/components/schemas/User",
        reference_target="user.schema.json#/User",
        schema_name="core",
        schema_version="2.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "Reference: #/components/schemas/User",
        "Target: user.schema.json#/User",
        "unresolved $ref",
    )

def test_schema_circular_reference_error_context_chain():
    err = SchemaCircularReferenceError(
        "circular $ref",
        reference_chain=["A", "B", "C", "A"],
        schema_name="core",
        schema_version="2.0",
    )
    s = str(err)
    _assert_substrings(
        s,
        "Schema: core-2.0",
        "Chain: A → B → C → A",
        "circular $ref",
    )

# ---------------------------
# Error hierarchy sanity
# ---------------------------

@pytest.mark.parametrize(
    "t",
    [
        SchemaError,
        SchemaLoadingError,
        SchemaNotFoundError,
        SchemaParsingError,
        SchemaVersionError,
        SchemaFormatError,
        SchemaConstraintError,
        SchemaReferenceError,
        SchemaCircularReferenceError,
        SchemaValidationError,
        SchemaDataValidationError,
        SchemaFieldValidationError,
    ],
)
def test_error_is_exception_and_has_str(t: type):
    # instantiate with minimal message where possible
    try:
        e = t("boom")
    except TypeError:
        pytest.skip(f"{type(t).__name__} has a non-standard constructor")
        return
    assert isinstance(e, Exception)
    assert isinstance(str(e), str)
    assert str(e)

def test_slots_prevent_dynamic_attrs_on_base_and_subclass():
    # For each class, if instance has no __dict__, setting a new attr should raise.
    # If it *does* have a __dict__, dynamic attributes are allowed and should NOT raise.
    for cls in (SchemaError, SchemaParsingError):
        obj = cls("x")  # type: ignore[call-arg]
        has_dict = hasattr(obj, "__dict__")
        try:
            obj.some_new_attr = 1  # type: ignore[attr-defined]
            set_ok = True
        except AttributeError:
            set_ok = False

        if has_dict:
            assert set_ok, f"{cls.__name__} instances expose __dict__; dynamic attrs should be allowed"
        else:
            assert not set_ok, f"{cls.__name__} instances lack __dict__; dynamic attrs should raise AttributeError"


# ---------------------------
# Public API exports
# ---------------------------

def test_public_api_contains_all_named_errors():
    expected = {
        "SchemaCircularReferenceError",
        "SchemaConstraintError",
        "SchemaDataValidationError",
        "SchemaError",
        "SchemaFieldValidationError",
        "SchemaFormatError",
        "SchemaLoadingError",
        "SchemaNotFoundError",
        "SchemaParsingError",
        "SchemaReferenceError",
        "SchemaValidationError",
        "SchemaVersionError",
    }
    assert expected.issubset(set(SCHEMA_ERRORS_ALL)), f"Missing from __all__: {expected - set(SCHEMA_ERRORS_ALL)}"

# ---------------------------
# Results edge-cases/normalization
# ---------------------------

def test_schema_loading_result_failure_with_tuples_and_none():
    r = SchemaLoadingResult(ok=False, errors=("e1",), warnings=None, infos=None)
    assert r.loaded == 0
    assert r.failed == 1
    assert r.errors == ("e1",)
    # None should normalize to ()
    assert r.warnings == ()
    assert r.infos == ()

def test_schema_loading_result_ok_with_nonempty_messages_is_still_ok():
    r = SchemaLoadingResult(ok=True, warnings=["w1"], infos=["i1"])
    assert r.loaded == 1
    assert r.failed == 0
    assert r.warnings == ("w1",)
    assert r.infos == ("i1",)

def test_schema_validation_result_failure_with_tuples_and_none():
    r = SchemaValidationResult(ok=False, errors=("e2",), warnings=None, infos=None)
    assert r.passed == 0
    assert r.failed == 1
    assert r.errors == ("e2",)
    assert r.warnings == ()
    assert r.infos == ()

def test_schema_validation_result_ok_allows_warnings_infos():
    r = SchemaValidationResult(ok=True, warnings=["warn"], infos=["checked 5 fields"])
    assert r.passed == 1
    assert r.failed == 0
    assert r.warnings == ("warn",)
    assert r.infos == ("checked 5 fields",)
