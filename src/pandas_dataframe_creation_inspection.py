import pandas as pd
from pathlib import Path


def inspect_dataframe(df: pd.DataFrame, name: str) -> None:
    print(f"\n{'=' * 72}")
    print(f"INSPECTING DATAFRAME: {name}")
    print(f"{'=' * 72}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nLast 5 rows:")
    print(df.tail())
    print(f"\nShape: {df.shape}  (rows, columns)")
    print(f"Columns: {list(df.columns)}")
    print("\nData types:")
    print(df.dtypes)
    print("\nSummary (describe):")
    print(df.describe(include='all'))
    print("\nInfo:")
    print(df.info())


def create_dictionary_dataframe() -> pd.DataFrame:
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [28, 34, 22, 45],
        "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    }

    df = pd.DataFrame(data)
    print("Dictionary DataFrame:")
    print(df)
    print("\nColumn names:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)
    return df


def create_sample_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        csv_content = (
            "Name,Age,City,Salary\n"
            "Alice,28,New York,72000\n"
            "Bob,34,Los Angeles,83000\n"
            "Charlie,22,Chicago,56000\n"
            "Diana,45,Houston,98000\n"
            "Ethan,30,Phoenix,67000\n"
        )
        path.write_text(csv_content, encoding="utf-8")
        print(f"Created sample CSV file at: {path}")
    else:
        print(f"Sample CSV already exists at: {path}")


def load_dataframe_from_csv(path: Path) -> pd.DataFrame:
    print(f"\nLoading CSV file from: {path}")
    df = pd.read_csv(path)
    print("CSV file loaded successfully.")
    print("Headers detected:", list(df.columns))
    return df


if __name__ == "__main__":
    print("PANDAS DATAFRAME CREATION & INSPECTION")
    print("~" * 72)

    # Task 1: Import pandas (already imported above)

    # Task 2: Create a DataFrame from a dictionary
    dict_df = create_dictionary_dataframe()
    inspect_dataframe(dict_df, "Dictionary DataFrame")

    # Task 3: Create a DataFrame from a CSV file
    sample_csv_path = Path(__file__).resolve().parents[1] / "data" / "raw" / "sample_people.csv"
    create_sample_csv(sample_csv_path)
    csv_df = load_dataframe_from_csv(sample_csv_path)
    inspect_dataframe(csv_df, "CSV DataFrame")
