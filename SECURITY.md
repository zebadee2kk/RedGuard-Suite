# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.x     | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in RedGuard Suite, **do not open a public issue**.

Instead, please report it responsibly:

1. **Email**: Send details to the maintainers (see CODEOWNERS) with subject line `[SECURITY] RedGuard Suite Vulnerability`
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (if any)

We will acknowledge receipt within 48 hours and provide a timeline for a fix.

## Scope

This policy applies to the **public RedGuard Suite repository only**. The internal/company-specific repo has its own security procedures.

### In Scope
- Code vulnerabilities (injection, path traversal, etc.)
- Credential/secret leaks in committed code
- Unsafe default configurations
- Supply chain risks in dependencies

### Out of Scope
- Vulnerabilities in upstream tools (ReconFTW, Nuclei, etc.) — report those to their respective projects
- Social engineering of maintainers
- Denial of service against CI/CD infrastructure

## Security Controls in This Project

- **Pre-commit hooks**: `detect-secrets` and `bandit` run on every commit
- **CI pipeline**: Automated security scanning with Bandit and TruffleHog
- **Dependencies**: Monitored via Dependabot (see `.github/dependabot.yml`)
- **Docker**: Containers run as non-root with `no-new-privileges` and read-only filesystem
- **Code review**: All PRs require maintainer approval via CODEOWNERS
