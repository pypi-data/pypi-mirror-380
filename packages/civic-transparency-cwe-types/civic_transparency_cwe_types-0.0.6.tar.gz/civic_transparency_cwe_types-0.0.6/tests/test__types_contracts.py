"""Contract tests: dataclass, slots, immutability, and message normalization."""

from dataclasses import FrozenInstanceError, is_dataclass

from ci.transparency.cwe.types.batch.results import BatchResult
from ci.transparency.cwe.types.schema.results import (
    SchemaLoadingResult,
    SchemaValidationResult,
)
from ci.transparency.cwe.types.cwe.schema.results import (
    CweSchemaLoadingResult,
    CweSchemaValidationResult,
)
from ci.transparency.cwe.types.schema_evolution.results import (
    SchemaDiff,
    SchemaEvolutionReport,
)


def _has_slots(obj: object) -> bool:
    # Works for classes and instances
    cls = obj if isinstance(obj, type) else obj.__class__
    return hasattr(cls, "__slots__")


def test_batchresult_is_frozen_slots_dataclass() -> None:
    r = BatchResult()
    assert is_dataclass(r)
    assert _has_slots(r)

    # Frozen: setting any field should fail
    try:
        r.loaded = 99  # type: ignore[attr-defined]
        raise AssertionError("BatchResult should be frozen")
    except (FrozenInstanceError, AttributeError):
        pass


def test_schema_loading_is_frozen_slots_and_normalizes_messages() -> None:
    r_ok = SchemaLoadingResult(ok=True, schema_name="s", schema_version="1")
    assert is_dataclass(r_ok)
    assert _has_slots(r_ok)
    assert r_ok.loaded == 1 and r_ok.failed == 0
    assert r_ok.errors == () and r_ok.warnings == () and r_ok.infos == ()

    r_fail = SchemaLoadingResult(
        ok=False, errors=["e"], warnings=["w"], infos=["i"], schema_name="x", schema_version="y"
    )
    assert r_fail.loaded == 0 and r_fail.failed == 1
    assert r_fail.errors == ("e",) and r_fail.warnings == ("w",) and r_fail.infos == ("i",)

    # Frozen behavior
    try:
        r_fail.schema_name = "new"  # type: ignore[attr-defined]
        raise AssertionError("SchemaLoadingResult should be frozen")
    except (FrozenInstanceError, AttributeError):
        pass


def test_schema_validation_is_frozen_slots_and_normalizes_messages() -> None:
    r_ok = SchemaValidationResult(ok=True, schema_name="s", schema_version="1", instance_summary=None)
    assert is_dataclass(r_ok)
    assert _has_slots(r_ok)
    assert r_ok.passed == 1 and r_ok.failed == 0
    assert r_ok.errors == () and r_ok.warnings == () and r_ok.infos == ()

    r_fail = SchemaValidationResult(ok=False, errors=["e"], warnings=["w"], infos=["i"])
    assert r_fail.passed == 0 and r_fail.failed == 1
    assert r_fail.errors == ("e",) and r_fail.warnings == ("w",) and r_fail.infos == ("i",)

    # Frozen behavior
    try:
        r_ok.instance_summary = "summary"  # type: ignore[attr-defined]
        raise AssertionError("SchemaValidationResult should be frozen")
    except (FrozenInstanceError, AttributeError):
        pass


def test_cwe_schema_loading_and_validation_contracts() -> None:
    r_l = CweSchemaLoadingResult(ok=True, schema_name="cwe", schema_version="1.0")
    r_v = CweSchemaValidationResult(
        ok=True, schema_name="cwe", schema_version="1.0", cwe_id="CWE-79", field_path="properties.id"
    )

    for inst in (r_l, r_v):
        assert is_dataclass(inst)
        assert _has_slots(inst)

    assert r_l.loaded == 1 and r_l.failed == 0
    assert r_v.passed == 1 and r_v.failed == 0
    assert r_v.cwe_id == "CWE-79" and r_v.field_path == "properties.id"

    # Frozen/slots behavior (pick one representative)
    try:
        r_v.cwe_id = "mutate"  # type: ignore[attr-defined]
        raise AssertionError("CweSchemaValidationResult should be frozen")
    except (FrozenInstanceError, AttributeError):
        pass


def test_schema_diff_defaults_and_values() -> None:
    d = SchemaDiff()
    assert d.added == [] and d.removed == [] and d.changed == []

    d2 = SchemaDiff(added=["/a"], removed=["/r"], changed=["/c"])
    assert d2.added == ["/a"] and d2.removed == ["/r"] and d2.changed == ["/c"]

    # Lists are real lists (mutable by design for this simple holder)
    d2.added.append("/a2")
    assert "/a2" in d2.added


def test_schema_evolution_report_contract_and_messages() -> None:
    rep_ok = SchemaEvolutionReport(ok=True, diff=SchemaDiff(), old_version="1", new_version="2")
    assert is_dataclass(rep_ok)
    assert _has_slots(rep_ok)
    assert rep_ok.passed == 1 and rep_ok.failed == 0
    assert rep_ok.errors == () and rep_ok.warnings == () and rep_ok.infos == ()
    assert isinstance(rep_ok.diff, SchemaDiff)
    assert rep_ok.old_version == "1" and rep_ok.new_version == "2"

    rep_fail = SchemaEvolutionReport(ok=False, errors=["E"], warnings=["W"], diff=None)
    assert rep_fail.passed == 0 and rep_fail.failed == 1
    assert rep_fail.errors == ("E",) and rep_fail.warnings == ("W",)

    # Frozen/slots behavior
    try:
        rep_ok.old_version = "3"  # type: ignore[attr-defined]
        raise AssertionError("SchemaEvolutionReport should be frozen")
    except (FrozenInstanceError, AttributeError):
        pass
