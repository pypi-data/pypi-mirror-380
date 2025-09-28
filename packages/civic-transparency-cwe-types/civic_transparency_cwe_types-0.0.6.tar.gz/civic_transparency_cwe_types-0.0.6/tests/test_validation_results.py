"""Tests for Phase validation result types and operations.

Tests for phase validation result types including single-phase and
multi-phase tracking, operations, and analysis functions.
"""

from ci.transparency.cwe.types.validation.phase.results import (
    # Result types
    PhaseValidationResult,
    MultiPhaseValidationResult,

    # Single phase operations
    set_phase_info,
    add_processed_item,
    update_phase_details,
    set_phase_detail,

    # Multi-phase operations
    add_phase,
    update_phase,
    set_current_phase,
    merge_phases,

    # Convenience operations
    add_item_to_phase,
    annotate_phase,
    phase_add_error,
    phase_add_warning,
    phase_add_info,

    # Analysis functions
    get_phase_summary,
    get_multiphase_summary,
    get_phase_by_name,
    get_phases_by_type,
    get_failed_phases,
    get_phase_completion_rate,
)


class TestPhaseValidationResult:
    """Test single-phase validation result type and operations."""

    def test_empty_phase_validation_result(self):
        """Test empty phase validation result initialization."""
        result = PhaseValidationResult()

        # Test basic properties
        assert result.phase_name == ""
        assert result.validation_type == ""
        assert result.items_count == 0
        assert not result.has_phase_details

        # Test tuples are empty
        assert len(result.items_processed) == 0
        assert len(result.phase_details) == 0

    def test_phase_validation_result_with_data(self):
        """Test phase validation result with sample data."""
        items_processed = ("item1", "item2", "item3")
        phase_details = {"processing_time": 45.2, "memory_used": "1.2GB"}

        result = PhaseValidationResult(
            phase_name="field-validation",
            validation_type="cwe",
            items_processed=items_processed,
            phase_details=phase_details,
            passed=25,
            failed=3,
            errors=("Error 1", "Error 2"),
            warnings=("Warning 1",)
        )

        # Test basic properties
        assert result.phase_name == "field-validation"
        assert result.validation_type == "cwe"
        assert result.items_count == 3
        assert result.has_phase_details

        # Test inherited properties
        assert result.passed == 25
        assert result.failed == 3
        assert result.error_count == 2
        assert result.warning_count == 1

        # Test detail access
        assert result.get_detail("processing_time") == 45.2
        assert result.get_detail("memory_used") == "1.2GB"
        assert result.get_detail("nonexistent") is None
        assert result.get_detail("nonexistent", "default") == "default"

    def test_set_phase_info(self):
        """Test setting phase identification information."""
        result = PhaseValidationResult()

        new_result = set_phase_info(result, "cwe-validation", "field-check")

        assert new_result.phase_name == "cwe-validation"
        assert new_result.validation_type == "field-check"

        # Verify original is unchanged (immutability)
        assert result.phase_name == ""
        assert result.validation_type == ""

    def test_add_processed_item(self):
        """Test adding processed items to phase."""
        result = PhaseValidationResult(phase_name="test-phase")

        # Add first item
        result1 = add_processed_item(result, "item1")
        assert result1.items_count == 1
        assert "item1" in result1.items_processed

        # Add second item
        result2 = add_processed_item(result1, "item2")
        assert result2.items_count == 2
        assert "item1" in result2.items_processed
        assert "item2" in result2.items_processed

        # Verify immutability
        assert result.items_count == 0
        assert result1.items_count == 1

    def test_update_phase_details(self):
        """Test updating phase details with shallow merge."""
        initial_details = {"key1": "value1", "key2": "value2"}
        result = PhaseValidationResult(phase_details=initial_details)

        # Update with new details (should merge)
        new_details = {"key2": "updated", "key3": "new"}
        updated_result = update_phase_details(result, new_details)

        assert updated_result.get_detail("key1") == "value1"  # Preserved
        assert updated_result.get_detail("key2") == "updated"  # Updated
        assert updated_result.get_detail("key3") == "new"     # Added

        # Verify original unchanged
        assert result.get_detail("key2") == "value2"
        assert result.get_detail("key3") is None

    def test_set_phase_detail(self):
        """Test setting individual phase detail."""
        result = PhaseValidationResult(phase_details={"existing": "value"})

        new_result = set_phase_detail(result, "new_key", "new_value")

        assert new_result.get_detail("existing") == "value"
        assert new_result.get_detail("new_key") == "new_value"

        # Verify original unchanged
        assert result.get_detail("new_key") is None

    def test_phase_details_with_complex_data(self):
        """Test phase details with complex data structures."""
        complex_details = {
            "metrics": {"processed": 100, "failed": 5},
            "timing": {"start": "2024-01-01T10:00:00Z", "end": "2024-01-01T10:05:30Z"},
            "resources": ["memory", "cpu", "disk"],
            "config": {"batch_size": 50, "timeout": 300}
        }

        result = PhaseValidationResult(phase_details=complex_details)

        assert result.get_detail("metrics")["processed"] == 100
        assert result.get_detail("timing")["start"] == "2024-01-01T10:00:00Z"
        assert "memory" in result.get_detail("resources")
        assert result.get_detail("config")["batch_size"] == 50


