"""
Solutions - Basics Exercises
=============================
Solutions to the practice exercises in basics_exercises.py
"""

# Exercise 1: Variable Swap
print("=" * 50)
print("Exercise 1: Variable Swap")
print("=" * 50)
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Solution: Using tuple unpacking
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Alternative: Using arithmetic
# a = a + b
# b = a - b
# a = a - b
print()

# Exercise 2: Temperature Converter
print("=" * 50)
print("Exercise 2: Temperature Converter")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"37°C = {celsius_to_fahrenheit(37)}°F")
print()

# Exercise 3: Even or Odd
print("=" * 50)
print("Exercise 3: Even or Odd")
print("=" * 50)

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")
print()

# Exercise 4: Sum of Numbers
print("=" * 50)
print("Exercise 4: Sum of Numbers")
print("=" * 50)

def sum_to_n(n):
    """Calculate sum of numbers from 1 to n."""
    return sum(range(1, n + 1))
    # Alternative: return n * (n + 1) // 2

print(f"sum_to_n(10): {sum_to_n(10)}")
print(f"sum_to_n(100): {sum_to_n(100)}")
print()

# Exercise 5: Factorial
print("=" * 50)
print("Exercise 5: Factorial")
print("=" * 50)

def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")
print()

# Exercise 6: Palindrome Checker
print("=" * 50)
print("Exercise 6: Palindrome Checker")
print("=" * 50)

def is_palindrome(text):
    """Check if text is a palindrome."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")
print(f"is_palindrome('madam'): {is_palindrome('madam')}")
print()

# Exercise 7: List Maximum
print("=" * 50)
print("Exercise 7: List Maximum")
print("=" * 50)

def find_max(numbers):
    """Find maximum value in a list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(f"find_max([3, 7, 2, 9, 1]): {find_max([3, 7, 2, 9, 1])}")
print()

# Exercise 8: Count Vowels
print("=" * 50)
print("Exercise 8: Count Vowels")
print("=" * 50)

def count_vowels(text):
    """Count number of vowels in text."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(f"count_vowels('Hello World'): {count_vowels('Hello World')}")
print(f"count_vowels('Python Programming'): {count_vowels('Python Programming')}")
print()

# Exercise 9: Fibonacci Sequence
print("=" * 50)
print("Exercise 9: Fibonacci Sequence")
print("=" * 50)

def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(f"fibonacci(10): {fibonacci(10)}")
print()

# Exercise 10: Prime Number Checker
print("=" * 50)
print("Exercise 10: Prime Number Checker")
print("=" * 50)

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(f"is_prime(7): {is_prime(7)}")
print(f"is_prime(10): {is_prime(10)}")
print(f"is_prime(17): {is_prime(17)}")
print(f"is_prime(20): {is_prime(20)}")
print()

print("=" * 50)
print("All exercises completed!")
print("=" * 50)
