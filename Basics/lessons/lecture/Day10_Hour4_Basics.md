# Day 10 Hour 4 (Course Hour 40): Checkpoint 5 Instructor Script — Functions, Modules, and Intro OOP

**Python Programming Basics – Session 10**
**Runbook alignment:** Hour 40, Checkpoint 5
**Duration:** 60 minutes
**Delivery mode:** Instructor-led checkpoint with active lab
**Scope guardrails:** Basics only, in-memory only, no file I/O, no package architecture

## Learning Outcomes

By the end of this checkpoint, learners will demonstrate the ability to:

1. **Design and build a menu-driven CLI application** that runs in a loop and maintains state across multiple user interactions.
2. **Organize code across multiple files** using functions for behavior reuse and modules for separation of concerns.
3. **Create and use a custom class** to represent a domain entity (record, contact, or task) with state and behavior.
4. **Implement core CRUD-like operations** (Create via add, Read via list and search, with attention to error handling).
5. **Write readable, self-documenting interfaces** through clear prompts, meaningful variable names, and graceful error feedback.
6. **Recognize and apply the principle of reduced duplication** by extracting repeated logic into reusable functions.
7. **Understand import mechanics** in multi-file Python projects and troubleshoot common module resolution issues.

## Instructor purpose for this hour

This is a synthesis checkpoint. Learners now have enough building blocks to create a small but complete command-line application. Your teaching priority in this hour is not visual polish, advanced architecture, or extra features. Your priority is to validate that learners can combine fundamentals in a disciplined structure:

- functions for repeated logic
- modules for separation of concerns
- one class for structured records
- a loop-driven interface that behaves consistently

The checkpoint project is intentionally small so learners can focus on organization, clarity, and correctness. This hour bridges Basics and Advanced because it requires learners to think about architectural decisions (where does this logic belong?) rather than just syntax. Strong performance here indicates readiness for file I/O, JSON, error handling at scale, and design patterns.

## Instructor Prep Notes

### Before class, prepare these artifacts:

1. **A working reference implementation** with all three files:
   - `main.py` — the entry point and orchestrator
   - `utils.py` — reusable helper functions
   - `record.py` — class definition (optional but recommended to demo)

2. **A terminal environment** already positioned in the project directory, with imports verified to work cleanly.

3. **A deterministic demo script** with fixed test data (Ada, Grace) so output is 100% reproducible every time you run it. Reuse the same names and search terms every session.

4. **A visible checklist** posted on screen or written on whiteboard listing all completion criteria (Menu loop, 3+ functions, 1+ module, 1+ class, add/list/search, no file I/O, two files minimum).

5. **One anchor sentence** you will repeat often:
   > "Keep it in memory. Keep it readable. Keep it organized."

6. **Fallback support plan** for the two most common failures: (a) import errors from wrong directory, (b) module name collision with standard library.

7. **Stretch goals** for faster learners (delete/update features, input validation examples, display formatting) that stay within Basics scope and do not require file I/O.

### Conceptual foundation for teaching this checkpoint:

Frame the checkpoint as **graduation from procedural scripts to structured applications**. Learners have learned functions, loops, and basic OOP pieces independently. Now they integrate these into one coherent system. Success means:

- Code runs without crashes on typical inputs (robustness).
- Code is organized for readability and maintenance (structure).
- Features work as designed (correctness).
- Code demonstrates that duplication was consciously reduced (discipline).

Do not grade on UI polish, performance, or advanced features. Grade on clarity, organization, and reliability.

## Read-aloud outcomes (start of hour)

Say this clearly at the beginning:

"By the end of this checkpoint, you will be able to:

1. Build a CLI Organizer that runs in memory and stays active in a menu loop until the user quits.
2. Organize code across multiple files, including `main.py` and `utils.py`, and optionally a separate class file.
3. Use at least three functions outside class methods to reduce duplication.
4. Create and use at least one class to represent a record in your organizer.
5. Deliver core features: add, list, and search."

Then add:

"This checkpoint tests modular organization plus class usage. That is today's definition of success. Your grade is about structure and reliability, not visual polish."

## Required talk points you must cover

Before coding starts, explicitly state all deliverables. Keep this list visible on screen.

1. **Deliverables**
   - `main.py` (required)
   - `utils.py` (required)
   - class file such as `record.py` (optional, but encouraged)

