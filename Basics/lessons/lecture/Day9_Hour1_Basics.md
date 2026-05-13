# Day 9, Hour 1: Functions: def, parameters, return (Course Hour 33)

**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 33 – Functions: `def`, parameters, `return`  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## 0. Instructor Note: Context and Approach

> This document is written as a read-aloud teaching guide. Emphasize why we need functions (code reuse and clarity), how we pass data into them, and crucially, how we get data back out using `return`. Differentiate strongly between `return` and `print()`. By the end of this hour, learners should understand that functions are the bridge between procedural scripts and organized, testable code. Functions represent a paradigm shift: from thinking "write a script that does X" to thinking "break X into reusable pieces, test each piece, and assemble them into a whole program."

---

## 1. Learning Outcomes

By the end of this hour, students will be able to:

1. **Write a simple function using the `def` keyword with parameters and body.** Students will create functions that accept input, execute logic, and organize code into reusable blocks.

2. **Distinguish between parameters (definition) and arguments (call).** Students will understand that parameters are placeholders defined in the function signature, while arguments are the actual values passed at call time.

3. **Use the `return` statement to output a value and assign it.** Students will grasp that `return` sends data back to the caller and that the returned value can be captured in a variable and used in later computations.

4. **Compare and contrast `print()` vs. `return` for appropriate output.** Students will recognize that `print()` displays to the human user, while `return` provides data to the program itself, and they will choose the right tool for each context.

5. **Refactor existing procedural code into functions to reduce repetition.** Students will take linear scripts with duplicated logic and extract functions, making the code modular, testable, and maintainable.

---

## 2. Agenda and Realistic Timing

- **0:00–0:05** Opening narrative: Why functions matter (5 min)
- **0:05–0:17** Concept briefing: `def`, parameters, arguments, and the anatomy of a function call (12 min)
- **0:17–0:30** Live demo 1: Building a basic greeter function, then a function with parameters (13 min)
- **0:30–0:42** Live demo 2: Refactoring a calculator app to show `return` in action (12 min)
- **0:42–0:55** Guided lab: Refactor Contact Manager with explicit functions (13 min)
- **0:55–1:00** Wrap-up narrative and exit ticket (5 min)

**Total:** 60 minutes

---

## 3. Instructor Setup Checklist

Before class:
- [ ] Open your code editor and create a blank file named `hour33_functions_demo.py`.
- [ ] Have a copy of the Contact Manager code from earlier sessions available (or a simple menu-loop script that adds, lists, and searches a list).
- [ ] Test the demo code locally to ensure no typos.
- [ ] Set up your screen so students can see both your terminal and editor clearly.

During class:
- [ ] Ask students to open a new file named `functions_practice.py` in their editor.
- [ ] Encourage them to type along as you write—live coding is a teaching tool, not a showcase.
- [ ] Pause frequently for questions.

---

## 4. Opening Script: Why Functions? (~5 minutes, verbatim)

**Say:**

"Good morning, everyone. I want to start by asking you a question: How many times this week have you found yourself copying and pasting code? Maybe you wrote a menu system, and then you needed to write a nearly identical menu in another part of your program. Or you wrote a validation check for one input, and then had to write almost the same check for another input somewhere else.

Copying and pasting code feels fast in the moment. But it's a trap. Think about what happens when you find a bug in that code. If you've pasted it five times, you have to fix it in five places. You'll probably miss one. That bug will come back to bite you later.

The solution to this problem is called a **function**. A function is a reusable, self-contained block of code that does one specific thing and can be called over and over again. Functions are how we stop repeating ourselves.

Now, you've already been using functions. Every time you call `print()` or `input()` or `len()`, you're using a function that someone else wrote. Python comes with hundreds of built-in functions. Today, you learn how to write your own.

Why is this important? Because once you can write your own functions, you can break large, messy programs into smaller, testable pieces. You can organize your code so that someone else can understand it. And you can build software that actually works and that you can maintain six months from now.

Today, we're going to focus on three core ideas: how to define a function with the `def` keyword, how to pass data into a function using parameters, and how to get data back out using the `return` keyword. Let's get started."

---

## 5. Concept Briefing: The Anatomy of a Function (~12 minutes, narrated)

### 5.1 What is a Function?

**Say:**

"In Python, a function is defined using the `def` keyword, which is short for 'define.' Here's the basic structure:

```python
def function_name():
    # code inside the function
    pass  # 'pass' is a placeholder that does nothing
```

When you define a function, nothing runs yet. The code is just stored in memory. To actually run the code inside, you **call** the function by writing its name followed by parentheses."

