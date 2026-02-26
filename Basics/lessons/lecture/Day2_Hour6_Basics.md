# Hour 6: String Methods — Normalize, Search, Replace
Python Programming (Basic) • Day 2, Session 2

---

## Learning Outcomes
- Use common string methods
- Explain immutability: methods return new strings
- Apply methods for data cleaning

---

## Key String Methods

### Case Conversion
```python
text = "Hello World"

print(text.lower())    # 'hello world'
print(text.upper())    # 'HELLO WORLD'
print(text.title())    # 'Hello World'
```

### Important: Original is Unchanged!
```python
original = "Hello"
result = original.lower()
print(original)  # Still 'Hello'
print(result)    # 'hello'
```

---

## String Immutability

### Strings Cannot Be Modified In Place
```python
message = "Hello"
# ❌ This doesn't work:
# message[0] = "h"  # TypeError!

# ✓ Create a new string instead:
message = message.lower()
print(message)  # 'hello'
```

### Always Assign the Result Back
```python
name = "  alice  "
name = name.strip()  # Must assign!
print(name)  # 'alice'
```

---

## The strip() Method

### Remove Whitespace
```python
user_input = "   hello   "

print(user_input.strip())   # 'hello' (both sides)
print(user_input.lstrip())  # 'hello   ' (left only)
print(user_input.rstrip())  # '   hello' (right only)
```

### Why This Matters
User input often has extra spaces:
```python
name = input("Enter name: ")  # User types "  Alice  "
name = name.strip()
print(f"Hello, {name}!")  # "Hello, Alice!"
```

---

## The replace() Method

### Substitute Substrings
```python
message = "I like cats. Cats are great!"

new_message = message.replace("cats", "dogs")
print(new_message)
# 'I like dogs. Cats are great!'
# Note: case-sensitive!
```

### Multiple Replacements
```python
text = "a-b-c-d"
clean = text.replace("-", " ")
print(clean)  # 'a b c d'
```

---

## The find() Method

### Locate Substrings
```python
message = "Hello, Python!"

position = message.find("Python")
print(position)  # 7

# Returns -1 if not found
position = message.find("Java")
print(position)  # -1
```

### Using find() for Checking
```python
email = "user@example.com"
if email.find("@") != -1:
    print("Valid email format")
else:
    print("Missing @ symbol")
```

---

## Using 'in' for Containment

### Simpler Than find() for Checks
```python
message = "Hello, Python!"

# Using 'in' (preferred for simple checks)
if "Python" in message:
    print("Found it!")

# Using find()
if message.find("Python") != -1:
    print("Found it!")
```

### Best Practice
- Use `in` for True/False checks
- Use `find()` when you need the position

---

## Demo: Clean Messy Input

### Before and After Comparison
```python
# Messy user input
raw_input = "   HELLO world   "

# Clean it up
cleaned = raw_input.strip()      # Remove whitespace
cleaned = cleaned.lower()        # Lowercase
# Or chain methods:
cleaned = raw_input.strip().lower()

print(f"Before: '{raw_input}'")
print(f"After:  '{cleaned}'")
# Before: '   HELLO world   '
# After:  'hello world'
```

---

## Demo: find() Returning -1

### Handle "Not Found" Cases
```python
text = "Python programming"

# Found
pos = text.find("prog")
print(f"'prog' found at position: {pos}")  # 7

# Not found
pos = text.find("java")
print(f"'java' found at position: {pos}")  # -1

# Use the result
if pos == -1:
    print("Keyword not found")
```

---

## Lab: Text Sanitizer

**Time: 25-35 minutes**

### Tasks
- Input a sentence
- Strip whitespace, make lowercase
- Replace multiple spaces with single spaces (basic approach)
- Report whether a chosen keyword appears

### Example Interaction
```
Enter a sentence:    Hello   World   
Enter keyword to find: world
Cleaned: 'hello world'
Keyword 'world' found: True
```

---

## Lab: Sample Solution Structure

```python
# Get input
sentence = input("Enter a sentence: ")
keyword = input("Enter keyword to find: ")

# Clean the sentence
cleaned = sentence.strip().lower()
# Basic approach to reduce multiple spaces
cleaned = cleaned.replace("  ", " ")

# Check for keyword
keyword_lower = keyword.lower()
found = keyword_lower in cleaned

# Display results
print(f"Cleaned: '{cleaned}'")
print(f"Keyword '{keyword}' found: {found}")
```

---

## Completion Criteria (Hour 6)

✓ Outputs transformed sentence  
✓ Correctly reports keyword presence  
✓ Handles whitespace properly

---

## Common Pitfalls (Hour 6)

⚠️ **Expecting replace to modify in place**
```python
text = "hello"
text.replace("e", "a")  # Returns new string!
print(text)  # Still 'hello'
# Fix: text = text.replace("e", "a")
```

⚠️ **Confusing find() results**
```python
pos = text.find("xyz")
if pos:  # ❌ Wrong! 0 is falsy but valid
    print("Found")
# ✓ Correct:
if pos != -1:
    print("Found")
```

---

## Optional Extensions

- Add: count occurrences using `.count()`
- Add: title-case name fields

```python
text = "hello hello world"
count = text.count("hello")
print(f"'hello' appears {count} times")  # 2
```

---

## Quick Check

**Question**: Why do we assign back after calling a string method?

**Answer**: Because strings are immutable — methods return a *new* string; the original is unchanged unless we assign the result back to the variable.

---
