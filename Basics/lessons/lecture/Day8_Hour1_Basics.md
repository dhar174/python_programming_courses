# Day 8, Hour 1: For Loops and Iteration (Course Hour 29)

**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 29 – For Loops and Iteration (state management focus)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Section 1: Learning Outcomes

By the end of this hour, you will be able to:

1. Build a menu-driven `while True` loop that keeps a program running until the user explicitly chooses to quit.
2. Display a clean list of options to the user and gracefully handle repeated menu cycles.
3. Route user actions (like 'Add', 'List', 'Search', 'Quit') using `if/elif/else` logic to dispatch the correct behavior.
4. Explain why initializing state (data structures like lists and dictionaries) *outside* the loop is necessary to preserve data across menu cycles.
5. Implement input validation and error handling within a menu-driven application to guide users toward valid choices.

---

## Section 2: Instructor Prep and Delivery Note

**Pre-Session Setup:**
- Open two empty Python files ready for live coding:
  - `hour29_menu_demo.py` – for demonstrating the concept progression
  - `hour29_menu_lab.py` – for showing the lab solution at the end
- Familiarize yourself with the exact structure you want to build during the live demo (starting with the scaffold, then adding the routing logic, then adding state management).
- Test the demo code to ensure there are no syntax errors before class begins.
- Have the runbook learning outcomes and lab specification nearby for quick reference.

**Delivery Philosophy:**
This hour introduces the foundational pattern of interactive, event-driven programming. Nearly every CLI tool, game, and application your learners will encounter works on this same principle: present options, accept input, act, and repeat. Emphasize that mastering this pattern will unlock the ability to build real, usable programs—not just scripts that run once and exit. Encourage learners to type along with the live demo; this reinforces muscle memory and helps them see the progression.

---

## Section 3: Opening Script (~5 minutes)

**Say:**
"Up until now, many of our programs ran from top to bottom and then stopped. You run it, you perhaps give it one input, it calculates something, prints the result, and exits.

But think about the applications you use every day—like a text editor, an ATM, a game, or a banking app. They don't just run once and exit. They present you with options, wait for you to do something, react to your choice, and then present the options again. They stay alive until you explicitly tell them to stop.

Today we are going to learn the pattern that makes our Python programs do exactly that. We are going to build **menu loops**—the backbone of nearly every interactive CLI application you'll ever write.

A CLI menu pattern has three essential structural parts:
1. **An infinite loop** that keeps the program running until explicitly told to stop.
2. **A menu display** (a block of print statements) showing the user their choices.
3. **Input gathering and routing logic** (`if/elif/else`) that carries out the specific action or breaks out of the loop.

This pattern is fundamental. Master it, and you unlock the ability to build real, usable programs."

---

## Section 4: Conceptual Briefing

### The Core Pattern: `while True` and `break`

**Say:**
"To keep a program alive, we use a `while True` loop. Because `True` is always true, this loop theoretically runs forever. To stop it, we use a **sentinel value** and a `break` statement—our escape hatch.

Here's the fundamental scaffold every menu follows:"

```python
while True:
    # Display options
    print("\n--- Main Menu ---")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Quit")
    
    # Get user input
    choice = input("Enter your choice: ")
    
    # Route and execute
    if choice == '3':
        print("Goodbye!")
        break  # This escapes the loop
    else:
        print(f"You chose {choice}")
```

**Key insight:** Without the `break`, the user is trapped forever. The `break` is your exit strategy. This is not a flaw—it's by design. The sentinel value (in this case, the choice '3' representing 'Quit') is our intentional control mechanism.

When we run this scaffold and the user enters '3', Python executes the `break` statement, which immediately exits the innermost loop and continues execution after the loop block. If there is no code after the loop, the program ends cleanly. This is the core control flow principle you need to master for any interactive application.

### Routing Actions with `if/elif/else`

**Say:**
"Once we have the framework, we expand it to actually *do* things. Each menu choice triggers different behavior via `if/elif` statements. The final `else` catches invalid input—a built-in validation mechanism.

Here's the expansion pattern:"

```python
if choice == '1':
    print("You chose Action 1")
elif choice == '2':
    print("You chose Action 2")
elif choice == '3':
    print("Goodbye!")
    break
else:
    print("Invalid choice. Please try again.")
```

**Why this structure matters:** Each `elif` represents a distinct code path. The program examines the user's choice and executes exactly one block—the one that matches. If none match, the `else` block runs. This is deterministic and predictable behavior.

