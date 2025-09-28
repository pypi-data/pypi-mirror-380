"""Tests for Phase validation error types.

Tests for phase-specific error types including context formatting,
error hierarchy, and specialized error information for phase validation processing.
"""

import pytest

from ci.transparency.cwe.types.validation.phase.errors import (
    # Base phase error
    PhaseError,

    # Operation errors
    PhaseAbortedError,
    PhaseTimeoutError,
    PhaseResourceError,
    PhaseIntegrityError,
    PhaseConfigurationError,
    PhaseValidationRuleError,
)


class TestPhaseError:
    """Test base Phase error functionality."""

    def test_phase_error_basic(self):
        """Test basic phase error creation."""
        error = PhaseError("Test error")
        assert str(error) == "Test error"
        assert error.phase_name is None
        assert error.stage is None
        assert error.items_processed is None

    def test_phase_error_with_phase_name(self):
        """Test phase error with phase name context."""
        error = PhaseError("Test error", phase_name="field-validation")
        assert "Phase: field-validation" in str(error)
        assert error.phase_name == "field-validation"

    def test_phase_error_with_stage(self):
        """Test phase error with processing stage context."""
        error = PhaseError("Test error", stage="processing")
        assert "Stage: processing" in str(error)
        assert error.stage == "processing"

    def test_phase_error_with_items_processed(self):
        """Test phase error with items processed context."""
        error = PhaseError("Test error", items_processed=150)
        assert "Processed: 150" in str(error)
        assert error.items_processed == 150

    def test_phase_error_with_validation_context(self):
        """Test phase error with validation context."""
        error = PhaseError("Test error", validation_context="cwe-validation")
        # Should inherit validation context from BaseValidationError
        error_str = str(error)
        assert "Test error" in error_str

    def test_phase_error_full_context(self):
        """Test phase error with all context information."""
        error = PhaseError(
            "Validation processing failed",
            phase_name="field-validation",
            stage="processing",
            items_processed=75,
            validation_context="cwe-data"
        )

        error_str = str(error)
        assert "Validation processing failed" in error_str
        assert "Phase: field-validation" in error_str
        assert "Stage: processing" in error_str
        assert "Processed: 75" in error_str

    def test_phase_error_context_order(self):
        """Test that phase name appears first in context."""
        error = PhaseError("Test", phase_name="test-phase", stage="setup")
        context_parts = error.get_context_parts()
        assert context_parts[0] == "Phase: test-phase"

    def test_phase_error_inheritance(self):
        """Test phase error inherits from BaseValidationError."""
        error = PhaseError("Test error")
        # Should inherit from BaseValidationError
        assert hasattr(error, 'validation_context')


class TestPhaseAbortedError:
    """Test phase aborted error type."""

    def test_phase_aborted_error_basic(self):
        """Test basic phase aborted error."""
        error = PhaseAbortedError("Phase was aborted", phase_name="data-loading")
        assert isinstance(error, PhaseError)
        assert "Phase: data-loading" in str(error)

    def test_phase_aborted_error_with_reason(self):
        """Test phase aborted error with abort reason."""
        error = PhaseAbortedError(
            "Phase aborted due to error threshold",
            abort_reason="Too many validation failures",
            phase_name="field-validation"
        )

        error_str = str(error)
        assert "Reason: Too many validation failures" in error_str
        assert error.abort_reason == "Too many validation failures"

    def test_phase_aborted_error_with_progress(self):
        """Test phase aborted error with progress information."""
        error = PhaseAbortedError(
            "Phase aborted mid-processing",
            phase_name="data-processing",
            stage="validation",
            items_processed=150,
            total_items=500
        )

        error_str = str(error)
        assert "Progress: 150/500" in error_str
        assert "Stage: validation" in error_str
        assert error.total_items == 500

    def test_phase_aborted_error_full_context(self):
        """Test phase aborted error with all context."""
        error = PhaseAbortedError(
            "Critical error caused abort",
            abort_reason="Memory exhaustion detected",
            phase_name="batch-processing",
            stage="processing",
            items_processed=1250,
            total_items=2000
        )

        error_str = str(error)
        assert "Critical error caused abort" in error_str
        assert "Phase: batch-processing" in error_str
        assert "Stage: processing" in error_str
        assert "Progress: 1250/2000" in error_str
        assert "Reason: Memory exhaustion detected" in error_str

    def test_phase_aborted_error_progress_override(self):
        """Test that progress format overrides simple processed count."""
        error = PhaseAbortedError(
            "Aborted",
            items_processed=10,
            total_items=100
        )

        error_str = str(error)
        # Should show progress format, not simple processed count
        assert "Progress: 10/100" in error_str
        assert "Processed: 10" not in error_str


