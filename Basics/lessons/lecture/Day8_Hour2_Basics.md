# Day 8, Hour 2: Input Validation (Course Hour 30)
**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 30 – Input validation (Basics approach)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. The focus of this hour is on using simple programmatic checks (like `if` statements and `.isdigit()`) inside loops to prevent a program from crashing when converting input types. Keep the scope limited to these basic guards; avoid teaching `try/except` in depth during this hour, as it will be covered fully in a later session (Day 11).

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Identify why gathering input directly into a type conversion (like `int(input())`) is dangerous.
2. Use the `.isdigit()` string method to verify if a string contains only numbers.
3. Write a `while` loop that continuously reprompts a user until they provide valid input.
4. Explain the limitations of `.isdigit()` when dealing with negative numbers or decimals."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: The danger of unquestioned input
- **0:05–0:15** Concept: The `.isdigit()` string method
- **0:15–0:25** Concept: Building a safe input loop
- **0:25–0:35** Live demo: The Safe Number function
- **0:35–0:40** Concept: Limitations of `.isdigit()`
- **0:40–0:55** Guided lab: Safe Number Entry
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour30_validation_demo.py` ready for live coding.
- Open another empty file named `hour30_validation_lab.py` to serve as a starter for the lab portion.
- Remember to strictly enforce the "Basic validation" constraint (no `try...except ValueError` yet).

**Say:** "Please have your editor open and an empty file ready. We are transitioning from just making our programs work, to making them bulletproof."

---

## 3) Opening Script: The Danger of Unquestioned Input (~5 minutes)

### 3.1 The Crash

**Say:**
"In our previous programs, we often wrote lines like `age = int(input('Enter your age: '))`. It works perfectly if the user cooperates.

But what happens if the user types 'twenty', or simply hits enter by accident? Python attempts to convert 'twenty' into an integer, fails, and the entire program crashes with a `ValueError`. 

If you are building a menu loop like we just did, and someone makes a typo, the program dies completely. All their memory and state are lost.

We must never trust user input. Today, we are going to learn how to validate input *before* we attempt to convert it, ensuring our program survives typos and mistakes."

---

## 4) Concept: The `.isdigit()` method

### 4.1 Checking strings before conversion

**Say:**
"Strings in Python come with several built-in methods. One of the most useful for basic validation is `.isdigit()`. It asks a simple question: 'Does this string consist entirely of numbers?'"

**Type to demonstrate in the REPL or script:**

```python
# hour30_validation_demo.py

print("42".isdigit())        # True
print("hello".isdigit())     # False
print("".isdigit())          # False (empty string)
print(" 42 ".isdigit())      # False (contains spaces!)
```

**Run it.**

**Say:**
"Notice that `.isdigit()` returns `True` only if every single character is a digit from 0 to 9. Even an invisible space causes it to return `False`.

This gives us a very powerful tool. If we check the string with `.isdigit()` first, and it returns `True`, we know with 100% certainty that calling `int()` on it will succeed and will not crash our program."

---

## 5) Concept: Building a Safe Input Loop

### 5.1 The Reprompt Pattern

**Say:**
"If the user gives us bad input, we don't just want to print a warning and exit. We want to ask them again. We do this using a `while` loop, very similar to our menu loop."

**Type and narrate:**

```python
# hour30_validation_demo.py

# A flawed approach (one-time check):
user_input = input("Enter a positive number: ")

if user_input.isdigit():
    num = int(user_input)
    print(f"Thank you! Valid number: {num}")
else:
    print("That is not a number. Try running the program again.")
```

**Say:**
"This is better than crashing, but the user has to restart the entire program to try again. Let's fix this so it keeps asking until they get it right."

**Type and narrate the improvement:**

```python
while True:
    user_input = input("Enter a positive number: ")
    
    if user_input.isdigit():
        num = int(user_input)
        print(f"Thank you! Valid number: {num}")
        break  # We only break when we succeed!
    else:
        print("Error: Please enter numbers only. Let's try again.")
```

**Run it.** Provide text, provide an empty string, provide a string with a space, and finally provide a valid number.

**Say:**
"The structure here is highly reliable:
1. We establish a `while True` loop.
2. We get the input as a raw string. We do NOT call `int()` yet.
3. We check the condition. If it passes, we convert it, do our work, and `break` out of the loop.
4. If it fails, we fall into the `else`, print an error, and the loop naturally restarts."

---

## 6) Live Demo: The Safe Number function

### 6.1 Creating a Reusable Validator

**Say:**
"Writing that `while` loop every time we need a number gets tedious. Let's package this logic into a simple reusable block that we can call on demand. While we haven't formally studied functions in great depth yet, I want to preview this because it is how validation is almost always handled."

**Type and narrate:**

```python
# hour30_validation_demo.py