class TestMultiPhaseValidationResult:
    """Test multi-phase validation result type and operations."""

    def test_empty_multiphase_validation_result(self):
        """Test empty multi-phase validation result initialization."""
        result = MultiPhaseValidationResult()

        # Test basic properties
        assert result.phase_count == 0
        assert result.items_processed_total == 0
        assert not result.has_current_phase
        assert result.current_phase is None

        # Test collections are empty
        assert len(result.phases) == 0
        assert len(result.phase_order) == 0
        assert len(result.ordered_phases) == 0

    def test_multiphase_validation_result_with_data(self):
        """Test multi-phase validation result with sample data."""
        phase1 = PhaseValidationResult(
            phase_name="phase1",
            items_processed=("item1", "item2"),
            passed=5,
            failed=1
        )
        phase2 = PhaseValidationResult(
            phase_name="phase2",
            items_processed=("item3",),
            passed=3,
            failed=0
        )
        phases = {"phase1": phase1, "phase2": phase2}
        phase_order = ("phase1", "phase2")

        result = MultiPhaseValidationResult(
            phases=phases,
            phase_order=phase_order,
            current_phase="phase2",
            # These should be aggregated from phases
            passed=8,  # 5 + 3
            failed=1   # 1 + 0
        )

        # Test basic properties
        assert result.phase_count == 2
        assert result.items_processed_total == 3  # 2 + 1
        assert result.has_current_phase
        assert result.current_phase == "phase2"

        # Test phase access
        assert result.has_phase("phase1")
        assert result.has_phase("phase2")
        assert not result.has_phase("nonexistent")

        retrieved_phase1 = result.get_phase("phase1")
        assert retrieved_phase1 is not None
        assert retrieved_phase1.phase_name == "phase1"

        # Test ordered phases
        ordered = result.ordered_phases
        assert len(ordered) == 2
        assert ordered[0].phase_name == "phase1"
        assert ordered[1].phase_name == "phase2"

    def test_add_phase(self):
        """Test adding phases to multi-phase result."""
        result = MultiPhaseValidationResult()

        # Create a phase to add
        phase1 = PhaseValidationResult(
            phase_name="test-phase",
            items_processed=("item1", "item2"),
            passed=5,
            failed=1,
            errors=("Error in phase1",)
        )

        new_result = add_phase(result, phase1)

        # Verify phase was added
        assert new_result.phase_count == 1
        assert new_result.has_phase("test-phase")
        assert new_result.items_processed_total == 2

        # Verify aggregation occurred
        assert new_result.passed == 5
        assert new_result.failed == 1
        assert new_result.error_count == 1
        assert "Error in phase1" in new_result.errors

        # Verify phase ordering
        assert "test-phase" in new_result.phase_order

        # Verify original unchanged
        assert result.phase_count == 0

    def test_add_phase_with_set_current(self):
        """Test adding phase and setting as current."""
        result = MultiPhaseValidationResult()
        phase = PhaseValidationResult(phase_name="current-phase")

        new_result = add_phase(result, phase, set_current=True)

        assert new_result.has_current_phase
        assert new_result.current_phase == "current-phase"

    def test_update_phase(self):
        """Test updating an existing phase."""
        phase1 = PhaseValidationResult(phase_name="phase1", passed=5)
        result = MultiPhaseValidationResult(phases={"phase1": phase1})

        def add_error_to_phase(phase: PhaseValidationResult) -> PhaseValidationResult:
            from ci.transparency.cwe.types.base import add_error
            return add_error(phase, "New error message")

        new_result = update_phase(result, "phase1", add_error_to_phase)

        # Verify phase was updated
        updated_phase = new_result.get_phase("phase1")
        assert updated_phase is not None
        assert updated_phase.error_count == 1
        assert "New error message" in updated_phase.errors

        # Verify aggregation occurred
        assert new_result.error_count == 1
        assert "New error message" in new_result.errors

    def test_update_nonexistent_phase(self):
        """Test updating a non-existent phase."""
        result = MultiPhaseValidationResult()

        def dummy_updater(phase: PhaseValidationResult) -> PhaseValidationResult:
            return phase

        new_result = update_phase(result, "nonexistent", dummy_updater)

        # Should add an error about missing phase
        assert new_result.has_errors
        assert any("not found" in error for error in new_result.errors)

    def test_set_current_phase(self):
        """Test setting the current phase."""
        phase1 = PhaseValidationResult(phase_name="phase1")
        result = MultiPhaseValidationResult(phases={"phase1": phase1})

        # Set existing phase as current
        result_with_current = set_current_phase(result, "phase1")
        assert result_with_current.current_phase == "phase1"

        # Clear current phase
        result_no_current = set_current_phase(result_with_current, None)
        assert result_no_current.current_phase is None

    def test_set_current_phase_nonexistent(self):
        """Test setting non-existent phase as current."""
        result = MultiPhaseValidationResult()

        new_result = set_current_phase(result, "nonexistent")

        # Should add warning and not change current
        assert new_result.has_warnings
        assert result.current_phase is None

    def test_merge_phases(self):
        """Test merging multiple multi-phase results."""
        # Create first result
        phase1 = PhaseValidationResult(phase_name="phase1", passed=5)
        result1 = MultiPhaseValidationResult(
            phases={"phase1": phase1},
            phase_order=("phase1",)
        )

        # Create second result
        phase2 = PhaseValidationResult(phase_name="phase2", passed=3)
        result2 = MultiPhaseValidationResult(
            phases={"phase2": phase2},
            phase_order=("phase2",)
        )

        # Create third result with overlapping phase name
        phase1_alt = PhaseValidationResult(phase_name="phase1", passed=7, failed=1)
        result3 = MultiPhaseValidationResult(
            phases={"phase1": phase1_alt},
            phase_order=("phase1",)
        )

        merged = merge_phases(result1, result2, result3)

        # Should have all unique phases (phase1 from result3 overwrites result1)
        assert merged.phase_count == 2
        assert merged.has_phase("phase1")
        assert merged.has_phase("phase2")

        # phase1 should be from result3 (last one wins)
        merged_phase1 = merged.get_phase("phase1")
        assert merged_phase1 is not None
        assert merged_phase1.passed == 7
        assert merged_phase1.failed == 1

        # Verify aggregation
        assert merged.passed == 10  # 7 + 3
        assert merged.failed == 1   # 1 + 0


