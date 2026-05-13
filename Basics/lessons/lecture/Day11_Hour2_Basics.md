# Day 11, Hour 2: JSON Persistence (Instructor Script)

## Instructor intent for this hour

This hour is where learners move from “my program works while it is running” to “my program remembers things tomorrow.” Keep repeating that idea. Most beginners can build menu loops and simple CRUD logic by now, but many still think in temporary memory. This lesson makes persistence concrete, practical, and safe.

Your goals in this hour are tightly aligned to the runbook:

- Learners can **serialize data to JSON**.
- Learners can **load JSON back into Python structures**.
- Learners understand the difference between Python objects in memory and JSON text on disk.
- Learners can explain why `json.dump()` cannot write a custom object directly.
- Learners can implement missing-file and corrupted-file handling so their app does not crash.

Keep the tone practical and confidence-building. We are not teaching databases, advanced serialization frameworks, or architecture patterns. We are teaching a reliable Basics-level persistence workflow that learners can use immediately in their own small projects.

---

## Outcomes (state these clearly at the start)

By the end of this hour, learners will be able to:

1. Use `json.dump()` to save Python data to a `.json` file.
2. Use `json.load()` to read JSON from a file back into Python data structures.
3. Identify JSON-supported types: object/dict, array/list, string, number, boolean, null.
4. Convert one simple class object to/from dictionaries using `to_dict()` and `from_dict()`.
5. Build a small app flow where data loads on startup and saves after changes.
6. Handle two critical error conditions safely:
   - missing file (`FileNotFoundError`)
   - corrupted JSON (`json.JSONDecodeError`)

---

## Run-of-show (60 minutes total)

Use this structure as your pacing guide:

- **0:00–0:05**: Warm-up and framing (why persistence matters)
- **0:05–0:20**: Instructor talk points (10–15 min target)
- **0:20–0:30**: Live demo (5–10 min target)
- **0:30–1:00**: Hands-on lab (25–35 min target) + checkoffs

If your class runs faster, spend extra time on lab troubleshooting and extension tasks. If your class runs slower, keep the core path: save/load + missing/corrupt file handling.

---

## Prerequisites you should quickly confirm

Before diving in, verify learners can already:

- create and use `dict` and `list`
- open files with `with open(...)`
- call functions and read basic tracebacks
- run the same script multiple times from the same folder

If one of these is shaky, do a 2-minute refresh now. Don’t let hidden prerequisites block the hour.

---

## Opening script (what to say in the first 3–5 minutes)

Suggested speaking guide:

“Up to now, many of our programs forget everything when they stop running. That’s normal because variables live in RAM and RAM is temporary. Today we’ll fix that using JSON files. JSON gives us a universal text format for storing app data. We’ll save Python data structures to disk with `json.dump()`, then load them back with `json.load()`. We’ll also handle missing and corrupted files, because real users and real files are messy. By the end of the hour, your app should remember data across runs without crashing.”

Prediction prompt:

- “If I close a Python script right now, what happens to its variables?”
- “What kind of data should survive restarts in a to-do app or contacts app?”

Use one or two student answers to connect motivation to real projects.

---

## Instructor talk points (10–15 min)

The runbook asks for JSON basics, supported types, and object mapping via `to_dict/from_dict`. Use the following 12-point flow.

### Talk point 1: Persistence vs memory

- Memory (`list`, `dict`, objects in variables) is temporary.
- Files are durable across program runs.
- Persistence means writing program state to storage, then restoring it later.

Say:

“Think of memory as a whiteboard in a room. When class ends, someone erases it. A file is like a notebook you can reopen tomorrow.”

### Talk point 2: What JSON is

- JSON = JavaScript Object Notation.
- Language-neutral text format.
- Human-readable and machine-readable.

Show a tiny JSON snippet verbally:

```json
{
  "name": "Ada",
  "active": true,
  "score": 98
}
```

Remind learners: JSON booleans are lowercase `true/false`, and null is `null`.

### Talk point 3: Python `json` module

- Built into standard library (`import json`).
- Core functions today:
  - `json.dump(python_data, file_handle)`
  - `json.load(file_handle)`

