# Day 9, Hour 4: Modules: Imports and Creating utils.py

## 1. Instructor Note: Why This Matters

This hour represents a critical inflection point in the Basics curriculum. Students transition from viewing Python as a single-file scripting environment to understanding it as a modular system where code organization and reuse become architectural concerns. By mastering imports and creating custom utility modules, learners develop professional coding habits that scale from command-line scripts to full applications.

The ability to write custom modules like `utils.py` teaches students that they are not limited to built-in functionality or third-party packages—they can architect their own solutions. This shift in mindset underpins everything that follows: object-oriented design, testing frameworks, and real-world software development. The challenges they overcome in this hour (naming conflicts, import syntax, relative vs. absolute imports) will surface repeatedly in their careers, making hands-on practice now invaluable.

Emphasize that professional Python developers spend significant time organizing code into logical modules and packages. Their success in this hour directly impacts their confidence and capability moving forward.

## 2. Learning Outcomes

By the end of this hour, students will be able to:

1. **Import from the Python Standard Library** using various import forms (`import module`, `from module import name`, `import module as alias`) and apply them correctly in real code.
2. **Understand the `__name__` special variable** and how it controls when code runs, enabling the creation of modules that work both as standalone scripts and as importable libraries.
3. **Create custom utility modules** (such as `utils.py`) with focused, reusable functions that encapsulate common tasks.
4. **Import custom modules into main scripts** using correct file organization and naming practices to avoid import errors.
5. **Troubleshoot common import errors** including naming conflicts, circular imports, and incorrect file paths, using effective debugging strategies.

## 3. Agenda and Timing (Total: 60 minutes)

- **0:00–0:03** — Opening Script: Module Philosophy (3 minutes)
- **0:03–0:18** — Concept Briefing: Import Forms, `__name__`, Naming Practices (15 minutes)
- **0:18–0:35** — Live Demo: Standard Library Imports and Custom Module Creation (17 minutes)
- **0:35–1:00** — Hands-On Lab: Building and Using `utils.py` (25 minutes)
  - Checkpoint 1 (0:35–0:40): Setup—Create file structure and initial functions
  - Checkpoint 2 (0:40–0:48): Implement `safe_int()` function with validation
  - Checkpoint 3 (0:48–0:56): Implement `format_money()` function with proper formatting
  - Checkpoint 4 (0:56–1:00): Test integration—Import and use functions in main script

## 4. Opening Script (~3 minutes)

Begin with a concrete scenario:

"Imagine you're building a financial tracking application. Your main script handles user interactions, but you need functions to safely convert user input to integers and format currency values. Do you hardcode these into your main file? No. Professional developers extract these into a utility module—a `.py` file full of helper functions.

Today, you become that professional developer. You'll create `utils.py`, a reusable module containing functions that can be used in multiple programs. When you're done, your main script will be cleaner, your code will be reusable, and you'll understand how real Python projects are organized.

Think of it this way: imports are how Python's ecosystem works. Every package you might use—data science libraries, web frameworks, testing tools—is organized around modules and imports. Learning this now isn't just about today's assignment; it's about building the mental model that powers your entire future in Python."

## 5. Concept Briefing: Import Forms, `__name__`, and Module Best Practices (15 minutes)

### Import Forms: Three Essential Patterns

Students should understand three core syntactic patterns, each with distinct advantages and use cases:

**1. `import module` — Full Module Import**

Syntax: `import math`  
Access: `math.sqrt(16)`  
Use Case: When you want organized namespacing and multiple functions from a module.

This form imports the entire module as a namespace. Every function or constant you use must be prefixed with the module name. The advantage is clarity: when you read `math.sqrt()`, you immediately know the function comes from the `math` module. This prevents name collisions when two modules have functions with the same name.

Example workflow:
```python
import math
import random

result = math.sqrt(25)           # Clear: sqrt is from math
value = random.randint(1, 100)   # Clear: randint is from random
```

The downside is verbosity. If you're calling the same function repeatedly, the module prefix gets repetitive. This form is ideal for one-off uses or when working with multiple modules simultaneously.

---

**2. `from module import name` — Targeted Import**

Syntax: `from math import sqrt`  
Access: `sqrt(16)`  
Use Case: When you need specific functions and plan to use them frequently.

This form brings specific names directly into your namespace. You can call `sqrt()` without the `math.` prefix, making the code more concise. The tradeoff is reduced clarity—someone reading `sqrt()` alone doesn't immediately know where it comes from.

Example workflow:
```python
from math import sqrt, pi, ceil
from random import choice, randint

result = sqrt(25)                        # Clean, but source isn't obvious
selected = choice([1, 2, 3, 4, 5])       # Where does choice come from?
```