class TestPhaseTimeoutError:
    """Test phase timeout error type."""

    def test_phase_timeout_error_basic(self):
        """Test basic phase timeout error."""
        error = PhaseTimeoutError("Phase timed out", phase_name="schema-validation")
        assert isinstance(error, PhaseError)
        assert "Phase: schema-validation" in str(error)

    def test_phase_timeout_error_with_timeout(self):
        """Test phase timeout error with timeout values."""
        error = PhaseTimeoutError(
            "Processing timeout exceeded",
            timeout_seconds=300.0,
            elapsed_seconds=305.7,
            phase_name="data-processing"
        )

        error_str = str(error)
        assert "Timeout: 300.0s" in error_str
        assert "Elapsed: 305.7s" in error_str
        assert error.timeout_seconds == 300.0
        assert error.elapsed_seconds == 305.7

    def test_phase_timeout_error_full_context(self):
        """Test phase timeout error with all context."""
        error = PhaseTimeoutError(
            "Validation phase exceeded time limit",
            timeout_seconds=180.0,
            elapsed_seconds=195.3,
            phase_name="relationship-validation",
            stage="analysis",
            items_processed=89
        )

        error_str = str(error)
        assert "Validation phase exceeded time limit" in error_str
        assert "Phase: relationship-validation" in error_str
        assert "Stage: analysis" in error_str
        assert "Processed: 89" in error_str
        assert "Timeout: 180.0s" in error_str
        assert "Elapsed: 195.3s" in error_str

    def test_phase_timeout_error_partial_timing(self):
        """Test phase timeout error with partial timing info."""
        # Test with only timeout
        error1 = PhaseTimeoutError("Timed out", timeout_seconds=60.0)
        assert "Timeout: 60.0s" in str(error1)
        assert "Elapsed:" not in str(error1)

        # Test with only elapsed
        error2 = PhaseTimeoutError("Timed out", elapsed_seconds=75.5)
        assert "Elapsed: 75.5s" in str(error2)
        assert "Timeout:" not in str(error2)


class TestPhaseResourceError:
    """Test phase resource error type."""

    def test_phase_resource_error_basic(self):
        """Test basic phase resource error."""
        error = PhaseResourceError("Resource exhausted", phase_name="bulk-processing")
        assert isinstance(error, PhaseError)
        assert "Phase: bulk-processing" in str(error)

    def test_phase_resource_error_with_resource_info(self):
        """Test phase resource error with resource information."""
        error = PhaseResourceError(
            "Memory limit exceeded",
            resource_type="memory",
            limit_reached="2GB",
            resource_usage="2.1GB",
            phase_name="data-loading"
        )

        error_str = str(error)
        assert "Resource: memory" in error_str
        assert "Limit: 2GB" in error_str
        assert "Usage: 2.1GB" in error_str
        assert error.resource_type == "memory"
        assert error.limit_reached == "2GB"
        assert error.resource_usage == "2.1GB"

    def test_phase_resource_error_full_context(self):
        """Test phase resource error with all context."""
        error = PhaseResourceError(
            "Disk space exhausted during processing",
            resource_type="disk",
            limit_reached="100GB",
            resource_usage="99.9GB",
            phase_name="file-processing",
            stage="export",
            items_processed=4500
        )

        error_str = str(error)
        assert "Disk space exhausted during processing" in error_str
        assert "Phase: file-processing" in error_str
        assert "Stage: export" in error_str
        assert "Processed: 4500" in error_str
        assert "Resource: disk" in error_str
        assert "Limit: 100GB" in error_str
        assert "Usage: 99.9GB" in error_str

    def test_phase_resource_error_different_resources(self):
        """Test phase resource error with different resource types."""
        resource_types = [
            ("memory", "8GB", "8.2GB"),
            ("disk", "50GB", "51GB"),
            ("threads", "100", "105"),
            ("connections", "1000", "1001")
        ]

        for resource_type, limit, usage in resource_types:
            error = PhaseResourceError(
                f"{resource_type} exhausted",
                resource_type=resource_type,
                limit_reached=limit,
                resource_usage=usage
            )
            error_str = str(error)
            assert f"Resource: {resource_type}" in error_str
            assert f"Limit: {limit}" in error_str
            assert f"Usage: {usage}" in error_str