Clarify pronunciation and meaning:

- dump = write out
- load = read in

### Talk point 4: File modes still matter

- `"w"` for write (overwrites existing content)
- `"r"` for read
- optional `"a"` for append (not typical for JSON document persistence)

Use this line:

“`json` handles format conversion, but you still control file opening and closing.”

### Talk point 5: JSON-supported types map to Python basics

Give this exact mapping table on screen:

| JSON | Python on load | Python before dump |
| --- | --- | --- |
| object | `dict` | `dict` |
| array | `list` | `list` or `tuple` |
| string | `str` | `str` |
| number | `int` or `float` | `int` or `float` |
| true/false | `bool` | `bool` |
| null | `None` | `None` |

Important note: tuples become lists in JSON and come back as lists.

### Talk point 6: `indent` for readability

- `json.dump(data, f, indent=2)` makes file easy to inspect.
- Pretty printing is optional but valuable in teaching and debugging.

Tie to optional extension later: pretty print with `indent=2`.

### Talk point 7: Determinism and classroom safety

For this course, use deterministic data:

- No random values
- No network calls
- No system-specific absolute paths

Say:

“If everyone runs the same code with the same starting file, everyone should see the same behavior. That makes debugging and instruction much easier.”

### Talk point 8: Missing file is normal

First run usually has no saved file.

- Use `try/except FileNotFoundError`
- Start with default data if file does not exist

This satisfies one completion criterion: no crash when file missing.

### Talk point 9: Corrupted JSON is also normal in real life

Learners must recognize:

- `json.JSONDecodeError` happens when file content is invalid JSON.
- App should recover gracefully, not crash.

Recovery strategy for Basics:

- print warning
- load fallback default data

Optional extension later: backup before overwrite to reduce risk.

### Talk point 10: Why custom objects fail with `json.dump()`

By default, JSON encoder does not know your class structure.

If you do:

```python
json.dump(my_book_object, f)
```

you get:

`TypeError: Object of type Book is not JSON serializable`

Because JSON only supports generic data types, not Python class instances.

### Talk point 11: Simple object mapping with `to_dict/from_dict`

Keep it basic:

- `to_dict()` converts object → serializable dictionary
- `from_dict()` converts dictionary → object

No advanced serializers, no custom encoders, no metaclasses.

### Talk point 12: Save points in app workflow

Common app pattern:

1. Program starts.
2. Try load JSON from disk.
3. If missing/corrupt, use fallback defaults.
4. User makes changes.
5. Program saves updated data to disk.
6. Next run restores those changes.

Have learners repeat this flow aloud once. It helps retention.

---

## Live demo (5–10 min): required runbook demo + object mapping

This demo is deterministic and classroom-safe. It includes:

- dump dict/list to `data.json`
- load and print
- operational `FileNotFoundError` and `JSONDecodeError` handling
- one simple class with `to_dict/from_dict`

### Demo setup instructions

Create a new file named `json_persistence_demo.py` in the same folder where learners are running code.

Paste and run this complete script:

```python
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

DATA_PATH = Path("data.json")


@dataclass
class Task:
    task_id: int
    title: str
    done: bool = False

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "done": self.done,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            task_id=int(data["task_id"]),
            title=str(data["title"]),
            done=bool(data["done"]),
        )


def build_demo_payload() -> dict:
    # Deterministic fallback dataset (no randomness, no external dependencies)
    tasks = [
        Task(task_id=1, title="Review JSON basics", done=True),
        Task(task_id=2, title="Practice dump and load", done=False),
    ]
    return {
        "app_name": "Hour42 Demo",
        "version": 1,
        "tasks": [task.to_dict() for task in tasks],  # object mapping here
        "tags": ["python", "json", "persistence"],
    }


def save_data(payload: dict, path: Path) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def load_data(path: Path, fallback: dict) -> dict:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[INFO] {path} not found. Using fallback data.")
        return fallback
    except json.JSONDecodeError:
        print(f"[WARNING] {path} is corrupted JSON. Using fallback data.")
        return fallback


def print_loaded_data(loaded: dict) -> None:
    print("\nLoaded dictionary:")
    print(loaded)

    print("\nTasks as Task objects reconstructed with from_dict:")
    task_objects = [Task.from_dict(item) for item in loaded.get("tasks", [])]
    for task in task_objects:
        status = "done" if task.done else "not done"
        print(f"- Task {task.task_id}: {task.title} ({status})")


def main() -> None:
    fallback_payload = build_demo_payload()

    print("[STEP 1] Load payload from data.json (or fallback if file is missing/corrupt)")
    loaded_payload = load_data(DATA_PATH, fallback_payload)
    print("[OK] Load complete.")

    print("\n[STEP 2] Save deterministic payload to data.json")
    save_data(loaded_payload, DATA_PATH)
    print("[OK] Save complete.")

    print_loaded_data(loaded_payload)


if __name__ == "__main__":
    main()
```

