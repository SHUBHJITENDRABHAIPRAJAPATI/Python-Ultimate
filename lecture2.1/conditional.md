
# Python Conditional Statements – Complete Beginner Guide (With Explanations)

Conditional statements allow a program to **make decisions** based on conditions.
They control the flow of execution using `if`, `elif`, and `else`.

---

## 1. `if` and `else` Statement
Used when there are **two possible outcomes**.

### Example: Voting Eligibility
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Explanation:
- The program takes the user's age as input.
- If the age is **18 or more**, the condition is `True`.
- If the condition is `False`, the `else` block runs.

👉 Only **one block** executes at a time.

---

## 2. `elif` Statement
Used when there are **multiple conditions** to check.

### Example: Grading System
```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
```

### Explanation:
- Conditions are checked **top to bottom**.
- The first condition that becomes `True` executes.
- If none are `True`, the `else` block runs.

👉 You can use **multiple `elif`**, but only **one `if` and one `else`**.

---

## 3. Nested `if-else`
A nested `if-else` means an `if` statement **inside another `if` or `else`**.

### Example: Positive, Negative, or Zero
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")
```

### Explanation:
- First, the program checks if the number is greater than zero.
- If not, it checks another condition inside `else`.
- This helps handle **complex decision-making**.

👉 Nested conditions should be used carefully to keep code readable.

---

## 4. Ternary Operator (Conditional Expression)
Used to write **simple if-else logic in one line**.

### Example: Even or Odd
```python
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)
```

### Explanation:
- Condition is written between the two values.
- If condition is `True`, first value is selected.
- If condition is `False`, second value is selected.

👉 Best for **short and simple conditions only**.

---

## 5. Comparison Operators Used in Conditions
| Operator | Meaning |
|--------|--------|
| == | Equal to |
| != | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

---

## 6. Logical Operators (Often Used with Conditions)
| Operator | Meaning |
|--------|--------|
| and | Both conditions must be true |
| or | At least one condition must be true |
| not | Reverses the condition |

---

## 7. Important Rules
- Indentation is **mandatory** in Python
- Conditions must return **True or False**
- `elif` is checked only if previous conditions fail
- `else` runs only when all conditions fail

---

## 8. Practice Questions
1. Check if a number is positive, negative, or zero  
2. Find the largest of three numbers  
3. Check if a year is a leap year  
4. Check if a number is divisible by 5 and 11  

---

Happy Coding 🚀
