"""Batch file processing operations.

Toolkit for batch loading operations across multiple files.
Provides generic file processing that works with any domain-specific
loader function and tracks statistics.

Core types:
    - BatchResult: Tracks batch loading with mappings, file statistics, and processing details

Error types:
    - BatchError: Base error for batch processing failures
    - BatchAbortedError: Batch operation was aborted before completion
    - BatchResourceError: Batch ran out of system resources (memory, disk, etc.)
    - BatchTimeoutError: Batch operation timed out
    - BatchValidationError: Batch-level validation failed
    - BatchIntegrityError: Data consistency compromised
    - BatchConfigurationError: Batch configuration is invalid
    - BatchFileNotFoundError: Required batch files could not be found
    - BatchParsingError: Batch file parsing failed
    - BatchDependencyError: Batch dependency resolution failed

Key operations:
    - store_item: Add successfully loaded item to batch result
    - skip_file: Skip a file with warning and tracking
    - record_file_error: Record file processing error
    - track_file_type: Track file extension statistics

Example usage:
    from ci.transparency.cwe.types.batch import (
        BatchResult, store_item, skip_file, BatchResourceError
    )

    result = BatchResult()

    try:
        result = store_item(result, "key1", data, file_path=Path("file.yaml"))
        result = skip_file(result, Path("bad.txt"), "unsupported format")
    except BatchResourceError as e:
        logger.error(f"Batch failed: {e}")  # Rich context with progress info

    # Convert to domain-specific result
    cwe_result = CweLoadingResult.from_result(result, cwes=result.mappings)
"""

from .errors import (
    # Common batch errors
    BatchAbortedError,
    BatchConfigurationError,
    BatchDependencyError,
    # Base batch error
    BatchError,
    BatchFileNotFoundError,
    BatchIntegrityError,
    BatchParsingError,
    # Advanced batch errors for error handling
    BatchResourceError,
    BatchTimeoutError,
    BatchValidationError,
)
from .results import (
    # Result types
    BatchResult,
    analyze_batch_performance,
    clear_items,
    filter_items,
    # Batch analysis
    get_batch_summary,
    initialize_batch_with_file_types,
    mark_processed,
    merge_batch_results,
    # Convenience functions
    process_file_result,
    record_file_error,
    skip_file,
    # Core batch operations
    store_item,
    track_file_type,
    update_file_type_stats,
)

__all__ = [
    # Result types
    "BatchResult",
    # Core operations
    "store_item",
    "skip_file",
    "record_file_error",
    "track_file_type",
    "mark_processed",
    "update_file_type_stats",
    "clear_items",
    "filter_items",
    # Analysis and reporting
    "get_batch_summary",
    "analyze_batch_performance",
    # Convenience functions
    "process_file_result",
    "initialize_batch_with_file_types",
    "merge_batch_results",
    # Base batch error
    "BatchError",
    # Common batch errors
    "BatchAbortedError",
    "BatchFileNotFoundError",
    "BatchParsingError",
    "BatchValidationError",
    # Advanced batch errors
    "BatchResourceError",
    "BatchTimeoutError",
    "BatchIntegrityError",
    "BatchConfigurationError",
    "BatchDependencyError",
]
