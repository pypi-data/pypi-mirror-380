"""Tests for CWE domain error types.

Tests for CWE-specific error types including context formatting,
error hierarchy, and specialized error information.
"""

import pytest
from pathlib import Path

from ci.transparency.cwe.types.cwe.errors import (
    # Base CWE errors
    CweError,

    # Loading errors
    CweLoadingError,
    CweFileNotFoundError,
    CweParsingError,
    CweDuplicateError,
    CweInvalidFormatError,
    CweMissingFieldError,

    # Validation errors
    CweValidationError,
    CweFieldValidationError,
    CweSchemaValidationError,
    CweConstraintViolationError,

    # Relationship errors
    CweRelationshipError,
    CweCircularRelationshipError,
    CweOrphanedError,
    CweInvalidReferenceError,

    # Processing errors
    CweProcessingError,
    CweIntegrityError,
    CweConfigurationError,
)


class TestCweError:
    """Test base CWE error functionality."""

    def test_cwe_error_basic(self):
        """Test basic CWE error creation."""
        error = CweError("Test error")
        assert str(error) == "Test error"
        assert error.cwe_id is None
        assert error.category is None

    def test_cwe_error_with_cwe_id(self):
        """Test CWE error with CWE ID context."""
        error = CweError("Test error", cwe_id="CWE-79")
        assert "CWE: CWE-79" in str(error)
        assert error.cwe_id == "CWE-79"

    def test_cwe_error_with_category(self):
        """Test CWE error with category context."""
        error = CweError("Test error", category="injection")
        assert "Category: injection" in str(error)
        assert error.category == "injection"

    def test_cwe_error_with_file_path(self):
        """Test CWE error with file path context."""
        file_path = Path("test.yaml")
        error = CweError("Test error", file_path=file_path)
        assert "File: test.yaml" in str(error)

    def test_cwe_error_full_context(self):
        """Test CWE error with all context information."""
        file_path = Path("cwe-79.yaml")
        error = CweError(
            "Validation failed",
            cwe_id="CWE-79",
            category="injection",
            file_path=file_path
        )

        error_str = str(error)
        assert "Validation failed" in error_str
        assert "CWE: CWE-79" in error_str
        assert "Category: injection" in error_str
        assert "File: cwe-79.yaml" in error_str

    def test_cwe_error_context_order(self):
        """Test that CWE ID appears first in context."""
        error = CweError("Test", cwe_id="CWE-79", category="injection")
        context_parts = error.get_context_parts()
        assert context_parts[0] == "CWE: CWE-79"


