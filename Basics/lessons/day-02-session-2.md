# Basics Day 2 — Session 2 (Hours 5–8)
Python Programming (Basic) • Strings, I/O, and Fundamentals Checkpoint

---

# Session 2 Overview

## Topics Covered Today
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

# Hour 6: String Methods — Normalize, Search, Replace

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

# Hour 7: Input/Output + Type Conversion

## Learning Outcomes
- Collect user input and convert types safely (happy path)
- Explain why input() returns a string
- Apply int() and float() for numeric conversions

---

## The input() Function

### Always Returns a String
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(type(name))  # <class 'str'>

age = input("Enter your age: ")
print(type(age))   # <class 'str'> - NOT int!
```

### Why This Matters
```python
age = input("Enter your age: ")  # User types 25
# age is "25", not 25
next_year = age + 1  # TypeError!
```

---

## Type Conversion Functions

### Converting to Numbers
```python
# String to integer
age_str = "25"
age = int(age_str)
print(age + 1)  # 26

# String to float
price_str = "19.99"
price = float(price_str)
print(price * 2)  # 39.98
```

### Converting Input Directly
```python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

---

## Common Conversion Patterns

### Safe Patterns for Numeric Input
```python
# Integer input
quantity = int(input("How many? "))

# Float input
temperature = float(input("Temperature: "))

# Combine operations
print(f"Double: {quantity * 2}")
```

### When Conversion Fails
```python
# If user types "abc" instead of a number:
# ValueError: invalid literal for int()
```

---

## ValueError Preview

### What Happens with Bad Input
```python
# User enters "hello" when asked for a number
number = int("hello")  # ValueError!
```

### For Now: Assume Valid Input
- In this hour, we practice the "happy path"
- Full error handling comes later (exceptions)
- Mention: "We'll learn to handle bad input later"

---

## Demo: Simple Converter

### Show Type Conversion in Action
```python
# Temperature converter (F to C)
fahrenheit = input("Enter temperature in °F: ")
print(f"Input type: {type(fahrenheit)}")

# Convert to float for math
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9

print(f"Fahrenheit type: {type(fahrenheit)}")
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

---

## Demo: Show ValueError

### What Happens with Non-Numeric Input
```python
# This will crash if user enters text
number = int("3.5")  # ValueError!
# Can't convert "3.5" directly to int

# Correct approach:
number = int(float("3.5"))  # 3
# Or just use float if decimals expected
```

---

## Lab: Unit Converter

**Time: 25-35 minutes**

### Tasks
- Choose: miles→km OR °F→°C
- Ask user for a number
- Convert and print formatted output

### Conversion Formulas
- Miles to km: `km = miles * 1.60934`
- °F to °C: `celsius = (fahrenheit - 32) * 5 / 9`

---

## Lab: Example Interaction

### Miles to Kilometers
```
=== Miles to Kilometers Converter ===
Enter distance in miles: 10
10.0 miles = 16.09 kilometers
```

### Fahrenheit to Celsius
```
=== Temperature Converter ===
Enter temperature in °F: 98.6
98.6°F = 37.0°C
```

---

## Lab: Sample Solution Structure

```python
# Miles to Kilometers
print("=== Miles to Kilometers Converter ===")
miles = float(input("Enter distance in miles: "))

# Convert
km = miles * 1.60934

# Display with formatting
print(f"{miles} miles = {km:.2f} kilometers")
```

---

## Lab: Alternative Solution (Temperature)

```python
# Fahrenheit to Celsius
print("=== Temperature Converter ===")
fahrenheit = float(input("Enter temperature in °F: "))

# Convert
celsius = (fahrenheit - 32) * 5 / 9

# Display with formatting
print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

---

## Completion Criteria (Hour 7)

✓ Correct conversion on sample input  
✓ Readable output with units  
✓ Uses proper type conversion

---

## Common Pitfalls (Hour 7)

⚠️ **ValueError when user types text**
```python
# Remind learners: for now, assume valid input
# We'll handle errors properly later
```

⚠️ **Hard-coded constants wrong**
```python
# Double-check your conversion factors!
# Miles to km: 1.60934
# F to C: (f - 32) * 5/9
```

---

## Optional Extensions

- Add a menu to choose conversion type (no loops yet)

```python
print("1. Miles to Kilometers")
print("2. Fahrenheit to Celsius")
choice = input("Choose (1 or 2): ")

if choice == "1":
    # miles conversion
    pass
elif choice == "2":
    # temperature conversion
    pass
```

---

## Quick Check

**Question**: What happens if you call `int()` on `'3.5'`?

**Answer**: `ValueError` — Python cannot convert a string with a decimal point directly to int. Use `int(float('3.5'))` if you need the integer value (3).

---

# Hour 8: Checkpoint 1 — Fundamentals Mini-Assessment

## Learning Outcomes
- Demonstrate basic script writing, variables, numbers, strings, and input
- Apply concepts from Hours 1–7 in a practical exercise
- Self-assess understanding of Python fundamentals

---

## Checkpoint Overview

### Assessment Format
- **Open-book**: Notes and slides allowed
- **Individual**: Complete your own work
- **Timeboxed**: 45–60 minutes for the lab
- **Focus**: Correctness first, then formatting

---

## Instructor Talk Points

### Before Starting
- Explain the rules: open-book, individual, timeboxed
- Remind: focus on **correctness first**, then formatting
- Encourage: test with sample inputs before submitting

