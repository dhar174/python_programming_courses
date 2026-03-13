# Session 12, Hour 1: Capstone Kickoff: Requirements & Scaffolding

## 🎯 Outcomes
- Define capstone requirements and plan steps.
- Build project skeleton and first working flow.

## 🗣️ Instructor Speaking Script

### Introduction (10-15 min)
"Welcome to Day 12! We've made it to the final day of our Python Basics course. Today is entirely focused on our Capstone Project and final review."

"We will kick off by reviewing the capstone specifications. Our goal is to build a CLI Personal Organizer. You can choose to make it a task manager, a contact book, or a notes app—it's up to you. But the core requirements are the same: a menu loop, modular functions, at least one class, JSON data persistence, and basic exception handling."

"Before writing any complex features, your objective is to build a Minimum Viable Product, or MVP. Get the absolute basics working first before adding bells and whistles."

"We'll start by laying out our files. You'll want a `main.py` as your starting point, and you can separate your functional logic into additional Python modules."

### Live Demo (5-10 min)
*Action: Share your screen and open a new Python project folder.*

"Let's look at how to scaffold this out. Let me draft a quick menu and one functional feature with save capabilities."

*Action: Write a basic scaffolding script.*
```python
import json
import os
from pathlib import Path

# Scaffold data/ directory if missing
Path("data").mkdir(exist_ok=True)

def load_data():
    try:
        with open("data/items.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open("data/items.json", "w") as f:
        json.dump(data, f)

def main():
    data = load_data()
    while True:
        print("\n--- Organizer MVP ---")
        print("1. Add Item")
        print("2. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            item = input("Enter new item: ")
            data.append(item)
            save_data(data)
            print("Item added and saved!")
        elif choice == '2':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
```

"Notice how I tackled load/save and just one piece of CRUD functionality—adding an item. Now it's your turn."

## 💻 Hands-On Lab: Capstone MVP (25-35 min)

**Prompt for Students:**
Build a CLI Personal Organizer.

**Choose a theme:**
- Tasks
- Contacts
- Notes

**Required:**
- Menu loop
- Functions split into modules
- At least one class
- JSON persistence in a `data/` folder
- Exception handling for input and file errors

**Deliverable this hour:** Project skeleton + load/save operations + one CRUD action fully working.

### ✅ Completion Criteria
- Repo/folder is created cleanly.
- Program runs and shows the menu.
- Load/save works even if the JSON file is missing.

### 🛑 Common Pitfalls (Instructor Eyes Only)
- **Overbuilding before MVP works:** Students might try building nested objects before they can even save a string.
- **Complex data models:** Keep dictionaries flat and classes simple at first.

### 🚀 Optional Extensions
- Add a search feature early to keep the capstone application useful from the start.

## 📝 Quick Check / Exit Ticket
**Ask the class:** "What is your MVP feature set going to be? What exactly will it do in its simplest form?"
