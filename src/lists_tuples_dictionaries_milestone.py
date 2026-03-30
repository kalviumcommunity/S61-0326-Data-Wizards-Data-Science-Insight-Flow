"""
MILESTONE: Working with Python Lists, Tuples, and Dictionaries
===============================================================

This module demonstrates Python's core collection data structures:
- Lists (ordered and mutable)
- Tuples (ordered and immutable)
- Dictionaries (key-value pairs, mutable)

Learning Objectives:
- Create and use lists, tuples, and dictionaries
- Access elements by index and by key
- Modify mutable structures safely
- Understand tuple immutability
- Choose the right structure for a task
"""

# =============================================================================
# SECTION 1: WORKING WITH PYTHON LISTS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 1: WORKING WITH PYTHON LISTS")
print("=" * 70)

print("\n1.1 CREATING A LIST")
print("-" * 70)

fruits = ["apple", "banana", "cherry", "mango"]
print(f"Original list: {fruits}")
print(f"Type: {type(fruits).__name__}")
print(f"Length: {len(fruits)}")

print("\n1.2 ACCESSING LIST ELEMENTS")
print("-" * 70)

print(f"First fruit (index 0): {fruits[0]}")
print(f"Third fruit (index 2): {fruits[2]}")
print(f"Last fruit (index -1): {fruits[-1]}")

safe_index = 5
if 0 <= safe_index < len(fruits):
    print(f"Fruit at index {safe_index}: {fruits[safe_index]}")
else:
    print(f"Index {safe_index} is out of range for the fruits list")

print("\n1.3 MODIFYING A LIST (MUTABLE)")
print("-" * 70)

fruits[1] = "blueberry"
print(f"After updating index 1: {fruits}")

fruits.append("orange")
print(f"After append('orange'): {fruits}")

fruits.insert(2, "kiwi")
print(f"After insert(2, 'kiwi'): {fruits}")

fruits.remove("apple")
print(f"After remove('apple'): {fruits}")

removed_item = fruits.pop()
print(f"After pop(): {fruits}")
print(f"Item removed by pop(): {removed_item}")

print("\n1.4 ITERATING THROUGH A LIST")
print("-" * 70)

for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# =============================================================================
# SECTION 2: WORKING WITH PYTHON TUPLES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 2: WORKING WITH PYTHON TUPLES")
print("=" * 70)

print("\n2.1 CREATING A TUPLE")
print("-" * 70)

rgb_color = (255, 140, 0)
print(f"Tuple value: {rgb_color}")
print(f"Type: {type(rgb_color).__name__}")
print(f"Length: {len(rgb_color)}")

print("\n2.2 ACCESSING TUPLE ELEMENTS")
print("-" * 70)

print(f"Red channel (index 0): {rgb_color[0]}")
print(f"Green channel (index 1): {rgb_color[1]}")
print(f"Blue channel (index 2): {rgb_color[2]}")

print("\n2.3 IMMUTABILITY BEHAVIOR")
print("-" * 70)

print("Attempting to modify tuple element rgb_color[0] = 0")
try:
    rgb_color[0] = 0
except TypeError as err:
    print(f"Tuple cannot be modified: {err}")

print("Tuples are useful when values should stay fixed.")

# =============================================================================
# SECTION 3: WORKING WITH PYTHON DICTIONARIES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 3: WORKING WITH PYTHON DICTIONARIES")
print("=" * 70)

print("\n3.1 CREATING A DICTIONARY")
print("-" * 70)

student = {
    "name": "Anika",
    "age": 21,
    "course": "Data Science",
    "is_active": True,
}

print(f"Dictionary value: {student}")
print(f"Type: {type(student).__name__}")

print("\n3.2 ACCESSING VALUES USING KEYS")
print("-" * 70)

print(f"Student name: {student['name']}")
print(f"Student course: {student['course']}")

print("Using get() for safer access:")
print(f"Email (missing key) with default: {student.get('email', 'not provided')}")

print("\n3.3 MODIFYING AND ADDING KEY-VALUE PAIRS")
print("-" * 70)

student["age"] = 22
print(f"After updating age: {student}")

student["city"] = "Bengaluru"
print(f"After adding city: {student}")

removed_course = student.pop("course")
print(f"After removing 'course': {student}")
print(f"Removed value: {removed_course}")

print("\n3.4 ITERATING THROUGH A DICTIONARY")
print("-" * 70)

for key, value in student.items():
    print(f"{key}: {value}")

# =============================================================================
# SECTION 4: CHOOSING THE RIGHT DATA STRUCTURE
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 4: CHOOSING THE RIGHT DATA STRUCTURE")
print("=" * 70)

use_cases = [
    "Store a changing shopping list -> list",
    "Store fixed coordinates (x, y) -> tuple",
    "Store student profile with named fields -> dictionary",
]

print("\n4.1 PRACTICAL CHOICES")
print("-" * 70)
for item in use_cases:
    print(item)

print("\n4.2 QUICK RULES")
print("-" * 70)
print("Use list when order matters and data may change.")
print("Use tuple when order matters and data should not change.")
print("Use dictionary when data has labels (keys) and named access is needed.")

print("\n" + "=" * 70)
print("MILESTONE COMPLETE")
print("=" * 70)
print("You practiced creating, accessing, and modifying Python collections.")
