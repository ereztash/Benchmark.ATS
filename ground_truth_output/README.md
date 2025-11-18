# Ground Truth Output Files

This directory contains the "ground truth" reference outputs for the ATS Benchmark.

## What is Ground Truth?

Ground truth files represent **perfect ATS extraction results**. They show exactly what an ideal ATS system should extract from the benchmark resume dataset.

## Contents

- **50 JSON files** (`resume_000.json` through `resume_049.json`)
- Each file corresponds to one resume from `benchmark_resumes_50.json`
- File naming: `resume_XXX.json` where XXX is the zero-padded index (000-049)

## Purpose

Use these files to:

1. **Compare your ATS output** - See how your system compares to perfect extraction
2. **Validate benchmark setup** - Confirm the validation scripts work correctly (should show 100% accuracy)
3. **Understand expected format** - Learn the exact JSON schema your ATS should produce
4. **Debug parsing issues** - Compare your output with ground truth to identify discrepancies

## How to Use

### Validate Against Ground Truth

To confirm the benchmark system is working correctly:

```bash
# From repository root
python3 dist/benchmark_package/bulk_validate.py \
  benchmark_resumes_50.json \
  ground_truth_output/ \
  validation_report.json
```

**Expected result:** 100% accuracy (all 50 resumes perfect)

### Compare Your ATS Output

After running your ATS parser:

```bash
# Validate your ATS results
python3 dist/benchmark_package/bulk_validate.py \
  benchmark_resumes_50.json \
  your_ats_output/ \
  your_validation_report.json
```

Then compare your results with the ground truth validation report.

### Manual Comparison

You can also manually compare individual files:

```bash
# View ground truth for first resume
cat ground_truth_output/resume_000.json

# Compare with your output
diff ground_truth_output/resume_000.json your_ats_output/resume_000.json
```

## File Format

Each ground truth file is a JSON document following the [JSON Resume](https://jsonresume.org/) schema with these main sections:

- `basics` - Name, email, phone, summary, location
- `work` - Employment history
- `education` - Academic credentials
- `skills` - Technical and professional skills
- `languages` - Language proficiencies

## Regenerating Ground Truth

If you need to regenerate these files:

```bash
# From repository root
python3 generate_ground_truth.py
```

This will recreate all 50 ground truth files from `benchmark_resumes_50.json`.

## Notes

- Ground truth files are **identical copies** of the source resumes
- For a perfect ATS system: `extracted_data == source_data`
- Any deviation from ground truth indicates a parsing error
- The validation script allows minor fuzzy matching (85%+) for certain text fields

## See Also

- `../benchmark_resumes_50.json` - Source resume dataset
- `../generate_ground_truth.py` - Script that generated these files
- `../ats_validation_script.py` - Validation logic
- `../README.md` - Main benchmark documentation
