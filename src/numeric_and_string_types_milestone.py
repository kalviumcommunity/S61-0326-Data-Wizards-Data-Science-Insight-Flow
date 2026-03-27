"""
MILESTONE: Understanding Python Numeric and String Data Types
==============================================================

This module demonstrates core concepts of Python's numeric and string data types,
which form the foundation of data processing and analysis.

Learning Objectives:
- Differentiate between numeric and string data types
- Perform arithmetic using Python numbers
- Manipulate and format strings correctly
- Identify data type mismatches
- Write clearer and safer Python code
"""

# =============================================================================
# SECTION 1: WORKING WITH NUMERIC DATA TYPES
# =============================================================================

print("\n" + "="*70)
print("SECTION 1: WORKING WITH NUMERIC DATA TYPES")
print("="*70)

# 1.1 Integer Data Type
print("\n1.1 INTEGER DATA TYPE")
print("-" * 70)

age = 25  # Integer variable
temperature = -10  # Negative integer
distance = 0  # Zero value

print(f"Integer Examples:")
print(f"  age = {age} (type: {type(age).__name__})")
print(f"  temperature = {temperature} (type: {type(temperature).__name__})")
print(f"  distance = {distance} (type: {type(distance).__name__})")

# Arithmetic operations with integers
print("\nArithmetic Operations with Integers:")
sum_result = age + 5
difference = temperature - (-5)  # Subtracting negative
product = age * 2
quotient = age // 3  # Floor division (returns integer)
remainder = age % 3  # Modulo operation

print(f"  {age} + 5 = {sum_result}")
print(f"  {temperature} - (-5) = {difference}")
print(f"  {age} * 2 = {product}")
print(f"  {age} // 3 = {quotient} (floor division)")
print(f"  {age} % 3 = {remainder} (remainder/modulo)")

# 1.2 Float Data Type
print("\n1.2 FLOAT DATA TYPE")
print("-" * 70)

pi = 3.14159  # Float variable
balance = -25.50  # Negative float
weight = 70.5  # Weight with decimal

print(f"Float Examples:")
print(f"  pi = {pi} (type: {type(pi).__name__})")
print(f"  balance = {balance} (type: {type(balance).__name__})")
print(f"  weight = {weight} (type: {type(weight).__name__})")

# Arithmetic operations with floats
print("\nArithmetic Operations with Floats:")
area = pi * (5 ** 2)  # Circle area (pi * r²)
average = (70.5 + 75.2 + 68.9) / 3
divided = 10 / 3  # Regular division (always returns float)

print(f"  π * 5² = {area:.4f}")
print(f"  Average of 70.5, 75.2, 68.9 = {average:.2f}")
print(f"  10 / 3 = {divided}")  # Note: this is a float, not 3 (like //would give)

# 1.3 Important: Integer vs Float Division
print("\n1.3 INTEGER VS FLOAT DIVISION")
print("-" * 70)

print(f"  10 / 4 = {10 / 4} (true division, returns float)")
print(f"  10 // 4 = {10 // 4} (floor division, returns integer)")
print(f"  Type of 10 / 4: {type(10 / 4).__name__}")
print(f"  Type of 10 // 4: {type(10 // 4).__name__}")

# 1.4 Numeric Precision and Float Limitations
print("\n1.4 NUMERIC PRECISION")
print("-" * 70)

precise_value = 0.1 + 0.2
print(f"  0.1 + 0.2 = {precise_value}")
print(f"  Is 0.1 + 0.2 == 0.3? {precise_value == 0.3}")
print(f"  Note: Floating-point precision is limited in computers")

# Rounding floats
rounded = round(precise_value, 2)
formatted = f"{precise_value:.2f}"
print(f"  Using round(): {rounded}")
print(f"  Using format string: {formatted}")

# =============================================================================
# SECTION 2: UNDERSTANDING STRING DATA TYPES
# =============================================================================

print("\n" + "="*70)
print("SECTION 2: UNDERSTANDING STRING DATA TYPES")
print("="*70)

# 2.1 Creating Strings
print("\n2.1 CREATING STRING VARIABLES")
print("-" * 70)

name = "Alice"
city = 'New York'  # Single quotes work too
message = """This is a
multi-line
string"""

print(f"String Examples:")
print(f"  name = {name!r}")  # !r shows string with quotes
print(f"  city = {city!r}")
print(f"  Multi-line string = {message!r}")

# 2.2 String Length and Indexing
print("\n2.2 STRING LENGTH AND INDEXING")
print("-" * 70)

