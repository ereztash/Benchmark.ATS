#!/usr/bin/env bash
# Run the benchmark end-to-end (assumes files are in current directory)
# Usage: ./run_benchmark.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_RESUMES="${ROOT_DIR}/../../benchmark_resumes_50.json"
OUTPUT_DIR="${ROOT_DIR}/ats_output"
REPORT_FILE="${ROOT_DIR}/validation_report.json"

echo "Benchmark runner — quick flow"

if [ ! -f "$SOURCE_RESUMES" ]; then
  echo "Error: source resumes not found at $SOURCE_RESUMES"
  echo "Place benchmark_resumes_50.json two levels up from this script, or adjust the script."
  exit 1
fi

if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Creating ats_output/ — please copy your ATS extracted JSON files into this folder (one JSON per resume)."
  mkdir -p "$OUTPUT_DIR"
  echo "When ready, re-run this script to validate."
  exit 0
fi

echo "Running bulk validation..."
python3 "$ROOT_DIR/bulk_validate.py" "$SOURCE_RESUMES" "$OUTPUT_DIR" "$REPORT_FILE"

echo "Done. Report: $REPORT_FILE"
echo "Tip: zip the package for distribution: 'zip -r benchmark_package.zip . -x \*/__pycache__\*'"