2. **Usability**
   - prompts must be readable
   - output must be readable
   - users should understand what to type and what happened after each action

3. **Core behavior**
   - menu loop continues until quit
   - add record
   - list records
   - search records

4. **Structural requirement**
   - at least three functions outside class methods
   - at least one custom class
   - at least one custom module

5. **Scope boundary**
   - no file I/O
   - no saving to JSON/text
   - no advanced OOP or package setup

Use this line:

"If your app is simple but organized and stable, you are succeeding."

## Minute-by-minute run plan

- **0:00–0:05** Checkpoint framing, outcomes, requirements, scope boundaries
- **0:05–0:10** Live demo checklist (required behavior only, deterministic inputs/outputs)
- **0:10–0:50** Hands-on checkpoint lab with instructor circulation
- **0:50–0:57** Debrief, quick share, quick check on duplication reduction
- **0:57–1:00** Completion criteria review and close

## Opening Script (first 5 minutes, near-verbatim)

Say:

"Welcome to Checkpoint 5. In this hour, we are proving that we can build software that is not just working, but organized. You already know loops, lists, functions, imports, and basic classes. Now you will combine them into one complete application."

"Your project is an in-memory CLI Organizer. Think of it as a tiny contacts or tasks app that lives in memory and disappears when you quit. Today, your grade is mostly about structure and reliability, not fancy features."

"Your required files are `main.py` and `utils.py`. You may add a class file like `record.py` if you want cleaner separation. I recommend it, but it is optional."

"Required features are add, list, and search. Your menu must run in a loop until the user chooses Quit. After any action, the menu reappears so the user can do something else."

"You need at least three functions outside class methods and at least one custom class record. The class should have an `__init__` method and at least one other method."

"No file I/O in this checkpoint. Do not read or write files yet. Data lives in memory and disappears when the program exits. That is expected and correct. We will add file I/O next session."

"I care about readable prompts and readable output. If a user cannot tell what to do, or what just happened, the program is not ready."

Pause and ask:

"Any requirement unclear before I demo expected behavior? Any questions about scope or structure?"

Take 1–2 clarifying questions, then transition:

"Great. Watch the next 5–10 minutes carefully. I'm about to show required behavior in sequence. Notice that the menu loops, that we handle empty inputs gracefully, and that search gives clear feedback."

## Concept Briefing: Key Architectural Decisions (10–15 minutes)

Before demoing, briefly explain the "why" behind the structure. This context helps learners design, not just copy.

### Why split `main.py` and `utils.py`?

Say:

"In a small script, everything can live in one file. But as code grows, one file becomes hard to read and maintain. We split by responsibility:

- `main.py` is the **orchestrator**: it owns the menu loop and talks to the user.
- `utils.py` holds **reusable helpers**: functions that could be called from multiple places or imported into other projects.

This separation makes each file easier to understand and test. It also prepares you for larger projects where you might have `database.py`, `ui.py`, `models.py`, etc., all working together."

Illustrate with a real-world analogy:

"Think of a restaurant. The front-of-house person (server) is like `main.py`—they talk to customers and take orders. The kitchen is like `utils.py`—it has standard recipes and prep methods that the servers use. If you have ten servers, they all use the same kitchen. If you decided to open a food truck, you could use the same kitchen code in a different context. That is why we separate concerns."

### Why use a class to represent a record?

Say:

"A record is a bundle of related data (name, note) plus behavior (display, search). We could store these as separate lists—names in one list, notes in another—but that's error-prone and creates a data cohesion problem. A class lets us group them together:

```python
record = Record(name="Ada", note="Pioneer")
```

Now `name` and `note` stay together as a logical unit. If we add a method like `matches(term)`, the record knows how to search itself. The class becomes a small, reusable object.

Think of it this way: if I ask you 'find all records where the name contains Grace', you instinctively think of a record as one thing. With a class, your code matches that intuition. Each record is one object, and you ask the object 'do you match this term?' The object answers yes or no."

### Why a menu loop?

Say:

"A menu loop is a core CLI pattern used everywhere. The user sees the menu, makes a choice, the choice is executed, and the menu reappears. This cycle repeats until they quit. It's like:

```
while True:
    show menu
    get choice
    do action
    if quit, break
```