In real applications, each branch might do significantly more: read from a file, perform calculations, modify a data structure, or call a function. The point is that the menu acts as a dispatcher—it routes traffic based on the user's selection. This is the fundamental pattern of command-driven interfaces."

### State Management: Data *Outside* the Loop (Critical!)

**Say:**
"Here's the most common mistake: initializing data structures *inside* the loop. Every loop iteration, that initialization runs again, wiping out all previous data. This is one of the top three bugs beginners make with menu loops, so let's be crystal clear about it.

**WRONG:**
```python
while True:
    items = []  # This resets every iteration!
    # ... menu logic ...
```

**RIGHT:**
```python
items = []  # Initialize OUTSIDE the loop

while True:
    # ... menu logic ...
    # items now persists across all iterations
```

**Why this matters:** Python reads and executes code line-by-line. When it encounters a line inside a loop, it executes that line *every time* the loop cycles. So if `items = []` is inside the loop, items gets reset to an empty list on every single iteration. Any data you added in the previous iteration is lost.

By contrast, if `items = []` is outside the loop (before the `while` statement), Python executes it exactly once, before the loop ever starts. The list is created once and persists throughout the program's lifetime until the loop ends or the program exits.

This principle applies to all persistent state: lists, dictionaries, counters, flags, user preferences—anything that needs to survive across menu cycles must be initialized before the loop starts. This is crucial. Many students struggle with this point, so internalize it now."

---

## Section 5: Live Demo (15–25 minutes)

**Say:**
"Let's build a complete, working menu application together. I'll demonstrate the full pattern: infinite loop, menu display, input routing, and persistent state. Please type along in your editor—this builds muscle memory."

### Demo: Inventory Tracker

**Open `hour29_menu_demo.py` and type line-by-line, narrating each piece:**

```python
# Inventory Tracker - A Complete Menu Application

print("Welcome to the Inventory Tracker!")
print("=" * 40)

# Initialize state OUTSIDE the loop
inventory = []

# Main menu loop
while True:
    # Display the menu
    print("\n--- INVENTORY MENU ---")
    print("1. Add an item")
    print("2. View all items")
    print("3. Search for an item")
    print("4. Count items")
    print("5. Quit")
    
    # Get the user's choice
    choice = input("\nEnter your choice (1-5): ")
    
    # Route based on choice
    if choice == '1':
        item = input("What item to add? ")
        inventory.append(item)
        print(f"✓ Added '{item}' to inventory.")
    
    elif choice == '2':
        print("\n--- CURRENT INVENTORY ---")
        if not inventory:
            print("(empty)")
        else:
            for idx, item in enumerate(inventory, 1):
                print(f"{idx}. {item}")
    
    elif choice == '3':
        query = input("Search for what? ")
        if query in inventory:
            print(f"✓ Found '{query}' in inventory!")
        else:
            print(f"✗ '{query}' not found.")
    
    elif choice == '4':
        count = len(inventory)
        print(f"Total items: {count}")
    
    elif choice == '5':
        print("Thank you for using Inventory Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1-5.")
```

**Run the demo and test all features:**
- Add several items
- List to show persistence
- Search for both existing and non-existing items
- Verify that data persists across loop cycles
- Quit cleanly with `break`

**Say:**
"Notice that `inventory` stays alive the entire time. We add to it, display it, search within it—all because it was initialized outside the loop. If we had put `inventory = []` inside the loop, every menu cycle would have erased everything we added. That's the critical mistake to avoid."

---

## Section 6: Practice Walkthrough (10 minutes)

**Say:**
"Let's build one more example together, but this time with a dictionary. I'll show you how the same pattern adapts to different data types."

### Demo: Phone Book

**Type into a new file or on screen:**

```python
# Phone Book - Menu Pattern with Dictionary

phone_book = {}

while True:
    print("\n--- PHONE BOOK MENU ---")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Remove contact")
    print("4. List all contacts")
    print("5. Quit")
    
    choice = input("Choose: ")
    
    if choice == '1':
        name = input("Name? ")
        number = input("Phone number? ")
        phone_book[name] = number
        print(f"Added {name}.")
    
    elif choice == '2':
        name = input("Look up: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print("Not found.")
    
    elif choice == '3':
        name = input("Remove: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Removed {name}.")
        else:
            print("Not found.")
    
    elif choice == '4':
        if not phone_book:
            print("(empty)")
        else:
            for name, number in phone_book.items():
                print(f"{name}: {number}")
    
    elif choice == '5':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")
```

**Say:**
"Same pattern, different data structure. The framework doesn't change—only what operations we perform on our data changes."