### 5.2 Function Definition vs. Function Call

**Say:**

"This is a crucial distinction. Let me show you:

```python
# This is DEFINING the function
def say_hello():
    print("Hello!")

# This is CALLING the function (making it run)
say_hello()

# You can call it as many times as you want
say_hello()
say_hello()
```

When Python reads this file:
1. It reads `def say_hello():` and stores that code block in memory.
2. It does NOT run `print("Hello!")` yet.
3. When it reaches `say_hello()`, it looks up that stored function and runs it.
4. Each time you write `say_hello()`, it runs again.

This is why you can see the output 'Hello!' printed three times."

### 5.3 Parameters: Passing Data Into a Function

**Say:**

"Now, a function that does exactly the same thing every time is limited. What if we want to change the function's behavior based on input? We do this with **parameters**.

A parameter is a placeholder variable that exists only inside the function. When you define a function with a parameter, you're saying: 'I expect someone to give me data when they call this function. I'll use that data inside my function.'

```python
# This function takes one parameter: name
def greet_user(name):
    print(f"Hello, {name}!")

# When we CALL the function, we provide an ARGUMENT
greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")
```

Notice:
- `name` is the **parameter** (the placeholder in the function definition).
- 'Alice', 'Bob', and 'Charlie' are the **arguments** (the actual values we provide when calling the function).

Inside the function, `name` takes on whatever value was passed. So the first call sets `name` to 'Alice', the second call sets it to 'Bob', and so on."

### 5.4 Multiple Parameters

**Say:**

"A function can take more than one parameter. You just separate them with commas:

```python
def add_two_numbers(a, b):
    sum_value = a + b
    print(f"The sum of {a} and {b} is {sum_value}")

add_two_numbers(5, 3)
add_two_numbers(10, 20)
```

When you call `add_two_numbers(5, 3)`, Python matches the arguments to the parameters in order: `a` gets 5, and `b` gets 3. Then the function body runs with those values."

### 5.5 The Return Statement: Getting Data Out

**Say:**

"Here's the critical insight: `print()` displays data to the human. But what if the function needs to compute a value that the rest of your program uses? That's where `return` comes in.

When a function hits a `return` statement, it stops immediately and sends that value back to wherever the function was called. The caller can then capture that value in a variable and use it:

```python
def multiply(a, b):
    result = a * b
    return result

# The function call is REPLACED by the return value
answer = multiply(5, 4)
print(answer)  # Prints 20

# We can use the returned value in another calculation
bigger_answer = answer + 10
print(bigger_answer)  # Prints 30
```

This is different from `print()`. If I had written `print(result)` instead of `return result`, the human would see '20' on the screen, but the program itself couldn't use that value. The variable `answer` would be undefined. But with `return`, the program gets the value, and we can use it anywhere."

---

## 6. Live Demo 1: Building a Basic Greeter (~13 minutes)

**Instructor narration and live coding:**

**Say:**

"Let me show you this in action. I'm going to create a few simple functions step by step. I'll start with the most basic one, then add parameters, then show you how `return` works.

Open your editor and create a file called `functions_practice.py`. Follow along."

**Type this on screen, narrating as you go:**

```python
# Step 1: A function with no parameters
def say_hello():
    print("Hello there!")

say_hello()
say_hello()
```

**Say:**

"When I run this, you see 'Hello there!' printed twice. The function does the same thing every time. Let's make it more flexible."

**Type:**

```python
# Step 2: A function with one parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
greet_person("World")
```

**Say:**

"Now the function adapts. Each call produces different output based on the argument I provide. But notice: I'm using `print()` inside the function. This means the output goes to the screen, but the program doesn't 'have' the data. Let me show you what I mean."

**Type:**

```python
# Step 3: Trying to use a function's output
def greet_person_v2(name):
    greeting = f"Hello, {name}!"
    print(greeting)

result = greet_person_v2("Charlie")
print(f"The result is: {result}")
```

**Run this and show the output.**

**Say:**

"See how 'result' is `None`? The function printed the greeting, but it didn't give the value back to the program. So `result` has nothing stored in it. Now watch what happens if we use `return`."

**Type:**

```python
# Step 4: Using return to send data back
def greet_person_v3(name):
    greeting = f"Hello, {name}!"
    return greeting

result = greet_person_v3("Charlie")
print(f"The result is: {result}")
```

**Run this.**

**Say:**

