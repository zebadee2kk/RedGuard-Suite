from redguard.modules.report import run


def test_report_returns_summary(sample_config):
    mock_results = {"recon": {"status": "ok"}, "scan": {"status": "ok"}}
    result = run(sample_config, mock_results)
    assert result["status"] == "ok"
    assert "modules_executed" in result["summary"]
    assert set(result["summary"]["modules_executed"]) == {"recon", "scan"}
