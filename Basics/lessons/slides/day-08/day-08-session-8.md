# Basics Day 8 — Session 8 (Hours 29–32)
Python Programming (Basic) • Menu Loops, Input Validation, and CLI Mini-Projects

## Session 8 Overview
- Hour 29: Menu loops - building simple CLI menus
- Hour 30: Input validation - basic guards and re-prompting
- Hour 31: Mini-project - CLI Contact Manager (in memory)
- Hour 32: Checkpoint 4 - control flow assessment with a CLI To-Do Manager

---

## Session Goal
- Turn one-run scripts into interactive command-line programs
- Show a menu, accept a choice, and repeat until the user quits
- Keep data in memory during the run of the program
- Validate basic input before converting or using it

---

## Scope Guardrail

### Stay in Basics Scope
- Use `while` loops for repeated prompts
- Use `if/elif/else` to route menu choices
- Use lists or dictionaries for in-memory state
- Use simple cleanup like `.strip()` and `.lower()`
- Use basic validation checks such as `.isdigit()` and non-empty strings

### Not Yet
- File saving or loading
- JSON, databases, or web APIs
- Classes or object-oriented design
- Advanced exception-handling patterns
- List comprehensions or generator expressions
- Multi-file application architecture

> Instructor note: Keep the message simple - we are building small, reliable CLI programs, not production applications.

---

# Hour 29: Menu Loops (CLI Pattern)

## Learning Outcomes
- Build a menu-driven `while` loop
- Route actions with `if/elif`
- Keep shared state in memory while the loop runs
- Explain why a menu loop is useful in CLI programs

---

## Why Menu Loops Matter

### The Problem
Many beginner scripts do one job and then stop:
1. ask for input
2. do one action
3. exit

### The Menu Loop Idea
A menu loop lets the program:
- show options
- read a choice
- do the chosen action
- return to the menu
- repeat until the user quits

---

## Core Pattern: Display -> Read -> Route -> Repeat
```python
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("Do action A")
    elif choice == "2":
        print("Do action B")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

### Talk Points
- `while True` keeps the program running until `break`
- `if/elif` ensures only one menu action runs per choice
- `.strip()` removes accidental spaces around the input

---

## Shared State in Memory

### What "State" Means Here
The program needs a place to remember data while it is running.

```python
students = []

while True:
    ...
```

### Why Placement Matters
- Create the list or dictionary before the loop starts
- Update the same structure inside each action
- Do not rebuild the structure every time the menu repeats

> Instructor pacing note: Pause here and ask learners what would happen if `students = []` were moved inside the loop.

---

## Demo: Student Menu Scaffold

### Watch For
- the menu prints each time through the loop
- the list is created once, before the loop
- each branch does one clear job
- `break` stops the program cleanly

```python
students = []

