# CONTRIBUTING.md

This repo hosts **Civic Transparency CWE Types** (MIT).
Goals: clarity, privacy-by-design, and low friction for collaborators.

> tl;dr - open an Issue/Discussion first for non-trivial work, keep PRs small, and run the quick checks below.

---

## Ways to Contribute

- **Docs**: Fix typos or improve examples in `docs/en/**`.
- **Code**: Add/refine typed result/error classes and tests (under `src/ci/transparency/cwe/types/`).
- **Tooling**: Improve checks and workflows to follow best practices.

---

## Ground Rules

- **Code of Conduct**: Be respectful and constructive. Reports: `info@civicinterconnect.org`.
- **License**: All contributions are accepted under the repo's **MIT License**.
- **Typing**: Package ships `py.typed`. Keep types strict (Pyright “strict”, mypy-friendly).
- **Imports**: No re-exports; import from **leaf modules** (prefer explicit).

---

## Before You Start

**Open an Issue or Discussion** for non-trivial changes so we can align early.

---

## Local Dev with `uv`

### Prerequisites

- Python **3.12+** (3.13 supported)
- Git, VS Code (optional), and **[uv](https://github.com/astral-sh/uv)**

### One-time setup

```bash
# Pin project interpreter and create venv
uv python pin 3.12
uv venv

# Install dev + docs extras (uses pyproject.toml)
uv sync --extra dev --extra docs --upgrade

# Install pre-commit hooks
uv run pre-commit install
```

> **VS Code tip:** Do **not** set `python.analysis.*` overrides in `.vscode/settings.json`.
> Pyright is configured in `pyproject.toml`. If you see “settingsNotOverridable” warnings, remove those workspace overrides.
> Select the interpreter at `.venv` (Command Palette → “Python: Select Interpreter”).

---

## Validate Your Changes

**Quick pass (Unix/macOS):**

```bash
uv run ruff check . --fix && uv run ruff format .
uv run pyright
uv run pytest --cov-fail-under=80
uv pip install -e ".[dev,docs]" --upgrade
uv run mkdocs build
```

**Quick pass (Windows PowerShell):**

```pwsh
uv run ruff check . --fix; uv run ruff format .
uv run pyright
uv run pytest --cov-fail-under=80
uv pip install -e ".[dev,docs]" --upgrade
uv run mkdocs build
```

Or run the project hooks (twice, if needed):

```bash
pre-commit run --all-files
```

---

## Commit & PR Guidelines

- **Small PRs**: one focused change per PR.
- **Title prefix**: `docs:`, `code:`, `types:`, `tests:`, `ci:`, etc.
- **Link** the related Issue/Discussion.
- Prefer **squash merge** for a clean history.
- Update docs and tests alongside behavior/API changes.

---

## Testing

```bash
uv run pytest -v --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml
```

- Coverage target is **80%** (config in `pyproject.toml`).
- Put tests under `tests/` and name files `test_*.py`.

---

## Linting & Types

- **Ruff** (lint + format): configured in `pyproject.toml`
- **Pyright** (strict): configured in `pyproject.toml`

```bash
uv run ruff check . --fix
uv run ruff format .
uv run pyright
```

---

## Build & Inspect the Package

```bash
uv run python -m build
# Inspect wheel contents (Unix/macOS):
unzip -l dist/*.whl
# Windows (PowerShell):
$TMP = New-Item -ItemType Directory -Path ([System.IO.Path]::GetTempPath()) -Name ("wheel_" + [System.Guid]::NewGuid())
Expand-Archive dist\*.whl -DestinationPath $TMP.FullName
Get-ChildItem -Recurse $TMP.FullName | ForEach-Object { $_.FullName.Replace($TMP.FullName + '\','') }
Remove-Item -Recurse -Force $TMP
```

Verify the wheel includes:

- `ci/transparency/cwe/types/**`
- `py.typed`
- No unexpected files

---

## Docs

```bash
# Build once
uv run mkdocs build

# Live preview
uv run mkdocs serve
# Visit http://127.0.0.1:8000/
```

Ensure:

- Autodoc renders without errors
- Navigation works
- Examples render correctly

---

## Release

We use **setuptools-scm**; version derives from **git tags**.

1. Update `CHANGELOG.md`.
2. Ensure CI is green.
3. Final local checks (lint, types, tests, docs).
4. Build locally and sanity-check the wheel.
5. Tag and push.

**Pre-release script:**

```bash
git add .
uv run ruff check . --fix && uv run ruff format .
pre-commit run --all-files
uv run pyright
uv run pytest --cov-fail-under=80
uv run mkdocs build
uv build

# Import sanity check (choose your platform command)
python -c "import ci.transparency.cwe.types; print('Package imports OK')"
# or
py -c "import ci.transparency.cwe.types; print('Package imports OK')"

git add .
git commit -m "Prep vX.Y.Z"
git push -u origin main

# Verify the GitHub actions run successfully. If so, continue:
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

A GitHub Action will:

- Build and publish to **PyPI** (Trusted Publishing),
- Create a **GitHub Release** with artifacts,
- Deploy **versioned docs** with `mike`.

## Cleanup

**Unix/macOS:**

```bash
find . -name '__pycache__' -type d -prune -exec rm -rf {} +
rm -rf build/ dist/ .eggs/ src/*.egg-info/
```

**Windows PowerShell:**

```pwsh
Get-ChildItem -Recurse -Include __pycache__,*.egg-info,build,dist | Remove-Item -Recurse -Force
```
---

## Support

- **Discussions**: Open design questions
- **Issues**: Bugs or concrete proposals
- **Private**: `info@civicinterconnect.org` (sensitive reports)
