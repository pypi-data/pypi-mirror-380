"""Tests for Standards result types and operations.

Tests for standards loading, validation, and mapping result types
including all operations and analysis functions.
"""

from pathlib import Path
from typing import cast

from ci.transparency.cwe.types.standards.results import (
    # Result types
    StandardsLoadingResult,
    StandardsValidationResult,
    StandardsMappingResult,
    StandardsDataDict,
    StandardsControlDict,
    StandardsMappingDict,

    # Loading operations
    add_standard,
    track_duplicate_standard,
    track_invalid_standards_file,
    track_skipped_standards_file,

    # Validation operations
    validate_standard,
    validate_standards_field,
    batch_validate_standards,

    # Mapping operations
    analyze_mappings,
    add_mapping,

    # Analysis functions
    get_standards_loading_summary,
    get_standards_validation_summary,
    get_mapping_summary,
    get_standards_by_framework,
    get_control_count,
    get_mapping_coverage,
)

from ci.transparency.cwe.types.batch import BatchResult


class TestStandardsLoadingResult:
    """Test standards loading result type and operations."""

    def test_empty_standards_loading_result(self):
        """Test empty standards loading result initialization."""
        result = StandardsLoadingResult()

        # Test basic properties
        assert result.standards_count == 0
        assert result.loaded_standard_ids == ()
        assert result.framework_count == 0
        assert result.invalid_file_count == 0
        assert result.skipped_file_count == 0
        assert result.duplicate_count == 0

        # Test boolean properties
        assert not result.has_duplicates

        # Test dictionaries are empty
        assert len(result.standards) == 0
        assert len(result.frameworks) == 0
        assert len(result.invalid_files) == 0
        assert len(result.skipped_files) == 0
        assert len(result.duplicate_standards) == 0

    def test_standards_loading_result_with_data(self):
        """Test standards loading result with sample data."""
        standards: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {
                "id": "NIST-SP-800-53",
                "name": "Security Controls for Federal Information Systems",
                "framework": "NIST",
                "version": "Rev 5"
            }),
            "ISO-27001": cast(StandardsDataDict, {
                "id": "ISO-27001",
                "name": "Information Security Management",
                "framework": "ISO",
                "version": "2013"
            })
        }
        frameworks = {"NIST": 1, "ISO": 1}
        invalid_files = (Path("invalid.yaml"), Path("malformed.json"))
        skipped_files = (Path("readme.txt"),)
        duplicate_standards = ("DUPLICATE-STD",)

        result = StandardsLoadingResult(
            standards=standards,
            frameworks=frameworks,
            invalid_files=invalid_files,
            skipped_files=skipped_files,
            duplicate_standards=duplicate_standards,
            loaded=2,
            failed=3
        )

        # Test counts
        assert result.standards_count == 2
        assert result.framework_count == 2
        assert result.invalid_file_count == 2
        assert result.skipped_file_count == 1
        assert result.duplicate_count == 1

        # Test boolean properties
        assert result.has_duplicates

        # Test standards access
        assert result.has_standard("NIST-SP-800-53")
        assert result.has_standard("ISO-27001")
        assert not result.has_standard("NONEXISTENT")

        # Test standards retrieval
        nist_std = result.get_standard("NIST-SP-800-53")
        assert nist_std is not None
        assert nist_std.get("framework") == "NIST"
        assert nist_std.get("version") == "Rev 5"

        # Test loaded standards IDs
        loaded_ids = result.loaded_standard_ids
        assert "NIST-SP-800-53" in loaded_ids
        assert "ISO-27001" in loaded_ids
        assert len(loaded_ids) == 2

        # Test frameworks
        frameworks_list = result.get_frameworks()
        assert "NIST" in frameworks_list
        assert "ISO" in frameworks_list

    def test_add_standard_operation(self):
        """Test adding standard to loading result."""
        result = StandardsLoadingResult()
        standards_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "NIST-SP-800-53",
            "name": "Security Controls",
            "framework": "NIST",
            "version": "Rev 5"
        })
        file_path = Path("nist-sp-800-53.yaml")

        new_result = add_standard(result, "NIST-SP-800-53", standards_data, file_path=file_path)

        # Verify standard was added
        assert new_result.standards_count == 1
        assert new_result.has_standard("NIST-SP-800-53")
        assert new_result.get_standard("NIST-SP-800-53") == standards_data
        assert new_result.loaded == 1

        # Verify framework tracking
        assert new_result.framework_count == 1
        assert "NIST" in new_result.frameworks
        assert new_result.frameworks["NIST"] == 1

        # Verify original result is unchanged (immutability)
        assert result.standards_count == 0
        assert result.loaded == 0

    def test_add_duplicate_standard(self):
        """Test adding duplicate standard ID."""
        # Start with one standard
        standards_data: StandardsDataDict = cast(StandardsDataDict, {"id": "NIST-SP-800-53", "name": "Security Controls", "framework": "NIST"})
        result = add_standard(StandardsLoadingResult(), "NIST-SP-800-53", standards_data)

        # Try to add duplicate
        duplicate_data: StandardsDataDict = cast(StandardsDataDict, {"id": "NIST-SP-800-53", "name": "Different Standard", "framework": "NIST"})

        new_result = add_standard(result, "NIST-SP-800-53", duplicate_data)

        # Should track duplicate and increment failed count
        assert new_result.standards_count == 1  # Still only one standard
        assert new_result.duplicate_count == 1
        assert new_result.failed == 1
        assert "NIST-SP-800-53" in new_result.duplicate_standards
        assert len(new_result.warnings) > 0

    def test_track_duplicate_standard(self):
        """Test explicit duplicate tracking."""
        result = StandardsLoadingResult()
        reason = "Already loaded from different directory"

        new_result = track_duplicate_standard(result, "ISO-27001", reason)

        assert new_result.duplicate_count == 1
        assert "ISO-27001" in new_result.duplicate_standards
        assert new_result.failed == 1
        assert any(reason in warning for warning in new_result.warnings)

    def test_track_invalid_standards_file(self):
        """Test tracking invalid standards files."""
        result = StandardsLoadingResult()
        file_path = Path("invalid.yaml")
        reason = "Malformed YAML structure"

        new_result = track_invalid_standards_file(result, file_path, reason)

        assert new_result.invalid_file_count == 1
        assert file_path in new_result.invalid_files
        assert new_result.failed == 1
        assert any(reason in error for error in new_result.errors)

    def test_track_skipped_standards_file(self):
        """Test tracking skipped standards files."""
        result = StandardsLoadingResult()
        file_path = Path("readme.txt")
        reason = "Non-standards file"

        new_result = track_skipped_standards_file(result, file_path, reason)

        assert new_result.skipped_file_count == 1
        assert file_path in new_result.skipped_files
        assert any(reason in info for info in new_result.infos)

    def test_from_batch_conversion(self):
        """Test creating StandardsLoadingResult from BatchResult."""
        batch_data = {
            "NIST-SP-800-53": {"id": "NIST-SP-800-53", "framework": "NIST"},
            "ISO-27001": {"id": "ISO-27001", "framework": "ISO"}
        }
        skipped_files = (Path("readme.txt"),)

        batch_result = BatchResult(
            items=batch_data,
            skipped_files=skipped_files,
            loaded=2,
            failed=0
        )

        standards_result = StandardsLoadingResult.from_batch(batch_result)

        assert standards_result.standards_count == 2
        assert "NIST-SP-800-53" in standards_result.standards
        assert "ISO-27001" in standards_result.standards
        assert standards_result.skipped_file_count == 1
        assert standards_result.loaded == 2

    def test_framework_tracking_with_multiple_standards(self):
        """Test framework counting with multiple standards."""
        result = StandardsLoadingResult()

        # Add multiple NIST standards
        for i in range(3):
            data: StandardsDataDict = cast(StandardsDataDict, {"id": f"NIST-{i}", "framework": "NIST"})
            result = add_standard(result, f"NIST-{i}", data)

        # Add one ISO standard
        iso_data: StandardsDataDict = cast(StandardsDataDict, {"id": "ISO-27001", "framework": "ISO"})
        result = add_standard(result, "ISO-27001", iso_data)

        assert result.framework_count == 2
        assert result.frameworks["NIST"] == 3
        assert result.frameworks["ISO"] == 1

    def test_framework_tracking_with_unknown(self):
        """Test framework tracking with missing framework field."""
        result = StandardsLoadingResult()
        data_without_framework: StandardsDataDict = cast(StandardsDataDict, {"id": "UNKNOWN-STD", "name": "Unknown Standard"})

        new_result = add_standard(result, "UNKNOWN-STD", data_without_framework)

        assert new_result.framework_count == 1
        assert "unknown" in new_result.frameworks
        assert new_result.frameworks["unknown"] == 1


