"""Tests for result type conversions and integration points.

Tests the conversion protocols between BatchResult and domain-specific
result types, ensuring seamless transitions and data preservation.
"""

import pytest
from pathlib import Path

from ci.transparency.cwe.types.batch import BatchResult
from ci.transparency.cwe.types.cwe import CweLoadingResult
from ci.transparency.cwe.types.standards import StandardsLoadingResult, StandardsValidationResult
from ci.transparency.cwe.types.validation.phase import PhaseValidationResult, MultiPhaseValidationResult
from ci.transparency.cwe.types.base import BaseLoadingResult, BaseValidationResult


class TestBatchToDomainConversions:
    """Test conversions from BatchResult to domain-specific results."""

    @pytest.fixture
    def sample_batch_result(self) -> BatchResult:
        """Create a sample BatchResult with varied data."""
        cwe_data = {
            "CWE-79": {"id": "CWE-79", "name": "XSS", "category": "injection"},
            "CWE-89": {"id": "CWE-89", "name": "SQL Injection", "category": "injection"}
        }

        return BatchResult(
            items=cwe_data,
            file_types={"yaml": 2},
            processed_files=(Path("cwe-79.yaml"), Path("cwe-89.yaml")),
            skipped_files=(Path("invalid.txt"),),
            loaded=2,
            failed=1,
            errors=("Parse error in file",),
            warnings=("Minor formatting issue",),
            infos=("Processing started",)
        )

    def test_batch_to_cwe_loading_result(self, sample_batch_result: BatchResult):
        """Test converting BatchResult to CweLoadingResult."""
        cwe_result = CweLoadingResult.from_batch(sample_batch_result)

        # Check that all base fields are preserved
        assert cwe_result.loaded == sample_batch_result.loaded
        assert cwe_result.failed == sample_batch_result.failed
        assert cwe_result.errors == sample_batch_result.errors
        assert cwe_result.warnings == sample_batch_result.warnings
        assert cwe_result.infos == sample_batch_result.infos

        # Check CWE-specific mappings
        assert len(cwe_result.cwes) == 2
        assert "CWE-79" in cwe_result.cwes
        assert "CWE-89" in cwe_result.cwes
        # Use .get() to safely access potentially missing keys
        assert cwe_result.cwes["CWE-79"].get("name") == "XSS"

        # Check file tracking
        assert cwe_result.skipped_files == sample_batch_result.skipped_files

        # Check derived properties work
        assert cwe_result.cwe_count == 2
        assert cwe_result.success_rate == sample_batch_result.success_rate

    def test_batch_to_standards_loading_result(self, sample_batch_result: BatchResult):
        """Test converting BatchResult to StandardsLoadingResult."""
        # Adapt sample data for standards
        standards_data = {
            "NIST-SP-800-53": {"id": "NIST-SP-800-53", "framework": "NIST", "version": "5.1"},
            "ISO-27001": {"id": "ISO-27001", "framework": "ISO", "version": "2022"}
        }
        standards_batch = BatchResult(
            items=standards_data,
            loaded=2,
            failed=0,
            file_types={"yaml": 2}
        )

        standards_result = StandardsLoadingResult.from_batch(standards_batch)

        # Check base field preservation
        assert standards_result.loaded == 2
        assert standards_result.failed == 0

        # Check standards-specific fields
        assert len(standards_result.standards) == 2
        assert "NIST-SP-800-53" in standards_result.standards
        assert "ISO-27001" in standards_result.standards

        # Check derived properties
        assert standards_result.standards_count == 2
        assert standards_result.framework_count == 0  # Frameworks populated via add_standard

    def test_empty_batch_conversions(self):
        """Test converting empty BatchResult to domain results."""
        empty_batch = BatchResult()

        cwe_result = CweLoadingResult.from_batch(empty_batch)
        standards_result = StandardsLoadingResult.from_batch(empty_batch)

        # Both should be empty but valid
        assert cwe_result.cwe_count == 0
        assert cwe_result.success_rate == 1.0
        assert not cwe_result.has_errors

        assert standards_result.standards_count == 0
        assert standards_result.success_rate == 1.0
        assert not standards_result.has_errors

    def test_batch_with_errors_conversion(self):
        """Test converting BatchResult with errors preserves error state."""
        error_batch = BatchResult(
            loaded=1,
            failed=3,
            errors=("Error 1", "Error 2", "Error 3"),
            warnings=("Warning 1",)
        )

        cwe_result = CweLoadingResult.from_batch(error_batch)

        assert cwe_result.has_errors
        assert len(cwe_result.errors) == 3
        assert cwe_result.error_count == 3
        assert cwe_result.warning_count == 1
        assert cwe_result.success_rate == 0.25  # 1/(1+3)


