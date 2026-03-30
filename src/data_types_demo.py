age = 25
height = 5.9

print(" Numeric Data Types")
print(f"Age: {age}")
print(f"Height: {height}")

addition = age + 5
subtraction = age - 3
multiplication = age * 2
division = age / 2
floor_division = age // 2

print("\nArithmetic Operations")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")

name = "Alice"
greeting = "Hello"

print("\n String Data Types")
print(f"Name: {name}")
print(f"Greeting: {greeting}")

full_greeting = greeting + ", " + name + "!"
print(f"Message: {full_greeting}")

print(f"\nFormatted: {greeting}, my name is {name} and I am {age} years old.")
print(f"First letter: {name[0]}")
print(f"Length of name: {len(name)}")

print("\n Mixing Numbers and Strings")

print("Example error (not executed): 'My age is ' + age")

age_str = str(age)
height_str = str(height)

print(f"Age as string: {age_str} ({type(age_str)})")
print(f"Height as string: {height_str} ({type(height_str)})")

message = "My age is " + age_str + " and height is " + height_str
print(f"Combined: {message}")

age_input = "30"
height_input = "6.1"

age_num = int(age_input)
height_num = float(height_input)

print("\nConverted values:")
print(f"Age: {age_num}")
print(f"Height: {height_num}")

print(f"New age total: {age + age_num}")
print(f"New height total: {height + height_num}")

print("\n Checking Data Types ")
print(type(age))
print(type(height))
print(type(name))
print(type(greeting))

numbers = [age, height, addition, division]
strings = [name, greeting, full_greeting]

print("Numeric types:", [type(x) for x in numbers])
print("String types:", [type(x) for x in strings])

print("\nWhy types matter:")
print("They help avoid errors, make debugging easier, and ensure correct operations.")