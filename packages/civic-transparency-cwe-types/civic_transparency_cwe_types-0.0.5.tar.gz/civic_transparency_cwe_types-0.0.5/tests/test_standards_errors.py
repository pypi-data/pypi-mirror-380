"""Tests for Standards domain error types.

Tests for standards-specific error types including context formatting,
error hierarchy, and specialized error information for standards processing.
"""

import pytest
from pathlib import Path

from ci.transparency.cwe.types.standards.errors import (
    # Base standards errors
    StandardsError,

    # Loading errors
    StandardsLoadingError,
    StandardsFileNotFoundError,
    StandardsParsingError,
    StandardsInvalidFormatError,
    StandardsMissingFieldError,

    # Validation errors
    StandardsValidationError,
    StandardsFieldValidationError,
    StandardsConstraintViolationError,

    # Mapping errors
    StandardsMappingError,
    StandardsInvalidMappingError,
    StandardsDuplicateMappingError,

    # Format and processing errors
    StandardsFormatError,
    StandardsConfigurationError,
    StandardsProcessingError,
    StandardsIntegrityError,
)


class TestStandardsError:
    """Test base Standards error functionality."""

    def test_standards_error_basic(self):
        """Test basic standards error creation."""
        error = StandardsError("Test error")
        assert str(error) == "Test error"
        assert error.standard_id is None
        assert error.framework is None

    def test_standards_error_with_standard_id(self):
        """Test standards error with standard ID context."""
        error = StandardsError("Test error", standard_id="NIST-SP-800-53")
        assert "Standard: NIST-SP-800-53" in str(error)
        assert error.standard_id == "NIST-SP-800-53"

    def test_standards_error_with_framework(self):
        """Test standards error with framework context."""
        error = StandardsError("Test error", framework="NIST")
        assert "Framework: NIST" in str(error)
        assert error.framework == "NIST"

    def test_standards_error_with_file_path(self):
        """Test standards error with file path context."""
        file_path = Path("standards") / "nist.yaml"
        error = StandardsError("Test error", file_path=file_path)
        assert "nist.yaml" in str(error)

    def test_standards_error_full_context(self):
        """Test standards error with all context information."""
        file_path = Path("standards") / "nist-sp-800-53.yaml"
        error = StandardsError(
            "Validation failed",
            standard_id="NIST-SP-800-53",
            framework="NIST",
            file_path=file_path
        )

        error_str = str(error)
        assert "Validation failed" in error_str
        assert "Standard: NIST-SP-800-53" in error_str
        assert "Framework: NIST" in error_str
        assert "nist-sp-800-53.yaml" in error_str

    def test_standards_error_context_order(self):
        """Test that standard ID appears first in context."""
        error = StandardsError("Test", standard_id="ISO-27001", framework="ISO")
        context_parts = error.get_context_parts()
        assert context_parts[0] == "Standard: ISO-27001"

    def test_standards_error_inheritance(self):
        """Test standards error inherits from BaseLoadingError."""
        error = StandardsError("Test error")
        # Should inherit from BaseLoadingError which provides file_path support
        assert hasattr(error, 'file_path')


