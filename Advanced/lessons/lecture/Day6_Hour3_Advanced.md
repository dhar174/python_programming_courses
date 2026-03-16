# Day 6 Hour 3 Advanced — GUI Mini-Project Sprint: Persistence and Polish

## Session context

This hour is the third block of **Session 6** in the Advanced Python full-stack tracker capstone. Learners now have a functional Tkinter GUI and, ideally, a cleaner `App` structure from Hour 2. The next milestone is to make the GUI feel like a real tool instead of a temporary demo.

The runbook outcome for this hour is clear: **add persistence and polish to the GUI milestone**. For this course, the default and recommended persistence target at this stage is **JSON save/load**, not SQLite yet. SQLite arrives in Session 7. Today’s goal is GUI readiness, predictable behavior, and user trust.

Emphasize this message repeatedly:

- JSON is not the final storage story of the capstone
- JSON is the right storage story for **this milestone** because it is transparent, portable, and quick to debug
- strong architecture today makes the future SQLite swap easier

Keep the neutral tracker framing so the examples fit tasks, inventory, contacts, notes, expenses, or similar domains.

---

## Learning objectives

By the end of this hour, learners should be able to:

1. Load tracker data from JSON when the app starts.
2. Save tracker data back to JSON after add, update, and delete operations.
3. Handle missing files and malformed JSON gracefully without crashing the GUI.
4. Add one or more small usability improvements such as a File menu, Help/About dialog, save shortcut, or status messages.
5. Explain why JSON is an appropriate persistence step before SQLite in the capstone sequence.
6. Prepare a GUI milestone that can be demonstrated confidently in the checkpoint hour.

---

## Prerequisites and starting assumptions

Learners should already have:

- a Tkinter GUI with add/update/delete wired through a service layer
- a stable record ID system
- an `App` or equivalent structure that can reasonably absorb persistence hooks
- familiarity with JSON from earlier course work or Basics-level file handling

If some learners still have a messier structure, that is okay. Persistence can still be added, but instructors should steer them toward clean boundaries:

- the UI should trigger save/load
- the service layer should define what item data looks like
- a dedicated storage function or class should manage JSON format details

---

## Materials and setup

- a working tracker project
- a writable project folder
- optional seed data in a JSON file
- sample malformed JSON file for error-path demonstration
- projector visible enough to show app restart and file contents side by side

Recommended pre-class setup:

- have one valid JSON file ready
- have one invalid JSON file ready, such as a missing comma or truncated structure
- pre-populate a few tracker items for faster demos

---

## Section navigation

1. Why persistence matters for user trust
2. Why JSON is the right milestone now
3. Designing a simple JSON storage layer
4. Load on startup, save after CRUD
5. Graceful file and JSON error handling
6. Usability polish: menus, About, shortcuts, status messages
7. Sprint lab with minimum and stretch goals
8. Debrief and checkpoint preparation

---

## Suggested timing

- **0–10 min:** motivation and persistence architecture
- **10–25 min:** live demo of load/save behavior and error handling
- **25–35 min:** add polish features in demo
- **35–55 min:** mini-project sprint
- **55–60 min:** debrief and checkpoint prep for Hour 4

---

## Instructor speaking script

### 1) Opening: why persistence changes the feel of an app

**Say:** “Until now, if we close the tracker, the data disappears unless we have manually preserved it somewhere else. That is fine for learning widget wiring, but it is not fine for a usable tool. Persistence is the moment the app starts earning user trust.”

Ask:

- “Would you use an expense tracker if every restart erased your data?”
- “Would you trust an inventory tool that forgot updates after closing?”

Expected answer: no.

**Say:** “So today’s work is not cosmetic. Persistence is core behavior. But we are choosing a persistence approach that matches the current stage of the course.”

### 2) Why JSON now instead of SQLite now

The runbook and user instructions both emphasize JSON for this hour and SQLite later. Make that reasoning explicit.

