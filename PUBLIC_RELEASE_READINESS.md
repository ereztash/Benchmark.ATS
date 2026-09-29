# Public Release Readiness

Status: **PUBLIC SOURCE / LICENSE + DATA PROVENANCE REVIEW REQUIRED**

This repository has a clear public utility: a small, runnable ATS parsing benchmark with reference outputs and validation scripts. Before calling it open source, two separate rights questions must be explicit: the code license and the dataset/content license.

## Public value

A stranger can use the project to:

- import a fixed resume corpus into an ATS;
- export parsed results;
- compare them with reference outputs;
- get per-field accuracy results;
- reproduce the benchmark locally.

That makes the repository potentially more useful than a general ATS demo because it provides a test harness rather than only an implementation.

## Evidence boundary

"Ground truth" here means the repository's reference extraction for the included benchmark cases. It should not be interpreted as evidence that the benchmark represents real-world hiring distributions, languages, document formats, or production ATS performance.

## Before OSS spotlight

1. **Code license** — add an explicit root license.
2. **Dataset provenance/license** — document whether every resume is synthetic, transformed, permissioned, or otherwise redistributable.
3. **Benchmark contract** — state exactly which fields count toward accuracy, how partial matches are scored, and what is excluded.
4. **One command** — reduce the default path to a single reproducible benchmark command if possible.

## Public one-liner

> A small reproducible benchmark for testing ATS resume extraction against fixed reference outputs instead of judging parsers by demos.

## Do not claim

- industry representativeness without a sampling study;
- production accuracy from the included corpus alone;
- "perfect" ground truth beyond the benchmark's own extraction schema.