class TestStandardsValidationResult:
    """Test standards validation result type and operations."""

    def test_empty_standards_validation_result(self):
        """Test empty validation result initialization."""
        result = StandardsValidationResult()

        assert result.validated_count == 0
        assert result.field_error_count == 0
        assert result.constraint_violation_count == 0
        assert result.control_validation_count == 0
        assert not result.has_field_errors
        assert not result.has_constraint_violations
        assert result.get_failed_standards() == []
        assert result.get_passed_standards() == []

    def test_standards_validation_result_with_data(self):
        """Test validation result with sample data."""
        validation_results = {
            "NIST-SP-800-53": True,
            "ISO-27001": True,
            "INVALID-STD": False,
            "INCOMPLETE-STD": False
        }
        field_errors = ("INVALID-STD.name", "INCOMPLETE-STD.controls")
        constraint_violations = ("INVALID-STD: too many controls",)
        validated_standards = ("NIST-SP-800-53", "ISO-27001", "INVALID-STD", "INCOMPLETE-STD")

        result = StandardsValidationResult(
            validation_results=validation_results,
            field_errors=field_errors,
            constraint_violations=constraint_violations,
            validated_standards=validated_standards,
            control_validation_count=150,
            passed=2,
            failed=2
        )

        assert result.validated_count == 4
        assert result.field_error_count == 2
        assert result.constraint_violation_count == 1
        assert result.control_validation_count == 150
        assert result.has_field_errors
        assert result.has_constraint_violations

        # Test pass/fail lists
        failed_standards = result.get_failed_standards()
        passed_standards = result.get_passed_standards()

        assert "INVALID-STD" in failed_standards
        assert "INCOMPLETE-STD" in failed_standards
        assert "NIST-SP-800-53" in passed_standards
        assert "ISO-27001" in passed_standards

    def test_validate_standard_success(self):
        """Test successful standard validation."""
        result = StandardsValidationResult()
        standards_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "NIST-SP-800-53",
            "name": "Security Controls",
            "framework": "NIST",
            "controls": [
                {"id": "AC-1", "title": "Access Control Policy"},
                {"id": "AC-2", "title": "Account Management"}
            ]
        })

        new_result = validate_standard(result, "NIST-SP-800-53", standards_data)

        assert new_result.validated_count == 1
        assert "NIST-SP-800-53" in new_result.validation_results
        assert new_result.validation_results["NIST-SP-800-53"] is True
        assert new_result.passed == 1
        assert new_result.failed == 0
        assert new_result.control_validation_count == 2
        assert "NIST-SP-800-53" in new_result.validated_standards

    def test_validate_standard_failure(self):
        """Test failed standard validation."""
        result = StandardsValidationResult()
        standards_data: StandardsDataDict = cast(StandardsDataDict, {"id": "INVALID-STD"})  # Missing name and framework

        new_result = validate_standard(result, "INVALID-STD", standards_data)

        assert new_result.validated_count == 1
        assert "INVALID-STD" in new_result.validation_results
        assert new_result.validation_results["INVALID-STD"] is False
        assert new_result.passed == 0
        assert new_result.failed == 1
        assert len(new_result.errors) > 0

        # Should have errors for missing name
        error_messages = " ".join(new_result.errors)
        assert "Missing name" in error_messages

    def test_validate_standard_with_controls(self):
        """Test standard validation with controls validation."""
        result = StandardsValidationResult()
        standards_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "TEST-STD",
            "name": "Test Standard",
            "framework": "TEST",
            "controls": [
                {"id": "C1", "title": "Control 1"},
                {},  # Missing ID - should cause validation error
                {"id": "C3", "title": "Control 3"}
            ]
        })

        new_result = validate_standard(result, "TEST-STD", standards_data)

        # Should fail due to control with missing ID
        assert new_result.validation_results["TEST-STD"] is False
        assert new_result.failed == 1
        assert new_result.control_validation_count == 2  # Only valid controls counted

        # Should have error about missing control ID
        error_messages = " ".join(new_result.errors)
        assert "Control missing ID" in error_messages

    def test_validate_standards_field(self):
        """Test individual field validation."""
        result = StandardsValidationResult()

        # Test successful field validation
        new_result = validate_standards_field(
            result, "NIST-SP-800-53", "name", "Security Controls", "must not be empty"
        )
        assert new_result.passed == 1

        # Test failed field validation
        failed_result = validate_standards_field(
            new_result, "NIST-SP-800-53", "version", None, "must not be None"
        )
        assert failed_result.failed == 1
        assert failed_result.field_error_count == 1
        assert "NIST-SP-800-53.version" in failed_result.field_errors

    def test_batch_validate_standards(self):
        """Test batch standards validation."""
        result = StandardsValidationResult()
        standards_dict: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {
                "id": "NIST-SP-800-53",
                "name": "Security Controls",
                "framework": "NIST"
            }),
            "ISO-27001": cast(StandardsDataDict, {
                "id": "ISO-27001",
                "name": "Information Security",
                "framework": "ISO"
            }),
            "INVALID-STD": cast(StandardsDataDict, {"id": "INVALID-STD"}),  # Missing name, should fail
            "GOOD-STD": cast(StandardsDataDict, {
                "id": "GOOD-STD",
                "name": "Good Standard"
                # Missing framework, should warn but pass
            })
        }

        new_result = batch_validate_standards(result, standards_dict)

        assert new_result.validated_count == 4
        assert new_result.passed >= 3  # At least 3 should pass
        assert new_result.failed >= 1   # At least 1 should fail

        # Check specific validations
        assert new_result.validation_results["NIST-SP-800-53"] is True
        assert new_result.validation_results["ISO-27001"] is True
        assert new_result.validation_results["INVALID-STD"] is False
        assert new_result.validation_results["GOOD-STD"] is True


