# School Enrollment and Geospatial Analysis

Public, privacy-aware methodological pilot connected to my Master's Final Integrative Project in Data Science.

This project transforms historical school enrollment records into aggregate quantitative analysis, geospatial visualization, methodological documentation, reusable Python modules, sanitized notebooks, automated tests, and a GitHub Pages report. It is designed to demonstrate analytical reasoning, reproducible workflow design, responsible publication, and educational-historical data interpretation without exposing raw sensitive records.

## Live project page

[`https://alexisfilosofia.github.io/school-enrollment-geospatial-analysis/`](https://alexisfilosofia.github.io/school-enrollment-geospatial-analysis/)

## Relation to the Master's TFI

This repository should be read as a public pilot, not as the complete thesis repository. The current Master's TFI develops a broader reproducible workflow for historical school archives: inventory, transcription and validation, structured data, quality control, quantitative analysis, geospatial interpretation, privacy-aware publication, and methodological documentation.

The public repository covers part of that trajectory. It shows how archival enrollment tables can be transformed into aggregate analytical outputs, but it intentionally excludes raw row-level records, names, addresses, exact sensitive coordinates, and private working files.

For a detailed mapping between this repository and the TFI workflow, see:

- [`docs/tfi_alignment.md`](docs/tfi_alignment.md)
- [`docs/methodology.md`](docs/methodology.md)
- [`docs/notebook_output_audit.md`](docs/notebook_output_audit.md)

## Public sanitized notebooks

The repository includes clean, reproducible notebooks based on a synthetic/anonymized sample dataset:

- [01 Quantitative Enrollment Analysis](notebooks/01_quantitative_enrollment_analysis_sanitized.ipynb)
- [02 Geospatial Analysis](notebooks/02_geospatial_analysis_sanitized.ipynb)
- [Notebook guide](notebooks/README.md)

These notebooks are public portfolio versions. They do not copy the private working notebooks or publish raw row-level records.

## Project scope

The public workflow consolidates historical enrollment spreadsheets and produces aggregate outputs for educational, institutional, and territorial interpretation.

The notebooks and modules document:

- consolidation of enrollment files from 1910 to 1915;
- normalization of heterogeneous course labels into canonical course categories;
- reconstruction and validation of dates and years;
- age cleaning, descriptive statistics, and cautious outlier review;
- enrollment counts by year and by course;
- age composition by range, year, and course;
- interannual variation in course enrollment;
- approximate distance analysis;
- guardian occupation summaries;
- student and guardian nationality summaries;
- methodological and privacy-aware export decisions.

## Data privacy

The original datasets are not included. This public version includes only:

- reusable Python modules;
- aggregate outputs;
- a synthetic/anonymized sample dataset;
- sanitized public notebooks;
- selected figures exported from the working notebooks;
- methodological documentation;
- a static web page for portfolio review.

No raw archival row-level dataset is published in this repository.

The public representation intentionally excludes or avoids direct publication of:

- raw Excel files;
- row-level enrollment tables;
- student names;
- guardian/family names;
- raw addresses;
- exact coordinates tied to individual records;
- maps that combine individual point locations with sensitive categories;
- private Google Drive paths and working-folder structures.

## Notebook-derived public snapshot

The quantitative pilot consolidates `1,408` records and `22` columns across six enrollment files. Course labels are normalized into:

```text
1º Año, 2º Año, 3º Año, 4º Año, 5º Año, 6º Año
```

Annual enrollment records increase from `155` in 1910 to `355` in 1915.

| Year | Records |
|---:|---:|
| 1910 | 155 |
| 1911 | 182 |
| 1912 | 183 |
| 1913 | 216 |
| 1914 | 317 |
| 1915 | 355 |

The course-year table shows a strong concentration in `1º Año`, especially from 1914 onward.

| Year | 1º Año | 2º Año | 3º Año | 4º Año | 5º Año | 6º Año |
|---:|---:|---:|---:|---:|---:|---:|
| 1910 | 44 | 22 | 21 | 12 | 35 | 21 |
| 1911 | 46 | 24 | 15 | 22 | 32 | 21 |
| 1912 | 67 | 30 | 21 | 14 | 38 | 13 |
| 1913 | 69 | 43 | 24 | 17 | 53 | 10 |
| 1914 | 126 | 45 | 45 | 19 | 66 | 15 |
| 1915 | 139 | 78 | 45 | 40 | 38 | 15 |

The geospatial notebook reports `323` geocoded cases, `77` spatial zones, an approximate mean distance of `3.12 km`, and a median distance of `2.34 km`. These figures are presented as aggregate outputs, not as a public individual-level geocoded dataset.

## Reusable Python code

The repository includes a lightweight `src/` layer that translates the Colab workflow into reusable Python modules:

- `src/data_cleaning.py` — column normalization, course canonicalization, age coercion, date parsing, and public-safe column selection.
- `src/enrollment_analysis.py` — annual counts, course-year matrices, age statistics, age ranges, and course-level change.
- `src/geospatial_analysis.py` — distance calculations, distance summaries, frequency tables, and spatial-zone summaries.
- `src/visualization.py` — public-safe chart and HTML table exports.
- `src/run_public_analysis.py` — command-line runner for anonymized or synthetic CSV files.

The original sensitive datasets are not included, so the runner is intended for anonymized, synthetic, or locally provided data with equivalent columns.

## Reproducing the public sample analysis

Install the project dependencies, then run the public analysis script against the synthetic/anonymized sample dataset:

```bash
python src/run_public_analysis.py \
  --input data/sample_anonymized_enrollment.csv \
  --output outputs
```

This command writes reproducible aggregate outputs to `outputs/` using the public synthetic/anonymized sample dataset.

## Repository structure

```text
school-enrollment-geospatial-analysis/
├── index.html
├── styles.css
├── README.md
├── requirements.txt
├── LICENSE
├── .github/workflows/tests.yml
├── assets/
├── data/
├── docs/
│   ├── methodology.md
│   ├── notebook_output_audit.md
│   ├── code_structure.md
│   ├── github_pages_setup.md
│   └── tfi_alignment.md
├── notebooks/
├── outputs/
├── src/
└── tests/
```

## Professional relevance

Although the case is historical and educational, the workflow demonstrates transferable skills: messy data ingestion, data validation, uncertainty-aware interpretation, documentation, Python-based analysis, privacy-aware publication, geospatial reasoning, testing, and reproducible reporting. These capacities are relevant to AI evaluation, educational analytics, technical QA, research support, data analysis, and public-facing analytical communication.
