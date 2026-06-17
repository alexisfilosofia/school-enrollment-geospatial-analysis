"""Geospatial analysis utilities for public-safe educational analytics.

The original project used geocoded addresses. This module documents reusable
aggregate logic without publishing or depending on private coordinates.
"""

from __future__ import annotations

import math

import pandas as pd


EARTH_RADIUS_KM = 6371.0088


def haversine_distance_km(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """Calculate the great-circle distance between two latitude/longitude points."""
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return EARTH_RADIUS_KM * c


def add_distance_to_point(
    df: pd.DataFrame,
    lat_column: str,
    lon_column: str,
    target_lat: float,
    target_lon: float,
    output_column: str = "distance_to_school_km",
) -> pd.DataFrame:
    """Add approximate distance to a fixed point, such as a school location."""
    working = df.copy()

    def compute(row: pd.Series) -> float | None:
        if pd.isna(row[lat_column]) or pd.isna(row[lon_column]):
            return None
        return haversine_distance_km(float(row[lat_column]), float(row[lon_column]), target_lat, target_lon)

    working[output_column] = working.apply(compute, axis=1)
    return working


def distance_summary(df: pd.DataFrame, distance_column: str) -> pd.Series:
    """Return aggregate distance statistics safe for public reporting."""
    distances = pd.to_numeric(df[distance_column], errors="coerce").dropna()
    return pd.Series(
        {
            "count": int(distances.count()),
            "mean_km": float(distances.mean()),
            "median_km": float(distances.median()),
            "min_km": float(distances.min()),
            "max_km": float(distances.max()),
        }
    )


def distance_bins(
    df: pd.DataFrame,
    distance_column: str,
    bins: list[float] | None = None,
    labels: list[str] | None = None,
) -> pd.DataFrame:
    """Aggregate distances into bins for privacy-aware visualization."""
    if bins is None:
        bins = [0, 1, 2, 3, 4, 5, float("inf")]
    if labels is None:
        labels = ["0–1 km", "1–2 km", "2–3 km", "3–4 km", "4–5 km", "5+ km"]

    working = df.copy()
    working["distance_bin"] = pd.cut(working[distance_column], bins=bins, labels=labels, include_lowest=True)
    return working["distance_bin"].value_counts().sort_index().rename_axis("distance_bin").reset_index(name="count")


def frequency_table(
    df: pd.DataFrame,
    column: str,
    missing_label: str = "sin_dato",
    top_n: int | None = None,
) -> pd.DataFrame:
    """Build an aggregate frequency and percentage table for a categorical field."""
    values = df[column].fillna(missing_label).astype(str).str.strip().replace("", missing_label)
    table = values.value_counts(dropna=False).rename_axis(column).reset_index(name="count")
    table["percentage"] = table["count"] / table["count"].sum() * 100

    if top_n is not None:
        table = table.head(top_n)

    return table


def public_zone_summary(df: pd.DataFrame, zone_column: str) -> pd.Series:
    """Return only the number of spatial zones, not point-level data."""
    return pd.Series({"spatial_zones": int(df[zone_column].nunique(dropna=True))})