class TestStandardsMappingResult:
    """Test standards mapping result type and operations."""

    def test_empty_mapping_result(self):
        """Test empty mapping result initialization."""
        result = StandardsMappingResult()

        assert result.total_mappings == 0
        assert result.invalid_mapping_count == 0
        assert result.duplicate_mapping_count == 0
        assert result.orphaned_control_count == 0
        assert not result.has_invalid_mappings
        assert not result.has_orphaned_controls

        assert len(result.mapping_results) == 0
        assert len(result.invalid_mappings) == 0
        assert len(result.duplicate_mappings) == 0
        assert len(result.orphaned_controls) == 0
        assert len(result.mapping_types) == 0

    def test_mapping_result_with_data(self):
        """Test mapping result with sample data."""
        mapping_results = {
            "NIST-SP-800-53": ["CWE-79", "CWE-89", "CWE-22"],
            "ISO-27001": ["CWE-200"]
        }
        invalid_mappings = ("NIST-SP-800-53:AC-1 → CWE-999",)
        duplicate_mappings = ("CWE-79 ← NIST-SP-800-53:AC-1, ISO-27001:A.9.1.1",)
        orphaned_controls = ("COBIT:APO01.01",)
        mapping_types = {"cwe": 4, "capec": 1}

        result = StandardsMappingResult(
            mapping_results=mapping_results,
            invalid_mappings=invalid_mappings,
            duplicate_mappings=duplicate_mappings,
            orphaned_controls=orphaned_controls,
            mapping_types=mapping_types,
            passed=4,
            failed=1
        )

        assert result.total_mappings == 4  # Sum of mapping lists
        assert result.invalid_mapping_count == 1
        assert result.duplicate_mapping_count == 1
        assert result.orphaned_control_count == 1
        assert result.has_invalid_mappings
        assert result.has_orphaned_controls

        # Test mapping access
        assert result.get_mappings("NIST-SP-800-53") == ["CWE-79", "CWE-89", "CWE-22"]
        assert result.get_mappings("ISO-27001") == ["CWE-200"]
        assert result.get_mappings("NONEXISTENT") == []

    def test_analyze_mappings_basic(self):
        """Test basic mapping analysis operation."""
        result = StandardsMappingResult()
        standards_dict: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {
                "id": "NIST-SP-800-53",
                "controls": [
                    {
                        "id": "AC-1",
                        "mappings": [
                            {"target_id": "CWE-79", "mapping_type": "cwe"},
                            {"target_id": "CWE-89", "mapping_type": "cwe"}
                        ]
                    }
                ]
            }),
            "ISO-27001": cast(StandardsDataDict, {
                "id": "ISO-27001",
                "controls": [
                    {
                        "id": "A.9.1.1",
                        "mappings": [
                            {"target_id": "CWE-200", "mapping_type": "cwe"}
                        ]
                    }
                ]
            })
        }

        new_result = analyze_mappings(result, standards_dict)

        # Should detect mappings
        assert new_result.total_mappings == 3
        assert len(new_result.mapping_results) == 2
        assert "NIST-SP-800-53" in new_result.mapping_results
        assert "ISO-27001" in new_result.mapping_results

        # Should count mapping types
        assert new_result.mapping_types["cwe"] == 3

    def test_analyze_mappings_with_validation(self):
        """Test mapping analysis with target validation."""
        result = StandardsMappingResult()
        standards_dict: dict[str, StandardsDataDict] = {
            "TEST-STD": cast(StandardsDataDict, {
                "id": "TEST-STD",
                "controls": [
                    {
                        "id": "C1",
                        "mappings": [
                            {"target_id": "CWE-79", "mapping_type": "cwe"},     # Valid
                            {"target_id": "CWE-999", "mapping_type": "cwe"}    # Invalid
                        ]
                    }
                ]
            })
        }
        valid_targets = {"CWE-79", "CWE-89", "CWE-22"}  # CWE-999 not included

        new_result = analyze_mappings(result, standards_dict, valid_targets)

        # Should detect invalid mapping
        assert new_result.invalid_mapping_count == 1
        assert any("CWE-999" in mapping for mapping in new_result.invalid_mappings)
        assert new_result.failed == 1

    def test_analyze_mappings_orphaned_controls(self):
        """Test detection of orphaned controls (no mappings)."""
        result = StandardsMappingResult()
        standards_dict: dict[str, StandardsDataDict] = {
            "TEST-STD": cast(StandardsDataDict, {
                "id": "TEST-STD",
                "controls": [
                    {
                        "id": "C1",
                        "mappings": [{"target_id": "CWE-79", "mapping_type": "cwe"}]
                    },
                    {
                        "id": "C2",
                        "mappings": []  # No mappings - orphaned
                    },
                    {
                        "id": "C3"
                        # No mappings field - orphaned
                    }
                ]
            })
        }

        new_result = analyze_mappings(result, standards_dict)

        # Should detect orphaned controls
        assert new_result.orphaned_control_count == 2
        assert any("TEST-STD:C2" in control for control in new_result.orphaned_controls)
        assert any("TEST-STD:C3" in control for control in new_result.orphaned_controls)

    def test_add_mapping(self):
        """Test adding individual mappings."""
        result = StandardsMappingResult()

        # Add first mapping
        new_result = add_mapping(result, "NIST-SP-800-53", "CWE-79", "cwe")

        assert "NIST-SP-800-53" in new_result.mapping_results
        assert "CWE-79" in new_result.mapping_results["NIST-SP-800-53"]
        assert new_result.mapping_types["cwe"] == 1

        # Add another mapping to same standard
        final_result = add_mapping(new_result, "NIST-SP-800-53", "CWE-89", "cwe")

        assert len(final_result.mapping_results["NIST-SP-800-53"]) == 2
        assert "CWE-79" in final_result.mapping_results["NIST-SP-800-53"]
        assert "CWE-89" in final_result.mapping_results["NIST-SP-800-53"]
        assert final_result.mapping_types["cwe"] == 2


