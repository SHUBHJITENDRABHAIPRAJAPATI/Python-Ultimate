"""
Lists in Python
===============
This file demonstrates list operations and methods.
"""

# Creating lists
print("=== Creating Lists ===")
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed list: {mixed}")

# Accessing elements
print("\n=== Accessing Elements ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# Slicing
print("\n=== List Slicing ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")
print(f"First 5 elements: {numbers[:5]}")
print(f"Last 5 elements: {numbers[-5:]}")
print(f"Elements 2 to 6: {numbers[2:7]}")
print(f"Every 2nd element: {numbers[::2]}")

# List methods
print("\n=== List Methods ===")
fruits = ["apple", "banana"]
print(f"Initial list: {fruits}")

fruits.append("cherry")
print(f"After append: {fruits}")

fruits.insert(1, "orange")
print(f"After insert at index 1: {fruits}")

fruits.remove("banana")
print(f"After removing banana: {fruits}")

last_fruit = fruits.pop()
print(f"Popped: {last_fruit}, List: {fruits}")

# List operations
print("\n=== List Operations ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(f"Combined: {combined}")

repeated = list1 * 3
print(f"Repeated: {repeated}")

# List comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Common list functions
print("\n=== Common List Functions ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"List: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sorted: {sorted(numbers)}")

# Sorting
numbers.sort()
print(f"After sort: {numbers}")

numbers.reverse()
print(f"After reverse: {numbers}")

# Checking membership
print("\n=== Membership ===")
print(f"Is 5 in list? {5 in numbers}")
print(f"Is 10 in list? {10 in numbers}")

print("\n✅ Lists demonstration complete!")
