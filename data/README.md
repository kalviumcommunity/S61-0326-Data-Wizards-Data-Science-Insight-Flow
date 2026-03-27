# Data Organization Guide

This project follows best practices for data organization to ensure reproducibility, data integrity, and clarity.

## Folder Structure

- `data/raw/` — **Raw Data**
  - Store original, untouched data files here.
  - Treat as read-only. Never modify files in this folder.
  - Example: `data/raw/survey_responses.csv`

- `data/processed/` — **Processed Data**
  - Save cleaned, transformed, or feature-engineered datasets here.
  - All files should be reproducible from raw data using scripts or notebooks.
  - Example: `data/processed/survey_cleaned.csv`

- `data/output/` — **Output Artifacts**
  - Store final results, plots, reports, or model files here.
  - Do not mix with raw or processed data.
  - Example: `data/output/summary_plot.png`

## Best Practices

- **Never edit raw data directly.**
- **Processed data must be generated from raw data.**
- **Outputs are for results and presentation only.**
- Use clear, descriptive filenames.
- Maintain one-way data flow: raw → processed → output.

## Why This Matters

- Prevents accidental data loss or corruption
- Supports reproducibility and auditability
- Makes collaboration and review easier

For more details, see the project Readme or ask the project maintainer.