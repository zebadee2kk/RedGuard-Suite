# CLAUDE.md - RedGuard Suite (Public Repo)

## Project Overview
RedGuard Suite is an ethical red teaming and penetration testing framework aligned to MITRE ATT&CK/ATLAS, OWASP, and NIST. This is the **public, generic** repo — it must NEVER contain company-specific data, credentials, or internal infrastructure details.

## Architecture
- **Monorepo layout**: `src/redguard/` is the main package
- **Module pattern**: Each attack phase is a module in `src/redguard/modules/` with a `run(config) -> dict` interface
- **Orchestrator**: `src/redguard/orchestrator.py` chains modules based on config
- **CLI entry point**: `src/redguard/cli.py` using argparse
- **Config-driven**: JSON configs in `configs/` control which modules run and against which targets

## Key Conventions
- Python 3.10+ required
- Use `ruff` for linting and formatting (config in pyproject.toml)
- Use `mypy` for type checking in strict mode
- Use `pytest` for testing; tests live in `tests/` mirroring `src/` structure
- All modules must return `dict` with at minimum `{"status": str, "detail": str}`
- Use `pathlib.Path` over `os.path`
- Use `logging` module, never `print()` for operational output

## Safety Rules (CRITICAL)
- NEVER commit real domains, IPs, credentials, or company names
- NEVER include offensive payloads or working exploit code in this public repo
- All example configs must use `example.com` or similar safe placeholders
- The `internal/` repo (separate Git) holds company-specific overlays
- Any module that touches the network MUST check `config.get("safety", {}).get("dry_run", True)` and default to dry-run

## Development Workflow
1. Create feature branch from `main`: `git checkout -b feat/<name>`
2. Write code + tests
3. Run `make check` (lint + type-check + test)
4. Open PR — CI must pass before merge
5. Squash-merge to `main`

## Commands
- `make install` — Install deps in dev mode
- `make lint` — Run ruff linter
- `make format` — Auto-format with ruff
- `make typecheck` — Run mypy
- `make test` — Run pytest
- `make check` — Run all checks (lint + typecheck + test)
- `make security` — Run bandit + safety checks

## File Naming
- Snake_case for all Python files and directories
- Modules: `src/redguard/modules/<phase_name>.py`
- Tests: `tests/modules/test_<phase_name>.py`
- Configs: `configs/config.<variant>.json`
