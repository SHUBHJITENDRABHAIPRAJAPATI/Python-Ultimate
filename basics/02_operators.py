"""
Operators in Python
===================
This file demonstrates different types of operators in Python.
"""

# Arithmetic Operators
print("=== Arithmetic Operators ===")
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison Operators
print("\n=== Comparison Operators ===")
x = 5
y = 10

print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# Logical Operators
print("\n=== Logical Operators ===")
p = True
q = False

print(f"{p} and {q}: {p and q}")
print(f"{p} or {q}: {p or q}")
print(f"not {p}: {not p}")

# Assignment Operators
print("\n=== Assignment Operators ===")
num = 10
print(f"Initial value: {num}")

num += 5  # num = num + 5
print(f"After += 5: {num}")

num -= 3  # num = num - 3
print(f"After -= 3: {num}")

num *= 2  # num = num * 2
print(f"After *= 2: {num}")

num //= 4  # num = num // 4
print(f"After //= 4: {num}")

print("\n✅ Operators demonstration complete!")
