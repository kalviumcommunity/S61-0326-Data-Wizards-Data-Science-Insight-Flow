import numpy as np
import pandas as pd

print("=" * 72)
print("PANDAS FUNDAMENTALS: CREATING SERIES FROM LISTS AND NUMPY ARRAYS")
print("=" * 72)

# ============================================================================
# SECTION 1: UNDERSTANDING PANDAS SERIES
# ============================================================================
print("\n[1] UNDERSTANDING PANDAS SERIES")
print("-" * 72)

simple_series = pd.Series([10, 20, 30, 40])

print("\nA Pandas Series is 1D labeled data (values + index labels).")
print("Series created:")
print(simple_series)

print("\nType:", type(simple_series))
print("Values:", simple_series.values)
print("Index:", simple_series.index)
print("Default index labels are created automatically: 0, 1, 2, ...")

# ============================================================================
# SECTION 2: CREATING SERIES FROM PYTHON LISTS
# ============================================================================
print("\n[2] CREATING SERIES FROM PYTHON LISTS")
print("-" * 72)

scores_list = [85, 90, 78, 92]
scores_series = pd.Series(scores_list)

print("\nPython list:", scores_list)
print("Series from list (default index):")
print(scores_series)

# Optional custom labels to add meaning
subjects_series = pd.Series(scores_list, index=["Math", "Science", "English", "History"])
print("\nSeries from list (custom index labels):")
print(subjects_series)

# ============================================================================
# SECTION 3: CREATING SERIES FROM NUMPY ARRAYS
# ============================================================================
print("\n[3] CREATING SERIES FROM NUMPY ARRAYS")
print("-" * 72)

temperature_array = np.array([28.5, 30.0, 31.2, 29.4], dtype=np.float64)
temperature_series = pd.Series(temperature_array, index=["Mon", "Tue", "Wed", "Thu"])

print("\nNumPy array:", temperature_array)
print("Array dtype:", temperature_array.dtype)

print("\nSeries from NumPy array:")
print(temperature_series)
print("Series values dtype:", temperature_series.values.dtype)
print("Data type is preserved from NumPy array.")

# ============================================================================
# SECTION 4: INDEX AND VALUES IN A SERIES
# ============================================================================
print("\n[4] UNDERSTANDING INDEX AND VALUES")
print("-" * 72)

print("\nSeries index:", temperature_series.index)
print("Series values:", temperature_series.values)

print("\nPositional access with iloc:")
print("temperature_series.iloc[0] ->", temperature_series.iloc[0])
print("temperature_series.iloc[2] ->", temperature_series.iloc[2])

print("\nLabel-based access with loc:")
print("temperature_series.loc['Mon'] ->", temperature_series.loc["Mon"])
print("temperature_series.loc['Wed'] ->", temperature_series.loc["Wed"])

# ============================================================================
# SECTION 5: SIMPLE OPERATIONS + NUMPY COMPARISON
# ============================================================================
print("\n[5] SIMPLE OPERATIONS + NUMPY COMPARISON")
print("-" * 72)

print("\nAdd 2 to each value (vectorized operation):")
print("NumPy array + 2 ->", temperature_array + 2)
print("Series + 2:")
print(temperature_series + 2)

print("\nMean temperature using Series:", temperature_series.mean())

print("\nFilter values > 30:")
print(temperature_series[temperature_series > 30])

print("\nLabel-aware alignment example:")
series_a = pd.Series([100, 200, 300], index=["a", "b", "c"])
series_b = pd.Series([1, 2, 3], index=["c", "b", "a"])

print("Series A:")
print(series_a)
print("Series B:")
print(series_b)

print("\nA + B aligns by labels, not by position:")
print(series_a + series_b)

array_a = np.array([100, 200, 300])
array_b = np.array([1, 2, 3])
print("\nNumPy arrays add by position:", array_a + array_b)

# ============================================================================
# SECTION 6: KEY TAKEAWAYS
# ============================================================================
print("\n[6] KEY TAKEAWAYS")
print("-" * 72)

print("""
[CHECK] Pandas Series is one-dimensional labeled data.
[CHECK] You can create Series from Python lists and NumPy arrays.
[CHECK] Series has two core parts: index (labels) and values (data).
[CHECK] .iloc uses position; .loc uses labels.
[CHECK] Series operations are label-aware, which helps avoid data mismatch.
[CHECK] Series is a building block for DataFrames.
""")

print("Run this file with:")
print("python src/pandas_series_from_lists_arrays_milestone.py")
