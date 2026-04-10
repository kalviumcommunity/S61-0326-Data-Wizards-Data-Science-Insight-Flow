from pathlib import Path

import pandas as pd


CSV_FILE = Path("data/raw/sample_people.csv")


def explain_milestone() -> None:
    print("=" * 78)
    print("MILESTONE: UNDERSTANDING DATA SHAPES AND COLUMN DATA TYPES")
    print("=" * 78)

    print("\nGoal of this milestone:")
    print("- Understand DataFrame shape (rows, columns)")
    print("- Inspect and interpret column data types")
    print("- Detect suspicious type-related issues early")

    print("\n[1] DATASET LOADING")
    print("-" * 78)
    print("We load a CSV file into a Pandas DataFrame.")
    print("No cleaning, transformations, or modeling are done in this milestone.")


def load_csv_file(csv_path: Path) -> pd.DataFrame:
    print("\n[2] LOADING CSV INTO A DATAFRAME")
    print("-" * 78)
    print(f"CSV file path: {csv_path}")

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print("CSV loaded successfully using pd.read_csv(...)")
    return df


def inspect_shape(df: pd.DataFrame) -> None:
    print("\n[3] UNDERSTANDING DATAFRAME SHAPE")
    print("-" * 78)
    shape = df.shape
    rows, columns = shape

    print(f"DataFrame shape: {shape}")
    print(f"Rows (observations/records): {rows}")
    print(f"Columns (features/attributes): {columns}")

    print("\nShape interpretation:")
    print("- First value in shape is number of rows")
    print("- Second value in shape is number of columns")
    print("- Rows represent individual records")
    print("- Columns represent variables describing each record")


def inspect_columns_and_dtypes(df: pd.DataFrame) -> None:
    print("\n[4] INSPECTING COLUMN NAMES AND DATA TYPES")
    print("-" * 78)

    print("Column names:")
    for col in df.columns:
        print(f"- {col}")

    print("\nColumn data types (df.dtypes):")
    print(df.dtypes)

    print("\nHigh-level type groups:")
    for col, dtype in df.dtypes.items():
        if pd.api.types.is_numeric_dtype(dtype):
            kind = "numeric"
        elif pd.api.types.is_string_dtype(dtype):
            kind = "text/categorical (object/string)"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            kind = "datetime"
        else:
            kind = "other"
        print(f"- {col}: {dtype} -> {kind}")


def detect_type_related_issues(df: pd.DataFrame) -> None:
    print("\n[5] EARLY TYPE-RELATED ISSUE DETECTION")
    print("-" * 78)

    found_issue = False

    for col in df.columns:
        series = df[col]
        dtype = series.dtype

        if pd.api.types.is_object_dtype(dtype):
            # Detect numeric-looking values inside object columns.
            non_null = series.dropna()
            if len(non_null) > 0:
                converted = pd.to_numeric(non_null, errors="coerce")
                numeric_like_ratio = converted.notna().mean()
                if numeric_like_ratio >= 0.8:
                    found_issue = True
                    print(
                        f"Potential issue: '{col}' is object but looks mostly numeric "
                        f"({numeric_like_ratio:.0%} numeric-like values)."
                    )
                    print("This can cause numeric operations to fail or behave unexpectedly.")

        missing_count = series.isna().sum()
        if missing_count > 0:
            found_issue = True
            print(
                f"Note: '{col}' contains {missing_count} missing value(s). "
                "Missing data can affect inferred data types."
            )

    if not found_issue:
        print("No obvious type-related issues detected.")

    print("\nWhy this matters:")
    print("- Correct types ensure valid operations")
    print("- Wrong types can silently produce incorrect results")
    print("- Early checks prevent downstream analysis errors")


def preview_data(df: pd.DataFrame) -> None:
    print("\n[6] QUICK DATA PREVIEW")
    print("-" * 78)
    print("First 5 rows (df.head()):")
    print(df.head())


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / CSV_FILE

    explain_milestone()
    df = load_csv_file(csv_path)
    inspect_shape(df)
    inspect_columns_and_dtypes(df)
    detect_type_related_issues(df)
    preview_data(df)

    print("\n[7] MILESTONE COMPLETION CHECK")
    print("-" * 78)
    print("[CHECK] DataFrame loaded")
    print("[CHECK] Shape inspected and interpreted")
    print("[CHECK] Rows and columns identified")
    print("[CHECK] Column data types inspected")
    print("[CHECK] Type-related issues checked")


if __name__ == "__main__":
    main()
