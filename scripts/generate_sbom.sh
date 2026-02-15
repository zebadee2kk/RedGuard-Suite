#!/usr/bin/env bash
# Generate a Software Bill of Materials (SBOM) for the project.
# Requires: pip-licenses (pip install pip-licenses)
# Usage: ./scripts/generate_sbom.sh
set -euo pipefail

OUTPUT_DIR="${1:-reports}"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")
SBOM_FILE="${OUTPUT_DIR}/sbom-${TIMESTAMP}.json"

mkdir -p "$OUTPUT_DIR"

echo "Generating SBOM..."
pip-licenses --format=json --with-urls --with-license-file --no-license-path \
    --output-file="$SBOM_FILE"

echo "SBOM written to: $SBOM_FILE"
echo "Package count: $(python -c "import json; print(len(json.load(open('$SBOM_FILE'))))")"