class TestPhaseIntegrityError:
    """Test phase integrity error type."""

    def test_phase_integrity_error_basic(self):
        """Test basic phase integrity error."""
        error = PhaseIntegrityError("Data integrity check failed", phase_name="validation")
        assert isinstance(error, PhaseError)
        assert "Phase: validation" in str(error)

    def test_phase_integrity_error_with_check_info(self):
        """Test phase integrity error with integrity check information."""
        error = PhaseIntegrityError(
            "Checksum validation failed",
            integrity_check="md5_checksum",
            expected_value="abc123def456",
            actual_value="xyz789uvw012",
            phase_name="file-validation"
        )

        error_str = str(error)
        assert "Check: md5_checksum" in error_str
        assert "Expected: abc123def456" in error_str
        assert "Actual: xyz789uvw012" in error_str
        assert error.integrity_check == "md5_checksum"
        assert error.expected_value == "abc123def456"
        assert error.actual_value == "xyz789uvw012"

    def test_phase_integrity_error_full_context(self):
        """Test phase integrity error with all context."""
        error = PhaseIntegrityError(
            "Record count mismatch detected",
            integrity_check="record_count",
            expected_value="10000",
            actual_value="9998",
            phase_name="data-import",
            stage="verification"
        )

        error_str = str(error)
        assert "Record count mismatch detected" in error_str
        assert "Phase: data-import" in error_str
        assert "Stage: verification" in error_str
        assert "Check: record_count" in error_str
        assert "Expected: 10000" in error_str
        assert "Actual: 9998" in error_str

    def test_phase_integrity_error_different_checks(self):
        """Test phase integrity error with different check types."""
        check_scenarios = [
            ("checksum", "abc123", "def456"),
            ("record_count", "1000", "999"),
            ("schema_version", "1.2", "1.1"),
            ("data_hash", "hash1", "hash2")
        ]

        for check_type, expected, actual in check_scenarios:
            error = PhaseIntegrityError(
                f"{check_type} mismatch",
                integrity_check=check_type,
                expected_value=expected,
                actual_value=actual
            )
            error_str = str(error)
            assert f"Check: {check_type}" in error_str
            assert f"Expected: {expected}" in error_str
            assert f"Actual: {actual}" in error_str


