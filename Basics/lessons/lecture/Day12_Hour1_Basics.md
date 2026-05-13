# Session 12, Hour 1: Capstone Kickoff — Requirements & Scaffolding

## Hour intent and instructor framing

This hour is the launchpad for the capstone. Keep students focused on one goal: **a working MVP skeleton** that runs, loads data, performs one useful action, and saves reliably.
Do not let the class drift into full-feature implementation yet. That belongs to later hours.

Use this script as a near-verbatim speaking guide. You can adapt your tone, but keep the sequence and constraints intact so all students leave Hour 45 with the same foundation.

---

## Outcomes (align to runbook Hour 45)

By the end of this hour, students will:

1. **Define capstone requirements and plan implementation steps.**
2. **Build a project skeleton and first working flow.**

---

## Suggested pacing map (60 minutes)

- **0:00-0:05** Welcome + hour objective
- **0:05-0:20** Talk points (10–15 min)
  - Capstone spec review
  - MVP-first principle
  - File layout: `main.py` + modules
- **0:20-0:30** Live demo (5–10 min)
  - Scaffold menu + load data + one action + save
- **0:30-0:58** Hands-on lab (25–35 min)
  - CLI Personal Organizer MVP
- **0:58-1:00** Quick check / exit ticket

---

## Instructor opening script (first 5 minutes)

> “Welcome to Day 12, Hour 1. Today we begin the capstone.
> The goal of this hour is not to finish a perfect app.
> The goal is to build a stable starting point we can trust.”

> “Your capstone app is a **CLI Personal Organizer**.
> You’ll choose one theme: **Tasks**, **Contacts**, or **Notes**.
> The theme can change the wording, but not the core structure.”

> “The structure is non-negotiable for this hour:
> - menu loop
> - functions split into modules
> - at least one class
> - JSON persistence in a `data/` folder
> - exception handling for input and file errors”

> “Today we ship the MVP skeleton:
> project setup + load/save + one CRUD action working end to end.”

Pause and ask:

> “Quick pulse check: who has ever tried to build too much too early and then got stuck?”

Most hands will go up. Use that moment:

> “Exactly. Today is how we avoid that trap.”

---

## Talk points block (10–15 minutes)

### 1) Capstone spec review (clear, concrete, non-negotiable)

Use this section to make requirements explicit and visible. Keep it concrete, not abstract.

Say:

> “Let’s translate the spec into engineering checks.
> If I can’t point to it in code, it doesn’t count.”

Write this on board or shared screen:

### Required for Hour 45

- A project/repo folder exists and is organized.
- Program runs from `main.py`.
- Menu appears in a loop until user exits.
- Logic is split into modules (not everything in one file).
- At least one class is present and used.
- Data persists to JSON in `data/`.
- Program handles:
  - bad menu input
  - missing or malformed JSON file
- One CRUD action works end-to-end.

Then emphasize:

> “One working flow beats five broken features.
> Our bar is reliability, not breadth.”

### 2) MVP-first principle (the mindset for successful capstones)

Define MVP in student-friendly language:

> “MVP means the **smallest useful version** that proves your architecture works.”

Then clarify what MVP is **not**:

- Not “minimum effort”
- Not sloppy code
- Not skipping structure

What MVP **is**:

- Small feature scope
- Good skeleton
- Reliable load/save path
- Clear extension points

Use an analogy:

> “Think of building a house.
> MVP is foundation + framing + one working door.
> It is not wallpaper, landscaping, and a second floor.”

### 3) File layout: `main.py` + modules

Introduce the mental model:

> “`main.py` should read like a control tower, not a warehouse.
> It orchestrates. Modules do the work.”

Recommended starter layout (for all themes):

```text
personal_organizer/
├─ main.py
├─ organizer/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ storage.py
│  └─ actions.py
└─ data/
   └─ items.json
```

Explain each file:

- `main.py`: menu loop + high-level flow
- `models.py`: class definitions (`Task`, `Contact`, or `Note`)
- `storage.py`: load/save JSON
- `actions.py`: CRUD action functions

Then set a boundary for this hour:

> “Today, your architecture must be extendable, but your features stay small.”

### 4) What “one CRUD action” means in this hour

Remind students of CRUD:

- Create
- Read
- Update
- Delete

For Hour 45, they need **at least one** action fully wired.
Best default is **Create** (`add item`) because it exercises class creation, validation, and persistence.

> “If your app can add one item and that item is still there after restart, you have a real product foundation.”

### 5) Common pitfalls (preemptive coaching)

