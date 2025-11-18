#!/usr/bin/env python3
"""
Generate Ground Truth Output Files

This script creates perfect ATS extraction outputs from the benchmark resume dataset.
These files serve as the "ground truth" reference for comparing ATS parsing accuracy.

For a perfect ATS system, the extracted data should match the source data exactly.
"""

import json
import os
import sys
from pathlib import Path


def generate_ground_truth(source_file: str, output_dir: str):
    """
    Generate ground truth files from source resumes.

    Args:
        source_file: Path to benchmark_resumes_50.json
        output_dir: Directory to write ground truth files
    """
    # Load source resumes
    with open(source_file, 'r', encoding='utf-8') as f:
        resumes = json.load(f)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating ground truth for {len(resumes)} resumes...")

    # Generate a file for each resume
    for idx, resume in enumerate(resumes):
        # Create filename: resume_000.json, resume_001.json, etc.
        filename = f"resume_{idx:03d}.json"
        output_path = os.path.join(output_dir, filename)

        # Write the resume data as-is (perfect extraction)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(resume, f, ensure_ascii=False, indent=2)

        if (idx + 1) % 10 == 0:
            print(f"  Generated {idx + 1}/{len(resumes)} files...")

    print(f"\n✓ Successfully generated {len(resumes)} ground truth files in: {output_dir}")
    print(f"\nYou can now test your ATS system by:")
    print(f"  1. Running your ATS parser on benchmark_resumes_50.json")
    print(f"  2. Exporting your ATS results to a directory (e.g., my_ats_output/)")
    print(f"  3. Running validation:")
    print(f"     python3 dist/benchmark_package/bulk_validate.py \\")
    print(f"       benchmark_resumes_50.json my_ats_output/ validation_report.json")
    print(f"\nOr compare against this perfect ground truth:")
    print(f"     python3 dist/benchmark_package/bulk_validate.py \\")
    print(f"       benchmark_resumes_50.json {output_dir}/ validation_report.json")
    print(f"     (Should show 100% accuracy)")


def main():
    # Default paths
    script_dir = Path(__file__).parent
    source_file = script_dir / "benchmark_resumes_50.json"
    output_dir = script_dir / "ground_truth_output"

    # Allow command-line arguments
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    if not os.path.exists(source_file):
        print(f"Error: Source file not found: {source_file}")
        print(f"\nUsage: {sys.argv[0]} [source_file] [output_dir]")
        print(f"  source_file: Path to benchmark_resumes_50.json (default: ./benchmark_resumes_50.json)")
        print(f"  output_dir:  Output directory (default: ./ground_truth_output)")
        sys.exit(1)

    generate_ground_truth(str(source_file), str(output_dir))


if __name__ == "__main__":
    main()