word = "Python"
print(f"String: '{word}'")
print(f"Length: {len(word)} characters")
print(f"Character at index 0: '{word[0]}'")
print(f"Character at index 5: '{word[5]}'")
print(f"Last character (index -1): '{word[-1]}'")

# 2.3 String Slicing
print("\n2.3 STRING SLICING")
print("-" * 70)

sentence = "Data Science"
print(f"Original string: '{sentence}'")
print(f"  sentence[0:4] = '{sentence[0:4]}'  (characters 0-3)")
print(f"  sentence[5:] = '{sentence[5:]}'    (from index 5 to end)")
print(f"  sentence[:4] = '{sentence[:4]}'    (from start to index 3)")
print(f"  sentence[::2] = '{sentence[::2]}'  (every 2nd character)")
print(f"  sentence[::-1] = '{sentence[::-1]}' (reversed)")

# 2.4 String Methods
print("\n2.4 COMMON STRING METHODS")
print("-" * 70)

text = "Hello World"
print(f"Original string: '{text}'")
print(f"  .lower(): '{text.lower()}'")
print(f"  .upper(): '{text.upper()}'")
print(f"  .replace('World', 'Python'): '{text.replace('World', 'Python')}'")
print(f"  .split(): {text.split()}")
print(f"  .strip(): ' hello '.strip() = '{' hello '.strip()}'")

# 2.5 String Concatenation
print("\n2.5 STRING CONCATENATION")
print("-" * 70)

first_name = "John"
last_name = "Doe"
age_str = "30"

full_name = first_name + " " + last_name
print(f"Concatenation with +:")
print(f"  '{first_name}' + ' ' + '{last_name}' = '{full_name}'")

# Better approach: using f-strings
info = f"{first_name} {last_name} is {age_str} years old"
print(f"\nUsing f-strings (better):")
print(f"  f\"{first_name} {last_name} is {age_str} years old\" = '{info}'")

# 2.6 String Formatting
print("\n2.6 STRING FORMATTING")
print("-" * 70)

price = 19.99
quantity = 5

# Different formatting methods
format1 = f"Price: ${price}, Quantity: {quantity}"
format2 = "Price: ${}, Quantity: {}".format(price, quantity)
format3 = "Price: $%.2f, Quantity: %d" % (price, quantity)

print(f"Using f-strings: {format1}")
print(f"Using .format(): {format2}")
print(f"Using % formatting: {format3}")

# =============================================================================
# SECTION 3: MIXING NUMBERS AND STRINGS SAFELY
# =============================================================================

print("\n" + "="*70)
print("SECTION 3: MIXING NUMBERS AND STRINGS SAFELY")
print("="*70)

# 3.1 Type Mismatch Errors
print("\n3.1 COMMON TYPE MISMATCH ERRORS")
print("-" * 70)

age_value = 25
age_string = "25"

print(f"Integer: {age_value} (type: {type(age_value).__name__})")
print(f"String: '{age_string}' (type: {type(age_string).__name__})")

# This works:
print(f"\nAddition with integers: {age_value} + 5 = {age_value + 5}")

# This will cause an error if attempted:
print(f"\nAttempting: age_string + 5")
print(f"Would result in: TypeError - cannot add str and int")
print(f"Why? '{age_string}' is text, not a number!")

# 3.2 Converting String to Number
print("\n3.2 CONVERTING STRINGS TO NUMBERS")
print("-" * 70)

num_string = "42"
num_string_float = "3.14"

# Convert string to integer
num_int = int(num_string)
print(f"int('{num_string}') = {num_int} (type: {type(num_int).__name__})")
print(f"  Now we can do math: {num_int} + 8 = {num_int + 8}")

# Convert string to float
num_float = float(num_string_float)
print(f"\nfloat('{num_string_float}') = {num_float} (type: {type(num_float).__name__})")
print(f"  Now we can do math: {num_float} * 2 = {num_float * 2}")

# 3.3 Converting Number to String
print("\n3.3 CONVERTING NUMBERS TO STRINGS")
print("-" * 70)

age_num = 25
price_num = 99.99

age_str = str(age_num)
price_str = str(price_num)

print(f"str({age_num}) = '{age_str}' (type: {type(age_str).__name__})")
print(f"str({price_num}) = '{price_str}' (type: {type(price_str).__name__})")

# Now we can concatenate:
message = f"The user is {age_str} years old"
print(f"\nConcatenation now works: '{message}'")

# 3.4 Practical Example: User Input Processing
print("\n3.4 PRACTICAL EXAMPLE: USER INPUT PROCESSING")
print("-" * 70)

# Simulating user input (normally from input())
user_input_age = "30"
user_input_salary = "50000.50"

# Convert to appropriate types
age = int(user_input_age)
salary = float(user_input_salary)