class TestMultiPhaseConvenienceOperations:
    """Test multi-phase convenience operations."""

    def test_add_item_to_phase(self):
        """Test adding item to a named phase."""
        result = MultiPhaseValidationResult()

        # Add item to non-existent phase (should create phase)
        result1 = add_item_to_phase(result, "new-phase", "item1")

        assert result1.phase_count == 1
        assert result1.has_phase("new-phase")
        created_phase = result1.get_phase("new-phase")
        assert created_phase is not None
        assert "item1" in created_phase.items_processed

        # Add item to existing phase
        result2 = add_item_to_phase(result1, "new-phase", "item2")

        assert result2.phase_count == 1  # Still same number of phases
        existing_phase = result2.get_phase("new-phase")
        assert existing_phase is not None
        assert len(existing_phase.items_processed) == 2
        assert "item1" in existing_phase.items_processed
        assert "item2" in existing_phase.items_processed

    def test_annotate_phase(self):
        """Test adding annotations to a named phase."""
        result = MultiPhaseValidationResult()

        # Annotate non-existent phase (should create phase)
        result1 = annotate_phase(
            result, "analysis-phase",
            processing_time=45.2,
            memory_used="1.5GB"
        )

        assert result1.phase_count == 1
        created_phase = result1.get_phase("analysis-phase")
        assert created_phase is not None
        assert created_phase.get_detail("processing_time") == 45.2
        assert created_phase.get_detail("memory_used") == "1.5GB"

        # Annotate existing phase (should update)
        result2 = annotate_phase(
            result1, "analysis-phase",
            cpu_usage="85%",
            processing_time=50.1  # Should update existing value
        )

        updated_phase = result2.get_phase("analysis-phase")
        assert updated_phase is not None
        assert updated_phase.get_detail("processing_time") == 50.1
        assert updated_phase.get_detail("cpu_usage") == "85%"
        assert updated_phase.get_detail("memory_used") == "1.5GB"  # Should be preserved

    def test_phase_add_error(self):
        """Test adding error to a named phase."""
        result = MultiPhaseValidationResult()

        # Add error to non-existent phase
        result1 = phase_add_error(result, "error-phase", "Critical validation error")

        assert result1.phase_count == 1
        created_phase = result1.get_phase("error-phase")
        assert created_phase is not None
        assert created_phase.has_errors
        assert "Critical validation error" in created_phase.errors

        # Verify aggregation
        assert result1.has_errors
        assert "Critical validation error" in result1.errors

    def test_phase_add_warning(self):
        """Test adding warning to a named phase."""
        result = MultiPhaseValidationResult()

        result1 = phase_add_warning(result, "warning-phase", "Minor validation issue")

        created_phase = result1.get_phase("warning-phase")
        assert created_phase is not None
        assert created_phase.has_warnings
        assert "Minor validation issue" in created_phase.warnings

        # Verify aggregation
        assert result1.has_warnings
        assert "Minor validation issue" in result1.warnings

    def test_phase_add_info(self):
        """Test adding info to a named phase."""
        result = MultiPhaseValidationResult()

        result1 = phase_add_info(result, "info-phase", "Processing completed successfully")

        created_phase = result1.get_phase("info-phase")
        assert created_phase is not None
        assert created_phase.has_infos
        assert "Processing completed successfully" in created_phase.infos

        # Verify aggregation
        assert result1.has_infos
        assert "Processing completed successfully" in result1.infos