This pattern is used in many real applications: banking ATMs, online stores, system admin tools, video game pause menus. Once you master the pattern, you can apply it to any domain. The menu loop is durable because it is simple and predictable for users. They know they can always get back to the menu."

### Why no file I/O yet?

Say:

"In-memory storage is simpler to debug and focus on. There are no file paths, no permissions, no format conversion—just a Python list in RAM. Once you master in-memory organization, adding file I/O is a natural next step. We will do that next session."

## Live demo checklist (5–10 minutes) — required feature behavior

Use this exact checklist while you demo:

1. Start program and show menu.
2. Attempt invalid add (blank name) and show graceful message.
3. Add one valid record.
4. Add second valid record.
5. List records.
6. Search with term that has no match.
7. Search with term that has a match.
8. Enter invalid menu choice and show graceful handling.
9. Quit cleanly.

Keep the demo deterministic. Use the same values every time:

- Name 1: `Ada Lovelace`
- Note 1: `First programmer`
- Name 2: `Grace Hopper`
- Note 2: `COBOL pioneer`
- No-match search term: `Linus`
- Match search term: `Grace`

### Deterministic demo transcript (example)

```text
=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 1
Enter name:
Name cannot be empty.

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 1
Enter name: Ada Lovelace
Enter note: First programmer
Record added.

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 1
Enter name: Grace Hopper
Enter note: COBOL pioneer
Record added.

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 2
1. Ada Lovelace — First programmer
2. Grace Hopper — COBOL pioneer

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 3
Search term: Linus
No matches found.

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 3
Search term: Grace
1 match:
1. Grace Hopper — COBOL pioneer

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 9
Invalid option. Choose 1, 2, 3, or 4.

=== CLI Organizer ===
1) Add record
2) List records
3) Search records
4) Quit
Choose an option: 4
Goodbye.
```

After the demo, say:

"Your text does not need to match mine exactly, but your behavior must match this checklist. Every feature shown here—add, list, search, quit, invalid choice handling, blank input handling—must be in your code."

## Practice Exercise (5–10 minutes)

Before diving into the full lab, guide learners through a quick "skeleton build" as a group.

### Live-code the menu loop structure

Say:

"Let me show you the simplest loop structure. You will build on this. Watch:"

On screen, type:

```python
def main():
    records = []

    while True:
        print("\n=== Menu ===")
        print("1) Add")
        print("2) List")
        print("3) Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            print("Add selected")
        elif choice == "2":
            print("List selected")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
```

Say:

"This is the skeleton. It runs, the menu loops, and it quits. Notice: the loop only stops when we `break`. Everything else cycles. Now you will fill in the behavior for add and list. And you will move repeated logic (like printing the menu) into a function."

Run it once, make a choice, quit, to show it works.

Then ask:

"Where would we put the menu printing code into a separate function? Raise your hand when you see it."

Wait for hands, then say:

"Exactly. The three `print` lines. We could move them to `def show_menu():` and call `show_menu()` here instead. That is what your `utils.py` will do."

## Hands-on checkpoint lab (40 minutes)

This is the exact lab statement. Read aloud and leave it projected.

### Checkpoint lab requirements (must include these exactly)

Build an **in-memory CLI Organizer** with the following requirements:

1. **Menu loop until quit:** the app runs in a loop and exits only when the user selects quit.
2. **At least 3 functions:** outside class methods, for repeated logic.
3. **At least 1 custom module:** required `utils.py` imported into `main.py`.
4. **At least 1 class record:** custom class with `__init__` plus at least one additional method.
5. **Features:** add, list, search.
6. **No file I/O:** keep all records in memory only.
7. **Deliverables:** `main.py` + `utils.py` (class file optional).

Say:

"Focus on correctness and organization before extra features. A working, boring app that is well-organized is better than a fancy app that crashes or is hard to understand."

### Suggested technical shape (share as guidance, not a lock)

Explain that this is a recommended pattern:

- `main.py`
  - owns the loop
  - collects user choices
  - calls helper functions
  - stores records list in memory

- `utils.py`
  - shared helper functions (menu printing, validation, search helper)
  - keeps `main.py` short

- `record.py` (optional)
  - class definition for one organizer record

Remind:

"A different structure is acceptable if all requirements are met clearly."