This form is useful when you're focused on a specific task (e.g., all math operations), but it can lead to namespace pollution if overused.

---

**3. `import module as alias` — Aliased Import**

Syntax: `import math as m` or `import numpy as np`  
Access: `m.sqrt(16)` or `np.array([1, 2, 3])`  
Use Case: Shortening long module names or avoiding naming conflicts.

This form assigns a module a shorter nickname. It's especially common with long module names (e.g., `numpy as np`, `pandas as pd`). It combines clarity (you still have module-like prefixing) with conciseness (the prefix is shorter).

Example workflow:
```python
import math as m
result = m.sqrt(25)
area = m.pi * m.sqrt(radius)

import datetime as dt
now = dt.datetime.now()
```

This form is professional convention for widely-used libraries. Learning it now prepares students for real-world code.

---

**Comparing the Three Forms**

| Form | Clarity | Conciseness | Best For |
|------|---------|-------------|----------|
| `import module` | High | Low | Organization, one-off uses |
| `from module import name` | Low | High | Frequent, focused use |
| `import module as alias` | High | Medium | Common libraries, avoiding conflicts |

Students should understand that all three are valid; the choice depends on context.

### The `__name__` Special Variable: Understanding Module Execution Context

Every Python file has access to a special variable called `__name__`. Its value depends on how the file is executed. This is one of the most important concepts in modular Python design.

**When run directly:**
```python
if __name__ == "__main__":
    print("This script was run directly")
```
The value is `"__main__"` (literally the string `__main__`).

**When imported as a module:**
```python
# In another file:
import utils
# Inside utils.py, __name__ would be "utils" (the module name)
```
The value is the module's name as a string (e.g., `"utils"`, `"math"`, `"random"`).

This powerful pattern enables a file to serve dual purposes:

1. **As a standalone script**: When executed directly, the setup code and tests run.
2. **As a reusable module**: When imported, only the function definitions are available; setup code is skipped.

