# Usage

Install the package in editable (development) mode with [uv](https://docs.astral.sh/uv/):

```bash
uv venv .venv
uv pip install -e ".[dev,docs]"
```

Run tools without activating the venv:

```bash
uv run pytest
uv run ruff check .
```

Or activate manually if you want an interactive shell:

```bash
source .venv/bin/activate       # Linux / macOS / WSL
.\.venv\Scripts\activate        # Windows PowerShell
```

## Basic Usage

### Importing Types

```python
from ci.transparency.cwe.types.cwe_result_loading import CweLoadingResult
from ci.transparency.cwe.types.base import BaseResult, add_error, merge_results

result = CweLoadingResult()
print(result.success_rate)
```

### Working with Base Results

The types follow an immutable design - helper functions return new instances:

```python
from ci.transparency.cwe.types.base import BaseResult, add_error, add_warning

# Start with a clean result
result = BaseResult.ok()
print(result.has_errors)  # False

# Add an error (returns a new instance)
result_with_error = add_error(result, "Validation failed")
print(result_with_error.has_errors)  # True
print(result.has_errors)  # Still False (original unchanged)

# Chain operations
final_result = add_warning(result_with_error, "Minor issue detected")
print(final_result.total_issues)  # 2 (1 error + 1 warning)
```

### Loading Results

Track success/failure rates for batch operations:

```python
from ci.transparency.cwe.types.loading import (
    BaseLoadingResult, increment_loaded, increment_failed
)

# Start with empty loading result
loading_result = BaseLoadingResult()

# Process items (each call returns new instance)
loading_result = increment_loaded(loading_result)
loading_result = increment_loaded(loading_result)
loading_result = increment_failed(loading_result)

print(f"Success rate: {loading_result.success_rate}")  # 0.67 (2/3)
print(f"Total attempted: {loading_result.total_attempted}")  # 3
```

### Validation Results

Track pass/fail validation outcomes:

```python
from ci.transparency.cwe.types.validation import (
    BaseValidationResult, increment_validation_passed, increment_validation_failed
)

validation_result = BaseValidationResult()
validation_result = increment_validation_passed(validation_result)
validation_result = increment_validation_failed(validation_result)

print(f"Pass rate: {validation_result.pass_rate}")  # 0.5
print(f"Processed: {validation_result.total_processed}")  # 2
```

### Merging Results

Combine multiple results for aggregation:

```python
from ci.transparency.cwe.types.base import merge_results

result1 = add_error(BaseResult.ok(), "Error 1")
result2 = add_warning(BaseResult.ok(), "Warning 1")

combined = merge_results(result1, result2)
print(combined.error_count)    # 1
print(combined.warning_count)  # 1
print(combined.total_issues)   # 2
```

## Design Principles

- **Immutable**: All operations return new instances; originals never change
- **Type-preserving**: Helper functions maintain your subclass types
- **Memory-efficient**: Uses `__slots__` for better performance
- **Truthiness**: Results evaluate to `False` when they have errors

```python
if result:
    print("No errors found")
else:
    print(f"Found {result.error_count} errors")
```

See the **API Reference** for the complete list of classes and helper functions.