class TestPhaseConfigurationError:
    """Test phase configuration error type."""

    def test_phase_configuration_error_basic(self):
        """Test basic phase configuration error."""
        error = PhaseConfigurationError("Invalid configuration", phase_name="setup")
        # Should inherit from BaseTransparencyError, not PhaseError
        assert "Phase: setup" in str(error)
        assert error.phase_name == "setup"

    def test_phase_configuration_error_with_parameter_info(self):
        """Test phase configuration error with parameter information."""
        valid_values = ["strict", "relaxed", "disabled"]
        error = PhaseConfigurationError(
            "Invalid validation mode",
            config_parameter="validation_mode",
            config_value="invalid",
            valid_values=valid_values,
            phase_name="validation-setup"
        )

        error_str = str(error)
        assert "Parameter: validation_mode" in error_str
        assert "Value: invalid" in error_str
        assert "Valid: strict, relaxed, disabled" in error_str
        assert error.config_parameter == "validation_mode"
        assert error.config_value == "invalid"
        assert error.valid_values == valid_values

    def test_phase_configuration_error_full_context(self):
        """Test phase configuration error with all context."""
        valid_values = ["json", "yaml", "xml"]
        error = PhaseConfigurationError(
            "Unsupported output format specified",
            config_parameter="output_format",
            config_value="csv",
            valid_values=valid_values,
            phase_name="export-configuration"
        )

        error_str = str(error)
        assert "Unsupported output format specified" in error_str
        assert "Phase: export-configuration" in error_str
        assert "Parameter: output_format" in error_str
        assert "Value: csv" in error_str
        assert "Valid: json, yaml, xml" in error_str

    def test_phase_configuration_error_context_order(self):
        """Test that phase name appears first in configuration error context."""
        error = PhaseConfigurationError(
            "Config error",
            phase_name="test-phase",
            config_parameter="test_param"
        )
        context_parts = error.get_context_parts()
        assert context_parts[0] == "Phase: test-phase"

    def test_phase_configuration_error_empty_valid_values(self):
        """Test phase configuration error with empty valid values list."""
        error = PhaseConfigurationError(
            "Invalid parameter",
            config_parameter="unknown_param",
            valid_values=[]
        )
        error_str = str(error)
        assert "Parameter: unknown_param" in error_str
        # Should handle empty valid values gracefully


class TestPhaseValidationRuleError:
    """Test phase validation rule error type."""

    def test_phase_validation_rule_error_basic(self):
        """Test basic phase validation rule error."""
        error = PhaseValidationRuleError("Rule validation failed", phase_name="field-validation")
        assert isinstance(error, PhaseError)
        assert "Phase: field-validation" in str(error)

    def test_phase_validation_rule_error_with_rule_info(self):
        """Test phase validation rule error with rule information."""
        error = PhaseValidationRuleError(
            "Field format validation failed",
            rule_name="email_format",
            rule_type="format",
            field_path="contacts[0].email",
            field_value="invalid-email",
            phase_name="data-validation"
        )

        error_str = str(error)
        assert "Rule: email_format" in error_str
        assert "Type: format" in error_str
        assert "Field: contacts[0].email" in error_str
        assert "Value: invalid-email" in error_str
        assert error.rule_name == "email_format"
        assert error.rule_type == "format"
        assert error.field_path == "contacts[0].email"
        assert error.field_value == "invalid-email"

    def test_phase_validation_rule_error_full_context(self):
        """Test phase validation rule error with all context."""
        error = PhaseValidationRuleError(
            "Reference validation rule violation",
            rule_name="cwe_reference_exists",
            rule_type="reference",
            field_path="mappings[5].target_id",
            field_value="CWE-999999",
            phase_name="mapping-validation",
            stage="reference-check"
        )

        error_str = str(error)
        assert "Reference validation rule violation" in error_str
        assert "Phase: mapping-validation" in error_str
        assert "Stage: reference-check" in error_str
        assert "Rule: cwe_reference_exists" in error_str
        assert "Type: reference" in error_str
        assert "Field: mappings[5].target_id" in error_str
        assert "Value: CWE-999999" in error_str

    def test_phase_validation_rule_error_different_rule_types(self):
        """Test phase validation rule error with different rule types."""
        rule_scenarios = [
            ("format", "email_format", "email", "invalid-email"),
            ("constraint", "max_length", "description", "too-long-value"),
            ("reference", "valid_cwe_id", "cwe_id", "CWE-INVALID"),
            ("required", "not_empty", "name", "")
        ]

        for rule_type, rule_name, field_path, field_value in rule_scenarios:
            error = PhaseValidationRuleError(
                f"{rule_type} rule failed",
                rule_name=rule_name,
                rule_type=rule_type,
                field_path=field_path,
                field_value=field_value
            )
            error_str = str(error)
            assert f"Rule: {rule_name}" in error_str
            assert f"Type: {rule_type}" in error_str
            assert f"Field: {field_path}" in error_str
            assert f"Value: {field_value}" in error_str


