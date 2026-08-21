# TFI alignment note

This document explains how the public `school-enrollment-geospatial-analysis` repository relates to the broader Master's Final Integrative Project in Data Science.

## General position

The repository is a public, privacy-aware methodological pilot. It should not be read as the complete thesis repository, nor as a raw data release. Its role is to show that historical school enrollment records can be transformed into documented, aggregate, reproducible, and communicable analytical outputs.

The broader TFI develops a more complete workflow: from source inventory and transcription/validation to structured datasets, quality control, quantitative analysis, geospatial interpretation, public artifacts, and methodological writing.

## Alignment matrix

| TFI component | Current public coverage | Missing or planned work |
|---|---|---|
| Source inventory | Partial; public repo documents processed files and sanitized samples. | Stable manifest, checksums, source IDs, image/folio mapping, and archival-quality metadata. |
| Transcription and validation | Not included as a full public process. | Ground-truth sample, human validation protocol, HTR/AI benchmark, field-level error analysis, and correction-time metrics. |
| Data model | Partial; public sample columns and cleaning modules exist. | Formal schema, codebook, original/normalized field distinction, uncertainty fields, and release versioning. |
| ETL and cleaning | Present in reusable Python modules and notebooks. | Stronger quality gates, configuration files, reproducible run manifests, and tests for field ranges, dates, years, and mappings. |
| Quantitative analysis | Present for the public 1910-1915 pilot. | Extension to the final research scope, frozen analysis plan, sensitivity checks, and claim registry. |
| Geospatial analysis | Present as aggregate distance/spatial-zone outputs. | Historical gazetteer, precision categories, validation of geocoding candidates, uncertainty-aware mapping, and exclusion rules. |
| Privacy and publication | Strong public-safe orientation: no raw names, addresses, or sensitive coordinates. | Formal publication protocol and final distinction between private, restricted, and public artifacts. |
| Reproducibility | Partial; modules, notebooks, tests, requirements, and outputs are included. | Orchestration, environment lockfile, run manifests, dependency graph, and clean re-execution audit. |
| Transferability | Suggested but not fully tested. | Test on a held-out subset, additional year, or comparable book without silently changing rules. |
| Thesis writing | Not included as manuscript text. | Methods, results, discussion, limitations, reproducibility appendix, and final defense materials. |

## Current public value

The public pilot already demonstrates several transferable capacities:

- converting messy historical/institutional spreadsheets into structured analytical outputs;
- documenting privacy boundaries and publication decisions;
- separating public demonstration artifacts from sensitive working materials;
- translating notebook work into reusable modules, tests, and a readable public report;
- combining quantitative analysis with geospatial interpretation;
- communicating technical results for a broader audience.

## Methodological principles to preserve

1. **Do not overwrite source uncertainty.** Original values, validated readings, normalized values, and analytical categories should remain conceptually distinct.
2. **Do not treat notebook outputs as self-justifying evidence.** Every public table or figure should be linked to an input, script, parameter set, and version.
3. **Do not publish sensitive records for portfolio visibility.** Public demonstration should remain aggregate, synthetic, anonymized, or methodological.
4. **Do not force historical data into present-day categories without documentation.** Especially for addresses, localities, nationalities, occupations, and course labels.
5. **Do not repair final figures manually.** Errors should be corrected at the source layer that produced them, then regenerated forward.

## Suggested next repository improvements

- Add a `metadata/` folder with a public-safe sample manifest.
- Add `docs/data_dictionary.md` for public sample fields and conceptual distinctions.
- Add `docs/quality_gates.md` documenting checks for years, ages, course mappings, missingness, and geocoding precision.
- Add a small `reports/` folder with reproducibility or audit summaries.
- Add badges for tests, Python version, and GitHub Pages.
- Add a roadmap distinguishing public portfolio work from private thesis work.

## Professional positioning

The repository should support a broad professional profile rather than lock the author into a single niche. The project is useful evidence for AI evaluation, data analysis, research support, educational analytics, documentation, technical QA, Python workflows, dashboarding, and reproducible analytical communication.
