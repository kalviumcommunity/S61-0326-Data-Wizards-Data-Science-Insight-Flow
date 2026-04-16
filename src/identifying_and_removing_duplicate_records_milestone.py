from __future__ import annotations

from pathlib import Path

import pandas as pd


CSV_FILE = Path("data/raw/sample_people.csv")


def explain_milestone() -> None:
    print("=" * 80)
    print("MILESTONE: IDENTIFYING AND REMOVING DUPLICATE RECORDS")
    print("=" * 80)
    print("\n[OBJECTIVE]")
    print("- Understand exact vs partial duplicates")
    print("- Detect duplicate rows")
    print("- Remove duplicates intentionally")
    print("- Verify data quality after cleanup")

    print("\n[WHY THIS MATTERS]")
    print("- Duplicates inflate counts and distort statistics")
    print("- Duplicate records can silently corrupt analysis")
    print("- Clean, unique records improve trust in downstream work")


def load_base_dataframe(csv_path: Path) -> pd.DataFrame:
    print("\n[STEP 1] LOAD BASE DATAFRAME")
    print("-" * 80)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"Loaded CSV from: {csv_path}")
    print(f"Base shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(df)
    return df


def create_dataframe_with_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[STEP 2] CREATE A DATAFRAME THAT CONTAINS DUPLICATES")
    print("-" * 80)
    print("To demonstrate deduplication clearly, we intentionally add duplicate rows.")

    duplicated_rows = pd.concat(
        [
            df,
            df.iloc[[1]],  # Exact duplicate of Bob
            df.iloc[[3]],  # Exact duplicate of Diana
            pd.DataFrame(
                [
                    {
                        "Name": "Alice",
                        "Age": 28,
                        "City": "Boston",
                        "Salary": 72000,
                    }
                ]
            ),  # Partial duplicate by Name+Age+Salary, different City
        ],
        ignore_index=True,
    )

    print(f"Shape after adding duplicates: {duplicated_rows.shape[0]} rows")
    print(duplicated_rows)
    return duplicated_rows


def inspect_exact_duplicates(df: pd.DataFrame) -> None:
    print("\n[STEP 3] DETECT EXACT DUPLICATES ACROSS ALL COLUMNS")
    print("-" * 80)

    duplicate_mask = df.duplicated()
    duplicate_count = int(duplicate_mask.sum())
    print("Boolean duplicate indicator (True means duplicate row):")
    print(duplicate_mask.to_string(index=True))
    print(f"\nExact duplicate rows found: {duplicate_count}")

    if duplicate_count > 0:
        print("\nDuplicate entries (all-column exact matches):")
        print(df[duplicate_mask])


def inspect_partial_duplicates(df: pd.DataFrame) -> None:
    print("\n[STEP 4] DETECT PARTIAL DUPLICATES ON SELECTED COLUMNS")
    print("-" * 80)
    print("Using subset = ['Name', 'Age', 'Salary']")

    subset_cols = ["Name", "Age", "Salary"]
    partial_mask = df.duplicated(subset=subset_cols, keep=False)
    partial_count = int(partial_mask.sum())

    print(f"Rows participating in partial duplicates: {partial_count}")
    if partial_count > 0:
        print(df[partial_mask].sort_values(by=subset_cols).reset_index(drop=True))


def remove_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[STEP 5] REMOVE EXACT DUPLICATES SAFELY")
    print("-" * 80)
    before_shape = df.shape

    deduped = df.drop_duplicates(keep="first").reset_index(drop=True)
    after_shape = deduped.shape

    print(f"Before drop_duplicates: {before_shape[0]} rows")
    print(f"After drop_duplicates:  {after_shape[0]} rows")
    print(f"Rows removed:           {before_shape[0] - after_shape[0]}")
    print("\nResult after exact deduplication:")
    print(deduped)
    return deduped


def remove_partial_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("\n[STEP 6] OPTIONAL: REMOVE DUPLICATES BY SELECTED COLUMNS")
    print("-" * 80)
    subset_cols = ["Name", "Age", "Salary"]
    print(f"Applying drop_duplicates(subset={subset_cols}, keep='first')")

    before_rows = df.shape[0]
    deduped_subset = df.drop_duplicates(subset=subset_cols, keep="first").reset_index(
        drop=True
    )
    after_rows = deduped_subset.shape[0]

    print(f"Before subset deduplication: {before_rows} rows")
    print(f"After subset deduplication:  {after_rows} rows")
    print(f"Rows removed:                {before_rows - after_rows}")
    print("\nResult after subset-based deduplication:")
    print(deduped_subset)
    return deduped_subset


def show_keep_options(df: pd.DataFrame) -> None:
    print("\n[STEP 7] UNDERSTAND KEEP OPTIONS")
    print("-" * 80)
    print("keep='first': keeps first occurrence")
    print("keep='last':  keeps last occurrence")
    print("keep=False:   marks all duplicate members as True")

    first_count = int(df.duplicated(keep="first").sum())
    last_count = int(df.duplicated(keep="last").sum())
    all_members_count = int(df.duplicated(keep=False).sum())

    print(f"Duplicate count with keep='first': {first_count}")
    print(f"Duplicate count with keep='last':  {last_count}")
    print(f"Duplicate member rows (keep=False): {all_members_count}")


def verify_results(df: pd.DataFrame) -> None:
    print("\n[STEP 8] VERIFY DEDUPLICATION RESULTS")
    print("-" * 80)
    remaining_exact = int(df.duplicated().sum())
    print(f"Remaining exact duplicates: {remaining_exact}")

    if remaining_exact == 0:
        print("Verification passed: no exact duplicate rows remain.")
    else:
        print("Verification failed: duplicate rows still exist.")


def print_video_walkthrough_guide() -> None:
    print("\n[STEP 9] 2-MINUTE VIDEO WALKTHROUGH GUIDE")
    print("-" * 80)
    print("1) Show duplicate detection with df.duplicated()")
    print("2) Inspect duplicate rows")
    print("3) Run drop_duplicates() and explain keep='first'")
    print("4) Compare shape before vs after cleanup")
    print("5) Recheck duplicates and explain why deduplication matters")


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / CSV_FILE

    explain_milestone()
    base_df = load_base_dataframe(csv_path)
    working_df = create_dataframe_with_duplicates(base_df)

    inspect_exact_duplicates(working_df)
    inspect_partial_duplicates(working_df)
    deduped_df = remove_exact_duplicates(working_df)
    _ = remove_partial_duplicates(working_df)
    show_keep_options(working_df)
    verify_results(deduped_df)
    print_video_walkthrough_guide()

    print("\n[COMPLETION CHECKLIST]")
    print("-" * 80)
    print("[CHECK] Duplicate rows detected")
    print("[CHECK] Duplicate rows inspected")
    print("[CHECK] Exact duplicates removed intentionally")
    print("[CHECK] Shape before and after compared")
    print("[CHECK] Verification completed")


if __name__ == "__main__":
    main()