from pathlib import Path
import pandas as pd


CSV_FILE = Path("data/raw/sample_people.csv")


def explain_milestone() -> None:
    """Explain the purpose and goals of this milestone."""
    print("=" * 80)
    print("MILESTONE: SELECTING ROWS AND COLUMNS USING INDEXING AND SLICING")
    print("=" * 80)

    print("\n[OBJECTIVE] Goals of this milestone:")
    print("   - Understand row vs column selection")
    print("   - Select columns by name (single and multiple)")
    print("   - Select rows by position (integer indexing)")
    print("   - Select rows by label (index labels)")
    print("   - Combine row and column selections")
    print("   - Avoid common selection pitfalls")

    print("\n[WHY IT MATTERS]:")
    print("   - Incorrect data selection causes silent errors in analysis")
    print("   - Clear selection skills ensure precision and readability")
    print("   - Selection is foundational for all downstream operations")


def load_csv_file(csv_path: Path) -> pd.DataFrame:
    """Load CSV file into a DataFrame."""
    print("\n[STEP 0] LOADING DATA")
    print("-" * 80)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"[OK] CSV loaded successfully: {csv_path}")
    print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
    print("First few rows of the DataFrame:")
    print(df)
    print()
    return df


def section_column_selection_single(df: pd.DataFrame) -> None:
    """SECTION 1: Select a single column by name."""
    print("\n" + "=" * 80)
    print("[SECTION 1] SELECTING A SINGLE COLUMN BY NAME")
    print("=" * 80)

    print("\n[CONCEPT]:")
    print("   - A single column is accessed using square brackets and a column name")
    print("   - Result is a pandas Series (1-dimensional)")

    print("\n[EXAMPLE 1] Select the 'Name' column")
    print("-" * 80)
    print("Code: df['Name']")
    names = df["Name"]
    print(f"\nResult type: {type(names)}")
    print("Result:")
    print(names)

    print("\n[EXAMPLE 2] Select the 'Salary' column")
    print("-" * 80)
    print("Code: df['Salary']")
    salaries = df["Salary"]
    print(f"\nResult type: {type(salaries)}")
    print("Result:")
    print(salaries)

    print("\n[KEY INSIGHT]:")
    print("   - Single column selection returns a Series, not a DataFrame")
    print("   - Series is 1-dimensional (like a list or array)")
    print("   - Use df['column_name'] for single column access")


def section_column_selection_multiple(df: pd.DataFrame) -> None:
    """SECTION 2: Select multiple columns using a list."""
    print("\n" + "=" * 80)
    print("[SECTION 2] SELECTING MULTIPLE COLUMNS BY NAME")
    print("=" * 80)

    print("\n[CONCEPT]:")
    print("   - Multiple columns are selected using a list of column names")
    print("   - Result is a pandas DataFrame (2-dimensional)")

    print("\n[EXAMPLE 1] Select 'Name' and 'Salary' columns")
    print("-" * 80)
    print("Code: df[['Name', 'Salary']]")
    subset = df[["Name", "Salary"]]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[EXAMPLE 2] Select all columns except 'City'")
    print("-" * 80)
    print("Code: df[['Name', 'Age', 'Salary']]")
    subset = df[["Name", "Age", "Salary"]]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[COMMON MISTAKE]:")
    print("   WRONG: df['Name', 'Salary']  <- This will cause an error!")
    print("   RIGHT: df[['Name', 'Salary']] <- Notice the double square brackets!")

    print("\n[KEY INSIGHT]:")
    print("   - Use double square brackets for multiple columns: df[[col1, col2, ...]")
    print("   - Result is always a DataFrame, even with one column: df[['Name']]")


