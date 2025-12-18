"""
Control Flow in Python
=======================
This file demonstrates if-else statements and conditional logic.
"""

# Simple if statement
print("=== Simple if Statement ===")
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
print("\n=== if-else Statement ===")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

# if-elif-else statement
print("\n=== if-elif-else Statement ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if statements
print("\n=== Nested if Statements ===")
num = 12

if num > 0:
    print(f"{num} is positive")
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    print(f"{num} is not positive")

# Multiple conditions
print("\n=== Multiple Conditions ===")
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials")

# Ternary operator (conditional expression)
print("\n=== Ternary Operator ===")
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(f"{x} is {result}")

print("\n✅ Control Flow demonstration complete!")
