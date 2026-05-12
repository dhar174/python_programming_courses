# Basics Day 12 — Session 12 (Hours 45–48)
Python Programming (Basic) • Capstone Delivery and Final Review

## Session 12 Overview
- Hour 45: Capstone kickoff — requirements + scaffolding
- Hour 46: Capstone build sprint
- Hour 47: Capstone polish + demo readiness
- Hour 48: Final assessment + certification-style review

---

# Day 12 Goal

## Finish With a Working Story
- Build a small command-line capstone project
- Save and load data with JSON in a `data/` folder
- Organize code with functions, modules, and at least one class
- Handle common input and file errors gracefully
- Demo the project clearly in under 3 minutes

---

# Capstone Theme Choices

## Choose One CLI Personal Organizer
- Tasks
- Contacts
- Notes

## Keep It Basics-Scope
- No web frameworks
- No databases
- No GUI frameworks
- No external packages required

---

# Required Capstone Features

## Minimum Requirements
- Menu loop
- Functions split into modules
- At least one class
- JSON persistence in a `data/` folder
- Exception handling for input and file errors

## Today’s Rule
Build the minimum viable product first, then polish.

---

# Hour 45: Kickoff + Scaffold

## Learning Outcomes
- Define capstone requirements
- Plan the first build steps
- Create the project skeleton
- Make one action work end to end

## Deliverable
Skeleton + load/save + one CRUD action working.

---

# Suggested File Layout

```text
personal_organizer/
├── main.py
├── models.py
├── storage.py
├── actions.py
├── data/
│   └── organizer.json
└── README.md
```

## Why This Layout Helps
- `main.py` owns the menu flow
- `storage.py` owns JSON load/save
- `models.py` owns the class
- `actions.py` owns add/list/search/update/delete behavior

---

# First Working Flow

## Live Demo Target
1. Show the menu
2. Load existing data or start with defaults
3. Add one item
4. Save data
5. Restart and prove the item loads

## MVP Question
What is the smallest useful version of your organizer?

---

# Load Safely When File Is Missing

```python
from pathlib import Path
import json

DATA_FILE = Path("data") / "organizer.json"

def load_items():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Data file is damaged; starting with an empty list.")
        return []
```

---

# Save After Changes

```python
def save_items(items):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(items, file, indent=2)
```

## Common Pitfall
If add/update/delete works during the run but disappears after restart, check whether `save_items()` was called.

---

# Hour 46: Build Sprint

## Learning Outcomes
- Complete the required CRUD feature set
- Improve UX and robustness
- Test features as they are added

## Build Order
Add → list → search → update/delete → save/load retest

---

# Build Sprint Checklist

## Required Actions
- Add an item
- List items
- Search or view one item
- Update or mark an item complete
- Delete an item
- Save data after changes

## Quality Improvement
Pick at least one: sorted output, confirmations, or input validation.

---

# Input Validation Pattern

```python
choice = input("Choose an option: ").strip()

if choice == "1":
    add_item(items)
elif choice == "2":
    list_items(items)
elif choice == "q":
    print("Goodbye!")
else:
    print("Please choose a listed option.")
```

## Keep It Clear
Friendly messages are part of user experience.

---

# Debug During the Sprint

## Spot-Check After Each Feature
- Does the menu still appear?
- Does the action change the right data?
- Does the data save?
- Does restart/load still work?
- Does invalid input avoid a crash?

## Exit Ticket
What is one bug you fixed today, and how did you find it?

---

# Hour 47: Polish + Demo Readiness

## Learning Outcomes
- Finalize capstone quality
- Prepare a short demo walkthrough
- Test from a fresh run

## Deliverable
A project that runs cleanly from scratch and supports a demo flow in under 3 minutes.

---

# Polish Checklist

## Before Demo
- Prompts are clear
- Output is readable
- Invalid menu choices are handled
- Missing or damaged data files are handled
- README explains how to run the project
- Full demo flow has been rehearsed

## Avoid
Last-minute refactors that break working code.

---

# Demo Script

## Recommended Flow
1. Start the program
2. Add an item
3. List items
4. Search or update an item
5. Save and quit
6. Restart and prove data persists

## Good Demo Habit
Say what you are proving before you run the step.

---

# README Minimum

```text
# Personal Organizer

Run:
python main.py

Features:
- Add items
- List items
- Search items
- Save/load JSON data
```

## Why It Matters
Run instructions make your project easier to grade, demo, and revisit.

---

# Hour 48: Final Assessment + Review

## Learning Outcomes
- Demonstrate Basics competency end to end
- Explain project structure at a high level
- Identify next study targets

## Final Activities
- Capstone demo + rubric scoring
- Short certification-style review
- Individual feedback

---

# Capstone Rubric

| Category | What We Look For |
| --- | --- |
| Requirements met | Menu, modules, class, JSON, exceptions |
| User experience | Clear prompts and readable output |
| Code organization | Clear responsibilities |
| Data persistence | Save/load works across runs |
| Demo & explanation | Clear walkthrough in under 3 minutes |

---

# Certification-Style Review Domains

## Review Agenda
- Types + conversions
- Strings + formatting
- Data structures: list, tuple, set, dict
- Conditionals + loops
- Functions + modules + basic classes
- Files, JSON, paths, and directories
- Exceptions: `ValueError`, `FileNotFoundError`, `JSONDecodeError`

---

# Code Reading Practice

## Predict or Explain
- String slicing + `len()`
- f-strings with numeric conversion
- `range()` boundaries
- Guarding list indexes with `len()`
- Safe dictionary access with `in` or `.get()`
- Function `return` vs `print`
- JSON load recovery when a file is missing

---

# Final Exit Ticket

## Reflection Prompts
- One concept I feel strong about is...
- One concept I should review is...
- One debugging habit I will keep using is...
- One improvement I would add to my capstone next is...

## Course Close
You now have the full Basics toolkit for building small, useful Python programs.