## Reference implementation (for instructor demonstration and rescue)

Use this only when needed. Do not force students to copy it.

### `record.py` (optional class file)

```python
class Record:
    def __init__(self, name: str, note: str) -> None:
        self.name = name.strip()
        self.note = note.strip()

    def matches(self, term: str) -> bool:
        normalized_term = term.strip().lower()
        return normalized_term in self.name.lower() or normalized_term in self.note.lower()

    def display(self) -> str:
        return f"{self.name} — {self.note}"
```

### `utils.py` (required custom module)

```python
from typing import Iterable

from record import Record


def show_menu() -> None:
    print("\n=== CLI Organizer ===")
    print("1) Add record")
    print("2) List records")
    print("3) Search records")
    print("4) Quit")


def get_non_empty_input(prompt: str) -> str:
    value = input(prompt).strip()
    return value


def list_records(records: Iterable[Record]) -> None:
    records_list = list(records)
    if not records_list:
        print("No records yet.")
        return

    for index, record in enumerate(records_list, start=1):
        print(f"{index}. {record.display()}")


def search_records(records: list[Record], term: str) -> list[Record]:
    cleaned_term = term.strip()
    if cleaned_term == "":
        return []
    return [record for record in records if record.matches(cleaned_term)]
```

### `main.py` (required entry file)

```python
from record import Record
from utils import get_non_empty_input, list_records, search_records, show_menu


def add_record(records: list[Record]) -> None:
    name = get_non_empty_input("Enter name: ")
    if name == "":
        print("Name cannot be empty.")
        return

    note = get_non_empty_input("Enter note: ")
    new_record = Record(name=name, note=note)
    records.append(new_record)
    print("Record added.")


def handle_search(records: list[Record]) -> None:
    term = input("Search term: ")
    matches = search_records(records, term)
    if not matches:
        print("No matches found.")
        return

    label = "match" if len(matches) == 1 else "matches"
    print(f"{len(matches)} {label}:")
    for index, record in enumerate(matches, start=1):
        print(f"{index}. {record.display()}")


def main() -> None:
    records: list[Record] = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            list_records(records)
        elif choice == "3":
            handle_search(records)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
```

## Why this structure is checkpoint-appropriate

As you circulate, explain the "why" behind the architecture:

1. **Function separation**
   - `add_record`, `handle_search`, `list_records`, and `show_menu` each have one clear job.
   - This reduces duplication and makes bugs easier to isolate.
   - Each function has a single reason to change, following the Single Responsibility Principle.

2. **Module separation**
   - `utils.py` stores reusable helpers.
   - `main.py` becomes an orchestrator, not a giant script.
   - If you later need these helpers in another project (like a web version), you can reuse `utils.py`.

3. **Class usage**
   - `Record` groups related fields and behavior (`matches`, `display`) in one object.
   - This is a gentle intro to OOP without advanced inheritance or design patterns.
   - The class encapsulates the concept of "a record" so main code does not have to reason about names and notes separately.

4. **In-memory list**
   - easiest data store for this checkpoint
   - no persistence complexity yet
   - easy to add features without debugging file I/O issues

5. **Menu loop**
   - core CLI interaction pattern
   - easy to verify for stability
   - familiar pattern from ATMs, online forms, many real applications

Keep repeating:

"Simple and structured beats clever and tangled."

## Instructor coaching model during the lab

Use this support policy:

- provide conceptual hints
- avoid writing full solutions for learners
- ask probing questions first
- only unblock hard blockers (especially import/setup issues)

### Coaching prompts that preserve learner ownership

If learner is stuck on menu loop:

"Where in your code does control return to the top of the menu? Point to that line. What keyword makes that happen?"

If learner code repeats printing logic:

"Can you move this repeated block into one function and call it from two places? What should the function be named?"

If learner search fails:

"What should happen when term is empty? Decide that rule and code exactly that rule."

If learner has mixed concerns in one function:

"Which lines are input/output, which lines are data logic? Can we split by responsibility?"

If learner app crashes on invalid choice:

"What does your `else` branch do when the menu choice is unknown? Does it handle all cases?"

## Circulation checkpoints (time-based)

### At 10 minutes into lab

Verify each learner has:

- project folder open
- `main.py` created
- `utils.py` created
- class plan identified

