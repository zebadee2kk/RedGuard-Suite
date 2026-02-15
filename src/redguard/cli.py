import argparse
import json
from pathlib import Path

from redguard.orchestrator import run


def main() -> int:
    parser = argparse.ArgumentParser(description="RedGuard Suite (public) CLI")
    parser.add_argument(
        "--config",
        default=str(Path("configs") / "config.public.example.json"),
        help="Path to a JSON configuration file",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    config = json.loads(config_path.read_text(encoding="utf-8"))

    run(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
