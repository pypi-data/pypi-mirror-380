"""Tests for batch error types and error handling.

Tests the batch error hierarchy including context formatting,
error construction, and inheritance behavior.
"""

from pathlib import Path

from ci.transparency.cwe.types.batch.errors import (
    BatchError,
    BatchAbortedError,
    BatchValidationError,
    BatchResourceError,
    BatchTimeoutError,
    BatchIntegrityError,
    BatchConfigurationError,
    BatchFileNotFoundError,
    BatchParsingError,
    BatchDependencyError,
)


class TestBatchError:
    """Test base BatchError class."""

    def test_basic_batch_error(self):
        """Test basic BatchError construction."""
        error = BatchError("Processing failed")

        assert str(error) == "Processing failed"
        assert error.message == "Processing failed"
        assert error.file_path is None
        assert error.files_processed is None
        assert error.total_files is None

    def test_batch_error_with_file_path(self):
        """Test BatchError with file path context."""
        file_path = Path("test.yaml")
        error = BatchError("Processing failed", file_path=file_path)

        assert str(error) == f"Processing failed | File: {file_path}"
        assert error.file_path == file_path

    def test_batch_error_with_progress_info(self):
        """Test BatchError with processing progress."""
        error = BatchError(
            "Processing failed",
            files_processed=15,
            total_files=100
        )

        assert str(error) == "Processing failed | Progress: 15/100"
        assert error.files_processed == 15
        assert error.total_files == 100

    def test_batch_error_with_all_context(self):
        """Test BatchError with all context information."""
        file_path = Path("error.yaml")
        error = BatchError(
            "Processing failed",
            file_path=file_path,
            files_processed=50,
            total_files=200,
            batch_size=10
        )

        expected = f"Processing failed | Progress: 50/200 | File: {file_path} | Batch Size: 10"
        assert str(error) == expected

    def test_batch_error_inheritance(self):
        """Test BatchError inherits from BaseLoadingError."""
        from ci.transparency.cwe.types.base.errors import BaseLoadingError

        error = BatchError("test")
        assert isinstance(error, BaseLoadingError)

    def test_batch_error_context_parts_ordering(self):
        """Test context parts are ordered correctly."""
        error = BatchError(
            "Error",
            file_path=Path("test.yaml"),
            files_processed=10,
            batch_size=5
        )

        context_parts = error.get_context_parts()
        assert context_parts[0] == "Processed: 10"  # Progress info comes first
        assert context_parts[1] == f"File: {Path('test.yaml')}"
        assert context_parts[2] == "Batch Size: 5"


class TestBatchAbortedError:
    """Test BatchAbortedError specific functionality."""

    def test_batch_aborted_basic(self):
        """Test basic BatchAbortedError."""
        error = BatchAbortedError("Batch aborted due to critical error")

        assert "Batch aborted due to critical error" in str(error)
        assert error.abort_reason is None

    def test_batch_aborted_with_reason(self):
        """Test BatchAbortedError with abort reason."""
        error = BatchAbortedError(
            "Operation aborted",
            abort_reason="Memory limit exceeded",
            files_processed=75,
            total_files=150
        )

        error_str = str(error)
        assert "Operation aborted" in error_str
        assert "Progress: 75/150" in error_str
        assert "Reason: Memory limit exceeded" in error_str

    def test_batch_aborted_progress_format(self):
        """Test progress formatting in abort context."""
        error = BatchAbortedError(
            "Aborted",
            files_processed=25,
            total_files=100
        )

        # Should show progress format instead of simple "Processed: X"
        assert "Progress: 25/100" in str(error)
        assert "Processed: 25" not in str(error)


class TestBatchValidationError:
    """Test BatchValidationError functionality."""

    def test_batch_validation_basic(self):
        """Test basic BatchValidationError."""
        error = BatchValidationError("Validation failed")

        assert "Validation failed" in str(error)
        assert error.validation_rule is None
        assert error.failed_files == []

    def test_batch_validation_with_rule(self):
        """Test BatchValidationError with validation rule."""
        failed_files = [Path("bad1.yaml"), Path("bad2.yaml")]
        error = BatchValidationError(
            "Schema validation failed",
            validation_rule="required_fields",
            failed_files=failed_files
        )

        error_str = str(error)
        assert "Schema validation failed" in error_str
        assert "Rule: required_fields" in error_str
        assert "Failed Files: 2" in error_str

    def test_batch_validation_empty_failed_files(self):
        """Test BatchValidationError with empty failed files list."""
        error = BatchValidationError("Validation error", failed_files=[])

        # Should not include failed files count if empty
        assert "Failed Files: 0" not in str(error)


