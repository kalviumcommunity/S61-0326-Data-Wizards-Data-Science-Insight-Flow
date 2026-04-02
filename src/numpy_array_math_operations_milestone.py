
import numpy as np

print("=" * 70)
print("NUMPY FUNDAMENTALS: BASIC MATHEMATICAL OPERATIONS ON ARRAYS")
print("=" * 70)

# ============================================================================
# SECTION 1: ELEMENT-WISE ARRAY OPERATIONS
# ============================================================================
print("\n[1] ELEMENT-WISE ARRAY OPERATIONS")
print("-" * 70)

# Create two arrays of the same shape
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([10, 20, 30, 40, 50])

print(f"\nArray A: {array_a}")
print(f"Array B: {array_b}")

# Addition: Element-wise
result_add = array_a + array_b
print(f"\nAddition (A + B):\n{result_add}")
print(">> Each corresponding element is added together")

# Subtraction: Element-wise
result_subtract = array_b - array_a
print(f"\nSubtraction (B - A):\n{result_subtract}")
print(">> Each element of A is subtracted from B")

# Multiplication: Element-wise
result_multiply = array_a * array_b
print(f"\nMultiplication (A * B):\n{result_multiply}")
print(">> Each corresponding element is multiplied together")

# Division: Element-wise
result_divide = array_b / array_a
print(f"\nDivision (B / A):\n{result_divide}")
print(">> Each element of B is divided by corresponding element from A")

# Power operation: Element-wise
result_power = array_a ** 2
print(f"\nPower (A ** 2):\n{result_power}")
print(">> Each element is raised to the power of 2")

# ============================================================================
# SECTION 2: SCALAR OPERATIONS ON ARRAYS
# ============================================================================
print("\n[2] SCALAR OPERATIONS ON ARRAYS")
print("-" * 70)

array_x = np.array([5, 10, 15, 20, 25])
scalar = 5

print(f"\nArray X: {array_x}")
print(f"Scalar: {scalar}")

# Adding a scalar to an array
result_add_scalar = array_x + scalar
print(f"\nArray + Scalar ({array_x} + {scalar}):\n{result_add_scalar}")
print(">> Scalar is added to ALL elements")

# Subtracting a scalar
result_subtract_scalar = array_x - scalar
print(f"\nArray - Scalar ({array_x} - {scalar}):\n{result_subtract_scalar}")
print(">> Scalar is subtracted from ALL elements")

# Multiplying by a scalar
result_multiply_scalar = array_x * scalar
print(f"\nArray * Scalar ({array_x} * {scalar}):\n{result_multiply_scalar}")
print(">> All elements are multiplied by the scalar")

# Dividing by a scalar
result_divide_scalar = array_x / scalar
print(f"\nArray / Scalar ({array_x} / {scalar}):\n{result_divide_scalar}")
print(">> All elements are divided by the scalar")

# ============================================================================
# SECTION 3: NUMPY ARRAYS VS PYTHON LISTS - BEHAVIOR COMPARISON
# ============================================================================
print("\n[3] NUMPY ARRAYS vs PYTHON LISTS: KEY DIFFERENCES")
print("-" * 70)

# Python list behavior
list_1 = [1, 2, 3, 4, 5]
list_2 = [10, 20, 30, 40, 50]

print("\n--- PYTHON LIST BEHAVIOR ---")
print(f"List 1: {list_1}")
print(f"List 2: {list_2}")

# List addition (concatenation, NOT element-wise)
list_addition = list_1 + list_2
print(f"\nList Addition (List1 + List2):\n{list_addition}")
print(">> Lists concatenate (combine end-to-end), NOT element-wise!")

# List multiplication (repetition, NOT element-wise multiplication)
list_multiplication = list_1 * 2
print(f"\nList Multiplication (List1 * 2):\n{list_multiplication}")
print(">> Lists repeat themselves, NOT multiply elements!")

# NumPy array behavior (comparison)
print("\n--- NUMPY ARRAY BEHAVIOR (COMPARISON) ---")
array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([10, 20, 30, 40, 50])

print(f"Array 1: {array_1}")
print(f"Array 2: {array_2}")

# Array addition (element-wise)
array_addition = array_1 + array_2
print(f"\nArray Addition (Array1 + Array2):\n{array_addition}")
print(">> NumPy performs element-wise addition!")

# Array multiplication (element-wise)
array_multiplication = array_1 * 2
print(f"\nArray Multiplication (Array1 * 2):\n{array_multiplication}")
print(">> NumPy performs element-wise multiplication!")

print("\n[!] KEY TAKEAWAY:")
print("   - Python lists: + means concatenate, * means repeat")
print("   - NumPy arrays: + means element-wise add, * means element-wise multiply")

# ============================================================================
# SECTION 4: AVOIDING COMMON MISTAKES
# ============================================================================
print("\n[4] COMMON MISTAKES AND HOW TO AVOID THEM")
print("-" * 70)

print("\n[MISTAKE 1] Shape Mismatch in Element-Wise Operations")
print("-" * 70)