**Say:** “Could we jump straight to SQLite? Yes, eventually. But that would overload this checkpoint. Today we want the GUI milestone to demonstrate reliable load/save behavior with a format learners can inspect directly. JSON is excellent for that.”

Benefits to name aloud:

- human-readable
- easy to inspect in the editor
- portable between machines
- no separate database setup step
- good for demonstrating serialization and recovery from file errors

Also name the limitation honestly:

- JSON is not ideal for concurrent editing, large datasets, or rich querying
- that is why SQLite comes next session

This is a strong place to reinforce sequencing as a professional skill.

**Say:** “Good engineers do not always start with the most powerful solution. They start with the solution that best fits the milestone.”

### 3) Storage design options

You have two reasonable teaching options here:

1. simple service methods `load_from_json()` and `save_to_json()`
2. a separate `JsonTrackerStore` helper class

Because the capstone architecture emphasizes a service layer, recommend either:

- UI calls `service.load_from_json(path)` / `service.save_to_json(path)`
- or UI calls a store, and the service manages conversion

For most classrooms, keeping JSON handling close to the service is the fastest path. If you want stronger separation, introduce a dedicated storage helper but keep it simple.

### 4) Example: service-side JSON persistence

Show a concrete implementation using modern Python patterns.

```python
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path


class StorageError(Exception):
    pass


class TrackerService:
    def __init__(self) -> None:
        self._items: list[TrackerItem] = []

    # ... existing CRUD methods ...

    def save_to_json(self, file_path: Path) -> None:
        data = [asdict(item) for item in self._items]
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except OSError as error:
            raise StorageError(f"Unable to save tracker data: {error}") from error

    def load_from_json(self, file_path: Path) -> None:
        if not file_path.exists():
            self._items = []
            return

        try:
            raw_text = file_path.read_text(encoding="utf-8")
            raw_items = json.loads(raw_text)
        except json.JSONDecodeError as error:
            raise StorageError(f"The data file is not valid JSON: {error}") from error
        except OSError as error:
            raise StorageError(f"Unable to read tracker data: {error}") from error

        loaded_items: list[TrackerItem] = []
        for raw_item in raw_items:
            loaded_items.append(
                TrackerItem(
                    item_id=raw_item["item_id"],
                    name=raw_item["name"],
                    category=raw_item["category"],
                    status=raw_item["status"],
                    notes=raw_item.get("notes", ""),
                )
            )
        self._items = loaded_items
```

Pause and point out the important ideas:

- `Path` from `pathlib`, not raw string paths everywhere
- JSON serialization done from the service’s current source of truth
- file missing is not treated as a crash-worthy event
- invalid JSON raises a custom storage-focused error with a clear message

### 5) Load on startup

Show where startup load belongs. If learners refactored to an `App` class, the constructor is the natural place.

```python
from pathlib import Path
from tkinter import messagebox


class TrackerApp:
    def __init__(self, root: tk.Tk, service: TrackerService) -> None:
        self.root = root
        self.service = service
        self.data_file = Path("data/tracker_items.json")
        self.selected_item_id: str | None = None
        self.status_text = tk.StringVar(value="Ready")
        self.name_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.build_ui()
        self.load_data_on_startup()
        self.refresh_items()

    def load_data_on_startup(self) -> None:
        try:
            self.service.load_from_json(self.data_file)
        except StorageError as error:
            messagebox.showerror("Load Error", str(error))
            self.set_status("Started with empty data due to load error")
            return

        self.set_status(f"Loaded {len(self.service.list_items())} items")
```

Discuss the user experience choice here. If the JSON file is missing, that is normal for a first run. If it is corrupted, that deserves a clear message.

### 6) Save after each CRUD operation

This is a key runbook point. State it explicitly.

**Say:** “A common bug is saving only after add, but forgetting to save after update or delete. That creates a mismatch between what the user sees now and what will still exist after restart. Save-after-change must apply consistently across CRUD operations.”

Show a helper method rather than repeating save logic in three callbacks.

