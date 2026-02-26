# Day 2, Hour 5: String Fundamentals — Indexing, Slicing, len()
Python Programming (Basic) • Session 2 Opening

---

# Session 2 Overview

## Topics Covered in Session 2
- Hour 5: String fundamentals – indexing, slicing, len()
- Hour 6: String methods – normalize, search, replace
- Hour 7: Input/output + type conversion
- Hour 8: Checkpoint 1 – Fundamentals mini-assessment

---

# Hour 5: String Fundamentals — Indexing, Slicing, len()

## Learning Outcomes
- Index and slice strings
- Use len() and basic membership checks
- Understand negative indexing

---

## String Indexing Basics

### Indexing Starts at 0
```python
message = "Python"
print(message[0])   # 'P'
print(message[1])   # 'y'
print(message[5])   # 'n'
```

### Think of Indices as Positions
```
P   y   t   h   o   n
0   1   2   3   4   5
```

---

## Negative Indexing

### Counting from the End
```python
message = "Python"
print(message[-1])  # 'n' (last character)
print(message[-2])  # 'o' (second to last)
print(message[-6])  # 'P' (same as [0])
```

### Negative Index Reference
```
 P    y    t    h    o    n
 0    1    2    3    4    5
-6   -5   -4   -3   -2   -1
```

---

## String Slicing

### Basic Slicing: s[start:end]
```python
message = "Python"
print(message[0:3])   # 'Pyt' (start to end-1)
print(message[2:5])   # 'tho'
print(message[1:])    # 'ython' (start to end)
print(message[:4])    # 'Pyth' (beginning to end-1)
```

### Remember: End Index is Exclusive
The slice `s[a:b]` includes index `a` but excludes index `b`.

---

## The len() Function

### Getting String Length
```python
message = "Hello, World!"
print(len(message))   # 13

# Useful for bounds checking
last_index = len(message) - 1
print(message[last_index])  # '!'
```

### Empty String Check
```python
user_input = ""
if len(user_input) == 0:
    print("No input provided")
```

---

## Membership with 'in'

### Checking for Substrings
```python
message = "Hello, Python!"

# Check if substring exists
print("Python" in message)     # True
print("python" in message)     # False (case-sensitive)
print("Java" in message)       # False

# Use in conditions
if "Python" in message:
    print("Found Python!")
```

---

## Demo: Practical String Operations

### Extract Initials from a Name
```python
full_name = "Alice Smith"
first_initial = full_name[0]
# Find space position to get last name initial
space_index = full_name.find(" ")
last_initial = full_name[space_index + 1]
print(f"Initials: {first_initial}.{last_initial}.")
# Output: Initials: A.S.
```

---

## Demo: Extract Domain from Email

### Using Slicing and find()
```python
email = "student@example.com"
at_position = email.find("@")
domain = email[at_position + 1:]
print(f"Domain: {domain}")
# Output: Domain: example.com
```

### Get Last Character
```python
filename = "document.pdf"
extension = filename[-3:]
print(f"Extension: {extension}")
# Output: Extension: pdf
```

---

## Lab: Username Builder

**Time: 25-35 minutes**

### Tasks
- Input first and last name
- Build a username: first initial + last name (lowercase)
- Show username length

### Example Interaction
```
Enter first name: Alice
Enter last name: Smith
Username: asmith
Length: 6 characters
```

---

## Lab: Sample Solution Structure

```python
# Get input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# Build username
first_initial = first_name[0].lower()
last_clean = last_name.lower().replace(" ", "")
username = first_initial + last_clean

# Display result
print(f"Username: {username}")
print(f"Length: {len(username)} characters")
```

---

## Completion Criteria (Hour 5)

✓ Correct username for multi-word last names (strip spaces)  
✓ Handles at least one realistic name  
✓ Displays username length correctly

---

## Common Pitfalls (Hour 5)

⚠️ **IndexError from empty strings**
```python
name = ""
first_char = name[0]  # IndexError!
# Fix: Check length first
```

⚠️ **Not normalizing case/spacing**
```python
# Don't forget: "Van Halen" → "vanhalen"
```

---

## Optional Extensions

- Add a rule: if username > 12 chars, shorten last name
- Add a numeric suffix if desired

```python
# Example extension
if len(username) > 12:
    username = username[:12]
print(f"Username: {username}")
```

---

## Quick Check

**Question**: What does `s[-1]` do?

**Answer**: Returns the last character of string `s` (counting from the end with -1).

---
