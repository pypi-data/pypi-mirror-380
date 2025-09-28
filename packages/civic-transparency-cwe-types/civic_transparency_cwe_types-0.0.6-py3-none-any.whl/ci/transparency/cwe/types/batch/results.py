"""Batch loading result types and operations.

Immutable, slotted dataclass for tracking batch file loading with items,
processed files, and file type statistics. Built on BaseLoadingResult for
count tracking and error handling.

Core type:
    - BatchResult: Tracks batch loading with items, file statistics, and processing details

Key operations:
    - store_item: Add successfully loaded item to batch result
    - skip_file: Skip a file with warning and tracking
    - record_file_error: Record file processing error
    - track_file_type: Track file extension statistics

Design principles:
    - Immutable: uses dataclasses.replace for all modifications
    - Generic: works with any file loading operation that produces key-value items
    - Type-aware: tracks file types and processing statistics
    - Conversion-ready: easily converts to domain-specific result types
"""

from collections.abc import Callable
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base import BaseLoadingResult


def _new_items() -> dict[str, dict[str, Any]]:
    """Typed default factory for items dictionary."""
    return {}


def _new_file_types() -> dict[str, int]:
    """Typed default factory for file type counts."""
    return {}


@dataclass(frozen=True, slots=True)
class BatchResult(BaseLoadingResult):
    """Result from generic batch file loading operations.

    Tracks loaded items, processed files, and file type statistics.
    Serves as the foundation for domain-specific loading operations.
    Extends BaseLoadingResult to provide loaded/failed counts and conversion protocol.
    """

    items: dict[str, dict[str, Any]] = field(default_factory=_new_items)
    processed_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()
    file_types: dict[str, int] = field(default_factory=_new_file_types)

    # ---- Derived metrics for batch operations ----

    @property
    def item_count(self) -> int:
        """Number of key-value items successfully loaded."""
        return len(self.items)

    @property
    def total_files_processed(self) -> int:
        """Total number of files encountered (processed + skipped)."""
        return len(self.processed_files) + len(self.skipped_files)

    @property
    def has_items(self) -> bool:
        """True if any items were successfully loaded."""
        return bool(self.items)

    @property
    def file_type_count(self) -> int:
        """Number of distinct file types encountered."""
        return len(self.file_types)

    @property
    def processed_file_count(self) -> int:
        """Number of files successfully processed."""
        return len(self.processed_files)

    @property
    def skipped_file_count(self) -> int:
        """Number of files that were skipped."""
        return len(self.skipped_files)

    @property
    def items_stored(self) -> int:
        """Return the number of items stored."""
        return len(self.items)

    # ---- File type analysis ----

    def get_files_by_type(self, file_type: str) -> int:
        """Get count of files processed for a specific type.

        Args:
            file_type: File extension (e.g., "yaml", "json")

        Returns:
            Number of files of that type processed
        """
        return self.file_types.get(file_type, 0)

    def get_most_common_file_type(self) -> str | None:
        """Get the most commonly processed file type.

        Returns:
            Most common file extension, or None if no files processed
        """
        if not self.file_types:
            return None
        return max(self.file_types, key=lambda k: self.file_types[k])

    def get_file_type_distribution(self) -> dict[str, float]:
        """Get percentage distribution of file types.

        Returns:
            Dictionary mapping file type to percentage (0.0 to 100.0)
        """
        if not self.file_types:
            return {}

        total = sum(self.file_types.values())
        return {file_type: (count / total) * 100.0 for file_type, count in self.file_types.items()}

    # ---- File path utilities ----

    def was_file_processed(self, file_path: Path) -> bool:
        """Check if a specific file was successfully processed.

        Args:
            file_path: Path to check

        Returns:
            True if the file was processed successfully
        """
        return file_path in self.processed_files

    def was_file_skipped(self, file_path: Path) -> bool:
        """Check if a specific file was skipped.

        Args:
            file_path: Path to check

        Returns:
            True if the file was skipped
        """
        return file_path in self.skipped_files

    def get_item_for_file(self, file_path: Path) -> dict[str, Any] | None:
        """Get the item that was loaded from a specific file.

        Args:
            file_path: Path to the source file

        Returns:
            The item data, or None if file wasn't processed or no item found
        """
        if not self.was_file_processed(file_path):
            return None

        # Linear search through items - could be optimized with reverse index
        for item_data in self.items.values():
            # Check if item has metadata pointing to this file
            metadata = item_data.get("_metadata", {})
            source_file = metadata.get("source_file")
            if source_file and Path(source_file) == file_path:
                return item_data

        return None

    # ---- Generic item access methods ----

    def get_item_by_key(self, key: str) -> dict[str, Any] | None:
        """Get a specific item by its key.

        Args:
            key: The key to look up

        Returns:
            The item data, or None if key not found
        """
        return self.items.get(key)

    def has_item_key(self, key: str) -> bool:
        """Check if a specific key exists in items.

        Args:
            key: The key to check

        Returns:
            True if key exists
        """
        return key in self.items

    def get_item_keys(self) -> list[str]:
        """Get all item keys.

        Returns:
            List of all keys in items dictionary
        """
        return list(self.items.keys())

    def get_item_values(self) -> list[dict[str, Any]]:
        """Get all item values.

        Returns:
            List of all values in items dictionary
        """
        return list(self.items.values())

    def get_items(self) -> dict[str, dict[str, Any]]:
        """Get a copy of all items.

        Returns:
            Copy of the items dictionary
        """
        return self.items.copy()