class TestBatchResourceError:
    """Test BatchResourceError functionality."""

    def test_batch_resource_basic(self):
        """Test basic BatchResourceError."""
        error = BatchResourceError("Out of memory")

        assert "Out of memory" in str(error)
        assert error.resource_type is None

    def test_batch_resource_with_details(self):
        """Test BatchResourceError with resource details."""
        error = BatchResourceError(
            "Resource exhausted",
            resource_type="memory",
            limit_reached="8GB",
            resource_usage="7.9GB used",
            files_processed=450
        )

        error_str = str(error)
        assert "Resource exhausted" in error_str
        assert "Resource: memory" in error_str
        assert "Limit: 8GB" in error_str
        assert "Usage: 7.9GB used" in error_str
        assert "Processed: 450" in error_str

    def test_batch_resource_different_types(self):
        """Test different resource types."""
        disk_error = BatchResourceError(
            "Disk full",
            resource_type="disk",
            limit_reached="/tmp full"
        )

        memory_error = BatchResourceError(
            "Memory exhausted",
            resource_type="memory"
        )

        assert "Resource: disk" in str(disk_error)
        assert "Resource: memory" in str(memory_error)


class TestBatchTimeoutError:
    """Test BatchTimeoutError functionality."""

    def test_batch_timeout_basic(self):
        """Test basic BatchTimeoutError."""
        error = BatchTimeoutError("Operation timed out")

        assert "Operation timed out" in str(error)
        assert error.timeout_seconds is None

    def test_batch_timeout_with_timing(self):
        """Test BatchTimeoutError with timing information."""
        error = BatchTimeoutError(
            "Batch processing timed out",
            timeout_seconds=300.0,
            elapsed_seconds=305.5,
            files_processed=89,
            total_files=100
        )

        error_str = str(error)
        assert "Batch processing timed out" in error_str
        assert "Progress: 89/100" in error_str
        assert "Timeout: 300.0s" in error_str
        assert "Elapsed: 305.5s" in error_str

    def test_batch_timeout_partial_timing(self):
        """Test BatchTimeoutError with only timeout specified."""
        error = BatchTimeoutError(
            "Timeout",
            timeout_seconds=120.0
        )

        error_str = str(error)
        assert "Timeout: 120.0s" in error_str
        assert "Elapsed:" not in error_str  # Should not appear if not provided


class TestBatchIntegrityError:
    """Test BatchIntegrityError functionality."""

    def test_batch_integrity_basic(self):
        """Test basic BatchIntegrityError."""
        error = BatchIntegrityError("Data integrity compromised")

        assert "Data integrity compromised" in str(error)
        assert error.integrity_check is None

    def test_batch_integrity_with_check_details(self):
        """Test BatchIntegrityError with check details."""
        affected_files = [Path("corrupt1.yaml"), Path("corrupt2.yaml")]
        error = BatchIntegrityError(
            "Integrity check failed",
            integrity_check="checksum_validation",
            affected_files=affected_files,
            files_processed=200
        )

        error_str = str(error)
        assert "Integrity check failed" in error_str
        assert "Check: checksum_validation" in error_str
        assert "Affected Files: 2" in error_str
        assert "Processed: 200" in error_str


class TestBatchConfigurationError:
    """Test BatchConfigurationError functionality."""

    def test_batch_config_basic(self):
        """Test basic BatchConfigurationError."""
        error = BatchConfigurationError("Invalid configuration")

        assert "Invalid configuration" in str(error)
        assert error.config_parameter is None

    def test_batch_config_with_parameter_details(self):
        """Test BatchConfigurationError with parameter details."""
        error = BatchConfigurationError(
            "Invalid batch size",
            config_parameter="batch_size",
            config_value="-5",
            valid_values=["1", "10", "50", "100"]
        )

        error_str = str(error)
        assert "Invalid batch size" in error_str
        assert "Parameter: batch_size" in error_str
        assert "Value: -5" in error_str
        assert "Valid: 1, 10, 50, 100" in error_str

    def test_batch_config_inheritance(self):
        """Test BatchConfigurationError inherits correctly."""
        from ci.transparency.cwe.types.base.errors import BaseTransparencyError

        error = BatchConfigurationError("Config error")
        assert isinstance(error, BaseTransparencyError)
        # Should not inherit from BaseLoadingError since it's config-related