Say:

"Do not start polishing output yet. First get skeleton structure in place. I want to see the loop and the files talking to each other."

### At 20 minutes into lab

Verify:

- menu loop exists
- at least one function extracted
- import line between files is working

Say:

"If import is failing, stop and fix that now. Everything else depends on it. Check your working directory. Check that files are in the same folder."

### At 30 minutes into lab

Verify:

- add feature works
- list feature works
- class object is being instantiated

Say:

"Now is the time to handle invalid inputs so your app does not crash. Add an `else` clause to catch unknown menu choices. In `add_record`, check that the name is not empty."

### At 40 minutes into lab

Verify:

- search works for match/no-match
- invalid menu choices handled
- quit works cleanly

Say:

"Last pass: readability and completion criteria check. Does a user know what to type? Does the output make sense? Is your code organized across the files as required?"

## Troubleshooting & Common Pitfalls

### Pitfall 1: import errors from wrong working directory

Typical symptom:

```text
ModuleNotFoundError: No module named 'utils'
```

Explain in detail:

- Python resolves imports relative to the current execution context.
- If terminal is not in the folder containing `main.py` and `utils.py`, import may fail.
- This is one of the hardest-to-debug issues for new Python programmers because the code looks correct, but the environment is wrong.
- When Python sees `from utils import show_menu`, it looks in specific places, starting with the directory of the script being run.
- If you run `python ../other_folder/main.py`, Python looks for `utils.py` in `../other_folder/`, not the current directory.

Fix pattern to teach:

1. Open terminal in project root folder (where `main.py` and `utils.py` sit side by side).
2. Confirm files are visible: `ls` (Mac/Linux) or `dir` (Windows). You should see both files.
3. Run `python main.py` from that same folder.
4. If still broken, run `python -c "import sys; print(sys.path)"` to see where Python is looking.
5. You can also check: `python -c "import os; print(os.getcwd())"` to verify current directory.

Say:

"The code can be correct but still fail if you run it from the wrong directory. This is not a code bug; it is a setup issue. Make sure your terminal is in the right folder. A common mistake is to open the terminal in the parent folder and try to run `python main.py` when you should first `cd` into the project folder."

### Pitfall 2: module name collision with standard library

Explain in depth with concrete examples:

- naming file `json.py` can shadow Python's `json` module
- naming file `random.py` can shadow Python's `random` module
- naming file `typing.py` can shadow `typing`
- naming file `os.py` can shadow the operating system module

This creates a subtle bug: Python finds your file first and tries to use it instead of the standard library version. If your file does not have the expected functions, you get confusing errors like `AttributeError: module 'json' has no attribute 'loads'`.

Checkpoint-safe naming guidance:

- keep required helper file as `utils.py`
- optional class file as `record.py` or `models.py`
- avoid stdlib names (search `import [name]` in Python docs to check)
- use descriptive names that reflect your domain (e.g., `organizer.py`, `contact.py` if appropriate)

Say:

"A file name can silently break imports. When you see `ModuleNotFoundError` or a weird import behavior, check your own files. Did you name a file `json.py` and then try to `import json`? Python found your file instead of the standard library version. To avoid this, choose distinctive names for your modules that are not in the standard library."

### Pitfall 3: class not being instantiated

Symptom: Class is defined but `add_record` is not creating objects; records are stored as strings or dicts instead. When you try to call methods on records, you get `AttributeError: 'str' object has no attribute 'matches'`.

Root cause: The learner defined the class but forgot to call it. They might be storing the name string directly or a dict instead of a Record object.

Explain with clarity:

"The class is a blueprint. To use it, you must call the blueprint to create an object: `new_record = Record(name, note)`. Then append that object to your list. If you append just the name string, you lose the structure."

Teach this pattern with emphasis:

```python
# Define the class (blueprint)
class Record:
    def __init__(self, name, note):
        self.name = name
        self.note = note

# Create an instance (actual object)
my_record = Record("Ada", "Pioneer")

# Use the object
print(my_record.name)
```

In `add_record`, the key line:

```python
new_record = Record(name=name, note=note)  # Create object here!
records.append(new_record)  # Store the object, not the string
```

### Pitfall 4: search method complexity

