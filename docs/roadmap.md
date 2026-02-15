# Project Roadmap

## Phase 1: Planning & Setup (Weeks 1-2)

- [x] Repository structure and isolation (public/internal)
- [x] Git initialization with branch protection
- [x] Development tooling (ruff, mypy, pytest, pre-commit)
- [x] CI/CD pipelines (GitHub Actions)
- [x] Docker containerization
- [x] Documentation framework
- [x] Rules of Engagement template
- [x] Risk matrix schema
- [ ] Finalize legal/authorization documents (internal)
- [ ] Asset inventory from CMDB (internal)
- [ ] Set up test lab environment (VMs)

## Phase 2: Generic Repo Build (Weeks 3-5)

### Recon Module
- [ ] Integrate ReconFTW as submodule/wrapper
- [ ] Add reconftw_ai for AI-assisted analysis
- [ ] Subdomain enumeration (Amass integration)
- [ ] OSINT data collection
- [ ] DNS and certificate transparency parsing

### Scan Module
- [ ] Nuclei integration with custom templates
- [ ] Nmap wrapper with service detection
- [ ] Web application scanning
- [ ] SSL/TLS configuration analysis

### C2 Module
- [ ] Sliver C2 integration (primary)
- [ ] Mythic framework support
- [ ] Beacon management and tracking

### LLM/Garak Module
- [ ] Garak probe integration
- [ ] Prompt injection testing
- [ ] Data leakage detection
- [ ] Jailbreak testing
- [ ] Custom probe development for domain-specific testing

### Orchestrator Enhancements
- [ ] Pydantic config validation
- [ ] Module dependency graph
- [ ] Parallel module execution
- [ ] Progress tracking with Rich

### Report Engine
- [ ] JSON finding aggregation
- [ ] Markdown executive report generation
- [ ] ATT&CK Navigator heatmap export
- [ ] Risk scoring automation
- [ ] LLM-powered summary generation (Ollama)

## Phase 3: Internal Customization (Weeks 6-8)

> These tasks are tracked in the internal repo.

- [ ] Clone/fork to internal GitLab
- [ ] Add company target configs (encrypted)
- [ ] Customize Garak probes for internal LLMs
- [ ] AD/Entra ID attack path mapping
- [ ] OT/ICS protocol testing (Modbus, read-only)
- [ ] Full kill-chain pilot in test lab

## Phase 4: Testing & Validation (Weeks 9-10)

- [ ] Unit test coverage > 90%
- [ ] Integration tests (end-to-end pipeline)
- [ ] Ethical simulation runs on shadow environments
- [ ] LLM-specific: Garak probes on staging models
- [ ] Blue team dry-run: share reports for feedback
- [ ] Remediation playbook generation

## Phase 5: Deployment & Continuous Ops (Weeks 11-12)

- [ ] Scheduler setup (cron/Ansible) for persistent runs
- [ ] DefectDojo integration for finding management
- [ ] Team training and documentation handover
- [ ] Quarterly review cadence established

## Post-MVP Enhancements

- [ ] PyRIT integration for advanced AI red teaming
- [ ] Custom Nuclei template library
- [ ] Automated TTP evolution via local LLM analysis
- [ ] Integration with SIEM/SOAR for alert correlation
- [ ] Web dashboard for engagement management
- [ ] API for programmatic access