---

## Section 7: Lab with Checkpoints (30 minutes)

**Say:**
"Now it's your turn. You'll create a menu-driven application using a data structure of your choice. You have 30 minutes. Here are the checkpoints to guide you:"

### Checkpoint 1: Initialize State (2 minutes)

Create a Python file. Initialize your chosen data structure *outside* any loop. Example:
```python
my_list = []
# or
my_dict = {}
```

### Checkpoint 2: Build the Loop Structure (5 minutes)

Create the skeleton of your menu:
```python
while True:
    print("\n--- MY MENU ---")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Quit")
    
    choice = input("> ")
    
    if choice == '3':
        break
    else:
        print("You chose:", choice)
```

Run it to confirm the loop works and exits cleanly.

### Checkpoint 3: Implement "Add" Feature (8 minutes)

Add logic for the user to add a new item to your collection:
```python
if choice == '1':
    item = input("What to add? ")
    my_list.append(item)  # or my_dict[key] = value
    print("Added!")
```

Test by adding a few items and checking the menu cycles correctly.

### Checkpoint 4: Implement "View" Feature (8 minutes)

Add logic to display all items in your collection:
```python
elif choice == '2':
    print("Current items:")
    for item in my_list:
        print(f"  - {item}")
```

Test that data persists across menu cycles.

### Checkpoint 5: Add "Search" or "Delete" (5 minutes)

Implement one additional feature (search, delete, update, or count). Test thoroughly.

### Checkpoint 6: Input Validation (2 minutes)

Add an `else` clause at the end to catch invalid menu choices:
```python
else:
    print("Invalid choice. Please try again.")
```

---

## Section 8: Troubleshooting Pitfalls

1. **Infinite loop traps:** If your program never returns to the menu, you may have nested loops or forgotten `break`. Check your indentation and ensure `break` is at the top level of the menu loop, not inside an inner conditional.

2. **Data loss on loop restart:** If your data disappears after each menu cycle, you initialized it inside the loop. Move all state declarations to before the `while True` line.

3. **Invalid input causing crashes:** If the program crashes when users enter unexpected input, wrap input in `try/except` or validate choices against a known set.

4. **Menu not displaying:** Ensure your `print` statements showing the menu are inside the loop, not outside. If they're outside, the menu only shows once.

5. **Forgetting the break:** Without a `break` statement in your quit option, the program never exits. The user is trapped forever in the loop.

6. **Indentation chaos:** Python's indentation-based syntax means misaligned lines can cause unexpected behavior. Use your editor's indentation guides. Lines inside the loop should be indented; lines outside should not be.

7. **Testing only the happy path:** Students often test only valid inputs. Spend time testing edge cases: invalid menu choices, empty collections, repeated operations, and quit sequences.

---

## Section 9: Quick-Check Questions

1. **Why do we initialize data (lists, dictionaries) outside the `while True` loop instead of inside?**
   - *Answer:* Because Python re-executes every line inside the loop on each iteration. If we initialize inside, every cycle resets our data to empty. By initializing outside, the data persists across cycles.

2. **What is the purpose of the `break` statement in a menu loop?**
   - *Answer:* The `break` statement exits the loop, allowing the program to end cleanly. Without it, `while True` would run forever (unless the program crashes).

3. **How do we route different menu choices to different actions?**
   - *Answer:* We use `if/elif/else` statements to check the user's input and execute the corresponding code block for each choice.

4. **What is an example of a real-world application that uses a menu loop pattern?**
   - *Answer:* ATMs, text editors, email clients, game menus, banking apps, any interactive console application. They all present choices, wait for input, act, and then repeat.

5. **If a user enters an invalid menu choice (like '99' when only 1-5 are valid), what should happen?**
   - *Answer:* The `else` clause should catch it and display an error message like "Invalid choice. Please try again." Then the loop naturally cycles back and re-displays the menu, giving the user another chance.

---

## Section 10: Wrap-Up Narrative (~2 minutes)

**Say:**
"Today we've mastered the menu loop—the cornerstone pattern of interactive programming. You now understand:

- How to use `while True` with a clear `break` strategy to keep a program alive and let it exit cleanly.
- How to display a menu and route user choices via `if/elif/else`.
- Why data must be initialized *outside* the loop to survive across menu cycles.
- How to build real, event-driven applications that respond to repeated user input.

This pattern scales beautifully. From a simple task tracker to a full-featured database interface, the framework remains the same. The only thing that changes is the complexity of the operations you perform on your data.

