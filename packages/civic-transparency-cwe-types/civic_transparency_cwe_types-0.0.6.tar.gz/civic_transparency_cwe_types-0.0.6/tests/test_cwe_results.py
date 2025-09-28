"""Tests for CWE result types and operations (strict, 3.12+).

Covers loading, validation, and relationship results:
- Result dataclasses and derived/boolean properties
- Core operations: add/track/validate/analyze/add_relationship
- Conversions to/from BatchResult
- Edge cases and immutability
"""

from __future__ import annotations

from pathlib import Path
from typing import cast, Any

import pytest

from ci.transparency.cwe.types.batch import BatchResult
from ci.transparency.cwe.types.cwe.results import (
    # Result types & typed dicts
    CweDataDict,
    CweLoadingResult,
    CweRelationshipDict,
    CweRelationshipResult,
    CweValidationResult,
    # Core ops
    add_cwe,
    add_relationship,
    analyze_relationships,
    batch_validate_cwes,
    get_cwe_loading_summary,
    track_invalid_file,
    track_skipped_cwe_file,
    validate_cwe,
    validate_cwe_field,
)


class TestCweLoadingResult:
    """Test CWE loading result type and operations."""

    def test_empty_cwe_loading_result(self) -> None:
        """Empty init has 0 counts and empty collections."""
        result = CweLoadingResult()

        assert result.cwe_count == 0
        assert result.loaded_cwe_ids == ()
        assert result.duplicate_count == 0
        assert result.invalid_file_count == 0
        assert result.skipped_file_count == 0

        assert not result.has_duplicates

        assert len(result.cwes) == 0
        assert len(result.duplicate_ids) == 0
        assert len(result.invalid_files) == 0
        assert len(result.skipped_files) == 0

    def test_cwe_loading_result_with_data(self) -> None:
        """Initialization with prefilled data yields correct counts."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": {"id": "CWE-79", "name": "Cross-site Scripting", "category": "injection"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection", "category": "injection"},
        }
        duplicates = {"CWE-100": [Path("duplicate.yaml")]}
        invalid_files = (Path("invalid.yaml"), Path("malformed.yaml"))
        skipped_files = (Path("skipped.yaml"),)

        result = CweLoadingResult(
            cwes=cwes,
            duplicate_ids=duplicates,
            invalid_files=invalid_files,
            skipped_files=skipped_files,
            loaded=2,
            failed=3,
        )

        assert result.cwe_count == 2
        assert result.duplicate_count == 1
        assert result.invalid_file_count == 2
        assert result.skipped_file_count == 1

        assert result.has_duplicates

        assert result.has_cwe("CWE-79")
        assert result.has_cwe("CWE-89")
        assert not result.has_cwe("CWE-999")

        cwe_79 = result.get_cwe("CWE-79")
        assert cwe_79 is not None and cwe_79.get("name") == "Cross-site Scripting"

        loaded_ids = result.loaded_cwe_ids
        assert set(loaded_ids) == {"CWE-79", "CWE-89"}

    def test_add_cwe_operation(self) -> None:
        """add_cwe adds item, increments loaded, preserves immutability."""
        result = CweLoadingResult()
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "Cross-site Scripting", "category": "injection"}
        file_path = Path("cwe-79.yaml")

        new_result = add_cwe(result, "CWE-79", cwe_data, file_path=file_path)

        assert new_result.cwe_count == 1
        assert new_result.has_cwe("CWE-79")
        assert new_result.get_cwe("CWE-79") == cwe_data
        assert new_result.loaded == 1

        # original unchanged
        assert result.cwe_count == 0
        assert result.loaded == 0

    def test_add_duplicate_cwe(self) -> None:
        """Duplicates tracked; failed increments; warnings recorded."""
        initial: CweDataDict = {"id": "CWE-79", "name": "XSS"}
        result = add_cwe(CweLoadingResult(), "CWE-79", initial)

        duplicate: CweDataDict = {"id": "CWE-79", "name": "Different XSS"}
        file_path = Path("duplicate.yaml")

        new_result = add_cwe(result, "CWE-79", duplicate, file_path=file_path)

        assert new_result.cwe_count == 1
        assert new_result.duplicate_count == 1
        assert new_result.failed == 1
        assert "CWE-79" in new_result.duplicate_ids
        assert len(new_result.warnings) > 0

    def test_track_invalid_file(self) -> None:
        """Invalid files recorded as errors; failed increments."""
        result = CweLoadingResult()
        file_path = Path("invalid.yaml")
        reason = "Malformed YAML syntax"

        new_result = track_invalid_file(result, file_path, reason)

        assert new_result.invalid_file_count == 1
        assert file_path in new_result.invalid_files
        assert new_result.failed == 1
        assert any(reason in msg for msg in new_result.errors)

    def test_track_skipped_file(self) -> None:
        """Skipped files recorded as infos."""
        result = CweLoadingResult()
        file_path = Path("skipped.yaml")
        reason = "File extension not supported"

        new_result = track_skipped_cwe_file(result, file_path, reason)

        assert new_result.skipped_file_count == 1
        assert file_path in new_result.skipped_files
        assert any(reason in msg for msg in new_result.infos)

    def test_from_batch_conversion(self) -> None:
        """from_batch converts BatchResult items to CWEs and preserves skips."""
        batch_data: dict[str, dict[str, Any]] = {
            "CWE-79": {"id": "CWE-79", "name": "XSS"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection"},
        }
        skipped = (Path("readme.txt"),)

        batch_result = BatchResult(items=batch_data, skipped_files=skipped, loaded=2, failed=0)

        cwe_result = CweLoadingResult.from_batch(batch_result)

        assert cwe_result.cwe_count == 2
        assert set(cwe_result.cwes) == {"CWE-79", "CWE-89"}
        assert cwe_result.skipped_file_count == 1
        assert cwe_result.loaded == 2


class TestCweValidationResult:
    """Test CWE validation result type and operations."""

    def test_empty_cwe_validation_result(self) -> None:
        """Empty init has no schema, no results, no field errors."""
        result = CweValidationResult()

        assert result.validated_count == 0
        assert result.field_error_count == 0
        assert not result.has_field_errors
        assert not result.schema_validation_used
        assert result.schema_version == ""
        assert result.get_failed_cwes() == []
        assert result.get_passed_cwes() == []

    def test_cwe_validation_result_with_data(self) -> None:
        """Property helpers compute counts and lists correctly."""
        validation_results: dict[str, bool] = {
            "CWE-79": True,
            "CWE-89": True,
            "CWE-22": False,
            "CWE-100": False,
        }
        field_errors = ("CWE-22.name", "CWE-100.description")
        validated_cwes = ("CWE-79", "CWE-89", "CWE-22", "CWE-100")

        result = CweValidationResult(
            validation_results=validation_results,
            field_errors=field_errors,
            validated_cwes=validated_cwes,
            schema_validation_used=True,
            schema_version="1.2",
            passed=2,
            failed=2,
        )

        assert result.validated_count == 4
        assert result.field_error_count == 2
        assert result.has_field_errors
        assert result.schema_validation_used
        assert result.schema_version == "1.2"

        failed_cwes = result.get_failed_cwes()
        passed_cwes = result.get_passed_cwes()
        assert set(failed_cwes) == {"CWE-22", "CWE-100"}
        assert set(passed_cwes) == {"CWE-79", "CWE-89"}

    def test_validate_cwe_failure(self) -> None:
        """Current validator flags minimal data and ID format issues."""
        result = CweValidationResult()
        cwe_data: CweDataDict = {"id": "CWE-79"}  # missing name/description etc.

        new_result = validate_cwe(result, "CWE-79", cwe_data)

        assert new_result.validated_count == 1
        assert new_result.validation_results.get("CWE-79") is False
        assert new_result.passed == 0
        assert new_result.failed == 1
        assert len(new_result.errors) > 0
        # optional: details mention format/description
        assert "CWE-79" in new_result.validation_details
        assert isinstance(new_result.validation_details["CWE-79"], list)

    def test_validate_cwe_field(self) -> None:
        """Field-level validation updates pass/fail and field_errors."""
        result = CweValidationResult()

        ok = validate_cwe_field(result, "CWE-79", "name", "Cross-site Scripting", "must not be empty")
        assert ok.passed == 1
        assert ok.failed == 0
        assert ok.field_error_count == 0

        failed = validate_cwe_field(ok, "CWE-79", "description", None, "must not be None")
        assert failed.passed == 1
        assert failed.failed == 1
        assert failed.field_error_count == 1
        assert "CWE-79.description" in failed.field_errors

    def test_batch_validate_cwes_current_rules(self) -> None:
        """Given current rules, 'CWE-79'/'CWE-89' fail (format + description)."""
        loading_like: dict[str, CweDataDict] = {
            "CWE-79": {"id": "CWE-79", "name": "XSS"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection"},
        }
        vr = CweValidationResult()
        final = batch_validate_cwes(vr, loading_like)

        assert final.validated_count == 2
        assert final.passed == 0
        assert final.failed == 2
        assert final.validation_results["CWE-79"] is False
        assert final.validation_results["CWE-89"] is False
        assert "Batch validated 2 CWEs" in final.infos


class TestCweRelationshipResult:
    """Test CWE relationship result type and operations."""

    def test_empty_relationship_result(self) -> None:
        """Empty init has zero counts and empty collections."""
        result = CweRelationshipResult()

        assert result.total_relationships == 0
        assert result.circular_dependency_count == 0
        assert result.orphaned_cwe_count == 0
        assert result.invalid_reference_count == 0
        assert not result.has_circular_dependencies
        assert not result.has_orphaned_cwes

        assert len(result.relationship_map) == 0
        assert len(result.circular_dependencies) == 0
        assert len(result.orphaned_cwes) == 0
        assert len(result.invalid_references) == 0
        assert len(result.relationship_types) == 0

    def test_relationship_result_with_data(self) -> None:
        """Counts derived from maps/lists are correct."""
        relationship_map: dict[str, list[str]] = {
            "CWE-79": ["CWE-80", "CWE-81"],
            "CWE-89": ["CWE-90"],
        }
        circular_dependencies = ("CWE-100", "CWE-101")
        orphaned_cwes = ("CWE-200",)
        invalid_references = ("CWE-79 → CWE-999",)
        relationship_types = {"ChildOf": 3, "ParentOf": 1}

        result = CweRelationshipResult(
            relationship_map=relationship_map,
            circular_dependencies=circular_dependencies,
            orphaned_cwes=orphaned_cwes,
            invalid_references=invalid_references,
            relationship_types=relationship_types,
            passed=3,
            failed=1,
        )

        assert result.total_relationships == 3
        assert result.circular_dependency_count == 2
        assert result.orphaned_cwe_count == 1
        assert result.invalid_reference_count == 1
        assert result.has_circular_dependencies
        assert result.has_orphaned_cwes

        assert result.get_relationships("CWE-79") == ["CWE-80", "CWE-81"]
        assert result.get_relationships("CWE-89") == ["CWE-90"]
        assert result.get_relationships("CWE-999") == []

    def test_analyze_relationships(self) -> None:
        """Analyze detects invalid refs, orphaned CWEs, and tallies types."""
        result = CweRelationshipResult()
        cwe_dict: dict[str, CweDataDict] = {
            "CWE-79": cast(
                CweDataDict,
                {
                    "id": "CWE-79",
                    "relationships": [
                        {"cwe_id": "CWE-80", "type": "ChildOf"},
                        {"cwe_id": "CWE-999", "type": "ParentOf"},  # invalid
                    ],
                },
            ),
            "CWE-80": cast(
                CweDataDict,
                {"id": "CWE-80", "relationships": [{"cwe_id": "CWE-79", "type": "ParentOf"}]},
            ),
            "CWE-200": cast(CweDataDict, {"id": "CWE-200", "relationships": []}),  # orphaned
        }

        new_result = analyze_relationships(result, cwe_dict)

        assert new_result.total_relationships > 0
        assert len(new_result.relationship_map) >= 2

        assert new_result.invalid_reference_count >= 1
        assert any("CWE-999" in ref for ref in new_result.invalid_references)

        assert new_result.orphaned_cwe_count >= 1
        assert "CWE-200" in new_result.orphaned_cwes

        assert "ChildOf" in new_result.relationship_types
        assert "ParentOf" in new_result.relationship_types

    def test_add_relationship(self) -> None:
        """Adding relationships updates map and type counts."""
        result = CweRelationshipResult()

        r1 = add_relationship(result, "CWE-79", "CWE-80", "ChildOf")
        assert "CWE-79" in r1.relationship_map
        assert "CWE-80" in r1.relationship_map["CWE-79"]
        assert r1.relationship_types["ChildOf"] == 1

        r2 = add_relationship(r1, "CWE-79", "CWE-81", "ChildOf")
        assert set(r2.relationship_map["CWE-79"]) == {"CWE-80", "CWE-81"}
        assert r2.relationship_types["ChildOf"] == 2

    def test_circular_dependency_detection(self) -> None:
        """Cycle across A->B->C->A is detected by analysis."""
        result = CweRelationshipResult()
        cwe_dict: dict[str, CweDataDict] = {
            "CWE-A": cast(CweDataDict, {"id": "CWE-A", "relationships": [{"cwe_id": "CWE-B", "type": "ChildOf"}]}),
            "CWE-B": cast(CweDataDict, {"id": "CWE-B", "relationships": [{"cwe_id": "CWE-C", "type": "ChildOf"}]}),
            "CWE-C": cast(CweDataDict, {"id": "CWE-C", "relationships": [{"cwe_id": "CWE-A", "type": "ChildOf"}]}),
        }

        analyzed = analyze_relationships(result, cwe_dict)
        assert len(analyzed.circular_dependencies) > 0


class TestAnalysisFunctions:
    """Test CWE analysis and summary functionality."""

    def test_cwe_loading_summary_data(self) -> None:
        """get_cwe_loading_summary mirrors key properties."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "name": "XSS", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "name": "SQL Injection", "category": "injection"}),
        }
        result = CweLoadingResult(
            cwes=cwes,
            duplicate_ids={"CWE-100": [Path("dup.yaml")]},
            invalid_files=(Path("invalid.yaml"),),
            skipped_files=(Path("skip.yaml"),),
            loaded=2,
            failed=2,
            errors=("Parse error",),
            warnings=("Duplicate warning",),
        )

        assert result.cwe_count == 2
        assert result.duplicate_count == 1
        assert result.invalid_file_count == 1
        assert result.skipped_file_count == 1
        assert result.success_rate == 0.5
        assert result.has_errors
        assert result.has_warnings
        assert len(result.loaded_cwe_ids) == 2

        summary = get_cwe_loading_summary(result)
        assert summary["cwes_loaded"] == 2
        assert summary["duplicate_ids"] == 1

    def test_cwe_validation_summary_data(self) -> None:
        """Validation summary derived values."""
        validation_results: dict[str, bool] = {"CWE-79": True, "CWE-89": True, "CWE-100": False}
        result = CweValidationResult(
            validation_results=validation_results,
            field_errors=("field1", "field2"),
            validated_cwes=("CWE-79", "CWE-89", "CWE-100"),
            schema_validation_used=True,
            schema_version="1.0",
            passed=2,
            failed=1,
        )

        assert result.validated_count == 3
        assert result.field_error_count == 2
        assert result.has_field_errors
        assert result.schema_validation_used
        assert result.schema_version == "1.0"
        expected_rate: float = 2.0 / 3.0
        assert result.success_rate == pytest.approx(float(expected_rate), abs=0.01) # type: ignore
        assert "CWE-100" in result.get_failed_cwes()
        assert set(result.get_passed_cwes()) == {"CWE-79", "CWE-89"}

    def test_relationship_summary_data(self) -> None:
        """Relationship properties reflect provided data."""
        relationship_map: dict[str, list[str]] = {
            "CWE-79": ["CWE-80", "CWE-81"],
            "CWE-89": ["CWE-90"],
        }
        result = CweRelationshipResult(
            relationship_map=relationship_map,
            circular_dependencies=("CWE-100", "CWE-101"),
            orphaned_cwes=("CWE-200",),
            invalid_references=("CWE-79 → CWE-999",),
            relationship_types={"ChildOf": 3, "ParentOf": 2},
        )

        assert result.total_relationships == 3
        assert len(result.relationship_map) == 2
        assert result.circular_dependency_count == 2
        assert result.orphaned_cwe_count == 1
        assert result.invalid_reference_count == 1
        assert result.has_circular_dependencies
        assert result.has_orphaned_cwes

    def test_cwes_by_category_direct(self) -> None:
        """Filter CWEs by category via direct dict comparison."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "category": "injection"}),
            "CWE-22": cast(CweDataDict, {"id": "CWE-22", "category": "path_traversal"}),
            "CWE-200": cast(CweDataDict, {"id": "CWE-200", "category": "information_disclosure"}),
        }
        result = CweLoadingResult(cwes=cwes)

        injection_cwes = {cid: data for cid, data in result.cwes.items() if data.get("category") == "injection"}
        assert set(injection_cwes) == {"CWE-79", "CWE-89"}

    def test_relationship_depth_calculation(self) -> None:
        """Sanity checks on get_relationships call shapes/depths."""
        relationship_map: dict[str, list[str]] = {
            "CWE-1": ["CWE-2"],
            "CWE-2": ["CWE-3"],
            "CWE-3": ["CWE-4"],
            "CWE-4": [],
        }
        result = CweRelationshipResult(relationship_map=relationship_map)

        assert len(result.get_relationships("CWE-1")) == 1
        assert len(result.get_relationships("CWE-2")) == 1
        assert len(result.get_relationships("CWE-4")) == 0


class TestResultImmutability:
    """Test that result operations maintain immutability."""

    def test_cwe_loading_result_immutability(self) -> None:
        """add_cwe returns a new instance; original unchanged."""
        original = CweLoadingResult(loaded=1, failed=0)
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "XSS"}

        new_result = add_cwe(original, "CWE-79", cwe_data)

        assert original.cwe_count == 0
        assert original.loaded == 1

        assert new_result.cwe_count == 1
        assert new_result.loaded == 2

    def test_cwe_validation_result_immutability(self) -> None:
        """validate_cwe returns a new instance; pass/fail reflect rule outcome."""
        original = CweValidationResult(passed=1)
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "XSS"}

        new_result = validate_cwe(original, "CWE-79", cwe_data)

        # original unchanged
        assert original.validated_count == 0
        assert original.passed == 1

        # current rules mark this as invalid -> passed stays at 1, failed increments
        assert new_result.validated_count == 1
        assert new_result.passed == 1
        assert new_result.failed == 1
        assert new_result.validation_results.get("CWE-79") is False

    def test_cwe_relationship_result_immutability(self) -> None:
        """add_relationship returns a new instance; original unchanged."""
        original = CweRelationshipResult()
        updated = add_relationship(original, "CWE-79", "CWE-80", "ChildOf")

        assert original.total_relationships == 0 and len(original.relationship_map) == 0
        assert updated.total_relationships == 1 and len(updated.relationship_map) == 1


class TestEdgeCases:
    """Edge cases and error conditions."""

    def test_empty_cwe_data_validation(self) -> None:
        """Empty dict fails validation; failed increments."""
        result = CweValidationResult()
        new_result = validate_cwe(result, "CWE-EMPTY", cast(CweDataDict, {}))
        assert new_result.validation_results["CWE-EMPTY"] is False
        assert new_result.failed == 1

    def test_none_field_validation(self) -> None:
        """None value -> field error + failed++."""
        result = CweValidationResult()
        new_result = validate_cwe_field(result, "CWE-79", "name", None, "required field")
        assert new_result.failed == 1
        assert new_result.field_error_count == 1

    def test_empty_relationship_analysis(self) -> None:
        """Empty input yields no relationships."""
        result = CweRelationshipResult()
        new_result = analyze_relationships(result, {})
        assert new_result.total_relationships == 0
        assert len(new_result.relationship_map) == 0

    def test_malformed_relationship_data(self) -> None:
        """Missing fields in relationship entries are tolerated (counted appropriately)."""
        result = CweRelationshipResult()
        malformed_raw: dict[str, dict[str, Any]] = {
            "CWE-79": {
                "id": "CWE-79",
                "relationships": [
                    {"type": "ChildOf"},  # missing cwe_id
                    {"cwe_id": "CWE-80"},  # missing type
                    {},  # empty
                ],
            }
        }
        malformed: dict[str, CweDataDict] = {k: cast(CweDataDict, v) for k, v in malformed_raw.items()}

        new_result = analyze_relationships(result, malformed)
        assert isinstance(new_result, CweRelationshipResult)

    def test_large_dataset_performance(self) -> None:
        """Adding many CWEs & summarizing remains functional."""
        result = CweLoadingResult()
        for i in range(100):
            cid = f"CWE-{i:04d}"
            data: CweDataDict = {"id": cid, "name": f"Test CWE {i}"}
            result = add_cwe(result, cid, data)

        assert result.cwe_count == 100
        assert result.loaded == 100

        summary = get_cwe_loading_summary(result)
        assert summary["cwes_loaded"] == 100

    def test_unicode_handling(self) -> None:
        """Unicode fields are stored/retrieved intact."""
        result = CweLoadingResult()
        unicode_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Скрипт межсайтовых атак",
            "category": "注入攻击",
        }
        new_result = add_cwe(result, "CWE-79", unicode_data)
        assert new_result.cwe_count == 1
        got = new_result.get_cwe("CWE-79")
        assert got is not None and got.get("name") == "Скрипт межсайтовых атак"

    def test_path_handling(self) -> None:
        """Paths with spaces/depth preserved in invalid_files."""
        result = CweLoadingResult()
        complex_path = Path("some") / "deeply" / "nested" / "path with spaces" / "cwe-79.yaml"
        new_result = track_invalid_file(result, complex_path, "Test reason")
        assert new_result.invalid_file_count == 1
        assert complex_path in new_result.invalid_files


class TestResultConversions:
    """Conversions and cross-result usage."""

    def test_batch_to_cwe_conversion(self) -> None:
        """BatchResult -> CweLoadingResult mapping and counters."""
        batch_data: dict[str, CweDataDict] = {
            "CWE-79": {"id": "CWE-79", "name": "XSS"},
            "CWE-89": {"id": "CWE-89", "name": "SQLi"},
        }
        batch = BatchResult(items=cast(dict[str, dict[str, Any]], batch_data), loaded=2, failed=0, skipped_files=(Path("README.md"),))
        cwe = CweLoadingResult.from_batch(batch)

        assert cwe.cwe_count == 2
        assert set(cwe.cwes) == {"CWE-79", "CWE-89"}
        assert cwe.skipped_file_count == 1
        assert cwe.loaded == 2
        assert cwe.failed == 0

    def test_loading_to_validation_context_current_rules(self) -> None:
        """Batch-style CWEs currently fail; assert that shape and messages align."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "name": "XSS", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "name": "SQLi", "category": "injection"}),
        }
        loading = CweLoadingResult(cwes=cwes, loaded=2)

        vr0 = CweValidationResult()
        final = batch_validate_cwes(vr0, loading.cwes)

        assert final.validated_count == 2
        assert final.passed == 0
        assert final.failed == 2
        # confirm per-CWE flags present
        assert final.validation_results["CWE-79"] is False
        assert final.validation_results["CWE-89"] is False
        assert "Batch validated 2 CWEs" in final.infos


class TestDataStructures:
    """Typed structure shape checks."""

    def test_cwe_data_dict_structure(self) -> None:
        """CweDataDict expected keys and relationships shape."""
        cwe_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Cross-site Scripting",
            "category": "injection",
            "relationships": [{"cwe_id": "CWE-80", "type": "ChildOf"}],
        }

        assert cwe_data["id"] == "CWE-79"
        assert cwe_data["name"] == "Cross-site Scripting"
        assert cwe_data["category"] == "injection"
        rels = cwe_data.get("relationships", [])
        assert isinstance(rels, list) and len(rels) == 1
        assert rels[0].get("cwe_id") == "CWE-80"

    def test_cwe_relationship_dict_structure(self) -> None:
        """CweRelationshipDict minimal shape."""
        relationship: CweRelationshipDict = {"cwe_id": "CWE-80", "type": "ChildOf"}
        assert relationship.get("cwe_id") == "CWE-80"
        assert relationship.get("type") == "ChildOf"
