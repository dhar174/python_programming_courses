#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 1 Homework
# 
# **Topics Covered:**
# - Environment setup and orientation
# - First scripts: print(), comments, and reading errors
# - Variables and basic types
# - Numbers and operators
# 
# **Instructions:**
# - Complete all exercises in order
# - Write your code in the provided cells
# - Test your code by running the cell (Shift+Enter)
# - Use modern Python practices: f-strings, type hints, clear variable names
# - Follow PEP 8 style guidelines
# - Add comments to explain your reasoning where appropriate
# 
# **Submission:**
# - Save your completed notebook
# - Ensure all cells run without errors
# - Submit according to your instructor's guidelines
# 
# ---
# 
# ### 🤖 Autograder Integration
# 
# This assignment is graded automatically by the **Global Autograder**. Please follow these rules carefully:
# 
# - **All solution code MUST be present and runnable** in this notebook.
# - The autograder converts this notebook to `day1.py` and grades it against `criteria.json`.
# - **Outputs must exactly match** the canonical strings in `criteria.json` for all graded exercises *except for the environment info in Exercise 1.1*.
#   - Example: `Addition: 22`, `Subtotal: 85.50`
#   - No extra whitespace, punctuation, or incorrect ordering.
# - **Numeric outputs** must show correct precision (e.g., 2 decimal places for money: `85.50`, not `85.5`).
# - All `print()` statements must be **deterministic** (no randomness or unseeded state). *Note: For Exercise 1.1, your name and the current date are expected to be dynamic; the autograder only checks for the labels (`Student:`, `Date:`).*
# - The notebook must **NOT** read or write files outside the assignment directory.
# - **Run all cells** and ensure no errors before submission.
# - **Do not rename** this notebook file, move it to a different directory, or alter the config files (`criteria.json`, `setup.json`). Doing so will break the autograder workflow.
# 
# A helper cell at the end of this notebook provides a canonical script (`day1.py`) showing the exact expected outputs for each graded section. Use it to preview and debug before submission.

# ---
# ## Part 1: Environment Check and First Scripts (15 points)
# 
# ### Exercise 1.1: System Information (5 points)
# 
# Write a script that prints:
# - Your name
# - Today's date
# - Your Python version
# 
# Use the `sys` module to get the Python version programmatically.
# 
# **Example output:**
# ```
# Student: Jane Doe
# Date: 2025-01-15
# Python Version: 3.11.5
# ```

# In[ ]:


# Your code here
import sys
from datetime import date

# TODO: Define variables for your name and today's date
# TODO: Print the information in a clear format


# ### Exercise 1.2: Multi-line Output with Comments (5 points)
# 
# Create a script that prints a course welcome banner with:
# - A title line
# - A welcome message
# - A motivational quote about learning
# - A separator line
# 
# Include a comment at the top explaining what the script does.

# In[ ]:


# Your code here
# TODO: Add a comment describing this script
# TODO: Print a multi-line welcome banner


# ### Exercise 1.3: Debugging Practice (5 points)
# 
# The code below has **three syntax errors**. 
# 
# 1. First, run the cell to see the error message
# 2. Read the error carefully
# 3. Fix each error one at a time
# 4. Add a comment above each fix explaining what was wrong
# 
# **Buggy code:**
# ```python
# print("Welcome to Python Basics)
# message = 'Let's learn Python'
# print message
# print("Ready to code!")
# ```

# In[ ]:


# Your fixed code here
# TODO: Fix the three errors and add explanatory comments


# ---
# ## Part 2: Variables and Basic Types (25 points)
# 
# ### Exercise 2.1: Type Exploration (8 points)
# 
# Create variables of different types and explore them:
# 
# 1. Create these variables:
#    - `student_name`: your name (string)
#    - `age`: your age (integer)
#    - `gpa`: a GPA value (float)
#    - `is_enrolled`: enrollment status (boolean)
#    - `favorite_number`: any number you like
# 
# 2. Print each variable with its type using `type()`
# 3. Use an f-string to create a formatted sentence: "My name is {name}, I am {age} years old."