class TestPhaseErrorInheritance:
    """Test phase error inheritance hierarchy."""

    def test_phase_error_inheritance(self):
        """Test that all phase errors inherit properly."""
        # Phase operation errors
        assert issubclass(PhaseAbortedError, PhaseError)
        assert issubclass(PhaseTimeoutError, PhaseError)
        assert issubclass(PhaseResourceError, PhaseError)
        assert issubclass(PhaseIntegrityError, PhaseError)
        assert issubclass(PhaseValidationRuleError, PhaseError)

        # Configuration error inherits from BaseTransparencyError
        from ci.transparency.cwe.types.base.errors import BaseTransparencyError
        assert issubclass(PhaseConfigurationError, BaseTransparencyError)

    def test_exception_catching_by_base_types(self):
        """Test that errors can be caught by their base types."""
        # Create specific errors
        aborted_error = PhaseAbortedError("Aborted")
        timeout_error = PhaseTimeoutError("Timed out")
        resource_error = PhaseResourceError("Resource exhausted")

        # Test catching by base types
        for error in [aborted_error, timeout_error, resource_error]:
            try:
                raise error
            except PhaseError:
                pass
            except Exception:
                pytest.fail(f"Should be caught as PhaseError: {type(error)}")

    def test_catch_all_phase_errors(self):
        """Test catching all phase errors with base PhaseError."""
        errors = [
            PhaseAbortedError("Aborted"),
            PhaseTimeoutError("Timed out"),
            PhaseResourceError("Resource exhausted"),
            PhaseIntegrityError("Integrity failed"),
            PhaseValidationRuleError("Rule failed")
        ]

        for error in errors:
            try:
                raise error
            except PhaseError:
                pass
            except Exception:
                pytest.fail(f"Should be caught as PhaseError: {type(error)}")

    def test_configuration_error_separate_inheritance(self):
        """Test that configuration error has separate inheritance."""
        config_error = PhaseConfigurationError("Config error")

        # Should NOT be catchable as PhaseError
        try:
            raise config_error
        except PhaseError:
            pytest.fail("PhaseConfigurationError should not be caught as PhaseError")
        except Exception:
            pass  # Expected - should be caught by general exception handling


class TestPhaseErrorSlots:
    """Test that phase errors use __slots__ efficiently."""

    def test_phase_error_slots(self):
        """Test that phase errors have __slots__ defined."""
        # Check base error
        assert hasattr(PhaseError, '__slots__')
        assert 'phase_name' in PhaseError.__slots__
        assert 'stage' in PhaseError.__slots__
        assert 'items_processed' in PhaseError.__slots__

        # Check specialized errors
        assert hasattr(PhaseAbortedError, '__slots__')
        assert 'abort_reason' in PhaseAbortedError.__slots__

        assert hasattr(PhaseTimeoutError, '__slots__')
        assert 'timeout_seconds' in PhaseTimeoutError.__slots__

        assert hasattr(PhaseResourceError, '__slots__')
        assert 'resource_type' in PhaseResourceError.__slots__

    def test_phase_error_memory_efficiency(self):
        """Test that phase errors have __slots__."""
        error = PhaseError("test")
        assert hasattr(error, '__slots__')
        aborted_error = PhaseAbortedError("aborted")
        assert hasattr(aborted_error, '__slots__')
        timeout_error = PhaseTimeoutError("timeout")
        assert hasattr(timeout_error, '__slots__')


