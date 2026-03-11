# Day 9, Hour 4: Modules: Imports and Creating utils.py (Course Hour 36)
**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 36 – Modules: imports and creating utils.py  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Beginners often struggle with how files connect to one another. Ensure you clearly explain the difference between `import X` and `from X import Y`. Emphasize the critical rule: never name a script `math.py` or `random.py`. Show how to make and import a custom `utils.py` module.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Import and use modules from the Python Standard Library (like `math` and `random`).
2. Explain the difference between `import module` and `from module import function`.
3. Create your own custom module file (`utils.py`).
4. Import your custom module into your main script."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Batteries Included
- **0:05–0:18** Core concept: The Standard Library (`math`, `random`) + Import syntax
- **0:18–0:25** Warning: The namespace clash (Don't name files `random.py`)
- **0:25–0:35** Live demo: Building `utils.py` and `main.py`
- **0:35–0:55** Guided lab: Create a utils module
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Ensure you are working in a clean directory to show how `utils.py` and `main.py` map to the same folder.
- Have a `main.py` and `utils.py` open in your editor side-by-side if possible.
- **Say:** "Please make sure you have your editor open and know exactly which folder you are saving your files into. For this to work, both files we create today must exist side-by-side in the exact same folder."

---

## 3) Opening Script: "Batteries Included" (~5 minutes)

**Say:**
"A core philosophy of Python is 'Batteries Included.' When you installed Python, you didn't just get the core language; you got a massive library containing hundreds of pre-written tools. Toolkits for math, toolkits for reading network data, toolkits for generating random numbers.

These toolkits are organized into files called **Modules**. A module is simply a completely normal `.py` Python script containing functions and variables. 

To use these toolkits, we have to tell Python to unlock them for our current script using the `import` command."

---

## 4) Concept: The Standard Library and Import Syntax

### 4.1 Basic module import

**Type and narrate:**

```python
# hour36_imports_demo.py

import math

print(math.sqrt(16))
print(math.pi)
```

**Say:**
"By typing `import math`, we pull the entire `math` toolkit into our script. To use a tool from within it, we use dot notation: `math.sqrt()` or `math.pi`. This keeps the `math` tools safely inside a `math` toolbox, so they don't accidentally conflict with names we might have created."

### 4.2 Specific function import (`from ... import`)

**Type and narrate:**

```python
from random import randint, choice

# Look, no "random." prefix needed!
dice_roll = randint(1, 6)
print(f"You rolled a {dice_roll}")

fruits = ["Apple", "Orange", "Banana"]
winner = choice(fruits)
print(f"The winner is {winner}")
```

**Say:**
"Alternatively, if we only need one or two specific tools from a massive toolbox, we can use `from module import tool`. 

If we do it this way, we don't need to type the toolbox name (`random.`). We just call `randint()` directly. Both ways are perfectly valid; `from X import Y` just saves typing if you use the tool heavily."

---

## 5) Critical Warning: The Namespace Clash

**Say:**
"Before we make our own modules, I need to issue a very stern warning. The most common error beginners make with imports is naming their file the wrong thing.

If you are following a tutorial on how the `random` module works, you might be tempted to save your file as `random.py`.

Python looks for modules in your current folder *first*, before it looks in the official standard library. If you name your file `random.py`, and inside it you type `import random`, Python tries to import your own file into itself! It will crash with horrible, confusing errors indicating that `randint` is missing. 

**Rule:** Never name your script the same name as a built-in module. Never name it `random.py`, `math.py`, `json.py`, or `datetime.py`."

---

## 6) Live Demo: Building Custom Modules

### 6.1 Creating `utils.py`

**Say:**
"Let's say our main program is getting very cluttered. We can take our helper functions, pull them into a separate file, and import them just like the standard library."

**Create a new file named `utils.py`. Type and narrate:**

```python
# utils.py

def format_currency(amount):
    """Formats a float as a $ currency string."""
    return f"${amount:.2f}"

def ask_yes_no(prompt):
    """Returns True for 'y', False for 'n'."""
    while True:
        ans = input(f"{prompt} (y/n): ").lower()
        if ans == 'y': return True
        if ans == 'n': return False
        print("Please enter 'y' or 'n'.")
```

**Say:**
"This is just a collection of tools. Notice it has no menu, no `while True` main program loop, and it doesn't run anything. It's just a toolbox."

### 6.2 Creating `main.py` and importing

**Create a new file named `main.py` in the SAME FOLDER. Type and narrate:**

```python
# main.py

import utils

print("--- Welcome to the store! ---")
total = 15.9

print(f"Your total is {utils.format_currency(total)}")

receipt = utils.ask_yes_no("Would you like a receipt?")
if receipt:
    print("Printing receipt...")
else:
    print("Have a nice day!")
```

**Run `main.py`.**

**Say:**
"Look at how clean `main.py` is. Our main program now reads like plain English. All the messy formatting strings and `while True` validation loops are tucked away in `utils.py`."

---

## 7) Hands-on Lab: Create a utils module

### 7.1 Lab overview

**Say:**
"You are going to practice this split. You'll make your own `utils.py` file to hold helper functions, and a `main.py` file to run your program."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Create a Utilities Module**

**Task:**
1. Create a file named `utils.py` in your workspace.
2. Inside `utils.py`, write a function `safe_int(prompt)`. 
   - *Wait, how do we make it safe?* For now, just have it wrap the standard `int(input(prompt))`. (If you know exception handling, you can use `try/except`, but a simple wrapping function is fine for now).
3. Inside `utils.py`, write a function `make_header(text)`.
   - It should take text, uppercase it, and return it sandwiched between dashes: `--- TEXT ---`
4. Create a second file named `main.py` in the exact same folder.
5. In `main.py`, use `import utils`.
6. Use `utils.make_header("Age Checker")` to print a header.
7. Use `utils.safe_int("Enter your age: ")` to get a numeric age, then print a message using that age.

**Requirements:**
- Be sure to run `main.py`, not `utils.py`.

---

**Instructor Note for Circulation:**
The biggest issue here will be learners running Python from a different working directory than where the files are saved, leading to a `ModuleNotFoundError: No module named 'utils'`. Ensure their IDE terminal is explicitly pointed at the folder containing both files.

### 7.3 Walkthrough solution

**After 20 minutes, show the configuration:**

`utils.py`:
```python
def make_header(text):
    clean = text.upper()
    return f"--- {clean} ---"

def safe_int(prompt):
    # For Basics, without try/except:
    val = input(prompt)
    if val.isdigit():
        return int(val)
    # Very crude fallback for now
    return 0
```

`main.py`:
```python
import utils

print(utils.make_header("Welcome to the System"))

age = utils.safe_int("What is your age? ")
print(f"You will be {age + 1} next year!")
```

**Say:**
"If you can split the 'dirty work' of validation and formatting into a module, and keep the 'business logic' of menus and calculations in a main file, you've taken the first big step into software engineering."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"Today we looked at using other people's code from the Standard Library, like `math` and `random`. Then, we looked at how to create our own modules by completely separating our functions into a custom file like `utils.py`."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: What is the main difference in how you write code when you use `import math` versus using `from math import sqrt`?"

**Expected answer:** Let them answer. "If you use `import math`, you have to type `math.sqrt()`. If you use `from math import sqrt`, you can just type `sqrt()`."
