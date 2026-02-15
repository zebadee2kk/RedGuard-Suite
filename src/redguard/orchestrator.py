from redguard.modules import llm_garak, recon, report, scan


def run(config: dict) -> dict:
    modules = config.get("modules", {})
    results = {}

    if modules.get("recon"):
        results["recon"] = recon.run(config)
    if modules.get("scan"):
        results["scan"] = scan.run(config)
    if modules.get("llm_garak"):
        results["llm_garak"] = llm_garak.run(config)
    if modules.get("report"):
        results["report"] = report.run(config, results)

    return results
