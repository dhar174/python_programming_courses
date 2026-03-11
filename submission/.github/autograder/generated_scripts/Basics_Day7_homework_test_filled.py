#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 7 Homework
# 
# **Runbook alignment (Day 7, Hours 25-28):**
# - Hour 25: Conditionals (`if/elif/else`) and boundary values
# - Hour 26: `while` loops + sentinel patterns
# - Hour 27: `for` loops + `range()`
# - Hour 28: Loop patterns (counter, accumulator, min/max)
# 
# Use only Basics-scope concepts from class. Keep output clear and deterministic.
# 

# ### Autograder Integration Requirements
# 
# This assignment is graded automatically.
# 
# - Put your complete runnable solutions in this notebook.
# - Your notebook will be converted to `day7.py` and checked against `criteria.json`.
# - Output strings must match expected labels and formatting exactly.
# - Keep numeric formatting precise when requested (for example, `8.40`).
# - Do not use randomness, live date/time, or external files.
# - Avoid infinite loops by updating loop-control variables correctly.
# 

# ---
# ## Part 1: Hour 25 - Conditionals and boundary handling (25 points)
# 

# ### Exercise 1.1: Shipping Tier Calculator (15 points - graded)
# 
# Use this tier policy:
# - `weight <= 2` -> **Standard** (`$5.00`)
# - `2 < weight <= 10` -> **Priority** (`$8.00`)
# - `weight > 10` -> **Heavy** (`$12.00`)
# 
# Test boundary inputs: `1.00`, `5.00`, `10.00`, and `10.01`.
# Print the category and cost for each weight using readable labels.
# 

# In[ ]:


# Exercise 1.1 - shipping tiers with boundaries
weights: list[float] = [1.00, 5.00, 10.00, 10.01]

for w in weights:
    if w <= 2:
        category = "Standard"
        cost = "$5.00"
    elif w <= 10:
        category = "Priority"
        cost = "$8.00"
    else:
        category = "Heavy"
        cost = "$12.00"
    print(f"Weight {w:.2f}kg -> {category} ({cost})")

print("Boundary check: ordering avoids overlap")


# ### Exercise 1.2: Score Band Classifier (10 points - graded)
# 
# Write branching logic that assigns bands:
# - `>= 90`: `A`
# - `>= 80`: `B`
# - `>= 70`: `C`
# - otherwise: `Needs Review`
# 
# Run it on `[90, 89, 80, 79, 70, 69]` and print deterministic output.
# Include one short line explaining why branch order matters.
# 

# In[ ]:


# Exercise 1.2 - score bands
scores: list[int] = [90, 89, 80, 79, 70, 69]

for score in scores:
    if score >= 90:
        band = "A"
    elif score >= 80:
        band = "B"
    elif score >= 70:
        band = "C"
    else:
        band = "Needs Review"
    print(f"Score {score} -> {band}")

print("Ordering note: highest thresholds must appear first in an if/elif chain.")


# ---
# ## Part 2: Hour 26 - while loops and sentinel patterns (25 points)
# 

# ### Exercise 2.1: Password Attempts Loop (15 points - graded)
# 
# Build a `while` loop with these rules:
# - Correct password is `python123`
# - Maximum of 3 attempts
# - Stop immediately on success
# - Otherwise lock after 3 failed attempts
# 
# For deterministic testing, use this simulated sequence:
# `["guess", "hello", "python123"]`
# Print each attempt result and final login status.
# 

# In[ ]:


# Exercise 2.1 - password attempts
correct_password = "python123"
attempt_inputs: list[str] = ["guess", "hello", "python123"]

attempt = 0
success = False
max_attempts = 3

while attempt < max_attempts and attempt < len(attempt_inputs):
    guess = attempt_inputs[attempt]
    attempt += 1

    if guess == correct_password:
        print(f"Attempt {attempt}: correct password")
        success = True
        break

    print(f"Attempt {attempt}: wrong password")

if success:
    print("Login status: success")
else:
    print("Login status: locked out")


# ### Exercise 2.2: Sentinel Command Collector (10 points - graded)
# 
# Collect commands until sentinel `q` appears.
# 
# Use deterministic input sequence:
# `["start", "help", "status", "q", "ignored"]`
# 
# Requirements:
# - Store accepted commands before sentinel
# - Stop loop when sentinel is reached
# - Print sentinel used and accepted command list
# 

# In[ ]:


# Exercise 2.2 - sentinel collector
command_inputs: list[str] = ["start", "help", "status", "q", "ignored"]
sentinel = "q"

accepted_commands: list[str] = []
idx = 0

while idx < len(command_inputs):
    cmd = command_inputs[idx]
    idx += 1

    if cmd == sentinel:
        break

    accepted_commands.append(cmd)

print(f"Sentinel stop word: {sentinel}")
print(f"Accepted commands: {accepted_commands}")


# ---
# ## Part 3: Hour 27 - for loops and range() (25 points)
# 

# ### Exercise 3.1: Multiplication Table (15 points - graded)
# 
# Set `n_value = 4` and print a multiplication table from `1` through `10` using `range()`.
# Use readable labels (for example: `Table 4 x 7 = 28`).
# Make sure your range end includes 10 correctly.
# 

# In[ ]:


# Exercise 3.1 - multiplication table
n_value = 4

for i in range(1, 11):
    print(f"Table {n_value} x {i} = {n_value * i}")


# ### Exercise 3.2: Range Pattern Checks (10 points - graded)
# 
# Print the exact lists produced by:
# - `range(1, 4)`
# - `range(0, 11, 2)`
# 
# Then print one sentence explaining why the stop value is excluded.
# 

