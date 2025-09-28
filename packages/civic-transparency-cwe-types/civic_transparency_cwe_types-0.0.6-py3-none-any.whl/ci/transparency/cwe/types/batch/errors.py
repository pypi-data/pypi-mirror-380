"""Batch processing error types with batch-specific context.

Domain-specific error hierarchy for batch file processing operations. Extends
base loading errors to provide batch-specific context like file counts, batch
sizes, and processing statistics.

Design principles:
    - Inherits consistent formatting from BaseLoadingError
    - Adds batch-specific context (file counts, batch sizes, processing stats)
    - Provides specific exception types for different batch failure scenarios
    - Maintains minimal memory overhead with __slots__

Core batch errors:
    - BatchError: Base batch processing error
    - BatchAbortedError: Batch operation was aborted before completion
    - BatchValidationError: Batch validation failed
    - BatchResourceError: Batch ran out of system resources

Typical usage:
    from ci.transparency.cwe.types.batch import BatchAbortedError

    try:
        process_large_batch(files)
    except BatchAbortedError as e:
        # Rich context: "Batch aborted | Files: 1000/5000 | Reason: memory limit"
        logger.error(f"Batch processing failed: {e}")
"""

from pathlib import Path

from ci.transparency.cwe.types.base.errors import BaseLoadingError, BaseTransparencyError


class BatchError(BaseLoadingError):
    """Base exception for batch processing operations.

    Extends BaseLoadingError to add batch-specific context like file counts
    and processing statistics.
    """

    __slots__ = ("files_processed", "total_files", "batch_size")

    def __init__(
        self,
        message: str,
        file_path: Path | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
        batch_size: int | None = None,
    ):
        """Initialize batch processing error.

        Args:
            message: The error message
            file_path: Optional file path where the error occurred
            files_processed: Optional number of files processed before error
            total_files: Optional total number of files in the batch
            batch_size: Optional size of the processing batch
        """
        super().__init__(message, file_path)
        self.files_processed = files_processed
        self.total_files = total_files
        self.batch_size = batch_size

    def get_context_parts(self) -> list[str]:
        """Add batch processing context to error message."""
        parts = super().get_context_parts()

        if self.files_processed is not None and self.total_files is not None:
            parts.insert(0, f"Progress: {self.files_processed}/{self.total_files}")
        elif self.files_processed is not None:
            parts.insert(0, f"Processed: {self.files_processed}")

        if self.batch_size is not None:
            parts.append(f"Batch Size: {self.batch_size}")

        return parts


# ============================================================================
# Specific batch processing error types
# ============================================================================


class BatchAbortedError(BatchError):
    """Batch operation was aborted before completion.

    Used when a batch processing operation needs to be terminated early
    due to critical errors, resource constraints, or user intervention.
    """

    __slots__ = ("abort_reason",)

    def __init__(
        self,
        message: str,
        abort_reason: str | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
        file_path: Path | None = None,
    ):
        """Initialize batch aborted error.

        Args:
            message: The abort error message
            abort_reason: Optional reason why the batch was aborted
            files_processed: Optional number of files processed before abort
            total_files: Optional total number of files in the batch
            file_path: Optional file path where abort was triggered
        """
        super().__init__(message, file_path, files_processed, total_files)
        self.abort_reason = abort_reason

    def get_context_parts(self) -> list[str]:
        """Add abort reason to context parts."""
        parts = super().get_context_parts()
        if self.abort_reason:
            parts.append(f"Reason: {self.abort_reason}")
        return parts


class BatchValidationError(BatchError):
    """Batch validation failed.

    Used when batch-level validation (as opposed to individual file validation)
    fails due to inconsistencies, missing dependencies, or constraint violations.
    """

    __slots__ = ("validation_rule", "failed_files")

    def __init__(
        self,
        message: str,
        validation_rule: str | None = None,
        failed_files: list[Path] | None = None,
        file_path: Path | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch validation error.

        Args:
            message: The validation error message
            validation_rule: Optional name of the validation rule that failed
            failed_files: Optional list of files that failed validation
            file_path: Optional specific file path where validation failed
            files_processed: Optional number of files processed before validation failure
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, file_path, files_processed, total_files)
        self.validation_rule = validation_rule
        self.failed_files = failed_files or []

    def get_context_parts(self) -> list[str]:
        """Add validation context to error message."""
        parts = super().get_context_parts()

        if self.validation_rule:
            parts.append(f"Rule: {self.validation_rule}")

        if self.failed_files:
            failed_count = len(self.failed_files)
            parts.append(f"Failed Files: {failed_count}")

        return parts


