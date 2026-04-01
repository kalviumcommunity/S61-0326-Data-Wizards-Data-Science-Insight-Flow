"""
MILESTONE: Defining and Calling Python Functions
================================================

This module demonstrates how to define and call Python functions to write
clean, reusable, and organized code.

Learning Objectives:
- Understand what functions are and why they are useful
- Define functions using def
- Call functions with arguments
- Use parameters to make function logic reusable
- Understand basic function scope (local vs global)
"""

# =============================================================================
# SECTION 1: DEFINING A FUNCTION
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 1: DEFINING A FUNCTION")
print("=" * 70)


def greet_user():
    """Print a simple greeting message."""
    print("Hello! Welcome to the Python functions milestone.")


print("\n1.1 Function definition created: greet_user()")
print("A function is reusable code grouped under a clear name.")

# =============================================================================
# SECTION 2: CALLING A FUNCTION
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 2: CALLING A FUNCTION")
print("=" * 70)

print("\n2.1 Calling greet_user() twice:")
greet_user()
greet_user()

print("\n2.2 Execution flow demo:")


def execution_flow_demo():
    print("  Step A: Entered function")
    print("  Step B: Running function body")
    print("  Step C: Returning control to caller")


print("Before function call")
execution_flow_demo()
print("After function call")

# =============================================================================
# SECTION 3: USING PARAMETERS AND ARGUMENTS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 3: USING PARAMETERS AND ARGUMENTS")
print("=" * 70)


def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def describe_student(name, course, score):
    """Print a formatted student summary."""
    print(f"Student: {name} | Course: {course} | Score: {score}")


print("\n3.1 Calling add_numbers(first_number, second_number):")
sum_result = add_numbers(10, 15)
print(f"add_numbers(10, 15) = {sum_result}")

print("\n3.2 Calling describe_student(name, course, score):")
describe_student("Asha", "Python Fundamentals", 92)
describe_student("Rahul", "Data Science Basics", 88)

print("\n3.3 Argument order matters with positional arguments:")


def subtract_numbers(a, b):
    """Return a - b to show argument order behavior."""
    return a - b


print(f"subtract_numbers(10, 3) = {subtract_numbers(10, 3)}")
print(f"subtract_numbers(3, 10) = {subtract_numbers(3, 10)}")

# =============================================================================
# SECTION 4: BASIC FUNCTION SCOPE
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 4: BASIC FUNCTION SCOPE")
print("=" * 70)

message = "I am a global variable"


def scope_demo():
    local_note = "I exist only inside scope_demo()"
    print(f"Inside function -> global variable: {message}")
    print(f"Inside function -> local variable: {local_note}")


print("\n4.1 Accessing variables inside function:")
scope_demo()

print("\n4.2 Accessing global variable outside function:")
print(f"Outside function -> global variable: {message}")

print("\n4.3 Local variable lifetime reminder:")
print("The variable 'local_note' cannot be used outside scope_demo().")
print("This keeps function logic self-contained and prevents side effects.")

print("\n" + "=" * 70)
print("MILESTONE COMPLETE")
print("=" * 70)
print("You practiced defining, calling, and reusing Python functions safely.")