# In[ ]:


# Exercise 3.2 - range checks
range_one = list(range(1, 4))
range_two = list(range(0, 11, 2))

print(f"range(1, 4) -> {range_one}")
print(f"range(0, 11, 2) -> {range_two}")
print("Loop type used: for")
print("range() includes the start value and excludes the stop value.")


# ---
# ## Part 4: Hour 28 - loop patterns (counter, accumulator, min/max) (25 points)
# 

# ### Exercise 4.1: Number Stats for Fixed Count (15 points - graded)
# 
# Given `numbers = [8, 3, 9, 15, 7]`, compute and print:
# - Count
# - Sum
# - Min
# - Max
# - Average (formatted to 2 decimals)
# 
# Use explicit loop patterns rather than calling `sum()`/`min()`/`max()` directly.
# 

# In[ ]:


# Exercise 4.1 - fixed-count stats using loop patterns
numbers: list[int] = [8, 3, 9, 15, 7]

count = 0
total = 0
min_val = numbers[0]
max_val = numbers[0]

for value in numbers:
    count += 1
    total += value

    if value < min_val:
        min_val = value
    if value > max_val:
        max_val = value

average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
print(f"Average: {average:.2f}")
print("Pattern check: counter+accumulator+min/max")


# ### Exercise 4.2: Variable Count with `done` Sentinel (10 points)
# 
# Optional extension (still in Basics scope):
# Use a `while` loop to read values until sentinel `done`, then print the same stats as above.
# Demonstrate with a deterministic list of pseudo-inputs in code comments.
# 

# In[ ]:


# Exercise 4.2 - optional variable-count stats
pseudo_inputs: list[str] = ["8", "3", "9", "15", "7", "done"]

values: list[int] = []
idx = 0

while idx < len(pseudo_inputs):
    raw = pseudo_inputs[idx]
    idx += 1

    if raw == "done":
        break

    values.append(int(raw))

if values:
    opt_count = 0
    opt_total = 0
    opt_min = values[0]
    opt_max = values[0]

    for value in values:
        opt_count += 1
        opt_total += value
        if value < opt_min:
            opt_min = value
        if value > opt_max:
            opt_max = value

    opt_avg = opt_total / opt_count
    print(f"Optional count: {opt_count}")
    print(f"Optional sum: {opt_total}")
    print(f"Optional min: {opt_min}")
    print(f"Optional max: {opt_max}")
    print(f"Optional average: {opt_avg:.2f}")

print("Safe min init: seed min/max from the first collected numeric value.")


# ---
# ## Reflection Questions (10 points)
# 
# Answer in the markdown cell below:
# 
# 1. Which boundary case was easiest to get wrong in Hour 25, and why?
# 2. What variable must change each loop iteration to avoid infinite loops?
# 3. How do `range(1, 4)` and `range(1, 5)` differ?
# 4. What is a safe strategy for initializing min/max before looping?
# 5. Which loop pattern (counter, accumulator, min/max) did you find most useful?
# 

# ### Your Answers
# 
# 1.
# 
# 2.
# 
# 3.
# 
# 4.
# 
# 5.
# 

# ---
# ## Submission Checklist
# 
# Before submitting, verify:
# 
# - [ ] All required code cells run without errors
# - [ ] Hour 25-28 tasks are completed
# - [ ] Boundary conditions are handled correctly
# - [ ] `while` loops terminate correctly and use sentinels safely
# - [ ] `for` + `range()` outputs are correct (no off-by-one)
# - [ ] Counter/accumulator/min/max outputs are deterministic
# - [ ] Reflection questions are answered
# 
# ### Autograder Checklist
# 
# - [ ] Output lines match canonical strings in `criteria.json`
# - [ ] No extra punctuation/whitespace in graded lines
# - [ ] Deterministic output only (no randomness, no live date/time)
# - [ ] Notebook file name and location are unchanged
# 

# ---
# ## Autograder Helper - Canonical Output Contract (`day7.py`)
# 
# Your notebook implementation should be able to produce output lines consistent with the canonical contract below.
# 
# ```python
# # Canonical script for Day 7 grading by autograder (day7.py)
# def main():
#     # Hour 25
#     print("Weight 1.00kg -> Standard ($5.00)")
#     print("Weight 5.00kg -> Priority ($8.00)")
#     print("Weight 10.00kg -> Priority ($8.00)")
#     print("Weight 10.01kg -> Heavy ($12.00)")
#     print("Boundary check: ordering avoids overlap")
# 
#     # Hour 26
#     print("Attempt 1: wrong password")
#     print("Attempt 2: wrong password")
#     print("Attempt 3: correct password")
#     print("Login status: success")
#     print("Sentinel stop word: q")
#     print("Accepted commands: ['start', 'help', 'status']")
# 
#     # Hour 27
#     print("Table 4 x 1 = 4")
#     print("Table 4 x 10 = 40")
#     print("range(1, 4) -> [1, 2, 3]")
#     print("range(0, 11, 2) -> [0, 2, 4, 6, 8, 10]")
#     print("Loop type used: for")
# 
#     # Hour 28
#     print("Count: 5")
#     print("Sum: 42")
#     print("Min: 3")
#     print("Max: 15")
#     print("Average: 8.40")
#     print("Pattern check: counter+accumulator+min/max")
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# ### Local validation
# 
# ```bash
# cd Basics/assignments/Basics_Day7_homework/
# python -m pip install nbconvert
# jupyter nbconvert --to script ../Basics_Day7_homework.ipynb --output day7 --output-dir .
# python day7.py
# ```
# 
# Compare printed lines to `criteria.json` exactly.
# 
# 