class TestPhaseContextFormatting:
    """Test phase error context formatting edge cases."""

    def test_empty_context_handling(self):
        """Test error with no additional context."""
        error = PhaseError("Simple error")
        context_parts = error.get_context_parts()
        # Should only have base context
        assert isinstance(context_parts, list)

    def test_none_values_ignored(self):
        """Test that None values are ignored in context."""
        error = PhaseError(
            "Test",
            phase_name=None,
            stage=None,
            items_processed=None
        )
        context_parts = error.get_context_parts()
        # Should not include None values
        assert not any("None" in part for part in context_parts)

    def test_zero_items_processed_included(self):
        """Test that zero items processed is included (not falsy ignored)."""
        error = PhaseError("Test", items_processed=0)
        error_str = str(error)
        assert "Processed: 0" in error_str

    def test_empty_list_handling(self):
        """Test handling of empty lists in context."""
        error = PhaseConfigurationError(
            "Config error",
            valid_values=[]  # Empty list
        )
        context_parts = error.get_context_parts()
        # Should handle empty list gracefully
        assert isinstance(context_parts, list)

    def test_numeric_precision_in_timeout(self):
        """Test numeric precision in timeout error formatting."""
        error = PhaseTimeoutError(
            "Timeout",
            timeout_seconds=123.456789,
            elapsed_seconds=125.987654321
        )
        error_str = str(error)
        assert "Timeout: 123.456789s" in error_str
        assert "Elapsed: 126.0s" in error_str  # Should be rounded to 1 decimal


class TestPhaseErrorMessages:
    """Test phase error message formatting and consistency."""

    def test_error_message_formatting_consistency(self):
        """Test that error messages are formatted consistently."""
        error = PhaseValidationRuleError(
            "Field validation failed",
            rule_name="format_check",
            field_path="data[0].value",
            phase_name="validation"
        )

        # Should use proper separator and ordering
        error_str = str(error)
        parts = error_str.split(" | ")
        assert len(parts) > 1
        assert "Field validation failed" in parts[0]

    def test_unicode_handling_in_phases(self):
        """Test handling of unicode in phase error messages."""
        error = PhaseError(
            "Phase failed: 验证失败",
            phase_name="数据验证"
        )
        error_str = str(error)
        assert "验证失败" in error_str
        assert "数据验证" in error_str

    def test_special_characters_in_field_paths(self):
        """Test handling of special characters in field paths."""
        field_path = "data['special-key'][0].sub-field"  # Complex field path
        error = PhaseValidationRuleError(
            "Validation error",
            field_path=field_path,
            phase_name="validation"
        )
        error_str = str(error)
        assert field_path in error_str

    def test_large_numeric_values(self):
        """Test formatting of large numeric values."""
        error = PhaseAbortedError(
            "Aborted",
            items_processed=1_500_000,
            total_items=2_000_000
        )
        error_str = str(error)
        assert "Progress: 1500000/2000000" in error_str

    def test_resource_units_formatting(self):
        """Test formatting of resource units."""
        resource_scenarios = [
            ("memory", "2.5GB", "3.1GB"),
            ("disk", "150TB", "155TB"),
            ("threads", "1000", "1024"),
            ("bandwidth", "100Mbps", "120Mbps")
        ]

        for resource_type, limit, usage in resource_scenarios:
            error = PhaseResourceError(
                f"{resource_type} limit exceeded",
                resource_type=resource_type,
                limit_reached=limit,
                resource_usage=usage
            )
            error_str = str(error)
            assert limit in error_str
            assert usage in error_str