class TestFromResultConversions:
    """Test the from_result conversion protocol."""

    def test_base_loading_to_cwe_conversion(self):
        """Test converting BaseLoadingResult to CweLoadingResult."""
        base_result = BaseLoadingResult(
            loaded=5,
            failed=2,
            errors=("Base error",),
            warnings=("Base warning",)
        )

        cwe_result = CweLoadingResult.from_result(
            base_result,
            cwes={"CWE-1": {"id": "CWE-1"}},
            duplicate_ids={"CWE-2": Path("dup.yaml")}
        )

        # Base fields should be copied
        assert cwe_result.loaded == 5
        assert cwe_result.failed == 2
        assert cwe_result.errors == ("Base error",)
        assert cwe_result.warnings == ("Base warning",)

        # CWE-specific fields should be set
        assert len(cwe_result.cwes) == 1
        assert len(cwe_result.duplicate_ids) == 1
        assert cwe_result.duplicate_count == 1

    def test_base_validation_to_standards_conversion(self):
        """Test converting BaseValidationResult to StandardsValidationResult."""
        base_result = BaseValidationResult(
            passed=8,
            failed=2,
            errors=("Validation error",)
        )

        standards_result = StandardsValidationResult.from_result(
            base_result,
            validation_results={"STD-1": True, "STD-2": False},
            field_errors=("field.error",)
        )

        # Base validation fields should be copied
        assert standards_result.passed == 8
        assert standards_result.failed == 2
        assert standards_result.errors == ("Validation error",)

        # Standards-specific fields should be set
        assert len(standards_result.validation_results) == 2
        assert len(standards_result.field_errors) == 1
        assert standards_result.field_error_count == 1

    def test_conversion_with_extra_fields(self):
        """Test from_result with additional keyword arguments."""
        base_result = BaseLoadingResult(loaded=3, failed=1)

        cwe_result = CweLoadingResult.from_result(
            base_result,
            cwes={"CWE-A": {"id": "CWE-A"}},
            invalid_files=(Path("bad.yaml"),),
        )

        assert cwe_result.loaded == 3
        assert cwe_result.failed == 1
        assert len(cwe_result.cwes) == 1
        assert len(cwe_result.invalid_files) == 1


class TestToSubtypeConversions:
    """Test the to_subtype conversion method."""

    def test_base_loading_to_subtype(self):
        """Test converting base result to subtype."""
        base_result = BaseLoadingResult(loaded=10, failed=2)

        cwe_result = base_result.to_subtype(
            CweLoadingResult,
            cwes={"CWE-1": {"id": "CWE-1"}},
            duplicate_ids={}
        )

        assert isinstance(cwe_result, CweLoadingResult)
        assert cwe_result.loaded == 10
        assert cwe_result.failed == 2
        assert len(cwe_result.cwes) == 1

    def test_base_validation_to_subtype(self):
        """Test converting base validation result to subtype."""
        base_result = BaseValidationResult(passed=5, failed=1)

        standards_result = base_result.to_subtype(
            StandardsValidationResult,
            validation_results={"STD-1": True},
            field_errors=()
        )

        assert isinstance(standards_result, StandardsValidationResult)
        assert standards_result.passed == 5
        assert standards_result.failed == 1
        assert len(standards_result.validation_results) == 1


class TestCrossLoadingConversions:
    """Test conversions between different loading result types."""

    def test_cwe_to_standards_data_transfer(self):
        """Test transferring compatible data between loading results."""
        cwe_result = CweLoadingResult(
            loaded=5,
            failed=1,
            errors=("CWE error",),
            cwes={"CWE-1": {"id": "CWE-1", "name": "Test CWE"}}
        )

        # Convert CWE result to Standards by extracting compatible data
        standards_result = StandardsLoadingResult.from_result(
            cwe_result,  # Use CWE result as base
            standards={},  # Empty standards dict
            frameworks={}  # Empty frameworks
        )

        # Base fields should transfer
        assert standards_result.loaded == 5
        assert standards_result.failed == 1
        assert standards_result.errors == ("CWE error",)

        # Domain-specific fields should be domain-appropriate
        assert len(standards_result.standards) == 0
        assert standards_result.standards_count == 0

    def test_preserve_success_rate_across_conversions(self):
        """Test that success_rate is preserved across conversions."""
        batch_result = BatchResult(loaded=8, failed=2)  # 80% success rate

        cwe_result = CweLoadingResult.from_batch(batch_result)
        standards_result = StandardsLoadingResult.from_batch(batch_result)

        # All should have same success rate
        assert batch_result.success_rate == 0.8
        assert cwe_result.success_rate == 0.8
        assert standards_result.success_rate == 0.8


