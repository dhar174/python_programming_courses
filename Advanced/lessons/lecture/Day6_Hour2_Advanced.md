# Day 6 Hour 2 Advanced — GUI Architecture: Controller Separation and Avoiding Callback Spaghetti

## Session context

This hour continues **Session 6** of the Advanced Python full-stack tracker capstone. In Hour 1, learners wired update and delete into a functioning GUI. That is excellent progress, but working code is not automatically maintainable code. Once an application has a form, a list, add/update/delete actions, status messages, and save/load hooks, the GUI can become tangled fast.

This hour is about architecture. The practical goal is to help learners refactor their Tkinter application so the code still makes sense one week from now, not just five minutes after it first ran.

The architectural stance for this course remains consistent:

- **widgets and event hooks belong to the UI layer**
- **business rules belong to the service layer**
- **the App/controller coordinates user actions**
- **stable IDs remain the bridge between UI selection and domain operations**

Keep the full-stack tracker framing neutral so it applies to tasks, inventory, contacts, notes, expenses, or similar domains.

---

## Learning objectives

By the end of this hour, learners should be able to:

1. Recognize the signs of “callback spaghetti” in a growing GUI codebase.
2. Explain the responsibilities of a Tkinter `App` or controller class.
3. Refactor a GUI so widget construction, event handling, and service calls are organized cleanly.
4. Keep callbacks thin by passing validated input to a service layer rather than embedding business logic in the UI.
5. Manage basic app state clearly, especially current selection and status messaging.
6. Avoid common refactor hazards such as circular imports and “change everything at once.”

---

## Prerequisites and starting assumptions

Learners should already have:

- a working Tkinter tracker GUI
- add/update/delete functionality connected to a service layer or at least to in-memory logic
- a stable record ID system
- enough confidence with classes and modules to move code between files

If some learners are still finishing Hour 1, tell them the minimum goal for Hour 2 is not perfection. It is to move from a pile of widget references and loose functions toward a clearer program structure.

---

## Materials and setup

- current tracker project open in the IDE
- a version of the GUI that still uses several top-level functions or global widget references
- projector view wide enough to show two files side by side if possible
- optional whiteboard diagram of layers: `ui -> service -> model`

---

## Section navigation

1. Why working GUIs become messy
2. What “callback spaghetti” looks like
3. The target architecture for this capstone
4. Refactoring into an `App` controller class
5. Keeping state and selection clean
6. Module boundaries and imports
7. Lab: refactor without breaking behavior
8. Debrief and quality checks

---

## Suggested timing

- **0–8 min:** recap and why maintainability matters
- **8–20 min:** identify callback spaghetti symptoms
- **20–35 min:** live refactor into an `App` class
- **35–50 min:** guided lab
- **50–60 min:** debrief, quick check, and transition to persistence in Hour 3

---

## Instructor speaking script

### 1) Opening: working is not the finish line

**Say:** “A lot of students reach a moment in GUI work where the program technically works, but they are afraid to touch it. If adding one button means editing six scattered functions, the problem is no longer Tkinter. The problem is structure.”

**Say:** “Today’s theme is maintainability. The question is not just ‘Can the app update and delete?’ The question is ‘Can we still understand the app when we add persistence, menus, keyboard shortcuts, and later a database?’”

Invite reflection:

- “Has anyone ever had code that worked yesterday and felt impossible to safely change today?”
- “What signs made it feel fragile?”

Use learner responses to introduce the phrase **callback spaghetti**.

### 2) What callback spaghetti looks like

Define it in plain language.

**Say:** “Callback spaghetti is what happens when GUI behavior is spread across too many disconnected functions, often with shared globals, repeated widget access, duplicated validation, and hidden state. You can still make progress for a while, but each new feature gets harder.”

List common symptoms on screen or board:

- many top-level functions with unclear ownership
- globals for widgets such as `name_entry`, `tree`, `status_label`
- duplicate code to gather form values in several handlers
- duplicate code to refresh the list after each action
- business rules embedded directly in callbacks
- mysterious bugs caused by stale selection state
- hard-to-test code because logic is fused to UI objects

