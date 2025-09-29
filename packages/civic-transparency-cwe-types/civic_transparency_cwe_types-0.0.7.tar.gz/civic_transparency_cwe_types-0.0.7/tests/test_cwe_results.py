# pyright: strict

import importlib
import inspect
from dataclasses import is_dataclass, fields
from pathlib import Path
import pytest

from ci.transparency.cwe.types.cwe.results import (
    CweLoadingResult,
    CweValidationResult,
    add_cwe,
    track_invalid_file,
    validate_cwe,
    batch_validate_cwes,
    get_cwe_loading_summary,
    get_cwe_validation_summary,
    CweRelationshipResult,
    analyze_relationships,
    CweItemDict,
    CweDataDict
)


def test_results_module_imports() -> None:
    # Ensure the module imports cleanly (no side-effects raising errors)
    mod = importlib.import_module("ci.transparency.cwe.types.cwe.results")
    # It should have at least a few attributes
    assert hasattr(mod, "__name__")


def test_results_dataclasses_can_instantiate_with_defaults() -> None:
    mod = importlib.import_module("ci.transparency.cwe.types.cwe.results")

    # Find dataclass types defined in this module
    dc_types = [
        obj for _name, obj in inspect.getmembers(mod)
        if inspect.isclass(obj)
        and obj.__module__ == mod.__name__
        and is_dataclass(obj)
    ]

    if not dc_types:
        pytest.skip("No dataclasses found in cwe.results (nothing to exercise).")

    for cls in dc_types:
        # Build kwargs only for fields that have defaults; otherwise we try no-arg init
        try:
            instance = cls()  # type: ignore[call-arg]
        except TypeError:
            # Provide defaults for fields without defaults where possible
            kwargs: dict[str, object] = {}
            for f in fields(cls):
                if f.default is not inspect._empty or f.default_factory is not inspect._empty:  # type: ignore[attr-defined]
                    # Dataclasses store default/default_factory, but we can skip here:
                    continue
                # Best-effort fillers for common types; otherwise skip the field (may still fail)
                if f.type in (int, "int"):
                    kwargs[f.name] = 0
                elif f.type in (float, "float"):
                    kwargs[f.name] = 0.0
                elif f.type in (str, "str"):
                    kwargs[f.name] = ""
                elif f.type in (bool, "bool"):
                    kwargs[f.name] = False
                else:
                    # Leave unset; constructor may still accept missing (unlikely), or fail
                    # If it fails, that signals a dataclass without defaults—we don't enforce here.
                    pass
            try:
                instance = cls(**kwargs)  # type: ignore[misc]
            except Exception as e:  # noqa: BLE001
                pytest.skip(f"Dataclass {cls.__name__} requires non-trivial constructor args: {e}")

        # Touch repr/str won’t throw
        _ = repr(instance)
        _ = str(instance)

        # Access all fields to ensure attributes are present
        for f in fields(cls):
            _ = getattr(instance, f.name, None)


def test_add_cwe_success():
    """Test successfully adding a CWE."""
    result = CweLoadingResult()
    cwe_data: CweItemDict = {"id": "CWE-79", "name": "XSS", "category": "injection"}  # Use correct type

    new_result = add_cwe(result, "CWE-79", cwe_data, file_path=Path("test.yaml"))

    assert new_result.cwe_count == 1
    assert "CWE-79" in new_result.cwes
    assert new_result.loading.loaded_count == 1
    assert new_result.messages.info_count == 1

def test_add_cwe_duplicate_handling():
    """Test duplicate CWE handling."""
    result = CweLoadingResult()
    cwe_data: CweItemDict = {"id": "CWE-79", "name": "XSS", "category": "injection"}  # Use correct type

    # Add first time
    result = add_cwe(result, "CWE-79", cwe_data)
    # Add duplicate
    result = add_cwe(result, "CWE-79", cwe_data, file_path=Path("dup.yaml"))

    assert result.cwe_count == 1  # Still only one
    assert result.duplicates.duplicate_count == 1
    assert result.messages.warning_count == 1

def test_track_invalid_file():
    """Test tracking invalid files."""
    result = CweLoadingResult()

    new_result = track_invalid_file(result, Path("bad.yaml"), "malformed")

    assert new_result.files.failed_file_count == 1
    assert new_result.loading.failed_count == 1
    assert new_result.messages.error_count == 1

# Validation Operations

def test_validate_cwe_success():
    """Test successful CWE validation."""
    result = CweValidationResult()
    cwe_data: CweItemDict = {
        "id": "CWE-79",
        "name": "Cross-site Scripting",
        "description": "XSS vulnerability description",
        "category": "injection"
    }

    new_result = validate_cwe(result, "CWE-79", cwe_data)

    assert new_result.validated_count == 1
    assert new_result.validation.passed_count == 1
    assert "CWE-79" in new_result.get_passed_cwes()

def test_validate_cwe_failures():
    """Test CWE validation failures."""
    result = CweValidationResult()
    cwe_data: CweItemDict = {"id": "INVALID", "name": ""}  # Missing fields, invalid ID

    new_result = validate_cwe(result, "INVALID", cwe_data)

    assert new_result.validation.failed_count == 1
    assert "INVALID" in new_result.get_failed_cwes()
    assert len(new_result.get_validation_errors("INVALID")) > 0

def test_batch_validate_cwes():
    """Test batch validation."""
    result = CweValidationResult()
    cwe_dict: dict[str, CweItemDict] = {
        "CWE-79": {"id": "CWE-79", "name": "XSS", "description": "desc"},
        "CWE-89": {"id": "CWE-89", "name": "SQLi", "description": "desc"}
    }

    new_result = batch_validate_cwes(result, cwe_dict)

    assert new_result.validated_count == 2


# Summary functions

def test_get_cwe_loading_summary():
    """Test loading summary generation."""
    result = CweLoadingResult()
    result = add_cwe(result, "CWE-79", {"id": "CWE-79", "name": "XSS"})

    summary = get_cwe_loading_summary(result)

    assert summary["cwes_loaded"] == 1
    assert summary["successful_loads"] == 1
    assert "CWE-79" in summary["loaded_cwe_ids"]

def test_get_cwe_validation_summary():
    """Test validation summary generation."""
    result = CweValidationResult()
    result = validate_cwe(
        result,
        "CWE-79",
        {
            "id": "CWE-79",
            "name": "XSS",
            "description": "Cross-site scripting vulnerability"  # 10+ characters
        }
    )

    summary = get_cwe_validation_summary(result)

    assert summary["cwes_validated"] == 1
    assert summary["validation_passed"] == 1


# Relationship analysis

def test_analyze_relationships():
    """Test relationship analysis."""
    result = CweRelationshipResult()
    cwe_dict: CweDataDict = {
        "CWE-79": {
            "id": "CWE-79",
            "relationships": [{"cwe_id": "CWE-80", "type": "child"}]
        },
        "CWE-80": {"id": "CWE-80", "relationships": []}
    }

    new_result = analyze_relationships(result, cwe_dict)

    assert new_result.references.total_references_count == 1
    assert len(new_result.relationship_types) > 0
