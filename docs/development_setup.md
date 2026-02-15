# Development Environment Setup

## Prerequisites

| Tool       | Version | Purpose                          |
|------------|---------|----------------------------------|
| Python     | 3.10+   | Runtime                          |
| Git        | 2.40+   | Version control                  |
| Docker     | 24+     | Containerized testing (optional) |
| Make       | 4.0+    | Task automation                  |

## Quick Setup

### 1. Clone the Repository

```bash
git clone https://github.com/zebadee2kk/RedGuard-Suite.git
cd RedGuard-Suite
```

### 2. Create Virtual Environment

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate
```

### 3. Install Dependencies

```bash
# Install package with all dev tools
make install-dev

# This runs:
#   pip install -e ".[dev]"
#   pre-commit install
```

### 4. Verify Setup

```bash
# Run all checks
make check

# Expected output:
#   ruff check passes
#   mypy passes
#   pytest passes (all tests green)
```

## Pre-commit Hooks

After `make install-dev`, the following hooks run on every `git commit`:

| Hook               | What It Does                                    |
|--------------------|-------------------------------------------------|
| trailing-whitespace| Removes trailing whitespace                      |
| end-of-file-fixer  | Ensures files end with a newline                |
| check-yaml/json    | Validates YAML and JSON syntax                  |
| check-added-large-files | Blocks files > 500KB                       |
| detect-private-key | Blocks commits containing private keys          |
| no-commit-to-branch| Prevents direct commits to `main`               |
| ruff               | Lints Python code (auto-fixes where possible)   |
| ruff-format        | Formats Python code                              |
| detect-secrets     | Scans for accidentally committed secrets        |
| bandit             | Security linter for Python                      |

If a hook fails, the commit is blocked. Fix the issue and re-commit.

### Bypassing Hooks (Emergency Only)

```bash
# NOT recommended — only for genuine emergencies
git commit --no-verify -m "emergency fix"
```

## IDE Configuration

### VSCode (Recommended)

Recommended extensions:
- **Python** (ms-python.python)
- **Ruff** (charliermarsh.ruff)
- **Mypy Type Checker** (ms-python.mypy-type-checker)

Workspace settings are managed via `.editorconfig`. VSCode will pick these up automatically with the EditorConfig extension.

### Suggested `.vscode/settings.json` (not committed)

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests/"],
  "mypy-type-checker.args": ["--config-file=pyproject.toml"]
}
```

## Docker Development

### Build and Run

```bash
# Build the image
make docker-build

# Run interactively
make docker-run

# Or use docker-compose
cd docker/
docker compose up
```

### Docker Security Features

The container is hardened:
- Runs as non-root user `redguard`
- Read-only filesystem with tmpfs for `/tmp`
- `no-new-privileges` security option
- Isolated bridge network

## Common Workflows

### Creating a Feature Branch

```bash
git checkout main
git pull origin main
git checkout -b feat/add-nuclei-scanner
```

### Running Specific Tests

```bash
# Single test file
pytest tests/modules/test_recon.py

# Single test function
pytest tests/modules/test_recon.py::test_recon_returns_status

# Tests with verbose output
pytest tests/ -v

# Tests with coverage
make test-cov
```

### Checking Code Quality

```bash
# Just linting
make lint

# Just type checking
make typecheck

# Just security
make security

# All at once
make check
```

## Troubleshooting

### `pre-commit` hooks not running
```bash
pre-commit install
pre-commit run --all-files  # Test on all files
```

### `mypy` errors on third-party packages
```bash
# Install type stubs
pip install types-PyYAML types-requests
```

### Tests failing with import errors
```bash
# Ensure you installed in editable mode
pip install -e ".[dev]"
```