def section_rows_by_position(df: pd.DataFrame) -> None:
    """SECTION 3: Select rows using position-based (iloc) indexing."""
    print("\n" + "=" * 80)
    print("[SECTION 3] SELECTING ROWS BY POSITION (INTEGER INDEXING)")
    print("=" * 80)

    print("\n[CONCEPT]:")
    print("   - Use .iloc[] for position-based indexing (integer location)")
    print("   - Indexing is zero-based (first row is at position 0)")
    print("   - Slicing is exclusive on the right end")

    print("\n[EXAMPLE 1] Select a single row by position")
    print("-" * 80)
    print("Code: df.iloc[0]  # Get the first row (position 0)")
    row_0 = df.iloc[0]
    print(f"\nResult type: {type(row_0)}")
    print("Result (Series):")
    print(row_0)

    print("\n[EXAMPLE 2] Select another single row")
    print("-" * 80)
    print("Code: df.iloc[2]  # Get the third row (position 2)")
    row_2 = df.iloc[2]
    print(f"\nResult type: {type(row_2)}")
    print("Result (Series):")
    print(row_2)

    print("\n[EXAMPLE 3] Select multiple consecutive rows (slice)")
    print("-" * 80)
    print("Code: df.iloc[0:2]  # Get rows at positions 0 and 1 (not 2)")
    slice_0_2 = df.iloc[0:2]
    print(f"\nResult type: {type(slice_0_2)}")
    print("Result (DataFrame):")
    print(slice_0_2)

    print("\n[EXAMPLE 4] Select rows with step")
    print("-" * 80)
    print("Code: df.iloc[::2]  # Get every other row (0, 2, ...)")
    slice_step = df.iloc[::2]
    print(f"\nResult type: {type(slice_step)}")
    print("Result (DataFrame):")
    print(slice_step)

    print("\n[EXAMPLE 5] Select from position 1 to the end")
    print("-" * 80)
    print("Code: df.iloc[1:]  # Get all rows from position 1 onwards")
    slice_from_1 = df.iloc[1:]
    print(f"\nResult type: {type(slice_from_1)}")
    print("Result (DataFrame):")
    print(slice_from_1)

    print("\n[IMPORTANT RULES]:")
    print("   - .iloc uses zero-based indexing")
    print("   - Slicing is exclusive on the right: iloc[0:2] includes 0 and 1, NOT 2")
    print("   - .iloc only works with integer positions, not labels")

    print("\n[KEY INSIGHT]:")
    print("   - Use .iloc[pos] for single row -> returns Series")
    print("   - Use .iloc[pos:pos+n] for multiple rows -> returns DataFrame")


def section_rows_by_label(df: pd.DataFrame) -> None:
    """SECTION 4: Select rows using label-based (loc) indexing."""
    print("\n" + "=" * 80)
    print("[SECTION 4] SELECTING ROWS BY LABEL (LABEL-BASED INDEXING)")
    print("=" * 80)

    print("\n[CONCEPT]:")
    print("   - Use .loc[] for label-based indexing")
    print("   - Labels come from the DataFrame's index")
    print("   - By default, index is 0, 1, 2, ... (same as position)")
    print("   - But index can be any custom labels (strings, dates, etc.)")

    print("\n[EXAMPLE 1] Check the current index")
    print("-" * 80)
    print("Code: df.index")
    print("Current index:")
    print(df.index)

    print("\n[EXAMPLE 2] Select a single row by label")
    print("-" * 80)
    print("Code: df.loc[0]  # Get row with label 0 (happens to be first row)")
    row_label_0 = df.loc[0]
    print(f"\nResult type: {type(row_label_0)}")
    print("Result:")
    print(row_label_0)

    print("\n[EXAMPLE 3] Select multiple rows by label range")
    print("-" * 80)
    print("Code: df.loc[0:2]  # Get rows with labels 0, 1, and 2 (INCLUSIVE!)")
    slice_label = df.loc[0:2]
    print(f"\nResult type: {type(slice_label)}")
    print("Result (note: INCLUSIVE on right end with .loc):")
    print(slice_label)

    print("\n[EXAMPLE 4] Select rows from label 1 onwards")
    print("-" * 80)
    print("Code: df.loc[1:]")
    slice_from_label_1 = df.loc[1:]
    print(f"\nResult type: {type(slice_from_label_1)}")
    print("Result:")
    print(slice_from_label_1)

    print("\n[KEY DIFFERENCE FROM .iloc]:")
    print("   .iloc[0:2] -> includes positions 0, 1 (EXCLUSIVE on right)")
    print("   .loc[0:2]  -> includes labels 0, 1, 2 (INCLUSIVE on right)")

    print("\n[KEY INSIGHT]:")
    print("   - Use .loc[label] for label-based access")
    print("   - .loc slicing is INCLUSIVE on both ends (unlike .iloc)")
    print("   - Custom indices make .loc more readable and intentional")


