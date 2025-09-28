"""Tests for batch results and operations (strict, 3.12 built-in generics).

Covers:
- BatchResult dataclass & derived properties
- Core ops: store/skip/error/mark/track/update/clear/filter
- Analysis: get_batch_summary, analyze_batch_performance
- Utilities: process_file_result, initialize_batch_with_file_types, merge_batch_results
- Edge behavior: noext bucket, immutability, vacuous success
"""

from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.batch import (
    BatchResult,
    analyze_batch_performance,
    clear_items,
    filter_items,
    get_batch_summary,
    initialize_batch_with_file_types,
    mark_processed,
    merge_batch_results,
    process_file_result,
    record_file_error,
    skip_file,
    store_item,
    track_file_type,
    update_file_type_stats,
)


class TestBatchResult:
    """Test BatchResult dataclass and properties."""

    def test_empty_batch_result_initialization(self) -> None:
        """Test creating empty BatchResult."""
        result = BatchResult()

        assert result.items == {}
        assert result.file_types == {}
        assert result.processed_files == ()
        assert result.skipped_files == ()
        assert result.loaded == 0
        assert result.failed == 0
        assert not result.has_errors
        assert result.success_rate == 1.0
        assert result.item_count == 0
        assert result.items_stored == 0
        assert result.file_type_count == 0
        assert result.processed_file_count == 0
        assert result.skipped_file_count == 0
        assert result.total_files_processed == 0

    def test_batch_result_with_data(self) -> None:
        """Test BatchResult with initial data."""
        items: dict[str, dict[str, Any]] = {
            "key1": {"data": "value1"},
            "key2": {"data": "value2"},
        }
        processed: tuple[Path, ...] = (Path("file1.yaml"), Path("file2.yaml"))

        result = BatchResult(items=items, processed_files=processed, loaded=2, failed=1)

        assert len(result.items) == 2
        assert result.processed_file_count == 2
        assert result.loaded == 2
        assert result.failed == 1
        assert result.total_processed == 3
        assert result.success_rate == 2 / 3

    def test_has_items_property(self) -> None:
        """Test has_items property."""
        empty_result = BatchResult()
        assert not empty_result.has_items

        result_with_items = BatchResult(items={"key": {"value": "value"}})
        assert result_with_items.has_items

    def test_has_processed_files_property(self) -> None:
        """Test has_processed_files property."""
        empty_result = BatchResult()
        assert len(empty_result.processed_files) == 0

        result_with_files = BatchResult(processed_files=(Path("test.yaml"),))
        assert len(result_with_files.processed_files) > 0

    def test_get_file_types_list(self) -> None:
        """Test getting file types as sorted list."""
        result = BatchResult(file_types={"yaml": 5, "json": 3, "txt": 1})
        file_types = sorted(result.file_types.keys())
        assert file_types == ["json", "txt", "yaml"]

    def test_get_processed_paths(self) -> None:
        """Test getting processed file paths."""
        paths: list[Path] = [Path("dir/file1.yaml"), Path("dir/file2.json")]
        result = BatchResult(processed_files=tuple(paths))
        processed_paths = list(result.processed_files)
        assert len(processed_paths) == 2
        assert all(isinstance(p, Path) for p in processed_paths)


