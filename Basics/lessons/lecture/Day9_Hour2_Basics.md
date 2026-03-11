# Day 9, Hour 2: Scope + Common Function Mistakes (Course Hour 34)
**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 34 – Scope + common function mistakes  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Scope is famously tricky for beginners. Clarify the boundary between the "inside" of a function and the "outside" global environment. Emphasize passing data explicitly rather than implicitly relying on global state. Introduce default parameters as a convenient feature.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain the difference between local scope and global scope.
2. Avoid common bugs by passing variables explicitly into functions instead of relying on global variables.
3. Understand variable shadowing.
4. Use default parameters to create optional arguments in functions."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: The concept of Scope
- **0:05–0:18** Core concept: Local vs Global Variables
- **0:18–0:30** Live demo: The danger of globals + passing variables cleanly
- **0:30–0:40** Core concept: Default parameters
- **0:40–0:55** Guided lab: Calculator Functions (avoiding divide-by-zero)
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour34_scope_demo.py` ready for live coding.
- Open another file named `hour34_calculator.py` for the lab.
- **Say:** "Please open a new file called `scope_testing.py`. We are going to intentionally break things to see how memory boundaries work."

---

## 3) Opening Script: The Concept of Scope (~5 minutes)

**Say:**
"When you learn functions, you almost immediately run into situations where your code complains that a variable isn't defined, even though you just defined it three lines ago.

This introduces us to **Scope**. 

Scope defines the visibility and lifetime of a variable. Not every variable is visible everywhere in your code. Python puts up walls around functions. What happens inside a function, stays inside that function... unless we explicitly pass it out using a `return` statement."

---

## 4) Concept: Local vs Global Variables

### 4.1 Local variables

**Say:**
"Variables created inside a function are called **local variables**. They only belong to that specific function call. Once the function finishes running, the local variables are thrown in the trash."

**Type and narrate:**

```python
def make_greeting():
    # 'message' is a local variable
    message = "Good morning!"
    print(message)

# Calling the function works fine
make_greeting()

# Trying to access the local variable from the outside will crash!
# print(message)  # NameError: name 'message' is not defined
```

**Say:**
"If you uncomment that last `print(message)` line, Python will throw a `NameError`. The outside program doesn't know what `message` is. It was safely isolated inside `make_greeting`."

### 4.2 Global variables and scope boundaries

**Say:**
"Variables created completely outside of any function, usually at the top level of your script, are called **global variables**. All functions can see them, but modifying them inside a function is a recipe for disaster."

**Type and narrate:**

```python
discount_rate = 0.10  # A global variable

def calculate_price(base_price):
    # The function can 'see' the global variable
    return base_price - (base_price * discount_rate)

print(calculate_price(100))
```

**Say:**
"While the function *can* read `discount_rate`, relying on global variables is generally considered bad practice. If your program is 500 lines long, and you have variables modified all over the place, finding bugs becomes nearly impossible."

---

## 5) Live Demo: The Danger of Globals + Variable Shadowing

### 5.1 Demonstrating the bug

**Say:**
"Let me show you a very common bug."

**Type and narrate:**

```python
score = 0  # Global tracker

def add_points(points):
    # Bug! Python thinks we are creating a new local 'score'
    # but we are trying to add to the global one.
    # score = score + points  # This causes an UnboundLocalError
    pass
```

**(Optional: you can show the `UnboundLocalError` if you try to assign `score = score + points`).**

**Say:**
"When you assign a value to a variable inside a function using `=`, Python assumes you mean a local variable. If you use a name that already exists globally, your local variable **shadows** the global one. It eclipses it.

The professional fix isn't to force Python to use the global variable. The fix is to pass the data in, and return the data out."

**Type the fix:**

```python
def add_points(current_score, points):
    # Takes data in, figures out new value, returns it out
    return current_score + points

score = 0
print(f"Start: {score}")

score = add_points(score, 50)
print(f"After add: {score}")
```

**Say:**
"Data goes in through parameters, data comes out through the `return` statement. This makes your function 'pure' and predictably easy to test. It doesn't secretly rely on any hidden global states."

---

## 6) Concept: Default Parameters

**Say:**
"Before we go to our lab, there is a very useful feature of function definitions: default parameters. Sometimes you want a parameter to be optional, falling back to a sensible default if the programmer doesn't provide one."

**Type and narrate:**

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Providing both arguments
greet("Alice", "Good morning")

# Provding only the required argument
greet("Bob") 
```

**Say:**
"By defining `greeting="Hello"` in the function header, we've made `greeting` optional. If you pass a second argument, it overrides the default. If you don't, it uses 'Hello'.
Important rule: All default parameters must come *after* required parameters in the definition."

---

## 7) Hands-on Lab: Calculator Functions without crashing

### 7.1 Lab overview

**Say:**
"We are going to build a suite of math functions for a calculator. You will need to make sure they use local variables correctly, return values safely, and avoid crashes—specifically, avoiding division by zero."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Calculator Functions**

**Task:**
1. Write four separate math functions: `add`, `subtract`, `multiply`, and `divide`.
2. Each function should take two parameters: `num1` and `num2`.
3. For the `divide` function, add a local `if` check. If `num2` is `0`, return the string `"Error: Cannot divide by zero!"`. Otherwise, return the normal result.
4. Build a very simple CLI loop that asks the user for an operation and two numbers, calls the correct function, and prints the returned result.
5. Provide a default parameter to your `multiply` function so that if the user somehow only passes one number, it multiplies it by 1 by default. (e.g., `def multiply(num1, num2=1):`)

**Requirements:**
- Do not use global variables inside your functions. The inputs must be passed through parameters.
- All functions must use `return`, not `print()`.

---

**Instructor Note for Circulation:**
Remind learners that asking for the numbers using `input()` needs to happen in the main loop, not inside the math functions. The math functions should just do math. Check that they correctly convert `input()` strings to floats before passing them to the functions.

### 7.3 Walkthrough solution

**After 15-20 minutes, review the solution:**

```python
# hour34_calculator.py

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2=1):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

# Main Program Scope
while True:
    print("\n--- Calc ---")
    op = input("Choose: [a]dd, [s]ubtract, [m]ultiply, [d]ivide or [q]uit: ")
    
    if op == 'q':
        break
        
    x = float(input("First number: "))
    # Simplification for demo: assuming they always enter two numbers
    y = float(input("Second number: "))
    
    if op == 'a':
        print("Result:", add(x, y))
    elif op == 's':
        print("Result:", subtract(x, y))
    elif op == 'm':
        print("Result:", multiply(x, y))
    elif op == 'd':
        print("Result:", divide(x, y))
    else:
        print("Invalid operation.")
```

**Say:**
"These four functions are independent, isolated silos. They don't know the main program exists. They take inputs safely, compute, and deal the data back out. This isolation prevents bugs from cascading."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"We explored Scope. A local variable created inside a function dies when the function is done. A global variable lives entirely outside. We learned that the safest way to write programs is to pass data *into* a function through parameters, and pass our data *out* via returns."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: If you create a variable inside a function, can you use it outside? Why or why not?"

**Expected answer:** Let learners answer. "No, because the variable has local scope. It only exists while the function is actively executing."