Learners sometimes write search inside `main.py` instead of as a method. Or they check for substring match but forget case-insensitivity, breaking the search when user types "grace" but the record has "Grace".

Common mistake:

```python
# Bad: repeated in main, no case-insensitivity
if search_term in record.name:
    matches.append(record)
```

Better approach:

Teach this principle with conviction:

"Search logic belongs in the `Record` class as a method. The class knows its own data best. `main.py` should just call the method and display results. This keeps `main.py` focused on the UI and the `Record` class focused on data behavior."

Example teaching moment:

```python
# Inside Record class
def matches(self, term: str) -> bool:
    normalized_term = term.strip().lower()
    return (normalized_term in self.name.lower() or
            normalized_term in self.note.lower())

# Inside main
matches = [r for r in records if r.matches(search_term)]
```

Why this works:

1. The `Record` class encapsulates the search behavior.
2. If you later decide to add a phone number field, you only change the `matches` method in one place.
3. The case-insensitive logic is centralized and tested once, not scattered throughout `main.py`.
4. Main code is readable: "find records that match the term" instead of nested `if` conditions.

## Quick-Check Questions (3–5 understanding probes)

Use these during or after the lab to gauge understanding:

1. **On functions:** "Show me one place where you extracted repeated code into a function. What did the repeated code look like, and what is the function called?"

2. **On modules:** "If you needed to use the same helper functions in a different Python project, where would they live? Which file can you copy?"

3. **On classes:** "Why did you use a class to represent a record? What would be harder to do if you stored names and notes in separate lists instead?"

4. **On scope:** "What data lives in memory? What happens to it when your program exits? Could you save it to a file next?"

5. **On loops:** "How does the menu loop know when to stop? What code makes it exit?"

## Wrap-Up Notes (summary + reflection prompts)

Say at the end:

"Congratulations. You have just built a small but real application. It has multiple files, a class, repeated logic extracted into functions, and a user interface. That is the foundation of professional software development."

Reflection prompts (ask 1–2):

- "What was the hardest part of organizing this code across files?"
- "If you added a delete feature, where would that code go? Would it be a function in utils, a method in Record, or part of main?"
- "How would saving this data to a file change your code? Where would that fit?"

## Facilitation Notes (instructor tips, timing guidance, extension ideas)

### Timing adjustments:

- If learners finish early (by 35 min), offer extensions: delete/update features, input validation for phone numbers, or display formatting.
- If learners are struggling at 35 min, reduce scope: ask them to skip search and focus on add/list, which can still meet 3+ function requirement.
- If import is breaking everyone, pause the lab and do a 3-minute "import clinic" as a whole group. Show the directory structure, the files, the import line, and run it together.

### Extension ideas (stay within Basics):

1. **Delete feature:** `def delete_record(records: list[Record], index: int)` — remove a record by position.
2. **Update feature:** `def update_record(records: list[Record], index: int, new_note: str)` — modify an existing note.
3. **Validation:** Ask for a phone number and validate format (e.g., must be 10 digits).
4. **Display formatting:** Color output with ANSI codes (even simple bold/underline), or add a separator line.
5. **Data conversion:** Accept name/note from a JSON string in the prompt and parse it (very light JSON use, no file I/O).

### Stretch goal rubric (if differentiating):

- **Base (meets checkpoint):** All 4 requirements, add/list/search work, 3+ functions, 1+ class.
- **Extended:** Base + one extension (delete, update, or validation).
- **Advanced:** Extended + two extensions or a creative feature that still stays in-memory and organized.

### Post-checkpoint plan:

Mention that next session moves to file I/O. Ask:

"How would you change this code to save records to a file? What new imports might you need? What if you wanted to load the file when the program starts?"

These questions bridge the checkpoint to the next unit and prime learners for the upcoming design challenges.

### Support for struggling learners:

If a learner is very stuck on class usage, offer this scaffolding:

```python
# Simplified Record class
class Record:
    def __init__(self, name, note):
        self.name = name
        self.note = note
```

They can fill this in, use it, and add methods (like `matches`) gradually. The key is getting the loop and multi-file structure working first. The class can be simple.

### Celebration and community:

At the end, ask 2–3 volunteers to share their solution briefly (screen share or describe). Highlight what is well-organized about each one. This normalizes different but correct approaches and reinforces that structure is a choice, not a formula.