Now contrast that with a healthy small GUI architecture.

### 3) The target structure for this capstone

Show a simple conceptual diagram:

- **model/domain**: `TrackerItem`, exceptions, possibly validators
- **service**: add, update, delete, list, get by ID, later save/load or repository use
- **UI/App class**: builds widgets, reads input, calls service methods, refreshes display, shows messages

**Say:** “The App or controller class is not the business brain of the program. It is the coordinator of user interaction. When a user clicks a button, the App collects input, calls the service, and updates the screen. That is enough responsibility for one class.”

Explain why this matters for future sessions:

- when JSON persistence arrives, the service can grow without turning the UI into a storage engine
- when SQLite arrives, the service can swap storage details while the UI mostly stays stable
- when testing arrives, core logic in the service is easier to test than button callbacks

### 4) A quick ‘before’ example

Show a small intentionally messy example. Read it with humor, not shame.

```python
service = TrackerService()
selected_item_id = None


def add_item():
    name = name_entry.get()
    category = category_entry.get()
    status = status_combo.get()
    notes = notes_text.get("1.0", "end").strip()
    item = service.add_item(name, category, status, notes)
    refresh_tree()
    status_label.config(text=f"Added {item.name}")


def update_item():
    global selected_item_id
    name = name_entry.get()
    category = category_entry.get()
    status = status_combo.get()
    notes = notes_text.get("1.0", "end").strip()
    service.update_item(selected_item_id, name, category, status, notes)
    refresh_tree()
    status_label.config(text="Updated item")


def delete_item():
    global selected_item_id
    service.delete_item(selected_item_id)
    refresh_tree()
    clear_form()
```

Ask learners what feels risky.

Expected observations:

- lots of global state
- repeated form extraction logic
- unclear error handling
- callbacks know too much
- no clear owner of widgets or app state

### 5) Refactoring goal: a single `App` class owns the GUI

**Say:** “We are not refactoring for elegance points. We are refactoring to reduce confusion. A practical step is to create one `TrackerApp` class that owns widget references, current selection, and event handlers.”

A helpful definition:

- the `App` class **builds the UI**
- the `App` class **responds to events**
- the `App` class **asks the service layer to perform operations**
- the `App` class **refreshes the display**
- the `App` class **does not become the database, validator, or domain model**

### 6) Suggested file structure

You can keep everything in one file for a small demo, but show the class-ready direction.

```text
advanced_tracker/
    main.py
    core/
        models.py
        service.py
        exceptions.py
    ui/
        app.py
```

If learners are not ready for multiple modules, keep the same conceptual separation inside one file and tell them the split can come later.

### 7) Live refactor: build the `TrackerApp` shell first

Narrate this slowly.

```python
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox

from core.exceptions import NotFoundError, ValidationError
from core.service import TrackerService


class TrackerApp:
    def __init__(self, root: tk.Tk, service: TrackerService) -> None:
        self.root = root
        self.service = service
        self.selected_item_id: str | None = None
        self.status_text = tk.StringVar(value="Ready")
        self.name_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.status_var = tk.StringVar()

        self.root.title("Full-Stack Tracker")
        self.build_ui()
        self.refresh_items()

    def build_ui(self) -> None:
        # widget creation lives here
        pass
```

**Say:** “This constructor creates application-level state and then hands off UI construction to a dedicated method. That gives us a clean entry point and a clean place to look when we need to change the screen.”

### 8) Refactor widget creation into `build_ui()`

Explain the principle while coding: put widget creation in one place and behavior in named methods.