# ============================================================================
# Batch operations
# ============================================================================


def store_item(
    result: BatchResult, key: str, value: Any, *, file_path: Path | None = None
) -> BatchResult:
    """Store an item in the batch result.

    Args:
        result: The batch result to update
        key: Key to store the item under
        value: Value to store
        file_path: Optional file path to track

    Returns:
        New result with item stored
    """
    new_items = {**result.items, key: value}
    result = replace(
        result,
        items=new_items,
        loaded=result.loaded + 1,
    )

    # Track file and file type if provided
    if file_path:
        result = mark_processed(result, file_path)
        # Extract and track file extension
        suffix = file_path.suffix.lower().lstrip(".") or "noext"
        result = track_file_type(result, suffix)

    return result


def skip_file(result: BatchResult, file_path: Path, reason: str) -> BatchResult:
    """Record a skipped file with reason.

    Args:
        result: The batch result to update
        file_path: Path to the skipped file
        reason: Reason the file was skipped

    Returns:
        New result with skipped file recorded
    """
    from ci.transparency.cwe.types.base import add_warning

    warning_message = f"Skipped {file_path.name}: {reason}"
    result = add_warning(result, warning_message)

    new_skipped = result.skipped_files + (file_path,)
    return replace(
        result,
        skipped_files=new_skipped,
        failed=result.failed + 1,
    )


def record_file_error(result: BatchResult, file_path: Path, error: Exception) -> BatchResult:
    """Record a file processing error.

    Args:
        result: The batch result to update
        file_path: Path to the file that had an error
        error: The exception that occurred

    Returns:
        New result with error recorded
    """
    from ci.transparency.cwe.types.base import add_error

    error_message = f"Error processing {file_path.name}: {error}"
    result = add_error(result, error_message)

    return replace(
        result,
        failed=result.failed + 1,
    )


def track_file_type[R: BatchResult](result: R, file_type: str) -> R:
    """Increment the count for a specific file type.

    Args:
        result: The batch result to update
        file_type: File extension (e.g., "yaml", "json", "txt")

    Returns:
        New result with file type count incremented
    """
    current_count = result.file_types.get(file_type, 0)
    new_types = {**result.file_types, file_type: current_count + 1}

    return replace(result, file_types=new_types)