# In[ ]:


# Your code here
# TODO: Create the five variables

# TODO: Print each variable and its type

# TODO: Print the formatted sentence using an f-string


# ### Exercise 2.2: Variable Reassignment (8 points)
# 
# Demonstrate understanding of variable reassignment:
# 
# 1. Create a variable `counter` with value 0
# 2. Print its value and type
# 3. Increment it by 5
# 4. Print the new value
# 5. Reassign it to a string "done"
# 6. Print the value and type again
# 7. Explain in a comment: Is this good practice? Why or why not?

# In[ ]:


# Your code here
# TODO: Create counter variable and perform the operations

# TODO: Add your explanation as a comment
# Explanation: 


# ### Exercise 2.3: Student Profile Card (9 points)
# 
# Create a complete student profile using variables:
# 
# Required information:
# - Full name (first and last)
# - Student ID (integer)
# - Email address
# - Major
# - Credits completed (integer)
# - Current GPA (float)
# - Is a full-time student (boolean)
# 
# Print a nicely formatted profile card using f-strings. Make it look professional!

# In[ ]:


# Your code here
# TODO: Define all required variables with appropriate types

# TODO: Print a formatted profile card
# Example format:
# ================================
# STUDENT PROFILE
# ================================
# Name: ...
# etc.


# ---
# ## Part 3: Numbers and Operators (30 points)
# 
# ### Exercise 3.1: Basic Arithmetic (8 points)
# 
# Given two numbers, perform and print the results of:
# - Addition
# - Subtraction
# - Multiplication
# - Division (float result)
# - Floor division (integer result)
# - Modulus (remainder)
# - Exponentiation
# 
# Use `num1 = 17` and `num2 = 5` for testing.

# In[ ]:


# Your code here
num1: int = 17
num2: int = 5

# TODO: Perform all arithmetic operations and print results with labels


# ### Exercise 3.2: Order of Operations (7 points)
# 
# Calculate the following expressions. For each:
# 1. First, predict the result (write as a comment)
# 2. Then calculate and print the actual result
# 3. Compare and note if your prediction was correct
# 
# Expressions:
# - `5 + 3 * 2`
# - `(5 + 3) * 2`
# - `10 / 2 * 5`
# - `10 / (2 * 5)`
# - `2 ** 3 ** 2`

# In[ ]:


# Your code here
# TODO: For each expression, write your prediction, then calculate and print

# Expression 1: 5 + 3 * 2
# My prediction: 
print(f"Result: {5 + 3 * 2}")

# Continue for all expressions...


# ### Exercise 3.3: Restaurant Bill Calculator (15 points)
# 
# Create a complete restaurant bill calculator that:
# 
# 1. Starts with these variables:
#    - `subtotal`: the bill amount before tax/tip (use 85.50)
#    - `tax_rate`: sales tax percentage (use 8.5 for 8.5%)
#    - `tip_percent`: tip percentage (use 18 for 18%)
#    - `num_people`: number of people splitting the bill (use 4)
# 
# 2. Calculate:
#    - Tax amount
#    - Tip amount (on subtotal only)
#    - Total bill (subtotal + tax + tip)
#    - Amount per person
# 
# 3. Print a detailed receipt showing:
#    - Subtotal
#    - Tax (with rate)
#    - Tip (with percentage)
#    - Total
#    - Per person amount
# 
# 4. Format all monetary amounts to 2 decimal places
# 
# **Hint:** To convert percentage to decimal, divide by 100

# In[ ]:


# Your code here
# TODO: Define the input variables with type hints
subtotal: float = 85.50
tax_rate: float = 8.5  # percentage
tip_percent: float = 18.0  # percentage
num_people: int = 4

# TODO: Calculate tax, tip, total, and per-person amount

# TODO: Print a formatted receipt


