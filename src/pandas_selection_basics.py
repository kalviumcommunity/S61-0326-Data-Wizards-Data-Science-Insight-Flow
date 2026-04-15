import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 22, 28],
    "marks": [88, 92, 85, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSelect a single column (name):")
print(df["name"])

print("\nSelect multiple columns (name and marks):")
print(df[["name", "marks"]])

print("\nSelect a single row by position (row 1, zero-based):")
print(df.iloc[1])

print("\nSelect a range of rows by position (rows 1 to 2):")
print(df.iloc[1:3])

custom_index = ["row1", "row2", "row3", "row4"]
df_label = df.copy()
df_label.index = custom_index

print("\nDataFrame with custom labels:")
print(df_label)

print("\nSelect a single row by label (row2):")
print(df_label.loc["row2"])

print("\nSelect a range of rows by label (row2 to row4):")
print(df_label.loc["row2":"row4"])

print("\nSelect a subset of rows and specific columns together:")
print(df_label.loc[["row2", "row4"], ["name", "marks"]])

print("\nSelect by position and column index together:")
print(df.iloc[0:2, 1:3])

print("\nExplanation:")
print("Column selection uses the column name or a list of names to pick one or more columns.")
print("Positional indexing with iloc uses integer positions starting at zero.")
print("Label-based indexing with loc uses custom index labels instead of row numbers.")
print("Combined selection can choose specific rows and columns in the same expression.")

print("\nRun this script with: python pandas_selection_basics.py")