class TestBatchOperations:
    """Test batch processing operations."""

    def test_store_item_basic(self) -> None:
        """Test storing a basic item."""
        result = BatchResult()
        file_path = Path("test.yaml")
        data: dict[str, Any] = {"id": "test", "content": "data"}

        new_result = store_item(result, "test", data, file_path=file_path)

        assert "test" in new_result.items
        assert new_result.items["test"] == data
        assert file_path in new_result.processed_files
        assert new_result.loaded == 1
        assert new_result.file_types.get("yaml") == 1

    def test_store_item_without_file_path(self) -> None:
        """Test storing item without file path: no processed tracking."""
        result = BatchResult()
        new_result = store_item(result, "key", {"content": "test"})

        assert "key" in new_result.items
        assert new_result.loaded == 1
        assert len(new_result.processed_files) == 0  # no file tracked

    def test_store_item_duplicate_key(self) -> None:
        """Test storing item with duplicate key overwrites."""
        result = BatchResult(items={"key": {"old": "value"}})
        file_path = Path("test.yaml")

        new_result = store_item(result, "key", {"new": "value"}, file_path=file_path)

        assert new_result.items["key"] == {"new": "value"}
        assert new_result.loaded == 1

    def test_skip_file(self) -> None:
        """Test skipping a file."""
        result = BatchResult()
        file_path = Path("bad.txt")
        reason = "unsupported format"

        new_result = skip_file(result, file_path, reason)

        assert file_path in new_result.skipped_files
        # Implementation uses file_path.name in message
        assert any(f"Skipped {file_path.name}: {reason}" in w for w in new_result.warnings)
        assert new_result.failed == 1

    def test_record_file_error(self) -> None:
        """Test recording file error."""
        result = BatchResult()
        file_path = Path("error.yaml")
        error = Exception("Parse error")

        new_result = record_file_error(result, file_path, error)

        # Implementation uses file_path.name in message
        assert any(f"Error processing {file_path.name}: Parse error" in e for e in new_result.errors)
        assert new_result.failed == 1

    def test_track_file_type(self) -> None:
        """Test tracking file type."""
        result = BatchResult()

        r1 = track_file_type(result, "yaml")
        assert r1.file_types.get("yaml") == 1

        r2 = track_file_type(r1, "yaml")
        assert r2.file_types.get("yaml") == 2

        r3 = track_file_type(r2, "json")
        assert r3.file_types.get("json") == 1

    def test_mark_processed(self) -> None:
        """Test marking file as processed."""
        result = BatchResult()
        file_path = Path("processed.yaml")

        new_result = mark_processed(result, file_path)

        assert file_path in new_result.processed_files

    def test_update_file_type_stats(self) -> None:
        """Test updating file type statistics."""
        result = BatchResult()

        r1 = update_file_type_stats(result, "yaml", 5)
        r2 = update_file_type_stats(r1, "json", 3)

        assert r2.file_types == {"yaml": 5, "json": 3}

    def test_clear_items(self) -> None:
        """Test clearing items."""
        result = BatchResult(items={"key1": {"value": "value1"}, "key2": {"value": "value2"}})

        new_result = clear_items(result)

        assert new_result.items == {}
        # ensure original not modified (immutability)
        assert result.items != {}

    def test_filter_items(self) -> None:
        """Test filtering items."""
        items: dict[str, dict[str, Any]] = {
            "keep": {"value": "value1"},
            "remove": {"value": "value2"},
            "keep_too": {"value": "value3"},
        }
        result = BatchResult(items=items, loaded=3, failed=0)

        def keep_filter(key: str, value: dict[str, Any]) -> bool:
            return "keep" in key

        new_result = filter_items(result, keep_filter)

        assert "keep" in new_result.items
        assert "keep_too" in new_result.items
        assert "remove" not in new_result.items
        # loaded updated to kept count; failed incremented by removed count
        assert new_result.loaded == 2
        assert new_result.failed == 1