def get_safe_integer(prompt_message):
    """Asks the user for input until a valid positive integer is provided."""
    while True:
        # We use stripping to be forgiving of accidental spaces
        user_input = input(prompt_message).strip()
        
        if user_input.isdigit():
            # It's safe to convert
            return int(user_input)
        else:
            print("Error: Invalid entry. Must be a whole positive number.")

# Now we can use it perfectly in our main program
print("Welcome to the tiny calculator!")
first_num = get_safe_integer("Enter the first number: ")
second_num = get_safe_integer("Enter the second number: ")

total = first_num + second_num
print(f"The total is: {total}")
```

**Run it.** Intentionally type bad data for the first number, then bad data for the second number.

**Say:**
"By passing a custom prompt string, we can use the exact same loop logic for different inputs. Notice I also added `.strip()` to the input. We want to be strict, but not punishing. If a user accidentally hits the spacebar before typing '42', `.strip()` cleans it up so `.isdigit()` doesn't fail them on a technicality."

---

## 7) Concept: Limitations of `.isdigit()`

### 7.1 What `.isdigit()` misses

**Say:**
"Before you go out and use `.isdigit()` for everything, you need to understand its limitations. What if the user wants to enter the number negative five?"

**Type to demonstrate:**

```python
print("-5".isdigit())
```

**Run it. Output is `False`.**

**Say:**
"It returned `False`. Why? Because the negative sign (`-`) is not a digit from 0 to 9. 
What about three point fourteen?"

**Type to demonstrate:**

```python
print("3.14".isdigit())
```

**Run it. Output is `False`.**

**Say:**
"It returned `False` because the decimal point (`.`) is not a digit from 0 to 9.

Therefore, this Basic approach with `.isdigit()` is fantastic for getting menus choices (1, 2, 3), looking up by ID, catching ages, or requesting positive counts. However, it cannot natively handle negative integers or floats. Later in the course, we will learn exception handling (`try/except`) which solves this completely. For now, we will work within these boundaries."

---

## 8) Hands-on Lab: Safe Number Entry

### 8.1 Lab overview

**Say:**
"Now you are going to practice this pattern. You have 15 minutes."

### 8.2 Lab specification

**Display or read aloud:**

---

**Lab: Safe Number Entry**

**Task:**
1. Write a script that asks the user to input their birth year.
2. Use a `while` loop and `.isdigit()` to prevent the program from crashing if they type letters.
3. If the input is invalid, show a helpful error message and re-prompt.
4. Once valid input is provided, convert it to an integer, calculate their approximate age (assume the current year), and print it.
5. Exit the loop.

**Expected Loop Interaction:**
```
Enter your birth year: nineteen ninety
Error: Please enter a valid number containing only digits.
Enter your birth year: 
Error: Please enter a valid number containing only digits.
Enter your birth year: 1990
You are approximately 34 years old!
```

**Extra Challenge (Optional):** Can you extend your validation to explicitly reject years that don't make sense (e.g., years in the future, or years less than 1900)?

---

Circulate the room. Look specifically for:
- Learners calling `int()` before validating with `.isdigit()`.
- Missing `break` statements causing valid entries to loop forever.
- Not saving the result of `int()` into a variable.

### 8.3 Walkthrough solution

After working time, write out a brief solution:

```python
# hour30_validation_lab.py

current_year = 2024

while True:
    year_str = input("Enter your birth year (e.g., 1990): ").strip()
    
    if year_str.isdigit():
        year_int = int(year_str)
        
        # Optional challenge: logical bounds checking
        if year_int < 1900 or year_int > current_year:
            print(f"Error: {year_int} doesn't seem like a valid birth year. Try again.")
        else:
            age = current_year - year_int
            print(f"You are approximately {age} years old!")
            break  # Success! Get out of the loop.
    else:
        print("Error: Please enter a valid number containing only digits.")
```

**Say:**
"Notice how we stack the validation. First we check if it is safe to convert (`.isdigit()`). Once it is safe to convert, we convert it. Then, we check the logical bounds to make sure the data actually makes sense. Only when all checks pass do we hit that glorious `break` statement."

---

## 9) Recap and Exit Ticket

### 9.1 Summary
**Say:**
"Today we built defensive loops. By using string methods like `.isdigit()` and `.strip()` combined with a `while True` loop, we protect our standard `int()` conversion from crashing the entire application upon receiving a typo."

### 9.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: What is one major limitation of relying exclusively on `.isdigit()` to validate a number?"

**Expected answer:** Let them respond. "It does not recognize negative signs or decimal points, so it only works for zero and positive whole numbers."

**Say:**
"Exactly right. In our next hour, we are going to combine this input validation with our menu routing to build a fully robust, in-memory Contact Manager CLI."