def section_rows_and_columns_combined(df: pd.DataFrame) -> None:
    """SECTION 5: Select specific rows AND columns together."""
    print("\n" + "=" * 80)
    print("[SECTION 5] SELECTING ROWS AND COLUMNS TOGETHER")
    print("=" * 80)

    print("\n[CONCEPT]:")
    print("   - Combine row and column selection using .iloc or .loc")
    print("   - Syntax: df.iloc[rows, columns] or df.loc[rows, columns]")
    print("   - Comma separates row selection from column selection")

    print("\n[EXAMPLE 1] Select rows 0-1 and columns 'Name' and 'Salary'")
    print("-" * 80)
    print("Code: df.loc[0:1, ['Name', 'Salary']]")
    subset = df.loc[0:1, ["Name", "Salary"]]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[EXAMPLE 2] Get the first 2 rows (positions 0-1) with all columns")
    print("-" * 80)
    print("Code: df.iloc[0:2, :]  or  df.iloc[0:2]")
    subset = df.iloc[0:2, :]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[EXAMPLE 3] Get the first 2 rows and just 'Name' column")
    print("-" * 80)
    print("Code: df.iloc[0:2, 0]  # Column at position 0 is 'Name'")
    subset = df.iloc[0:2, 0]
    print(f"\nResult type: {type(subset)} (Series because single column)")
    print("Result:")
    print(subset)

    print("\n[EXAMPLE 4] Get first 2 rows and columns at positions 0 and 2")
    print("-" * 80)
    print("Code: df.iloc[0:2, [0, 2]]  # Name and City")
    subset = df.iloc[0:2, [0, 2]]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[EXAMPLE 5] Get specific rows by label with specific columns")
    print("-" * 80)
    print("Code: df.loc[1:3, ['Name', 'Age']]")
    subset = df.loc[1:3, ["Name", "Age"]]
    print(f"\nResult type: {type(subset)}")
    print("Result:")
    print(subset)

    print("\n[KEY INSIGHT]:")
    print("   - Use .iloc[row_positions, col_positions] for integer indexing")
    print("   - Use .loc[row_labels, col_names] for label-based indexing")
    print("   - Order: rows first, then columns (separated by comma)")


def section_common_mistakes(df: pd.DataFrame) -> None:
    """SECTION 6: Common mistakes and how to avoid them."""
    print("\n" + "=" * 80)
    print("[SECTION 6] COMMON MISTAKES AND HOW TO AVOID THEM")
    print("=" * 80)

    print("\n[MISTAKE 1] Forgetting double brackets for multiple columns")
    print("-" * 80)
    print("WRONG: df['Name', 'Salary']")
    print("RIGHT: df[['Name', 'Salary']]")
    print("       (Notice the double square brackets!)")

    print("\n[MISTAKE 2] Confusing .iloc (position) with .loc (label)")
    print("-" * 80)
    print("WRONG: df.iloc['Name']  <- Will cause error (iloc needs integers)")
    print("RIGHT: df.loc[0, 'Name'] <- Correct")
    print("  OR : df.iloc[0, 0]    <- Also correct (position-based)")

    print("\n[MISTAKE 3] Forgetting that .loc is inclusive on the right")
    print("-" * 80)
    print("df.iloc[0:2]  -> includes positions 0, 1 (EXCLUDES 2)")
    print("df.loc[0:2]   -> includes labels 0, 1, 2 (INCLUDES 2)")

    print("\n[MISTAKE 4] Chained indexing can be unpredictable")
    print("-" * 80)
    print("AVOID: df['Name'][0]  <- Works but unpredictable")
    print("PREFER: df.loc[0, 'Name']  <- Clear and safe")

    print("\n[MISTAKE 5] Modifying a selection without realizing it's a view")
    print("-" * 80)
    print("RISKY: df[['Name']].iloc[0, 0] = 'NewName'")
    print("SAFE:  df.loc[0, 'Name'] = 'NewName'")

    print("\n[BEST PRACTICES]:")
    print("   1. Use df[['col1', 'col2']] for column-only selection")
    print("   2. Use .loc[row_label, col_name] when row/column labels are clear")
    print("   3. Use .iloc[row_pos, col_pos] when working with positions")
    print("   4. Verify your selection before using results")
    print("   5. Always check that you got exactly what you expected")