def mark_processed[R: BatchResult](result: R, file_path: Path) -> R:
    """Mark a file as processed (successful or skipped).

    Args:
        result: The batch result to update
        file_path: Path to the processed file

    Returns:
        New result with file added to processed list
    """
    return replace(result, processed_files=result.processed_files + (file_path,))


def update_file_type_stats[R: BatchResult](result: R, file_type: str, count: int) -> R:
    """Set the count for a specific file type (replaces existing count).

    Args:
        result: The batch result to update
        file_type: File extension to update
        count: New count for this file type

    Returns:
        New result with file type count set to the specified value
    """
    new_types = {**result.file_types, file_type: count}
    return replace(result, file_types=new_types)


def clear_items[R: BatchResult](result: R) -> R:
    """Remove all items from the batch result.

    Useful for creating a fresh result while preserving file statistics.

    Args:
        result: The batch result to clear

    Returns:
        New result with empty items dictionary
    """
    return replace(result, items={})


def filter_items[R: BatchResult](result: R, predicate: Callable[[str, dict[str, Any]], bool]) -> R:
    """Filter items based on a predicate function.

    Args:
        result: The batch result to filter
        predicate: Function that takes (key, data) and returns True to keep the item

    Returns:
        New result with filtered items
    """
    filtered_items = {key: data for key, data in result.items.items() if predicate(key, data)}

    # Adjust loaded count to match filtered items
    new_loaded = len(filtered_items)
    removed_count = result.item_count - new_loaded

    return replace(
        result,
        items=filtered_items,
        loaded=new_loaded,
        failed=result.failed + removed_count,
    )


# ============================================================================
# Batch analysis and reporting
# ============================================================================


def get_batch_summary(result: BatchResult) -> dict[str, Any]:
    """Generate batch processing summary.

    Args:
        result: The batch result to summarize

    Returns:
        Dictionary with detailed batch statistics
    """
    performance = analyze_batch_performance(result)

    return {
        # Core metrics (matching test expectations)
        "items_stored": result.items_stored,
        "files_processed": len(result.processed_files),
        "successful_loads": result.loaded,
        "failed_loads": result.failed,
        "files_skipped": len(result.skipped_files),
        # Success metrics
        "success_rate_percent": round(result.success_rate * 100, 2),
        "efficiency_score": performance["efficiency_score"],
        # File type analysis
        "file_type_breakdown": dict(result.file_types),
        "file_type_count": len(result.file_types),
        # Message counts
        "error_count": result.error_count,
        "warning_count": result.warning_count,
        "info_count": result.info_count,
        # Status flags
        "has_errors": result.has_errors,
        "has_warnings": result.has_warnings,
        "has_infos": result.has_infos,
        # Performance metrics
        "items_per_file": performance["items_per_file"],
        "average_items_per_type": performance["average_items_per_type"],
        # Lists for detailed analysis
        "processed_files": [str(p) for p in result.processed_files],
        "skipped_files": [str(p) for p in result.skipped_files],
    }


def analyze_batch_performance(result: BatchResult) -> dict[str, Any]:
    """Analyze batch processing performance metrics.

    Args:
        result: The batch result to analyze

    Returns:
        Dictionary with performance analysis
    """
    total_operations = result.loaded + result.failed

    # Calculate efficiency score (0.0 to 1.0)
    efficiency_score = 1.0 if total_operations == 0 else result.loaded / total_operations

    # Calculate error rate (0.0 to 1.0)
    error_rate = 0.0 if total_operations == 0 else result.failed / total_operations

    # Calculate processing rates
    items_per_file = (
        result.items_stored / len(result.processed_files) if result.processed_files else 0
    )

    # Find dominant file type
    dominant_file_type = "none"
    if result.file_types:
        dominant_file_type = max(result.file_types.keys(), key=lambda k: result.file_types[k])

    return {
        "efficiency_score": round(efficiency_score, 3),
        "error_rate": round(error_rate, 3),
        "items_per_file": round(items_per_file, 2),
        "total_operations": total_operations,
        "success_rate": round(result.success_rate, 3),
        "file_types_processed": len(result.file_types),
        "file_type_diversity": len(result.file_types),
        "dominant_file_type": dominant_file_type,
        "average_items_per_type": (
            round(result.items_stored / len(result.file_types), 2) if result.file_types else 0
        ),
        "skipped_file_rate": (
            round(len(result.skipped_files) / len(result.processed_files), 3)
            if result.processed_files
            else 0
        ),
    }


