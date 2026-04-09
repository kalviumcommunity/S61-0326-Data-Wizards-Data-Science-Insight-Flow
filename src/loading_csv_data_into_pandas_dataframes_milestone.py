from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["Name", "Age", "City", "Salary"]


def explain_csv_concept() -> None:
    print("=" * 78)
    print("MILESTONE: LOADING CSV DATA INTO PANDAS DATAFRAMES")
    print("=" * 78)

    print("\n[1] UNDERSTANDING CSV FILES")
    print("-" * 78)
    print("CSV means Comma-Separated Values.")
    print("Each row represents one record, and each column represents one field.")
    print("The first row usually contains headers (column names).")
    print("Pandas reads CSV files and converts them into DataFrames (table-like data).")


def load_csv_file(csv_path: Path) -> pd.DataFrame:
    print("\n[2] LOADING CSV INTO A DATAFRAME")
    print("-" * 78)
    print(f"CSV file path: {csv_path}")

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print("CSV loaded successfully with pd.read_csv(...)")
    return df


def inspect_loaded_data(df: pd.DataFrame) -> None:
    print("\n[3] INSPECTING LOADED DATA")
    print("-" * 78)

    print("First 5 rows (df.head()):")
    print(df.head())

    print("\nColumn names:")
    print(list(df.columns))

    print("\nShape (rows, columns):")
    print(df.shape)

    print("\nTotal row count:")
    print(len(df))

    print("\nData types:")
    print(df.dtypes)


def check_common_loading_issues(df: pd.DataFrame) -> None:
    print("\n[4] CHECKING COMMON CSV LOADING ISSUES")
    print("-" * 78)

    found_issue = False

    actual_columns = list(df.columns)
    if actual_columns != REQUIRED_COLUMNS:
        found_issue = True
        print("Potential issue: Unexpected column structure.")
        print(f"Expected columns: {REQUIRED_COLUMNS}")
        print(f"Actual columns:   {actual_columns}")
    else:
        print("Column structure looks correct.")

    if df.shape[1] != len(REQUIRED_COLUMNS):
        found_issue = True
        print("Potential issue: Missing or extra columns detected.")

    if df.columns.duplicated().any():
        found_issue = True
        print("Potential issue: Duplicate column names detected.")

    if not found_issue:
        print("No obvious loading issues detected in this file.")

    print("\nWhy inspection matters:")
    print("If columns are wrong at loading time, all downstream analysis becomes unreliable.")


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "raw" / "sample_people.csv"

    explain_csv_concept()
    df = load_csv_file(csv_path)
    inspect_loaded_data(df)
    check_common_loading_issues(df)

    print("\n[5] MILESTONE COMPLETION CHECK")
    print("-" * 78)
    print("[CHECK] CSV loaded into a Pandas DataFrame")
    print("[CHECK] Data previewed with head()")
    print("[CHECK] Columns and row counts verified")
    print("[CHECK] Common loading issues reviewed")


if __name__ == "__main__":
    main()
