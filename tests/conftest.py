import json
from pathlib import Path

import pytest


@pytest.fixture()
def sample_config() -> dict:
    """Minimal valid config for testing."""
    return {
        "targets": ["example.com"],
        "modules": {
            "recon": True,
            "scan": True,
            "llm_garak": False,
            "report": True,
        },
        "safety": {
            "dry_run": True,
            "stop_on_prod": True,
        },
        "risk_matrix": {
            "impact_levels": ["Low", "Medium", "High", "Critical"],
            "likelihood_levels": ["Rare", "Possible", "Likely", "Almost Certain"],
        },
    }


@pytest.fixture()
def config_file(tmp_path: Path, sample_config: dict) -> Path:
    """Write sample config to a temp file and return its path."""
    p = tmp_path / "config.json"
    p.write_text(json.dumps(sample_config), encoding="utf-8")
    return p
