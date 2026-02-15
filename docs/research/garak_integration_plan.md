# Garak LLM Red Teaming Integration Plan

> Design and implementation plan for integrating NVIDIA Garak into RedGuard Suite.

## Overview

Garak (Generative AI Red-teaming & Assessment Kit) acts as an "nmap/Metasploit for LLMs" — systematically probing models for vulnerabilities like prompt injection, jailbreaks, hallucination, data leakage, toxicity generation, and misinformation.

### Why Integrate Garak

- **Complements existing stack**: Dedicated AI/LLM-specific phase alongside traditional red team modules
- **Continuous and automated**: Run in CI/CD-like loops on test models, feed results to DefectDojo
- **Ethical and authorized**: Fully open-source (Apache 2.0), CLI-driven, designed for authorized red teaming
- **Actively maintained**: NVIDIA + community, with new probes for emerging threats like multi-turn crescendo attacks

## 1. Public Repo Integration (Generic)

### Module Design

Add as `src/redguard/modules/llm_garak.py` with standard module interface:

```python
def run(config: dict) -> dict:
    """Run Garak probes against configured LLM endpoints."""
    dry_run = config.get("safety", {}).get("dry_run", True)
    garak_config = config.get("llm_garak", {})

    if dry_run:
        return {"status": "dry_run", "detail": "Would run Garak probes"}

    # Build Garak CLI command from config
    cmd = ["garak", "--model_type", garak_config["model_type"]]
    if "model_name" in garak_config:
        cmd.extend(["--model_name", garak_config["model_name"]])
    if "uri" in garak_config:
        cmd.extend(["--uri", garak_config["uri"]])

    cmd.extend(["--probes", ",".join(garak_config.get("probes", ["default"]))])
    cmd.extend(["--detectors", ",".join(garak_config.get("detectors", ["default"]))])
    # ... execute and parse results ...
```

### Config Schema

```json
{
  "llm_garak": {
    "model_type": "rest",
    "uri": "http://localhost:11434/v1/chat/completions",
    "probes": ["prompt_injection", "jailbreak", "data_leakage", "hallucination"],
    "detectors": ["default"]
  }
}
```

### Probe Categories

| Category | What It Tests | ATLAS Mapping |
|----------|---------------|---------------|
| Prompt Injection | Override system instructions | AML.T0051 |
| Jailbreak | Bypass safety guardrails | AML.T0054 |
| Data Leakage | Exfiltrate training/context data | AML.T0025 |
| Hallucination | Generate false/harmful information | N/A |
| Toxicity | Produce harmful or offensive content | N/A |
| Encoding-based | Unicode/encoding attacks to bypass filters | AML.T0051 |

## 2. Internal Overlay (Company-Specific)

### Custom Probes
- Domain-specific data leakage testing (proprietary information, supplier data)
- Business-context toxicity testing (harmful advice in company domain)
- RAG poisoning — test if retrieval-augmented generation can be manipulated

### Automation
- Schedule weekly scans via cron/Ansible on staging LLM instances
- Parse Garak JSON reports → feed to local LLM (Ollama) for executive summary
- Integrate with risk matrix: "LLM Prompt Injection Success → Data Exfil" (Severity: Critical)

### Orchestration Chain
1. **Recon** → Discover LLM-exposed endpoints (Nuclei templates for /v1/chat, OpenAI-compatible APIs)
2. **If found** → Auto-trigger Garak probes
3. **Post-scan** → If vulnerabilities detected → simulate exploit in test environment
4. **Report** → Aggregate probe-by-probe results with repro prompts, impact, and mitigations

## 3. Best Practices

- **Run in isolation**: Use test/staging LLM instances only — never prod without explicit RoE
- **Ethical use**: Document all probes as authorized testing
- **Updates**: Periodically pull from upstream NVIDIA/garak for new probes
- **Complement**: Pair with PyRIT for more dynamic, goal-oriented multi-turn attacks

## GitHub Repos by Phase (Reference)

| Phase | Repositories |
|-------|-------------|
| Recon | six2dez/reconftw, OWASP/Amass, projectdiscovery/httpx |
| Scan | projectdiscovery/nuclei, nmap/nmap, zaproxy/zaproxy |
| C2 | BishopFox/sliver, its-a-feature/Mythic |
| BAS | redcanaryco/atomic-red-team, facebookincubator/TTPForge |
| LLM | NVIDIA/garak, Azure/PyRIT |

## Lab Planning Notes

- Use Kali Linux for operator parity and training, but keep automation portable
- Docker-based toolchain avoids hard dependencies on Kali packages
- Enforce safe lab standards: VM snapshots, network isolation, change windows