Call these out before coding starts:

1. **Overbuilding before MVP works**
   - Students add tags, priorities, deadlines, categories before save path works.
2. **Complex data model too early**
   - Deep nesting and relationships too soon.

Say:

> “Your first version should feel almost boring.
> Boring is good. Boring means stable.”

---

## Live demo script (5–10 minutes): scaffold menu + load data + one action + save

### Demo objective

Build a small but real CLI organizer (Task theme in demo) that:

- starts cleanly even if `data/items.json` is missing
- shows menu loop
- adds one task (Create)
- saves and reloads from JSON

### Step 0: show expected folder structure

Speak while creating folders:

> “I’m creating structure first, before feature code, because structure reduces chaos.”

```text
personal_organizer/
├─ main.py
├─ organizer/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ storage.py
│  └─ actions.py
└─ data/
```

### Step 1: `organizer/models.py` (at least one class)

```python
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            done=bool(data.get("done", False)),
        )
```

Narration:

> “This class gives us structure and consistency.
> `to_dict()` and `from_dict()` make JSON conversion explicit.”

### Step 2: `organizer/storage.py` (JSON persistence + file error handling)

```python
import json
from pathlib import Path

from organizer.models import Task


DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "items.json"


def load_tasks() -> list[Task]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            raw_items: list[dict] = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: data/items.json is invalid JSON. Starting with empty data.")
        return []
    except OSError as error:
        print(f"Warning: could not read data file ({error}). Starting with empty data.")
        return []

    tasks: list[Task] = []
    for item in raw_items:
        try:
            tasks.append(Task.from_dict(item))
        except (KeyError, TypeError, ValueError):
            print(f"Warning: skipped invalid item: {item}")
    return tasks


def save_tasks(tasks: list[Task]) -> bool:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        payload = [task.to_dict() for task in tasks]
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2)
        return True
    except OSError as error:
        print(f"Error: could not save data ({error}).")
        return False
```

Narration:

> “Notice the missing-file path: if file does not exist, we return an empty list.
> That is exactly one of our completion criteria.”

### Step 3: `organizer/actions.py` (one CRUD action: Create)

```python
from organizer.models import Task


def next_task_id(tasks: list[Task]) -> int:
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1


def add_task(tasks: list[Task], title: str) -> Task:
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Task title cannot be empty.")

    task = Task(id=next_task_id(tasks), title=cleaned_title)
    tasks.append(task)
    return task


def display_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("No tasks saved yet.")
        return

    print("\nSaved Tasks:")
    for task in tasks:
        status = "done" if task.done else "open"
        print(f"- [{status}] #{task.id}: {task.title}")
```

Narration:

> “This file is intentionally tiny.
> We only implement what we need for today’s flow.”

### Step 4: `main.py` (menu loop + input handling + save)

```python
from organizer.actions import add_task, display_tasks
from organizer.storage import load_tasks, save_tasks


def print_menu() -> None:
    print("\n=== Personal Organizer MVP ===")
    print("1) Add task")
    print("2) List tasks")
    print("3) Save and exit")


def read_menu_choice() -> int:
    raw_choice = input("Choose an option (1-3): ").strip()
    return int(raw_choice)


def main() -> None:
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s).")

    while True:
        print_menu()

        try:
            choice = read_menu_choice()
        except ValueError:
            print("Please enter a number: 1, 2, or 3.")
            continue

        if choice == 1:
            title = input("Enter task title: ")
            try:
                task = add_task(tasks, title)
                print(f"Added task #{task.id}: {task.title}")
            except ValueError as error:
                print(f"Input error: {error}")
        elif choice == 2:
            display_tasks(tasks)
        elif choice == 3:
            if save_tasks(tasks):
                print("Data saved. Goodbye.")
            else:
                print("Exiting without confirmed save.")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
```

Narration:

> “This is our complete Hour 45 target: menu, load, one action, save, and error handling.”

### Step 5: quick deterministic run (show evidence)

Use this exact flow in terminal:

1. Start app when no JSON exists.
2. Add task: `Buy groceries`
3. List tasks.
4. Save and exit.
5. Restart app and list again.

Expected behavior:

- First run starts with `Loaded 0 task(s).`
- After add + save, `data/items.json` is created.
- Restart shows `Loaded 1 task(s).`

