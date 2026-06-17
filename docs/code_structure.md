# Code structure

The repository includes a lightweight reusable Python layer under `src/`.

## `src/data_cleaning.py`

Reusable cleaning utilities:

- column-name normalization;
- course-label canonicalization;
- numeric age coercion;
- date parsing;
- public-safe column selection.

## `src/enrollment_analysis.py`

Aggregate enrollment analysis utilities:

- annual enrollment counts;
- course-year matrices;
- course-level change between years;
- age statistics by year;
- age-range distributions;
- course participation percentages.

## `src/geospatial_analysis.py`

Privacy-aware geospatial helpers:

- Haversine distance calculation;
- distance-to-school calculation;
- aggregate distance summaries;
- distance binning;
- categorical frequency tables;
- public spatial-zone summaries.

## `src/visualization.py`

Public-safe visualization helpers:

- annual enrollment bar chart;
- course-year heatmap-style chart;
- categorical frequency bar charts;
- simple HTML table export.

## `src/run_public_analysis.py`

Example command-line runner for anonymized or synthetic datasets.

```bash
python src/run_public_analysis.py \
  --input data/anonymized_enrollment.csv \
  --output outputs
```

The original source datasets are not included in the repository. This script is provided to document how the workflow can be reproduced on safe local data.

## Tests

Minimal tests are included in:

```text
tests/test_enrollment_analysis.py
```

They validate the core aggregate-count and course-change logic.