# ---
# ## Part 4: Integration Challenge (30 points)
# 
# ### Exercise 4.1: Unit Converter (30 points)
# 
# Create a comprehensive unit converter that converts:
# - Temperature: Celsius to Fahrenheit and vice versa
# - Distance: Kilometers to miles
# - Weight: Kilograms to pounds
# 
# **Requirements:**
# 
# 1. Use these conversion formulas:
#    - Fahrenheit = (Celsius × 9/5) + 32
#    - Celsius = (Fahrenheit - 32) × 5/9
#    - Miles = Kilometers × 0.621371
#    - Pounds = Kilograms × 2.20462
# 
# 2. Start with these test values:
#    - Temperature: 25°C and 77°F
#    - Distance: 10 km
#    - Weight: 70 kg
# 
# 3. For each conversion:
#    - Store the original value with a descriptive variable name
#    - Perform the calculation
#    - Store the result in a new variable
#    - Print both original and converted values with units
#    - Format decimal values to 2 places
# 
# 4. Print a clear, organized output showing all conversions
# 
# 5. Use type hints for all variables
# 
# 6. Include comments explaining each conversion formula
# 
# **Bonus (+5 points):** Add conversions in both directions for all units

# In[ ]:


# Your code here
# TODO: Define all test values with type hints

# Temperature conversions
# TODO: Convert 25°C to Fahrenheit

# TODO: Convert 77°F to Celsius

# Distance conversion
# TODO: Convert 10 km to miles

# Weight conversion
# TODO: Convert 70 kg to pounds

# TODO: Print all results in a clear, organized format


# ---
# ## Reflection Questions (10 points)
# 
# Answer these questions in the markdown cell below:
# 
# 1. What's the difference between `=` and `==` in Python?
# 
# 2. Why do we use f-strings instead of string concatenation with `+`?
# 
# 3. When would you use `//` (floor division) instead of `/` (regular division)?
# 
# 4. What happens if you try to use a variable before assigning it a value?
# 
# 5. Why is it important to use descriptive variable names like `student_name` instead of `sn` or `x`?

# ### Your Answers:
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
# - [ ] All code cells run without errors
# - [ ] All exercises are complete
# - [ ] Code follows PEP 8 style guidelines
# - [ ] Variables have descriptive names
# - [ ] F-strings are used for formatting
# - [ ] Type hints are included where requested
# - [ ] Comments explain your reasoning
# - [ ] Reflection questions are answered
# - [ ] Output is clear and well-formatted
# 
# **Total Points: 115 (110 base + 5 bonus possible)**
# 
# Great work on completing Day 1! 🎉
# 
# ### Autograder Checklist
# 
# - [ ] Outputs match canonical strings in `criteria.json` exactly
# - [ ] Numeric values use correct precision (2 decimal places for currency)
# - [ ] No extra whitespace or punctuation in output lines
# - [ ] All outputs are deterministic (no randomness, no live date/time)
# - [ ] Notebook has not been renamed or moved from its original location

# ---
# ## 🤖 Autograder Helper — Canonical Output Script
# 
# The script below shows the **exact expected outputs** that the autograder checks.
# Your notebook code in the exercises above must produce output lines that match these canonical strings exactly (same labels, same values, same formatting).
# 
# ```python
# # Canonical script for Day 1 grading by autograder (day1.py)
# def main():
#     print("Student: Jane Doe")
#     print("Date: 2026-02-11")
#     print("Python Version: 3.11.5")
#     print("Addition: 22")
#     print("Subtraction: 12")
#     print("Multiplication: 85")
#     print("Division: 3.4")
#     print("Floor division: 3")
#     print("Modulus: 2")
#     print("Exponentiation: 1419857")
#     print("Subtotal: 85.50")
#     print("Tax (8.5%): 7.27")
#     print("Tip (18.0%): 15.39")
#     print("Total: 108.16")
#     print("Per person: 27.04")
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# ### Local testing steps
# 
# ```bash
# python -m pip install nbconvert
# jupyter nbconvert --to script Basics_Day1_homework.ipynb --output day1.py
# python day1.py
# ```
# 
# Compare the output to the canonical strings in `criteria.json`.