Possible resulting JSON:

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "done": false
  }
]
```

Close demo with:

> “Not fancy. But solid. This is exactly what we want before scaling features.”

---

## Hands-on lab (25–35 minutes): CLI Personal Organizer MVP

### Student prompt (say this clearly)

> “Now you will build your own organizer MVP.
> Choose **one theme**: Tasks, Contacts, or Notes.
> Keep scope tight and ship a working skeleton.”

### Theme choice options

- **Tasks**: track short task titles and completion state
- **Contacts**: store name + phone/email
- **Notes**: save short text notes with titles

### Non-negotiable constraints

Students must include all of the following:

1. **Menu loop**
2. **Functions split into modules**
3. **At least one class**
4. **JSON persistence in `data/` folder**
5. **Exception handling for input and file errors**

### Deliverable this hour

**Skeleton + load/save + one CRUD action working**

### Completion criteria

- Repo/folder created.
- Program runs and shows menu.
- Load/save works even if file missing.

---

## Lab facilitation guide (what to say while students work)

Use this progression to keep students moving:

### Minute 0–5 of lab: lock in scope

Ask every student/team:

- “Which theme did you choose?”
- “What is your one CRUD action for today?”
- “What is your data file name in `data/`?”

If they cannot answer in 30 seconds, they are not scoped yet.

Recommended one-action defaults:

- Tasks: Add task
- Contacts: Add contact
- Notes: Add note

### Minute 5–12: scaffold folders and files

Require this minimal structure:

```text
student_project/
├─ main.py
├─ organizer/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ storage.py
│  └─ actions.py
└─ data/
```

Coach line:

> “If your folders are unclear, your code will be unclear.”

### Minute 12–20: implement class + storage

Students should complete:

- one class in `models.py`
- `load_*()` and `save_*()` in `storage.py`
- missing-file handling

Checkpoint question to each student:

> “If I delete your JSON file and run again, does your app still start?”

If no, help them first before any additional feature.

### Minute 20–28: menu loop + one action

Students wire:

- menu loop in `main.py`
- one action function in `actions.py`
- save on exit (or immediately after add)

Checkpoint:

> “Can you add one item, exit, restart, and still see it?”

### Minute 28–35: stabilize and verify

Students test:

- invalid menu input
- empty text input for add
- malformed JSON file scenario (if possible, quickly simulate)

End state should meet completion criteria, not extra features.

---

## Guidance you can give without taking over student code

Use these coaching prompts instead of solving everything for them:

- “Where should this logic live: `main.py` or a module?”
- “What does this function return on error?”
- “How will you prove load/save works?”
- “What happens if input is blank?”
- “Is this today’s MVP or tomorrow’s enhancement?”

When students are stuck, ask them to verbalize flow:

1. load data
2. show menu
3. receive choice
4. run one action
5. save data
6. exit safely

If they can explain it, they can implement it.

---

## Theme-specific starter schemas (keep simple)

Use these examples to keep students from overmodeling too early.

### Tasks schema

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "done": false
  }
]
```

### Contacts schema

```json
[
  {
    "id": 1,
    "name": "Ari Patel",
    "phone": "555-0101"
  }
]
```

### Notes schema

```json
[
  {
    "id": 1,
    "title": "Ideas",
    "body": "Build a study plan."
  }
]
```

Important reminder to students:

> “Flat, simple fields now.
> No nested subtasks, no tags list, no extra metadata unless your MVP is already done.”

---

## Reference implementation pattern (students can adapt by theme)

If learners need a clearer template, share this generic pattern.

### `organizer/models.py`

```python
from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title}

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        return cls(id=int(data["id"]), title=str(data["title"]))
```

### `organizer/storage.py`

```python
import json
from pathlib import Path

from organizer.models import Item


DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "items.json"


def load_items() -> list[Item]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            payload: list[dict] = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: invalid JSON. Starting with empty list.")
        return []
    except OSError as error:
        print(f"Warning: file read error: {error}")
        return []

    items: list[Item] = []
    for raw in payload:
        try:
            items.append(Item.from_dict(raw))
        except (KeyError, TypeError, ValueError):
            print(f"Warning: skipped invalid item: {raw}")
    return items


def save_items(items: list[Item]) -> bool:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump([item.to_dict() for item in items], file, indent=2)
        return True
    except OSError as error:
        print(f"Error: save failed: {error}")
        return False
```

### `organizer/actions.py`

```python
from organizer.models import Item


def _next_id(items: list[Item]) -> int:
    if not items:
        return 1
    return max(item.id for item in items) + 1


def add_item(items: list[Item], title: str) -> Item:
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Title cannot be empty.")
    item = Item(id=_next_id(items), title=cleaned)
    items.append(item)
    return item
```

