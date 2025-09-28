# Civic Transparency CWE Types

[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)](https://civic-interconnect.github.io/civic-transparency-cwe-types/)
[![PyPI](https://img.shields.io/pypi/v/civic-transparency-cwe-types.svg)](https://pypi.org/project/civic-transparency-cwe-types/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue?logo=python)](#)
[![CI Status](https://github.com/civic-interconnect/civic-transparency-cwe-types/actions/workflows/ci.yml/badge.svg)](https://github.com/civic-interconnect/civic-transparency-cwe-types/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

> Maintained by [**Civic Interconnect**](https://github.com/civic-interconnect).

- **Documentation:** https://civic-interconnect.github.io/civic-transparency-cwe-types/
- **Contributing:** [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## Overview

Immutable datatype library for Common Weakness Enumeration (CWE) analysis and validation workflows. Provides strongly-typed Python models with zero runtime dependencies.

**Key Features:**

- **Zero Dependencies:** Pure Python with no external requirements
- **Immutable Design:** Functional-style helpers return new instances
- **Type Safety:** Full static typing with py.typed marker
- **Memory Efficient:** Slotted dataclasses for better performance
- **CWE Ecosystem:** Foundation types for transparency workflows

## Installation

```bash
pip install civic-transparency-cwe-types
```

For development:

```bash
pip install "civic-transparency-cwe-types[dev]"
```

---

## Quick Start

```python

# Multiple result types available
from ci.transparency.cwe.types.base import BaseResult, add_error
from ci.transparency.cwe.types.schema_result_loading import SchemaLoadingResult
from ci.transparency.cwe.types.standards_result_validation import StandardsValidationResult

# Import CWE Loading Result and Add CWE function
from ci.transparency.cwe.types.cwe_result_loading import CweLoadingResult, add_cwe

# Create and work with immutable result types
result = CweLoadingResult()
result = add_cwe(result, "CWE-79", {"name": "Cross-site Scripting"})

print(f"Loaded CWEs: {result.cwe_count}")
print(f"Success rate: {result.success_rate}")
```

See the [Usage Guide](https://civic-interconnect.github.io/civic-transparency-cwe-types/usage/) for more examples.

## Development Setup

```bash
git clone https://github.com/civic-interconnect/civic-transparency-cwe-types
cd civic-transparency-cwe-types
uv venv
.venv\Scripts\activate
uv sync --extra dev --extra docs --upgrade
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

---

## Support and Community

- **Documentation:** https://civic-interconnect.github.io/civic-transparency-cwe-types/
- **Issues:** [GitHub Issues](https://github.com/civic-interconnect/civic-transparency-cwe-types/issues)
- **Discussions:** [GitHub Discussions](https://github.com/civic-interconnect/civic-transparency-cwe-types/discussions)
- **Email:** info@civicinterconnect.org

---

## About Civic Transparency

Civic Transparency is an open standard for privacy-preserving, non-partisan analysis of how information spreads in civic contexts. The specification enables researchers, platforms, and civic organizations to share insights while protecting individual privacy.

**Core Principles:**
- **Privacy by Design:** No personally identifiable information
- **Aggregation First:** Time-bucketed, statistical summaries
- **Open Standard:** Collaborative, transparent development
- **Practical Implementation:** Real-world deployment focus