### Demo narration checklist

As you run the script, narrate these exact ideas:

1. We are writing a dictionary that contains a list and primitive JSON-compatible values.
2. The `Task` objects are converted to dictionaries first via `to_dict()`.
3. We read with `json.load()` and get a Python dictionary back.
4. We map dictionaries back to `Task` objects with `from_dict()`.
5. We protect load with `FileNotFoundError` and `json.JSONDecodeError`.

### Mini corruption test (operationalize JSONDecodeError handling)

After first successful run:

1. Open `data.json`.
2. Intentionally break it by deleting a comma.
3. Save file.
4. Run `json_persistence_demo.py` again.

Expected result:

- Script prints warning about corrupted JSON.
- Script continues running with fallback data.
- Script rewrites a valid `data.json` in Step 2 save.
- No crash.

This is crucial. Learners should see this behavior, not just hear about it.

### Mini missing-file test

1. Delete `data.json`.
2. Run script again.

Expected:

- Script prints info message that file is missing.
- Uses fallback data.
- Recreates valid `data.json` in Step 2 save.

You just demonstrated both required resilience conditions in a deterministic way.

---

## Transition into lab (what to say)

“Now you’ll implement the same persistence lifecycle in your own mini app: load at startup, modify data, save after changes, survive missing/corrupted files. If you don’t have a previous app ready, you’ll use today’s fallback starter so everyone can complete the hour.”

---

## Hands-on lab (25–35 min): JSON persistence mini app

### Lab objective

Implement persistence for app data using `data.json` so that:

- app data persists across runs
- app does not crash when file is missing
- app handles corrupted JSON with a safe fallback
- app saves again after changes

### Deterministic fallback mini-app dataset (required support)

Use this starter dataset so learners do **not** need a previous app:

```python
DEFAULT_DATA = {
    "next_id": 4,
    "contacts": [
        {"id": 1, "name": "Ava", "email": "ava@example.com"},
        {"id": 2, "name": "Noah", "email": "noah@example.com"},
        {"id": 3, "name": "Mia", "email": "mia@example.com"},
    ],
}
```

This dataset is deterministic, realistic, and easy to test.

### Lab scaffold (give students this full baseline)

Create `contacts_json_app.py`:

