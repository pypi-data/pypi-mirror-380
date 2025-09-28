# Usage Guide

This guide covers common patterns for using the Civic Transparency CWE Types library.

## Installation

```bash
pip install civic-transparency-cwe-types
```

For development:

```bash
pip install "civic-transparency-cwe-types[dev]"
```

## Core Concepts

### Immutability

All operations return new instances - originals are never modified:

```python
from ci.transparency.cwe.types.base import BaseResult, add_error

original = BaseResult()
with_error = add_error(original, "Failed validation")

print(original.has_errors)    # False
print(with_error.has_errors)  # True
```

### Type Preservation

Helper functions maintain your specific result types:

```python
from ci.transparency.cwe.types.cwe import CweLoadingResult, add_cwe

# CweLoadingResult stays CweLoadingResult
cwe_result = CweLoadingResult()
updated = add_cwe(cwe_result, "CWE-79", {"id": "CWE-79", "name": "XSS"})
print(type(updated))  #
```

## Working with Base Types

### Basic Result Operations

```python
from ci.transparency.cwe.types.base import (
    BaseResult, add_error, add_warning, add_info
)

# Start clean
result = BaseResult()

# Add different message types
result = add_error(result, "Critical failure")
result = add_warning(result, "Potential issue")
result = add_info(result, "Processing complete")

# Check status
print(f"Errors: {result.error_count}")
print(f"Warnings: {result.warning_count}")
print(f"Total issues: {result.total_issues}")
print(f"Has problems: {not bool(result)}")  # Results are falsy when they have errors
```

### Loading Operations

```python
from ci.transparency.cwe.types.base import BaseLoadingResult

# Track loading progress
loading = BaseLoadingResult()
loading = loading.increment_loaded()  # Or use helper functions
loading = loading.increment_loaded()
loading = loading.increment_failed()

print(f"Success rate: {loading.success_rate:.2%}")
print(f"Total attempted: {loading.total_attempted}")
```

### Validation Operations

```python
from ci.transparency.cwe.types.base import BaseValidationResult

validation = BaseValidationResult()
validation = validation.increment_passed()
validation = validation.increment_failed()

print(f"Pass rate: {validation.success_rate:.2%}")
print(f"Total validated: {validation.total_processed}")
```

## CWE Domain Operations

### Loading CWE Data

```python
from ci.transparency.cwe.types.cwe import (
    CweLoadingResult, add_cwe, track_duplicate_cwe
)
from pathlib import Path

result = CweLoadingResult()

# Add CWE definitions
cwe_data = {
    "id": "CWE-79",
    "name": "Cross-site Scripting",
    "category": "injection",
    "relationships": [
        {"cwe_id": "CWE-80", "type": "ChildOf"}
    ]
}
result = add_cwe(result, "CWE-79", cwe_data, file_path=Path("cwe-79.yaml"))

# Handle duplicates
result = track_duplicate_cwe(result, "CWE-79", Path("duplicate.yaml"))

# Check results
print(f"CWEs loaded: {result.cwe_count}")
print(f"Duplicates found: {result.duplicate_count}")
print(f"Has CWE-79: {result.has_cwe('CWE-79')}")
```

### CWE Validation

```python
from ci.transparency.cwe.types.cwe import (
    CweValidationResult, validate_cwe, batch_validate_cwes
)

validation = CweValidationResult()

# Validate individual CWE
cwe_data = {"id": "CWE-79", "name": "XSS", "category": "injection"}
validation = validate_cwe(validation, "CWE-79", cwe_data)

# Batch validation
cwe_dict = {
    "CWE-79": {"id": "CWE-79", "name": "XSS"},
    "CWE-89": {"id": "CWE-89", "name": "SQL Injection"}
}
validation = batch_validate_cwes(validation, cwe_dict)

print(f"Validated: {validation.validated_count}")
print(f"Passed: {len(validation.get_passed_cwes())}")
print(f"Failed: {len(validation.get_failed_cwes())}")
```

### CWE Relationships

```python
from ci.transparency.cwe.types.cwe import (
    CweRelationshipResult, analyze_relationships
)

relationships = CweRelationshipResult()

# Analyze CWE relationships
cwe_dict = {
    "CWE-79": {
        "id": "CWE-79",
        "relationships": [{"cwe_id": "CWE-80", "type": "ChildOf"}]
    },
    "CWE-80": {
        "id": "CWE-80",
        "relationships": [{"cwe_id": "CWE-79", "type": "ParentOf"}]
    }
}

relationships = analyze_relationships(relationships, cwe_dict)

print(f"Total relationships: {relationships.total_relationships}")
print(f"Circular dependencies: {relationships.circular_dependency_count}")
print(f"Orphaned CWEs: {relationships.orphaned_cwe_count}")
```

