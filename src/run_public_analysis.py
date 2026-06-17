"""Example public-safe analysis runner.

This script shows how the reusable modules can be combined on an anonymized or
synthetic dataset. The original sensitive datasets are not included in the public
repository.

Usage example:

    python src/run_public_analysis.py --input data/anonymized_enrollment.csv --output outputs

Expected minimum columns can be adapted with command-line arguments.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data_cleaning import add_canonical_course_column, coerce_numeric_age, normalize_columns
from enrollment_analysis import (
    DEFAULT_COURSE_ORDER,
    age_statistics_by_year,
    annual_enrollment_counts,
    course_change_between_years,
    course_year_matrix,
)
from visualization import export_table_html, save_annual_enrollment_chart, save_course_matrix_heatmap


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run public-safe enrollment analysis on anonymized data.")
    parser.add_argument("--input", required=True, help="Path to an anonymized CSV file.")
    parser.add_argument("--output", default="outputs", help="Directory where aggregate outputs will be written.")
    parser.add_argument("--year-column", default="anio_libro", help="Registry year column name after normalization.")
    parser.add_argument("--course-column", default="curso", help="Course column name after normalization.")
    parser.add_argument("--age-column", default="edad", help="Age column name after normalization.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    df = normalize_columns(df)

    if args.course_column in df.columns:
        df = add_canonical_course_column(df, args.course_column)
        course_column = "curso_canonico"
    else:
        course_column = args.course_column

    if args.age_column in df.columns:
        df = coerce_numeric_age(df, args.age_column)
        age_column = "edad_num"
    else:
        age_column = args.age_column

    annual = annual_enrollment_counts(df, args.year_column)
    annual.to_csv(output_dir / "annual_enrollment_counts.csv", index=False)
    save_annual_enrollment_chart(annual, args.year_column, "records", output_dir / "annual_enrollment_counts.png")

    matrix = course_year_matrix(df, args.year_column, course_column, DEFAULT_COURSE_ORDER)
    matrix.to_csv(output_dir / "course_year_matrix.csv", index=False)
    export_table_html(matrix, output_dir / "course_year_matrix.html", title="Course-year matrix")
    save_course_matrix_heatmap(matrix, args.year_column, output_dir / "course_year_matrix.png")

    try:
        change = course_change_between_years(matrix, args.year_column, int(annual[args.year_column].min()), int(annual[args.year_column].max()))
        change.to_csv(output_dir / "course_change.csv", index=False)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not compute course change table: {exc}")

    if age_column in df.columns:
        ages = age_statistics_by_year(df, args.year_column, age_column)
        ages.to_csv(output_dir / "age_statistics_by_year.csv", index=False)

    print(f"Public-safe aggregate outputs written to: {output_dir}")


if __name__ == "__main__":
    main()
