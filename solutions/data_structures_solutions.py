"""
Solutions - Data Structures Exercises
======================================
Solutions to the practice exercises in data_structures_exercises.py
"""

# Exercise 1: Filter Even Numbers
print("=" * 50)
print("Exercise 1: Filter Even Numbers")
print("=" * 50)

def filter_evens(numbers):
    """Return only even numbers from the list."""
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Input: {numbers}")
print(f"Output: {filter_evens(numbers)}")
print()

# Exercise 2: Merge Dictionaries
print("=" * 50)
print("Exercise 2: Merge Dictionaries")
print("=" * 50)

def merge_dicts(dict1, dict2):
    """Merge two dictionaries."""
    return {**dict1, **dict2}
    # Alternative: dict1.update(dict2); return dict1

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Merged: {merge_dicts(dict1, dict2)}")
print()

# Exercise 3: Remove Duplicates
print("=" * 50)
print("Exercise 3: Remove Duplicates")
print("=" * 50)

def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

items = [1, 2, 2, 3, 4, 4, 5]
print(f"Input: {items}")
print(f"Output: {remove_duplicates(items)}")
print()

# Exercise 4: Word Frequency
print("=" * 50)
print("Exercise 4: Word Frequency Counter")
print("=" * 50)

def word_frequency(sentence):
    """Count frequency of each word."""
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence = "the quick brown fox jumps over the lazy dog"
print(f"Sentence: {sentence}")
print(f"Frequency: {word_frequency(sentence)}")
print()

# Exercise 5: List Intersection
print("=" * 50)
print("Exercise 5: List Intersection")
print("=" * 50)

def list_intersection(list1, list2):
    """Find common elements between two lists."""
    return list(set(list1) & set(list2))
    # Alternative: [x for x in list1 if x in list2]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Intersection: {list_intersection(list1, list2)}")
print()

# Exercise 6: Reverse Dictionary
print("=" * 50)
print("Exercise 6: Reverse Dictionary")
print("=" * 50)

def reverse_dict(d):
    """Swap keys and values in dictionary."""
    return {value: key for key, value in d.items()}

original = {"a": 1, "b": 2, "c": 3}
print(f"Original: {original}")
print(f"Reversed: {reverse_dict(original)}")
print()

# Exercise 7: Flatten Nested List
print("=" * 50)
print("Exercise 7: Flatten Nested List")
print("=" * 50)

def flatten(nested_list):
    """Flatten a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

nested = [[1, 2], [3, 4], [5, 6]]
print(f"Nested: {nested}")
print(f"Flattened: {flatten(nested)}")
print()

# Exercise 8: Group by Length
print("=" * 50)
print("Exercise 8: Group Words by Length")
print("=" * 50)

def group_by_length(words):
    """Group words by their length."""
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

words = ["cat", "dog", "fish", "bird"]
print(f"Words: {words}")
print(f"Grouped: {group_by_length(words)}")
print()

# Exercise 9: Sort Dictionary by Value
print("=" * 50)
print("Exercise 9: Sort Dictionary by Value")
print("=" * 50)

def sort_dict_by_value(d):
    """Sort dictionary by values."""
    return dict(sorted(d.items(), key=lambda item: item[1]))

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
print(f"Original: {scores}")
print(f"Sorted: {sort_dict_by_value(scores)}")
print()

# Exercise 10: Find Missing Number
print("=" * 50)
print("Exercise 10: Find Missing Number")
print("=" * 50)

def find_missing(numbers):
    """Find the first missing number in sequence."""
    if not numbers:
        return None
    
    full_set = set(range(min(numbers), max(numbers) + 1))
    number_set = set(numbers)
    missing = full_set - number_set
    
    # Return the smallest missing number if any exist
    return min(missing) if missing else None

numbers = [1, 2, 3, 5, 6, 7]
print(f"Numbers: {numbers}")
print(f"Missing: {find_missing(numbers)}")
print()

print("=" * 50)
print("All exercises completed!")
print("=" * 50)
