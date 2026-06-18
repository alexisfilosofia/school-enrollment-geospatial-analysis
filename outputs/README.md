# Generated Public Sample Outputs

These files are generated from `data/sample_anonymized_enrollment.csv`, a synthetic/anonymized public sample dataset. They are not generated from the raw historical source files.

Reproduce them from the repository root with:

```bash
python src/run_public_analysis.py \
  --input data/sample_anonymized_enrollment.csv \
  --output outputs
```

Generated text outputs committed to this repository:

- `annual_enrollment_counts.csv`
- `course_year_matrix.csv`
- `course_change.csv`
- `age_statistics_by_year.csv`
- `course_year_matrix.html`

The command also writes chart PNG files locally. They are reproducible artifacts from the same synthetic/anonymized sample dataset.