class TestAnalysisFunctions:
    """Test standards analysis and summary functions."""

    def test_get_standards_loading_summary(self):
        """Test standards loading summary generation."""
        standards: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {"id": "NIST-SP-800-53", "framework": "NIST"}),
            "ISO-27001": cast(StandardsDataDict, {"id": "ISO-27001", "framework": "ISO"}),
            "COBIT-2019": cast(StandardsDataDict, {"id": "COBIT-2019", "framework": "ISACA"})
        }
        frameworks = {"NIST": 1, "ISO": 1, "ISACA": 1}
        result = StandardsLoadingResult(
            standards=standards,
            frameworks=frameworks,
            duplicate_standards=("DUP-STD",),
            invalid_files=(Path("invalid.yaml"),),
            skipped_files=(Path("readme.txt"),),
            loaded=3,
            failed=2,
            errors=("Parse error",),
            warnings=("Duplicate warning",)
        )

        summary = get_standards_loading_summary(result)

        assert summary["standards_loaded"] == 3
        assert summary["successful_loads"] == 3
        assert summary["failed_loads"] == 2
        assert summary["frameworks_detected"] == 3
        assert summary["frameworks"] == {"NIST": 1, "ISO": 1, "ISACA": 1}
        assert summary["duplicate_standards"] == 1
        assert summary["invalid_files"] == 1
        assert summary["skipped_files"] == 1
        assert summary["success_rate_percent"] == 60.0  # 3/(3+2)
        assert summary["loaded_standard_ids"] == ["NIST-SP-800-53", "ISO-27001", "COBIT-2019"]
        assert summary["has_errors"] is True
        assert summary["has_warnings"] is True

    def test_get_standards_validation_summary(self):
        """Test standards validation summary generation."""
        validation_results = {
            "NIST-SP-800-53": True,
            "ISO-27001": True,
            "INVALID-STD": False
        }
        result = StandardsValidationResult(
            validation_results=validation_results,
            field_errors=("field1", "field2"),
            constraint_violations=("constraint1",),
            control_validation_count=45,
            passed=2,
            failed=1
        )

        summary = get_standards_validation_summary(result)

        assert summary["standards_validated"] == 3
        assert summary["validation_passed"] == 2
        assert summary["validation_failed"] == 1
        assert summary["field_errors"] == 2
        assert summary["constraint_violations"] == 1
        assert summary["controls_validated"] == 45
        assert abs(summary["success_rate_percent"] - 66.67) < 0.1
        assert "INVALID-STD" in summary["failed_standards"]
        assert "NIST-SP-800-53" in summary["passed_standards"]
        assert "ISO-27001" in summary["passed_standards"]

    def test_get_mapping_summary(self):
        """Test mapping summary generation."""
        mapping_results = {
            "NIST-SP-800-53": ["CWE-79", "CWE-89"],
            "ISO-27001": ["CWE-200"]
        }
        result = StandardsMappingResult(
            mapping_results=mapping_results,
            invalid_mappings=("NIST:AC-1 → CWE-999",),
            duplicate_mappings=("CWE-79 ← NIST:AC-1, ISO:A.9.1.1",),
            orphaned_controls=("COBIT:APO01.01",),
            mapping_types={"cwe": 3, "capec": 1}
        )

        summary = get_mapping_summary(result)

        assert summary["total_mappings"] == 3
        assert summary["mapped_standards"] == 2
        assert summary["mapping_types"] == {"cwe": 3, "capec": 1}
        assert summary["invalid_mappings"] == ["NIST:AC-1 → CWE-999"]
        assert summary["duplicate_mappings"] == ["CWE-79 ← NIST:AC-1, ISO:A.9.1.1"]
        assert summary["orphaned_controls"] == ["COBIT:APO01.01"]
        assert summary["has_invalid_mappings"] is True
        assert summary["has_orphaned_controls"] is True

        # Test mapping coverage rate calculation
        # 2 mapped standards, 1 orphaned control = 2/3 coverage
        expected_coverage = 2 / 3
        assert abs(summary["mapping_coverage_rate"] - expected_coverage) < 0.01

    def test_get_standards_by_framework(self):
        """Test filtering standards by framework."""
        standards: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {"id": "NIST-SP-800-53", "framework": "NIST"}),
            "NIST-SP-800-171": cast(StandardsDataDict, {"id": "NIST-SP-800-171", "framework": "NIST"}),
            "ISO-27001": cast(StandardsDataDict, {"id": "ISO-27001", "framework": "ISO"}),
            "COBIT-2019": cast(StandardsDataDict, {"id": "COBIT-2019", "framework": "ISACA"})
        }
        result = StandardsLoadingResult(standards=standards)

        nist_standards = get_standards_by_framework(result, "NIST")

        assert len(nist_standards) == 2
        assert "NIST-SP-800-53" in nist_standards
        assert "NIST-SP-800-171" in nist_standards
        assert "ISO-27001" not in nist_standards

        # Test non-existent framework
        empty_standards = get_standards_by_framework(result, "NONEXISTENT")
        assert len(empty_standards) == 0

    def test_get_control_count(self):
        """Test total control count calculation."""
        standards: dict[str, StandardsDataDict] = {
            "NIST-SP-800-53": cast(StandardsDataDict, {
                "id": "NIST-SP-800-53",
                "controls": [
                    {"id": "AC-1"}, {"id": "AC-2"}, {"id": "AC-3"}
                ]
            }),
            "ISO-27001": cast(StandardsDataDict, {
                "id": "ISO-27001",
                "controls": [
                    {"id": "A.9.1.1"}, {"id": "A.9.1.2"}
                ]
            }),
            "NO-CONTROLS": cast(StandardsDataDict, {
                "id": "NO-CONTROLS"
                # No controls field
            })
        }
        result = StandardsLoadingResult(standards=standards)

        total_controls = get_control_count(result)

        assert total_controls == 5  # 3 + 2 + 0

    def test_get_mapping_coverage(self):
        """Test mapping coverage calculation."""
        # Test with some mapped and some orphaned
        mapping_results = {"STD1": ["CWE-79"], "STD2": ["CWE-89"]}
        orphaned_controls = ("STD3:C1",)

        result = StandardsMappingResult(
            mapping_results=mapping_results,
            orphaned_controls=orphaned_controls
        )

        coverage = get_mapping_coverage(result)
        expected = 2 / 3  # 2 mapped standards, 1 orphaned
        assert abs(coverage - expected) < 0.01

        # Test with no mappings or orphaned controls
        empty_result = StandardsMappingResult()
        empty_coverage = get_mapping_coverage(empty_result)
        assert empty_coverage == 1.0  # 100% coverage when nothing to map


