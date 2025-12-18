"""
Functions in Python
===================
This file demonstrates how to define and use functions.
"""

# Simple function
def greet():
    """A simple function that prints a greeting."""
    print("Hello, welcome to Python!")

print("=== Simple Function ===")
greet()

# Function with parameters
def greet_person(name):
    """Function that greets a specific person."""
    print(f"Hello, {name}!")

print("\n=== Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    """Function that adds two numbers."""
    return a + b

print("\n=== Function with Return Value ===")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    """Function with default parameter value."""
    print(f"Hello, {title} {name}!")

print("\n=== Function with Default Parameters ===")
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# Function with keyword arguments
def describe_person(name, age, city):
    """Function demonstrating keyword arguments."""
    print(f"{name} is {age} years old and lives in {city}")

print("\n=== Keyword Arguments ===")
describe_person(name="Alice", age=25, city="New York")
describe_person(age=30, city="London", name="Bob")

# Function with *args (variable number of arguments)
def sum_all(*numbers):
    """Function that accepts variable number of arguments."""
    total = sum(numbers)
    return total

print("\n=== Variable Arguments (*args) ===")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs (keyword arguments)
def print_info(**info):
    """Function that accepts variable keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n=== Keyword Variable Arguments (**kwargs) ===")
print_info(name="Alice", age=25, profession="Engineer")

# Lambda function (anonymous function)
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"10 + 20 = {add(10, 20)}")

# Recursive function
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n=== Recursive Function ===")
print(f"Factorial of 5: {factorial(5)}")

print("\n✅ Functions demonstration complete!")
