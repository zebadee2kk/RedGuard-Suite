# Initial Design: Generic Red Team Suite

> Sanitized version of original planning notes. Company-specific references removed.

## Approach

This project prioritizes data security by keeping the public GitHub repository fully generic (no company-specific data, configs, or references), while enabling a seamless fork or clone to a private/local Git setup where authorized real-world details can be integrated.

## Step 1: Generic GitHub Repository

Create a public repo hosting a modular, extensible framework that chains open-source tools for red teaming phases. Focus on documentation, scripts, and Dockerfiles — no placeholders for sensitive data. License under MIT or Apache 2.0 for easy forking.

### Repo Structure (Original Design)

- `/docs/` — Setup guides, phase overviews, ethical guidelines, MITRE ATT&CK mappings
- `/modules/` — Subdirs for each phase (recon, vuln_scan, c2, phishing, ai_enhance, atomic_tests)
- `/orchestrator/` — Core Python scripts to chain modules via CLI
- `/configs/` — Generic YAML/JSON templates with safe placeholders
- `/reports/` — Output templates and exec summary generation
- `/tests/` — Unit tests and sample datasets
- `/ci-cd/` — GitHub Actions for linting, building, smoke tests

### Integrated Tools (2026)

1. **Recon & OSINT**: ReconFTW, Amass, SpiderFoot, Sherlock, Woodpecker (API/K8s)
2. **Vuln Scanning & Exploitation**: Nmap, Nuclei, Metasploit, ZAP
3. **C2 & Emulation**: Sliver (primary), Mythic, Havoc, AdaptixC2
4. **Atomic/Scenario Testing**: Atomic Red Team, TTPForge
5. **Phishing & Social Engineering**: Gophish, Social-Engineer Toolkit, AI-generated lures via Ollama
6. **AI Enhancements**: reconftw_ai, PentestGPT, PyRIT, Woodpecker, CAI, OpenRT
7. **Orchestration**: Python (Click/argparse), Ansible, Docker, Rigging for agent harnesses

## Step 2: Transition to Local Git with Real Data

### Customization Process

1. Clone and branch for internal use
2. Add real data securely (encrypted via git-crypt or SOPS)
3. Enhance for company-specific risks (OT/ICS, cloud paths, identity abuse)
4. Build risk assessment engine with LLM-powered analysis
5. Implement security controls (encryption, RBAC, audit logs, lab isolation)

### AI Learning Loop

- Use local LLM (Ollama on air-gapped hardware) to analyze past runs
- Fine-tune on anonymized logs for evolving TTP suggestions
- Pull public zero-days via NVD API and simulate

## Operational Principles

- Toolchains and automation matter more than any single tool; pair with human analysis
- Identity and attack paths are primary risk; prioritize privilege path mapping
- Continuous validation beats annual point-in-time tests
- Detection feedback loops improve both red and blue team outcomes

## Governance and Safety

- Encrypt sensitive configs (SOPS/age or vault) — no plaintext data in public repos
- Data classification headers and retention tags for audit readiness
- Supply chain controls: SBOM generation, pinned dependencies, signed releases, image scanning
- Safety gates: dry-run defaults, rate limits, kill switches, change windows