class TestResultImmutability:
    """Test that result operations maintain immutability."""

    def test_standards_loading_result_immutability(self):
        """Test standards loading result immutability."""
        original = StandardsLoadingResult(loaded=1, failed=0)
        standards_data: StandardsDataDict = cast(StandardsDataDict, {"id": "TEST-STD", "name": "Test", "framework": "TEST"})

        new_result = add_standard(original, "TEST-STD", standards_data)

        # Original should be unchanged
        assert original.standards_count == 0
        assert original.loaded == 1

        # New result should have changes
        assert new_result.standards_count == 1
        assert new_result.loaded == 2

    def test_standards_validation_result_immutability(self):
        """Test standards validation result immutability."""
        original = StandardsValidationResult(passed=1)
        standards_data: StandardsDataDict = cast(StandardsDataDict, {"id": "TEST-STD", "name": "Test", "framework": "TEST"})

        new_result = validate_standard(original, "TEST-STD", standards_data)

        # Original should be unchanged
        assert original.validated_count == 0
        assert original.passed == 1

        # New result should have changes
        assert new_result.validated_count == 1
        assert new_result.passed == 2

    def test_standards_mapping_result_immutability(self):
        """Test standards mapping result immutability."""
        original = StandardsMappingResult()

        new_result = add_mapping(original, "TEST-STD", "CWE-79", "cwe")

        # Original should be unchanged
        assert original.total_mappings == 0
        assert len(original.mapping_results) == 0

        # New result should have changes
        assert new_result.total_mappings == 1
        assert len(new_result.mapping_results) == 1


