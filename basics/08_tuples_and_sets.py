"""
Tuples and Sets in Python
==========================
This file demonstrates tuples and sets.
"""

# TUPLES - Immutable sequences
print("=== TUPLES ===")
print("\n--- Creating Tuples ---")
fruits_tuple = ("apple", "banana", "cherry")
numbers_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
single_element = (1,)  # Note the comma

print(f"Fruits: {fruits_tuple}")
print(f"Numbers: {numbers_tuple}")
print(f"Mixed: {mixed_tuple}")
print(f"Single element: {single_element}")

# Accessing tuple elements
print("\n--- Accessing Tuple Elements ---")
print(f"First fruit: {fruits_tuple[0]}")
print(f"Last fruit: {fruits_tuple[-1]}")

# Tuple unpacking
print("\n--- Tuple Unpacking ---")
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Tuple methods
print("\n--- Tuple Methods ---")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Tuples are immutable
print("\n--- Immutability ---")
print("Tuples cannot be modified after creation")
print("This makes them useful for fixed data")

# SETS - Unordered collections of unique elements
print("\n\n=== SETS ===")
print("\n--- Creating Sets ---")
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
print(f"Fruits set: {fruits_set}")
print(f"Numbers set: {numbers_set}")

# Sets automatically remove duplicates
print("\n--- Automatic Duplicate Removal ---")
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"Set with duplicates removed: {numbers_with_duplicates}")

# Adding and removing elements
print("\n--- Adding and Removing Elements ---")
colors = {"red", "green", "blue"}
print(f"Original: {colors}")

colors.add("yellow")
print(f"After add: {colors}")

colors.remove("green")
print(f"After remove: {colors}")

colors.discard("purple")  # Doesn't raise error if not found
print(f"After discard (element not present): {colors}")

# Set operations
print("\n--- Set Operations ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# Set methods
print("\n--- Set Methods ---")
print(f"Union (method): {set1.union(set2)}")
print(f"Intersection (method): {set1.intersection(set2)}")
print(f"Difference (method): {set1.difference(set2)}")

# Checking membership
print("\n--- Membership ---")
print(f"Is 3 in set1? {3 in set1}")
print(f"Is 10 in set1? {10 in set1}")

# Set comprehension
print("\n--- Set Comprehension ---")
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

print("\n✅ Tuples and Sets demonstration complete!")
