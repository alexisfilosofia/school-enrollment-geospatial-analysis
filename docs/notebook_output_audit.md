# Notebook output audit

This document records how the public portfolio version was derived from the original Colab notebooks while avoiding publication of raw sensitive data.

## Source notebooks

- `Archivo_PST_Cuanti.ipynb`: quantitative enrollment workflow.
- `Archivo_PST_GEO_Final.ipynb`: geospatial and socio-spatial workflow.

The public site does not reproduce all notebook outputs. It selects aggregate results that are useful for portfolio presentation and safe to publish.

## Quantitative notebook outputs used

### Consolidation

The notebook consolidates historical enrollment spreadsheets into a unified table.

Key printed output:

```text
Dimensión consolidada: (1408, 22)
Cursos únicos canonizados:
['1º Año', '2º Año', '3º Año', '4º Año', '5º Año', '6º Año']
```

### Annual enrollment count

Used in the public web page and README.

```text
1910: 155
1911: 182
1912: 183
1913: 216
1914: 317
1915: 355
```

This corresponds to the annual count table and chart from the quantitative notebook.

### Age statistics by year

Used in the web interpretation of age structure and outliers.

```text
1910: n=154, mean=18.86, median=18, min=15, max=28
1911: n=182, mean=18.51, median=18, min=13, max=29
1912: n=183, mean=18.57, median=18, min=14, max=28
1913: n=215, mean=18.78, median=18, min=16, max=32
1914: n=317, mean=18.70, median=18, min=15, max=30
1915: n=354, mean=18.15, median=17, min=15, max=37
```

### Course-year matrix

Used in the README and web page table.

```text
Year   1º Año  2º Año  3º Año  4º Año  5º Año  6º Año
1910      44      22      21      12      35      21
1911      46      24      15      22      32      21
1912      67      30      21      14      38      13
1913      69      43      24      17      53      10
1914     126      45      45      19      66      15
1915     139      78      45      40      38      15
```

### Course-level change from 1910 to 1915

Used to interpret the expansion of the lower entry courses.

```text
1º Año: 44 to 139, +95, +215.91%
2º Año: 22 to 78, +56, +254.55%
3º Año: 21 to 45, +24, +114.29%
4º Año: 12 to 40, +28, +233.33%
5º Año: 35 to 38, +3, +8.57%
6º Año: 21 to 15, -6, -28.57%
```

## Geospatial notebook outputs used

### Socio-spatial summary

Used in the public geospatial section.

```text
casos_geocodificados: 323
grupos_ocupacionales_distintos: 9
nacionalidades_distintas: 7
zonas_espaciales_distintas: 77
proporcion_extranjeros: 0.077
distancia_media_al_colegio_km: 3.120
distancia_mediana_al_colegio_km: 2.340
```

### Student nationality summary

Used only as aggregate interpretation.

```text
argentino: 326 (91.83%)
espanol: 13 (3.66%)
italiano: 6 (1.69%)
uruguayo: 5 (1.41%)
paraguayo: 2 (0.56%)
nat. arg.: 1 (0.28%)
nat. arg.*: 1 (0.28%)
sin_dato: 1 (0.28%)
```

### Guardian nationality summary

Used in the web page and README.

```text
argentino: 121 (34.08%)
italiano: 86 (24.23%)
sin_dato: 62 (17.46%)
espanol: 53 (14.93%)
frances: 14 (3.94%)
```

## Outputs intentionally not published

The public repository intentionally excludes or avoids direct publication of:

- raw Excel files;
- row-level enrollment tables;
- names of students, guardians or family members;
- raw addresses;
- exact coordinates linked to individual records;
- maps that combine individual point locations with sensitive categories such as nationality;
- Google Drive paths and private folder structures.

## Public representation strategy

The repository uses public-safe SVG figures and aggregate tables. These are not a full data release. They are a portfolio-oriented representation of the analytical workflow and its main findings.