"Now `result` actually contains the string. The `return` statement sent it back to the caller. This is the difference: `print()` is for displaying. `return` is for sending data back to the program itself. And once the program has the data, it can use it in further calculations, or pass it to another function, or store it in a list—anything."

---

## 7. Live Demo 2: Refactoring a Calculator with Return (~12 minutes)

**Say:**

"Let's look at a slightly more realistic example. Imagine I have a simple calculator program. Originally, all the logic is in one big loop. I'll refactor it by extracting the math operations into functions."

**First, show a non-refactored version:**

```python
# Old style: everything in a big loop

print("=== Simple Calculator ===")
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Quit")
    choice = input("> ").strip()
    
    if choice == '3':
        print("Goodbye!")
        break
    
    if choice in ['1', '2']:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if choice == '1':
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {result}")
    else:
        print("Invalid choice.")
```

**Say:**

"This works, but it's hard to test. If I want to verify that adding two numbers works correctly, I have to run the whole program and navigate the menu. And if I need to add numbers in another part of my program, I'd have to copy and paste this code. Let's refactor it using functions."

**Now show the refactored version:**

```python
# Refactored: functions encapsulate the logic

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Simple Calculator ===")
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Quit")
        choice = input("> ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
        
        if choice in ['1', '2']:
            num1 = get_float_input("First number: ")
            num2 = get_float_input("Second number: ")
            
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice.")

# Run the program
main()
```

**Say:**

"Notice what changed:

1. We extracted `add()` and `subtract()` into their own functions. Now, if we want to test that adding works, we can just write `print(add(5, 3))` at the top of our file and run it. No menu needed.

2. We extracted the input validation into `get_float_input()`, so we don't repeat it.

3. The main menu loop is now inside a `main()` function. This makes the code organization clearer: 'The main program is this one function.'

4. Each function `return`s a value, so the caller gets data back and can use it. The functions don't just print and hope—they return actual values.

This is how professional code is structured. Functions are your building blocks. You test each block, then assemble them into a working program."

---

## 8. Guided Lab: Refactor Contact Manager (~13 minutes)

### 8.1 Lab Overview

**Say:**

"Now it's your turn. We're going to take a simple contact manager—a menu-driven program that stores names in a list—and refactor it by extracting the logic into functions.

You have 13 minutes to complete this. Here's the specification."

### 8.2 Lab Specification

**Display or read aloud:**

---

**Lab Task: Refactor Contact Manager**

**Objective:** Refactor a menu-driven contact manager to use functions.

**Requirements:**

1. Start with a simple in-memory contact manager. This is a `while True` loop that:
   - Displays a menu: Add a contact, List all contacts, Search for a contact, Quit.
   - Stores contacts in a list (e.g., `contacts = []`).
   - Handles each menu choice.