class TestAnalysisFunctions:
    """Test phase analysis and summary functions."""

    def test_get_phase_summary(self):
        """Test single-phase summary generation."""
        phase_details = {"processing_time": 30.5, "items_skipped": 2}
        result = PhaseValidationResult(
            phase_name="cwe-validation",
            validation_type="field-check",
            items_processed=("cwe-1", "cwe-2", "cwe-3"),
            phase_details=phase_details,
            passed=15,
            failed=3,
            errors=("Error 1",),
            warnings=("Warning 1", "Warning 2"),
            infos=("Info 1",)
        )

        summary = get_phase_summary(result)

        assert summary["phase_name"] == "cwe-validation"
        assert summary["validation_type"] == "field-check"
        assert summary["items_processed"] == 3
        assert summary["validation_passed"] == 15
        assert summary["validation_failed"] == 3
        assert abs(summary["success_rate_percent"] - 83.33) < 0.1
        assert summary["has_errors"] is True
        assert summary["has_warnings"] is True
        assert summary["has_infos"] is True
        assert summary["error_count"] == 1
        assert summary["warning_count"] == 2
        assert summary["info_count"] == 1
        assert summary["phase_details"] == phase_details

    def test_get_multiphase_summary(self):
        """Test multi-phase summary generation."""
        phase1 = PhaseValidationResult(
            phase_name="loading",
            items_processed=("item1", "item2"),
            passed=10,
            failed=1,
            errors=("Load error",)
        )
        phase2 = PhaseValidationResult(
            phase_name="validation",
            items_processed=("item3", "item4", "item5"),
            passed=8,
            failed=2,
            warnings=("Validation warning",)
        )

        result = MultiPhaseValidationResult(
            phases={"loading": phase1, "validation": phase2},
            phase_order=("loading", "validation"),
            current_phase="validation",
            # Manually set aggregated values for test
            passed=18,  # 10 + 8
            failed=3,   # 1 + 2
            errors=("Load error",),
            warnings=("Validation warning",)
        )

        summary = get_multiphase_summary(result)

        # Phase organization
        assert summary["phase_count"] == 2
        assert summary["phase_order"] == ["loading", "validation"]
        assert summary["current_phase"] == "validation"

        # Aggregated totals
        assert summary["items_processed_total"] == 5  # 2 + 3
        assert summary["validation_passed_total"] == 18  # 10 + 8
        assert summary["validation_failed_total"] == 3   # 1 + 2

        # Message totals
        assert summary["errors_total"] == 1
        assert summary["warnings_total"] == 1
        assert summary["infos_total"] == 0

        # Overall metrics
        assert abs(summary["success_rate_percent"] - 85.71) < 0.1  # 18/(18+3)
        assert summary["has_errors"] is True
        assert summary["has_warnings"] is True
        assert summary["has_infos"] is False

        # Per-phase details
        assert "phases" in summary
        assert "loading" in summary["phases"]
        assert "validation" in summary["phases"]

    def test_get_phase_by_name(self):
        """Test getting phase by name."""
        phase1 = PhaseValidationResult(phase_name="phase1")
        result = MultiPhaseValidationResult(phases={"phase1": phase1})

        # Test existing phase
        found_phase = get_phase_by_name(result, "phase1")
        assert found_phase is not None
        assert found_phase.phase_name == "phase1"

        # Test non-existent phase
        missing_phase = get_phase_by_name(result, "nonexistent")
        assert missing_phase is None

    def test_get_phases_by_type(self):
        """Test filtering phases by validation type."""
        phase1 = PhaseValidationResult(phase_name="phase1", validation_type="cwe")
        phase2 = PhaseValidationResult(phase_name="phase2", validation_type="standards")
        phase3 = PhaseValidationResult(phase_name="phase3", validation_type="cwe")

        result = MultiPhaseValidationResult(phases={
            "phase1": phase1,
            "phase2": phase2,
            "phase3": phase3
        })

        cwe_phases = get_phases_by_type(result, "cwe")
        assert len(cwe_phases) == 2
        phase_names = [p.phase_name for p in cwe_phases]
        assert "phase1" in phase_names
        assert "phase3" in phase_names

        standards_phases = get_phases_by_type(result, "standards")
        assert len(standards_phases) == 1
        assert standards_phases[0].phase_name == "phase2"

        # Test non-existent type
        empty_phases = get_phases_by_type(result, "nonexistent")
        assert len(empty_phases) == 0

    def test_get_failed_phases(self):
        """Test getting phases that have failures."""
        phase1 = PhaseValidationResult(phase_name="success", passed=5, failed=0)
        phase2 = PhaseValidationResult(phase_name="partial", passed=3, failed=2)
        phase3 = PhaseValidationResult(phase_name="failure", passed=0, failed=5)

        result = MultiPhaseValidationResult(phases={
            "success": phase1,
            "partial": phase2,
            "failure": phase3
        })

        failed_phases = get_failed_phases(result)
        assert len(failed_phases) == 2
        phase_names = [p.phase_name for p in failed_phases]
        assert "partial" in phase_names
        assert "failure" in phase_names
        assert "success" not in phase_names

    def test_get_phase_completion_rate(self):
        """Test calculating phase completion rate."""
        # Create phases with different error states
        phase1 = PhaseValidationResult(phase_name="success")  # No errors
        phase2 = PhaseValidationResult(
            phase_name="failed",
            errors=("Error message",)
        )  # Has errors
        phase3 = PhaseValidationResult(phase_name="another_success")  # No errors

        result = MultiPhaseValidationResult(phases={
            "success": phase1,
            "failed": phase2,
            "another_success": phase3
        })

        completion_rate = get_phase_completion_rate(result)
        # 2 out of 3 phases completed successfully
        assert abs(completion_rate - 0.667) < 0.01

        # Test with no phases
        empty_result = MultiPhaseValidationResult()
        empty_rate = get_phase_completion_rate(empty_result)
        assert empty_rate == 1.0


