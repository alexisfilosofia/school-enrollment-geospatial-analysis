"""Data cleaning utilities for historical school enrollment records.

These functions are intentionally generic. They do not depend on the private source
files used in the original Colab notebooks. Instead, they capture the reusable cleaning
logic: column normalization, course standardization, date parsing, and age coercion.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable

import pandas as pd


COURSE_CANONICAL_ORDER = ["1º Año", "2º Año", "3º Año", "4º Año", "5º Año", "6º Año"]

COURSE_PATTERNS = {
    "1º Año": ["1", "1ro", "1ero", "primero", "primer"],
    "2º Año": ["2", "2do", "segundo"],
    "3º Año": ["3", "3ro", "tercero"],
    "4º Año": ["4", "4to", "cuarto"],
    "5º Año": ["5", "5to", "quinto"],
    "6º Año": ["6", "6to", "sexto"],
}


def strip_accents(value: str) -> str:
    """Return a lowercase ASCII-like representation for matching."""
    value = unicodedata.normalize("NFKD", str(value))
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return value.lower().strip()


def normalize_column_name(name: str) -> str:
    """Normalize a column name into a machine-friendly snake_case format."""
    name = strip_accents(name)
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of a DataFrame with normalized column names."""
    cleaned = df.copy()
    cleaned.columns = [normalize_column_name(col) for col in cleaned.columns]
    return cleaned


def canonicalize_course(value: object) -> str | None:
    """Map heterogeneous course labels to canonical course categories.

    Examples of labels handled include `1`, `1ro`, `primer año`, `2do`,
    `sexto`, etc. Unknown or empty labels return `None`.
    """
    if pd.isna(value):
        return None

    text = strip_accents(str(value))
    text = text.replace("ano", "anio")

    for canonical, patterns in COURSE_PATTERNS.items():
        for pattern in patterns:
            if re.search(rf"(^|\D){re.escape(pattern)}($|\D)", text) or pattern in text:
                return canonical
    return None


def add_canonical_course_column(
    df: pd.DataFrame,
    source_column: str,
    output_column: str = "curso_canonico",
) -> pd.DataFrame:
    """Add a canonical course column based on a source course column."""
    cleaned = df.copy()
    cleaned[output_column] = cleaned[source_column].map(canonicalize_course)
    return cleaned


def coerce_numeric_age(df: pd.DataFrame, age_column: str, output_column: str = "edad_num") -> pd.DataFrame:
    """Convert an age column to numeric values, preserving invalid values as NaN."""
    cleaned = df.copy()
    cleaned[output_column] = pd.to_numeric(cleaned[age_column], errors="coerce")
    return cleaned


def parse_dates(
    df: pd.DataFrame,
    date_column: str,
    output_column: str = "fecha_parseada",
    dayfirst: bool = True,
) -> pd.DataFrame:
    """Parse a date column into pandas datetime values."""
    cleaned = df.copy()
    cleaned[output_column] = pd.to_datetime(cleaned[date_column], errors="coerce", dayfirst=dayfirst)
    return cleaned


def keep_public_safe_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Return only columns that are safe for public aggregate workflows.

    Use this helper after reviewing the dataset manually. Do not include names,
    addresses, exact coordinates, phone numbers, or other identifying attributes.
    """
    existing = [col for col in columns if col in df.columns]
    return df.loc[:, existing].copy()