class TestDataStructures:
    """Test typed data structures."""

    def test_standards_data_dict_structure(self):
        """Test standards data dictionary structure."""
        standards_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "NIST-SP-800-53",
            "name": "Security and Privacy Controls",
            "framework": "NIST",
            "version": "Rev 5",
            "controls": [
                {
                    "id": "AC-1",
                    "title": "Policy and Procedures",
                    "description": "Access control policy and procedures",
                    "mappings": [
                        {"target_id": "CWE-79", "mapping_type": "cwe", "confidence": "high"}
                    ]
                }
            ]
        })

        assert standards_data.get("id") == "NIST-SP-800-53"
        assert standards_data.get("framework") == "NIST"
        assert len(standards_data.get("controls", [])) == 1

        control = standards_data.get("controls", [])[0]
        assert control.get("id") == "AC-1"
        assert len(control.get("mappings", [])) == 1

        mapping = control.get("mappings", [])[0]
        assert mapping.get("target_id") == "CWE-79"
        assert mapping.get("mapping_type") == "cwe"
        assert mapping.get("confidence") == "high"

    def test_standards_control_dict_structure(self):
        """Test standards control dictionary structure."""
        control: StandardsControlDict = cast(StandardsControlDict, {
            "id": "AC-1",
            "title": "Access Control Policy and Procedures",
            "description": "Policy and procedures for access control",
            "mappings": [
                {"target_id": "CWE-284", "mapping_type": "cwe"}
            ]
        })

        assert control.get("id") == "AC-1"
        assert len(control.get("mappings", [])) == 1
        assert control.get("mappings", [])[0].get("target_id") == "CWE-284"

    def test_standards_mapping_dict_structure(self):
        """Test standards mapping dictionary structure."""
        mapping: StandardsMappingDict = cast(StandardsMappingDict, {
            "target_id": "CWE-79",
            "mapping_type": "cwe",
            "confidence": "medium"
        })

        assert mapping.get("target_id") == "CWE-79"
        assert mapping.get("mapping_type") == "cwe"
        assert mapping.get("confidence") == "medium"


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_standards_data_validation(self):
        """Test validation with empty standards data."""
        result = StandardsValidationResult()
        empty_data: StandardsDataDict = cast(StandardsDataDict, {})

        new_result = validate_standard(result, "EMPTY-STD", empty_data)

        # Should fail validation
        assert new_result.validation_results["EMPTY-STD"] is False
        assert new_result.failed == 1

    def test_malformed_mapping_data(self):
        """Test mapping analysis with malformed data."""
        result = StandardsMappingResult()
        malformed_dict: dict[str, StandardsDataDict] = {
            "BAD-STD": cast(StandardsDataDict, {
                "id": "BAD-STD",
                "controls": [
                    {
                        "id": "C1",
                        "mappings": [
                            {"mapping_type": "cwe"},  # Missing target_id
                            {"target_id": "CWE-79"},  # Missing mapping_type
                            {}                        # Empty mapping
                        ]
                    }
                ]
            })
        }

        # Should handle malformed data without crashing
        new_result = analyze_mappings(result, malformed_dict)
        assert isinstance(new_result, StandardsMappingResult)

    def test_large_dataset_performance(self):
        """Test performance with large datasets."""
        result = StandardsLoadingResult()

        # Add many standards efficiently
        for i in range(50):
            standard_id = f"STD-{i:04d}"
            standards_data: StandardsDataDict = cast(StandardsDataDict, {
                "id": standard_id,
                "name": f"Test Standard {i}",
                "framework": f"FRAMEWORK-{i % 5}"  # 5 different frameworks
            })
            result = add_standard(result, standard_id, standards_data)

        assert result.standards_count == 50
        assert result.loaded == 50
        assert result.framework_count == 5

        # Test summary generation performance
        summary = get_standards_loading_summary(result)
        assert summary["standards_loaded"] == 50

    def test_unicode_handling(self):
        """Test handling of unicode in standards data."""
        result = StandardsLoadingResult()
        unicode_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "GB-T-22080-2016",
            "name": "信息安全管理体系要求",  # Chinese
            "framework": "国标"  # Chinese
        })

        new_result = add_standard(result, "GB-T-22080-2016", unicode_data)

        assert new_result.standards_count == 1
        retrieved = new_result.get_standard("GB-T-22080-2016")
        assert retrieved is not None
        assert retrieved.get("name") == "信息安全管理体系要求"
        assert retrieved.get("framework") == "国标"

    def test_complex_control_structures(self):
        """Test handling of complex control structures."""
        result = StandardsValidationResult()
        complex_data: StandardsDataDict = cast(StandardsDataDict, {
            "id": "COMPLEX-STD",
            "name": "Complex Standard",
            "framework": "TEST",
            "controls": [
                {
                    "id": "COMPLEX-1(a)(1)",
                    "title": "Complex Control with Sub-parts",
                    "description": "A control with complex identifier",
                    "mappings": [
                        {"target_id": "CWE-79", "mapping_type": "primary"},
                        {"target_id": "CWE-89", "mapping_type": "secondary"},
                        {"target_id": "CAPEC-66", "mapping_type": "attack_pattern"}
                    ]
                }
            ]
        })

        new_result = validate_standard(result, "COMPLEX-STD", complex_data)

        assert new_result.validation_results["COMPLEX-STD"] is True
        assert new_result.control_validation_count == 1

    def test_framework_case_sensitivity(self):
        """Test framework handling with different cases."""
        result = StandardsLoadingResult()

        # Add standards with different framework cases
        data1: StandardsDataDict = cast(StandardsDataDict, {"id": "STD1", "framework": "NIST"})
        data2: StandardsDataDict = cast(StandardsDataDict, {"id": "STD2", "framework": "nist"})
        data3: StandardsDataDict = cast(StandardsDataDict, {"id": "STD3", "framework": "Nist"})

        result = add_standard(result, "STD1", data1)
        result = add_standard(result, "STD2", data2)
        result = add_standard(result, "STD3", data3)

        # Should treat as separate frameworks (case-sensitive)
        assert result.framework_count == 3
        assert "NIST" in result.frameworks
        assert "nist" in result.frameworks
        assert "Nist" in result.frameworks