```python
def persist_changes(self) -> bool:
    try:
        self.service.save_to_json(self.data_file)
    except StorageError as error:
        messagebox.showerror("Save Error", str(error))
        self.set_status("Save failed")
        return False

    self.set_status("Changes saved")
    return True
```

Then show how callbacks use it.

```python
def on_add(self) -> None:
    try:
        item = self.service.add_item(**self.get_form_data())
    except ValidationError as error:
        messagebox.showerror("Validation Error", str(error))
        return

    self.persist_changes()
    self.refresh_items(selected_item_id=item.item_id)
    self.clear_form(keep_status=True)


def on_update(self) -> None:
    if self.selected_item_id is None:
        messagebox.showwarning("No Selection", "Select a record to update.")
        return

    try:
        item = self.service.update_item(self.selected_item_id, **self.get_form_data())
    except (ValidationError, NotFoundError) as error:
        messagebox.showerror("Update Error", str(error))
        return

    self.persist_changes()
    self.refresh_items(selected_item_id=item.item_id)


def on_delete(self) -> None:
    if self.selected_item_id is None:
        messagebox.showwarning("No Selection", "Select a record to delete.")
        return

    try:
        item = self.service.get_item(self.selected_item_id)
    except NotFoundError as error:
        messagebox.showerror("Delete Error", str(error))
        return

    confirmed = messagebox.askyesno("Confirm Delete", f"Delete '{item.name}'?")
    if not confirmed:
        return

    self.service.delete_item(item.item_id)
    self.persist_changes()
    self.refresh_items()
    self.clear_form(keep_status=True)
    self.selected_item_id = None
```

Narrate the pattern repeatedly:

- do the domain action
- persist the current truth
- refresh the interface
- give feedback

### 7) Graceful handling of malformed JSON

This part matters because the runbook explicitly calls out file/JSON problems.

**Say:** “What should happen if the data file is corrupted? The wrong answer is a traceback and a dead app. The better answer is: explain the problem, avoid crashing, and let the user recover.”

You may choose one of these instructor-approved recovery strategies:

- start with empty data and show an error message
- offer to back up the bad file and continue
- block normal work until the file is fixed, if the class is ready for that discussion

For this milestone, the simplest is:

- show an error dialog
- keep the app open
- continue with an empty list or previously loaded in-memory state

### 8) A dedicated JSON store helper, if you want stronger separation

If your class is moving quickly, briefly show the storage-helper version.

```python
class JsonTrackerStore:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def save_items(self, items: list[TrackerItem]) -> None:
        payload = [asdict(item) for item in items]
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load_items(self) -> list[TrackerItem]:
        if not self.file_path.exists():
            return []
        raw_items = json.loads(self.file_path.read_text(encoding="utf-8"))
        return [TrackerItem(**raw_item) for raw_item in raw_items]
```

Then tell learners they do not need this extra class unless they are comfortable. The checkpoint does not require abstraction for its own sake.

### 9) Usability polish: turn the demo into a tool

The runbook suggests menu items, a help dialog, or keyboard shortcuts. Present these as small but meaningful touches.

**Say:** “Polish is not decoration. Polish is what helps users understand and trust the application.”

Suggested polish options:

- **File menu** with Save, Export, Exit
- **Help menu** with About
- **status bar** showing last action
- **keyboard shortcut** such as `Ctrl+S`
- **clear form** button
- more informative window title
- default focus placement on startup

Show a small menu example.

```python
def build_menu(self) -> None:
    menubar = tk.Menu(self.root)

    file_menu = tk.Menu(menubar, tearoff=False)
    file_menu.add_command(label="Save", command=self.persist_changes, accelerator="Ctrl+S")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    help_menu = tk.Menu(menubar, tearoff=False)
    help_menu.add_command(label="About", command=self.show_about)
    menubar.add_cascade(label="Help", menu=help_menu)

    self.root.config(menu=menubar)
    self.root.bind("<Control-s>", lambda event: self.persist_changes())


def show_about(self) -> None:
    messagebox.showinfo(
        "About",
        "Full-Stack Tracker
Tkinter milestone with JSON persistence."
    )
```

