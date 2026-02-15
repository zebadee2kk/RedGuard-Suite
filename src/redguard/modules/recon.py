def run(config: dict) -> dict:
    targets = config.get("targets", [])
    return {"status": "skipped", "detail": f"Recon stub for {len(targets)} target(s)"}
