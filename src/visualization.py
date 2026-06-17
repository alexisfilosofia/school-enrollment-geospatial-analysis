"""Visualization helpers for aggregate educational analytics outputs.

These helpers generate public-safe charts from aggregate tables. They are meant
for reproducible portfolio workflows and avoid plotting row-level sensitive data.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DEFAULT_FIGSIZE = (10, 6)


def save_annual_enrollment_chart(
    counts: pd.DataFrame,
    year_column: str,
    count_column: str,
    output_path: str | Path,
) -> None:
    """Save a bar chart of annual enrollment counts."""
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    ax.bar(counts[year_column].astype(str), counts[count_column])
    ax.set_title("Annual enrollment volume")
    ax.set_xlabel("Registry year")
    ax.set_ylabel("Student records")
    ax.bar_label(ax.containers[0])
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def save_course_matrix_heatmap(
    matrix: pd.DataFrame,
    year_column: str,
    output_path: str | Path,
) -> None:
    """Save a heatmap-style chart for a course-year matrix using matplotlib only."""
    values = matrix.drop(columns=[year_column])
    fig, ax = plt.subplots(figsize=(10, 6))
    image = ax.imshow(values.values, aspect="auto")

    ax.set_xticks(range(values.shape[1]))
    ax.set_xticklabels(values.columns, rotation=45, ha="right")
    ax.set_yticks(range(matrix.shape[0]))
    ax.set_yticklabels(matrix[year_column].astype(str))
    ax.set_title("Entry course frequency by year")

    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            ax.text(j, i, int(values.iloc[i, j]), ha="center", va="center")

    fig.colorbar(image, ax=ax, label="Records")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def save_frequency_bar_chart(
    table: pd.DataFrame,
    category_column: str,
    count_column: str,
    output_path: str | Path,
    title: str,
) -> None:
    """Save a horizontal bar chart from a categorical frequency table."""
    fig, ax = plt.subplots(figsize=DEFAULT_FIGSIZE)
    ordered = table.sort_values(count_column)
    ax.barh(ordered[category_column], ordered[count_column])
    ax.set_title(title)
    ax.set_xlabel("Count")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def export_table_html(table: pd.DataFrame, output_path: str | Path, title: str | None = None) -> None:
    """Export a DataFrame as a simple standalone HTML table."""
    heading = f"<h1>{title}</h1>" if title else ""
    html = "\n".join(
        [
            "<!DOCTYPE html>",
            "<html lang='en'>",
            "<head><meta charset='utf-8'><title>Aggregate table</title></head>",
            "<body>",
            heading,
            table.to_html(index=False),
            "</body></html>",
        ]
    )
    Path(output_path).write_text(html, encoding="utf-8")
