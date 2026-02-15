# RedGuard Suite

[![CI](https://github.com/zebadee2kk/RedGuard-Suite/actions/workflows/ci.yml/badge.svg)](https://github.com/zebadee2kk/RedGuard-Suite/actions/workflows/ci.yml)
[![CodeQL](https://github.com/zebadee2kk/RedGuard-Suite/actions/workflows/codeql.yml/badge.svg)](https://github.com/zebadee2kk/RedGuard-Suite/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

An ethical red teaming and penetration testing framework aligned to MITRE ATT&CK/ATLAS, OWASP, and NIST.

> **This is the public, generic repository.** It contains no company-specific data, credentials, or internal infrastructure details.

## Features

- **Modular architecture** — each attack phase is an independent module
- **Config-driven** — JSON configs control targets, modules, and safety constraints
- **Safety-first** — dry-run defaults, scope enforcement, production detection
- **MITRE ATT&CK mapped** — 45 techniques mapped across modules
- **LLM red teaming** — Garak integration for AI/ML security testing
- **Automated reporting** — risk matrix generation with impact/likelihood scoring
- **Operational playbooks** — OPSEC, incident response, evidence handling, deconfliction

## Quick Start

```bash
# Clone
git clone https://github.com/zebadee2kk/RedGuard-Suite.git
cd RedGuard-Suite

# Install (dev mode)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install

# Run checks
./scripts/run_checks.sh    # Or: ruff check src/ && pytest tests/

# Run the CLI
redguard --config configs/config.public.example.json
```

## Project Structure

```
.
├── .github/
│   ├── workflows/           # CI, CodeQL, release automation
│   ├── ISSUE_TEMPLATE/      # Bug report, feature request forms
│   ├── pull_request_template.md
│   ├── CODEOWNERS
│   └── dependabot.yml
├── configs/                 # Example configuration files
├── docker/
│   ├── Dockerfile           # Non-root, hardened container
│   └── docker-compose.yml   # Security-constrained orchestration
├── docs/
│   ├── playbooks/           # Operational security protocols
│   │   ├── operational_security.md
│   │   ├── incident_response.md
│   │   ├── evidence_handling.md
│   │   ├── deconfliction_guide.md
│   │   └── legal_compliance_checklist.md
│   ├── research/            # Design rationale and research
│   ├── architecture.md      # System design and module interface
│   ├── attack_mapping.md    # 45 MITRE ATT&CK/ATLAS techniques
│   ├── module_development_guide.md
│   ├── development_setup.md
│   ├── roadmap.md
│   ├── risk_matrix_schema.md
│   └── roe_template.md      # Rules of Engagement template
├── reports/                 # Generated reports (gitignored content)
├── scripts/                 # Utility scripts
│   ├── run_checks.sh        # Local CI equivalent
│   └── generate_sbom.sh     # Software bill of materials
├── src/redguard/            # Main package
│   ├── modules/             # Attack phase modules
│   │   ├── recon.py
│   │   ├── scan.py
│   │   ├── llm_garak.py
│   │   └── report.py
│   ├── cli.py               # CLI entry point
│   └── orchestrator.py      # Module orchestration engine
├── tests/                   # Test suite (mirrors src/ structure)
├── CHANGELOG.md             # Version history
├── CLAUDE.md                # AI-assisted development guide
├── CODE_OF_CONDUCT.md       # Ethical use requirements
├── CONTRIBUTING.md          # Contribution guidelines
├── LICENSE                  # MIT License
├── Makefile                 # Dev task automation
├── SECURITY.md              # Vulnerability reporting policy
└── pyproject.toml           # Python project config
```

## Development

| Command            | Description                          |
|--------------------|--------------------------------------|
| `make install-dev` | Install with dev dependencies        |
| `make lint`        | Run ruff linter                      |
| `make format`      | Auto-format code                     |
| `make typecheck`   | Run mypy type checker                |
| `make test`        | Run pytest                           |
| `make test-cov`    | Run tests with coverage report       |
| `make check`       | Run all checks (lint+typecheck+test) |
| `make security`    | Run security scans (bandit)          |
| `make docker-build`| Build Docker image                   |

## Security Controls

| Control | Implementation |
|---------|---------------|
| Linting | ruff with 13 rule categories including security (S, B) |
| Type safety | mypy in strict mode |
| Testing | pytest with 80% coverage threshold, Python 3.10-3.12 matrix |
| Security scanning | Bandit (SAST) + TruffleHog (secrets) + CodeQL (weekly) |
| Secret detection | detect-secrets pre-commit + GitHub push protection |
| Dependency monitoring | Dependabot alerts + automated security updates |
| Container hardening | Non-root user, read-only FS, no-new-privileges |
| Branch protection | PR required, code owner review, all CI must pass |
| Data isolation | .gitignore blocks internal patterns; no company data in public repo |

## Operational Playbooks

Before any engagement, review the [playbooks](docs/playbooks/):

- [Operational Security](docs/playbooks/operational_security.md) — OPSEC for operators
- [Incident Response](docs/playbooks/incident_response.md) — when things go wrong
- [Evidence Handling](docs/playbooks/evidence_handling.md) — chain of custody
- [Deconfliction Guide](docs/playbooks/deconfliction_guide.md) — red/blue coordination
- [Legal Compliance](docs/playbooks/legal_compliance_checklist.md) — pre-engagement checklist

## License

MIT License. See [LICENSE](LICENSE) for details.
