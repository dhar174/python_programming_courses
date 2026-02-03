# Day 2, Hour 4: Debugging Habits (Basics Level)
**Python Programming Basics – Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Hour 11: 3 minutes
- Reading Tracebacks and Error Messages: 10-12 minutes
- Common Error Types: 10-12 minutes
- Print-Debugging Strategies: 8-10 minutes
- Platform-Specific Debugging (Working Directory): 5 minutes
- Live Demo (Break and Fix): 5-10 minutes
- Hands-On Lab (Debugging Drill): 25-35 minutes
- Optional: Python 2 vs 3 Note: 5-10 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Read and interpret Python tracebacks from bottom to top
2. Identify and fix the four most common error types (NameError, TypeError, ValueError, IndexError)
3. Use print-debugging strategically to isolate problems
4. Check your working directory to diagnose import and file issues
5. Form a hypothesis about an error before making changes
6. Apply a systematic debugging process: reproduce, isolate, hypothesize, test, verify
7. Distinguish Python 2 vs Python 3 syntax when encountering legacy code online

---

## Section 1: Recap & Transition from Hour 11 (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome to the final hour of Day 2! Let's do a quick recap:

**Today's Journey:**
- **Hour 9**: Comparison operators and boolean logic—making decisions
- **Hour 10**: F-strings—formatting output professionally
- **Hour 11**: `.split()` and `.join()`—processing and transforming text

You've learned a lot today! Quick show of hands: **Who's feeling more confident about making programs that make decisions and process data?**

[Wait for responses]

Excellent! You should be proud of what you've built.

### The Reality of Programming

**[Instructor speaks:]**

Now, let me be honest with you: **no matter how good you get at programming, you will encounter errors. Every. Single. Day.**

I've been programming for years, and I still see error messages multiple times an hour. The difference between a beginner and an experienced programmer isn't that experienced programmers don't make mistakes—**it's that they know how to debug quickly**.

**Hour 12 (right now)** is about **building debugging habits** that will make you self-sufficient. By the end of this hour:
- Error messages won't intimidate you
- You'll know exactly where to look when something breaks
- You'll have a systematic process for fixing problems

This is one of the most important hours in the entire course. Let's dive in!

---

## Section 2: Reading Tracebacks and Error Messages (10-12 minutes)

### What Is a Traceback?

**[Instructor speaks:]**

When Python encounters an error it can't handle, it stops and prints a **traceback** (also called a "stack trace"). This is Python's way of saying: "Here's what I was doing when things went wrong."

**Important mindset shift:** Tracebacks are not punishment. They're **helpful diagnostic information**. Learning to read them is like learning to read X-rays—once you know what to look for, they tell you exactly what's wrong.

### Anatomy of a Traceback

**[Instructor speaks:]**

Let's look at a real traceback:

```python
# broken_script.py
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

scores = [85, 90, 78]
result = calculate_average(score)
print(f"Average: {result}")
```

**When we run this:**

```
Traceback (most recent call last):
  File "broken_script.py", line 7, in <module>
    result = calculate_average(score)
NameError: name 'score' is not defined
```

**Let's break down each part:**

1. **`Traceback (most recent call last):`**
   - This header tells you a traceback is coming
   - "Most recent call last" means the **bottom** of the traceback is where the error occurred

2. **`File "broken_script.py", line 7, in <module>`**
   - **File**: Which file had the problem
   - **Line 7**: The line number where the error occurred
   - **in <module>**: The context (here, top-level code)

3. **`result = calculate_average(score)`**
   - This is the actual line of code that caused the problem

