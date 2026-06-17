"""Aggregate enrollment analysis utilities.

The functions in this module reproduce the main aggregate outputs used in the
portfolio page: annual counts, course-year matrices, course-level change, and
age statistics by registry year.
"""

from __future__ import annotations

import pandas as pd


DEFAULT_COURSE_ORDER = ["1º Año", "2º Año", "3º Año", "4º Año", "5º Año", "6º Año"]


def annual_enrollment_counts(df: pd.DataFrame, year_column: str) -> pd.DataFrame:
    """Compute student record counts by registry year."""
    result = (
        df.dropna(subset=[year_column])
        .groupby(year_column)
        .size()
        .rename("records")
        .reset_index()
        .sort_values(year_column)
    )
    return result


def course_year_matrix(
    df: pd.DataFrame,
    year_column: str,
    course_column: str,
    course_order: list[str] | None = None,
) -> pd.DataFrame:
    """Build a year-by-course enrollment matrix."""
    matrix = pd.crosstab(df[year_column], df[course_column])
    matrix.index.name = year_column

    if course_order is not None:
        matrix = matrix.reindex(columns=course_order, fill_value=0)

    return matrix.reset_index()


def course_change_between_years(
    matrix: pd.DataFrame,
    year_column: str,
    start_year: int,
    end_year: int,
) -> pd.DataFrame:
    """Compute absolute and relative course-level change between two years."""
    indexed = matrix.set_index(year_column)

    start = indexed.loc[start_year]
    end = indexed.loc[end_year]

    result = pd.DataFrame(
        {
            "course": start.index,
            "start_year_count": start.values,
            "end_year_count": end.values,
        }
    )
    result["absolute_change"] = result["end_year_count"] - result["start_year_count"]
    result["relative_change_pct"] = result["absolute_change"] / result["start_year_count"].replace(0, pd.NA) * 100
    return result


def age_statistics_by_year(df: pd.DataFrame, year_column: str, age_column: str) -> pd.DataFrame:
    """Compute descriptive age statistics by registry year."""
    stats = (
        df.dropna(subset=[year_column, age_column])
        .groupby(year_column)[age_column]
        .agg(n="count", mean="mean", median="median", min="min", max="max")
        .reset_index()
        .sort_values(year_column)
    )
    return stats


def assign_age_range(age: object) -> str | None:
    """Assign an age to the public age ranges used in the project."""
    if pd.isna(age):
        return None

    age = float(age)
    if age <= 13:
        return "13 or less"
    if 14 <= age <= 15:
        return "14–15"
    if 16 <= age <= 17:
        return "16–17"
    if 18 <= age <= 24:
        return "18–24"
    return "25+"


def age_range_distribution(df: pd.DataFrame, year_column: str, age_column: str) -> pd.DataFrame:
    """Compute age-range counts by year."""
    working = df.copy()
    working["age_range"] = working[age_column].map(assign_age_range)
    result = pd.crosstab(working[year_column], working["age_range"])
    return result.reset_index()


def participation_by_course(matrix: pd.DataFrame, year_column: str) -> pd.DataFrame:
    """Convert course-year counts into yearly participation percentages."""
    working = matrix.set_index(year_column).copy()
    pct = working.div(working.sum(axis=1), axis=0) * 100
    return pct.reset_index()
