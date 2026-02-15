from redguard.orchestrator import run


def test_run_returns_dict(sample_config):
    result = run(sample_config)
    assert isinstance(result, dict)


def test_run_executes_enabled_modules(sample_config):
    result = run(sample_config)
    assert "recon" in result
    assert "scan" in result
    assert "report" in result


def test_run_skips_disabled_modules(sample_config):
    result = run(sample_config)
    assert "llm_garak" not in result


def test_run_empty_modules():
    config = {"targets": ["example.com"], "modules": {}}
    result = run(config)
    assert result == {}
