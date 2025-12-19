"""
Variables and Data Types in Python
===================================
This file demonstrates basic variables and data types in Python.
"""

# Variables - containers for storing data values
# Python is dynamically typed, so you don't need to declare variable types

# Integer - whole numbers
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float - decimal numbers
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String - text data
name = "Python Learner"
print(f"Name: {name}, Type: {type(name)}")

# Boolean - True or False
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Multiple assignments
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# Type conversion
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' converted to integer: {num_int}")

float_num = 45.67
int_num = int(float_num)
print(f"Float {float_num} converted to integer: {int_num}")

# String operations
first_name = "Python"
last_name = "Ultimate"
full_name = first_name + " " + last_name  # Concatenation
print(f"Full name: {full_name}")

# String repetition
stars = "*" * 10
print(stars)

print("\n✅ Variables and Data Types demonstration complete!")
