# Day 10, Hour 4: Checkpoint 5: Functions + modules + intro OOP (Course Hour 40)
**Python Programming Basics – Session 10**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 40 – Checkpoint 5: Functions + modules + intro OOP  
**Duration:** 60 minutes  
**Mode:** Instructor-led + checkpoint assessment  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This is a major checkpoint. The focus is entirely on structure: passing data into functions, extracting functions to an external module file (`utils.py`), and demonstrating basic OOP concepts. Keep the scope strictly to in-memory operations (no file handling yet).

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Demonstrate modular code organization by separating logic into multiple files.
2. Build an interactive CLI program utilizing loops, functions, and standard library modules.
3. Integrate at least one custom Python class to manage structured data."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Checkpoint instructions and criteria
- **0:05–0:10** Live demo: Expected behavior of the end product
- **0:10–0:50** Checkpoint Lab 5: CLI Organizer
- **0:50–1:00** Debrief, showcase, and wrap-up

---

## 2) Instructor Setup Checklist

- Ensure you have a working solution for the CLI organizer ready to run.
- Keep the grading rubric handy.
- **Say:** "This is an open-book, open-notes checkpoint. You will be building a complete script from the ground up to prove you understand functions, modules, and classes."

---

## 3) Opening Script: Checkpoint Instructions (~5 minutes)

**Say:**
"We have covered a massive amount of ground. You've learned logic, loops, data structures, functions, and today, you've learned how to harness Object-Oriented Programming and split code into external modules.

For this checkpoint, your goal is to cleanly integrate all of those concepts into a single robust program: a CLI Organizer. This could be a Task manager or a polished Contact Manager. 

The primary grading criteria is not how fancy the menu looks, but **how cleanly your code is organized.** I am going to look for a completely separated `utils` module, a custom class with its own methods, and a clean main loop."

---

## 4) Live Demo: Expected Behavior (~5 minutes)

**Say:**
"Before you begin, let me show you the expected behavior. Watch how my program handles invalid inputs, searches gracefully, and keeps running."

**Run your prepared solution and narrate:**
1. Start the program. Show the menu.
2. Try adding an empty name. Show it get rejected.
3. Add a valid entry.
4. List entries.
5. Search for a name that doesn't exist.
6. Search for an entry that does exist.
7. Quit cleanly.

**Say:**
"It doesn't have to look exactly like this, but this is the baseline functionality."

---

## 5) Hands-on Checkpoint Lab (40–45 min)

### 5.1 Lab specification

**Display or read aloud:**

---

**Checkpoint Lab 5: CLI Organizer**

**Task:** Build an interactive Command Line Organizer (e.g., Task Tracker or Contact App) that runs completely in-memory.

**Requirements:**
1. **Multiple Files**: Your project must have a `main.py` and at least one other file called `utils.py` (or similar). You must import from the second file.
2. **OOP**: Define at least 1 custom class (e.g., `Task` or `Contact`). The class must have an `__init__` method and at least one other custom method (like `display` or `validate`).
3. **Functions**: You must write and utilize at least 3 distinct functions outside of your class methods (e.g., `show_menu()`, `find_item()`, `clear_screen()`).
4. **Interactivity**: A `while` loop that keeps the menu running until the user selects a "Quit" option.
5. **Features**: Add, List, and Search.
6. **No File I/O**: Keep everything in a list in memory. We will cover saving to disk next session.

---

**Instructor Note for Circulation:**
This is an assessment. Limit your help to conceptual unblocking ("Take a look at how you are importing your `utils` module — what folder are you in?"). Let them struggle with logic errors. 

A common pitfall will be file organization. If they run `main.py` but their terminal is in a different directory, Python won't find `utils.py`. Help them navigate terminal directories using `cd` if they get stuck on imports.

---

## 6) Debrief and Wrap-up (~10 minutes)

### 6.1 Review common themes

**Say:**
"Time is up! Please submit your code according to our standard procedures. Let's do a quick debrief. 

Did anyone run into issues when trying to import their variables or functions from the `utils.py` file?"

*Allow 1-2 learners to share. Quickly review that `from utils import ...` relies on the files sitting together in the same working directory.*

### 6.2 Showcase

**Say:**
"Is there anyone who wants to quickly screen-share or point to one place where they reduced code duplication by using a function?"

*Select a learner who successfully separated their logic to explain how their `main.py` is much shorter than it used to be.*

### 6.3 Wrapping up the Day

**Say:**
"Excellent work today. At this point, you have seen all the major puzzle pieces of standard programming layout: data structures, loops, functions, objects, and modular files.

The missing piece is persistence. Right now, when our script stops, our data evaporates. In our next session, we will learn how to read and write text files and JSON files to save our data permanently. See you next time!"
