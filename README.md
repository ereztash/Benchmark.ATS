# ATS Benchmark Dataset — Quick Start

Purpose: a ready-to-run benchmark for testing ATS parsing and extraction accuracy.

Key files (repo root):
- `benchmark_resumes_50.json` — main dataset (50 resumes)
- `edge_case_resumes.json` — 8 edge-case resumes
- `ats_validation_script.py` — validation script (Python 3.7+)
- `generate_ground_truth.py` — script to generate perfect reference outputs
- `ground_truth_output/` — 50 perfect ATS extraction examples (ground truth)
- `implementation_guide_he.md` — Hebrew implementation guide
- `dist/benchmark_package/` — distributable package with helpers and README

Quick prerequisites:
- Python 3.7 or later
- An ATS that can import JSON resumes and export parsed results as JSON

Quick run steps:

1. Place `benchmark_resumes_50.json` where your ATS can import it.

2. Import into your ATS and verify all 50 resumes were imported successfully.

3. Run your ATS parsing/extraction on the imported resumes and export the parsed outputs
   as one JSON file per resume into `dist/benchmark_package/ats_output/`.

4. Validate results (package flow):

```bash
cd dist/benchmark_package
./run_benchmark.sh
```

Or run the bulk validator directly:

```bash
cd dist/benchmark_package
python3 bulk_validate.py ../../benchmark_resumes_50.json ats_output/ validation_report.json
```

Outputs:
- `dist/benchmark_package/validation_report.json` — aggregated accuracy report with per-field metrics and recommendations.

## Ground Truth Reference

This repository includes **ground truth** files — perfect ATS extraction outputs that you can use as a reference:

```bash
# View the ground truth files (50 perfect examples)
ls ground_truth_output/

# Verify ground truth is perfect (should show 100% accuracy)
python3 dist/benchmark_package/bulk_validate.py \
  benchmark_resumes_50.json ground_truth_output/ ground_truth_validation.json

# Compare your ATS output against ground truth manually
diff ground_truth_output/resume_000.json your_ats_output/resume_000.json
```

To regenerate ground truth files:

```bash
python3 generate_ground_truth.py
```

See `ground_truth_output/README.md` for detailed documentation.

## Packaging for Distribution

Packaging for distribution (already included in this repo):
- `benchmark_package.zip` — zip of `dist/benchmark_package/` placed at repo root (if present).

Developer notes:
- `ats_validation_script.py` exposes `ResumeValidator` and `BenchmarkRunner` classes for programmatic use.
- Schema and dataset details are in `benchmark_documentation.json`.

If you want, I can:
- create example ATS extraction stubs so you can test `bulk_validate.py` immediately,
- or regenerate the `benchmark_package.zip` with additional files.
