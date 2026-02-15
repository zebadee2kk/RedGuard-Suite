# Module Development Guide

This guide explains how to create new attack phase modules for RedGuard Suite.

## Module Structure

Each module is a Python file in `src/redguard/modules/` that implements the standard interface.

### Minimal Module

```python
"""
Module: example_phase
ATT&CK Mapping: T1595 - Active Scanning
Phase: Reconnaissance
"""
from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def run(config: dict[str, Any]) -> dict[str, Any]:
    """Execute the example phase.

    Args:
        config: Full engagement configuration.

    Returns:
        Result dict with status, detail, and optional findings.
    """
    # Safety check: always respect dry_run
    dry_run = config.get("safety", {}).get("dry_run", True)
    targets = config.get("targets", [])

    if not targets:
        return {"status": "skipped", "detail": "No targets configured"}

    findings: list[dict[str, Any]] = []

    for target in targets:
        if dry_run:
            logger.info("DRY RUN: Would scan %s", target)
            continue

        # Actual scanning logic here
        logger.info("Scanning %s", target)
        # ... tool integration ...

    return {
        "status": "ok" if not dry_run else "dry_run",
        "detail": f"Processed {len(targets)} target(s)",
        "findings": findings,
    }
```

## Step-by-Step: Adding a New Module

### 1. Create the Module File

```bash
touch src/redguard/modules/lateral_movement.py
```

### 2. Implement the Interface

Follow the template above. Key requirements:
- Must have a `run(config: dict) -> dict` function
- Must return `{"status": str, "detail": str}` at minimum
- Must check `config["safety"]["dry_run"]` before any network operations
- Must validate targets are within `config["safety"]["allowed_networks"]` if applicable

### 3. Register in the Orchestrator

Edit `src/redguard/orchestrator.py`:

```python
from redguard.modules import lateral_movement  # Add import

def run(config: dict) -> dict:
    modules = config.get("modules", {})
    results = {}

    # ... existing modules ...

    if modules.get("lateral_movement"):              # Add block
        results["lateral_movement"] = lateral_movement.run(config)

    # Report must always run last
    if modules.get("report"):
        results["report"] = report.run(config, results)

    return results
```

### 4. Write Tests

Create `tests/modules/test_lateral_movement.py`:

```python
from redguard.modules.lateral_movement import run


def test_returns_required_fields(sample_config):
    result = run(sample_config)
    assert "status" in result
    assert "detail" in result


def test_dry_run_mode(sample_config):
    sample_config["safety"]["dry_run"] = True
    result = run(sample_config)
    assert result["status"] in ("dry_run", "skipped")


def test_skips_without_targets():
    config = {"targets": [], "modules": {}, "safety": {"dry_run": True}}
    result = run(config)
    assert result["status"] == "skipped"
```

### 5. Update Config Schema

Add the module to `configs/config.public.example.json`:

```json
{
  "modules": {
    "lateral_movement": false
  }
}
```

### 6. Document ATT&CK Mapping

Update `docs/attack_mapping.md` with the technique coverage.

## Integrating External Tools

Many modules wrap external security tools. Use `subprocess` with safety:

```python
import subprocess
import shlex


def _run_tool(command: list[str], timeout: int = 300) -> subprocess.CompletedProcess:
    """Run an external tool with safety constraints."""
    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,  # Don't raise on non-zero exit; we handle errors
    )
```

### Tool Wrapper Pattern

```python
def run(config: dict) -> dict:
    dry_run = config.get("safety", {}).get("dry_run", True)

    if dry_run:
        return {"status": "dry_run", "detail": "Would run nuclei scan"}

    targets = config.get("targets", [])
    all_findings = []

    for target in targets:
        result = _run_tool(["nuclei", "-u", target, "-json", "-silent"])

        if result.returncode != 0:
            logger.error("nuclei failed for %s: %s", target, result.stderr)
            continue

        # Parse tool output into standard finding format
        for line in result.stdout.strip().splitlines():
            finding = _parse_nuclei_finding(line)
            if finding:
                all_findings.append(finding)

    return {
        "status": "ok",
        "detail": f"Scanned {len(targets)} targets; found {len(all_findings)} issues",
        "findings": all_findings,
    }
```

## Finding Format

All findings should use this schema for consistency with the report engine:

```python
finding = {
    "finding_id": "RG-2026-XXX",       # Auto-generated or manual
    "title": "Short description",
    "description": "Detailed explanation",
    "attack_technique": "T1190",         # MITRE ATT&CK technique ID
    "impact": 3,                         # 1-4
    "likelihood": 4,                     # 1-4
    "exploitability": 3,                 # 1-4
    "affected_assets": ["target.com"],
    "evidence": "path/to/screenshot.png",
    "remediation": "How to fix this",
    "references": ["https://..."],
}
```

## Testing Checklist

Before submitting a PR for a new module:

- [ ] `run()` function implemented with correct signature
- [ ] Returns `{"status", "detail"}` in all code paths
- [ ] Respects `dry_run` flag (no network calls when True)
- [ ] Validates `allowed_networks` for network-touching operations
- [ ] Handles missing/empty targets gracefully
- [ ] Handles tool failures (non-zero exit, timeout) gracefully
- [ ] Unit tests cover: happy path, dry run, no targets, tool failure
- [ ] `ruff check` passes
- [ ] `mypy` passes with type annotations
- [ ] ATT&CK technique documented