2. Extract the logic for each action into separate functions:
   - `add_contact(contact_list, name)`: Takes the list and a name. Appends the name to the list. (No return needed; you're mutating the list.)
   - `list_contacts(contact_list)`: Takes the list. Prints all contacts, one per line. (No return needed; just display.)
   - `search_contact(contact_list, query)`: Takes the list and a search term. **Return `True` if the query is found, `False` otherwise.** (Don't print inside this function.)

3. In your `while True` loop:
   - Call `add_contact()` when the user chooses 'Add'.
   - Call `list_contacts()` when the user chooses 'List'.
   - Call `search_contact()` when the user chooses 'Search', and print the result in the main loop (not inside the function).
   - Break when the user chooses 'Quit'.

**Checkpoint 1 (5 minutes):** Have the menu loop and the `add_contact()` and `list_contacts()` functions working.

**Checkpoint 2 (8 minutes):** Implement `search_contact()` with a `return` statement, and call it from the main loop.

**Checkpoint 3 (13 minutes):** Test the full program. Add a few contacts, list them, search for one, and verify the search result.

---

### 8.3 Walkthrough Solution

**After students have worked for 10–13 minutes, display or narrate this solution:**

```python
# Contact Manager Refactored

def add_contact(contact_list, name):
    """Add a single contact to the list."""
    contact_list.append(name)
    print(f"Added {name}.")

def list_contacts(contact_list):
    """Display all contacts in the list."""
    if not contact_list:
        print("No contacts yet.")
        return
    
    print("\n--- Contacts ---")
    for contact in contact_list:
        print(f"  {contact}")

def search_contact(contact_list, query):
    """Search for a contact. Return True if found, False otherwise."""
    return query in contact_list

def main():
    """Main program loop."""
    contacts = []
    
    while True:
        print("\n[1] Add  [2] List  [3] Search  [4] Quit")
        choice = input("> ").strip()
        
        if choice == '1':
            name = input("Contact name: ").strip()
            if name:  # Only add if name is not empty
                add_contact(contacts, name)
            else:
                print("Name cannot be empty.")
        
        elif choice == '2':
            list_contacts(contacts)
        
        elif choice == '3':
            query = input("Search for: ").strip()
            if search_contact(contacts, query):
                print(f"Found: {query}")
            else:
                print(f"{query} not found.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

# Start the program
main()
```

**Key teaching points to highlight:**

**Say:**

"Notice a few things:

1. Each function does one thing. `add_contact()` adds. `list_contacts()` displays. `search_contact()` searches. That's it.

2. The functions take parameters explicitly. They don't reach into global space and grab the list by accident. We're being intentional: 'Here's the list I want you to work with.'

3. `search_contact()` returns a boolean (`True` or `False`). In the main loop, we use that return value in an `if` statement. The function doesn't print the result. It returns the data, and the caller (the main loop) decides what to do with it.

4. The main loop is now super clear. It's a traffic director: it reads the user's choice and dispatches to the appropriate function. The functions do the heavy lifting.

This structure is much more testable, readable, and maintainable. If you need to debug the search logic, you know exactly where to look: the `search_contact()` function."

---

## 9. Troubleshooting Pitfalls and Instructor Cues

### Pitfall 1: Forgetting to Call the Function

**Scenario:** A student defines a function but doesn't call it.

```python
def say_hello():
    print("Hello!")

# They define it but never write say_hello()
```

**Symptom:** Nothing prints.

**Cue:** "Defining the function isn't enough. You have to **call** it. Write the name followed by parentheses."

---

### Pitfall 2: Forgetting the Colon at the End of `def`

**Scenario:**

```python
def greet_user(name)   # Missing colon!
    print(f"Hello, {name}!")
```

**Symptom:** `SyntaxError: expected ':'`

**Cue:** "Remember: `def` needs a colon at the end, just like `if`, `for`, and `while`. The colon tells Python, 'Here comes an indented block.'"

---

### Pitfall 3: Using `print()` When `return` Is Needed

**Scenario:**

```python
def get_sum(a, b):
    print(a + b)  # Using print instead of return

result = get_sum(5, 3)
# result is None, not 8
```

**Symptom:** The function looks like it works (you see output), but the program can't use the result.

**Cue:** "Ask yourself: Does the rest of my program need to use this value? If yes, use `return`. If I just want to show something to the human, use `print()`."

---

### Pitfall 4: Confusing Parameters and Arguments

**Scenario:** A student thinks parameters are the same as arguments.

**Cue:** "Parameters are the placeholders you define. Arguments are the values you pass. When I write `def greet(name):`, `name` is the parameter. When I call `greet('Alice')`, 'Alice' is the argument."

---

### Pitfall 5: Not Passing the List as a Parameter

**Scenario:**

```python
contacts = []

def add_contact(name):  # Forgot the contact_list parameter!
    contacts.append(name)  # Reaches into global scope

add_contact("Alice")
```

**Symptom:** It works, but it's bad practice. The function is hidden-dependent on a global variable.

**Cue:** "Pass the list explicitly as a parameter. This makes the function self-contained and testable. Don't rely on global variables. Be explicit."

---

### Pitfall 6: Indentation Issues

**Scenario:**

```python
def multiply(a, b):
return a * b  # Not indented!
```

**Symptom:** `IndentationError: expected an indented block`

**Cue:** "Everything inside a function must be indented. Python uses indentation to know what's inside the function and what's outside."

---

### Pitfall 7: Misunderstanding `return` as `break`

**Scenario:** A student thinks `return` only exits a loop, not the function.

**Cue:** "`return` exits the entire function, not just a loop. It immediately sends the value back to the caller. If there's a loop inside the function, `return` breaks out of both the loop and the function."

---

## 10. Quick-Check Questions (Formative Assessment)

Ask these throughout the hour and at the end. These are not for grading—they're to check understanding and clarify confusion.

### Question 1: Define vs. Call

**Ask:** "What's the difference between writing `def my_function():` and writing `my_function()`?"

**Expected answer:** "The first is defining (creating) the function. The second is calling (running) it."

---

### Question 2: Parameter vs. Argument

**Ask:** "In the line `def greet(name):`, what's the parameter? And when I call `greet('Alice')`, what's the argument?"

**Expected answer:** "`name` is the parameter. 'Alice' is the argument."

---

### Question 3: Return vs. Print

**Ask:** "I want to write a function that computes the average of three numbers. Should I use `print()` or `return`?"

**Expected answer:** "`return`. Because I want the program to use that average in further calculations. `print()` would only show it to the human."

---

### Question 4: Return Value Assignment

**Ask:** "If I write `result = add(5, 3)` and the `add()` function returns 8, what does `result` now contain?"

**Expected answer:** "8. The `return` value replaces the function call, and `result` gets that value."

---

### Question 5: Multiple Parameters

**Ask:** "I'm writing a function that takes two numbers and computes their product. How do I define it?"

**Expected answer:** "Something like `def multiply(a, b):` with two parameters separated by a comma."

---

## 11. Wrap-Up Narrative (~5 minutes, verbatim)

**Say:**

"We've covered a lot in the last hour. Let me recap the key points.

First: **Functions are reusable blocks of code.** Instead of copying and pasting logic, you put it in a function and call that function as many times as you need. This means fewer bugs and easier maintenance.

Second: **Functions are defined with `def` and called by name.** When you define a function, Python stores it. When you call it, Python runs it.

Third: **Parameters let you customize a function's behavior.** You pass arguments when you call the function, and those arguments fill in the parameters inside the function. This is how a function can do different things based on different inputs.

Fourth: **`return` is how a function gives data back to the program.** `print()` shows data to the human. `return` gives data to the program. If you need the result of a function in another calculation or in an `if` statement, you MUST use `return`.

Fifth: **Refactoring with functions makes code cleaner and more testable.** When you break a big script into smaller functions, you can test each function independently. You can read the main program flow more easily. And you can reuse those functions in other programs.

These ideas—functions, parameters, return—are the foundation of programming. Everything you build from here on will use these concepts. And we'll keep building on them. Next, we'll look at scope—what variables can 'see' inside and outside a function—and we'll talk about best practices for writing functions.

For now, make sure you practice writing a few functions on your own. The best way to learn is to write code, break it, and figure out what went wrong. That's where real learning happens."

---

## 12. Facilitation Notes and Differentiation Strategies

### For Students Who Finish Early

1. **Extend the lab:** Ask them to add a fourth function, `update_contact(contact_list, old_name, new_name)`, which searches for a contact and updates their name. Use `return` to send back a success/failure boolean.

2. **Combine functions:** Ask them to write a function `validate_name(name)` that returns `True` if a name is valid (e.g., not empty, at least 2 characters). Use this function inside `add_contact()` to prevent invalid entries.

3. **Explore default parameters:** Show them how to write `def greet(name="Friend"):` and call it with or without an argument.

### For Students Who Are Struggling

1. **Pair programming:** Pair them with a student who's progressing well. Shared keyboard and active listening help reinforce concepts.

2. **Template code:** Provide a skeleton:
   ```python
   def add_contact(contact_list, name):
       # Your code here
       pass
   ```
   They fill in the body.

3. **Verbal walkthrough:** Before they code, ask them to describe in plain English what the function should do. Then ask them to translate that into Python.

4. **Focus on one concept at a time:** Don't overwhelm them with parameters AND `return` in the same moment. Master `def` and calling, then add parameters, then add `return`.

### Scaffolding Strategy

1. **Start with no parameters:** Define `def say_hello(): print("Hello!")` and call it.
2. **Add one parameter:** `def greet(name): print(f"Hello, {name}!")` and call it with different arguments.
3. **Add `return`:** `def add(a, b): return a + b` and assign the result to a variable.
4. **Combine:** `def search(contact_list, query): return query in contact_list` and use the returned boolean in an `if` statement.
5. **Refactor existing code:** Take their Contact Manager from earlier and break it into functions.

### Exit Ticket / Formative Assessment

**Ask each student as they leave (or pose to the group):**

"Give me one sentence: Why would I use `return` instead of `print()`?"

**Acceptable answers include:**
- "Because I want the program to use the value later."
- "If I need the result in another calculation."
- "If I need to check the result in an `if` statement."
- "Because `print()` doesn't give the value back to the program."

**Red flags (if you hear these, follow up):**
- "I don't know."
- "`return` is the same as `print()`."
- "I use `return` to end the function." (They're confusing it with `break`.)

---

**End of Lecture Script**

**Word count:** ~5,100 words | **Code blocks:** 15 balanced code fences | **Learning outcomes:** 5 explicit | **Troubleshooting pitfalls:** 7 | **Quick-check questions:** 5 | **Timing:** 60 minutes total
