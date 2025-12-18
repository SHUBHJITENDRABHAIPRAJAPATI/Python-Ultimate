"""
Error Handling in Python
=========================
This file demonstrates exception handling with try-except blocks.
"""

# Basic try-except
print("=== Basic Try-Except ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Try-except with multiple exceptions
print("\n=== Multiple Exceptions ===")
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid value for conversion!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# Catching multiple exception types
print("\n=== Catching Multiple Exception Types ===")
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except (IndexError, KeyError) as e:
    print(f"Error: {e}")

# Try-except-else
print("\n=== Try-Except-Else ===")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful! Result: {result}")

# Try-except-finally
print("\n=== Try-Except-Finally ===")
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes (cleanup code)")

# Raising exceptions
print("\n=== Raising Exceptions ===")

def check_age(age):
    """Check if age is valid."""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        print("You are a minor")
    else:
        print("You are an adult")

try:
    check_age(25)
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# Custom exceptions
print("\n=== Custom Exceptions ===")

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

def withdraw_money(balance, amount):
    """Withdraw money from account."""
    if amount > balance:
        raise InsufficientFundsError("Not enough money in account!")
    return balance - amount

try:
    balance = 100
    balance = withdraw_money(balance, 50)
    print(f"Withdrawal successful! Remaining balance: ${balance}")
    balance = withdraw_money(balance, 100)
except InsufficientFundsError as e:
    print(f"Error: {e}")

# Getting exception details
print("\n=== Exception Details ===")
try:
    result = 10 / 0
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")

# Using assertions
print("\n=== Assertions ===")

def calculate_average(numbers):
    """Calculate average of numbers."""
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([10, 20, 30])
    print(f"Average: {avg}")
    
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion Error: {e}")

print("\n✅ Error Handling demonstration complete!")