class BatchResourceError(BatchError):
    """Batch operation ran out of system resources.

    Used when batch processing fails due to memory limits, disk space,
    file handle limits, or other system resource constraints.
    """

    __slots__ = ("resource_type", "limit_reached", "resource_usage")

    def __init__(
        self,
        message: str,
        resource_type: str | None = None,
        limit_reached: str | None = None,
        resource_usage: str | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch resource error.

        Args:
            message: The resource error message
            resource_type: Optional type of resource (e.g., "memory", "disk", "file_handles")
            limit_reached: Optional description of the limit that was reached
            resource_usage: Optional description of current resource usage
            files_processed: Optional number of files processed before resource exhaustion
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, None, files_processed, total_files)
        self.resource_type = resource_type
        self.limit_reached = limit_reached
        self.resource_usage = resource_usage

    def get_context_parts(self) -> list[str]:
        """Add resource context to error message."""
        parts = super().get_context_parts()

        if self.resource_type:
            parts.append(f"Resource: {self.resource_type}")

        if self.limit_reached:
            parts.append(f"Limit: {self.limit_reached}")

        if self.resource_usage:
            parts.append(f"Usage: {self.resource_usage}")

        return parts


class BatchTimeoutError(BatchError):
    """Batch operation timed out.

    Used when batch processing takes longer than the configured timeout
    and needs to be terminated.
    """

    __slots__ = ("timeout_seconds", "elapsed_seconds")

    def __init__(
        self,
        message: str,
        timeout_seconds: float | None = None,
        elapsed_seconds: float | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch timeout error.

        Args:
            message: The timeout error message
            timeout_seconds: Optional timeout limit that was exceeded
            elapsed_seconds: Optional actual time elapsed before timeout
            files_processed: Optional number of files processed before timeout
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, None, files_processed, total_files)
        self.timeout_seconds = timeout_seconds
        self.elapsed_seconds = elapsed_seconds

    def get_context_parts(self) -> list[str]:
        """Add timeout context to error message."""
        parts = super().get_context_parts()

        if self.timeout_seconds:
            parts.append(f"Timeout: {self.timeout_seconds}s")

        if self.elapsed_seconds:
            parts.append(f"Elapsed: {self.elapsed_seconds:.1f}s")

        return parts


class BatchIntegrityError(BatchError):
    """Batch data integrity compromised.

    Used when batch processing detects data corruption, inconsistencies,
    or integrity violations across the batch.
    """

    __slots__ = ("integrity_check", "affected_files")

    def __init__(
        self,
        message: str,
        integrity_check: str | None = None,
        affected_files: list[Path] | None = None,
        file_path: Path | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch integrity error.

        Args:
            message: The integrity error message
            integrity_check: Optional name of the integrity check that failed
            affected_files: Optional list of files with integrity issues
            file_path: Optional specific file path where integrity issue was detected
            files_processed: Optional number of files processed before integrity failure
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, file_path, files_processed, total_files)
        self.integrity_check = integrity_check
        self.affected_files = affected_files or []

    def get_context_parts(self) -> list[str]:
        """Add integrity context to error message."""
        parts = super().get_context_parts()

        if self.integrity_check:
            parts.append(f"Check: {self.integrity_check}")

        if self.affected_files:
            affected_count = len(self.affected_files)
            parts.append(f"Affected Files: {affected_count}")

        return parts


class BatchConfigurationError(BaseTransparencyError):
    """Batch configuration is invalid or incomplete.

    Used when batch processing configuration parameters are invalid,
    missing, or incompatible.
    """

    __slots__ = ("config_parameter", "config_value", "valid_values")

    def __init__(
        self,
        message: str,
        config_parameter: str | None = None,
        config_value: str | None = None,
        valid_values: list[str] | None = None,
    ):
        """Initialize batch configuration error.

        Args:
            message: The configuration error message
            config_parameter: Optional name of the invalid configuration parameter
            config_value: Optional value that was provided
            valid_values: Optional list of valid values for the parameter
        """
        super().__init__(message)
        self.config_parameter = config_parameter
        self.config_value = config_value
        self.valid_values = valid_values or []

    def get_context_parts(self) -> list[str]:
        """Add configuration context to error message."""
        parts = super().get_context_parts()

        if self.config_parameter:
            parts.append(f"Parameter: {self.config_parameter}")

        if self.config_value:
            parts.append(f"Value: {self.config_value}")

        if self.valid_values:
            valid_str = ", ".join(self.valid_values)
            parts.append(f"Valid: {valid_str}")

        return parts


