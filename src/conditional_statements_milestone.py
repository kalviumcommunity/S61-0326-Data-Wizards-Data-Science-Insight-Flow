"""
Milestone: Writing Conditional Statements for Data Logic
This script demonstrates:
- Basic if statement
- if–else branching
- if–elif–else for multiple conditions
- Logical operators (and, or, not)
Each section prints outputs to show decision paths.
"""

# 1. Basic if statement
number = 10
print("1. Basic if statement:")
if number > 5:
    print(f"{number} is greater than 5")
print()

# 2. if–else branching
print("2. if–else branching:")
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
print()

# 3. if–elif–else for multiple conditions
print("3. if–elif–else for multiple conditions:")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")
print()

# 4. Logical operators (and, or, not)
print("4. Logical operators:")
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed: Age >= 18 and has ID")

username = "admin"
if username == "admin" or username == "superuser":
    print("Access granted: admin or superuser")

is_active = False
if not is_active:
    print("User is not active (not operator)")

print("\nAll conditional logic examples complete.")