while True:
    print("\nStudent Menu")
    print("1. Add student")
    print("2. List students")
    print("3. Search student")
    print("4. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        students.append(name)
        print(f"Added: {name}")

    elif choice == "2":
        if students:
            print("Students:")
            for student in students:
                print(f"- {student}")
        else:
            print("No students yet.")

    elif choice == "3":
        target = input("Search name: ").strip()
        if target in students:
            print(f"{target} found.")
        else:
            print(f"{target} not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")
```

### Expected Output
```text
Student Menu
1. Add student
2. List students
3. Search student
4. Quit
Choose an option: 1
Enter student name: Ava
Added: Ava

Student Menu
1. Add student
2. List students
3. Search student
4. Quit
Choose an option: 2
Students:
- Ava
```

---

## Lab: Upgrade Menu

### Instructions (30 minutes)
Turn a previous script into a looped menu program.

### Requirements
1. Choose a simple data set: names, books, scores, products, or guests
2. Include these actions: add, list, search, quit
3. Keep the data in memory while the program runs
4. Re-show the menu after every action until the user quits

### Suggested Build Order
1. Write the menu and quit option
2. Add the add action
3. Add the list action
4. Add the search action
5. Test all choices

---

## Lab: Completion Criteria
- Menu repeats until quit
- Each action works for at least one example
- Shared data is updated correctly
- Invalid menu choices show a helpful message

> Instructor note: If learners are behind, provide the menu scaffold and let them finish only add plus list before attempting search.

---

## Common Pitfalls - Hour 29

### Pitfall 1: Resetting Data Inside the Loop
```python
while True:
    students = []
```
Fix: create the collection before the loop.

### Pitfall 2: Forgetting to Reprint the Menu
If the menu only appears once, users lose the prompt for what to do next.

### Pitfall 3: Using Separate `if` Statements
Use `if/elif/else` so one choice triggers one branch.

---

## Optional Extensions - Hour 29
- Add an update option
- Add a delete option
- Keep the data in memory and use simple list or dict operations only

> Scope note: Do not turn this into a multi-file app or introduce functions beyond a light preview.

---

## Quick Check - Hour 29
**Exit ticket:** Why is a menu loop useful for CLI programs?

**Model answer:** It lets users do multiple actions in one run of the program instead of restarting the script after every task.

---

# Hour 30: Input Validation (Basics Approach)

## Learning Outcomes
- Use simple guards to prevent crashes
- Re-prompt when input is invalid
- Use `.isdigit()` for basic whole-number checks
- Explain one important limitation of `.isdigit()`

---

## Why Validate Input?

### The Problem
If a program assumes input is valid, it may:
- crash
- convert the wrong value
- produce confusing output

### Goal
Before converting input, do a simple check:
- is it empty?
- is it numeric?
- does it fit the expected format?

---

## Check First, Convert Second

### Risky Version
```python
age = int(input("Enter age: "))
print(age + 1)
```
If the user types `abc`, the program crashes.

### Safer Basics Pattern
```python
text = input("Enter age: ").strip()

if text.isdigit():
    age = int(text)
    print(f"Next year you will be {age + 1}.")
else:
    print("Please enter a whole number.")
```

> Teaching point: read text -> check text -> convert text.

---

## What `.isdigit()` Can and Cannot Do
```python
print("42".isdigit())
print("004".isdigit())
print("abc".isdigit())
print("4.5".isdigit())
print("-3".isdigit())
```

### Talk Points
- Good for menu numbers, counts, ages, and quantities
- Not enough for negative numbers or decimals
- Works better after `.strip()` removes extra spaces

> Scope note: Mention `try/except` exists, but keep the lesson focused on simple guards and re-prompting.

---

## Demo: Safe Whole Number Entry

### Watch For
- `.strip()` removes extra spaces
- `.isdigit()` checks before conversion
- the loop repeats on invalid input
- valid input gets used in a small calculation

```python
while True:
    text = input("How many tickets do you want? ").strip()

    if text.isdigit():
        tickets = int(text)
        total = tickets * 12
        print(f"Total cost: ${total}")
        break
    else:
        print("Invalid input. Enter a whole number like 1, 2, or 3.")
```

### Expected Output
```text
How many tickets do you want? two
Invalid input. Enter a whole number like 1, 2, or 3.
How many tickets do you want? 4
Total cost: $48
```

---

## Lab: Safe Number Entry

### Instructions (30 minutes)
Build a program that safely asks for a whole number and uses it in a small calculator.

### Requirements
1. Ask for a whole number
2. If the input is invalid, show an error and ask again
3. Once valid input is entered, use it in a calculation
4. Print the result with a clear label

### Example Ideas
- quantity times price
- ticket total
- doubled practice number
- square of a number

---

## Lab: Completion Criteria
- Program never crashes on non-numeric input
- Program accepts valid whole numbers correctly
- Program re-prompts until valid input is entered
- Program uses the validated number in a calculation

> Instructor pacing note: If the room is moving slowly, give learners the validation loop and ask them to customize only the final calculation.

---

## Common Pitfalls - Hour 30

### Pitfall 1: Converting Before Checking
```python
text = input("Enter a number: ")
number = int(text)
```
Fix: check first, then convert.

### Pitfall 2: Forgetting `.strip()`
Inputs like ` 7 ` may fail without cleanup.

### Pitfall 3: Over-trusting `.isdigit()`
`.isdigit()` does not handle negatives or decimals.

---

## Optional Extensions - Hour 30
- Extend validation to allow negative whole numbers by checking an optional leading `-`
- Use the same validation idea for menu choices like `1`, `2`, `3`

> Scope note: Keep parsing simple. Do not move into advanced validation libraries or full exception-handling lessons.

---

## Quick Check - Hour 30
**Exit ticket:** What is one limitation of `.isdigit()`?

**Model answer:** It only returns `True` for strings made entirely of digits, so values like `-3` and `4.5` do not pass.

---

# Hour 31: Mini-Project - CLI Contact Manager (In Memory)

## Learning Outcomes
- Combine loops and data structures into a working CLI program
- Build a contact manager with clear prompts and confirmations
- Choose a reasonable structure for storing contacts
- Test add, list, search, and delete features step by step

---

## Mini-Project Goal

### Build a Small but Real Program
This hour combines:
- a menu loop
- strings and input
- list or dictionary storage
- searching and deleting
- clear user feedback

### Required Features
- add contact
- list contacts
- search by name
- delete by name
- quit

---

## Choosing a Structure

### Option 1: Dictionary
```python
contacts = {
    "Ava": "555-1234",
    "Liam": "555-8888"
}
```
Good when each name should map to one phone number.

### Option 2: List of Dictionaries
```python
contacts = [
    {"name": "Ava", "phone": "555-1234"},
    {"name": "Liam", "phone": "555-8888"}
]
```
Good when you may want extra fields later.

> Teaching point: For most learners in this session, a dictionary is the simplest choice.

---

## Suggested Build Order
1. Create the menu loop
2. Add the add-contact action
3. Add the list action
4. Add the search action
5. Add the delete action
6. Test missing-name cases
7. Improve messages and formatting

---

## Demo: Add and List Contacts

### Watch For
- contacts are stored outside the loop
- names are cleaned with `.strip()`
- duplicate names overwrite in a dictionary
- an empty contact list is handled clearly

```python
contacts = {}

while True:
    print("\nContact Menu")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Saved contact for {name}.")

    elif choice == "2":
        if contacts:
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"- {name}: {phone}")
        else:
            print("No contacts saved.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
```

### Expected Output
```text
Contact Menu
1. Add contact
2. List contacts
3. Quit
Choose an option: 1
Enter contact name: Ava
Enter phone number: 555-1234
Saved contact for Ava.

Contact Menu
1. Add contact
2. List contacts
3. Quit
Choose an option: 2
Contacts:
- Ava: 555-1234
```

---

## Lab: Contact Manager (In Memory)

### Instructions (35 minutes)
Build a CLI Contact Manager that runs until the user chooses quit.

### Required Features
1. Add contact (`name`, `phone`)
2. List contacts
3. Search by name
4. Delete by name
5. Quit from the menu

### Rules
- Keep everything in memory
- Use a menu loop
- Show helpful messages for success and failure
- Handle missing names safely

### Suggested Menu
```text
1. Add contact
2. List contacts
3. Search contact
4. Delete contact
5. Quit
```

---

## Lab: Completion Criteria
- All required actions work
- Program does not crash when a name is missing
- Menu repeats until quit
- Prompts and confirmations are easy to understand
- Contact data stays available while the program runs

> Instructor note: If time is tight, require add, list, and search first. Treat delete as the extension feature for learners who finish early.

---

## Common Pitfalls - Hour 31

### Pitfall 1: Case Sensitivity
Searching for `ava` will not match `Ava` unless the program normalizes names.

### Pitfall 2: Deleting Without Checking First
```python
if name in contacts:
    del contacts[name]
else:
    print(f"{name} not found.")
```
Use a membership check before deleting.

### Pitfall 3: Deleting While Iterating
If learners choose a list-based design, search first and delete after you know the correct item.

---

## Optional Extensions - Hour 31
- Update an existing phone number
- Normalize names with `.title()` or compare with `.lower()`
- Print a formatted contact report as plain text

> Scope note: Print only. Do not save contacts to a file.

---

## Quick Check - Hour 31
**Exit ticket:** What was the hardest bug you hit in the menu loop?

**Model answer:** Accept any specific debugging answer such as resetting the dictionary inside the loop, forgetting `break`, or deleting a missing name without checking first.

---

# Hour 32: Checkpoint 4 - Control Flow Assessment

## Learning Outcomes
- Demonstrate conditionals, loops, and data structures in one coherent program
- Build a menu-driven CLI program with basic validation
- Test both normal cases and boundary cases
- Explain simple choices made for readability and robustness

---

## Checkpoint Goal

### Build: CLI To-Do Manager
Learners combine:
- menu loops
- basic validation
- list or dictionary storage
- update and delete actions
- readable program flow

### Required Features
- add task
- list tasks
- mark task complete
- delete task
- quit

---

## Checkpoint Rubric Focus
- Correctness: required features actually work
- Readability: code is clear and organized
- Required constructs: loops, conditionals, and a data structure are present
- Robustness: invalid or missing input is handled reasonably

> Basics reminder: This checkpoint rewards a clean, working basics solution - not advanced features.

---

## Suggested Data Structure Options

### Option 1: List of Dictionaries
```python
tasks = [
    {"name": "Buy milk", "done": False},
    {"name": "Email team", "done": True}
]
```

### Option 2: Dictionary of Status
```python
tasks = {
    "Buy milk": False,
    "Email team": True
}
```

### Recommendation
A list of dictionaries is often easier when learners want numbered task lists.

---

## Demo: Quick Spot-Check Strategy

### Watch For
- the task list is not reset inside the loop
- add, list, complete, and delete all update the same data
- invalid task numbers are handled safely
- empty task names are rejected

```python
tasks = [
    {"name": "Buy milk", "done": False},
    {"name": "Email team", "done": False}
]

task_number = 2

if 1 <= task_number <= len(tasks):
    tasks[task_number - 1]["done"] = True

for index, task in enumerate(tasks, start=1):
    status = "done" if task["done"] else "todo"
    print(f"{index}. [{status}] {task['name']}")
```

### Expected Output
```text
1. [todo] Buy milk
2. [done] Email team
```

---

## Lab: Checkpoint Lab 4

### Instructions (50 minutes)
Build a CLI To-Do Manager.

### Requirements
1. Program runs in a menu loop until the user chooses quit
2. User can add a task
3. User can list all tasks
4. User can mark a task complete
5. User can delete a task
6. Program uses basic input validation:
   - task name should not be empty
   - task number must be valid

### Suggested Menu
```text
1. Add task
2. List tasks
3. Mark task complete
4. Delete task
5. Quit
```

---

## Lab: Completion Criteria
- Menu loop works until quit
- Tasks persist in memory during the run
- Complete and delete actions work correctly
- Empty task names are rejected
- Invalid task numbers are handled safely
- Output is clear and easy to follow

> Instructor pacing note: If learners need support, give them the add/list scaffold first and coach mark-complete plus delete as the second pass.

---

## Common Pitfalls - Hour 32

### Pitfall 1: Reinitializing the Task List
```python
while True:
    tasks = []
```
Fix: create the task list before the loop.

### Pitfall 2: Index Errors
```python
index = task_number - 1
if 0 <= index < len(tasks):
    tasks.pop(index)
```
Convert user-friendly numbering to a safe list index.

### Pitfall 3: Empty Task Names
Reject blank input after `.strip()` before saving the task.

---

## Optional Extensions - Hour 32
- Add a filter for completed versus uncompleted tasks
- Add a confirmation message after mark-complete and delete
- Sort the display so unfinished tasks appear first

> Scope note: Keep the project in memory and in one file. No persistence layer, no classes, no advanced error handling.

---

## Quick Check - Hour 32
**Exit ticket:** What is one strategy you used to test boundary cases?

**Model answer:** Try an invalid menu choice, an empty task name, or a task number that does not exist and confirm the program stays usable.
