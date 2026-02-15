def run(config: dict, results: dict) -> dict:
    summary = {"modules_executed": list(results.keys())}
    return {"status": "ok", "summary": summary}