class TestResultImmutability:
    """Test that result operations maintain immutability."""

    def test_phase_validation_result_immutability(self):
        """Test phase validation result immutability."""
        original = PhaseValidationResult(phase_name="original")

        # Test set_phase_info immutability
        new_result = set_phase_info(original, "new-phase", "new-type")
        assert original.phase_name == "original"
        assert original.validation_type == ""
        assert new_result.phase_name == "new-phase"
        assert new_result.validation_type == "new-type"

        # Test add_processed_item immutability
        item_result = add_processed_item(original, "item1")
        assert original.items_count == 0
        assert item_result.items_count == 1

    def test_multiphase_validation_result_immutability(self):
        """Test multi-phase validation result immutability."""
        phase1 = PhaseValidationResult(phase_name="phase1")
        original = MultiPhaseValidationResult()

        # Test add_phase immutability
        new_result = add_phase(original, phase1)
        assert original.phase_count == 0
        assert new_result.phase_count == 1

        # Test set_current_phase immutability
        current_result = set_current_phase(new_result, "phase1")
        assert new_result.current_phase is None
        assert current_result.current_phase == "phase1"

    def test_nested_immutability(self):
        """Test that nested operations maintain immutability."""
        original = MultiPhaseValidationResult()

        # Chain multiple operations using assignment
        result = add_item_to_phase(original, "phase1", "item1")
        result = annotate_phase(result, "phase1", detail1="value1")
        result = phase_add_error(result, "phase1", "test error")

        # Original should be unchanged
        assert original.phase_count == 0

        # Final result should have all changes
        assert result.phase_count == 1
        final_phase = result.get_phase("phase1")
        assert final_phase is not None
        assert final_phase.items_count == 1
        assert final_phase.get_detail("detail1") == "value1"
        assert final_phase.has_errors


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_phase_name_handling(self):
        """Test handling of empty or None phase names."""
        result = MultiPhaseValidationResult()

        # Phase with empty name
        empty_phase = PhaseValidationResult(phase_name="")
        result_with_empty = add_phase(result, empty_phase)

        # Should generate a default name
        assert result_with_empty.phase_count == 1
        phase_names = list(result_with_empty.phases.keys())
        assert len(phase_names) == 1
        # Should have generated a default name like "phase-1"
        assert phase_names[0].startswith("phase-")

    def test_duplicate_phase_names(self):
        """Test handling of duplicate phase names."""
        result = MultiPhaseValidationResult()

        # Add first phase
        phase1 = PhaseValidationResult(phase_name="duplicate", passed=5)
        result1 = add_phase(result, phase1)

        # Add second phase with same name (should replace)
        phase2 = PhaseValidationResult(phase_name="duplicate", passed=10)
        result2 = add_phase(result1, phase2)

        assert result2.phase_count == 1
        final_phase = result2.get_phase("duplicate")
        assert final_phase is not None
        assert final_phase.passed == 10  # Should be the newer one

    def test_large_number_of_phases(self):
        """Test performance with large number of phases."""
        result = MultiPhaseValidationResult()

        # Add many phases
        for i in range(100):
            phase = PhaseValidationResult(
                phase_name=f"phase-{i}",
                passed=i,
                failed=i % 3  # Some failures
            )
            result = add_phase(result, phase)

        assert result.phase_count == 100

        # Test aggregation works correctly
        expected_passed = sum(range(100))  # 0 + 1 + 2 + ... + 99
        expected_failed = sum(i % 3 for i in range(100))

        assert result.passed == expected_passed
        assert result.failed == expected_failed

    def test_complex_phase_details(self):
        """Test phase details with complex nested data."""
        complex_details = {
            "nested": {
                "deeply": {
                    "nested": {
                        "value": "found"
                    }
                }
            },
            "list": [1, 2, {"inner": "value"}],
            "mixed": {
                "numbers": [1, 2, 3],
                "strings": ["a", "b", "c"],
                "booleans": [True, False]
            }
        }

        result = PhaseValidationResult(phase_details=complex_details)

        # Should handle complex access patterns
        nested_val = result.get_detail("nested")["deeply"]["nested"]["value"]
        assert nested_val == "found"

        list_val = result.get_detail("list")[2]["inner"]
        assert list_val == "value"

    def test_unicode_in_phase_data(self):
        """Test handling of unicode in phase data."""
        unicode_details = {
            "中文": "中文值",
            "العربية": "القيمة العربية",
            "русский": "русское значение"
        }

        result = PhaseValidationResult(
            phase_name="unicode-phase-名前",
            phase_details=unicode_details
        )

        assert result.phase_name == "unicode-phase-名前"
        assert result.get_detail("中文") == "中文值"
        assert result.get_detail("العربية") == "القيمة العربية"
        assert result.get_detail("русский") == "русское значение"


