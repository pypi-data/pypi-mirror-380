# Changelog

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

### Added

- (placeholder) Notes for the next release.

---

## [0.0.6] - 2025-09-27

### Changed

- Refactored schema-related type definitions to separate **domain-neutral** logic from CWE-specific types.
- Updated internal imports to use the new generic schema layer, simplifying future maintenance.

### Added

- **`schema`** package: generic dataclasses, slots-based result types, and supporting functions for JSON-schema
  loading and validation that can be reused across domains.
- **`schema_evolution`** package: supporting types and utilities for tracking schema changes across versions.

### Fixed

- Improved test coverage and consistency for schema error/result types (normalized cross-platform path handling).

### Developer Notes

- This package remains **types-only** (dataclasses, slots, and helper functions).
  Domain intelligence and catalog-specific logic continue to live in the **cwe-catalog** project.
- The generic schema layer now underpins the CWE schema types.

---

## [0.0.5] - 2025-09-27

### Changed

- Refactored `BatchResult` to use generic `items` terminology instead of `mappings`
- Renamed functions: `filter_mappings()` → `filter_items()`, `clear_mappings()` → `clear_items()`
- Updated property names: `mapping_count` → `item_count`, `has_mappings` → `has_items`
- Renamed `get_mapping_for_file()` method to `get_item_for_file()`

### Added

- Generic item access methods: `get_item_by_key()`, `has_item_key()`, `get_item_keys()`
- Utility methods: `get_item_values()`, `get_items()`
- Helper functions: `find_items_by_pattern()`, `get_items_with_field()`

### Fixed

- Corrected variable name inconsistencies throughout batch operations
- Fixed all function implementations to use new field names consistently

### Developer Notes

- This refactor prepares the foundation for domain-specific types (CWE, Standards)
- Generic terminology enables better polymorphism across layers
- Tests confirmed the layered architecture's maintainability, minimal files affected

---

## [0.0.4] - 2025-09-25

### Added

- **Initial public release**: initial CWE types

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking model changes relative to the spec
  - **MINOR** – backward-compatible additions
  - **PATCH** – clarifications, docs, tooling
- Versions are driven by git tags via `setuptools_scm`. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

[Unreleased]: https://github.com/civic-interconnect/civic-transparency-cwe-types/compare/v0.0.6...HEAD
[0.0.6]: https://github.com/civic-interconnect/civic-transparency-cwe-types/releases/tag/v0.0.6
[0.0.5]: https://github.com/civic-interconnect/civic-transparency-cwe-types/releases/tag/v0.0.5
[0.0.4]: https://github.com/civic-interconnect/civic-transparency-cwe-types/releases/tag/v0.0.4