## Batch Processing

### Basic Batch Operations

```python
from ci.transparency.cwe.types.batch import (
    BatchResult, add_mapping, skip_file, track_invalid_file
)
from pathlib import Path

batch = BatchResult()

# Process items
batch = add_mapping(batch, "item1", {"data": "value1"})
batch = add_mapping(batch, "item2", {"data": "value2"})

# Handle skipped files
batch = skip_file(batch, Path("README.md"), "Not a data file")

# Track errors
batch = track_invalid_file(batch, Path("corrupt.yaml"), "Malformed YAML")

print(f"Items processed: {batch.total_items}")
print(f"Success rate: {batch.success_rate:.2%}")
print(f"Skipped files: {batch.skipped_file_count}")
```

## Standards Processing

### Loading Standards

```python
from ci.transparency.cwe.types.standards import (
    StandardsLoadingResult, add_standard
)

standards = StandardsLoadingResult()

# Add standards
nist_data = {
    "id": "NIST-SP-800-53",
    "name": "Security Controls",
    "framework": "NIST",
    "version": "Rev 5"
}
standards = add_standard(standards, "NIST-SP-800-53", nist_data)

print(f"Standards loaded: {standards.standards_count}")
print(f"Frameworks: {standards.framework_count}")
print(f"Has NIST: {standards.has_standard('NIST-SP-800-53')}")
```

### Standards Mapping

```python
from ci.transparency.cwe.types.standards import (
    StandardsMappingResult, analyze_mappings
)

mappings = StandardsMappingResult()

# Analyze control mappings
standards_dict = {
    "NIST-SP-800-53": {
        "id": "NIST-SP-800-53",
        "controls": [
            {
                "id": "AC-1",
                "mappings": [
                    {"target_id": "CWE-79", "mapping_type": "cwe"}
                ]
            }
        ]
    }
}

mappings = analyze_mappings(mappings, standards_dict)

print(f"Total mappings: {mappings.total_mappings}")
print(f"Invalid mappings: {mappings.invalid_mapping_count}")
```

## Phase-Based Validation

### Single Phase Tracking

```python
from ci.transparency.cwe.types.validation.phase import (
    PhaseValidationResult, add_processed_item, set_phase_detail
)

phase = PhaseValidationResult(phase_name="cwe-loading")
phase = add_processed_item(phase, "CWE-79")
phase = add_processed_item(phase, "CWE-89")
phase = set_phase_detail(phase, "processing_time", 45.2)

print(f"Phase: {phase.phase_name}")
print(f"Items processed: {phase.items_count}")
print(f"Processing time: {phase.get_detail('processing_time')}ms")
```

### Multi-Phase Workflows

```python
from ci.transparency.cwe.types.validation.phase import (
    MultiPhaseValidationResult, add_phase, set_current_phase,
    add_item_to_phase, annotate_phase
)

# Create workflow
workflow = MultiPhaseValidationResult()

# Add phases
loading_phase = PhaseValidationResult(phase_name="loading")
workflow = add_phase(workflow, loading_phase, set_current=True)

# Work with phases by name
workflow = add_item_to_phase(workflow, "validation", "CWE-79")
workflow = annotate_phase(workflow, "validation",
                         rules_checked=["required_fields", "format"])

print(f"Phases: {workflow.phase_count}")
print(f"Current: {workflow.current_phase}")
print(f"Total items: {workflow.items_processed_total}")
```

## Error Handling

All result types include rich error context:

```python
from ci.transparency.cwe.types.cwe import CweLoadingResult, track_invalid_file
from pathlib import Path

result = CweLoadingResult()
result = track_invalid_file(result, Path("bad.yaml"), "Invalid YAML syntax")

if result.has_errors:
    print("Errors occurred:")
    for error in result.errors:
        print(f"  - {error}")

    print(f"Error count: {result.error_count}")
    print(f"Failed operations: {result.failed}")
```

## Conversion Between Types

```python
from ci.transparency.cwe.types.batch import BatchResult
from ci.transparency.cwe.types.cwe import CweLoadingResult

# Convert batch result to CWE result
batch_data = {
    "CWE-79": {"id": "CWE-79", "name": "XSS"},
    "CWE-89": {"id": "CWE-89", "name": "SQLi"}
}
batch = BatchResult(mappings=batch_data, loaded=2)

cwe_result = CweLoadingResult.from_batch(batch)
print(f"Converted CWEs: {cwe_result.cwe_count}")
```

See the **API Reference** for complete documentation of all classes and functions.
