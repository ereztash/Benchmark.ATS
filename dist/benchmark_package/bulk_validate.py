#!/usr/bin/env python3
"""
Bulk validation helper that uses `ats_validation_script.py` classes.

Usage:
  python3 bulk_validate.py benchmark_resumes_50.json ats_output/ validation_report.json

The script will:
 - Load source resumes from the given source file
 - Read all JSON files from the `ats_output/` directory (sorted)
 - Pair each extracted file with the corresponding source resume by index
 - Run validation for each pair and produce an aggregated report
"""
import json
import sys
import os
from typing import List

try:
    import ats_validation_script as validator_module
except Exception:
    print("Error: cannot import ats_validation_script.py. Ensure it is in the same folder or on PYTHONPATH.")
    raise


def load_extracted_files(output_dir: str) -> List[str]:
    files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith('.json')]
    files.sort()
    return files


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 bulk_validate.py source_resumes.json ats_output_dir/ output_report.json")
        sys.exit(1)

    source_file = sys.argv[1]
    output_dir = sys.argv[2]
    report_file = sys.argv[3]

    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        sys.exit(1)

    if not os.path.isdir(output_dir):
        print(f"ATS output directory not found: {output_dir}")
        sys.exit(1)

    runner = validator_module.BenchmarkRunner(source_file)
    extracted_files = load_extracted_files(output_dir)

    if not extracted_files:
        print(f"No extracted JSON files found in {output_dir}")
        sys.exit(1)

    total = min(len(runner.resumes), len(extracted_files))
    if len(runner.resumes) != len(extracted_files):
        print(f"Warning: source resumes = {len(runner.resumes)}, extracted files = {len(extracted_files)}. Will validate {total} pairs.")

    validation_results = []

    for i in range(total):
        extracted_path = extracted_files[i]
        try:
            with open(extracted_path, 'r', encoding='utf-8') as f:
                extracted_data = json.load(f)
        except Exception as e:
            print(f"Failed to load extracted file {extracted_path}: {e}")
            continue

        result = runner.validate_resume(i, extracted_data)
        validation_results.append(result)

    report = runner.generate_report(validation_results)

    with open(report_file, 'w', encoding='utf-8') as outf:
        json.dump(report, outf, ensure_ascii=False, indent=2)

    print(f"Validation complete. Report written to {report_file}")


if __name__ == '__main__':
    main()