try:
    array_shape1 = np.array([1, 2, 3])  # Shape: (3,)
    array_shape2 = np.array([10, 20])   # Shape: (2,) - INCOMPATIBLE!
    result = array_shape1 + array_shape2
except ValueError as e:
    print(f"Error caught: {e}")
    print("\n[SOLUTION] Ensure arrays have matching shapes!")
    array_shape1 = np.array([1, 2, 3])
    array_shape2 = np.array([10, 20, 30])  # Now shape matches
    result = array_shape1 + array_shape2
    print(f"After fix: {result}")

print("\n[MISTAKE 2] Using Loops for Simple Array Math")
print("-" * 70)

print("\n[INEFFICIENT] Using a loop:")
array_data = np.array([1, 2, 3, 4, 5])
multiplied_slow = []
for element in array_data:
    multiplied_slow.append(element * 10)
print(f"Result (loop): {multiplied_slow}")
print("Problem: Slower, verbose, not Pythonic")

print("\n[EFFICIENT] Vectorized with NumPy:")
multiplied_fast = array_data * 10
print(f"Result (NumPy): {multiplied_fast}")
print("Benefit: Faster, concise, readable!")

print("\n[MISTAKE 3] Assuming Division Always Results in Float")
print("-" * 70)

array_int = np.array([10, 20, 30, 40, 50], dtype=np.int32)
print(f"Integer array: {array_int} (dtype: {array_int.dtype})")

result_division = array_int / 3
print(f"\nDivision result: {result_division}")
print(f"Result dtype: {result_division.dtype}")
print("Note: Division always produces float64, even if array was integer")

print("\n[MISTAKE 4] Mixing Broadcasting with Incompatible Shapes")
print("-" * 70)

try:
    matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Shape: (3, 3)
    vector_bad = np.array([1, 2, 3, 4])  # Shape: (4,) - INCOMPATIBLE!
    result = matrix_2d + vector_bad
except ValueError as e:
    print(f"Error: {e}")

print("\n[CORRECT] Using compatible shapes for broadcasting")
matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Shape: (3, 3)
vector_good = np.array([1, 2, 3])  # Shape: (3,) - COMPATIBLE!
result = matrix_2d + vector_good
print(f"Matrix:\n{matrix_2d}")
print(f"\nVector: {vector_good}")
print(f"\nResult (broadcasts):\n{result}")
print("Note: Vector added to each row of the matrix!")

# ============================================================================
# SECTION 5: PRACTICAL EXAMPLES WITH REAL-WORLD INTENT
# ============================================================================
print("\n[5] PRACTICAL EXAMPLES: REAL-WORLD SCENARIOS")
print("-" * 70)

print("\n[SCENARIO 1] Computing Sales Revenue")
print("-" * 70)

quantities = np.array([10, 25, 15, 30, 20])  # Units sold per product
prices = np.array([25.0, 50.0, 100.0, 75.0, 40.0])  # Price per unit

print(f"Quantities: {quantities}")
print(f"Prices: {prices}")

revenue = quantities * prices
print(f"\nRevenue (Qty × Price): {revenue}")
print(f"Total Revenue: ${revenue.sum():.2f}")

print("\n[SCENARIO 2] Temperature Conversion")
print("-" * 70)

celsius = np.array([0, 10, 20, 30, 100])
print(f"Celsius: {celsius}")

# Formula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"Fahrenheit: {fahrenheit}")
print("Formula applied element-wise to all temperatures!")

print("\n[SCENARIO 3] Percentage Discount Application")
print("-" * 70)

original_prices = np.array([100.0, 250.0, 75.0, 150.0])
discount_rate = 0.20  # 20% discount

print(f"Original Prices: ${original_prices}")
print(f"Discount: {discount_rate * 100}%")

discounted_prices = original_prices * (1 - discount_rate)
savings = original_prices - discounted_prices

print(f"Discounted Prices: ${discounted_prices}")
print(f"Savings per item: ${savings}")
print(f"Total Savings: ${savings.sum():.2f}")

# ============================================================================
# SECTION 6: KEY TAKEAWAYS
# ============================================================================
print("\n[6] KEY TAKEAWAYS")
print("-" * 70)

print("""
[CHECK] NumPy performs ELEMENT-WISE operations on arrays
  - Addition: [1,2,3] + [4,5,6] = [5,7,9]
  - Multiplication: [1,2,3] * 2 = [2,4,6]

[CHECK] Scalar operations apply to ALL elements
  - Simple and efficient for batch computation

[CHECK] NumPy arrays are fundamentally different from Python lists
  - Lists: + means concatenate, * means repeat
  - Arrays: + means add, * means multiply

[CHECK] Always ensure compatible shapes for operations
  - Use error messages to guide shape adjustments
  - Broadcasting extends rules for different shapes

[CHECK] Avoid loops for simple array math
  - Use vectorized operations instead
  - More efficient, more readable, more Pythonic

[CHECK] NumPy math is the foundation for data analysis
  - Prepare for pandas, scikit-learn, scipy
  - Master these basics before moving forward
""")

print("\n" + "=" * 70)
print("MILESTONE COMPLETE: NumPy Array Math Operations Mastered!")
print("=" * 70)