```python
from __future__ import annotations

import json
from pathlib import Path

DATA_PATH = Path("data.json")

DEFAULT_DATA = {
    "next_id": 4,
    "contacts": [
        {"id": 1, "name": "Ava", "email": "ava@example.com"},
        {"id": 2, "name": "Noah", "email": "noah@example.com"},
        {"id": 3, "name": "Mia", "email": "mia@example.com"},
    ],
}


def load_data(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if "next_id" not in data or "contacts" not in data:
                print("[WARNING] data.json missing expected keys. Using defaults.")
                return {
                    "next_id": DEFAULT_DATA["next_id"],
                    "contacts": [dict(item) for item in DEFAULT_DATA["contacts"]],
                }
            return data
    except FileNotFoundError:
        print("[INFO] data.json not found. Starting with default data.")
        return {
            "next_id": DEFAULT_DATA["next_id"],
            "contacts": [dict(item) for item in DEFAULT_DATA["contacts"]],
        }
    except json.JSONDecodeError:
        print("[WARNING] data.json is corrupted JSON. Starting with default data.")
        return {
            "next_id": DEFAULT_DATA["next_id"],
            "contacts": [dict(item) for item in DEFAULT_DATA["contacts"]],
        }


def save_data(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def list_contacts(data: dict) -> None:
    print("\n--- Contacts ---")
    contacts = data["contacts"]
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f'{contact["id"]}: {contact["name"]} <{contact["email"]}>')


def add_contact(data: dict) -> None:
    print("\n--- Add Contact ---")
    name = input("Name: ").strip()
    email = input("Email: ").strip()

    if not name or not email:
        print("[ERROR] Name and email are required.")
        return

    new_contact = {
        "id": data["next_id"],
        "name": name,
        "email": email,
    }
    data["contacts"].append(new_contact)
    data["next_id"] += 1
    print("[OK] Contact added.")


def main() -> None:
    data = load_data(DATA_PATH)

    while True:
        print("\n=== Contact App (JSON) ===")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Save and exit")
        choice = input("Choose 1-3: ").strip()

        if choice == "1":
            list_contacts(data)
        elif choice == "2":
            add_contact(data)
        elif choice == "3":
            save_data(DATA_PATH, data)
            print("[OK] Data saved to data.json. Goodbye.")
            break
        else:
            print("[ERROR] Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
```

### Lab tasks (student instructions)

#### Task 1: Run baseline app and inspect behavior

1. Run `contacts_json_app.py`.
2. Choose “List contacts.”
3. Choose “Save and exit.”
4. Open `data.json` and inspect its structure.

Expected:

- JSON file exists.
- It contains `next_id` and `contacts`.
- File is pretty-printed (`indent=2`).

#### Task 2: Verify persistence across runs

1. Run app again.
2. Add one new contact.
3. Save and exit.
4. Run app again.
5. List contacts.

Expected:

- Newly added contact is still there.
- IDs remain consistent and incrementing.

This proves data persists across runs.

#### Task 3: Verify missing-file safety

1. Delete `data.json`.
2. Run app.
3. List contacts.

Expected:

- App does **not** crash.
- App shows default contacts.
- Saving recreates `data.json`.

#### Task 4: Verify corrupted-file safety (operational acceptance)

1. Open `data.json` and break syntax, for example delete a quote or comma.
2. Save file.
3. Run app.

Expected:

- App prints warning about corrupted JSON (`JSONDecodeError` handling path).
- App does not crash.
- App uses default dataset.

This is now part of acceptance verification, not optional discussion.

#### Task 5: Save after changes

1. Add another contact.
2. Save and exit.
3. Reopen file and verify update.

Expected:

- New contact appears in file.
- Next run loads updated data.

### Instructor facilitation notes during lab

Walk the room (or breakout channels) with these quick checks:

- “Show me your `load_data` function. Do you catch both missing and corrupted cases?”
- “Show me where your save happens after changes.”
- “Can you demonstrate persistence with two runs?”
- “Can you explain `json.dump` vs `json.load` without reading your code?”

If students finish early, give extension tasks (below).

---

## Lab completion criteria (must be explicit)

Students are complete when all are true:

1. **Persistence works across runs**: data saved in one run appears in later runs.
2. **Missing file does not crash app**: handled gracefully with fallback data.
3. **Corrupted JSON does not crash app**: `json.JSONDecodeError` path is handled and app continues.
4. **After changes, data saves again**: modifications are written back to `data.json`.

Note: The runbook specifically requires no crash when file missing. This script also operationalizes corrupted-file handling to satisfy real-world robustness and your critique adjustment.

---

## Common pitfalls to watch for (and fixes)

### Pitfall 1: Trying to dump custom object directly

Symptom:

`TypeError: Object of type Contact is not JSON serializable`

Cause:

Custom Python object was passed directly to `json.dump`.

Fix:

Convert object to dictionary first:

```python
json.dump(contact.to_dict(), file, indent=2)
```

or for list of objects:

```python
json.dump([c.to_dict() for c in contacts], file, indent=2)
```