4. **`NameError: name 'score' is not defined`**
   - **NameError**: The type of error
   - **Message**: What went wrong (we tried to use a variable called `score` that doesn't exist)

### How to Read a Traceback: Bottom to Top

**[Instructor speaks:]**

**Key rule: Read tracebacks from bottom to top.**

1. **Start at the bottom:** Look at the error type and message
2. **Read the message:** It often tells you exactly what's wrong
3. **Look at the line number:** That's where Python detected the problem
4. **Examine the code:** Look at the line mentioned

**In our example:**
- **Error:** `NameError: name 'score' is not defined`
- **Line:** Line 7
- **The code:** `result = calculate_average(score)`
- **The problem:** We wrote `score` but the variable is actually called `scores` (with an 's')

**The fix:**

```python
result = calculate_average(scores)  # Fixed the typo
```

### Multi-Level Tracebacks

**[Instructor speaks:]**

Sometimes the traceback has multiple levels:

```python
# multi_level.py
def divide_values(a, b):
    return a / b

def calculate_ratio(x, y):
    return divide_values(x, y)

result = calculate_ratio(10, 0)
print(result)
```

**Traceback:**

```
Traceback (most recent call last):
  File "multi_level.py", line 8, in <module>
    result = calculate_ratio(10, 0)
  File "multi_level.py", line 6, in calculate_ratio
    return divide_values(x, y)
  File "multi_level.py", line 3, in divide_values
    return a / b
ZeroDivisionError: division by zero
```

**Reading this:**
1. **Bottom:** `ZeroDivisionError: division by zero` on line 3 in `divide_values`
2. **Middle:** `divide_values` was called from line 6 in `calculate_ratio`
3. **Top:** `calculate_ratio` was called from line 8 in our main code

**The path:** Line 8 → called function on Line 6 → called function on Line 3 → **error occurred here**

**The traceback shows the call chain**, but the **actual error** is at the bottom.

### Quick Check #1

**[Instructor asks:]**

Look at this traceback:

```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(message)
NameError: name 'message' is not defined
```

**Questions:**
1. What line has the problem?
2. What's the error type?
3. What went wrong?

[Pause for student predictions]

**Answers:**
1. Line 5
2. `NameError`
3. We're trying to use a variable called `message` that doesn't exist (maybe we forgot to define it, or we misspelled it)

---

## Section 3: Common Error Types (10-12 minutes)

### The Four Most Common Errors (and How to Fix Them)

**[Instructor speaks:]**

At the Basics level, you'll encounter four error types over and over. Let's learn to recognize and fix each one.

### 1. NameError: Variable Doesn't Exist

**What it means:** You're trying to use a variable, function, or module that Python doesn't know about.

**Common causes:**

```python
# Cause 1: Typo
name = "Alice"
print(nam)  # NameError: name 'nam' is not defined

# Cause 2: Variable not defined yet
print(greeting)  # NameError: name 'greeting' is not defined
greeting = "Hello"

# Cause 3: Wrong scope (we'll cover this later)
def my_function():
    x = 10

print(x)  # NameError: name 'x' is not defined
```

**How to fix:**
- Check spelling carefully
- Make sure the variable is defined before you use it
- Check for scope issues (variables defined inside functions aren't visible outside)

### 2. TypeError: Wrong Type for Operation

**What it means:** You're trying to do something with a value that doesn't support that operation.

**Common causes:**

```python
# Cause 1: Can't add string and number
age = 25
message = "I am " + age  # TypeError: can only concatenate str (not "int") to str

# Fix: Convert to string
message = "I am " + str(age)  # Works
# Or use f-string
message = f"I am {age}"  # Better!

# Cause 2: Can't call a non-function
name = "Alice"
result = name(10)  # TypeError: 'str' object is not callable

# Cause 3: Wrong argument type
number = int("hello")  # ValueError (actually), but shows type issues
```

**How to fix:**
- Check the types of your variables with `print(type(variable))`
- Convert types explicitly: `str()`, `int()`, `float()`
- Read the error message—it often tells you what types are involved

### 3. ValueError: Right Type, Wrong Value

**What it means:** The type is correct, but the specific value can't be used.

**Common causes:**

```python
# Cause 1: Can't convert non-numeric string to int
age = int("twenty")  # ValueError: invalid literal for int() with base 10: 'twenty'

# Fix: Make sure the string contains a number
age = int("20")  # Works

# Cause 2: Unpacking wrong number of values
name = "Alice"
first, last = name.split()  # ValueError: not enough values to unpack (expected 2, got 1)

# Fix: Make sure the data matches expectations
name = "Alice Johnson"
first, last = name.split()  # Works
```

**How to fix:**
- Validate input before converting
- Check that the value makes sense for the operation
- Use try/except for user input (we'll cover this in error handling later)

### 4. IndexError: Index Out of Range

**What it means:** You're trying to access a position in a list/string that doesn't exist.

**Common causes:**

```python
# Cause 1: List index too large
fruits = ["apple", "banana"]
print(fruits[2])  # IndexError: list index out of range

# Fix: Use valid indices (0 and 1 in this case)
print(fruits[1])  # "banana"

# Cause 2: Empty list
words = []
print(words[0])  # IndexError: list index out of range

# Fix: Check length first
if len(words) > 0:
    print(words[0])

# Cause 3: Off-by-one error
numbers = [1, 2, 3, 4, 5]
print(numbers[5])  # IndexError: list index out of range
# Remember: indices are 0-4, not 1-5

# Fix:
print(numbers[4])  # 5 (the last element)
```

**How to fix:**
- Check the length of your list/string: `len(my_list)`
- Remember indices start at 0
- Use negative indices to count from the end: `my_list[-1]` (last element)
- Validate indices before accessing

### Quick Check #2

**[Instructor asks:]**

What error type would each of these cause?

```python
# A
numbers = [10, 20, 30]
print(numbers[3])

# B
result = "5" + 5

# C
total = sum(items)
```

[Pause for student predictions]

**Answers:**
- **A:** `IndexError` (list only has indices 0, 1, 2)
- **B:** `TypeError` (can't add string and int)
- **C:** `NameError` (if `items` wasn't defined earlier)

### Less Common Errors (Honorable Mentions)

**[Instructor speaks:]**

You might also see:

- **`SyntaxError`**: Your code isn't valid Python (missing colon, unmatched parentheses, etc.)
- **`IndentationError`**: Your indentation is wrong (Python cares about this!)
- **`AttributeError`**: You're calling a method that doesn't exist on that type
- **`KeyError`**: You're accessing a dictionary key that doesn't exist (we'll cover this later)

**For now, focus on the Big Four:** NameError, TypeError, ValueError, IndexError.

---

## Section 4: Print-Debugging Strategies (8-10 minutes)

### The Power of Print Statements

**[Instructor speaks:]**

The simplest and most effective debugging tool is the humble `print()` statement. Professional developers use this technique constantly.

**The idea:** Insert `print()` statements at strategic points to see:
- What values variables have
- Which code paths are executed
- Where the program crashes

### Strategy 1: Print Variable Values

**[Instructor speaks:]**

When something doesn't work as expected, print the variables involved:

```python
# Broken code
bill = input("Enter bill: ")
tip_percent = input("Enter tip %: ")
tip = bill * (tip_percent / 100)
print(f"Tip: ${tip:.2f}")
```

**This will crash with a `TypeError`. Why?**

**Add debug prints:**

```python
bill = input("Enter bill: ")
tip_percent = input("Enter tip %: ")

# Debug prints
print(f"DEBUG: bill = {bill}, type = {type(bill)}")
print(f"DEBUG: tip_percent = {tip_percent}, type = {type(tip_percent)}")

tip = bill * (tip_percent / 100)
print(f"Tip: ${tip:.2f}")
```

**Output:**
```
Enter bill: 50
Enter tip %: 18
DEBUG: bill = 50, type = <class 'str'>
DEBUG: tip_percent = 18, type = <class 'str'>
TypeError: can't multiply sequence by non-int of type 'str'
```

**Aha!** Both are strings. We forgot to convert them.

**The fix:**

```python
bill = float(input("Enter bill: "))
tip_percent = float(input("Enter tip %: "))
tip = bill * (tip_percent / 100)
print(f"Tip: ${tip:.2f}")
```

**[Key insight]:** Print statements revealed the problem immediately.

### Strategy 2: Print Checkpoints

**[Instructor speaks:]**

When you don't know where the crash is happening, add checkpoints:

```python
print("DEBUG: Starting program")

name = input("Enter name: ")
print("DEBUG: Got name")

age = int(input("Enter age: "))
print("DEBUG: Got age")

if age >= 18:
    print("DEBUG: In adult branch")
    print("You are an adult")
else:
    print("DEBUG: In minor branch")
    print("You are a minor")

print("DEBUG: Program complete")
```

**If the program crashes between "Got name" and "Got age", you know the problem is on the `age = int(...)` line.**

### Strategy 3: Print Type Information

**[Instructor speaks:]**

When you get type-related errors, print the types:

```python
value = input("Enter a number: ")
result = value * 2

# Add this to debug:
print(f"value = {value}, type = {type(value)}")
print(f"result = {result}, type = {type(result)}")
```

**This reveals:** `value` is a string, and `value * 2` repeats the string, not multiplies a number.

### Strategy 4: Print in Small Test Cases

**[Instructor speaks:]**

When a function is misbehaving, test it with a small, known input:

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Test with simple input
test_data = [10, 20, 30]
print(f"Testing with: {test_data}")
result = calculate_average(test_data)
print(f"Result: {result}")
print(f"Expected: 20.0")
```

**This lets you verify the function works before using it with real data.**

### The Debug Print Pattern

**[Instructor speaks:]**

A useful pattern:

```python
DEBUG = True  # Set to False when done debugging

if DEBUG:
    print(f"DEBUG: variable_name = {variable_name}")

# Or use a function:
def debug_print(message):
    if DEBUG:
        print(f"DEBUG: {message}")

debug_print(f"Processing item {item}")
```

**This lets you turn all debug output on/off with one variable.**

---

## Section 5: Platform-Specific Debugging – Working Directory (5 minutes)

### "Where Am I?" – The Working Directory Problem

**[Instructor speaks:]**

A very common issue, especially with file operations and imports:

**Error message:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

**The problem:** Python is looking for `data.txt` in the **current working directory**, but the file is somewhere else.

### Checking Your Working Directory

**[Instructor speaks:]**

Add this to your script to see where Python thinks you are:

```python
import os

print(f"Current working directory: {os.getcwd()}")
```

**Example output:**
```
Current working directory: /home/username/Documents
```

**If your script is in `/home/username/python_basics/` but Python is running from `/home/username/Documents/`, it won't find files in the `python_basics` folder.**

### The Fix: Run from the Correct Directory

**[Instructor speaks:]**

**In your terminal:**

```bash
# Check where you are
pwd

# Change to your project folder
cd python_basics

# Now run the script
python my_script.py
```

**This is why we established the folder structure in Hour 1**—keeping everything in one course folder prevents path confusion.

### Common Working Directory Issues

**[Instructor speaks:]**

1. **Running from the wrong folder:**
   ```bash
   # BAD: Running from home directory
   python python_basics/my_script.py
   
   # GOOD: Change to the folder first
   cd python_basics
   python my_script.py
   ```

2. **IDE running from a different folder:**
   - In VS Code, open the `python_basics` folder as your workspace
   - Check the terminal shows you're in the correct folder

3. **Using absolute paths as a workaround (not ideal but works):**
   ```python
   # Instead of: data.txt
   # Use full path: /home/username/python_basics/data.txt
   ```

**[Best practice]:** Always `cd` to your project folder before running scripts.

---

## Section 6: Live Demo – Break and Fix (5-10 minutes)

### Demo Script: Deliberate Debugging

**[Instructor speaks:]**

Now I'm going to deliberately break a script and show you how I debug it systematically.

**[Open editor and create `buggy_calculator.py`]**

**[Instructor types:]**

```python
# buggy_calculator.py
# Purpose: Calculate average of three scores (with bugs!)

print("=== Score Average Calculator ===\n")

score1 = input("Enter score 1: ")
score2 = input("Enter score 2: ")
score3 = input("Enter score 3: ")

total = score1 + score2 + score3
average = total / 3

print(f"Average score: {average:.1f}")
```

**[Run the program]**

```
Enter score 1: 85
Enter score 2: 90
Enter score 3: 78
Traceback (most recent call last):
  File "buggy_calculator.py", line 11, in <module>
    average = total / 3
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

**[Instructor narrates the debugging process:]**

**Step 1: Read the error**
- **Error type:** `TypeError`
- **Message:** Can't divide string by int
- **Line:** 11 (`average = total / 3`)

**Step 2: Form a hypothesis**
"The error says `total` is a string. That means line 10 didn't add numbers—it concatenated strings. This is because `input()` returns strings, and we didn't convert them."

**Step 3: Add debug prints to verify**

```python
total = score1 + score2 + score3
print(f"DEBUG: total = {total}, type = {type(total)}")
average = total / 3
```

**Run again:**
```
DEBUG: total = 859078, type = <class 'str'>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

**Confirmed!** `total` is `"859078"` (concatenated strings), not `253` (sum of numbers).

**Step 4: Fix the bug**

```python
score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
```

**Step 5: Test again**

```
Enter score 1: 85
Enter score 2: 90
Enter score 3: 78
Average score: 84.3
```

**Success!**

**[Key teaching moments:]**
1. Read the error message—it told us exactly what was wrong
2. Form a hypothesis before making changes
3. Use debug prints to verify the hypothesis
4. Make the smallest fix possible
5. Test to verify it works

### Adding More Debug Checkpoints

**[Instructor speaks:]**

Let me show you what the fully-debugged version might look like:

```python
# buggy_calculator.py (with debugging)
# Purpose: Calculate average of three scores

DEBUG = True  # Turn off when done

print("=== Score Average Calculator ===\n")

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

if DEBUG:
    print(f"DEBUG: score1={score1}, score2={score2}, score3={score3}")

total = score1 + score2 + score3

if DEBUG:
    print(f"DEBUG: total={total}")

average = total / 3

if DEBUG:
    print(f"DEBUG: average={average}")

print(f"Average score: {average:.1f}")
```

**Once you verify it works, set `DEBUG = False` to hide the debug output.**

---

## Section 7: Hands-On Lab – Debugging Drill (25-35 minutes)

### Lab Overview

**[Instructor speaks:]**

Now it's your turn! You're going to receive three broken scripts. For each one:
1. Run it and observe the error
2. Read the traceback
3. Form a hypothesis about what's wrong
4. Add debug prints if needed
5. Fix the problem
6. Write a 1-sentence explanation of what went wrong

**Lab Goal:** Practice systematic debugging.

### Lab Instructions: Debugging Drill

**You'll fix three broken scripts. Create each file and debug it.**

---

#### **Script 1: Greeting Program (broken_greeter.py)**

```python
# broken_greeter.py
# Purpose: Greet a user by name

print("=== Greeter ===\n")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_nam} {last_name}!")
print(f"Your full name has {len(first_name + last_name)} characters.")
```

**Expected behavior:** Greet the user and count total characters in their full name.

**Your tasks:**
1. Run the script and observe the error
2. Read the traceback—what's the error type and line number?
3. Fix the bug
4. Test with your name
5. **Write 1 sentence explaining what was wrong**

---

#### **Script 2: Temperature Converter (broken_temp_converter.py)**

```python
# broken_temp_converter.py
# Purpose: Convert Fahrenheit to Celsius

print("=== Temperature Converter ===\n")

fahrenheit = input("Enter temperature in Fahrenheit: ")

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {celsius:.1f}°C")
```

**Expected behavior:** Convert Fahrenheit to Celsius using the formula: C = (F - 32) × 5/9

**Your tasks:**
1. Run the script and observe the error
2. Identify the problem (hint: it's a type issue)
3. Add debug prints to confirm the types of variables
4. Fix the bug
5. Test with 32°F (should output 0.0°C) and 212°F (should output 100.0°C)
6. **Write 1 sentence explaining what was wrong**

---

#### **Script 3: List Average (broken_average.py)**

```python
# broken_average.py
# Purpose: Calculate average of a list of numbers

print("=== Average Calculator ===\n")

numbers = [85, 92, 78, 90]

total = sum(numbers)
average = total / len(numbers)

print(f"Numbers: {numbers}")
print(f"Average: {average:.1f}")

# Now try to access the 5th number
fifth_number = numbers[5]
print(f"The 5th number is: {fifth_number}")
```

**Expected behavior:** Calculate average and show the 5th number.

**Your tasks:**
1. Run the script—it works partially then crashes
2. Read the traceback—what error occurs?
3. Identify why this error happens (hint: count the elements)
4. Fix the bug by correcting the index
5. Test and verify all output is correct
6. **Write 1 sentence explaining what was wrong**

---

### Completion Criteria

For each script, you must:
- ✅ Identify the error type from the traceback
- ✅ Fix the bug so the script runs without errors
- ✅ Test with appropriate inputs
- ✅ Write a 1-sentence explanation of the root cause

### Hints and Strategies

**[Instructor speaks:]**

As you work through these:

1. **Don't change multiple things at once**—make one small fix at a time
2. **Run the script after each change**—verify your fix works
3. **Use debug prints liberally**—`print(f"DEBUG: var = {var}, type = {type(var)}")`
4. **Read the error message carefully**—it often tells you exactly what's wrong
5. **Check line numbers**—go to the exact line mentioned in the traceback

**Common debugging questions:**
- **NameError?** Check for typos in variable names
- **TypeError?** Check if you need to convert types (`int()`, `str()`, `float()`)
- **IndexError?** Count your list elements—remember indices start at 0
- **ValueError?** Check if the value makes sense for the operation

### Optional Extensions

If you finish early, try these:

1. **Add input validation to Script 2:** Check that the user enters a valid number before converting

2. **Extend Script 3:** Modify it to safely handle lists of any size (don't hardcode the index)

3. **Create a 4th broken script:** Write a buggy script and challenge a neighbor to fix it

**[Instructor speaks:]**

Alright, you have 25-35 minutes. Remember:
- Read tracebacks from bottom to top
- Form a hypothesis before fixing
- Change one thing at a time
- Test after each fix

Let's debug!

---

## Section 8: Optional – Python 2 vs Python 3 Quick Differences (5-10 minutes)

**[Instructor speaks:]**

**Note:** This section is optional and only relevant if students encounter old code online or need to work with legacy Python 2 code.

### Why This Matters

**[Instructor speaks:]**

Python 3 was released in 2008, and Python 2 reached end-of-life in 2020. **All new code should use Python 3.** 

However, you might encounter Python 2 code in:
- Old tutorials and Stack Overflow answers
- Legacy codebases at companies
- Academic papers and research code

**You should NOT learn Python 2**, but you should be able to **recognize** it.

### Key Differences to Recognize

**[Instructor speaks:]**

Here are the most visible differences:

#### 1. print is a Function in Python 3

**Python 2:**
```python
print "Hello, world"
print "Age:", age
```

**Python 3:**
```python
print("Hello, world")
print("Age:", age)
```

**If you see `print` without parentheses, it's Python 2 code.**

#### 2. Integer Division Behavior

**Python 2:**
```python
print 5 / 2        # 2 (floor division)
```

**Python 3:**
```python
print(5 / 2)       # 2.5 (true division)
print(5 // 2)      # 2 (floor division)
```

**Python 3 requires explicit `//` for floor division.**

#### 3. Unicode is Default in Python 3

**Python 2:**
```python
name = u"José"     # u prefix for unicode
```

**Python 3:**
```python
name = "José"      # unicode by default
```

#### 4. input() Behavior

**Python 2:**
```python
# input() evaluates the input as Python code (dangerous!)
# raw_input() gets a string
name = raw_input("Name: ")
```

**Python 3:**
```python
# input() always returns a string (safe)
name = input("Name: ")
```

### What to Do When You See Python 2 Code

**[Instructor speaks:]**

1. **Check the date:** Is the tutorial/article from before 2015? It might be Python 2
2. **Look for the telltale signs:** `print` without parentheses, `raw_input()`, etc.
3. **Find a Python 3 equivalent:** Search for "Python 3 [topic]"
4. **Use a converter:** The `2to3` tool can convert Python 2 code to Python 3

**Bottom line: Write all your code in Python 3. Just be aware Python 2 exists when reading old resources.**

---

## Section 9: Debrief & Exit Ticket (5 minutes)

### Solution Walkthrough

**[Instructor shares solutions:]**

#### Script 1: Greeting Program

**Bug:** Typo in variable name (`first_nam` instead of `first_name`)

**Fixed code:**
```python
print(f"Hello, {first_name} {last_name}!")
```

**Explanation:** NameError occurred because we misspelled the variable name.

---

#### Script 2: Temperature Converter

**Bug:** `fahrenheit` is a string (from `input()`), but we're trying to do math with it.

**Fixed code:**
```python
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
```

**Explanation:** TypeError occurred because we didn't convert the input string to a number.

---

#### Script 3: List Average

**Bug:** List only has 4 elements (indices 0-3), but we're trying to access index 5.

**Fixed code:**
```python
fifth_number = numbers[4]  # Wait, there's no 5th element!
# OR better yet, don't hardcode:
# if len(numbers) >= 5:
#     fifth_number = numbers[4]
```

**Actually, the list only has 4 numbers, so asking for the 5th doesn't make sense. The bug is a logic error.**

**Better fix:**
```python
# Remove or comment out the problematic lines
# fifth_number = numbers[5]
# print(f"The 5th number is: {fifth_number}")
```

**Explanation:** IndexError occurred because the list has only 4 elements (indices 0-3), and we tried to access index 5.

---

### Key Debugging Takeaways

**[Instructor speaks:]**

Let me summarize the debugging mindset we practiced today:

**The Debugging Process:**
1. ✅ **Reproduce** the error (run the code)
2. ✅ **Read** the traceback (bottom to top)
3. ✅ **Isolate** the problem (which line? which variable?)
4. ✅ **Hypothesize** the cause (form a theory)
5. ✅ **Test** your hypothesis (add debug prints if needed)
6. ✅ **Fix** the bug (smallest change possible)
7. ✅ **Verify** the fix (test with multiple inputs)

**This process works for ANY bug, from beginner to expert level.**

### Exit Ticket

**[Instructor asks:]**

Before we wrap up Day 2, answer this in your notes or in the chat:

**Question:** When is it helpful to print `type(variable)`, and why?

**Expected answer:** It's helpful when you get type-related errors (TypeError, ValueError). Printing the type reveals if a variable is a string when you expected a number, or vice versa, which helps you know where to add type conversions.

---

## Recap: What We Accomplished in Hour 12

In this hour, you:
✅ Learned to read tracebacks from bottom to top  
✅ Identified the four most common error types (NameError, TypeError, ValueError, IndexError)  
✅ Used print-debugging to isolate problems  
✅ Checked your working directory to diagnose file/import issues  
✅ Applied a systematic debugging process  
✅ Fixed three broken scripts using the debugging workflow  
✅ (Optional) Recognized Python 2 vs Python 3 differences  

**This is a career-changing skill.** Being able to debug your own code makes you self-sufficient and confident. You're no longer dependent on others to fix your errors—you can figure them out yourself.

---

## Recap: What We Accomplished in Day 2

**Day 2 Complete!** Let's review the full day:

✅ **Hour 9:** Comparisons and boolean logic—making complex decisions  
✅ **Hour 10:** F-strings—formatting output like a pro  
✅ **Hour 11:** `.split()` and `.join()`—processing text data  
✅ **Hour 12:** Debugging habits—fixing errors systematically  

**You've made incredible progress.** You can now:
- Build programs that make multi-condition decisions
- Format output beautifully
- Process and transform text
- Debug problems independently

**In Day 3 (Session 4), we'll dive into lists in detail and learn about loops.**

**Amazing work today! See you next session!**

---

## Quick Reference Card (for students)

**Reading Tracebacks:**
- Read from **bottom to top**
- Bottom line = error type and message
- Look at the line number mentioned
- Examine that line in your code

**Common Error Types:**
- **NameError:** Variable doesn't exist (typo? not defined yet?)
- **TypeError:** Wrong type for operation (need to convert?)
- **ValueError:** Right type, wrong value (invalid number string?)
- **IndexError:** List/string index out of range (off-by-one?)

**Debugging Strategies:**
```python
# Print variable values and types
print(f"DEBUG: {var} (type: {type(var)})")

# Print checkpoints
print("DEBUG: Reached checkpoint 1")

# Check working directory
import os
print(f"Working directory: {os.getcwd()}")
```

**Debugging Process:**
1. Reproduce the error
2. Read the traceback
3. Isolate the problem
4. Form a hypothesis
5. Test (add debug prints)
6. Fix (smallest change)
7. Verify (test again)

**Remember:**
- Errors are feedback, not failure
- Change one thing at a time
- Run after each change
- Debug prints are your friend

---

**End of Hour 12 Script / End of Day 2**