class BatchFileNotFoundError(BatchError):
    """Required batch file could not be found.

    Used when specific files required for batch processing are missing.
    Different from individual file not found errors because it affects
    the entire batch operation.
    """

    __slots__ = ("missing_files",)

    def __init__(
        self,
        message: str,
        missing_files: list[Path] | None = None,
        file_path: Path | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch file not found error.

        Args:
            message: The file not found error message
            missing_files: Optional list of missing files
            file_path: Optional specific file path that was not found
            files_processed: Optional number of files processed before missing file detected
            total_files: Optional total number of files expected in the batch
        """
        super().__init__(message, file_path, files_processed, total_files)
        self.missing_files = missing_files or []

    def get_context_parts(self) -> list[str]:
        """Add missing files context to error message."""
        parts = super().get_context_parts()

        if self.missing_files:
            missing_count = len(self.missing_files)
            parts.append(f"Missing Files: {missing_count}")

        return parts


class BatchParsingError(BatchError):
    """Batch file parsing failed.

    Used when parsing errors affect the batch operation as a whole,
    such as when too many individual files fail to parse.
    """

    __slots__ = ("parser_type", "failed_files", "error_threshold")

    def __init__(
        self,
        message: str,
        parser_type: str | None = None,
        failed_files: list[Path] | None = None,
        error_threshold: int | None = None,
        file_path: Path | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch parsing error.

        Args:
            message: The parsing error message
            parser_type: Optional type of parser used (e.g., "YAML", "JSON")
            failed_files: Optional list of files that failed to parse
            error_threshold: Optional threshold that was exceeded
            file_path: Optional specific file path where parsing failed
            files_processed: Optional number of files processed before parsing failure
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, file_path, files_processed, total_files)
        self.parser_type = parser_type
        self.failed_files = failed_files or []
        self.error_threshold = error_threshold

    def get_context_parts(self) -> list[str]:
        """Add parsing context to error message."""
        parts = super().get_context_parts()

        if self.parser_type:
            parts.append(f"Parser: {self.parser_type}")

        if self.failed_files:
            failed_count = len(self.failed_files)
            parts.append(f"Parse Failures: {failed_count}")

        if self.error_threshold:
            parts.append(f"Threshold: {self.error_threshold}")

        return parts


class BatchDependencyError(BatchError):
    """Batch dependency resolution failed.

    Used when batch processing fails due to missing dependencies
    between files or external systems.
    """

    __slots__ = ("dependency_type", "missing_dependencies", "circular_dependencies")

    def __init__(
        self,
        message: str,
        dependency_type: str | None = None,
        missing_dependencies: list[str] | None = None,
        circular_dependencies: list[str] | None = None,
        files_processed: int | None = None,
        total_files: int | None = None,
    ):
        """Initialize batch dependency error.

        Args:
            message: The dependency error message
            dependency_type: Optional type of dependency (e.g., "file", "service", "schema")
            missing_dependencies: Optional list of missing dependencies
            circular_dependencies: Optional list of circular dependencies detected
            files_processed: Optional number of files processed before dependency failure
            total_files: Optional total number of files in the batch
        """
        super().__init__(message, None, files_processed, total_files)
        self.dependency_type = dependency_type
        self.missing_dependencies = missing_dependencies or []
        self.circular_dependencies = circular_dependencies or []

    def get_context_parts(self) -> list[str]:
        """Add dependency context to error message."""
        parts = super().get_context_parts()

        if self.dependency_type:
            parts.append(f"Dependency Type: {self.dependency_type}")

        if self.missing_dependencies:
            missing_count = len(self.missing_dependencies)
            parts.append(f"Missing: {missing_count}")

        if self.circular_dependencies:
            circular_count = len(self.circular_dependencies)
            parts.append(f"Circular: {circular_count}")

        return parts