### During Assessment
- Circulate and observe (don't solve for them)
- Note common struggles for debrief
- Allow questions about requirements, not solutions

---

## Demo: Sample Rubric Walkthrough

### How Submissions Will Be Evaluated
1. **Runs without errors** (40%)
   - Program executes end-to-end
   - No crashes on valid input

2. **Correct calculations** (30%)
   - Math is accurate
   - Type conversions done properly

3. **Readable output** (20%)
   - Formatted nicely
   - Clear labels for values

4. **Code quality** (10%)
   - Meaningful variable names
   - Appropriate comments

---

## Checkpoint Lab: Simple Receipt Generator

**Time: 45-60 minutes**

### Requirements
- Input: item name, quantity, price per item
- Compute subtotal and total
- Print a receipt with aligned lines and 2-decimal money formatting

---

## Receipt Generator: Expected Output

### Example Interaction
```
=== Receipt Generator ===
Enter item name: Widget
Enter quantity: 3
Enter price per item: 9.99

========== RECEIPT ==========
Item:     Widget
Quantity: 3
Price:    $9.99 each
-----------------------------
Subtotal: $29.97
=============================
```

---

## Receipt Generator: Sample Solution

```python
# Receipt Generator
print("=== Receipt Generator ===")

# Get input
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

# Calculate
subtotal = quantity * price

# Print receipt
print()
print("=" * 28)
print("         RECEIPT")
print("=" * 28)
print(f"Item:     {item_name}")
print(f"Quantity: {quantity}")
print(f"Price:    ${price:.2f} each")
print("-" * 28)
print(f"Subtotal: ${subtotal:.2f}")
print("=" * 28)
```

---

## Optional Quiz (10 minutes)

### Quick Knowledge Check
8–10 questions covering:
- Variable types (str, int, float, bool)
- Arithmetic operators
- String indexing and slicing
- String methods
- Type conversion

---

## Sample Quiz Questions

### Question 1
What is the output of `print(type(42))`?
- A) `int`
- B) `<class 'int'>`
- C) `42`
- D) `number`

**Answer**: B

---

## Sample Quiz Questions

### Question 2
What does `"Python"[2:5]` return?
- A) `"Pyt"`
- B) `"yth"`
- C) `"tho"`
- D) `"thon"`

**Answer**: C (`"tho"` — indices 2, 3, 4)

---

## Sample Quiz Questions

### Question 3
Why does `input()` always return a string?
- A) Because keyboards only type text
- B) To avoid errors with special characters
- C) Because Python doesn't know what type you want
- D) It's a bug in Python

**Answer**: C

---

## Completion Criteria (Hour 8)

✓ Program runs end-to-end without crashes  
✓ Correct math and type conversions  
✓ Output is readable and formatted

---

## Common Pitfalls (Hour 8)

⚠️ **Forgetting float conversion for price**
```python
price = input("Price: ")  # String!
total = price * 3  # '9.999.999.99' not 29.97
```

⚠️ **String concatenation vs numeric addition**
```python
# ❌ Wrong
result = "3" + "5"  # '35'
# ✓ Correct
result = int("3") + int("5")  # 8
```

---

## Optional Extensions

- Add: discount percent
- Add: tax percent

```python
# Extension example
tax_rate = 0.08  # 8% tax
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Total:    ${total:.2f}")
```

---

## Quick Check (Debrief)

**Question**: Ask 2–3 learners to explain how they debugged one error.

### Discussion Points
- What error did you encounter?
- How did you identify the problem?
- What was your fix?

---

# Session 2 Wrap-Up

## What We Covered Today

### Hour 5: String Fundamentals
- Indexing and negative indexing
- Slicing with `s[start:end]`
- The `len()` function
- Membership with `in`

### Hour 6: String Methods
- `.lower()`, `.upper()`, `.strip()`
- `.replace()` and `.find()`
- String immutability

### Hour 7: Input/Output
- `input()` returns strings
- Type conversion with `int()` and `float()`
- Unit converter exercise

### Hour 8: Checkpoint 1
- Receipt Generator assessment
- Fundamentals review

---

## Scope Guardrail Reminder

### Stay in Basics Scope
✓ Core string operations and methods  
✓ Simple type conversion  
✓ Basic input/output patterns  
✓ Clear variable names and formatting

### Not Yet (Advanced Topics)
✗ Regular expressions  
✗ String formatting with format()  
✗ Advanced string parsing  
✗ Exception handling (try/except)

---

## No-Go Topics for Basics Course

### Keep for Advanced
- Web frameworks (Flask/Django)
- Databases/SQL/ORM
- GUI frameworks (Tkinter/PyQt)
- Testing frameworks (pytest)
- Packaging/distribution

---

## Homework / Practice

### Recommended Exercises
1. Create a username generator with additional rules
2. Build a simple data cleaner for messy text
3. Create a multi-unit converter (length, weight, temperature)
4. Practice string slicing with different scenarios

---

## Next Session Preview

### Session 3 (Hours 9–12)
- Hour 9: Booleans and comparisons
- Hour 10: if/elif/else branching
- Hour 11: Combining conditions
- Hour 12: Checkpoint 2 – Branching mini-assessment

---

## Questions?

**Remember**:
- Strings are immutable — always assign back
- `input()` returns strings — convert when needed
- Use `in` for simple membership checks
- Test with sample data before submitting

---

# Thank You!

See you in Session 3!
