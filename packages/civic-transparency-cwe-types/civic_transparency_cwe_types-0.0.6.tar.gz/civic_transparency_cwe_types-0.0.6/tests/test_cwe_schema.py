# tests/test_cwe_schema.py
"""Tests for CWE schema result types (loading/validation)."""

from ci.transparency.cwe.types.cwe.schema.results import (
    CweSchemaLoadingResult,
    CweSchemaValidationResult,
)


def test_loading_ok_minimal():
    r = CweSchemaLoadingResult(ok=True, schema_name="cwe", schema_version="1.0")
    assert r.loaded == 1
    assert r.failed == 0
    assert r.success_rate == 1.0
    assert r.schema_name == "cwe"
    assert r.schema_version == "1.0"
    assert r.errors == ()
    assert r.warnings == ()
    assert r.infos == ()


def test_loading_failure_normalizes_messages():
    r = CweSchemaLoadingResult(
        ok=False,
        errors=["bad schema"],
        warnings=["non-fatal"],
        infos=["note"],
        schema_name="cwe",
        schema_version="2.0",
    )
    assert r.loaded == 0
    assert r.failed == 1
    assert r.errors == ("bad schema",)
    assert r.warnings == ("non-fatal",)
    assert r.infos == ("note",)
    assert r.schema_name == "cwe"
    assert r.schema_version == "2.0"


def test_validation_ok_with_metadata():
    r = CweSchemaValidationResult(
        ok=True,
        schema_name="cwe",
        schema_version="1.0",
        cwe_id="CWE-A001",
        field_path="properties.id",
    )
    assert r.passed == 1
    assert r.failed == 0
    assert r.schema_name == "cwe"
    assert r.schema_version == "1.0"
    assert r.cwe_id == "CWE-A001"
    assert r.field_path == "properties.id"
    assert r.errors == ()
    assert r.warnings == ()
    assert r.infos == ()


def test_validation_failure_normalizes_messages():
    r = CweSchemaValidationResult(
        ok=False,
        errors=["id missing"],
        warnings=["short description"],
        infos=["checked 12 fields"],
        schema_name="cwe",
        schema_version="1.1",
    )
    assert r.passed == 0
    assert r.failed == 1
    assert r.errors == ("id missing",)
    assert r.warnings == ("short description",)
    assert r.infos == ("checked 12 fields",)
