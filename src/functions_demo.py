# Function to greet a person by name
def greet(name):
    message = "Hello, " + name + "!"
    print(message)

# Function to add two numbers
def add(a, b):
    result = a + b
    return result

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Global variable accessible everywhere
global_var = "I am global"

# Function to demonstrate local and global variables
def show_scope():
    local_var = "I am local"
    print("Inside function: " + local_var)
    print("Inside function: " + global_var)

# Print global variable before calling function
print("Global variable outside function: " + global_var)

# Call greet function
greet("Alice")

# Call add function and print result
sum_result = add(5, 3)
print("Sum of 5 and 3 is:", sum_result)

# Call calculate_area function and print result
area_result = calculate_area(4, 6)
print("Area of rectangle with length 4 and width 6 is:", area_result)

# Call is_even function and print results
even_check1 = is_even(10)
print("Is 10 even?", even_check1)

even_check2 = is_even(7)
print("Is 7 even?", even_check2)

# Call show_scope function
show_scope()

# Print global variable after function call
print("Global variable after function call: " + global_var)

# Explanation of functions
print("\nFunctions are like reusable blocks of code that perform specific tasks.")
print("They help organize code, avoid repetition, and make programs easier to understand.")
print("When you call a function, the code inside it runs, and then execution returns to where it was called.")
print("Parameters let functions work with different inputs each time.")
print("Local variables exist only inside the function, while global ones are accessible everywhere.")

# Instructions to run the script
print("\nTo run this script, open a terminal and type: python functions_demo.py")