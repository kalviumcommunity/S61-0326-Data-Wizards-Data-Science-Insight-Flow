"""
Loops and Iterative Data Processing Milestone
This module demonstrates:
- For loops for iteration over sequences
- While loops for condition-based repetition
- Break and continue statements to control loop flow
- How to avoid infinite loops
"""

print("=" * 70)
print("SECTION 1: FOR LOOPS - ITERATION FUNDAMENTALS")
print("=" * 70)

# 1.1 For loop with range - iterate over numbers
print("\n1.1 For Loop with Range (0 to 4):")
for i in range(5):
    print(f"  Iteration {i}")

# 1.2 For loop with custom range - start, stop, step
print("\n1.2 For Loop with Custom Range (2, 10, 2):")
for i in range(2, 10, 2):
    print(f"  Number: {i}")

# 1.3 For loop iterating over a list
print("\n1.3 For Loop Over a List:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"  - {fruit}")

# 1.4 For loop with index using enumerate
print("\n1.4 For Loop with Index (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# 1.5 Practical example: Sum numbers using for loop
print("\n1.5 Summing Numbers with For Loop:")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
    print(f"  Added {num}, Running total: {total}")
print(f"  Final sum: {total}")


print("\n" + "=" * 70)
print("SECTION 2: WHILE LOOPS - CONDITION-BASED REPETITION")
print("=" * 70)

# 2.1 Simple while loop - countdown
print("\n2.1 While Loop - Countdown:")
countdown = 5
while countdown > 0:
    print(f"  Countdown: {countdown}")
    countdown -= 1
print("  Blast off!")

# 2.2 While loop - condition changes based on user simulation
print("\n2.2 While Loop - Processing Until Target:")
current_value = 1
target = 16
print(f"  Starting at {current_value}, doubling until >= {target}")
while current_value < target:
    print(f"  Current value: {current_value}")
    current_value *= 2
print(f"  Target reached! Final value: {current_value}")

# 2.3 While loop with multiple conditions
print("\n2.3 While Loop with Multiple Conditions:")
count = 0
max_iterations = 5
is_active = True
while count < max_iterations and is_active:
    print(f"  Iteration {count}")
    count += 1
print("  Loop completed")

# 2.4 While loop - validating input simulation
print("\n2.4 While Loop - Input Validation Pattern:")
attempts = 0
max_attempts = 3
password = "python"
simulated_guess = None

# Simulating input attempts
guesses = ["java", "javascript", "python"]
attempts = 0

while attempts < max_attempts:
    simulated_guess = guesses[attempts]
    print(f"  Attempt {attempts + 1}: Trying '{simulated_guess}'")
    if simulated_guess == password:
        print(f"  ✓ Correct!")
        break
    attempts += 1
else:
    print("  ✗ Maximum attempts exceeded")


print("\n" + "=" * 70)
print("SECTION 3: CONTROLLING LOOP FLOW - BREAK AND CONTINUE")
print("=" * 70)

# 3.1 Using break to exit early
print("\n3.1 Using 'break' to Exit Loop Early:")
print("  Searching for value 5 in list:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(f"    Checking {num}...")
    if num == 5:
        print(f"    Found it! Breaking out.")
        break
print("  Loop ended early.")

# 3.2 Using continue to skip iterations
print("\n3.2 Using 'continue' to Skip Iterations:")
print("  Processing numbers, skipping even numbers:")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"    Skipping {num} (even)")
        continue
    print(f"    Processing {num} (odd)")

# 3.3 Practical example: Finding first number meeting condition
print("\n3.3 Practical Example - First Number > 15:")
values = [5, 10, 8, 20, 12, 25, 3]
for value in values:
    if value > 15:
        print(f"  Found: {value}")
        break
else:
    print("  No value found greater than 15")

# 3.4 Combining break and continue
print("\n3.4 Combining 'break' and 'continue':")
print("  Processing items, skipping 'skip' and stopping at 'stop':")
items = ["apple", "skip", "banana", "skip", "stop", "cherry"]
for item in items:
    if item == "skip":
        print(f"    Skipping '{item}'")
        continue
    if item == "stop":
        print(f"    Stopping at '{item}'")
        break
    print(f"    Processing '{item}'")


print("\n" + "=" * 70)
print("SECTION 4: AVOIDING INFINITE LOOPS")
print("=" * 70)

# 4.1 Common mistake: Forgetting to update loop variable
print("\n4.1 MISTAKE Example: Forgetting to Update Variable")
print("  (This code is commented out - it would loop forever)")
print("""
  # BAD CODE - Never do this!
  # while True:
  #     print("This will run forever!")
  #     # Forgot to add break condition
""")

# 4.2 Safe while loop with guaranteed termination
print("\n4.2 CORRECT: Ensuring Loop Terminates")
count = 0
max_count = 5
print(f"  Safe loop: incrementing {max_count} times")
while count < max_count:
    print(f"    Count: {count}")
    count += 1  # This ensures termination
print("  Loop safely completed")

# 4.3 Using a counter as insurance
print("\n4.3 PROTECTION: Loop Counter as Safety Net")
iterations = 0
max_iterations = 10
value = 100

while value > 0 and iterations < max_iterations:
    print(f"    Iteration {iterations}: value = {value}")
    value -= 30
    iterations += 1

if iterations >= max_iterations:
    print("  Safety limit reached! Prevented potential infinite loop")
else:
    print("  Loop completed normally")

# 4.4 Print to debug loops
print("\n4.4 DEBUGGING: Using Print Statements")
print("  Monitoring loop state to prevent infinite loops:")
x = 10
while x > 5:
    print(f"    x = {x}, condition (x > 5) is True, continuing...")
    x -= 2
    if x <= 5:
        print(f"    x = {x}, condition (x > 5) is False, exiting...")


print("\n" + "=" * 70)
print("SECTION 5: PRACTICAL DATA PROCESSING EXAMPLES")
print("=" * 70)

# 5.1 Processing a list of numbers
print("\n5.1 Processing List - Filter and Count:")
data = [2, 4, 5, 8, 10, 15, 20, 23, 30]
count_over_10 = 0
for value in data:
    if value > 10:
        count_over_10 += 1
print(f"  Numbers over 10: {count_over_10}")

# 5.2 Nested loops for 2D iteration
print("\n5.2 Nested Loops - Creating a Table:")
print("  Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"    {i} × {j} = {i*j}")

# 5.3 While loop for running total
print("\n5.3 While Loop - Running Total:")
numbers = [5, 10, 15, 20, 25]
index = 0
total = 0
while index < len(numbers):
    total += numbers[index]
    print(f"  Step {index}: Added {numbers[index]}, Total = {total}")
    index += 1

# 5.4 For-else construct
print("\n5.4 For-Else: Finding Items in List:")
search_list = ["red", "blue", "green", "yellow"]
target = "purple"
for color in search_list:
    if color == target:
        print(f"  Found '{target}'!")
        break
else:
    print(f"  '{target}' not found in list")


print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
Key Takeaways:

1. FOR LOOPS:
   - Use range(n) to iterate a specific number of times
   - Iterate directly over lists, strings, and other sequences
   - Use enumerate() to get both index and value
   
2. WHILE LOOPS:
   - Use when repetition depends on a condition
   - Always ensure the condition changes to avoid infinite loops
   - Update loop variables inside the loop
   
3. CONTROL FLOW:
   - break: Exit the loop immediately
   - continue: Skip to the next iteration
   - Both improve code readability and efficiency
   
4. AVOID INFINITE LOOPS:
   - Always update loop variables
   - Test conditions carefully
   - Use print statements to debug
   - Add safety counters if needed
   
5. ITERATION IN DATA PROCESSING:
   - Loops are essential for processing sequences
   - Combine loops with conditions for sophisticated data handling
   - Use nested loops for multi-dimensional iteration
""")

print("=" * 70)
print("End of demonstration")
print("=" * 70)