### `main.py`

```python
from organizer.actions import add_item
from organizer.storage import load_items, save_items


def show_menu() -> None:
    print("\n=== Organizer ===")
    print("1) Add item")
    print("2) Save and exit")


def main() -> None:
    items = load_items()
    print(f"Loaded {len(items)} item(s).")

    while True:
        show_menu()
        try:
            choice = int(input("Choose (1-2): ").strip())
        except ValueError:
            print("Enter a number.")
            continue

        if choice == 1:
            title = input("Title: ")
            try:
                item = add_item(items, title)
                print(f"Added #{item.id}: {item.title}")
            except ValueError as error:
                print(f"Input error: {error}")
        elif choice == 2:
            if save_items(items):
                print("Saved. Bye.")
            else:
                print("Could not confirm save.")
            break
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
```

This pattern satisfies Hour 45 requirements and leaves room for later expansion.

---

## Instructor QA checklist during lab

Walk around and verify each student against this checklist:

### Structure checks

- [ ] `main.py` exists
- [ ] modules exist (`models.py`, `storage.py`, plus action module)
- [ ] `data/` folder used for JSON

### Behavior checks

- [ ] app runs and shows menu
- [ ] bad menu input handled
- [ ] app starts when JSON file is missing
- [ ] one CRUD action works
- [ ] data persists after restart

### Code quality checks (Hour 45 level)

- [ ] class is actually used, not just defined
- [ ] functions are small and named clearly
- [ ] `with` used for file operations
- [ ] no giant “everything” function

If a student is missing one constraint, coach to repair that first before adding features.

---

## Common pitfalls and intervention scripts

### Pitfall 1: Overbuilding before MVP works

Symptoms:

- Student starts building update/delete/search before create/save works
- Student starts UI polish before persistence works

Intervention script:

> “Pause feature expansion.
> Show me one successful add + save + restart cycle first.”

### Pitfall 2: Complex data model too early

Symptoms:

- deeply nested dictionaries
- multiple classes with unclear relationships
- confusion about serialization

Intervention script:

> “Flatten the model for now.
> One class, 2–4 fields, deterministic ID, save/load stable.
> Complexity comes after reliability.”

### Pitfall 3: Everything in `main.py`

Symptoms:

- 100+ lines in one file quickly
- repeated code

Intervention script:

> “`main.py` should orchestrate only.
> Move storage and action logic to modules.”

### Pitfall 4: Input assumptions

Symptoms:

- direct `int(input())` with no exception handling
- blank titles accepted silently

Intervention script:

> “Assume users type unexpected values.
> Handle `ValueError` and validate blank input.”

### Pitfall 5: Save path not tested

Symptoms:

- student says “it should save” but never reopened app

Intervention script:

> “Don’t trust assumptions.
> Run the restart test now.”

---

## Optional extension (Basics scope): add a basic search feature early

If a team stabilizes menu, load/save, and one action quickly, allow an early basic-search extension during this hour.

Keep search minimal:

- one prompt term
- case-insensitive substring match
- print matched items

Example (tasks/items):

```python
def search_items(items: list[Item], term: str) -> list[Item]:
    query = term.strip().lower()
    if not query:
        return []
    return [item for item in items if query in item.title.lower()]
```

Coach boundary:

> “Search is optional polish.
> If load/save isn’t stable yet, search waits.”

---

## Full speaking script (expanded, near-verbatim delivery)

Use this if you want a continuous narrative for the hour without improvising transitions.

### Segment A: transition into capstone mindset

> “Team, today is the first capstone build hour.
> I want you to hear one sentence clearly: **we are building for reliability first**.”

> “When beginners struggle in final projects, it is rarely because they can’t write Python syntax.
> It is usually because scope grows faster than structure.
> So in this hour, we reverse that pattern.”

> “You are not being graded on how many features you list in a plan.
> You are being graded on whether your current build can run, load, process one action, and save safely.”

> “That means you will probably write less code than you expect—and that is exactly right.”

### Segment B: spec-to-code translation

> “Let’s map each requirement to concrete code evidence.”

> “Requirement one: menu loop.
> Evidence: I can run the app and it keeps prompting until I choose exit.”

> “Requirement two: functions split into modules.
> Evidence: storage logic is not buried in `main.py`; action logic is not duplicated in the menu block.”

> “Requirement three: at least one class.
> Evidence: a class exists and is actually used to create objects that get persisted.”

> “Requirement four: JSON persistence in `data/`.
> Evidence: after running one add action and saving, we can see a JSON file in `data/` and it reloads next run.”