def section_verification_exercise(df: pd.DataFrame) -> None:
    """SECTION 7: Verification exercises."""
    print("\n" + "=" * 80)
    print("[SECTION 7] VERIFICATION EXERCISES")
    print("=" * 80)

    print("\n[EXERCISE 1] Extract just the 'Age' column")
    print("-" * 80)
    print("Try: age_values = df['Age']")
    age_values = df["Age"]
    print(f"[OK] Result type: {type(age_values).__name__}")
    print(age_values)

    print("\n[EXERCISE 2] Extract 'Name' and 'City' columns only")
    print("-" * 80)
    print("Try: name_city = df[['Name', 'City']]")
    name_city = df[["Name", "City"]]
    print(f"[OK] Result type: {type(name_city).__name__}")
    print(name_city)

    print("\n[EXERCISE 3] Get the second row (position 1)")
    print("-" * 80)
    print("Try: second_row = df.iloc[1]")
    second_row = df.iloc[1]
    print(f"[OK] Result type: {type(second_row).__name__}")
    print("[OK] Values:")
    print(second_row)

    print("\n[EXERCISE 4] Get rows 1 and 2, only 'Name' and 'Salary'")
    print("-" * 80)
    print("Try: subset = df.loc[1:2, ['Name', 'Salary']]")
    subset = df.loc[1:2, ["Name", "Salary"]]
    print(f"[OK] Result type: {type(subset).__name__}")
    print(subset)

    print("\n[EXERCISE 5] Get the first 2 rows using .iloc")
    print("-" * 80)
    print("Try: first_two = df.iloc[0:2]")
    first_two = df.iloc[0:2]
    print(f"[OK] Result type: {type(first_two).__name__}")
    print(first_two)

    print("\n[OK] All exercises completed successfully!")


def main() -> None:
    """Main execution."""
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / CSV_FILE

    explain_milestone()
    df = load_csv_file(csv_path)

    # Run all sections
    section_column_selection_single(df)
    section_column_selection_multiple(df)
    section_rows_by_position(df)
    section_rows_by_label(df)
    section_rows_and_columns_combined(df)
    section_common_mistakes(df)
    section_verification_exercise(df)

    # Final summary
    print("\n" + "=" * 80)
    print("MILESTONE COMPLETION SUMMARY")
    print("=" * 80)
    print("\n[OK] Understood row vs column selection")
    print("[OK] Selected columns by name (single and multiple)")
    print("[OK] Selected rows by position using .iloc")
    print("[OK] Selected rows by label using .loc")
    print("[OK] Combined row and column selections")
    print("[OK] Learned common mistakes and best practices")
    print("[OK] Completed verification exercises")

    print("\n[READY] You are now ready to:")
    print("   - Extract any subset of data from a DataFrame with confidence")
    print("   - Choose the right selection method for each scenario")
    print("   - Write clear, readable, and reliable selection code")
    print("   - Avoid silent data errors from incorrect selections")

    print("\n[VIDEO TASK] Next Step - Record a 2-minute screen walkthrough video")
    print("   Your video should demonstrate:")
    print("   [1] Selecting one or more columns")
    print("   [2] Selecting rows by position")
    print("   [3] Selecting rows by label")
    print("   [4] Selecting a subset of rows and columns together")
    print("   [5] Explanation of when to use each approach")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