### Pitfall 2: Crashing when file doesn’t exist

Symptom:

`FileNotFoundError` on first run.

Cause:

Program assumes `data.json` already exists.

Fix:

Add `try/except FileNotFoundError` and return default data.

### Pitfall 3: Crashing on invalid JSON

Symptom:

`json.JSONDecodeError` when loading file.

Cause:

File was manually edited incorrectly or partially written.

Fix:

Catch `json.JSONDecodeError`, warn user, load fallback defaults.

### Pitfall 4: Forgetting to save after mutation

Symptom:

User adds contact, exits, data disappears.

Cause:

Changes happened in memory only; no save call executed.

Fix:

Call `save_data(...)` on explicit save/exit action (or after every write operation if desired).

### Pitfall 5: Confusing JSON booleans/null with Python values

Symptom:

Expecting `True` in JSON file, sees `true` instead.

Cause:

JSON has its own literal spellings.

Fix:

Explain conversion is automatic:

- Python `True` ↔ JSON `true`
- Python `None` ↔ JSON `null`

### Pitfall 6: Overbuilding beyond Basics

Symptom:

Student starts building complex serializer classes or database migration logic.

Cause:

Scope drift.

Fix:

Bring them back to hour outcomes: `dump/load`, supported types, simple `to_dict/from_dict`, safe file handling.

---

## Optional extensions (if time remains, still Basics scope)

These align to the runbook’s optional ideas and stay beginner-friendly.

### Extension A: Backup previous JSON before overwrite

Goal:

Before writing new data, save old file as `data.backup.json`.

Simple implementation:

```python
from pathlib import Path
import json

DATA_PATH = Path("data.json")
BACKUP_PATH = Path("data.backup.json")


def save_with_backup(path: Path, backup_path: Path, data: dict) -> None:
    if path.exists():
        backup_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        print("[INFO] Backup created at data.backup.json")

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
```

Teaching note: This is a practical safety net for accidental corruption.

### Extension B: Pretty print with `indent=2` everywhere

Goal:

Make JSON files easy for humans to inspect and debug.

Reminder:

```python
json.dump(data, file, indent=2)
```

If students used compact JSON, have them compare readability side by side.

---

## Simple object mapping mini-section (one class only, Basics level)

Use this if learners ask, “Can I save my class objects?”

```python
from dataclasses import dataclass


@dataclass
class Note:
    note_id: int
    text: str

    def to_dict(self) -> dict:
        return {
            "note_id": self.note_id,
            "text": self.text,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        return cls(
            note_id=int(data["note_id"]),
            text=str(data["text"]),
        )
```

Usage pattern:

```python
note = Note(note_id=1, text="Remember to persist data")
payload = note.to_dict()

loaded_note = Note.from_dict(payload)
```

Keep it here. Do not introduce custom encoders/decoders in this hour.

---

## Assessment and quick checks during instruction

Ask these short checks while teaching:

1. “What is the difference between `json.dump` and `json.load`?”
2. “Which Python types are safe to dump directly?”
3. “What exception do we catch for corrupted JSON?”
4. “Why do we need default data on first run?”
5. “If I add a contact but never save, what happens next run?”

Look for conceptual clarity, not memorized wording.

---

## Exit ticket (required quick check)

**Question:** Why can’t `json.dump()` write a custom object directly?

**Model answer:**
Because JSON only supports basic language-neutral data types (object, array, string, number, boolean, null). A custom Python object includes class-specific behavior and structure JSON does not understand. We must first convert the object to a JSON-compatible representation, usually a dictionary via `to_dict()`.

---

## Suggested speaking script (long-form, near-verbatim)

Use this if you want a tighter delivery script during class.

“Let’s make our programs remember. Right now, if we store data in a list or dictionary and then close the script, that data disappears. Variables live in memory, and memory is temporary. We need a persistence format, and for Basics, JSON is a perfect fit.

JSON is plain text. It is language-neutral, easy to read, and included in Python via the built-in `json` module. We don’t install anything. Two functions matter most today: `json.dump` to write Python data into a file, and `json.load` to read JSON from a file back into Python data.