> “Requirement five: exception handling for input and file errors.
> Evidence: invalid menu input does not crash; missing JSON file does not crash.”

> “If you can show all five evidences, you are on track.”

### Segment C: MVP-first boundary setting

> “Now let’s define what we are intentionally not doing this hour.”

> “We are not implementing complete CRUD suites for every theme.
> We are not designing perfect domain models.
> We are not polishing UX text for ten edge cases.”

> “We are doing one stable flow.
> I want your future self to inherit clean, testable code—not an unfinished pile of features.”

> “When you feel the urge to add ‘just one more thing,’ stop and ask:
> does this improve today’s MVP checklist?
> If not, park it.”

### Segment D: module architecture explanation

> “Modularity is not ceremony. It reduces cognitive load.”

> “When your app grows, every file should answer one question:
> - `main.py`: What is the control flow?
> - `models.py`: What does one data object look like?
> - `storage.py`: How does data move to and from disk?
> - `actions.py`: What behavior can users trigger?”

> “This separation makes bugs easier to isolate.
> If save fails, check storage.
> If IDs break, check actions.
> If menu loops wrong, check main.
> That is maintainability.”

### Segment E: pre-lab confidence reset

> “Some of you may think, ‘my app is too simple.’
> Simplicity is a strength right now.”

> “A stable simple app can become a strong complex app.
> An unstable complex app usually collapses.”

> “Your target at end of this hour is not impressive complexity.
> Your target is dependable behavior.”

---

## Planning worksheet you can run live (5 minutes before coding)

Have students fill this quickly in notes before they touch code:

1. **Theme chosen:** Tasks / Contacts / Notes
2. **One CRUD action today:** Create / Read / Update / Delete
3. **Class name:** `Task`, `Contact`, or `Note`
4. **JSON file path:** `data/items.json` (or theme-specific equivalent)
5. **Menu options today (max 3):**
   - option 1: action
   - option 2: optional list/preview
   - option 3: save and exit
6. **Input validation rule:** one sentence
7. **File error handling rule:** one sentence
8. **Proof test they will run:** add → save → restart → verify

Say:

> “If you cannot complete this worksheet, coding now will be guesswork.”

Collect quick verbal confirmations:

- “What is your action?”
- “What is your JSON path?”
- “How do you handle missing file?”

This prevents 20 minutes of preventable drift.

---

## Additional deterministic demo variants (if students use different themes)

If many students choose Contacts or Notes, use these tiny substitutions so they can map from your demo quickly.

### Contacts class variant

```python
from dataclasses import dataclass


@dataclass
class Contact:
    id: int
    name: str
    phone: str

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "phone": self.phone}

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        return cls(
            id=int(data["id"]),
            name=str(data["name"]),
            phone=str(data["phone"]),
        )
```

### Notes class variant

```python
from dataclasses import dataclass


@dataclass
class Note:
    id: int
    title: str
    body: str

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "body": self.body}

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            body=str(data["body"]),
        )
```

### Menu wording adaptation examples

Tasks:

```text
1) Add task
2) List tasks
3) Save and exit
```

Contacts:

```text
1) Add contact
2) List contacts
3) Save and exit
```

Notes:

```text
1) Add note
2) List notes
3) Save and exit
```

Reinforce:

> “Theme changes labels, not architecture.”

---

## Error-handling mini-lesson (embedded during lab support)

When you see repeated crashes, pause the room for a 2-minute micro-teach:

### Input error pattern

```python
try:
    choice = int(input("Choose: ").strip())
except ValueError:
    print("Please enter a valid number.")
    continue
```

Explain:

- `input()` always returns a string.
- `int(...)` raises `ValueError` if conversion fails.
- handle and continue loop; do not crash.

### File error pattern

```python
try:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        raw = json.load(file)
except FileNotFoundError:
    raw = []
except json.JSONDecodeError:
    print("Invalid JSON. Starting empty.")
    raw = []
```

Explain:

- missing file is normal on first run
- malformed JSON should not end program
- safe fallback is empty list

### Why this matters in real software

Say:

> “Your user doesn’t care that Python threw a traceback.
> Your user cares whether the app recovers gracefully.”

This helps students see exceptions as UX design, not only technical requirement.

---

## Instructor triage guide for different student profiles

### Profile 1: fast coder, unstable architecture

Pattern:

- many functions, little testing
- no restart verification

Coaching:

> “Freeze feature work.
> Run a clean proof: add, save, restart, verify.
> If this fails, features are irrelevant.”