class TestBatchFileNotFoundError:
    """Test BatchFileNotFoundError functionality."""

    def test_file_not_found_basic(self):
        """Test basic BatchFileNotFoundError."""
        error = BatchFileNotFoundError("Required files missing")

        assert "Required files missing" in str(error)
        assert error.missing_files == []

    def test_file_not_found_with_files(self):
        """Test BatchFileNotFoundError with missing files list."""
        missing = [Path("required1.yaml"), Path("required2.yaml")]
        error = BatchFileNotFoundError(
            "Critical files not found",
            missing_files=missing,
            files_processed=50,
            total_files=100
        )

        error_str = str(error)
        assert "Critical files not found" in error_str
        assert "Missing Files: 2" in error_str
        assert "Progress: 50/100" in error_str


class TestBatchParsingError:
    """Test BatchParsingError functionality."""

    def test_parsing_error_basic(self):
        """Test basic BatchParsingError."""
        error = BatchParsingError("Parsing failed")

        assert "Parsing failed" in str(error)
        assert error.parser_type is None

    def test_parsing_error_with_details(self):
        """Test BatchParsingError with parsing details."""
        failed_files = [Path("bad1.yaml"), Path("bad2.json")]
        error = BatchParsingError(
            "Multiple parsing failures",
            parser_type="YAML",
            failed_files=failed_files,
            error_threshold=5,
            files_processed=95
        )

        error_str = str(error)
        assert "Multiple parsing failures" in error_str
        assert "Parser: YAML" in error_str
        assert "Parse Failures: 2" in error_str
        assert "Threshold: 5" in error_str
        assert "Processed: 95" in error_str


class TestBatchDependencyError:
    """Test BatchDependencyError functionality."""

    def test_dependency_error_basic(self):
        """Test basic BatchDependencyError."""
        error = BatchDependencyError("Dependency resolution failed")

        assert "Dependency resolution failed" in str(error)
        assert error.dependency_type is None

    def test_dependency_error_with_details(self):
        """Test BatchDependencyError with dependency details."""
        missing_deps = ["schema.json", "config.yaml"]
        circular_deps = ["file_a -> file_b -> file_a"]

        error = BatchDependencyError(
            "Dependency issues found",
            dependency_type="file",
            missing_dependencies=missing_deps,
            circular_dependencies=circular_deps,
            files_processed=75,
            total_files=100
        )

        error_str = str(error)
        assert "Dependency issues found" in error_str
        assert "Dependency Type: file" in error_str
        assert "Missing: 2" in error_str
        assert "Circular: 1" in error_str
        assert "Progress: 75/100" in error_str


class TestErrorContextFormatting:
    """Test error context formatting across different error types."""

    def test_context_parts_empty_values_omitted(self):
        """Test that empty/None context values are omitted."""
        error = BatchError(
            "Test error",
            file_path=None,
            files_processed=None,
            total_files=100,  # This alone doesn't generate context parts
            batch_size=None
        )

        context_parts = error.get_context_parts()
        # Should only contain non-None/non-empty values
        # Since total_files alone (without files_processed) doesn't generate context,
        # the context_parts should be empty
        assert len(context_parts) == 0

        # Test that meaningful combinations DO create context parts
        error_with_progress = BatchError(
            "Test error",
            files_processed=50,
            total_files=100
        )
        context_parts_with_progress = error_with_progress.get_context_parts()
        assert len(context_parts_with_progress) > 0
        assert any("50/100" in part for part in context_parts_with_progress)

    def test_error_message_consistency(self):
        """Test that error message format is consistent."""
        errors = [
            BatchError("Base error"),
            BatchAbortedError("Aborted error"),
            BatchResourceError("Resource error"),
            BatchTimeoutError("Timeout error")
        ]

        for error in errors:
            error_str = str(error)
            # All should start with the message
            assert error_str.startswith(error.message)
            # Context should be separated by " | " if present
            if " | " in error_str:
                parts = error_str.split(" | ")
                assert parts[0] == error.message

    def test_slots_memory_efficiency(self):
        """Test that error classes use __slots__ for memory efficiency."""
        error = BatchError("test")

        # Check that __slots__ is defined
        assert hasattr(error, '__slots__')

        # Should have the expected slots
        assert 'files_processed' in error.__slots__
        assert 'total_files' in error.__slots__
        assert 'batch_size' in error.__slots__