When you hear ‘dump,’ think ‘write out.’ When you hear ‘load,’ think ‘read in.’

Now let’s connect Python types to JSON types. A Python `dict` maps to a JSON object. A Python list maps to a JSON array. Strings, numbers, booleans, and `None` map naturally too. One detail: if you dump a tuple, JSON stores it like an array, so when you load it back you get a list, not a tuple.

We also want readable files. If I use `indent=2`, the JSON file is pretty printed and easy to debug. That’s not required for machines, but great for people.

Now important real-world behavior: on first run, `data.json` might not exist. That is normal, not an error in your logic. So we catch `FileNotFoundError` and start from default data.

Second real-world behavior: files can be corrupted. Maybe someone edited manually and broke syntax, maybe a save was interrupted. When JSON is invalid, `json.load` raises `JSONDecodeError`. Our app should not crash. We catch that exception and recover with fallback defaults.

Now one common beginner confusion: ‘Why can’t I just dump my custom class object?’ Great question. JSON has no idea what your class is. It only understands basic, language-neutral structures. So we convert object to dictionary first using `to_dict`, and after loading we can rebuild the object with `from_dict`.

Our app flow today is simple and powerful: startup load, user changes data, save changes, next run restores state. If you can do this reliably, your projects become much more useful.

As we demo, watch for four anchors: what gets written, what gets loaded, where exceptions are handled, and where object mapping happens.”

After demo:

“Now your lab is to apply this workflow in a small contact app. If you don’t have a previous app, use the fallback starter dataset so everyone can complete the objective. Your checkoff is not only ‘it saves’ but also ‘it survives missing and corrupted files.’”

When circulating:

“Show me where your app decides fallback data. Show me where you save after mutation. Show me one run-to-run persistence proof.”

Wrap-up:

“Today is one of the biggest practical upgrades in the course. You moved from temporary scripts to stateful programs. Next time you build even a tiny app, you now have a durable data strategy.”

---

## Instructor troubleshooting guide for this hour

Use these fast fixes during lab support.

### Error: `TypeError: Object of type ... is not JSON serializable`

Ask:

- “Are you dumping a class instance directly?”

Fix:

- Convert with `to_dict()` first.

### Error: `JSONDecodeError`

Ask:

- “Can we open `data.json` and check commas, quotes, and brackets?”

Fix:

- restore from default data path in code
- optionally delete bad file and rerun

### Error: `FileNotFoundError` on load

Ask:

- “Do you have a `try/except` around your `json.load` call?”

Fix:

- catch file missing and return default dataset.

### Symptom: Data not persisting

Ask:

- “Where exactly do you call `save_data`?”

Fix:

- ensure save is called on exit or after write actions.

### Symptom: Data overwritten unexpectedly

Ask:

- “Are you always writing defaults at startup before load?”

Fix:

- load first, then only save after user changes (or explicit save action).

---

## Stretch discussion prompts (if class is ahead)

Stay in Basics while deepening thinking:

1. “What are tradeoffs of one `data.json` file versus multiple smaller files?”
2. “Would you save after every change or only on exit? Why?”
3. “If file corruption is detected, should we automatically overwrite, or ask user?”
4. “How might backup files reduce recovery risk?”

These prompts build design reasoning without adding advanced tooling.

---

## Recap (last 2–3 minutes)

Recap script:

“Today you learned JSON persistence using the standard library. You can now write Python data to disk with `json.dump`, read it back with `json.load`, and recover safely from missing and corrupted files. You also saw why custom objects need a dictionary mapping through `to_dict` and `from_dict`. In lab, you proved persistence across runs and no-crash behavior for missing files, plus graceful handling for invalid JSON. That is production-minded thinking at a Basics level.”

Quick final call:

- “Before you leave, run your app one more time and prove to yourself: add data, save, rerun, reload, verify.”

---

## Extended lab coaching script (use if learners need more structure)

If your group needs tighter scaffolding, run this guided sequence slowly and have everyone type each step. This section is still Basics-level and reinforces the same runbook requirements.

### Step-by-step coaching pass