# ============================================================================
# Convenience functions for common patterns
# ============================================================================


def process_file_result(
    result: BatchResult, file_path: Path, file_result: tuple[str, Any] | None, context: str
) -> BatchResult:
    """Process a file processing result (success or error).

    Args:
        result: The batch result to update
        file_path: Path to the file that was processed
        file_result: Either a (key, value) tuple for success or None for error
        context: Context string (error message if file_result is None)

    Returns:
        New result with file result processed
    """
    if file_result is None:
        # Error case - context contains the error message
        error = Exception(context)
        return record_file_error(result, file_path, error)

    # Success case - file_result is (key, value) tuple
    key, value = file_result
    return store_item(result, key, value, file_path=file_path)


def initialize_batch_with_file_types(file_paths: list[Path]) -> BatchResult:
    """Initialize a batch result with file type counts from a file list.

    Args:
        file_paths: List of files that will be processed

    Returns:
        New BatchResult with file type statistics pre-populated
    """
    result = BatchResult()

    for file_path in file_paths:
        # Extract file extension, handle files without extensions
        suffix = file_path.suffix.lower().lstrip(".") or "noext"
        result = track_file_type(result, suffix)

    return result


def merge_batch_results[R: BatchResult](primary: R, *others: R) -> R:
    """Merge multiple batch results into one.

    Args:
        primary: The primary result (type is preserved)
        *others: Additional batch results to merge

    Returns:
        New result of primary's type with all data merged
    """
    result = primary

    for other in others:
        # Merge base loading result data
        from ci.transparency.cwe.types.base import merge_loading

        result = merge_loading(result, other)

        # Merge batch-specific data
        new_items = {**result.items, **other.items}
        new_processed = result.processed_files + other.processed_files
        new_skipped = result.skipped_files + other.skipped_files

        # Merge file type counts
        new_file_types = result.file_types.copy()
        for file_type, count in other.file_types.items():
            new_file_types[file_type] = new_file_types.get(file_type, 0) + count

        result = replace(
            result,
            items=new_items,
            processed_files=new_processed,
            skipped_files=new_skipped,
            file_types=new_file_types,
        )

    return result


# ============================================================================
# Item access convenience functions
# ============================================================================


def get_item_count(result: BatchResult) -> int:
    """Get the number of items stored."""
    return result.item_count


def has_any_items(result: BatchResult) -> bool:
    """Check if result has any items."""
    return result.has_items


def get_all_item_keys(result: BatchResult) -> list[str]:
    """Get all item keys as a list."""
    return result.get_item_keys()


def find_items_by_pattern(result: BatchResult, key_pattern: str) -> dict[str, dict[str, Any]]:
    """Find items whose keys match a pattern.

    Args:
        result: BatchResult to search
        key_pattern: Pattern to match (simple string contains)

    Returns:
        Dictionary of matching items
    """
    return {key: data for key, data in result.items.items() if key_pattern in key}


def get_items_with_field(result: BatchResult, field_name: str) -> dict[str, dict[str, Any]]:
    """Get items that contain a specific field.

    Args:
        result: BatchResult to search
        field_name: Field name to look for

    Returns:
        Dictionary of items that contain the field
    """
    return {key: data for key, data in result.items.items() if field_name in data}