class TestRealWorldScenarios:
    """Test phase validation in realistic usage scenarios."""

    def test_cwe_validation_pipeline(self):
        """Test realistic CWE validation pipeline scenario."""
        result = MultiPhaseValidationResult()

        # Phase 1: Data Loading
        result = add_item_to_phase(result, "data-loading", "cwe-definitions.yaml")
        result = annotate_phase(result, "data-loading",
                               files_loaded=1,
                               records_loaded=1421,
                               processing_time_ms=250)

        # Phase 2: Field Validation
        for cwe_id in ["CWE-79", "CWE-89", "CWE-22"]:
            result = add_item_to_phase(result, "field-validation", cwe_id)

        result = annotate_phase(result, "field-validation",
                               validation_rules=["required_fields", "format_check"],
                               processing_time_ms=1500)

        # Phase 3: Relationship Validation (with some failures)
        result = add_item_to_phase(result, "relationship-validation", "parent-child-check")
        result = phase_add_error(result, "relationship-validation",
                                "CWE-999 references non-existent parent CWE-9999")
        result = annotate_phase(result, "relationship-validation",
                               relationships_checked=157,
                               circular_dependencies_found=0,
                               orphaned_cwes_found=5)

        # Verify pipeline structure
        assert result.phase_count == 3
        assert result.items_processed_total == 5  # 1 + 3 + 1

        # Check phase order preservation (implicit from order of operations)
        phase_names = list(result.phases.keys())
        assert "data-loading" in phase_names
        assert "field-validation" in phase_names
        assert "relationship-validation" in phase_names

        # Verify error propagation
        assert result.has_errors
        rel_phase = result.get_phase("relationship-validation")
        assert rel_phase is not None
        assert rel_phase.has_errors

    def test_standards_mapping_validation(self):
        """Test realistic standards mapping validation scenario."""
        result = MultiPhaseValidationResult()

        # Phase 1: Standards Loading
        standards = ["NIST-SP-800-53", "ISO-27001", "COBIT-2019"]
        for std in standards:
            result = add_item_to_phase(result, "standards-loading", std)

        result = annotate_phase(result, "standards-loading",
                               frameworks_detected=3,
                               total_controls=864,
                               loading_time_ms=750)

        # Phase 2: Mapping Validation
        result = phase_add_warning(result, "mapping-validation",
                                  "5 controls have no CWE mappings")
        result = phase_add_error(result, "mapping-validation",
                                "AC-1 maps to non-existent CWE-99999")

        result = annotate_phase(result, "mapping-validation",
                               total_mappings=2400,
                               invalid_mappings=1,
                               orphaned_controls=5,
                               validation_time_ms=3200)

        # Phase 3: Cross-Framework Analysis
        result = add_item_to_phase(result, "cross-framework", "mapping-conflicts")
        result = phase_add_info(result, "cross-framework",
                               "Found 15 overlapping control mappings between frameworks")

        # Set current phase
        result = set_current_phase(result, "cross-framework")

        # Verify scenario
        assert result.current_phase == "cross-framework"
        assert result.has_errors
        assert result.has_warnings
        assert result.has_infos

        # Check specific phases
        mapping_phase = result.get_phase("mapping-validation")
        assert mapping_phase is not None
        assert mapping_phase.get_detail("invalid_mappings") == 1

        standards_phase = result.get_phase("standards-loading")
        assert standards_phase is not None
        assert standards_phase.items_count == 3

    def test_multi_batch_processing(self):
        """Test multi-batch processing scenario."""
        result = MultiPhaseValidationResult()

        # Process multiple batches
        batch_sizes = [100, 150, 75, 200]
        total_processed = 0

        for i, batch_size in enumerate(batch_sizes, 1):
            phase_name = f"batch-{i}"

            # Add items for this batch
            for j in range(batch_size):
                result = add_item_to_phase(result, phase_name, f"item-{total_processed + j}")

            total_processed += batch_size

            # Add batch-specific details
            result = annotate_phase(result, phase_name,
                                   batch_number=i,
                                   batch_size=batch_size,
                                   processing_time_ms=batch_size * 10,  # Simulated time
                                   memory_used_mb=batch_size * 2)  # Simulated memory

            # Simulate some failures in larger batches
            if batch_size > 100:
                failures = batch_size // 50  # Some failures
                for f in range(failures):
                    result = phase_add_error(result, phase_name, f"Validation error {f+1}")

        # Verify multi-batch processing
        assert result.phase_count == 4
        assert result.items_processed_total == sum(batch_sizes)

        # Check that larger batches have more errors
        batch_4 = result.get_phase("batch-4")  # Largest batch
        assert batch_4 is not None
        assert batch_4.error_count > 0

        batch_3 = result.get_phase("batch-3")  # Smallest batch
        assert batch_3 is not None

        # Verify aggregated totals
        summary = get_multiphase_summary(result)
        assert summary["items_processed_total"] == sum(batch_sizes)
        assert summary["phase_count"] == 4

    def test_pipeline_with_abort(self):
        """Test pipeline that gets aborted mid-processing."""
        result = MultiPhaseValidationResult()

        # Start with successful phases
        result = add_item_to_phase(result, "initialization", "config-loaded")
        result = annotate_phase(result, "initialization", success=True)

        result = add_item_to_phase(result, "data-loading", "data-file")
        result = annotate_phase(result, "data-loading",
                               records_loaded=5000,
                               success=True)

        # Critical failure in processing phase
        result = phase_add_error(result, "processing",
                                "Critical system error: out of memory")
        result = phase_add_error(result, "processing",
                                "Processing aborted after 2500 items")
        result = annotate_phase(result, "processing",
                               items_attempted=2500,
                               items_completed=2347,
                               success=False,
                               abort_reason="memory_exhaustion")

        # Cleanup phase (still runs after abort)
        result = add_item_to_phase(result, "cleanup", "temp-files")
        result = phase_add_info(result, "cleanup", "Cleaned up temporary resources")
        result = annotate_phase(result, "cleanup",
                               success=True,
                               cleanup_completed=True)

        # Verify abort scenario
        assert result.phase_count == 4
        assert result.has_errors

        processing_phase = result.get_phase("processing")
        assert processing_phase is not None
        assert not processing_phase.get_detail("success", True)
        assert processing_phase.get_detail("abort_reason") == "memory_exhaustion"

        # Verify cleanup still completed
        cleanup_phase = result.get_phase("cleanup")
        assert cleanup_phase is not None
        assert cleanup_phase.get_detail("cleanup_completed") is True

        # Calculate completion rate
        completion_rate = get_phase_completion_rate(result)
        # 3 out of 4 phases succeeded (processing failed)
        assert abs(completion_rate - 0.75) < 0.01