class TestStandardsLoadingErrors:
    """Test standards loading error types."""

    def test_standards_loading_error(self):
        """Test base standards loading error."""
        error = StandardsLoadingError("Loading failed", standard_id="NIST-SP-800-53")
        assert isinstance(error, StandardsError)
        assert "Standard: NIST-SP-800-53" in str(error)

    def test_standards_file_not_found_error(self):
        """Test standards file not found error."""
        file_path = Path("missing") / "nist.yaml"
        error = StandardsFileNotFoundError(
            "Standards file not found",
            standard_id="NIST-SP-800-53",
            file_path=file_path
        )
        assert isinstance(error, StandardsLoadingError)
        assert "Standard: NIST-SP-800-53" in str(error)
        assert "nist.yaml" in str(error)

    def test_standards_parsing_error_basic(self):
        """Test basic standards parsing error."""
        error = StandardsParsingError("Parse failed", standard_id="ISO-27001")
        assert isinstance(error, StandardsLoadingError)
        assert "Standard: ISO-27001" in str(error)

    def test_standards_parsing_error_full(self):
        """Test standards parsing error with all context."""
        file_path = Path("standards") / "invalid.yaml"
        error = StandardsParsingError(
            "YAML syntax error",
            parser_type="YAML",
            line_number=25,
            parse_details="Invalid control mapping structure",
            standard_id="NIST-SP-800-53",
            file_path=file_path
        )

        error_str = str(error)
        assert "YAML syntax error" in error_str
        assert "Parser: YAML" in error_str
        assert "Line: 25" in error_str
        assert "Details: Invalid control mapping structure" in error_str
        assert "Standard: NIST-SP-800-53" in error_str

    def test_standards_invalid_format_error(self):
        """Test standards invalid format error."""
        file_path = Path("standards") / "bad_format.txt"
        supported_formats = ["YAML", "JSON", "XML"]
        error = StandardsInvalidFormatError(
            "Unsupported format",
            detected_format="TXT",
            supported_formats=supported_formats,
            format_issue="Standards files must be structured data",
            standard_id="NIST-SP-800-53",
            file_path=file_path
        )

        error_str = str(error)
        assert "Detected: TXT" in error_str
        assert "Supported: YAML, JSON, XML" in error_str
        assert "Issue: Standards files must be structured data" in error_str

    def test_standards_missing_field_error(self):
        """Test standards missing field error."""
        required_fields = ["id", "title", "controls", "mappings"]
        error = StandardsMissingFieldError(
            "Required field missing",
            field_name="controls",
            required_fields=required_fields,
            standard_id="ISO-27001"
        )

        error_str = str(error)
        assert "Field: controls" in error_str
        assert "Required: id, title, controls, mappings" in error_str

    def test_standards_missing_field_empty_list(self):
        """Test standards missing field error with empty required list."""
        error = StandardsMissingFieldError(
            "Field missing",
            field_name="title",
            required_fields=[],  # Empty list should be handled gracefully
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Field: title" in error_str
        # Should not crash on empty required fields


class TestStandardsValidationErrors:
    """Test standards validation error types."""

    def test_standards_validation_error(self):
        """Test base standards validation error."""
        error = StandardsValidationError(
            "Validation failed",
            validation_type="schema",
            standard_id="NIST-SP-800-53",
            framework="NIST"
        )

        assert isinstance(error, StandardsError)
        assert "Validation: schema" in str(error)
        assert "Standard: NIST-SP-800-53" in str(error)
        assert "Framework: NIST" in str(error)

    def test_standards_field_validation_error(self):
        """Test standards field validation error."""
        error = StandardsFieldValidationError(
            "Control ID validation failed",
            field_name="controls[0].id",
            field_value="invalid-control-id",
            validation_rule="must match [A-Z]+-[0-9]+",
            expected_value="AC-1",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Field: controls[0].id" in error_str
        assert "Value: invalid-control-id" in error_str
        assert "Expected: AC-1" in error_str
        assert "Rule: must match [A-Z]+-[0-9]+" in error_str
        assert "Validation: field" in error_str  # Should be set automatically

    def test_standards_constraint_violation_error(self):
        """Test standards constraint violation error."""
        error = StandardsConstraintViolationError(
            "Control count constraint violated",
            constraint_name="max_controls_per_family",
            expected="100",
            actual="150",
            standard_id="NIST-SP-800-53",
            framework="NIST"
        )

        error_str = str(error)
        assert "Constraint: max_controls_per_family" in error_str
        assert "Expected: 100" in error_str
        assert "Actual: 150" in error_str
        assert "Validation: constraint" in error_str  # Should be set automatically

    def test_standards_validation_error_minimal(self):
        """Test standards validation error with minimal context."""
        error = StandardsValidationError("Simple validation failure")
        error_str = str(error)
        assert "Simple validation failure" in error_str
        # Should not crash with minimal context


class TestStandardsMappingErrors:
    """Test standards mapping error types."""

    def test_standards_mapping_error(self):
        """Test base standards mapping error."""
        error = StandardsMappingError(
            "Mapping failed",
            mapping_key="AC-1",
            target_id="CWE-79",
            mapping_type="cwe",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Mapping: AC-1" in error_str
        assert "Target: CWE-79" in error_str
        assert "Type: cwe" in error_str

    def test_standards_invalid_mapping_error(self):
        """Test standards invalid mapping error."""
        error = StandardsInvalidMappingError(
            "Invalid CWE reference in mapping",
            target_id="CWE-999",
            mapping_key="AC-1",
            reference_source="cwe_mappings",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Target: CWE-999" in error_str
        assert "Mapping: AC-1" in error_str
        assert "Source: cwe_mappings" in error_str
        assert "Type: invalid" in error_str  # Should be set automatically

    def test_standards_duplicate_mapping_error(self):
        """Test standards duplicate mapping error."""
        error = StandardsDuplicateMappingError(
            "Duplicate mapping detected",
            mapping_key="AC-1",
            existing_target="CWE-79",
            duplicate_target="CWE-89",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Mapping: AC-1" in error_str
        assert "Existing: CWE-79" in error_str
        assert "Duplicate: CWE-89" in error_str
        assert "Type: duplicate" in error_str  # Should be set automatically

    def test_standards_mapping_error_partial_context(self):
        """Test standards mapping error with partial context."""
        error = StandardsMappingError(
            "Mapping error",
            mapping_key="AC-2",
            # Missing target_id and mapping_type
            standard_id="ISO-27001"
        )

        error_str = str(error)
        assert "Mapping: AC-2" in error_str
        assert "Standard: ISO-27001" in error_str
        # Should handle missing fields gracefully


class TestStandardsFormatAndProcessingErrors:
    """Test standards format and processing error types."""

    def test_standards_format_error(self):
        """Test standards format error."""
        error = StandardsFormatError(
            "Export format error",
            format_type="export",
            export_template="nist-oscal",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Format: export" in error_str
        assert "Template: nist-oscal" in error_str

    def test_standards_configuration_error(self):
        """Test standards configuration error."""
        valid_values = ["yaml", "json", "xml", "oscal"]
        error = StandardsConfigurationError(
            "Invalid output format",
            config_key="output_format",
            config_value="txt",
            valid_values=valid_values
        )

        error_str = str(error)
        assert "Config: output_format" in error_str
        assert "Value: txt" in error_str
        assert "Valid: yaml, json, xml, oscal" in error_str

    def test_standards_processing_error(self):
        """Test standards processing error."""
        error = StandardsProcessingError(
            "Processing failed during mapping validation",
            operation="validate_mappings",
            stage="validation",
            processed_count=45,
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Operation: validate_mappings" in error_str
        assert "Stage: validation" in error_str
        assert "Processed: 45" in error_str

    def test_standards_integrity_error(self):
        """Test standards integrity error."""
        error = StandardsIntegrityError(
            "Control count mismatch",
            integrity_check="control_count",
            expected_value="864",
            actual_value="863",
            standard_id="NIST-SP-800-53"
        )

        error_str = str(error)
        assert "Check: control_count" in error_str
        assert "Expected: 864" in error_str
        assert "Actual: 863" in error_str

    def test_standards_configuration_error_minimal(self):
        """Test standards configuration error with minimal context."""
        error = StandardsConfigurationError("Configuration error")
        error_str = str(error)
        assert "Configuration error" in error_str
        # Should not crash with minimal context


class TestStandardsErrorInheritance:
    """Test standards error inheritance hierarchy."""

    def test_standards_error_inheritance(self):
        """Test that all standards errors inherit properly."""
        # Loading errors
        assert issubclass(StandardsLoadingError, StandardsError)
        assert issubclass(StandardsFileNotFoundError, StandardsLoadingError)
        assert issubclass(StandardsParsingError, StandardsLoadingError)
        assert issubclass(StandardsInvalidFormatError, StandardsLoadingError)
        assert issubclass(StandardsMissingFieldError, StandardsLoadingError)

        # Validation errors
        assert issubclass(StandardsValidationError, StandardsError)
        assert issubclass(StandardsFieldValidationError, StandardsValidationError)
        assert issubclass(StandardsConstraintViolationError, StandardsValidationError)

        # Mapping errors
        assert issubclass(StandardsMappingError, StandardsError)
        assert issubclass(StandardsInvalidMappingError, StandardsMappingError)
        assert issubclass(StandardsDuplicateMappingError, StandardsMappingError)

        # Processing errors
        assert issubclass(StandardsFormatError, StandardsError)
        assert issubclass(StandardsProcessingError, StandardsError)
        assert issubclass(StandardsIntegrityError, StandardsError)

    def test_exception_catching_by_base_types(self):
        """Test that errors can be caught by their base types."""
        # Create specific errors
        parsing_error = StandardsParsingError("Parse failed")
        field_error = StandardsFieldValidationError("Field invalid")
        mapping_error = StandardsInvalidMappingError("Invalid mapping")

        # Test catching by base types
        try:
            raise parsing_error
        except StandardsLoadingError:
            pass
        except Exception:
            pytest.fail("Should be caught as StandardsLoadingError")

        try:
            raise field_error
        except StandardsValidationError:
            pass
        except Exception:
            pytest.fail("Should be caught as StandardsValidationError")

        try:
            raise mapping_error
        except StandardsMappingError:
            pass
        except Exception:
            pytest.fail("Should be caught as StandardsMappingError")

    def test_catch_all_standards_errors(self):
        """Test catching all standards errors with base StandardsError."""
        errors = [
            StandardsLoadingError("Loading error"),
            StandardsValidationError("Validation error"),
            StandardsMappingError("Mapping error"),
            StandardsFormatError("Format error")
        ]

        for error in errors:
            try:
                raise error
            except StandardsError:
                pass
            except Exception:
                pytest.fail(f"Should be caught as StandardsError: {type(error)}")


class TestStandardsErrorSlots:
    """Test that standards errors use __slots__ efficiently."""

    def test_standards_error_slots(self):
        """Test that standards errors have __slots__ defined."""
        # Check base error
        assert hasattr(StandardsError, '__slots__')
        assert 'standard_id' in StandardsError.__slots__
        assert 'framework' in StandardsError.__slots__

        # Check specialized errors
        assert hasattr(StandardsParsingError, '__slots__')
        assert 'parser_type' in StandardsParsingError.__slots__

        assert hasattr(StandardsFieldValidationError, '__slots__')
        assert 'field_name' in StandardsFieldValidationError.__slots__

        assert hasattr(StandardsMappingError, '__slots__')
        assert 'mapping_key' in StandardsMappingError.__slots__

    def test_standards_error_memory_efficiency(self):
        """Test that standards errors have __slots__."""
        error = StandardsError("test")
        assert hasattr(error, '__slots__')




class TestStandardsContextFormatting:
    """Test standards error context formatting edge cases."""

    def test_empty_context_handling(self):
        """Test error with no additional context."""
        error = StandardsError("Simple error")
        context_parts = error.get_context_parts()
        # Should only have base context
        assert isinstance(context_parts, list)

    def test_none_values_ignored(self):
        """Test that None values are ignored in context."""
        error = StandardsError(
            "Test",
            standard_id=None,
            framework=None
        )
        context_parts = error.get_context_parts()
        # Should not include None values
        assert not any("None" in part for part in context_parts)

    def test_empty_list_handling(self):
        """Test handling of empty lists in context."""
        error = StandardsMissingFieldError(
            "Missing fields",
            required_fields=[]  # Empty list
        )
        context_parts = error.get_context_parts()
        # Should handle empty list gracefully
        assert isinstance(context_parts, list)

    def test_complex_path_formatting(self):
        """Test that complex Path objects are formatted correctly."""
        file_path = Path("standards") / "frameworks" / "nist" / "sp-800-53-r5.yaml"
        error = StandardsError("Test", file_path=file_path)
        error_str = str(error)
        assert "sp-800-53-r5.yaml" in error_str

    def test_long_standard_id_formatting(self):
        """Test formatting of long standard identifiers."""
        long_standard_id = "NIST-SP-800-53-Rev-5-AC-Access-Control-Family"
        error = StandardsError("Test", standard_id=long_standard_id)
        error_str = str(error)
        assert long_standard_id in error_str


class TestStandardsErrorMessages:
    """Test standards error message formatting and consistency."""

    def test_error_message_formatting_consistency(self):
        """Test that error messages are formatted consistently."""
        file_path = Path("standards") / "nist.yaml"
        error = StandardsFieldValidationError(
            "Control validation failed",
            field_name="controls[0].id",
            field_value="invalid",
            standard_id="NIST-SP-800-53",
            file_path=file_path
        )

        # Should use proper separator and ordering
        error_str = str(error)
        parts = error_str.split(" | ")
        assert len(parts) > 1
        assert "Control validation failed" in parts[0]

    def test_unicode_handling_in_standards(self):
        """Test handling of unicode in standards error messages."""
        error = StandardsError(
            "Test with unicode: 标准验证失败",
            standard_id="GB-T-22080-2016"
        )
        error_str = str(error)
        assert "标准验证失败" in error_str
        assert "GB-T-22080-2016" in error_str

    def test_special_characters_in_mappings(self):
        """Test handling of special characters in mapping keys."""
        mapping_key = "AC-1(a)(1)"  # Common NIST control format with special chars
        error = StandardsMappingError(
            "Mapping error",
            mapping_key=mapping_key,
            standard_id="NIST-SP-800-53"
        )
        error_str = str(error)
        assert mapping_key in error_str

    def test_framework_specific_context(self):
        """Test framework-specific context in error messages."""
        frameworks = ["NIST", "ISO", "COBIT", "COSO", "SOC2"]

        for framework in frameworks:
            error = StandardsError(
                "Framework test",
                framework=framework,
                standard_id=f"{framework}-TEST"
            )
            error_str = str(error)
            assert f"Framework: {framework}" in error_str
            assert f"Standard: {framework}-TEST" in error_str


class TestStandardsErrorEdgeCases:
    """Test standards error edge cases and unusual scenarios."""

    def test_extremely_long_field_names(self):
        """Test handling of very long field names."""
        long_field = "controls[0].implementation_guidance.assessment_procedures.assessment_objects.assessment_methods[0].assessment_details"
        error = StandardsFieldValidationError(
            "Field too nested",
            field_name=long_field
        )
        error_str = str(error)
        assert long_field in error_str

    def test_mapping_with_special_target_ids(self):
        """Test mapping errors with special target ID formats."""
        special_targets = [
            "CWE-79",           # Standard CWE
            "CAPEC-66",         # CAPEC attack pattern
            "CVE-2021-44228",   # CVE identifier
            "CCE-27072-8",      # CCE identifier
        ]

        for target_id in special_targets:
            error = StandardsInvalidMappingError(
                "Invalid mapping",
                target_id=target_id,
                mapping_key="AC-1"
            )
            error_str = str(error)
            assert target_id in error_str

    def test_configuration_error_with_complex_values(self):
        """Test configuration error with complex configuration values."""
        error = StandardsConfigurationError(
            "Complex config error",
            config_key="mapping_validation.cwe_references.validation_strategy",
            config_value="strict_with_fallback_to_fuzzy_matching",
            valid_values=["strict", "relaxed", "disabled"]
        )
        error_str = str(error)
        assert "strict_with_fallback_to_fuzzy_matching" in error_str

    def test_circular_reference_in_context(self):
        """Test error context doesn't create circular references."""
        error = StandardsInvalidMappingError(
            "Circular mapping",
            target_id="SELF-REFERENCE",
            mapping_key="SELF-REFERENCE"
        )
        error_str = str(error)
        # Should handle self-references without issues
        assert "SELF-REFERENCE" in error_str
        assert error_str.count("SELF-REFERENCE") >= 2  # Should appear for both mapping and target

    def test_empty_string_values_in_context(self):
        """Test handling of empty string values."""
        error = StandardsFieldValidationError(
            "Empty field value",
            field_name="title",
            field_value="",  # Empty string
            expected_value="Non-empty title"
        )
        error_str = str(error)
        assert "Field: title" in error_str
        assert "Value:" in error_str  # Should include empty value context
        assert "Expected: Non-empty title" in error_str

    def test_numeric_values_in_constraints(self):
        """Test handling of numeric values in constraint violations."""
        error = StandardsConstraintViolationError(
            "Numeric constraint",
            constraint_name="min_control_count",
            expected="100",
            actual="85"
        )
        error_str = str(error)
        assert "Expected: 100" in error_str
        assert "Actual: 85" in error_str


class TestStandardsRealWorldScenarios:
    """Test standards errors in realistic usage scenarios."""

    def test_nist_sp_800_53_parsing_error(self):
        """Test realistic NIST SP 800-53 parsing error."""
        error = StandardsParsingError(
            "Failed to parse control family structure",
            parser_type="YAML",
            line_number=1247,
            parse_details="Invalid control identifier format in AC family",
            standard_id="NIST-SP-800-53-Rev-5",
            file_path=Path("standards") / "nist" / "sp-800-53-r5-controls.yaml"
        )

        error_str = str(error)
        assert "NIST-SP-800-53-Rev-5" in error_str
        assert "Line: 1247" in error_str
        assert "AC family" in error_str

    def test_iso_27001_mapping_validation_error(self):
        """Test realistic ISO 27001 mapping validation error."""
        error = StandardsInvalidMappingError(
            "CWE mapping references non-existent weakness",
            target_id="CWE-999999",
            mapping_key="A.12.6.1",
            reference_source="cwe_mappings",
            standard_id="ISO-27001-2013"
        )

        error_str = str(error)
        assert "ISO-27001-2013" in error_str
        assert "A.12.6.1" in error_str
        assert "CWE-999999" in error_str

    def test_cobit_control_validation_error(self):
        """Test realistic COBIT control validation error."""
        error = StandardsFieldValidationError(
            "COBIT control objective validation failed",
            field_name="control_objectives[15].maturity_level",
            field_value="6",
            validation_rule="maturity_level must be 1-5",
            expected_value="1-5",
            standard_id="COBIT-2019"
        )

        error_str = str(error)
        assert "COBIT-2019" in error_str
        assert "maturity_level" in error_str
        assert "must be 1-5" in error_str

    def test_multi_framework_mapping_conflict(self):
        """Test error involving multiple framework conflicts."""
        error = StandardsDuplicateMappingError(
            "Control mapping conflict between frameworks",
            mapping_key="Access_Control_Policy",
            existing_target="NIST-AC-1",
            duplicate_target="ISO-A.9.1.1",
            standard_id="UNIFIED-CONTROL-FRAMEWORK"
        )

        error_str = str(error)
        assert "NIST-AC-1" in error_str
        assert "ISO-A.9.1.1" in error_str
        assert "Access_Control_Policy" in error_str
