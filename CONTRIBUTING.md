# Contributing to RedGuard Suite

Thank you for your interest in contributing to RedGuard Suite. This document outlines the process and guidelines.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/<you>/RedGuard-Suite.git`
3. Create a feature branch: `git checkout -b feat/your-feature`
4. Install dev dependencies: `make install-dev`
5. Make your changes
6. Run checks: `make check`
7. Commit and push
8. Open a Pull Request

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
make install-dev
```

This installs the package in editable mode with all dev tools (ruff, mypy, pytest, pre-commit).

## Branch Naming

| Prefix     | Purpose                        |
|------------|--------------------------------|
| `feat/`    | New feature or module          |
| `fix/`     | Bug fix                        |
| `docs/`    | Documentation only             |
| `refactor/`| Code restructuring             |
| `test/`    | Adding or fixing tests         |
| `ci/`      | CI/CD changes                  |

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(recon): add subdomain enumeration via amass
fix(report): handle empty results without crashing
docs: update installation instructions
```

## Pull Request Process

1. Ensure `make check` passes (lint + typecheck + test)
2. Update documentation if adding new modules
3. Fill out the PR template completely
4. Map changes to MITRE ATT&CK techniques where applicable
5. PRs require at least one maintainer review

## Adding a New Module

1. Create `src/redguard/modules/<module_name>.py`
2. Implement the standard interface: `def run(config: dict) -> dict`
3. Return at minimum `{"status": str, "detail": str}`
4. Default to dry-run mode unless explicitly configured otherwise
5. Add tests in `tests/modules/test_<module_name>.py`
6. Register in `src/redguard/orchestrator.py`
7. Document the ATT&CK mapping

## Security Requirements

- **No secrets**: Never commit credentials, API keys, or internal data
- **No live exploits**: Public repo must not contain weaponized code
- **Dry-run default**: All network-touching modules must default to dry-run
- **Bandit clean**: Code must pass bandit security linter
- **Dependencies**: Only add well-maintained, reputable packages
