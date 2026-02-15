from redguard.modules.recon import run


def test_recon_returns_status(sample_config):
    result = run(sample_config)
    assert "status" in result
    assert "detail" in result


def test_recon_reports_target_count(sample_config):
    result = run(sample_config)
    assert "1 target(s)" in result["detail"]