# Now we can do calculations
new_salary = salary * 1.10  # 10% raise
age_next_year = age + 1

print(f"User entered age: '{user_input_age}' → converted to {age}")
print(f"User entered salary: '{user_input_salary}' → converted to {salary}")
print(f"\nCalculations:")
print(f"  10% raise: {salary} * 1.10 = {new_salary}")
print(f"  Next year: {age} + 1 = {age_next_year}")

# 3.5 Safe Conversion with Error Handling
print("\n3.5 SAFE CONVERSION (ERROR HANDLING)")
print("-" * 70)

strings_to_convert = ["42", "invalid", "3.14", "25abc"]

print("Attempting to convert various strings to integers:\n")
for s in strings_to_convert:
    try:
        result = int(s)
        print(f"  ✓ int('{s}') = {result}")
    except ValueError:
        print(f"  ✗ int('{s}') = ERROR - cannot convert '{s}' to integer")

# =============================================================================
# SECTION 4: INSPECTING DATA TYPES
# =============================================================================

print("\n" + "="*70)
print("SECTION 4: INSPECTING DATA TYPES")
print("="*70)

# 4.1 Using type() Function
print("\n4.1 USING THE type() FUNCTION")
print("-" * 70)

variables = {
    "integer": 42,
    "float": 3.14,
    "string": "Hello",
    "boolean": True,
    "list": [1, 2, 3],
}

print("Inspecting variable types:\n")
for name, value in variables.items():
    data_type = type(value).__name__
    print(f"  {name:12} = {str(value):20} → type: {data_type}")

# 4.2 Using isinstance() Function
print("\n4.2 USING THE isinstance() FUNCTION")
print("-" * 70)

value = 25
print(f"Variable: value = {value}\n")
print(f"isinstance(value, int) = {isinstance(value, int)}")
print(f"isinstance(value, float) = {isinstance(value, float)}")
print(f"isinstance(value, str) = {isinstance(value, str)}")

# 4.3 Type Checking in Functions
print("\n4.3 TYPE CHECKING IN FUNCTIONS")
print("-" * 70)

def process_number(value):
    """Process a numeric value safely."""
    if isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, str):
        try:
            num = float(value)
            return num * 2
        except ValueError:
            return f"Error: '{value}' is not a valid number"
    else:
        return f"Error: Expected number or string, got {type(value).__name__}"

test_values = [10, 5.5, "20", "abc", [1, 2, 3]]

print("Testing process_number() with different types:\n")
for val in test_values:
    result = process_number(val)
    print(f"  process_number({val!r:15}) = {result}")

# =============================================================================
# SECTION 5: UNIFIED EXAMPLE - PROCESSING TEMPERATURE DATA
# =============================================================================

print("\n" + "="*70)
print("SECTION 5: UNIFIED EXAMPLE - TEMPERATURE DATA PROCESSING")
print("="*70)

# Raw temperature data (mixed types for learning)
temp_data_raw = {
    "Monday": 22,
    "Tuesday": "23.5",
    "Wednesday": 19,
    "Thursday": "25.8",
    "Friday": 21,
}

print("\nRaw temperature data (mixed int and string):")
for day, temp in temp_data_raw.items():
    print(f"  {day}: {temp!r} (type: {type(temp).__name__})")

# Processing: Convert all to float for calculations
temp_data_processed = {}
print("\nConverting all temperatures to float:")

for day, temp in temp_data_raw.items():
    if isinstance(temp, str):
        temp_float = float(temp)
        print(f"  {day}: '{temp}' → {temp_float}")
    else:
        temp_float = float(temp)
        print(f"  {day}: {temp} → {temp_float}")
    
    temp_data_processed[day] = temp_float

# Perform calculations
print("\nCalculations:")
temperatures = list(temp_data_processed.values())
avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

print(f"  Average: {temperatures} → {avg_temp:.2f}°C")
print(f"  Maximum: {max_temp:.1f}°C")
print(f"  Minimum: {min_temp:.1f}°C")

# Generate formatted report (mixing strings and numbers)
print("\nFormatted Report:")
print(f"  Weekly Temperature Summary")
print(f"  ├─ Average: {avg_temp:.2f}°C")
print(f"  ├─ Max: {max_temp:.1f}°C")
print(f"  └─ Min: {min_temp:.1f}°C")

report = f"\nThis week, the average temperature was {avg_temp:.2f}°C, with a high of {max_temp:.1f}°C and a low of {min_temp:.1f}°C."
print(report)

# =============================================================================
# SUMMARY AND KEY TAKEAWAYS
# =============================================================================

print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)

