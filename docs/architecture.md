# Architecture Overview

## System Design

RedGuard Suite follows a **modular, pipeline-based architecture** where each attack phase is an independent module orchestrated by a central engine.

```
┌─────────────────────────────────────────────────────────┐
│                     CLI (cli.py)                         │
│              User interface / entry point                │
└──────────────────────┬──────────────────────────────────┘
                       │ config
                       ▼
┌─────────────────────────────────────────────────────────┐
│                 Orchestrator (orchestrator.py)            │
│          Reads config → sequences modules → collects     │
│          results → passes to report engine                │
└──┬──────┬──────┬──────┬──────┬──────┬───────────────────┘
   │      │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼      ▼
┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐
│Recon││Scan ││Expl.││ C2  ││Garak││ ... │  ← Modules
└──┬──┘└──┬──┘└──┬──┘└──┬──┘└──┬──┘└──┬──┘
   │      │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼      ▼
┌─────────────────────────────────────────────────────────┐
│              Report Engine (report.py)                    │
│     Aggregates findings → scores risk → generates        │
│     executive report + ATT&CK heatmap                    │
└─────────────────────────────────────────────────────────┘
```

## Module Interface Contract

Every module must implement:

```python
def run(config: dict) -> dict:
    """
    Execute this attack phase.

    Args:
        config: Full configuration dict including targets, safety, and module-specific settings.

    Returns:
        dict with at minimum:
            - "status": "ok" | "skipped" | "error"
            - "detail": Human-readable description
            - "findings": list[dict] (optional, for modules that produce findings)
    """
```

The report module has an extended signature:

```python
def run(config: dict, results: dict) -> dict:
    """
    Generate report from all module results.

    Args:
        config: Full configuration dict.
        results: Dict of {module_name: module_result} from prior phases.
    """
```

## Configuration Structure

```json
{
  "targets": ["example.com"],
  "modules": {
    "recon": true,
    "scan": true,
    "exploit": false,
    "c2": false,
    "llm_garak": false,
    "report": true
  },
  "safety": {
    "dry_run": true,
    "stop_on_prod": true,
    "allowed_networks": ["10.0.0.0/24"],
    "max_rate": 100
  },
  "risk_matrix": {
    "impact_levels": ["Low", "Medium", "High", "Critical"],
    "likelihood_levels": ["Rare", "Possible", "Likely", "Almost Certain"]
  },
  "reporting": {
    "output_dir": "reports/",
    "format": ["json", "markdown"],
    "include_attack_navigator": true
  }
}
```

## Data Flow

1. **Config loading** — CLI reads JSON config, validates with Pydantic schema
2. **Safety checks** — Orchestrator verifies targets are in `allowed_networks`, `dry_run` state, etc.
3. **Module execution** — Each enabled module runs in sequence; results accumulate
4. **Finding aggregation** — Report engine collects all findings, scores via risk matrix
5. **Output generation** — Produces JSON findings + Markdown executive report + ATT&CK heatmap

## Safety Architecture

```
                    ┌──────────────────┐
                    │   Config Loader   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Safety Validator │ ← Checks before ANY module runs
                    │  - dry_run flag   │
                    │  - network scope  │
                    │  - prod detection │
                    │  - rate limits    │
                    └────────┬─────────┘
                             │ PASS
                    ┌────────▼─────────┐
                    │   Module Runner   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Per-Module Guard │ ← Each module re-checks scope
                    └──────────────────┘
```

Safety is enforced at two layers:
1. **Orchestrator level**: Validates config before any module executes
2. **Module level**: Each module independently checks `dry_run` and scope before network operations

## Planned Module Roadmap

| Module           | ATT&CK Phase        | Tool Integration     | Status    |
|-----------------|---------------------|----------------------|-----------|
| `recon`         | Reconnaissance      | ReconFTW, Amass      | Stub      |
| `scan`          | Discovery           | Nuclei, Nmap         | Stub      |
| `exploit`       | Initial Access      | Metasploit           | Planned   |
| `c2`            | Command & Control   | Sliver, Mythic       | Planned   |
| `phishing`      | Initial Access      | Gophish              | Planned   |
| `atomic`        | Execution           | Atomic Red Team      | Planned   |
| `llm_garak`     | ML Attack (ATLAS)   | Garak                | Stub      |
| `lateral`       | Lateral Movement    | Custom               | Planned   |
| `exfil`         | Exfiltration        | Custom               | Planned   |
| `report`        | N/A                 | DefectDojo, LLM      | Stub      |

## Repo Separation (Public vs Internal)

```
public/ (GitHub)              internal/ (Private Git)
├── Generic framework code    ├── Company configs (encrypted)
├── Module interfaces         ├── Real target data
├── Example configs           ├── Custom modules
├── Safe stubs                ├── Engagement reports
└── Community docs            └── Signed RoE documents
```

The internal repo imports the public package and overlays company-specific configuration. No code flows from internal → public.
