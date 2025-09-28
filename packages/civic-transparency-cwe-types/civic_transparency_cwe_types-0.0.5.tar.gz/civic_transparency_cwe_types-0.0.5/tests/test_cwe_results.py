"""Tests for CWE result types and operations.

Tests for CWE loading, validation, and relationship result types
including all operations and analysis functions.
"""

import pytest
from pathlib import Path
from typing import cast

from ci.transparency.cwe.types.cwe.results import (
    # Result types
    CweLoadingResult,
    CweValidationResult,
    CweRelationshipResult,
    CweDataDict,
    CweRelationshipDict,

    # Core operations
    add_cwe,
    track_duplicate_cwe,
    track_invalid_file,
    track_skipped_cwe_file,
    validate_cwe,
    validate_cwe_field,
    batch_validate_cwes,
    analyze_relationships,
    add_relationship,
)

from ci.transparency.cwe.types.batch import BatchResult
from ci.transparency.cwe.types.cwe.results import get_cwe_loading_summary


class TestCweLoadingResult:
    """Test CWE loading result type and operations."""

    def test_empty_cwe_loading_result(self):
        """Test empty CWE loading result initialization."""
        result = CweLoadingResult()

        # Test basic properties
        assert result.cwe_count == 0
        assert result.loaded_cwe_ids == ()
        assert result.duplicate_count == 0
        assert result.invalid_file_count == 0
        assert result.skipped_file_count == 0

        # Test boolean properties
        assert not result.has_duplicates

        # Test dictionaries are empty
        assert len(result.cwes) == 0
        assert len(result.duplicate_ids) == 0
        assert len(result.invalid_files) == 0
        assert len(result.skipped_files) == 0

    def test_cwe_loading_result_with_data(self):
        """Test CWE loading result with sample data."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": {"id": "CWE-79", "name": "Cross-site Scripting", "category": "injection"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection", "category": "injection"}
        }
        duplicates = {"CWE-100": Path("duplicate.yaml")}
        invalid_files = (Path("invalid.yaml"), Path("malformed.yaml"))
        skipped_files = (Path("skipped.yaml"),)

        result = CweLoadingResult(
            cwes=cwes,
            duplicate_ids=duplicates,
            invalid_files=invalid_files,
            skipped_files=skipped_files,
            loaded=2,
            failed=3
        )

        # Test counts
        assert result.cwe_count == 2
        assert result.duplicate_count == 1
        assert result.invalid_file_count == 2
        assert result.skipped_file_count == 1

        # Test boolean properties
        assert result.has_duplicates

        # Test CWE access
        assert result.has_cwe("CWE-79")
        assert result.has_cwe("CWE-89")
        assert not result.has_cwe("CWE-999")

        # Test CWE retrieval
        cwe_79 = result.get_cwe("CWE-79")
        assert cwe_79 is not None
        assert cwe_79.get("name") == "Cross-site Scripting"

        # Test loaded CWE IDs
        loaded_ids = result.loaded_cwe_ids
        assert "CWE-79" in loaded_ids
        assert "CWE-89" in loaded_ids
        assert len(loaded_ids) == 2

    def test_add_cwe_operation(self):
        """Test adding CWE to loading result."""
        result = CweLoadingResult()
        cwe_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Cross-site Scripting",
            "category": "injection"
        }
        file_path = Path("cwe-79.yaml")

        new_result = add_cwe(result, "CWE-79", cwe_data, file_path=file_path)

        # Verify CWE was added
        assert new_result.cwe_count == 1
        assert new_result.has_cwe("CWE-79")
        assert new_result.get_cwe("CWE-79") == cwe_data
        assert new_result.loaded == 1

        # Verify original result is unchanged (immutability)
        assert result.cwe_count == 0
        assert result.loaded == 0

    def test_add_duplicate_cwe(self):
        """Test adding duplicate CWE ID."""
        # Start with one CWE
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "XSS"}
        result = add_cwe(CweLoadingResult(), "CWE-79", cwe_data)

        # Try to add duplicate
        duplicate_data: CweDataDict = {"id": "CWE-79", "name": "Different XSS"}
        file_path = Path("duplicate.yaml")

        new_result = add_cwe(result, "CWE-79", duplicate_data, file_path=file_path)

        # Should track duplicate and increment failed count
        assert new_result.cwe_count == 1  # Still only one CWE
        assert new_result.duplicate_count == 1
        assert new_result.failed == 1
        assert "CWE-79" in new_result.duplicate_ids
        assert len(new_result.warnings) > 0

    def test_track_duplicate_cwe(self):
        """Test explicit duplicate tracking."""
        result = CweLoadingResult()
        file_path = Path("duplicate.yaml")

        new_result = track_duplicate_cwe(result, "CWE-79", file_path)

        assert new_result.duplicate_count == 1
        assert new_result.duplicate_ids["CWE-79"] == file_path
        assert new_result.failed == 1
        assert len(new_result.warnings) > 0

    def test_track_invalid_file(self):
        """Test tracking invalid files."""
        result = CweLoadingResult()
        file_path = Path("invalid.yaml")
        reason = "Malformed YAML syntax"

        new_result = track_invalid_file(result, file_path, reason)

        assert new_result.invalid_file_count == 1
        assert file_path in new_result.invalid_files
        assert new_result.failed == 1
        assert any(reason in error for error in new_result.errors)

    def test_track_skipped_file(self):
        """Test tracking skipped files."""
        result = CweLoadingResult()
        file_path = Path("skipped.yaml")
        reason = "File extension not supported"

        new_result = track_skipped_cwe_file(result, file_path, reason)

        assert new_result.skipped_file_count == 1
        assert file_path in new_result.skipped_files
        assert any(reason in info for info in new_result.infos)

    def test_from_batch_conversion(self):
        """Test creating CweLoadingResult from BatchResult."""
        batch_data = {
            "CWE-79": {"id": "CWE-79", "name": "XSS"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection"}
        }
        skipped_files = (Path("readme.txt"),)

        batch_result = BatchResult(
            items=batch_data,
            skipped_files=skipped_files,
            loaded=2,
            failed=0
        )

        cwe_result = CweLoadingResult.from_batch(batch_result)

        assert cwe_result.cwe_count == 2
        assert "CWE-79" in cwe_result.cwes
        assert "CWE-89" in cwe_result.cwes
        assert cwe_result.skipped_file_count == 1
        assert cwe_result.loaded == 2


class TestCweValidationResult:
    """Test CWE validation result type and operations."""

    def test_empty_cwe_validation_result(self):
        """Test empty validation result initialization."""
        result = CweValidationResult()

        assert result.validated_count == 0
        assert result.field_error_count == 0
        assert not result.has_field_errors
        assert not result.schema_validation_used
        assert result.schema_version == ""
        assert result.get_failed_cwes() == []
        assert result.get_passed_cwes() == []

    def test_cwe_validation_result_with_data(self):
        """Test validation result with sample data."""
        validation_results = {
            "CWE-79": True,
            "CWE-89": True,
            "CWE-22": False,
            "CWE-100": False
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
            failed=2
        )

        assert result.validated_count == 4
        assert result.field_error_count == 2
        assert result.has_field_errors
        assert result.schema_validation_used
        assert result.schema_version == "1.2"

        # Test pass/fail lists
        failed_cwes = result.get_failed_cwes()
        passed_cwes = result.get_passed_cwes()

        assert "CWE-22" in failed_cwes
        assert "CWE-100" in failed_cwes
        assert "CWE-79" in passed_cwes
        assert "CWE-89" in passed_cwes

    def test_validate_cwe_success(self):
        """Test successful CWE validation."""
        result = CweValidationResult()
        cwe_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Cross-site Scripting",
            "category": "injection"
        }

        new_result = validate_cwe(result, "CWE-79", cwe_data)

        assert new_result.validated_count == 1
        assert "CWE-79" in new_result.validation_results
        assert new_result.validation_results["CWE-79"] is True
        assert new_result.passed == 1
        assert new_result.failed == 0
        assert "CWE-79" in new_result.validated_cwes

    def test_validate_cwe_failure(self):
        """Test failed CWE validation."""
        result = CweValidationResult()
        cwe_data: CweDataDict = {"id": "CWE-79"}  # Missing name

        new_result = validate_cwe(result, "CWE-79", cwe_data)

        assert new_result.validated_count == 1
        assert "CWE-79" in new_result.validation_results
        assert new_result.validation_results["CWE-79"] is False
        assert new_result.passed == 0
        assert new_result.failed == 1
        assert len(new_result.errors) > 0

    def test_validate_cwe_field(self):
        """Test individual field validation."""
        result = CweValidationResult()

        # Test successful field validation
        new_result = validate_cwe_field(
            result, "CWE-79", "name", "Cross-site Scripting", "must not be empty"
        )
        assert new_result.passed == 1

        # Test failed field validation
        failed_result = validate_cwe_field(
            new_result, "CWE-79", "description", None, "must not be None"
        )
        assert failed_result.failed == 1
        assert failed_result.field_error_count == 1
        assert "CWE-79.description" in failed_result.field_errors

    def test_batch_validate_cwes(self):
        """Test batch CWE validation."""
        result = CweValidationResult()
        cwe_dict: dict[str, CweDataDict] = {
            "CWE-79": {"id": "CWE-79", "name": "XSS", "category": "injection"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection", "category": "injection"},
            "CWE-100": {"id": "CWE-100"},  # Missing name, should fail
            "CWE-200": {"id": "CWE-200", "name": "Information Exposure"}  # Missing category, should warn but pass
        }

        new_result = batch_validate_cwes(result, cwe_dict)

        assert new_result.validated_count == 4
        assert new_result.passed >= 3  # At least 3 should pass
        assert new_result.failed >= 1   # At least 1 should fail

        # Check specific validations
        assert new_result.validation_results["CWE-79"] is True
        assert new_result.validation_results["CWE-89"] is True
        assert new_result.validation_results["CWE-100"] is False
        assert new_result.validation_results["CWE-200"] is True


class TestCweRelationshipResult:
    """Test CWE relationship result type and operations."""

    def test_empty_relationship_result(self):
        """Test empty relationship result initialization."""
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

    def test_relationship_result_with_data(self):
        """Test relationship result with sample data."""
        relationship_map = {
            "CWE-79": ["CWE-80", "CWE-81"],
            "CWE-89": ["CWE-90"]
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
            failed=1
        )

        assert result.total_relationships == 3  # Sum of relationship lists
        assert result.circular_dependency_count == 2
        assert result.orphaned_cwe_count == 1
        assert result.invalid_reference_count == 1
        assert result.has_circular_dependencies
        assert result.has_orphaned_cwes

        # Test relationship access
        assert result.get_relationships("CWE-79") == ["CWE-80", "CWE-81"]
        assert result.get_relationships("CWE-89") == ["CWE-90"]
        assert result.get_relationships("CWE-999") == []  # Non-existent

    def test_analyze_relationships(self):
        """Test relationship analysis operation."""
        result = CweRelationshipResult()
        cwe_dict: dict[str, CweDataDict] = {
            "CWE-79": cast(CweDataDict, {
                "id": "CWE-79",
                "relationships": [
                    {"cwe_id": "CWE-80", "type": "ChildOf"},
                    {"cwe_id": "CWE-999", "type": "ParentOf"}  # Invalid reference
                ]
            }),
            "CWE-80": cast(CweDataDict, {
                "id": "CWE-80",
                "relationships": [
                    {"cwe_id": "CWE-79", "type": "ParentOf"}
                ]
            }),
            "CWE-200": cast(CweDataDict, {  # Orphaned - no relationships
                "id": "CWE-200",
                "relationships": []
            })
        }

        new_result = analyze_relationships(result, cwe_dict)

        # Should detect relationships
        assert new_result.total_relationships > 0
        assert len(new_result.relationship_map) >= 2

        # Should detect invalid reference (CWE-999 doesn't exist)
        assert new_result.invalid_reference_count >= 1
        assert any("CWE-999" in ref for ref in new_result.invalid_references)

        # Should detect orphaned CWE
        assert new_result.orphaned_cwe_count >= 1
        assert "CWE-200" in new_result.orphaned_cwes

        # Should count relationship types
        assert "ChildOf" in new_result.relationship_types
        assert "ParentOf" in new_result.relationship_types

    def test_add_relationship(self):
        """Test adding individual relationships."""
        result = CweRelationshipResult()

        # Add first relationship
        new_result = add_relationship(result, "CWE-79", "CWE-80", "ChildOf")

        assert "CWE-79" in new_result.relationship_map
        assert "CWE-80" in new_result.relationship_map["CWE-79"]
        assert new_result.relationship_types["ChildOf"] == 1

        # Add another relationship to same CWE
        final_result = add_relationship(new_result, "CWE-79", "CWE-81", "ChildOf")

        assert len(final_result.relationship_map["CWE-79"]) == 2
        assert "CWE-80" in final_result.relationship_map["CWE-79"]
        assert "CWE-81" in final_result.relationship_map["CWE-79"]
        assert final_result.relationship_types["ChildOf"] == 2

    def test_circular_dependency_detection(self):
        """Test circular dependency detection through relationship analysis."""
        result = CweRelationshipResult()

        # Create CWE data with circular dependencies
        cwe_dict: dict[str, CweDataDict] = {
            "CWE-A": cast(CweDataDict, {
                "id": "CWE-A",
                "relationships": [{"cwe_id": "CWE-B", "type": "ChildOf"}]
            }),
            "CWE-B": cast(CweDataDict, {
                "id": "CWE-B",
                "relationships": [{"cwe_id": "CWE-C", "type": "ChildOf"}]
            }),
            "CWE-C": cast(CweDataDict, {
                "id": "CWE-C",
                "relationships": [{"cwe_id": "CWE-A", "type": "ChildOf"}]  # Creates cycle
            })
        }

        # Analyze relationships should detect circular dependencies
        new_result = analyze_relationships(result, cwe_dict)

        # The analysis should populate circular_dependencies
        assert len(new_result.circular_dependencies) > 0


class TestAnalysisFunctions:
    """Test CWE analysis and summary functionality."""

    def test_cwe_loading_summary_data(self):
        """Test CWE loading result data access."""
        cwes: dict[str, CweDataDict] = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "name": "XSS", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "name": "SQL Injection", "category": "injection"})
        }
        result = CweLoadingResult(
            cwes=cwes,
            duplicate_ids={"CWE-100": Path("dup.yaml")},
            invalid_files=(Path("invalid.yaml"),),
            skipped_files=(Path("skip.yaml"),),
            loaded=2,
            failed=2,
            errors=("Parse error",),
            warnings=("Duplicate warning",)
        )

        # Test direct property access instead of summary function
        assert result.cwe_count == 2
        assert result.duplicate_count == 1
        assert result.invalid_file_count == 1
        assert result.skipped_file_count == 1
        assert result.success_rate == 0.5  # 2/(2+2)
        assert result.has_errors
        assert result.has_warnings
        assert len(result.loaded_cwe_ids) == 2

    def test_cwe_validation_summary_data(self):
        """Test CWE validation result data access."""
        validation_results = {
            "CWE-79": True,
            "CWE-89": True,
            "CWE-100": False
        }
        result = CweValidationResult(
            validation_results=validation_results,
            field_errors=("field1", "field2"),
            validated_cwes=("CWE-79", "CWE-89", "CWE-100"),
            schema_validation_used=True,
            schema_version="1.0",
            passed=2,
            failed=1
        )

        # Test direct property access
        assert result.validated_count == 3
        assert result.field_error_count == 2
        assert result.has_field_errors
        assert result.schema_validation_used
        assert result.schema_version == "1.0"
        assert result.success_rate == pytest.approx(0.667, abs=0.01)  # type: ignore
        assert "CWE-100" in result.get_failed_cwes()
        assert "CWE-79" in result.get_passed_cwes()
        assert "CWE-89" in result.get_passed_cwes()

    def test_relationship_summary_data(self):
        """Test relationship result data access."""
        relationship_map = {
            "CWE-79": ["CWE-80", "CWE-81"],
            "CWE-89": ["CWE-90"]
        }
        result = CweRelationshipResult(
            relationship_map=relationship_map,
            circular_dependencies=("CWE-100", "CWE-101"),
            orphaned_cwes=("CWE-200",),
            invalid_references=("CWE-79 → CWE-999",),
            relationship_types={"ChildOf": 3, "ParentOf": 2}
        )

        # Test direct property access
        assert result.total_relationships == 3
        assert len(result.relationship_map) == 2
        assert result.circular_dependency_count == 2
        assert result.orphaned_cwe_count == 1
        assert result.invalid_reference_count == 1
        assert result.has_circular_dependencies
        assert result.has_orphaned_cwes

    def test_cwes_by_category_direct(self):
        """Test filtering CWEs by category directly."""
        cwes = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "category": "injection"}),
            "CWE-22": cast(CweDataDict, {"id": "CWE-22", "category": "path_traversal"}),
            "CWE-200": cast(CweDataDict, {"id": "CWE-200", "category": "information_disclosure"})
        }
        result = CweLoadingResult(cwes=cwes)

        # Test filtering directly
        injection_cwes = {
            cwe_id: cwe_data for cwe_id, cwe_data in result.cwes.items()
            if cwe_data.get("category") == "injection"
        }

        assert len(injection_cwes) == 2
        assert "CWE-79" in injection_cwes
        assert "CWE-89" in injection_cwes
        assert "CWE-22" not in injection_cwes

    def test_relationship_depth_calculation(self):
        """Test relationship depth calculation logic."""
        relationship_map = {
            "CWE-1": ["CWE-2"],
            "CWE-2": ["CWE-3"],
            "CWE-3": ["CWE-4"],
            "CWE-4": []
        }
        result = CweRelationshipResult(relationship_map=relationship_map)

        # Test basic depth logic
        assert len(result.get_relationships("CWE-1")) == 1
        assert len(result.get_relationships("CWE-2")) == 1
        assert len(result.get_relationships("CWE-4")) == 0


class TestResultImmutability:
    """Test that result operations maintain immutability."""

    def test_cwe_loading_result_immutability(self):
        """Test CWE loading result immutability."""
        original = CweLoadingResult(loaded=1, failed=0)
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "XSS"}

        new_result = add_cwe(original, "CWE-79", cwe_data)

        # Original should be unchanged
        assert original.cwe_count == 0
        assert original.loaded == 1

        # New result should have changes
        assert new_result.cwe_count == 1
        assert new_result.loaded == 2

    def test_cwe_validation_result_immutability(self):
        """Test CWE validation result immutability."""
        original = CweValidationResult(passed=1)
        cwe_data: CweDataDict = {"id": "CWE-79", "name": "XSS"}

        new_result = validate_cwe(original, "CWE-79", cwe_data)

        # Original should be unchanged
        assert original.validated_count == 0
        assert original.passed == 1

        # New result should have changes
        assert new_result.validated_count == 1
        assert new_result.passed == 2

    def test_cwe_relationship_result_immutability(self):
        """Test CWE relationship result immutability."""
        original = CweRelationshipResult()

        new_result = add_relationship(original, "CWE-79", "CWE-80", "ChildOf")

        # Original should be unchanged
        assert original.total_relationships == 0
        assert len(original.relationship_map) == 0

        # New result should have changes
        assert new_result.total_relationships == 1
        assert len(new_result.relationship_map) == 1


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_cwe_data_validation(self):
        """Test validation with empty CWE data."""
        result = CweValidationResult()
        empty_data: CweDataDict = {}

        new_result = validate_cwe(result, "CWE-EMPTY", empty_data)

        # Should fail validation
        assert new_result.validation_results["CWE-EMPTY"] is False
        assert new_result.failed == 1

    def test_none_field_validation(self):
        """Test field validation with None values."""
        result = CweValidationResult()

        new_result = validate_cwe_field(result, "CWE-79", "name", None, "required field")

        assert new_result.failed == 1
        assert new_result.field_error_count == 1

    def test_empty_relationship_analysis(self):
        """Test relationship analysis with empty data."""
        result = CweRelationshipResult()
        empty_cwe_dict: dict[str, CweDataDict] = {}

        new_result = analyze_relationships(result, empty_cwe_dict)

        # Should handle empty input gracefully
        assert new_result.total_relationships == 0
        assert len(new_result.relationship_map) == 0

    def test_malformed_relationship_data(self):
        """Test relationship analysis with malformed data."""
        result = CweRelationshipResult()
        malformed_dict = {
            "CWE-79": {
                "id": "CWE-79",
                "relationships": [
                    {"type": "ChildOf"},  # Missing cwe_id
                    {"cwe_id": "CWE-80"}, # Missing type
                    {}                    # Empty relationship
                ]
            }
        }
        # Cast each value to CweDataDict to satisfy type checker
        malformed_cwe_dict: dict[str, CweDataDict] = {
            k: cast(CweDataDict, v) for k, v in malformed_dict.items()
        }

        # Should handle malformed data without crashing
        new_result = analyze_relationships(result, malformed_cwe_dict)
        assert isinstance(new_result, CweRelationshipResult)

    def test_large_dataset_performance(self):
        """Test performance with large datasets."""
        result = CweLoadingResult()

        # Add many CWEs efficiently
        for i in range(100):
            cwe_id = f"CWE-{i:04d}"
            cwe_data: CweDataDict = {"id": cwe_id, "name": f"Test CWE {i}"}
            result = add_cwe(result, cwe_id, cwe_data)

        assert result.cwe_count == 100
        assert result.loaded == 100

        # Test summary generation performance
        summary = get_cwe_loading_summary(result)
        assert summary["cwes_loaded"] == 100

    def test_unicode_handling(self):
        """Test handling of unicode in CWE data."""
        result = CweLoadingResult()
        unicode_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Скрипт межсайтовых атак",  # Russian
            "category": "注入攻击"  # Chinese
        }

        new_result = add_cwe(result, "CWE-79", unicode_data)

        assert new_result.cwe_count == 1
        retrieved = new_result.get_cwe("CWE-79")
        assert retrieved is not None
        assert retrieved.get("name") == "Скрипт межсайтовых атак"

    def test_path_handling(self):
        """Test handling of complex file paths."""
        result = CweLoadingResult()
        complex_path = Path("some") / "deeply" / "nested" / "path with spaces" / "cwe-79.yaml"

        new_result = track_invalid_file(result, complex_path, "Test reason")

        assert new_result.invalid_file_count == 1
        assert complex_path in new_result.invalid_files


class TestResultConversions:
    """Test result type conversions and integrations."""

    def test_batch_to_cwe_conversion(self):
        """Test converting BatchResult to CweLoadingResult."""
        batch_data = {
            "CWE-79": {"id": "CWE-79", "name": "XSS"},
            "CWE-89": {"id": "CWE-89", "name": "SQLi"}
        }

        batch_result = BatchResult(
            items=batch_data,
            loaded=2,
            failed=0,
            skipped_files=(Path("README.md"),)
        )

        cwe_result = CweLoadingResult.from_batch(batch_result)

        assert cwe_result.cwe_count == 2
        assert "CWE-79" in cwe_result.cwes
        assert "CWE-89" in cwe_result.cwes
        assert cwe_result.skipped_file_count == 1
        assert cwe_result.loaded == 2
        assert cwe_result.failed == 0

    def test_loading_to_validation_context(self):
        """Test using loading result context in validation."""
        # Create loading result
        cwes = {
            "CWE-79": cast(CweDataDict, {"id": "CWE-79", "name": "XSS", "category": "injection"}),
            "CWE-89": cast(CweDataDict, {"id": "CWE-89", "name": "SQLi", "category": "injection"})
        }
        loading_result = CweLoadingResult(cwes=cwes, loaded=2)

        # Use in validation
        validation_result = CweValidationResult()
        final_result = batch_validate_cwes(validation_result, loading_result.cwes)

        assert final_result.validated_count == 2
        assert final_result.passed == 2  # Both should pass


class TestDataStructures:
    """Test typed data structures."""

    def test_cwe_data_dict_structure(self):
        """Test CWE data dictionary structure."""
        cwe_data: CweDataDict = {
            "id": "CWE-79",
            "name": "Cross-site Scripting",
            "category": "injection",
            "relationships": [
                {"cwe_id": "CWE-80", "type": "ChildOf"}
            ]
        }

        assert cwe_data["id"] == "CWE-79"
        assert cwe_data["name"] == "Cross-site Scripting"
        assert cwe_data["category"] == "injection"
        assert len(cwe_data["relationships"]) == 1
        relationships = cwe_data.get("relationships", [])
        assert relationships and relationships[0].get("cwe_id", "") == "CWE-80"

    def test_cwe_relationship_dict_structure(self):
        """Test CWE relationship dictionary structure."""
        relationship: CweRelationshipDict = {
            "cwe_id": "CWE-80",
            "type": "ChildOf"
        }

        assert relationship.get("cwe_id") == "CWE-80"
        assert relationship.get("type") == "ChildOf"
