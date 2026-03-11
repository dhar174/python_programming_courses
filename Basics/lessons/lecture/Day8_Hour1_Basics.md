# Day 8, Hour 1: Menu Loops (Course Hour 29)
**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 29 – Menu loops (CLI pattern)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Emphasize that a menu loop is the core of most interactive CLI applications. Demonstrate how to route actions using `if/elif` blocks and validate basic input. By the end of this hour, learners should understand how to build a program that repeatedly presents choices until the user explicitly requests to quit.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Build a menu-driven `while` loop that keeps a program running until the user quits.
2. Display a list of options cleanly to the user.
3. Route user actions (like 'Add', 'List', 'Quit') using `if/elif`/`else` logic.
4. Explain why keeping state in memory outside of the loop is necessary so data isn't lost."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: The need for continuous interaction
- **0:05–0:18** Core concept: The endless `while True` loop and `break` setup
- **0:18–0:25** Showing the menu and getting input
- **0:25–0:33** Routing actions via `if/elif/else`
- **0:33–0:43** Live demo: A complete simple menu
- **0:43–0:57** Guided lab: Upgrade Menu
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour29_menu_demo.py` ready for live coding.
- Open another empty file named `hour29_menu_lab.py` to serve as a starter for the lab portion.
- Familiarize yourself with how you want to build the scaffolded menu in front of the class, showing a continuous loop.

**Say:** "Please have your editor open and an empty file ready. We are building the backbone of interactive console applications today, so typing along is essential."

---

## 3) Opening Script: The Need for Continuous Interaction (~5 minutes)

### 3.1 Reviewing previous scripts

**Say:**
"Up until now, many of our programs ran from top to bottom and then stopped. You run it, you perhaps give it one input, it calculates something, prints the result, and exits. 

But think about the applications you use every day—like a text editor, an ATM or a game. They don't just run once and exit. They present you with options, wait for you to do something, react, and then present the options again. They stay alive until you explicitly tell them to stop.

Today we are going to learn the pattern to make our Python programs do exactly that. We are going to build **menu loops**."

### 3.2 The CLI Menu Pattern

**Say:**
"A Command Line Interface (CLI) menu pattern has three main parts:
1. An infinite loop that keeps the program running.
2. A block of print statements showing the user their choices.
3. Input gathering and conditional logic (`if/elif/else`) that carries out the specific choice or breaks out of the loop."

---

## 4) Concept: The Core Menu Architecture

### 4.1 The `while True` loop

**Say:**
"We will start by looking at how to keep the program alive. For a menu, the standard approach is to use a `while True` loop. Because `True` is always true, this loop will theoretically run forever.

To stop it, we need a Sentinel value or a specific condition that triggers a `break` statement."

### 4.2 Building the Scaffold

**Type and narrate:**

```python
# hour29_menu_demo.py

print("Welcome to the Menu App!")