class TestBatchAnalysis:
    """Test batch analysis and reporting functions."""

    def test_get_batch_summary_empty(self) -> None:
        """Test batch summary for empty result."""
        result = BatchResult()

        summary = get_batch_summary(result)

        assert summary["items_stored"] == 0
        assert summary["files_processed"] == 0
        assert summary["success_rate_percent"] == 100.0
        assert summary["file_type_breakdown"] == {}
        assert summary["has_errors"] is False
        assert summary["has_warnings"] is False
        assert summary["has_infos"] is False

    def test_get_batch_summary_with_data(self) -> None:
        """Test batch summary with data."""
        result = BatchResult(
            items={"key1": {"value": "value1"}, "key2": {"value": "value2"}},
            processed_files=(Path("file1.yaml"), Path("file2.json")),
            file_types={"yaml": 1, "json": 1},
            loaded=2,
            failed=1,
            errors=("Error 1",),
            warnings=("Warning 1",),
        )

        summary = get_batch_summary(result)

        assert summary["items_stored"] == 2
        assert summary["files_processed"] == 2
        assert summary["successful_loads"] == 2
        assert summary["failed_loads"] == 1
        assert summary["success_rate_percent"] == 66.67
        assert summary["has_errors"] is True
        assert summary["has_warnings"] is True
        assert summary["file_type_breakdown"] == {"yaml": 1, "json": 1}
        # presence checks for other computed fields
        assert "items_per_file" in summary
        assert "average_items_per_type" in summary
        assert summary["processed_files"] == ["file1.yaml", "file2.json"]

    def test_analyze_batch_performance_empty(self) -> None:
        """Test performance analysis for empty batch."""
        result = BatchResult()

        performance = analyze_batch_performance(result)

        assert performance["efficiency_score"] == 1.0
        assert performance["error_rate"] == 0.0
        assert performance["dominant_file_type"] == "none"
        assert performance["skipped_file_rate"] == 0

    def test_analyze_batch_performance_with_data(self) -> None:
        """Test performance analysis with data."""
        result = BatchResult(
            file_types={"yaml": 8, "json": 2},
            loaded=8,
            failed=2,
            processed_files=(Path("a"), Path("b"), Path("c"), Path("d")),
            skipped_files=(Path("e"), Path("f")),
        )

        performance = analyze_batch_performance(result)

        assert performance["efficiency_score"] == 0.8
        assert performance["error_rate"] == 0.2
        assert performance["dominant_file_type"] == "yaml"
        assert performance["file_type_diversity"] == 2
        # items_per_file uses items_stored/len(processed_files); here items_stored=0
        assert performance["items_per_file"] == 0
        # skipped_file_rate = 2/4 = 0.5 (rounded to 3 decimals -> exact 0.5)
        assert performance["skipped_file_rate"] == 0.5

    def test_process_file_result_success(self) -> None:
        """Test processing successful file result."""
        result = BatchResult()
        file_path = Path("success.yaml")
        file_result: tuple[str, Any] = ("key", {"data": "success"})

        new_result = process_file_result(result, file_path, file_result, "success context")

        assert "key" in new_result.items
        assert file_path in new_result.processed_files
        assert new_result.loaded == 1

    def test_process_file_result_with_error(self) -> None:
        """Test processing file result with error."""
        result = BatchResult()
        file_path = Path("error.yaml")

        new_result = process_file_result(result, file_path, None, "Processing failed")

        assert file_path not in new_result.processed_files
        assert new_result.failed == 1
        assert any("Processing failed" in e for e in new_result.errors)

    def test_initialize_batch_with_file_types(self) -> None:
        """Test initializing batch with file types."""
        file_paths: list[Path] = [
            Path("test.yaml"),
            Path("test.json"),
            Path("test2.yaml"),
            Path("test2.json"),
            Path("test3.yaml"),
            Path("no_suffix"),
        ]

        result = initialize_batch_with_file_types(file_paths)

        assert result.file_types.get("yaml") == 3
        assert result.file_types.get("json") == 2
        assert result.file_types.get("noext") == 1

    def test_merge_batch_results(self) -> None:
        """Test merging multiple batch results."""
        result1 = BatchResult(
            items={"key1": {"value": "value1"}},
            loaded=1,
            failed=0,
            file_types={"yaml": 1},
            processed_files=(Path("a.yaml"),),
            skipped_files=(Path("s1"),),
            infos=("i1",),
        )

        result2 = BatchResult(
            items={"key2": {"value": "value2"}},
            loaded=1,
            failed=1,
            file_types={"json": 1},
            errors=("Error from result2",),
            warnings=("w2",),
            processed_files=(Path("b.json"),),
            skipped_files=(Path("s2"),),
        )

        merged = merge_batch_results(result1, result2)

        assert len(merged.items) == 2
        assert "key1" in merged.items and "key2" in merged.items
        assert merged.loaded == 2
        assert merged.failed == 1
        assert merged.file_types == {"yaml": 1, "json": 1}
        assert Path("a.yaml") in merged.processed_files and Path("b.json") in merged.processed_files
        assert Path("s1") in merged.skipped_files and Path("s2") in merged.skipped_files
        assert "Error from result2" in merged.errors and "w2" in merged.warnings and "i1" in merged.infos


class TestBatchResultEdgeCases:
    """Test edge cases and error conditions."""

    def test_store_item_none_data(self) -> None:
        """Test storing empty/minimal data."""
        result = BatchResult()
        file_path = Path("test.yaml")

        new_result = store_item(result, "key", {}, file_path=file_path)

        assert new_result.items["key"] == {}
        assert new_result.loaded == 1

    def test_track_file_type_no_extension(self) -> None:
        """Test tracking explicit empty file-type key."""
        result = BatchResult()
        new_result = track_file_type(result, "")
        assert new_result.file_types.get("") == 1

    def test_filter_items_empty_result(self) -> None:
        """Test filtering empty items."""
        result = BatchResult()

        def always_true(key: str, value: dict[str, Any]) -> bool:  # noqa: ARG001 - required signature
            return True

        new_result = filter_items(result, always_true)

        assert new_result.items == {}

    def test_success_rate_with_no_processing(self) -> None:
        """Test success rate when no processing occurred."""
        result = BatchResult()
        assert result.success_rate == 1.0  # Vacuous success

    def test_batch_result_immutability(self) -> None:
        """Test that batch result operations don't modify original."""
        original = BatchResult()
        file_path = Path("test.yaml")

        new_result = store_item(original, "key", {"value": "value"}, file_path=file_path)

        assert len(original.items) == 0
        assert len(new_result.items) == 1
