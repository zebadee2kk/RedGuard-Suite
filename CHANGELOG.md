# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CodeQL static analysis workflow for automated vulnerability scanning
- Operational security playbooks: OPSEC, incident response, evidence handling, deconfliction, legal compliance
- GitHub project management: milestones, labels, and backlog issues for all 5 phases
- Docker build validation in CI pipeline

### Changed
- Hardened branch protection: require code owner reviews, conversation resolution, all CI jobs
- Pinned TruffleHog action to specific version tag
- Enabled Dependabot vulnerability alerts and security updates
- Enabled GitHub secret scanning with push protection

## [0.1.0] - 2026-02-15

### Added
- Initial project scaffolding with modular pipeline architecture
- CLI entry point (`redguard`) with JSON config-driven execution
- Module stubs: recon, scan, llm_garak, report
- Orchestrator engine sequencing modules from config
- CI/CD: GitHub Actions for lint (ruff), typecheck (mypy), test matrix (Python 3.10-3.12), security scan (bandit + TruffleHog)
- Release workflow with automated GitHub Releases on tag push
- Pre-commit hooks: ruff, detect-secrets, bandit, safety, trailing whitespace, YAML/TOML validation
- Docker: Dockerfile with non-root user, docker-compose with security hardening
- Dependabot configuration for pip and GitHub Actions
- Comprehensive documentation:
  - Architecture overview with module interface contract
  - 45 MITRE ATT&CK/ATLAS techniques mapped to modules
  - Module development guide with templates and checklists
  - Development setup guide
  - Project roadmap (5 phases, 12 weeks)
  - Risk matrix schema with 3-factor scoring
  - Rules of Engagement template with ATT&CK-mapped techniques
- Research library: initial design, modern practices, executive validation, Garak integration, tooling reference, 2026 landscape, learning roadmap
- Security policy (SECURITY.md) with vulnerability reporting process
- Contributing guidelines with branch naming and conventional commits
- Code of Conduct adapted for ethical red teaming
- MIT License

[Unreleased]: https://github.com/zebadee2kk/RedGuard-Suite/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/zebadee2kk/RedGuard-Suite/releases/tag/v0.1.0