class TestPhaseErrorEdgeCases:
    """Test phase error edge cases and unusual scenarios."""

    def test_extremely_long_phase_names(self):
        """Test handling of very long phase names."""
        long_phase_name = "very-long-phase-name-with-many-hyphens-and-descriptive-text-that-goes-on-and-on"
        error = PhaseError("Test", phase_name=long_phase_name)
        error_str = str(error)
        assert long_phase_name in error_str

    def test_nested_field_path_validation(self):
        """Test validation rule error with deeply nested field paths."""
        nested_path = "data.organizations[0].departments[5].employees[99].contact_info.addresses[0].postal_code"
        error = PhaseValidationRuleError(
            "Deep field validation failed",
            field_path=nested_path
        )
        error_str = str(error)
        assert nested_path in error_str

    def test_timeout_with_fractional_seconds(self):
        """Test timeout error with fractional second values."""
        error = PhaseTimeoutError(
            "Timeout",
            timeout_seconds=0.5,
            elapsed_seconds=0.75
        )
        error_str = str(error)
        assert "Timeout: 0.5s" in error_str
        assert "Elapsed: 0.8s" in error_str  # Should round to 1 decimal

    def test_empty_string_values_in_context(self):
        """Test handling of empty string values."""
        error = PhaseValidationRuleError(
            "Empty field validation",
            field_value="",  # Empty string
            field_path="required_field"
        )
        error_str = str(error)
        assert "Field: required_field" in error_str
        assert "Value:" in error_str  # Should include empty value context

    def test_resource_error_without_units(self):
        """Test resource error with numeric-only limits."""
        error = PhaseResourceError(
            "Connection limit exceeded",
            resource_type="connections",
            limit_reached="100",
            resource_usage="105"
        )
        error_str = str(error)
        assert "Limit: 100" in error_str
        assert "Usage: 105" in error_str


class TestPhaseRealWorldScenarios:
    """Test phase errors in realistic usage scenarios."""

    def test_cwe_validation_phase_abort(self):
        """Test realistic CWE validation phase abort scenario."""
        error = PhaseAbortedError(
            "CWE validation phase aborted due to excessive errors",
            abort_reason="Error rate exceeded 10% threshold",
            phase_name="cwe-field-validation",
            stage="processing",
            items_processed=250,
            total_items=1000
        )

        error_str = str(error)
        assert "cwe-field-validation" in error_str
        assert "Progress: 250/1000" in error_str
        assert "Error rate exceeded 10%" in error_str

    def test_standards_mapping_timeout(self):
        """Test realistic standards mapping timeout scenario."""
        error = PhaseTimeoutError(
            "Standards mapping validation exceeded time limit",
            timeout_seconds=600.0,
            elapsed_seconds=612.3,
            phase_name="standards-mapping-validation",
            stage="cross-reference-check",
            items_processed=1500
        )

        error_str = str(error)
        assert "standards-mapping-validation" in error_str
        assert "Timeout: 600.0s" in error_str
        assert "cross-reference-check" in error_str

    def test_batch_processing_resource_exhaustion(self):
        """Test realistic batch processing resource exhaustion."""
        error = PhaseResourceError(
            "Memory exhausted during batch CWE processing",
            resource_type="memory",
            limit_reached="8GB",
            resource_usage="8.1GB",
            phase_name="batch-cwe-processing",
            stage="aggregation",
            items_processed=50000
        )

        error_str = str(error)
        assert "batch-cwe-processing" in error_str
        assert "aggregation" in error_str
        assert "Memory exhausted" in error_str

    def test_data_integrity_check_failure(self):
        """Test realistic data integrity check failure."""
        error = PhaseIntegrityError(
            "CWE count mismatch after processing",
            integrity_check="cwe_count_verification",
            expected_value="1421",
            actual_value="1420",
            phase_name="post-processing-verification",
            stage="integrity-check"
        )

        error_str = str(error)
        assert "CWE count mismatch" in error_str
        assert "cwe_count_verification" in error_str
        assert "Expected: 1421" in error_str
        assert "Actual: 1420" in error_str

    def test_validation_rule_complex_scenario(self):
        """Test realistic complex validation rule scenario."""
        error = PhaseValidationRuleError(
            "CWE relationship validation failed",
            rule_name="valid_parent_child_relationship",
            rule_type="constraint",
            field_path="cwes[79].relationships[0].target_id",
            field_value="CWE-999999",
            phase_name="cwe-relationship-validation",
            stage="constraint-checking"
        )

        error_str = str(error)
        assert "CWE relationship validation failed" in error_str
        assert "valid_parent_child_relationship" in error_str
        assert "cwes[79].relationships[0].target_id" in error_str
        assert "CWE-999999" in error_str