```python
def build_ui(self) -> None:
    main_frame = ttk.Frame(self.root, padding=12)
    main_frame.grid(row=0, column=0, sticky="nsew")

    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(5, weight=1)

    ttk.Label(main_frame, text="Name").grid(row=0, column=0, sticky="w")
    ttk.Entry(main_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, sticky="ew")

    ttk.Label(main_frame, text="Category").grid(row=1, column=0, sticky="w")
    ttk.Entry(main_frame, textvariable=self.category_var, width=30).grid(row=1, column=1, sticky="ew")

    ttk.Label(main_frame, text="Status").grid(row=2, column=0, sticky="w")
    self.status_combo = ttk.Combobox(
        main_frame,
        textvariable=self.status_var,
        values=["Open", "In Progress", "Done"],
        state="readonly",
    )
    self.status_combo.grid(row=2, column=1, sticky="ew")

    ttk.Label(main_frame, text="Notes").grid(row=3, column=0, sticky="nw")
    self.notes_text = tk.Text(main_frame, width=40, height=5)
    self.notes_text.grid(row=3, column=1, sticky="ew")

    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 8))

    ttk.Button(button_frame, text="Add", command=self.on_add).grid(row=0, column=0, padx=(0, 8))
    ttk.Button(button_frame, text="Update", command=self.on_update).grid(row=0, column=1, padx=(0, 8))
    ttk.Button(button_frame, text="Delete", command=self.on_delete).grid(row=0, column=2, padx=(0, 8))
    ttk.Button(button_frame, text="Clear Form", command=self.clear_form).grid(row=0, column=3)

    self.tree = ttk.Treeview(
        main_frame,
        columns=("id", "name", "category", "status"),
        show="headings",
        height=10,
    )
    self.tree.grid(row=5, column=0, columnspan=2, sticky="nsew")
    self.tree.heading("id", text="ID")
    self.tree.heading("name", text="Name")
    self.tree.heading("category", text="Category")
    self.tree.heading("status", text="Status")
    self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)

    ttk.Label(main_frame, textvariable=self.status_text).grid(row=6, column=0, columnspan=2, sticky="ew", pady=(8, 0))
```

Point out the benefit: every widget reference owned by the GUI now lives on `self`, making behavior methods easier to read.

### 9) Thin callbacks as methods

Refactor one callback at a time. Stress behavior preservation.

**Say:** “A refactor should not change what the user can do. It should change how understandable the code is.”

Example `on_add` method:

```python
def on_add(self) -> None:
    try:
        item = self.service.add_item(**self.get_form_data())
    except ValidationError as error:
        messagebox.showerror("Validation Error", str(error))
        return

    self.refresh_items(selected_item_id=item.item_id)
    self.set_status(f"Added: {item.name}")
    self.clear_form(keep_status=True)
```

Example helper used by several callbacks:

```python
def get_form_data(self) -> dict[str, str]:
    return {
        "name": self.name_var.get(),
        "category": self.category_var.get(),
        "status": self.status_var.get(),
        "notes": self.notes_text.get("1.0", tk.END).strip(),
    }
```

**Say:** “Notice what just happened. We removed duplicated form-reading logic from multiple callbacks. That is one of the quickest ways to reduce GUI mess.”

### 10) State management: selection and status

Explain that not all state is bad. Hidden, unmanaged state is bad. Cleanly named app state is useful.

Recommended app state examples:

- `self.selected_item_id`
- `self.status_text`
- form variables such as `self.name_var`

Bad hidden state examples:

- relying on whatever tree row happens to still exist after refresh
- using global variables changed from multiple functions
- leaving form fields populated without knowing which record they map to

Show a clear selection handler:

```python
def on_item_selected(self, event: tk.Event | None = None) -> None:
    selection = self.tree.selection()
    if not selection:
        self.selected_item_id = None
        return

    values = self.tree.item(selection[0], "values")
    item_id = values[0]

    try:
        item = self.service.get_item(item_id)
    except NotFoundError as error:
        messagebox.showerror("Selection Error", str(error))
        self.refresh_items()
        self.clear_form()
        self.selected_item_id = None
        return

    self.selected_item_id = item.item_id
    self.name_var.set(item.name)
    self.category_var.set(item.category)
    self.status_var.set(item.status)
    self.notes_text.delete("1.0", tk.END)
    self.notes_text.insert("1.0", item.notes)
    self.set_status(f"Editing: {item.name}")
```

### 11) A healthy `refresh_items()` method

Refactor list rebuilding into one place. This is the kind of method that pays off repeatedly.