while True:
    print("\n--- Main Menu ---")
    print("1. Action A")
    print("2. Action B")
    print("3. Quit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '3':
        print("Goodbye!")
        break
    else:
        print(f"You chose: {choice}. Coming back to the menu...")
```

**Run it.** Test a few inputs, then type '3' to quit.

**Say:**
"Notice the structure here:
- We print a welcome message *outside* the loop. We only want to say welcome once.
- Inside the loop, we repeatedly show the menu.
- We grab the user's input.
- Our crucial mechanism is `if choice == '3': break`. This is the escape hatch. Without it, the user would be trapped forever.
- Everything else falls into the `else` block for now, and the loop simply cycles back to the top."

### 4.3 Routing actions with `elif`

**Say:**
"Now let's expand the structure to actually do things based on the user's choices. We will replace the `else` with a series of `elif` statements—one for each action."

**Type and modify:**

```python
# hour29_menu_demo.py

print("Welcome to the Menu App!")

while True:
    print("\n--- Main Menu ---")
    print("1. Say Hello")
    print("2. Tell a Joke")
    print("3. Quit")
    
    choice = input("Enter your choice (1-3): ")
    
    # Route the user's choice
    if choice == '1':
        print("Hello there! I hope you are having a wonderful day.")
    elif choice == '2':
        print("Why do Python programmers prefer dark mode? Because light attracts bugs.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select 1, 2, or 3.")
```

**Run it.** Demonstrate choosing 1, choosing 2, entering 'hello' (which triggers the invalid message), and finally 3 to quit.

**Say:**
"By using `if/elif`, we route the program flow. The final `else` serves as a catch-all for bad input. Notice how simple input validation is built right into this pattern: if they don't type '1', '2', or '3', we tell them it's invalid, and the loop seamlessly reprints the menu and asks again."

---

## 5) Concept: State and Memory Outside the Loop

### 5.1 Keeping track of data

**Say:**
"A menu is usually manipulating some data. Let's look at a very critical pitfall. What happens if we initialize a list *inside* the `while True` loop?"

**Type to demonstrate the flaw (pause before running):**

```python
while True:
    my_items = []  # Do not do this!
    
    print("\n1. Add item")
    print("2. List items")
    print("3. Quit")
    
    choice = input("> ")
    if choice == '1':
        item = input("What to add: ")
        my_items.append(item)
    elif choice == '2':
        print(f"Items: {my_items}")
    elif choice == '3':
        break
```

**Say:**
"If I add an item, and then list my items, what will happen?
Every time the loop restarts, it hits `my_items = []`. It wipes out all the memory.

To keep data persistent across loop cycles, you MUST initialize your data structures *before* the loop starts."

---

## 6) Live Demo: A Complete Simple Menu

### 6.1 Building an in-memory inventory tracker

**Say:**
"Let's put it all together. I am going to build a simple application that tracks an inventory of items. Please type along with me in `hour29_menu_demo.py`. I will build it out fully."

**Type and narrate:**

```python
# A simple Inventory Tracker using a Menu Loop

print("Starting Inventory Tracker...")

# 1. State goes OUTSIDE the loop
inventory = []

while True:
    # 2. Display the menu
    print("\n=== Inventory Menu ===")
    print("1. Add an item")
    print("2. List all items")
    print("3. Search for an item")
    print("4. Quit")
    
    # 3. Get input
    choice = input("Choose an option (1-4): ")
    
    # 4. Route logic
    if choice == '1':
        new_item = input("Enter item name to add: ")
        inventory.append(new_item)
        print(f"Added {new_item} to inventory.")
        
    elif choice == '2':
        print("\n--- Current Inventory ---")
        if not inventory:
            print("The inventory is empty.")
        else:
            for item in inventory:
                print(f"- {item}")
                
    elif choice == '3':
        query = input("Enter item to search for: ")
        if query in inventory:
            print(f"Yes, {query} is in the inventory.")
        else:
            print(f"No, {query} is not here.")
            
    elif choice == '4':
        print("Exiting tracker. Goodbye!")
        break
        
    else:
        print("Unrecognized option. Please try again.")
```

**Run it and test all features.**

**Say:**
"We have a shared data structure, `inventory`, sitting safely outside our loop.
We have four distinct actions routing perfectly.
We have a fallback `else` to catch mistakes.
This is a fully functional, event-driven pattern for the console."

---

## 7) Hands-on Lab: Upgrade Menu

### 7.1 Lab overview

**Say:**
"It's your turn to employ this pattern. You are going to take a data set you have worked with previously, or build a new simple list or dictionary, and attach it to a looped menu. You have about 14 minutes."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Upgrade Menu**

**Task:**
1. Create a menu-driven program that operates on a collection of your choice (for example, a list of favorite movies, a dictionary of friend names to phone numbers, or an expense tracker).
2. The core requirement: the program must cycle repeatedly until the user quits.
3. The menu must include actions to **add**, **list**, and **search**.
4. Remember to initialize your state (`[]` or `{}`) OUTSIDE the loop!

**Expected Menu Output Example:**
```
=== My Movie Database ===
[1] Add Movie
[2] List Movies
[3] Search Movie
[4] Quit
> 
```

**Extra Challenge (Optional):** Add a feature to **update** or **delete** an existing entry.

---

Circulate the room. Look specifically for:
- Not reprinting the menu on every iteration.
- Trapping themselves inside an inner loop instead of resolving back to the main loop.
- Initializing the collection inside the loop.

### 7.3 Walkthrough solution

After working time, write out a brief solution relying on a list:

```python
# hour29_menu_lab.py

movies = []

while True:
    print("\n=== My Movie Database ===")
    print("[1] Add Movie")
    print("[2] List Movies")
    print("[3] Search Movie")
    print("[4] Quit")
    
    choice = input("> ")
    
    if choice == '1':
        title = input("Enter movie title: ")
        movies.append(title)
        print(f"Added {title}.")
    elif choice == '2':
        for m in movies:
            print(f" - {m}")
    elif choice == '3':
        title = input("Search for: ")
        if title in movies:
            print("Found it!")
        else:
            print("Not in your database.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
```

**Say:**
"This is the cornerstone. Nearly every terminal program you use works identically to this pattern under the hood."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"Today we built menu loops. We placed our active memory outside the loop, presented choices inside the loop, and used `if/elif/else` blocks to dispatch the commands, ensuring an explicit `break` strategy so the program can end properly."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: Why is a menu loop useful for CLI programs instead of just running code linearly?"

**Expected answer:** Let them respond. "It allows for continuous interaction without forcing the user to repeatedly restart the script, mimicking how real applications run."

**Say:**
"Excellent. We are setting the stage perfectly for integrating robust validation in the next hour."
