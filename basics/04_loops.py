"""
Loops in Python
===============
This file demonstrates for loops and while loops.
"""

# For loop with range
print("=== For Loop with Range ===")
for i in range(5):
    print(f"Count: {i}")

# For loop with range (start, stop, step)
print("\n=== For Loop with Range (start, stop, step) ===")
for i in range(2, 10, 2):
    print(f"Even number: {i}")

# For loop with list
print("\n=== For Loop with List ===")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with enumerate
print("\n=== For Loop with Enumerate ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# While loop
print("\n=== While Loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
print("\n=== While Loop with Condition ===")
number = 1
sum_total = 0
while number <= 10:
    sum_total += number
    number += 1
print(f"Sum of numbers 1 to 10: {sum_total}")

# Break statement
print("\n=== Break Statement ===")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"Number: {i}")

# Continue statement
print("\n=== Continue Statement ===")
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(f"Number: {i}")

# Nested loops
print("\n=== Nested Loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}", end="  ")
    print()  # New line after inner loop

print("\n✅ Loops demonstration complete!")