Next hour, we'll add robust input validation and error handling to make these applications bulletproof. For now, practice building different menus with different data types. Get comfortable with the rhythm: display, input, route, repeat."

---

## Section 11: Facilitation Notes

### Pacing Strategy

- **0:00–0:05** — Opening: Set context and enthusiasm. Real-world relevance is key.
- **0:05–0:13** — Conceptual Briefing: Move briskly through the three key concepts (loop structure, routing, state management). Use a whiteboard or projector to annotate code as you explain.
- **0:13–0:33** — Live Demos (20 min): Inventory Tracker demo (15 min, all features tested), then Phone Book demo (5 min). Build slowly, pausing after each logical block. Encourage students to ask questions.
- **0:33–1:03** — Checkpoints Lab (30 min): Circulate frequently. By checkpoint 3, most students should have a working "add" feature. By checkpoint 5, they should have at least a "view" and ideally a second feature (search/delete).
- **1:03–1:08** — Q&A and troubleshooting.
- **1:08–1:10** — Wrap-up and exit ticket.

### Circulation Checklist During Lab

Watch for and intervene on:
- Students initializing data *inside* the loop (ask them to trace what happens each iteration).
- Students nesting loops incorrectly (e.g., a menu inside a menu with no clear exit).
- Students who don't print the menu on every iteration (leading to a confusing UX).
- Students whose `break` is in the wrong indentation level.

### Q&A Strategies

- **"Why does my data disappear?"** → Trace the execution line-by-line. Point out where data is initialized and ask, "When does this line run?"
- **"How do I exit?"** → Confirm they have a `break` statement. Check its indentation.
- **"Can I use a different data type?"** → Absolutely. Demonstrate with a dict or set to show the pattern scales.

### Engagement Tips

- Use live demo failures as teaching moments. If a bug appears, debug it visibly. Say, "I made a mistake on purpose—let's find it together."
- Celebrate small wins. When a student gets their first menu working, acknowledge it.
- Challenge faster students: "Can you add a feature to count items?" or "Can you modify this to use a dictionary instead?"

---

## Section 12: Assessment and Differentiation Rubric

### Formative Assessment Criteria

| Criterion | Proficient | Developing | Not Yet |
|-----------|-----------|-----------|---------|
| **Loop Structure** | `while True` present; `break` used correctly to exit; program runs without hanging | Loop present but `break` may be missing or misplaced; occasional hang-ups | Loop missing or infinite without exit mechanism |
| **Menu Display** | Menu clearly printed on each iteration; options numbered and easy to follow | Menu displayed but may be missing on some iterations or lacks clarity | No menu or menu only displayed once |
| **Input Routing** | `if/elif/else` correctly routes all choices; each choice triggers intended action | Most choices routed correctly; some edge cases missed | Routing missing or severely incomplete |
| **State Management** | Data structure (list/dict) initialized outside loop; data persists across iterations | Data structure present but may be reset on some iterations | Data lost on each iteration or not present |
| **Input Validation** | Invalid choices handled gracefully; user directed to re-enter | Invalid choices sometimes cause errors or are ignored | No validation; crashes or silent failures |
| **Code Readability** | Well-commented; variable names clear; indentation consistent | Mostly readable; minor inconsistencies in naming or comments | Difficult to follow; inconsistent indentation |

### Rubric Scoring

- **Proficient (3 points):** Meets all criteria in the "Proficient" column. Student demonstrates solid understanding.
- **Developing (2 points):** Meets criteria in the "Developing" column with minor gaps. Student has core understanding but needs refinement.
- **Not Yet (1 point):** Meets criteria in the "Not Yet" column. Student needs significant rework or re-teaching.

### Differentiation Strategies

**For Faster Learners:**
- Extend the lab with additional features: "Delete" items, "Edit" items, "Sort" items, "Count" items, or filtering by category.
- Have them implement a **nested menu** (a submenu within a choice).
- Challenge them to use a more complex data type (list of dictionaries) or add file I/O to persist data.

**For Struggling Learners:**
- Provide a partially complete scaffold with comments indicating where to fill in code.
- Pair with a peer mentor for the lab portion.
- Reduce the scope: focus on "Add" and "View" only; skip "Delete" and "Edit" for now.
- Use a simpler data type (list) instead of a dictionary.

**For Advanced Learners:**
- Introduce multi-level menus with submenus.
- Discuss design patterns: command pattern, state pattern, MVC separation.
- Show how this pattern scales to web frameworks (Flask routes, Django views).
- Challenge: "How would you persist this menu's data to a file so it survives program restarts?"