### 10) Optional export-to-CSV teaser

The runbook lists export-to-CSV as an optional extension. Mention it as future-friendly and relevant for analytics.

**Say:** “If you have fast finishers, a small CSV export button is an excellent extension because it connects today’s GUI work to the later analytics session. But it is optional. Persistence comes first.”

### 11) Live demo plan

#### Demo A: successful load/save cycle

1. Start with the app closed.
2. Show the JSON file contents in the editor if it already exists.
3. Launch the app.
4. Narrate startup load.
5. Add a record.
6. Update a record.
7. Delete a record.
8. Close the app.
9. Re-open the JSON file and point out the saved structure.
10. Restart the app and show the same data loaded.

Narration prompt:

**Say:** “The app is now preserving state across runs. That is a major milestone in user trust.”

#### Demo B: malformed JSON path

1. Intentionally break the JSON file.
2. Launch the app.
3. Show the error dialog.
4. Explain why the app does not simply crash.

Narration prompt:

**Say:** “Graceful failure is part of usability. Users remember whether software helped them recover.”

#### Demo C: polish feature

Show one quick feature such as Ctrl+S, About dialog, or a status bar.

**Say:** “These details matter because they teach the user what the application is doing.”

### 12) Sprint instructions for learners

Read or paste the following:

#### Lab: GUI Milestone Sprint — Persistence and Polish

Bring your tracker to a checkpoint-ready state.

##### Required tasks

- Load records from JSON on app startup.
- Save records to JSON after add, update, and delete.
- Handle a missing data file without crashing.
- Handle invalid JSON with a clear error message.
- Add at least one usability improvement.

##### Choose at least one polish feature

- File menu with Save and Exit
- Help/About dialog
- status bar message for last action
- Ctrl+S save shortcut
- Clear Form button
- better empty-state or no-selection messaging

##### Minimum definition of done

- data persists across app restarts
- user feedback is understandable
- no obvious crash during normal use
- code remains organized enough to explain during the checkpoint

##### Stretch goals

- export current records to CSV
- confirm on app close if there are unsaved changes
- hide the ID column visually while still using it internally
- add automatic backup file creation when JSON load fails

### 13) Instructor circulation notes

While learners work, ask these questions:

- “When exactly does your app load data?”
- “When exactly does your app save data?”
- “What happens if the JSON file is missing?”
- “What happens if the JSON file is invalid?”
- “What polish feature did you choose, and why does it help the user?”

If a learner’s data file keeps getting corrupted, check for common causes:

- writing partial JSON because of manual string building instead of `json.dumps`
- writing unsupported objects directly instead of converting dataclasses to dictionaries
- not encoding/decoding consistently with UTF-8
- forgetting to strip trailing whitespace in notes fields only if their logic depends on exact comparisons

### 14) Why design choices matter

Use this hour to make a larger point about software design.

**Say:** “The architecture matters because persistence magnifies sloppy design. If your GUI is the only place that knows how records are structured, save/load becomes awkward. If your service layer already owns that model cleanly, persistence becomes an addition, not a rewrite.”

**Say:** “Also remember that JSON is transparent. If something goes wrong, you can inspect the file. That makes today’s milestone excellent for learning because the system state is visible.”

---

## Common pitfalls to watch for

### Pitfall 1: saving after add, but not after update/delete

This is the most common persistence bug for this hour. Tie it directly to user trust.

### Pitfall 2: crashing on malformed JSON

Some learners will call `json.loads` without exception handling. Use this as a teaching moment about graceful failure.

### Pitfall 3: saving UI-only state instead of domain state

Encourage learners to serialize the actual tracker items, not widget objects or temporary screen details.

### Pitfall 4: storing records without stable IDs

If IDs are recreated on every load, updates later become unreliable. The saved JSON must preserve the existing `item_id`.

