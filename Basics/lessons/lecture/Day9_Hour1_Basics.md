# Day 9, Hour 1: Functions: def, parameters, return (Course Hour 33)
**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 33 – Functions: def, parameters, return  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Emphasize why we need functions (code reuse and clarity), how we pass data into them, and crucially, how we get data back out using `return`. Differentiate strongly between `return` and `print()`.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Write simple functions using the `def` keyword.
2. Pass data into functions using parameters.
3. Use `return` to send data back from a function.
4. Explain the difference between returning a value and printing a value."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Why functions?
- **0:05–0:15** Core concept: Defining a function, parameters, and arguments
- **0:15–0:25** Core concept: Return vs print
- **0:25–0:35** Live demo: Refactoring a calculator
- **0:35–0:55** Guided lab: Refactor Contact Manager
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour33_functions_demo.py` ready for live coding.
- Keep the `contact_manager` code handy from previous sessions to use as a base for the lab.
- **Say:** "Please open your editors and create a new file called `functions_practice.py`. You will want to type along as we introduce the most important structure for organizing our code."

---

## 3) Opening Script: Why Functions? (~5 minutes)

**Say:**
"Think back to the programs we've built so far. We wrote menus, calculators, and trackers. As our programs grew, you might have found yourself copying and pasting similar blocks of code. For example, validating an input, or formatting a string to print it nicely multiple times.

Copying and pasting code is a shortcut that quickly becomes a trap. If you find a bug in that copied code, you have to go fix it in five different places.

Instead of repeating ourselves, we can group a block of code, give it a name, and run it whenever we want. This is called a **function**. A function is a reusable, self-contained block of code that does one specific thing. 

You've already been using functions—like `print()`, `input()`, and `len()`. Those are built into Python. Today, you learn how to write your own."

---

## 4) Concept: `def`, Parameters, and Arguments

### 4.1 Defining a basic function

**Say:**
"To create our own function, we use the `def` keyword, which stands for define."

**Type and narrate:**

```python
# hour33_functions_demo.py

def say_hello():
    print("Hello there!")

# Nothing happens until we call it!
say_hello()
say_hello()
```

**Say:**
"Notice the colon at the end of the `def` line, and notice that the body is indented. Just like `if` statements and loops, indentation defines what is *inside* the function.

Also, notice that just defining the function doesn't run the code. We have to **call** it by using its name followed by parentheses: `say_hello()`."

### 4.2 Passing data in: Parameters

**Say:**
"A function that says exactly the same thing every time is okay, but functions become powerful when we can alter their behavior by passing data into them. We do this using variables called parameters."

**Type and narrate:**

```python
def greet_user(name):
    print(f"Welcome to the system, {name}!")

greet_user("Alice")
greet_user("Bob")
```

**Say:**
"Here, `name` is a **parameter**. It acts like a placeholder or a variable that only exists inside the function. When we call the function and pass in 'Alice', 'Alice' is the **argument** that fills that placeholder."

---

## 5) Concept: Return vs Print

**Say:**
"So far, our functions have used `print()`. This is fine for displaying things to the user. However, what if we want the function to compute a value that we can use later in our code? 

If a function just prints the answer, the rest of the program can't 'see' or use that answer. To hand data back to the main program, we use the `return` keyword."

**Type and narrate:**

```python
def multiply(a, b):
    result = a * b
    return result

# Calling the function and saving the output
answer = multiply(5, 4)
print(f"The answer is {answer}")

# Using the result in further math
bigger_answer = answer + 10
print(f"The bigger answer is {bigger_answer}")
```

**Say:**
"When Python hits a `return` statement, two things happen immediately:
1. The function immediately stops running.
2. It spits out the value exactly where the function was called.

**Crucial difference:** `print()` shows data to the *human*. `return` gives data to the *program*. If you need to use the result later, you MUST `return` it."

---

## 6) Live Demo: Refactor a Calculator

**Say:**
"Let's look at how refactoring—rewriting code to be cleaner—works using functions. We will take a simple calculator script and break it down into functional units, making it much easier to test."

**Type and narrate:**

```python
# A simple calculator program structured with functions

# 1. Define our math operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# 2. Main program loop
print("--- My Calculator ---")
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")
    
    choice = input("> ")
    
    if choice == '3':
        break
        
    if choice in ['1', '2']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        
        if choice == '1':
            res = add(num1, num2)
            print(f"Result: {res}")
        elif choice == '2':
            res = subtract(num1, num2)
            print(f"Result: {res}")
```

**Run it and demonstrate.**

**Say:**
"Now our math logic is separated from our menu logic. If we want to test our `add` function independently, we can just write `print(add(10, 5))` at the top of the file before the menu even runs. This modular approach is how professional software is built."

---

## 7) Hands-on Lab: Refactor Contact Manager

### 7.1 Lab overview

**Say:**
"Now it's your turn. We are going to look back at the contact managers we've built using menu loops, and extract the logic into functions."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Refactor Contact Manager**

**Task:**
1. Start with a simple in-memory contact manager (a menu loop that adds, lists, and searches a list of names).
2. Extract the logic for your actions into three separate functions:
   - `add_contact(contact_list, name)`: takes the list and the new name as parameters, and appends the name to the list.
   - `list_contacts(contact_list)`: takes the list as a parameter and prints all the contacts.
   - `search_contact(contact_list, query)`: takes the list and the search query as parameters. **Return** the result (e.g., return True if found, False if not) rather than printing inside the function.
3. In your main `while` loop, call these functions when the user makes a choice.

---

**Instructor Note for Circulation:**
Look for learners trying to use the global list inside the function without passing it as a parameter. Encourage them to explicitly define the parameter `contact_list` and pass `contacts` when they call it. Also, verify that `search_contact` actually uses the `return` keyword and prints the message back in the `elif` routing block.

### 7.3 Walkthrough solution

**After 20 minutes, show a brief solution:**

```python
def add_contact(contact_list, name):
    contact_list.append(name)
    # Mutating the list in place, no return strictly needed

def list_contacts(contact_list):
    print("\n--- Contacts ---")
    for c in contact_list:
        print(f" - {c}")

def search_contact(contact_list, query):
    if query in contact_list:
        return True
    return False

# Main Program
directory = []

while True:
    print("\n[1] Add [2] List [3] Search [4] Quit")
    choice = input("> ")
    
    if choice == '1':
        new_name = input("Name: ")
        add_contact(directory, new_name)
    elif choice == '2':
        list_contacts(directory)
    elif choice == '3':
        q = input("Search for: ")
        # Using the returned boolean value
        found = search_contact(directory, q)
        if found:
            print(f"{q} is in the directory!")
        else:
            print("Not found.")
    elif choice == '4':
        break
```

**Say:**
"Notice how much cleaner the menu loop is? The `while True` loop is acting like the manager, directing traffic, while the functions do the actual heavy lifting. This makes code incredibly readable."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"We've just introduced the `def` keyword. You learned how to define a function, how to pass data in using parameters, and how to get data back using `return`. We separated the 'printing' for humans from 'returning' for the program."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: Give me an example of a situation where a function absolutely MUST use `return` instead of `print()`?"

**Expected answer:** Let them answer. "Anytime the result needs to be used later in the program—like doing a calculation, converting a string, checking if a user exists—if we need that answer to inform a later `if` statement or another calculation, it must be returned."
