"""Minimal tests for aggregate enrollment utilities."""

import pandas as pd

from src.enrollment_analysis import annual_enrollment_counts, course_year_matrix, course_change_between_years


def test_annual_enrollment_counts():
    df = pd.DataFrame({"anio_libro": [1910, 1910, 1911]})
    result = annual_enrollment_counts(df, "anio_libro")
    assert result.to_dict("records") == [
        {"anio_libro": 1910, "records": 2},
        {"anio_libro": 1911, "records": 1},
    ]


def test_course_year_matrix_and_change():
    df = pd.DataFrame(
        {
            "anio_libro": [1910, 1910, 1915, 1915, 1915],
            "curso": ["1º Año", "2º Año", "1º Año", "1º Año", "2º Año"],
        }
    )
    matrix = course_year_matrix(df, "anio_libro", "curso", ["1º Año", "2º Año"])
    assert matrix.loc[matrix["anio_libro"] == 1910, "1º Año"].item() == 1
    assert matrix.loc[matrix["anio_libro"] == 1915, "1º Año"].item() == 2

    change = course_change_between_years(matrix, "anio_libro", 1910, 1915)
    first_course = change[change["course"] == "1º Año"].iloc[0]
    assert first_course["absolute_change"] == 1