```python
def refresh_items(self, selected_item_id: str | None = None) -> None:
    for row_id in self.tree.get_children():
        self.tree.delete(row_id)

    for item in self.service.list_items():
        row_id = self.tree.insert(
            "",
            tk.END,
            values=(item.item_id, item.name, item.category, item.status),
        )
        if selected_item_id == item.item_id:
            self.tree.selection_set(row_id)
            self.tree.focus(row_id)
```

**Say:** “Any code path that changes the underlying data can now call one refresh method. That centralizes list logic and reduces bugs.”

### 12) Circular imports and module boundaries

The runbook warns about circular imports. Explain what that means in a friendly way.

**Say:** “A circular import happens when module A imports module B and module B also imports module A. GUI projects are especially vulnerable when UI code starts reaching deeply into the core, and the core also tries to import the UI.”

Practical rule for this course:

- `main.py` can assemble the app
- `ui/app.py` can import the service and exceptions
- `core/service.py` should **not** import the UI

That direction of dependency keeps the architecture cleaner.

### 13) Refactor strategy: do not rebuild the plane midair

Students often over-refactor. Give them a concrete safe method.

**Say:** “Move one piece, run the app, then move the next piece. Don’t rewrite the whole GUI from scratch because you ‘see the better version in your head.’ That is how working features disappear.”

Recommended sequence:

1. create the `App` class shell
2. move widget references into `build_ui()`
3. move one callback, such as add
4. test
5. move refresh helper
6. test
7. move update/delete/selection handlers
8. test
9. only then split modules if desired

### 14) Live demo plan

#### Demo A: identify code smells

Open a messy version and narrate what feels hard to trust.

**Say:** “I can make this work, but I cannot answer simple questions quickly, like ‘Who owns the current selection?’ or ‘Where do all service calls happen?’ That is a structural problem.”

#### Demo B: create `TrackerApp`

Move just enough to get the app launching. Show that the window still opens. Celebrate the small checkpoint.

#### Demo C: move one callback and test immediately

Use Add first because it is usually the simplest. Then show Update and Delete still pending. This models safe refactoring.

#### Demo D: finish the refactor and compare readability

At the end, scroll through the new class and point out that the code now reads like a table of contents:

- `build_ui`
- `get_form_data`
- `clear_form`
- `refresh_items`
- `on_add`
- `on_update`
- `on_delete`
- `on_item_selected`
- `set_status`

**Say:** “That list of methods tells the story of the app. Good structure often looks like clear storytelling.”

### 15) Practice lab script

Read or paste this to learners:

#### Lab: Refactor the GUI Without Breaking Behavior

Refactor your tracker so the GUI has a clear owner and the callbacks remain thin.

##### Required tasks

- Create an `App` or `TrackerApp` class that builds the interface.
- Move widget references into the class.
- Move event handlers into methods on the class.
- Keep add/update/delete/select behavior working.
- Keep business rules in the service layer.
- Verify that the UI still refreshes correctly after each change.

##### Minimum definition of done

- a new teammate can locate widget creation and callback logic quickly
- the app still launches and performs CRUD correctly
- selection state is managed in one clear place
- no new circular import problems are introduced

##### Stretch goals

- add a status bar showing the last action
- split the GUI into `build_form()`, `build_buttons()`, and `build_list()` helper methods
- add a dedicated `load_selected_item()` helper for readability

### 16) Instructor coaching moves during lab

When a learner says “I know it should be cleaner, but I don’t know where to start,” use this sequence:

1. “Show me where the widgets are created.”
2. “Show me where the current selection is stored.”
3. “Show me one callback that repeats code from another callback.”
4. “Can we extract that repeated behavior into a helper?”

When a learner breaks the app during refactor, model calm debugging:

- read the traceback aloud
- identify the first line in their code that matters
- ask whether a widget attribute was created before use
- ask whether a method name changed but a button command did not
- ask whether an import path is now wrong after moving files

### 17) Why this matters in real projects

Connect the lesson to professional habits.

**Say:** “In a real application, the first version of the GUI is rarely the last. Features accumulate. If the codebase has no structure, progress slows down because every change risks surprising side effects. The point of architecture is not ceremony. The point is making future work cheaper and safer.”

Relate to the next session:

- JSON save/load is easier to add when the UI has one place for app startup and one place for post-CRUD hooks
- SQLite integration later will be easier if the service layer is already the gateway for operations
- testing will be easier if core logic is not hidden inside widget callbacks

---

## Worked example: a clean small Tkinter entry point

Use this as a reference pattern, not necessarily as a file learners must copy exactly.

```python
import tkinter as tk

from core.service import TrackerService
from ui.app import TrackerApp


def main() -> None:
    root = tk.Tk()
    service = TrackerService()
    app = TrackerApp(root=root, service=service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

Explain why `main()` is useful:

- it is an obvious application entry point
- it wires dependencies together cleanly
- it keeps setup code out of the middle of the UI class

---

## Common pitfalls to watch for

### Pitfall 1: over-refactoring midstream

Learners may try to split into four files, rename everything, add menus, and change validation rules all at once. Remind them that a refactor is successful when behavior is preserved.

### Pitfall 2: circular imports

If `service.py` imports `app.py` and `app.py` imports `service.py`, step back and re-establish one-way dependencies.

### Pitfall 3: leaving business logic in the UI

Examples include directly modifying the service’s internal list or duplicating validation rules in callbacks only.

### Pitfall 4: storing too much state

The app needs some state, but not every little detail. Encourage learners to store only what they need, like the selected ID and status message, rather than shadow copies of the full dataset unless there is a clear reason.

### Pitfall 5: giant methods

An `App` class is not automatically good if `build_ui()` is 250 lines with no helpers. Encourage extraction by region: form, buttons, list, menus, status bar.

---

## Completion criteria for this hour

Learners are in a strong position if they can show:

- a clear `App` or controller class
- widget construction separated from event logic
- thin callbacks that call the service layer
- centralized helpers for repeated behavior such as `refresh_items()` and `get_form_data()`
- behavior preserved after refactor

If learners are not fully done, prioritize in this order:

1. establish the `App` class
2. move one working callback into the class
3. centralize refresh and form extraction helpers
4. clean up remaining duplication

---

## Quick check / exit ticket

Ask one or more of the following:

1. What is one sign that GUI code needs refactoring?
2. What responsibilities belong in an `App` class?
3. Why should the service layer not import the UI layer?
4. What is one helper method that reduced duplication in your refactor?

A strong response to question 1 sounds like:

> “If I have to edit multiple unrelated functions or globals to add one behavior, my GUI probably needs refactoring.”

---

## Preview of the next hour

Hour 3 turns the GUI into a more realistic milestone by adding JSON persistence and user-facing polish. Because we refactored now, we have clean places to add startup load, save-after-change behavior, menus, shortcuts, and error handling without turning the application into a tangle again.


---

## Extended architecture notes for instructors

This section gives you more language and examples for learners who need stronger mental models around structure, not just syntax.

### A practical definition of controller separation

When learners hear “controller,” some imagine a huge framework concept. Keep it simple.

**Say:** “In this course, a controller is just the part of the program that coordinates what happens when the user does something. It is not magical. It gathers input, calls the right service method, and updates the visible interface.”

The controller or `App` class is a traffic director, not the whole city. That metaphor helps learners keep the role modest and understandable.

### What belongs where

A common source of confusion is responsibility drift. Use this simple chart verbally or on the board.

**UI/App layer**

- create widgets
- bind events
- read form values
- show dialogs and status text
- refresh the visual list

**Service layer**

- validate business rules
- create/update/delete records
- look up records by ID
- raise domain-specific errors
- later coordinate with storage/repository logic

**Model layer**

- represent the data shape
- preserve stable identity
- support conversion to and from dictionaries if useful

Then ask learners to classify a few actions:

- “Checking whether name is blank—UI or service?”
- “Showing an error dialog—UI or service?”
- “Finding a record by ID—UI or service?”
- “Deciding what field labels look like—UI or service?”

This turns abstraction into a classification exercise they can reason through.

### Signs that a callback is doing too much

Teach learners to diagnose overload using questions:

- Does this callback directly manipulate the raw list of records?
- Does it repeat validation rules that already exist elsewhere?
- Does it contain 20–30 lines of mixed UI, domain, and storage logic?
- Would changing the record model force edits in many callbacks?

If the answer is yes, the callback is probably too large or too responsible.

### Why thin callbacks matter beyond style

Learners sometimes hear “thin callbacks” as a preference rather than an engineering advantage. Name the concrete benefits.

- easier to read during debugging
- easier to test service logic without launching the GUI
- easier to reuse service methods when the course later adds different interfaces
- easier to switch persistence from JSON to SQLite
- fewer accidental differences between add/update/delete behavior

**Say:** “When the interface stays thin, the app becomes more adaptable. That flexibility is a practical advantage, not a style trophy.”

---

## Step-by-step refactor checklist for classroom use

If your learners need a more mechanical process, use this checklist on screen.

### Stage 1: freeze behavior before moving code

- run the app once
- perform add, update, and delete once each
- identify what currently works
- commit or save a backup copy if learners are using Git

### Stage 2: create the class shell

- define `TrackerApp`
- move shared state into `self`
- keep `main()` small and clear
- verify the app still opens

### Stage 3: move widget creation

- put form widgets in `build_ui()`
- store widgets or `StringVar` instances on `self`
- wire one button command at a time
- verify widget names match callback references

### Stage 4: extract helpers

- `get_form_data()`
- `clear_form()`
- `set_status()`
- `refresh_items()`

Explain that helpers are often the fastest improvement because they reduce duplication immediately.

### Stage 5: migrate callbacks safely

- move `on_add()` first
- test
- move selection handler
- test
- move `on_update()` and `on_delete()`
- test again

### Stage 6: optional module split

Only after the refactor is working:

- move service/core code into `core/`
- move GUI code into `ui/`
- fix imports carefully
- test once more

### Stage 7: stop and explain the code aloud

A useful test for architecture is whether the learner can narrate it:

- “Here is where widgets are created.”
- “Here is where selection state lives.”
- “Here is the one method that refreshes the list.”
- “Here is where the service layer handles record operations.”

If learners can explain the structure calmly, the refactor is probably doing its job.

---

## Debugging after refactor: instructor coaching script

Refactoring introduces a specific class of bugs. The key teaching move is to normalize them and debug systematically.

### Common post-refactor bug: attribute does not exist

Typical cause:

- a widget used to be a local name and now should be `self.widget_name`
- `build_ui()` creates it conditionally or after a method tries to use it

Debugging prompt:

**Ask:** “Where is that attribute supposed to be created, and does that happen before this method runs?”

### Common post-refactor bug: button command points to an old function name

Typical cause:

- command still references `update_item` instead of `self.on_update`

Debugging prompt:

**Ask:** “If I click the button, which exact callable is Tkinter trying to invoke?”

### Common post-refactor bug: selection state is lost

Typical cause:

- `selected_item_id` is now on `self`, but one method still uses a global or local version

Debugging prompt:

**Ask:** “Do all methods agree on one source of truth for the current selection?”

### Common post-refactor bug: import errors after splitting modules

Typical cause:

- file moved, import path not updated
- circular dependency created

Debugging prompt:

**Ask:** “Which module is responsible for assembly, and which direction should imports flow?”

Model calm problem-solving in front of the class. That is as valuable as the final refactor itself.

---

## Instructor language for code review and feedback

Use supportive but specific language. Here are sample phrases.

### When the structure is improving

- “This is easier to navigate because widget creation now has one home.”
- “I like that your callbacks mostly delegate to the service layer.”
- “Your `refresh_items()` helper is carrying a lot of weight in a good way.”

### When the code still needs separation

- “Your GUI works, but I still see business rules leaking into multiple callbacks.”
- “You have the right idea; now let’s make one method responsible for gathering form data so the handlers don’t repeat it.”
- “This is a good time to move from ‘it works’ to ‘it is safe to extend.’”

### When a learner over-refactored and broke things

- “Let’s reduce scope. Which smallest working version can we get back first?”
- “Refactoring is most effective when we change one layer at a time.”
- “Your instinct to organize is correct. Now let’s recover a stable base and continue in smaller steps.”

These phrases keep the focus on engineering decisions rather than personal judgment.