**Practical Example: Dual-Purpose File**

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    # This only runs when the file is executed directly
    print("Testing math functions:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
```

When you run this file directly (`python math_module.py`), you see the test output. When another file imports it (`from math_module import add`), the test code is skipped, and only the functions are available.

This is why most professional Python modules end with an `if __name__ == "__main__":` block. It's not required, but it's standard practice and demonstrates that the author understands the pattern.

**Why This Matters**

Many learners struggle because they run their module file directly, see the test output, assume everything works, then panic when `main.py` imports it and fails. Understanding `__name__` prevents this confusion.

### Naming Practices and Avoiding Conflicts: A Critical Skill

A critical pitfall occurs when students create files with names matching standard library modules. This is more than a minor inconvenience—it's a common source of confusion and errors.

**Why Naming Matters**

Python searches for modules in a specific order:

1. The current directory (highest priority)
2. Directories in `PYTHONPATH`
3. Installation-dependent default paths (standard library, site-packages)

If you create `random.py` in your project directory, Python finds it first before the standard library `random` module. Your file shadows the built-in, and any `import random` brings in your file instead of the standard library. This causes unexpected behavior or import errors if your file lacks the expected functions.

**Example of the Problem:**

```python
# File: random.py (your custom module)
def get_random_number():
    return 42

# File: main.py
import random
print(random.randint(1, 10))  # Error! Your random.py has no randint() function
```

Running `main.py` fails because `random` refers to your file, which doesn't have `randint()`.

**Best Practices for Naming**

1. **Avoid single-word names** that might match the standard library:
   - ❌ `random.py` (shadows `random` module)
   - ❌ `string.py` (shadows `string` module)
   - ❌ `math.py` (shadows `math` module)

2. **Use descriptive, multi-word names**:
   - ✅ `utils.py` (generic but clear, not a stdlib name)
   - ✅ `math_helpers.py` (clearly custom, math-related)
   - ✅ `formatters.py` (descriptive, single-function purpose)
   - ✅ `validators.py` (descriptive, validation-focused)

3. **Use prefixes if collision risk is high**:
   - ✅ `my_math.py` (the `my_` prefix signals it's custom)
   - ✅ `app_utils.py` (prefixed with context)

4. **Document your module's purpose in the filename**:
   - ✅ `input_handlers.py` (clearly handles input)
   - ✅ `data_formatters.py` (clearly formats data)

By following these conventions, you prevent hours of debugging frustration later.

### File Organization

For the remainder of the Basics course, a typical project structure looks like:

```
project_folder/
├── main.py            (entry point; contains user interaction and control flow)
├── utils.py           (reusable utility functions)
└── config.py          (if config is needed; optional)
```

The key principle: separable concerns live in separate files. `main.py` orchestrates; `utils.py` provides reusable helpers. This mirrors professional practice.

## 6. Live Demo: Standard Library Imports and Custom Module Demo (17 minutes)

### Demo 1: Standard Library Imports (5 minutes)

Create a file called `stdlib_demo.py`:

```python
import math
import random
from datetime import datetime
from random import choice

print("=== Standard Library Import Demonstrations ===\n")

# Demo 1: math module
print("1. Using the math module:")
print(f"   math.sqrt(25) = {math.sqrt(25)}")
print(f"   math.pi = {math.pi}")
print(f"   math.ceil(3.2) = {math.ceil(3.2)}\n")

# Demo 2: random module
print("2. Using the random module:")
numbers = [1, 2, 3, 4, 5]
print(f"   random.choice({numbers}) = {random.choice(numbers)}")
print(f"   random.randint(1, 10) = {random.randint(1, 10)}\n")

# Demo 3: datetime
print("3. Using the datetime module:")
now = datetime.now()
print(f"   Current time: {now}")
print(f"   Year: {now.year}, Month: {now.month}, Day: {now.day}\n")

# Demo 4: Using 'from' import
print("4. Using 'from' import (directly calling choice):")
selected = choice(["apple", "banana", "cherry"])
print(f"   Selected fruit: {selected}")
```

**Teaching Point**: Run this file and show the output. Emphasize that these modules are built into Python and are accessible immediately via imports. Show how different import forms (`import X`, `from X import Y`) affect how you call the functions.

### Demo 2: Creating a Simple Custom Module (6 minutes)

Create a file called `math_helpers.py`:

```python
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Raise base to exponent."""
    return base ** exponent

if __name__ == "__main__":
    print("Testing math_helpers when run directly:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")
    print(f"power(2, 8) = {power(2, 8)}")
```

Create a companion file called `use_math_helpers.py`:

```python
from math_helpers import add, multiply, power

print("Using math_helpers module:")
print(f"add(10, 20) = {add(10, 20)}")
print(f"multiply(3, 9) = {multiply(3, 9)}")
print(f"power(3, 4) = {power(3, 4)}")
```

**Teaching Point**: Run `math_helpers.py` directly to show the "Testing" output. Then run `use_math_helpers.py` to show the functions being imported and used. Demonstrate that `math_helpers.py` can act as both a standalone script and a reusable module. This is the `__name__ == "__main__"` pattern in action.

### Demo 3: Preview of Today's Lab — utils.py Structure (6 minutes)

Create a skeleton `utils.py` that students will complete in the lab:

```python
def safe_int(prompt):
    """
    Safely get an integer from the user.
    Keeps asking until valid input is provided.
    """
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("   ERROR: Please enter a valid integer.")

def format_money(value):
    """
    Format a numeric value as USD currency.
    Example: 1234.5 becomes $1,234.50
    """
    return f"${value:,.2f}"

if __name__ == "__main__":
    print("Testing utils.py:")
    value = safe_int("Enter a number: ")
    print(f"You entered: {value}")
    print(f"Formatted as money: {format_money(value)}")
```

Create a companion `main.py`:

```python
from utils import safe_int, format_money

print("=== Simple Banking Demo ===")
balance = safe_int("Enter your account balance: $")
withdrawal = safe_int("Enter withdrawal amount: $")

new_balance = balance - withdrawal
print(f"Previous balance: {format_money(balance)}")
print(f"Withdrawal:      {format_money(withdrawal)}")
print(f"New balance:     {format_money(new_balance)}")
```

**Teaching Point**: Run both files to show the integrated workflow. Emphasize that `main.py` is the user-facing script; `utils.py` contains the reusable functions. This structure is exactly what the lab will produce.

## 7. Lab Specification and Walkthrough: Building and Using utils.py (25 minutes)

### Lab Objective

Students will create a `utils.py` module containing two essential functions (`safe_int()` and `format_money()`) and use them in a `main.py` script. They will practice proper module structure, imports, and the `__name__ == "__main__"` pattern.

### Lab Walkthrough with Checkpoints

#### Checkpoint 1: Setup and File Creation (0:35–0:40, 5 minutes)

**Objective:** Students create the basic file structure and establish the project foundation. This checkpoint ensures they understand file organization before writing code.

**Tasks:**

1. **Create two empty `.py` files in the same folder:** `utils.py` and `main.py`.
   - Navigate to a project folder (e.g., `~/Desktop/Day9Lab/`).
   - Create two new files with these exact names.
   - Verify both files exist in the same directory.

2. **Add a module docstring to `utils.py`:**

```python
"""
utils.py
Utility functions for common programming tasks.
Provides reusable functions for input validation and output formatting.
"""
```

This docstring serves two purposes: it documents the module's purpose and is required by professional Python style guides (PEP 257).

3. **Add the beginning of `main.py`:**

```python
"""
main.py
Main script demonstrating use of utils.py
Orchestrates user interaction using utility functions.
"""

from utils import safe_int, format_money

print("=== Utility Functions Demo ===")
```

Note: The imports at the top will initially cause an error because `safe_int` and `format_money` don't exist yet. This is intentional—students should see the error, understand it, and resolve it in subsequent checkpoints.

**Validation Criteria:**
- [ ] Both files exist in the same directory.
- [ ] Each file has a docstring explaining its purpose.
- [ ] `main.py` already imports the functions (error expected at this stage).
- [ ] Students can explain why `main.py` currently fails when run.

**Common Question:** "Why would we import functions that don't exist yet?"  
**Answer:** This mirrors real development. You often design the interface (what functions you'll use) before implementing them. This checkpoint establishes the contract: `main.py` expects `utils.py` to provide these functions. In the next checkpoint, you make good on that promise.

---

#### Checkpoint 2: Implement safe_int() (0:40–0:48, 8 minutes)

**Objective:** Students implement a robust input validation function that exemplifies defensive programming. This function demonstrates error handling and user experience considerations.

**Task:** In `utils.py`, add the `safe_int()` function:

```python
def safe_int(prompt):
    """
    Safely request and return an integer from the user.
    Loops until valid input is provided.
    
    Args:
        prompt (str): The message to display to the user.
    
    Returns:
        int: The validated integer input.
    
    Example:
        >>> value = safe_int("Enter your age: ")
        Enter your age: abc
        ERROR: Invalid input. Please enter an integer.
        Enter your age: 25
        >>> value
        25
    """
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("   ERROR: Invalid input. Please enter an integer.")
```

**Key Teaching Points:**
- The `while True` loop continues until `return` is called (when `int()` succeeds).
- The `try-except` block catches `ValueError`, which `int()` raises for non-numeric input.
- The error message is intentionally friendly ("Please enter an integer") rather than technical.
- The indented error message (with spaces) provides visual feedback to the user.

**Validation Criteria:**
- [ ] Function is defined in `utils.py`.
- [ ] It includes a complete docstring with description, arguments, return value, and example.
- [ ] It uses a `while True` loop to handle repeated invalid input.
- [ ] It includes a `try-except` block catching `ValueError`.
- [ ] It provides user-friendly error messages.
- [ ] The function has no syntax errors and can be called successfully.

**Quick Test in the Python Interpreter:**
```python
# Run this in Python REPL to test:
from utils import safe_int
value = safe_int("Enter a number: ")
# Type an invalid value, see the error message, then enter a valid one
```

---

#### Checkpoint 3: Implement format_money() (0:48–0:56, 8 minutes)

**Objective:** Students learn formatted output using f-strings and format specifiers. This function demonstrates how to present data professionally.

**Task:** In `utils.py`, add the `format_money()` function:

```python
def format_money(value):
    """
    Format a numeric value as US currency.
    
    Args:
        value (float or int): The amount to format.
    
    Returns:
        str: Formatted string like "$1,234.50"
    
    Example:
        >>> format_money(1234.5)
        '$1,234.50'
        >>> format_money(5)
        '$5.00'
        >>> format_money(999999.1)
        '$999,999.10'
    """
    return f"${value:,.2f}"
```

**Key Teaching Points:**
- F-strings (f"...") allow expressions inside curly braces.
- The format specifier `:,.2f` does three things:
  - `,.` adds thousand-separators (commas).
  - `2f` formats as a float with exactly 2 decimal places.
- This replaces older string formatting methods and is the modern Python standard.

**Validation Criteria:**
- [ ] Function is defined in `utils.py`.
- [ ] It includes a complete docstring with examples showing various inputs.
- [ ] It uses f-string formatting with the `:,.2f` specifier.
- [ ] It returns a properly formatted string with dollar sign, commas, and two decimals.
- [ ] The function has no syntax errors.

**Quick Test in the Python Interpreter:**
```python
# Mentally verify or test these:
format_money(1234.5)      # Should return "$1,234.50"
format_money(5)           # Should return "$5.00"
format_money(999999.1)    # Should return "$999,999.10"
format_money(0)           # Should return "$0.00"
```

---

#### Checkpoint 4: Integration and Testing (0:56–1:00, 4 minutes)

**Objective:** Students complete the module structure, verify both functions work together, and experience the satisfying moment when separate pieces integrate seamlessly.

**Tasks:**

1. **Add the `if __name__ == "__main__":` guard to `utils.py`** so it can test itself:

```python
if __name__ == "__main__":
    print("Testing utils.py directly:")
    print()
    test_value = safe_int("Enter a test number: ")
    print(f"You entered: {test_value}")
    print(f"Formatted as money: {format_money(test_value)}")
```

2. **Flesh out `main.py`** to use both functions in a realistic scenario:

```python
from utils import safe_int, format_money

print("=== Simple Account Manager ===\n")

account_balance = safe_int("Enter your starting balance: $")
print(f"Your balance: {format_money(account_balance)}\n")

transaction = safe_int("Enter a transaction amount: $")
new_balance = account_balance + transaction

print(f"Previous balance: {format_money(account_balance)}")
print(f"Transaction:     {format_money(transaction)}")
print(f"New balance:     {format_money(new_balance)}")
```

3. **Testing:**
   - Run `python utils.py` directly. It should prompt for input, accept a number, and display formatted output.
   - Run `python main.py` directly. It should simulate a simple banking interaction without errors.
   - Verify that both scripts accept invalid input gracefully and re-prompt.

**Validation Criteria:**
- [ ] Both files are in the same directory with correct naming (no naming conflicts).
- [ ] `main.py` successfully imports and uses both functions.
- [ ] Running `utils.py` directly displays the test output.
- [ ] Running `main.py` provides a functional banking interface.
- [ ] User can enter integers without the program crashing.
- [ ] Currency values are formatted correctly with commas and two decimal places.
- [ ] No import errors occur when running either file.

**Celebration Point:** At this stage, students have created a working modular system. `main.py` is clean and focused on user interaction. `utils.py` provides reusable, tested functions. This is the professional pattern scaled down for learning.

---

### Stretch Goals (If Time Permits)

Students who finish early can extend the lab:

1. **Add a `menu_choice()` function to `utils.py`**: Creates a simple menu and returns the user's choice as an integer.
2. **Create a second module**: Extract formatting functions into `formatters.py` and import from there.
3. **Add more functions**: Implement `get_positive_number()`, `percent_of()`, or `compound_interest()` in `utils.py`.

## 8. Troubleshooting: Common Import Pitfalls and Fixes (Reference Material for Instructors)

### Pitfall 1: Naming Conflict with Standard Library

**Symptom:** Student creates a file named `random.py`. When they try to `import random` in their main script, it imports their file instead of the standard library module. Suddenly, functions like `random.randint()` stop working, and instead they get an error like `AttributeError: module 'random' has no attribute 'randint'`.

**Root Cause:** Python searches for modules in the current directory first, before checking the standard library. Creating `random.py` in your project directory shadows the built-in `random` module. Any script that imports `random` gets your file instead of the standard library.

**Fix:** Rename the custom file to something descriptive that doesn't collide with standard library names. Good alternatives: `random_utils.py`, `my_random.py`, `game_random.py`, or `custom_random.py`. This establishes a naming convention that avoids collisions entirely.

**Prevention Strategy:** Avoid single-word module names that match standard library modules. Aim for multi-word names or clearly prefixed names. When in doubt, check the Python documentation for a list of standard library module names.

**Interactive Debugging:**
```python
# To see which file Python is importing, use:
import random
print(random.__file__)  # Shows the file path
# If it shows your current directory, you've shadowed the stdlib
```

---

### Pitfall 2: Incorrect Import Syntax

**Symptom:** Student writes `import math.sqrt()` or `from math import sqrt()` or `import math sqrt`. The code fails with a `SyntaxError` or `ImportError`.

**Root Cause:** Confusion between importing a module vs. calling a function. The syntax is very strict:
- Import statements do NOT use parentheses.
- You import names (modules, functions), not expressions.

**Fix:** Clarify the three correct forms:
```python
import math                    # Correct: import module
from math import sqrt          # Correct: import function from module
sqrt(25)                       # Correct: call function

# These are WRONG:
import math.sqrt()             # Wrong: mixing import and function call
from math import sqrt()        # Wrong: parentheses in import
math.sqrt(25)                  # Correct (this one is right)
```

**Prevention Strategy:** Create a reference card with the three import forms clearly labeled. Practice writing imports until they become second nature.

---

### Pitfall 3: Incorrect File Organization

**Symptom:** `utils.py` is in one folder, `main.py` is in another folder (e.g., different directories or a `src/` subfolder structure). When `main.py` tries to `from utils import function`, it fails with `ModuleNotFoundError: No module named 'utils'`.

**Root Cause:** Python doesn't find `utils.py` because it's not in the same directory or on the Python path. The search strategy is:
1. The directory where the running script lives (first priority)
2. The `PYTHONPATH` environment variable directories
3. Standard library locations

For Basics-level projects, files must be in the same directory.

**Fix:** Keep related files in the same directory. For the purposes of this course, maintain a flat structure:

```
project/
├── main.py
└── utils.py
```

Both files live in the same folder. When you run `python main.py`, Python looks in the same directory for imports.

**Prevention Strategy:** Always verify that `main.py` and `utils.py` are in the same folder before attempting to import. Use `os.getcwd()` and `os.listdir()` to verify your working directory and file structure if confused.

**Advanced Note (for later):** As projects grow, Python uses packages (folders with `__init__.py` files) to organize modules. This is beyond Basics scope but worth knowing exists.

---

### Pitfall 4: Using `__name__` Incorrectly

**Symptom:** Code under `if __name__ == "__main"` (missing closing underscores) or `if __name__ == "main"` (without underscores) never runs. Or the code runs when it shouldn't.

**Root Cause:** Typo in the special variable name or incorrect string comparison. Common mistakes:
- `if __name__ == "__main"` (missing closing `__`)
- `if __name__ == "main"` (missing underscores entirely)
- `if name == "__main__"` (forgot the double underscores on the variable)

**Fix:** The correct form is `if __name__ == "__main__":` with:
- Double underscores at the start: `__`
- Double underscores at the end: `__`
- The word `main` in the middle
- Double quotes around the string

```python
# Correct:
if __name__ == "__main__":
    print("Running as main")

# Wrong:
if __name__ == "__main":        # Missing closing __
if __name__ == "main":           # Missing all underscores
if name == "__main__":           # Forgot __ on variable
```

**Prevention Strategy:** Copy-paste the correct form from trusted documentation or a template. Type it slowly and deliberately until it becomes muscle memory. Use your IDE's autocomplete if available.

---

### Pitfall 5: Circular Imports

**Symptom:** `module_a.py` imports from `module_b.py`, and `module_b.py` imports from `module_a.py`. Python raises `ImportError` or `ModuleNotFoundError`, or functions are unexpectedly undefined.

**Root Cause:** Each module tries to import the other, creating a circular dependency. When Python tries to import `module_a`, it discovers that `module_a` imports `module_b`. It starts importing `module_b`, but then discovers that `module_b` imports `module_a`. Python can't complete either import, resulting in errors.

**Fix:** Restructure code so one module is independent and doesn't import from the other. In Basics projects, the standard pattern is:
- `utils.py` (or other utility modules) contain **only functions**, with **no imports** from `main.py`.
- `main.py` imports from `utils.py`, but `utils.py` never imports from `main.py`.

This hierarchical structure ensures no circular dependencies.

**Prevention Strategy:** Follow a clear import hierarchy:
- Entry point (`main.py`) sits at the top.
- Utility modules (`utils.py`) sit below.
- Main imports utilities; utilities don't import main.
- Never have two files importing from each other.

**Example Structure:**

```python
# File: utils.py
def helper():
    return "I help"

# File: main.py
from utils import helper      # OK: main imports utils

print(helper())               # OK: works fine
```

**Never do this:**

```python
# File: utils.py
from main import setup_data   # WRONG: circular!

# File: main.py
from utils import helper      # This creates a cycle
```

---

### Bonus Pitfall: Running the Wrong File

**Symptom:** Student runs `utils.py` directly and sees test output. They assume everything works. Then they run `main.py`, which imports `utils.py`, and suddenly new errors appear.

**Root Cause:** Running `utils.py` directly executes the `if __name__ == "__main__":` block. When `main.py` imports `utils.py`, this block is skipped. If there's an error in the import or in the module-level code (outside the main guard), it surfaces only when importing.

**Fix:** Always test by running `main.py` (the entry point), not `utils.py` (the utility module). If `main.py` works, the imports are correct. If `utils.py` errors when imported, debug the import or the module-level code.

**Prevention Strategy:** Establish a testing workflow:
1. Run the entry point (`main.py`).
2. If errors occur, check the full error message to identify the source.
3. Debug the module or import that's causing the issue.

---

## 9. Quick-Check Formative Assessment (Reference Material for Instructors)

**Question 1:** What is the value of `__name__` when `utils.py` is imported into `main.py` as a module?

**Answer:** `__name__` equals `"utils"` (the module name).

---

**Question 2:** If you want to use only the `sqrt` function from the `math` module without prefixing it with `math.`, which import form do you use?

**Answer:** `from math import sqrt`

---

**Question 3:** Why is naming a custom file `string.py` problematic?

**Answer:** It shadows the standard library `string` module, causing import errors or unexpected behavior.

---

**Question 4:** In the `safe_int()` function, which exception is caught to detect invalid integer input?

**Answer:** `ValueError` (raised by `int()` when the string cannot be converted to an integer).

---

**Question 5:** What is the purpose of the `if __name__ == "__main__":` pattern?

**Answer:** It allows a file to run standalone while also being importable as a module without executing setup code.

---

## 10. Wrap-Up Narrative: Professional Context

This section is delivered during the final 2–3 minutes of the 60-minute hour as the in-class wrap-up. The following reference materials (Sections 8–9) are not part of the core 60-minute delivery and are provided for instructors who want extension activities, additional troubleshooting examples, or advanced practice problems after class.

### In-Class Wrap-Up (2–3 minutes)

"Today, you've learned something fundamental that professional Python developers use every single day. Every large project—web applications, data analysis pipelines, machine learning systems—is built on the principle of modules and imports.

Think about NumPy, Pandas, Django, or any package you might encounter. They're all organized the same way: a collection of modules that you import as needed. By writing `utils.py` today, you're not just completing an assignment. You're practicing the architectural thinking that underpins real software.

Moreover, you've solved practical problems: input validation (`safe_int`), formatting (`format_money`). These aren't contrived exercises. Real applications validate user input constantly and format data for display. Your `utils.py` is the beginning of a personal library of reusable code.

As you progress—to object-oriented programming, web frameworks, testing—you'll use these same patterns. Import a class. Create a helper. Organize logic into files. This foundation is essential.

In your next assignment, when you're working on a larger project, remember today: separate concerns into modules, avoid naming conflicts, and use imports to bring it all together. That's how professionals build software."

---

## 11. Facilitation Notes: Classroom Management and Differentiation

### Pre-Class Setup and Materials Preparation

- **Test your demo files thoroughly** (`stdlib_demo.py`, `math_helpers.py`, `use_math_helpers.py`) on your system and the current Python version before teaching. Ensure they run without errors and produce the expected output. This prevents embarrassing failures during live demonstrations.
- **Have template code ready** (`utils.py` and `main.py` skeletons) on a slide or in a shareable document so students can copy-paste the base structure if they get stuck on file creation.
- **Set up a class project folder structure** (e.g., `day9_lab/`) that students can reference, or guide them through creating one. Verify that all students have the same directory structure before they start writing code.
- **Have backup implementations** available in case you need to share a working solution on screen. This accelerates debugging if a student's code is irreparably broken mid-lab.

### Classroom Management During the Lab

- **Circulate frequently** during Checkpoint 1 and 2. File organization and import errors are the most common blockers at this stage. Catching them early prevents cascading failures.
- **Use error messages as teaching moments**. When a student encounters an import error, don't fix it for them. Ask: "What file is Python looking for? Where is it? Are they in the same directory?" Guide them to the diagnosis.
- **Celebrate small wins**. When a checkpoint passes without errors, acknowledge it. This hour represents a significant mindset shift for learners; positive reinforcement matters.

### Common Misconceptions and Interventions

1. **"I have to use the exact names `utils.py` and `main.py`."**
   - Clarify: The names are project convention, not Python law. However, using clear, descriptive names prevents errors. Discourage students from using single-word names that shadow the standard library. Emphasize professional convention: clarity and consistency matter in shared codebases.

2. **"`__name__` is something I create, like a variable."**
   - Clarify: `__name__` is a **special variable** created automatically by Python. Every module has it. You don't create it; you check its value. It's read-only. Analogy: "It's like your social security number—the system assigns it, and you can look at it, but you can't change it."

3. **"If I import a module, all the code in it runs."**
   - Clarify: Only the code outside of `if __name__ == "__main__":` runs on import. Code inside that guard runs only when the file is executed directly. This is why test code goes inside the guard—it shouldn't clutter imports.

4. **"The error message is confusing. I don't know how to fix it."**
   - Teach error message reading systematically: ModuleNotFoundError tells you Python can't find a file. ImportError tells you the module exists but doesn't have what you're looking for. Guide students to extract the key information and reason about what's wrong.

### Differentiation Strategies for Varied Learners

**For Students Who Finish Early:**
- Assign stretch goals immediately: build a `formatters.py` module with additional functions (`format_percentage()`, `format_phone_number()`) and import from both `utils.py` and `formatters.py` in `main.py`.
- Have them create a `config.py` module to store constants (e.g., `COMPANY_NAME`, `MAX_TRANSACTION_AMOUNT`) and import them in `main.py`.
- Ask them to document their modules with comprehensive docstrings following the Google or NumPy style guide.
- Introduce the concept of packages (folders with `__init__.py`), which naturally extends module organization.

**For Students Struggling:**
- Pair them with a peer who successfully completed Checkpoint 1 (file organization). Peer teaching is often more accessible than instructor re-teaching.
- Provide a partially completed `utils.py` and have them finish the functions. This reduces cognitive load.
- Walk through Checkpoints 1–2 together as a small group, then release them to complete Checkpoints 3–4 independently.
- Use the **debugging strategy session**: Together, run `utils.py` directly, check for errors, fix them, then attempt `main.py`. This establishes a systematic debugging workflow.

### Pacing Guidance and Time Management

- **If running behind by 5–10 minutes**: Skip the second demo (`math_helpers.py` / `use_math_helpers.py`) and move directly to the third demo (preview of today's lab). The second demo reinforces the `__name__` pattern, but Checkpoint 4 covers this anyway.
- **If running exactly on time**: Proceed as planned. The lab fits snugly into 25 minutes with all four checkpoints.
- **If running ahead by 10+ minutes**: Use extra time for the stretch goals, code review (examine a student's solution on screen), or introduce the concept of packages or relative imports (beyond Basics scope but intellectually enriching).

## 12. Assessment and Differentiation Rubric

### Completion Checklist (All items required to pass)

- [ ] `utils.py` exists in the same directory as `main.py`.
- [ ] `utils.py` contains `safe_int()` function with a try-except block and a while loop.
- [ ] `utils.py` contains `format_money()` function that formats values as USD currency.
- [ ] `utils.py` includes the `if __name__ == "__main__":` guard with test code.
- [ ] `main.py` successfully imports both functions from `utils.py`.
- [ ] `main.py` runs without `ImportError` or `ModuleNotFoundError`.
- [ ] `safe_int()` handles invalid user input and re-prompts (no crashes on non-integer input).
- [ ] `format_money()` produces output like `"$1,234.50"` (with commas and two decimal places).

### Grading Rubric (10 points)

| Criterion | Points | Rubric |
|-----------|--------|--------|
| **Module Structure** | 2 | File organization is correct; both files in same directory with no naming conflicts. (2 pts) or File exists but minor naming confusion. (1 pt) or Files in wrong location or wrong names. (0 pts) |
| **safe_int() Implementation** | 2 | Robust input validation with try-except and while loop. (2 pts) or Basic loop and try-except but missing edge case handling. (1 pt) or Function missing or non-functional. (0 pts) |
| **format_money() Implementation** | 2 | Correct f-string format specifier `:,.2f` producing proper output. (2 pts) or Formatting works but specifier is slightly off (e.g., `:,.1f`). (1 pt) or Function missing or formatting incorrect. (0 pts) |
| **Module Imports** | 2 | `main.py` correctly imports both functions with no errors. (2 pts) or Import succeeds but syntax is unconventional. (1 pt) or Import fails or missing. (0 pts) |
| **Execution and Testing** | 2 | Both files run without errors; functions produce correct output. (2 pts) or Files run but output has minor issues (e.g., rounding). (1 pt) or Files crash or produce incorrect output. (0 pts) |

**Total: 10 points**

---

### Completion Criteria

- **Pass (7–10 points)**: Student demonstrates understanding of modules, imports, and custom function creation. They can run both files without errors and produce correct output.
- **Needs Revision (4–6 points)**: Core functionality works, but there are naming conflicts, import errors, or minor logic bugs. Student should revise and resubmit.
- **Incomplete (0–3 points)**: Major structural issues (file organization, missing functions, or import errors). Student needs re-teaching or one-on-one support.

---

### Stretch Goals (Bonus, up to +2 points)

- [ ] **Bonus +1**: Create a `formatters.py` module with additional formatting functions (e.g., `format_percentage()`, `format_phone_number()`) and import from both `utils.py` and `formatters.py` in `main.py`.
- [ ] **Bonus +1**: Add comprehensive docstrings to all functions and modules, and write a README file explaining how to use the modules.

---

### Exit Ticket (Verbal or Written)

Before students leave, ask:

1. **What does `__name__ == "__main__"` do?** (Understanding the control flow pattern)
2. **If you created a file called `math.py`, what would happen?** (Anticipate naming conflicts)
3. **Why is it better to have `utils.py` and `main.py` separate instead of putting everything in one file?** (Code organization and reusability)

---

## Summary

This hour equips students with professional module and import practices. By creating and using `utils.py`, they move beyond single-file scripts to organized, reusable code. The troubleshooting section prepares them for the real errors they'll encounter, and the assessment rubric ensures they've internalized the concepts. This foundation directly supports all advanced topics that follow.