### Profile 2: cautious coder, slow but clean

Pattern:

- good structure
- hesitant confidence

Coaching:

> “You are exactly on track.
> Finish one action, then run the completion checklist out loud.”

### Profile 3: overwhelmed beginner

Pattern:

- uncertain where to start
- large blank file syndrome

Coaching:

Give explicit sequence:

1. create folders/files
2. write class with two fields
3. write load function with missing-file fallback
4. write save function
5. write menu with add + exit

Then:

> “Do not jump steps. Show me each step passing.”

### Profile 4: perfectionist overmodeler

Pattern:

- asks about enums, inheritance, complex indexing

Coaching:

> “Great instincts for future refactor.
> For Hour 45, keep one class and simple JSON objects.
> We optimize only after baseline works.”

---

## Verification script you can perform at each desk

Use this exact script to ensure consistent grading and feedback:

1. “Please run your app from terminal.”
2. “Show me the menu.”
3. “Enter invalid menu input once.”
4. “Now perform your one CRUD action.”
5. “Save and exit.”
6. “Run again and prove the new item persists.”
7. “Now tell me where class, storage, and action code live.”

If all seven steps pass, student has met Hour 45 intent.

---

## Language for keeping scope tight without discouraging ambition

Students often have excellent ideas and want to implement all of them immediately.
Use language that protects momentum while honoring their creativity:

> “That is a strong feature idea. Let’s log it in a ‘Next’ list so it is not lost.
> For this hour, finish your foundation first.”

> “Your idea is not being rejected; it is being scheduled.”

> “Stable core first, then expand.”

This framing reduces resistance and improves execution quality.

---

## Rubric-aligned feedback phrases (fast grading comments)

Use these short comments in live feedback:

- “Meets structure requirement: modules are clearly separated.”
- “Class exists and is serialized correctly.”
- “Good recovery path when JSON is missing.”
- “Menu loop is robust against non-numeric input.”
- “One CRUD action works end to end.”
- “Scope is controlled; MVP achieved.”

If not yet complete:

- “Feature ambition is high, but MVP evidence is incomplete.”
- “Need restart proof for persistence.”
- “Need explicit file-error handling.”
- “Need class usage, not only dictionary objects.”

---

## Reinforcement: what success looks like at end of Hour 45

At the end of this hour, a successful student project should feel like this:

- small codebase
- clear file boundaries
- predictable terminal behavior
- recoverable error paths
- persistent data that survives restart

It may still feel basic. That is expected and correct.

Say explicitly:

> “If your app is simple and reliable, you won this hour.”

---

## End-of-hour wrap script (last 2–3 minutes)

Bring class attention back. Ask for quick demos from 1–2 volunteers:

- run menu
- add one item
- save and exit
- restart and confirm persistence

Then summarize:

> “Today was about architecture discipline.
> You now have a working capstone core: structure, persistence, one action.
> That foundation is what makes next hour productive.”

Reinforce confidence:

> “If your app starts cleanly, handles errors, and saves data, you are doing real software engineering.”

---

## Instructor pacing recovery plan (if timing drifts)

Use this when the room falls behind so you still finish Hour 45 objectives without scope drift.

If talk points overrun:

- compress examples to one concrete theme (tasks)
- keep only one module-boundary explanation
- move deeper design discussion to Hour 46

If demo overrun happens:

- show one shortest happy path only: launch -> add -> save -> restart -> verify
- skip extra commentary and narrate only required checks
- publish the remaining demo notes in chat or LMS for later reading

If lab support load is high:

- run a 2-minute stop-and-fix pulse every 8-10 minutes
- ask students to show menu loop and file path first before debugging features
- require each team to prove one completed gate before asking for optional help

Use this closing line when recovering:

> "We are protecting the MVP milestone first. A stable base today gives you speed tomorrow."

---

## Quick check / exit ticket

Ask every student:

**“What’s your MVP feature set?”**

Expected strong answers sound like:

- “My app can load data, show a menu, add one item, and save to JSON.”
- “If the JSON file is missing, it starts with empty data.”
- “I split logic across modules and use one class for data objects.”

If a student answers with broad future plans (“I’ll build reminders, tags, and export”), redirect:

> “Good future ideas. Now restate your Hour 45 MVP only.”

---

## Instructor note for scope control

Stay strictly inside Hour 45 objectives:

- requirements clarity
- skeleton architecture
- first working flow

Do **not** let this hour become a full feature sprint or polish session.
Students should leave with reliable groundwork, not feature overload.