### Pitfall 5: adding too many polish features before persistence is solid

Remind the room that a stylish app that loses data is still a failed milestone.

---

## Completion criteria for this hour

Learners are ready for the checkpoint if they can demonstrate:

- load from JSON on startup
- save after add/update/delete
- restart the app and show data persists
- handle at least one error path without crashing
- describe at least one usability improvement they added

If time is short, prioritize in this order:

1. load on startup
2. save after every CRUD change
3. clear user-facing error handling
4. one polish feature

---

## Quick check / exit ticket

Ask learners:

1. Why is JSON the preferred persistence target for this GUI milestone?
2. What must happen after update and delete to keep persistence trustworthy?
3. What should the app do if the JSON file exists but is malformed?
4. What usability improvement did you add, and why does it matter?

A strong answer to question 1 sounds like:

> “JSON is a good checkpoint choice because it is simple, readable, portable, and easy to debug while we focus on GUI readiness before moving to SQLite.”

---

## Preparing learners for Hour 4

End this hour by giving learners a clear picture of the checkpoint.

**Say:** “In the next hour, you are not being asked for a perfect product. You are being asked to show a reliable milestone. That means your GUI launches, CRUD works through the UI, persistence survives restart, and you can explain your code organization. Use the last few minutes now to make sure your demo path is smooth: add, update, delete, restart, reload.”


---

## Extended teaching notes: persistence design, usability, and checkpoint readiness

This section gives instructors more depth for classes that need stronger explanation or additional guided practice.

### A simple mental model for persistence

Use this sentence repeatedly:

**Say:** “Persistence means the app remembers the truth after the program stops running.”

Then map that idea to the tracker.

- in memory, records exist only while the process runs
- in JSON, records survive process restarts
- later, in SQLite, records survive with stronger query and integrity capabilities

This model helps learners see persistence as a behavior of the application rather than just a file-format trick.

### Why stable IDs must survive save and load

A subtle but important point for this hour is that the saved data must preserve record identity. Explain it directly.

**Say:** “If an item gets a new ID every time the app loads, then the app has lost continuity. Updates, selections, and future database mapping become much harder. Persistence is not only about saving field values. It is about saving identity.”

Ask learners:

- “What would happen if you exported only name, category, and status but regenerated IDs on each load?”

Good answers:

- previously selected references would no longer match
- future synchronization becomes confusing
- history or relationships become impossible to track reliably

### Suggested JSON shape for the milestone

Show learners that the JSON file should be plain and boring. Boring is good here.

```json
[
  {
    "item_id": "c09b1d33-f0b4-4d10-a12f-1cb8d4317bd1",
    "name": "Prepare weekly report",
    "category": "Work",
    "status": "In Progress",
    "notes": "Need updated totals before Friday"
  },
  {
    "item_id": "63dfa576-2cc1-4589-bf5d-fefde55ea53b",
    "name": "Call supplier",
    "category": "Operations",
    "status": "Open",
    "notes": "Confirm next shipment window"
  }
]
```

Explain why this structure is useful:

- easy to inspect manually
- easy to iterate over when loading
- easy to convert from dataclasses using `asdict`
- future-friendly for migration into tabular storage

### Autosave versus explicit save

Learners may ask whether auto-save or manual save is better. Use that as a design discussion.

**Say:** “For this checkpoint, either explicit save or save-after-change is acceptable if it is clear and reliable. Because the runbook emphasizes saving after CRUD, auto-save after add/update/delete is the most straightforward classroom pattern.”

Name the trade-offs clearly.

**Auto-save advantages**

- fewer forgotten saves
- simpler demo path
- closer to user expectations for many small tools

**Explicit save advantages**

- easier to reason about when writes happen
- opens the door to unsaved-change prompts later

For this milestone, recommend auto-save after CRUD unless learners have a strong reason to do otherwise.

### Error-handling philosophy for file-based apps

Teach a three-part recovery mindset:

1. detect the problem
2. explain the problem in user language
3. move to a safe state

