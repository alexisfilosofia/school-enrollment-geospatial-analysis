# Data folder

This folder contains a public-safe sample dataset derived from the structure and aggregate distributions of the historical enrollment spreadsheets.

## Included file

```text
sample_anonymized_enrollment.csv
```

The sample contains 180 records: 30 synthetic/anonymized records for each registry year from 1910 to 1915.

The original Excel files are not included in this repository.

## Why this is anonymized / synthetic

Even though the original records are historical, the public repository uses an anonymized sample for portfolio purposes. The sample preserves analytical structure while avoiding publication of direct names and addresses.

The file keeps useful analytical variables such as:

- registry year;
- enrollment date;
- canonical course;
- age and age range;
- grouped student nationality;
- grouped guardian nationality;
- grouped guardian occupation;
- origin group;
- repeat flag;
- approximate synthetic distance to school;
- synthetic spatial zone.

## Columns

| Column | Description |
|---|---|
| `synthetic_student_id` | Public-safe synthetic identifier. |
| `registry_year` | Year of the enrollment book. |
| `enrollment_date` | Enrollment date normalized to the registry year. |
| `course` | Canonical course label. |
| `age` | Student age as a numeric value. |
| `age_range` | Public age range used in the analysis. |
| `student_nationality_group` | Normalized student nationality group. |
| `guardian_nationality_group` | Normalized guardian nationality group. |
| `guardian_occupation_group` | Grouped guardian occupation category. |
| `origin_group` | Grouped origin/procedencia category. |
| `repeat_flag` | Boolean indicator derived from observations mentioning repetition. |
| `approx_distance_km` | Synthetic approximate distance to school in kilometers. |
| `synthetic_spatial_zone` | Synthetic spatial zone identifier. |

## Important note

This dataset is intended for reproducing the public code examples and demonstrating the analytical workflow. It should not be treated as the original archival dataset.