**Step 1: Confirm startup load path**

Ask learners to point to exactly where `load_data(DATA_PATH)` is called.
Prompt:

- “Does your program load once at startup before the menu loop?”
- “If `data.json` is missing, what exact object do you return?”

Expected answer: a dictionary with keys like `next_id` and `contacts`.

**Step 2: Confirm safe fallback structure**

Many beginner bugs come from returning the wrong shape. If one student returns `[]` while the app expects a dict, later code fails.

Have learners print structure once:

```python
data = load_data(DATA_PATH)
print(type(data), data.keys())
```

Then remove debug print.

**Step 3: Confirm mutation in memory**

When adding a contact, ask:

- “Which line changes `data`?”
- “Which line increments `next_id`?”

If students create `new_contact` but forget to append, nothing persists.

**Step 4: Confirm explicit save timing**

Students often assume data auto-saves.
Ask:

- “When exactly is `save_data` called?”
- “Can your program exit without saving?”

In this lab, “Save and exit” is explicit, so they can reason about persistence behavior.

**Step 5: Run acceptance sequence live**

Have learners execute this exact acceptance script:

1. Delete `data.json`.
2. Start app.
3. List contacts (should show fallback defaults).
4. Add one contact named `Liam` with `liam@example.com`.
5. Save and exit.
6. Restart app.
7. List contacts (Liam should still exist).
8. Open `data.json`, remove a comma to corrupt JSON.
9. Start app again (should warn and recover, not crash).

This sequence operationalizes both runbook completion and resilience behavior.

### Common debugging dialogue you can use

When a student says, “It doesn’t work,” avoid immediately fixing it. Guide:

1. “What exactly happened versus what did you expect?”
2. “What was the last successful step?”
3. “What line threw the error?”
4. “What is the type of the value on that line?”
5. “What minimal change can we test next?”

This helps students learn process, not just patches.

### Three quick rescue patterns

**Rescue pattern A: Reset to known good default**

If a student app is heavily broken, have them:

- copy the baseline scaffold again
- run it once successfully
- re-add their custom changes one at a time

**Rescue pattern B: Validate JSON file directly**

If load keeps failing:

- open `data.json`
- verify brackets/braces/quotes/commas
- if uncertain, delete file and rerun to regenerate

**Rescue pattern C: Print before and after save**

```python
print("Before save:", data)
save_data(DATA_PATH, data)
```

Then inspect `data.json` and compare with print output.

### Instructor decision rule for pacing

If at least 70% of learners can:

- add a record
- save
- rerun and see persistence

then move into extension work.

If less than 70% can do this, pause and do a full-class re-demo of:

- load with exceptions
- one mutation
- save and rerun

Keep the class on core outcomes rather than optional polish.

---

## Reference snippets for board/slide use

### Minimal save

```python
import json

data = {"name": "Ava", "score": 100}
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
```

### Minimal load with resilience

```python
import json

try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"name": "Default User", "score": 0}
except json.JSONDecodeError:
    data = {"name": "Default User", "score": 0}
```

### Object mapping essentials

```python
class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name

    def to_dict(self) -> dict:
        return {"user_id": self.user_id, "name": self.name}

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(user_id=int(data["user_id"]), name=str(data["name"]))
```

---

## Final instructor checklist (use before ending hour)

- [ ] I explicitly stated both outcomes.
- [ ] I explained `json.dump` and `json.load` basics.
- [ ] I taught JSON-supported data types clearly.
- [ ] I showed one class with `to_dict/from_dict` only (no advanced serializer).
- [ ] I ran a live demo writing and loading `data.json`.
- [ ] I demonstrated missing-file handling.
- [ ] I demonstrated corrupted-file (`JSONDecodeError`) handling in practice.
- [ ] Students had a deterministic fallback mini-app dataset.
- [ ] Lab required load on startup and save after changes.
- [ ] Completion checks included persistence across runs and no crash when file missing.
- [ ] I asked the quick check: why custom objects cannot be dumped directly.

If all boxes are checked, this hour is aligned with runbook Hour 42 and classroom-ready.
