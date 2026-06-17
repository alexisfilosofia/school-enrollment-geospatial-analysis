# Methodological note

This project is a public, privacy-aware reconstruction of a larger Colab-based workflow for historical school enrollment analysis.

## 1. Data consolidation

The quantitative notebook consolidates several historical enrollment spreadsheets into a single analytical table. During this process, column names and course labels are normalized so that records from different years can be compared consistently.

The consolidated table reported by the notebook contains `1,408` records and `22` columns.

## 2. Course normalization

Course labels are standardized into six canonical categories:

```text
1º Año, 2º Año, 3º Año, 4º Año, 5º Año, 6º Año
```

This enables year-by-year comparison of enrollment volume, course participation and interannual variation.

## 3. Age analysis

The workflow converts age values into numeric form, computes descriptive statistics by year and builds visualizations for:

- annual age distribution;
- age ranges;
- median and mean age;
- dispersion and outlier detection;
- course-level age patterns.

Outliers are interpreted cautiously. In historical institutional records, unusual ages may represent transcription issues, late enrollment, special trajectories or archival inconsistencies.

## 4. Course-level analysis

The project calculates enrollment counts by course and year, interannual absolute change, interannual percentage change and participation of each course in annual enrollment.

The most relevant public finding is that the expansion between 1910 and 1915 is concentrated in lower courses, especially `1º Año` and `2º Año`.

## 5. Geospatial analysis

The geospatial notebook works with geocoded addresses and produces distance-to-school and socio-spatial summaries. The public version only reports aggregate metrics, such as:

- geocoded cases;
- mean and median distance to school;
- number of spatial zones;
- occupational group counts;
- aggregate nationality distributions.

Exact coordinates, raw addresses and point-level sensitive maps are excluded from the public repository.

## 6. Privacy decisions

The project follows a conservative publication strategy:

- no raw student-level dataset is published;
- no names or addresses are included;
- geospatial outputs are summarized rather than exposed at row level;
- sensitive categories are not combined with exact point locations in the public version;
- public figures are aggregate or public-safe renderings.

## 7. Portfolio transformation

The original notebooks are useful as analytical workspaces. The static web page transforms them into a portfolio-readable narrative: problem, method, selected outputs, findings, technical stack and ethical decisions.
