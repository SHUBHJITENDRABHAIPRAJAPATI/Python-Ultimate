
# Python Strings – Complete Beginner Guide (With Explanations)

## 1. What is a String?
A **string** is a sequence of characters used to store text in Python.
Strings are written inside **single (' ')**, **double (" ")**, or **triple quotes (''' ''' or """ """)**.

```python
name = "Shubh"
greeting = 'Hello'
```

👉 Strings can contain letters, numbers, spaces, and symbols.

---

## 2. Creating Strings
You can create strings in multiple ways:

```python
a = "Single quotes"
b = 'Double quotes'
c = '''Multiline
string'''
```

👉 Triple quotes are mainly used when text spans multiple lines.

---

## 3. Accessing Characters (Indexing)
Each character in a string has a position called an **index**.
Indexing always starts from **0**.

```python
word = "Python"
print(word[0])   # P
print(word[-1])  # n
```

👉 Negative indexing starts from the end of the string.

---

## 4. String Slicing
Slicing allows you to extract part of a string.

```python
text = "Programming"
print(text[0:6])   # Progra
print(text[:4])    # Prog
print(text[4:])    # ramming
```

👉 Syntax: `string[start:end]`  
👉 End index is **not included**.

---

## 5. String Length
The `len()` function returns the number of characters in a string.

```python
len("Python")  # 6
```

---

## 6. String Methods
String methods perform operations on strings.

```python
text = " hello world "

text.upper()                 # Converts to uppercase
text.lower()                 # Converts to lowercase
text.strip()                 # Removes extra spaces
text.replace("world", "Python")
text.split()                 # Splits string into list
```

👉 Strings are **immutable**, so methods return a new string.

---

## 7. String Concatenation
Concatenation means joining strings together.

```python
a = "Hello"
b = "World"
print(a + " " + b)
```

---

## 8. String Formatting

### f-strings (Recommended)
Used to insert variables directly into strings.

```python
name = "Shubh"
age = 19
print(f"My name is {name} and I am {age}")
```

### format() method
```python
print("My name is {} and I am {}".format(name, age))
```

---

## 9. Escape Characters
Escape characters allow special characters inside strings.

```python
print("He said, \"Hello\"")
print("Line1\nLine2")
```

👉 `\n` creates a new line  
👉 `\"` allows double quotes inside strings

---

## 10. String Membership
Used to check if a word exists inside a string.

```python
text = "Python Programming"
print("Python" in text)      # True
print("Java" not in text)    # True
```

---

## 11. Looping Through a String
You can loop through each character using a `for` loop.

```python
for char in "Python":
    print(char)
```

---

## 12. String Comparison
Strings can be compared using comparison operators.

```python
a = "apple"
b = "banana"
print(a == b)
print(a < b)
```

👉 Comparison is based on **alphabetical order (ASCII values)**.

---

## 13. Common String Functions

| Function | Description |
|--------|------------|
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| strip() | Removes spaces |
| split() | Splits string |
| replace() | Replaces text |
| find() | Finds position |
| count() | Counts occurrences |

---

## 14. Important Notes
- Strings are **immutable**
- Indexing starts from **0**
- Negative indexing works from the end

---

## 15. Practice Questions
1. Reverse a string  
2. Count vowels in a string  
3. Check if a string is palindrome  
4. Replace spaces with hyphens  

---

Happy Coding 🚀