class TestValidationResultConversions:
    """Test validation result conversions."""

    def test_phase_to_base_validation_compatibility(self):
        """Test PhaseValidationResult compatibility with BaseValidationResult."""
        phase_result = PhaseValidationResult(
            passed=10,
            failed=2,
            phase_name="schema_validation",
            items_processed=("item1", "item2", "item3")
        )

        # Should be usable as BaseValidationResult
        assert isinstance(phase_result, BaseValidationResult)
        assert phase_result.success_rate == 10/12
        assert phase_result.total_processed == 12

        # Can convert to other validation results
        standards_validation = StandardsValidationResult.from_result(
            phase_result,
            validation_results={"STD-1": True},
            field_errors=()
        )

        assert standards_validation.passed == 10
        assert standards_validation.failed == 2
        assert len(standards_validation.validation_results) == 1

    def test_multiphase_aggregation_conversion(self):
        """Test MultiPhaseValidationResult aggregation properties."""
        phase1 = PhaseValidationResult(
            passed=5,
            failed=1,
            phase_name="phase1",
            errors=("Phase1 error",)
        )

        phase2 = PhaseValidationResult(
            passed=3,
            failed=2,
            phase_name="phase2",
            warnings=("Phase2 warning",)
        )

        # Create multi-phase result
        multi_result = MultiPhaseValidationResult(
            phases={"phase1": phase1, "phase2": phase2},
            phase_order=("phase1", "phase2"),
            # Should aggregate totals
            passed=8,  # 5 + 3
            failed=3,  # 1 + 2
            errors=("Phase1 error",),
            warnings=("Phase2 warning",)
        )

        assert multi_result.success_rate == 8/11
        assert multi_result.phase_count == 2
        assert multi_result.items_processed_total == 0  # No items in these phases


class TestConversionEdgeCases:
    """Test edge cases and error conditions in conversions."""

    def test_conversion_with_empty_data(self):
        """Test conversions handle empty dict values appropriately."""
        # Use empty dict instead of None to match type requirements
        batch_result = BatchResult(items={"key": {}})

        cwe_result = CweLoadingResult.from_batch(batch_result)

        assert "key" in cwe_result.cwes
        assert cwe_result.cwes["key"] == {}

    def test_conversion_preserves_immutability(self):
        """Test that conversions don't modify original results."""
        original_batch = BatchResult(loaded=5, failed=2)

        cwe_result = CweLoadingResult.from_batch(original_batch)

        # Original should be unchanged
        assert original_batch.loaded == 5
        assert original_batch.failed == 2
        assert len(original_batch.items) == 0

        # New result should be independent
        assert cwe_result.loaded == 5
        assert cwe_result.failed == 2

    def test_type_safety_in_conversions(self):
        """Test that conversions maintain type safety."""
        base_result = BaseLoadingResult(loaded=1, failed=0)

        cwe_result = CweLoadingResult.from_result(base_result, cwes={})

        # Should be correct type
        assert isinstance(cwe_result, CweLoadingResult)
        assert isinstance(cwe_result, BaseLoadingResult)  # Inheritance

        # Should have CWE-specific attributes
        assert hasattr(cwe_result, 'cwes')
        assert hasattr(cwe_result, 'duplicate_ids')
        assert hasattr(cwe_result, 'cwe_count')

    def test_from_counts_constructors(self):
        """Test from_counts constructors work with conversions."""
        # Test BaseLoadingResult.from_counts
        base_result = BaseLoadingResult.from_counts(loaded=10, failed=3)

        cwe_result = CweLoadingResult.from_result(base_result, cwes={})

        assert cwe_result.loaded == 10
        assert cwe_result.failed == 3
        assert cwe_result.success_rate == 10/13

        # Test BaseValidationResult.from_counts
        validation_base = BaseValidationResult.from_counts(passed=8, failed=1)

        standards_validation = StandardsValidationResult.from_result(
            validation_base,
            validation_results={}
        )

        assert standards_validation.passed == 8
        assert standards_validation.failed == 1

    def test_invalid_conversion_params(self):
        """Test conversion with invalid parameters."""
        # Should raise ValueError for negative counts
        with pytest.raises(ValueError, match="Counts must be non-negative"):
            BaseLoadingResult.from_counts(loaded=-1, failed=0)

        with pytest.raises(ValueError, match="Counts must be non-negative"):
            BaseValidationResult.from_counts(passed=0, failed=-1)

    def test_conversion_chain_integrity(self):
        """Test that chained conversions preserve data integrity."""
        # Start with BatchResult
        original = BatchResult(
            loaded=15,
            failed=3,
            errors=("Original error",),
            items={"item1": {"data": "test"}}
        )

        # Convert to CWE
        cwe_result = CweLoadingResult.from_batch(original)

        # Convert CWE to base, then to Standards
        base_intermediate = BaseLoadingResult(
            loaded=cwe_result.loaded,
            failed=cwe_result.failed,
            errors=cwe_result.errors,
            warnings=cwe_result.warnings,
            infos=cwe_result.infos
        )

        final_standards = StandardsLoadingResult.from_result(
            base_intermediate,
            standards={}
        )

        # Check integrity through the chain
        assert final_standards.loaded == original.loaded
        assert final_standards.failed == original.failed
        assert final_standards.errors == original.errors
        assert final_standards.success_rate == original.success_rate
