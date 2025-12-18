"""
Dictionaries in Python
======================
This file demonstrates dictionary operations and methods.
"""

# Creating dictionaries
print("=== Creating Dictionaries ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")

# Another way to create a dictionary
student = dict(name="Bob", grade="A", subject="Math")
print(f"Student: {student}")

# Accessing values
print("\n=== Accessing Values ===")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'Not specified')}")  # Default value

# Modifying dictionaries
print("\n=== Modifying Dictionaries ===")
person["age"] = 26
print(f"Updated age: {person}")

person["profession"] = "Engineer"
print(f"Added profession: {person}")

# Dictionary methods
print("\n=== Dictionary Methods ===")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Iterating through dictionaries
print("\n=== Iterating Through Dictionary ===")
for key in person:
    print(f"{key}: {person[key]}")

print("\nUsing items():")
for key, value in person.items():
    print(f"{key}: {value}")

# Removing items
print("\n=== Removing Items ===")
temp_dict = {"a": 1, "b": 2, "c": 3}
print(f"Original: {temp_dict}")

removed = temp_dict.pop("b")
print(f"Removed 'b' (value: {removed}): {temp_dict}")

del temp_dict["a"]
print(f"Deleted 'a': {temp_dict}")

# Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Nested dictionaries
print("\n=== Nested Dictionaries ===")
school = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
    "student3": {"name": "Charlie", "grade": "A"}
}
print(f"School: {school}")
print(f"Student1 name: {school['student1']['name']}")

# Checking membership
print("\n=== Membership ===")
print(f"Is 'name' a key? {'name' in person}")
print(f"Is 'email' a key? {'email' in person}")

# Merging dictionaries (Python 3.9+)
print("\n=== Merging Dictionaries ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

print("\n✅ Dictionaries demonstration complete!")