class TestCweLoadingErrors:
    """Test CWE loading error types."""

    def test_cwe_loading_error(self):
        """Test base CWE loading error."""
        error = CweLoadingError("Loading failed", cwe_id="CWE-79")
        assert isinstance(error, CweError)
        assert "CWE: CWE-79" in str(error)

    def test_cwe_file_not_found_error(self):
        """Test CWE file not found error."""
        file_path = Path("missing.yaml")
        error = CweFileNotFoundError("File not found", file_path=file_path)
        assert isinstance(error, CweLoadingError)
        assert "File: missing.yaml" in str(error)

    def test_cwe_parsing_error_basic(self):
        """Test basic CWE parsing error."""
        error = CweParsingError("Parse failed", cwe_id="CWE-79")
        assert isinstance(error, CweLoadingError)
        assert "CWE: CWE-79" in str(error)

    def test_cwe_parsing_error_full(self):
        """Test CWE parsing error with all context."""
        file_path = Path("invalid.yaml")
        error = CweParsingError(
            "YAML syntax error",
            parser_type="YAML",
            line_number=15,
            parse_details="Invalid indentation",
            cwe_id="CWE-79",
            file_path=file_path
        )

        error_str = str(error)
        assert "YAML syntax error" in error_str
        assert "Parser: YAML" in error_str
        assert "Line: 15" in error_str
        assert "Details: Invalid indentation" in error_str
        assert "CWE: CWE-79" in error_str

    def test_cwe_duplicate_error(self):
        """Test CWE duplicate error."""
        existing_file = Path("original.yaml")
        duplicate_file = Path("duplicate.yaml")
        error = CweDuplicateError(
            "Duplicate CWE ID",
            cwe_id="CWE-79",
            existing_file=existing_file,
            duplicate_file=duplicate_file
        )

        error_str = str(error)
        assert "CWE: CWE-79" in error_str
        assert "Existing: original.yaml" in error_str
        assert "Duplicate: duplicate.yaml" in error_str

    def test_cwe_invalid_format_error(self):
        """Test CWE invalid format error."""
        file_path = Path("bad_format.txt")
        error = CweInvalidFormatError(
            "Unsupported format",
            expected_format="YAML",
            detected_format="TXT",
            format_issue="File extension not supported",
            file_path=file_path
        )

        error_str = str(error)
        assert "Expected: YAML" in error_str
        assert "Detected: TXT" in error_str
        assert "Issue: File extension not supported" in error_str

    def test_cwe_missing_field_error(self):
        """Test CWE missing field error."""
        required_fields = ["id", "name", "description"]
        error = CweMissingFieldError(
            "Required field missing",
            field_name="name",
            required_fields=required_fields,
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Field: name" in error_str
        assert "Required: id, name, description" in error_str


class TestCweValidationErrors:
    """Test CWE validation error types."""

    def test_cwe_validation_error(self):
        """Test base CWE validation error."""
        error = CweValidationError(
            "Validation failed",
            validation_type="schema",
            cwe_id="CWE-79"
        )

        assert isinstance(error, CweError)
        assert "Validation: schema" in str(error)

    def test_cwe_field_validation_error(self):
        """Test CWE field validation error."""
        error = CweFieldValidationError(
            "Field validation failed",
            field_name="relationships[0].id",
            field_value="invalid-id",
            validation_rule="must match CWE-\\d+",
            expected_value="CWE-123",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Field: relationships[0].id" in error_str
        assert "Value: invalid-id" in error_str
        assert "Expected: CWE-123" in error_str
        assert "Rule: must match CWE-\\d+" in error_str

    def test_cwe_schema_validation_error(self):
        """Test CWE schema validation error."""
        error = CweSchemaValidationError(
            "Schema validation failed",
            schema_name="cwe-definition",
            schema_version="1.0",
            field_path="relationships[0]",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Schema: cwe-definition-1.0" in error_str
        assert "Field: relationships[0]" in error_str

    def test_cwe_constraint_violation_error(self):
        """Test CWE constraint violation error."""
        error = CweConstraintViolationError(
            "Constraint violated",
            constraint_name="max_relationships",
            constraint_value="10",
            actual_value="15",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Constraint: max_relationships" in error_str
        assert "Expected: 10" in error_str
        assert "Actual: 15" in error_str


class TestCweRelationshipErrors:
    """Test CWE relationship error types."""

    def test_cwe_relationship_error(self):
        """Test base CWE relationship error."""
        error = CweRelationshipError(
            "Relationship invalid",
            related_cwe_id="CWE-80",
            relationship_type="ChildOf",
            relationship_direction="outbound",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Related: CWE-80" in error_str
        assert "Type: ChildOf" in error_str
        assert "Direction: outbound" in error_str

    def test_cwe_circular_relationship_error(self):
        """Test CWE circular relationship error."""
        chain = ["CWE-79", "CWE-80", "CWE-81", "CWE-79"]
        error = CweCircularRelationshipError(
            "Circular dependency detected",
            relationship_chain=chain,
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Chain: CWE-79 → CWE-80 → CWE-81 → CWE-79" in error_str

    def test_cwe_orphaned_error(self):
        """Test CWE orphaned error."""
        error = CweOrphanedError(
            "CWE has no relationships",
            cwe_id="CWE-79",
            category="injection"
        )

        error_str = str(error)
        assert "CWE: CWE-79" in error_str
        assert "Category: injection" in error_str

    def test_cwe_invalid_reference_error(self):
        """Test CWE invalid reference error."""
        error = CweInvalidReferenceError(
            "Invalid CWE reference",
            related_cwe_id="CWE-999",
            reference_source="relationships",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Related: CWE-999" in error_str
        assert "Source: relationships" in error_str


class TestCweProcessingErrors:
    """Test CWE processing error types."""

    def test_cwe_processing_error(self):
        """Test CWE processing error."""
        error = CweProcessingError(
            "Processing failed",
            operation="validation",
            processed_count=50,
            total_count=100
        )

        error_str = str(error)
        assert "Operation: validation" in error_str
        assert "Progress: 50/100" in error_str

    def test_cwe_processing_error_partial(self):
        """Test CWE processing error with only processed count."""
        error = CweProcessingError(
            "Processing stopped",
            processed_count=25
        )

        error_str = str(error)
        assert "Processed: 25" in error_str

    def test_cwe_integrity_error(self):
        """Test CWE integrity error."""
        error = CweIntegrityError(
            "Data integrity violation",
            integrity_check="checksum",
            expected_value="abc123",
            actual_value="def456",
            cwe_id="CWE-79"
        )

        error_str = str(error)
        assert "Check: checksum" in error_str
        assert "Expected: abc123" in error_str
        assert "Actual: def456" in error_str

    def test_cwe_configuration_error(self):
        """Test CWE configuration error."""
        valid_values = ["yaml", "json", "xml"]
        error = CweConfigurationError(
            "Invalid configuration",
            config_key="file_format",
            config_value="txt",
            valid_values=valid_values
        )

        error_str = str(error)
        assert "Config: file_format" in error_str
        assert "Value: txt" in error_str
        assert "Valid: yaml, json, xml" in error_str


class TestErrorInheritance:
    """Test error inheritance hierarchy."""

    def test_cwe_error_inheritance(self):
        """Test that all CWE errors inherit properly."""
        # Loading errors
        assert issubclass(CweLoadingError, CweError)
        assert issubclass(CweFileNotFoundError, CweLoadingError)
        assert issubclass(CweParsingError, CweLoadingError)
        assert issubclass(CweDuplicateError, CweLoadingError)
        assert issubclass(CweInvalidFormatError, CweLoadingError)
        assert issubclass(CweMissingFieldError, CweLoadingError)

        # Validation errors
        assert issubclass(CweValidationError, CweError)
        assert issubclass(CweFieldValidationError, CweValidationError)
        assert issubclass(CweSchemaValidationError, CweValidationError)
        assert issubclass(CweConstraintViolationError, CweValidationError)

        # Relationship errors
        assert issubclass(CweRelationshipError, CweValidationError)
        assert issubclass(CweCircularRelationshipError, CweRelationshipError)
        assert issubclass(CweOrphanedError, CweRelationshipError)
        assert issubclass(CweInvalidReferenceError, CweRelationshipError)

    def test_exception_catching(self):
        """Test that errors can be caught by their base types."""
        # Create specific errors
        parsing_error = CweParsingError("Parse failed")
        field_error = CweFieldValidationError("Field invalid")
        relationship_error = CweCircularRelationshipError("Circular dependency")

        # Test catching by base types
        try:
            raise parsing_error
        except CweLoadingError:
            pass
        except Exception:
            pytest.fail("Should be caught as CweLoadingError")

        try:
            raise field_error
        except CweValidationError:
            pass
        except Exception:
            pytest.fail("Should be caught as CweValidationError")

        try:
            raise relationship_error
        except CweRelationshipError:
            pass
        except Exception:
            pytest.fail("Should be caught as CweRelationshipError")


class TestErrorSlots:
    """Test that errors use __slots__ efficiently."""

    def test_error_slots(self):
        """Test that errors have __slots__ defined."""
        # Check base error
        assert hasattr(CweError, '__slots__')
        assert 'cwe_id' in CweError.__slots__
        assert 'category' in CweError.__slots__

        # Check specialized errors
        assert hasattr(CweParsingError, '__slots__')
        assert 'parser_type' in CweParsingError.__slots__

        assert hasattr(CweFieldValidationError, '__slots__')
        assert 'field_name' in CweFieldValidationError.__slots__

    def test_error_memory_efficiency(self):
        """Test that errors have __slots__."""
        error = CweError("test")
        assert hasattr(error, '__slots__')


class TestErrorContextFormatting:
    """Test error context formatting edge cases."""

    def test_empty_context(self):
        """Test error with no additional context."""
        error = CweError("Simple error")
        context_parts = error.get_context_parts()
        # Should only have base context from BaseLoadingError
        assert len(context_parts) >= 0

    def test_none_values_ignored(self):
        """Test that None values are ignored in context."""
        error = CweError("Test", cwe_id=None, category=None)
        context_parts = error.get_context_parts()
        # Should not include None values
        assert not any("None" in part for part in context_parts)

    def test_empty_list_handling(self):
        """Test handling of empty lists in context."""
        error = CweMissingFieldError(
            "Missing fields",
            required_fields=[]
        )
        context_parts = error.get_context_parts()
        # Should handle empty list gracefully
        assert isinstance(context_parts, list)

    def test_path_object_formatting(self):
        """Test that Path objects are formatted correctly."""
        file_path = Path("some") / "nested" / "path.yaml"
        error = CweError("Test", file_path=file_path)
        error_str = str(error)
        assert "path.yaml" in error_str


class TestErrorMessages:
    """Test error message formatting and consistency."""

    def test_error_message_formatting(self):
        """Test that error messages are formatted consistently."""
        file_path = Path("test.yaml")
        error = CweFieldValidationError(
            "Field validation failed",
            field_name="name",
            field_value="",
            cwe_id="CWE-79",
            file_path=file_path
        )

        # Should use proper separator and ordering
        error_str = str(error)
        parts = error_str.split(" | ")
        assert len(parts) > 1
        assert "Field validation failed" in parts[0]

    def test_unicode_handling(self):
        """Test handling of unicode in error messages."""
        error = CweError("Test with unicode: 测试", cwe_id="CWE-79")
        error_str = str(error)
        assert "测试" in error_str

    def test_special_characters(self):
        """Test handling of special characters in paths and messages."""
        file_path = Path("path with spaces & symbols.yaml")
        error = CweError("Test", file_path=file_path)
        error_str = str(error)
        assert "path with spaces & symbols.yaml" in error_str
