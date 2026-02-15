# RedGuard Suite

An ethical red teaming and penetration testing framework aligned to MITRE ATT&CK/ATLAS, OWASP, and NIST.

> **This is the public, generic repository.** It contains no company-specific data, credentials, or internal infrastructure details.

## Features

- **Modular architecture** — each attack phase is an independent module
- **Config-driven** — JSON configs control targets, modules, and safety constraints
- **Safety-first** — dry-run defaults, scope enforcement, production detection
- **MITRE ATT&CK mapped** — modules align to ATT&CK/ATLAS techniques
- **LLM red teaming** — Garak integration for AI/ML security testing
- **Automated reporting** — risk matrix generation with impact/likelihood scoring

## Quick Start

```bash
# Clone
git clone https://github.com/<org>/RedGuard-Suite.git
cd RedGuard-Suite

# Install (dev mode)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
make install-dev

# Run checks
make check

# Run the CLI
redguard --config configs/config.public.example.json
```

## Project Structure

```
public/
├── .github/              # CI/CD, issue templates, PR templates
│   ├── workflows/        # GitHub Actions (CI, release)
│   ├── ISSUE_TEMPLATE/   # Bug report, feature request forms
│   └── dependabot.yml    # Dependency update automation
├── configs/              # Example configuration files
├── docker/               # Dockerfile and docker-compose
├── docs/                 # Project documentation
│   ├── risk_matrix_schema.md
│   └── roe_template.md
├── reports/              # Generated reports (gitignored content)
├── src/redguard/         # Main package
│   ├── modules/          # Attack phase modules
│   │   ├── recon.py      # Reconnaissance
│   │   ├── scan.py       # Vulnerability scanning
│   │   ├── llm_garak.py  # LLM red teaming (Garak)
│   │   └── report.py     # Report generation
│   ├── cli.py            # CLI entry point
│   └── orchestrator.py   # Module orchestration
├── tests/                # Test suite
├── CLAUDE.md             # AI-assisted development guide
├── CONTRIBUTING.md       # Contribution guidelines
├── CODE_OF_CONDUCT.md    # Community standards
├── SECURITY.md           # Vulnerability reporting policy
├── Makefile              # Dev task automation
└── pyproject.toml        # Python project config (deps, linting, testing)
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

## Security

- Pre-commit hooks enforce secret detection and security linting
- CI pipeline runs Bandit and TruffleHog on every PR
- Docker containers run as non-root with minimal privileges
- See [SECURITY.md](SECURITY.md) for vulnerability reporting

## License

MIT License. See [LICENSE](LICENSE) for details.