That gives instructors a clean way to evaluate malformed JSON behavior. The student does not need a perfect recovery wizard. They need a reasonable recovery path.

### Usability polish that supports learning goals

If learners finish persistence early, guide them toward polish that teaches durable habits, not random decoration.

Strong polish tasks:

- a status bar that reports “Loaded 6 items,” “Saved changes,” or “Deleted record”
- a disabled Update/Delete button when nothing is selected
- focus returning to the first form field after Add
- a help/about dialog with app purpose and version
- a File menu that mirrors visible actions

Less valuable polish at this stage:

- visual themes that consume the whole hour
- deeply custom styling
- animation or unusual widget behavior unrelated to the checkpoint

**Say:** “Polish should clarify behavior, not distract from reliability.”

---

## Sprint support: checkpoints you can call out during lab time

If the room needs more structure, pause at these time markers.

### Sprint checkpoint 1: load works

Ask learners to show you one of these:

- app starts with existing data visible
- app starts empty without crashing when the file does not exist

### Sprint checkpoint 2: save works for add/update/delete

Ask learners:

- “Which method is responsible for persistence?”
- “How many callbacks call it?”
- “Did you remember update and delete?”

### Sprint checkpoint 3: restart proof

Ask learners to close and relaunch the app, not just inspect the JSON file. The real user experience is restart, not a file viewer.

### Sprint checkpoint 4: one polish feature

Ask learners to demo the feature and explain the benefit to the user in one sentence.

This keeps the hour moving toward the checkpoint rather than toward endless “just one more feature” drift.

---

## Troubleshooting guide for common persistence issues

### Symptom: JSON file writes, but load fails later

Possible causes:

- malformed manual JSON string construction
- missing required keys
- notes or text values not encoded consistently
- partial file writes caused by experimental save logic

Fix guidance:

- use `json.dumps` instead of building JSON strings by hand
- verify each saved item includes `item_id`, `name`, `category`, and `status`
- inspect the file immediately after save

### Symptom: records save, but IDs change after restart

Possible causes:

- learner recreates each item with a factory that always generates a new UUID
- load path ignores the stored `item_id`

Instructional language:

**Say:** “When loading existing data, we are reconstructing identity, not creating a fresh record. That means we must reuse the stored ID.”

### Symptom: app crashes if the `data/` folder does not exist

Possible cause:

- save method writes directly without creating parent directories

Fix guidance:

- use `file_path.parent.mkdir(parents=True, exist_ok=True)` before writing

### Symptom: save appears to work, but the app restarts empty

Possible causes:

- save path and load path are different
- relative path confusion based on current working directory
- save only happens on explicit button press, but the learner forgot to press it

What to ask:

- “Can you print the path used for save and the path used for load?”
- “Are they the same file?”

### Symptom: malformed JSON path is handled, but the app silently wipes the file

Possible cause:

- learner responds to load error by immediately overwriting with empty data

Teaching point:

**Say:** “Recovering from a bad file should not destroy evidence. At minimum, inform the user before replacing anything.”

---

## Checkpoint-prep script for the final five minutes

Use this script to help learners organize their Hour 4 demo.

**Say:** “Before we end this hour, I want you to rehearse your checkpoint path mentally. You should know exactly which record you will add, which one you will update, and how you will prove persistence.”

Ask learners to prepare these items:

1. one clean sample record to add
2. one existing record to edit
3. one record safe to delete
4. a sentence explaining where the service layer lives
5. a sentence explaining how the app tracks the correct record ID

Then say:

**Say:** “If your demo depends on luck, it is not ready. If your demo depends on a predictable path you have practiced once or twice, you are in a strong position.”

### Suggested learner self-check before checkpoint

- Can I launch the app without last-minute edits?
- Do add, update, and delete all trigger save behavior?
- Can I close and reopen the app without losing data?
- If no record is selected, does my app handle that calmly?
- Can I explain my architecture in 30 seconds?

That self-check often prevents avoidable checkpoint stumbles.
