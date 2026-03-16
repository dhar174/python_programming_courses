# Day 6 Hour 1 Advanced — CRUD Wiring in the GUI: Update and Delete Workflows

## Session context

This hour is part of **Session 6** of the Advanced Python full-stack tracker capstone. Learners already built the essential GUI surface in Session 5: a Tkinter window, a form for entering tracker data, and a list-style display using a `Treeview` or `Listbox`. Today we move from “a screen that can add records” to “a tool that behaves like a real application.”

The focus of this hour is the second half of CRUD: **Update** and **Delete**. In many beginner GUI projects, create and read work, but update and delete are fragile because the interface is wired directly to list positions instead of stable record identifiers. This hour deliberately corrects that pattern. The guiding design choice for the session is:

- the **service layer owns business rules**
- the **UI owns display and user interaction**
- the **record ID stays stable even when sort order, filtering, or selection changes**

Use a neutral “tracker” framing throughout so instructors can adapt examples to tasks, inventory, contacts, notes, expenses, or another domain.

Tkinter is the default framework for reliability in classroom environments. If a learner asks about PyQt, acknowledge that the same architectural ideas apply, but keep the official demo in Tkinter.

---

## Learning objectives

By the end of this instructional hour, learners should be able to:

1. Explain why update and delete workflows should target a **stable record ID**, not a visual list index.
2. Implement the standard GUI update flow: **select -> load into form -> edit -> save update -> refresh list**.
3. Implement a delete flow with **confirmation** and clear post-delete refresh behavior.
4. Handle missing-record errors gracefully, including cases where the selected record no longer exists.
5. Keep GUI callbacks thin by delegating actual work to a **service layer**.
6. Refresh the visible list after each change so the interface stays in sync with the underlying data.

---

## Prerequisites and starting assumptions

Before class begins, confirm that learners have:

- a working Tkinter app window
- a form with entry fields or a combination of `Entry`, `Combobox`, `Checkbutton`, or `Text`
- a record display using `ttk.Treeview` or `Listbox`
- a basic model and service layer from earlier capstone work
- stable IDs in the domain model or at least a plan to add them immediately
- create/add behavior already working through the service layer

If some learners are behind, tell them the minimum viable starting point for this hour is:

- a window
- one form
- one list display
- a service method that returns all records
- a service method that can update and delete by ID

If they do not yet have update/delete service methods, they can still follow the hour by implementing those first in plain Python, then wiring them into the GUI.

---

## Materials and setup

- Python 3.11+
- Tkinter / `ttk`
- Existing tracker project folder
- Optional sample JSON data file, though JSON persistence is formally emphasized in Hour 23
- Projector-ready font size because learners need to watch selection and refresh behavior closely

Recommended pre-class instructor setup:

- open the project in the editor
- have one version with an intentional bug that uses list index as ID
- have one corrected version using stable IDs
- have sample records loaded so update and delete demonstrations feel realistic

---

## Section navigation

1. Why update/delete are harder than add
2. The design rule: stable IDs over list positions
3. Update workflow, step by step
4. Delete workflow, step by step
5. Graceful error handling with `messagebox`
6. Live demo guidance and code snippets
7. Practice lab
8. Checkpoint, debrief, and common pitfalls

---

## Suggested timing

- **0–10 min:** recap and motivation
- **10–22 min:** teach update flow and stable ID reasoning
- **22–32 min:** teach delete flow and confirmation pattern
- **32–42 min:** live coding demo with update/delete wiring
- **42–55 min:** guided lab and instructor circulation
- **55–60 min:** quick check and debrief

Adjust pacing based on learner progress. If learners still need more support on the update flow, prioritize that over polishing delete confirmations.

---

## Instructor speaking script

### 1) Opening recap and framing

**Say:** “Last session, we gave our tracker a user interface. It could collect information, validate it, and display a list of records. Today we make the interface trustworthy. A tracker is not useful if people can only add records forever. Real tools must let users correct mistakes and remove data safely.”

**Say:** “The hidden challenge is that update and delete are not just button-click problems. They are identity problems. We need to know exactly which record the user is changing, and we need to still be correct after sorting, filtering, or refreshing the visible list.”

Pause and ask:

- “If I click the third row in a list, is ‘third row’ the identity of the record?”
- “What happens if I delete row one first? Is the old third row still the third row?”

Expected conclusion: a visual position is not a reliable identity.

**Say:** “That is why this hour keeps repeating one design rule: **use a stable record ID everywhere that matters**. The list index is for display. The ID is for truth.”

### 2) Why add is easy and update/delete are trickier

Use the board or screen to compare the operations.

**Create** is usually straightforward:

- collect form data
- validate it
- create a new record
- append to storage
- refresh the list

**Update** adds more moving parts:

- detect which record is selected
- retrieve the selected record ID
- load that record into the form
- allow edits
- save changes back to the same ID
- refresh the list
- preserve or intentionally clear selection

**Delete** also has more responsibility:

- detect selection
- confirm destructive action
- delete by ID
- handle “already gone” cases safely
- refresh the list
- clear stale form values or stale selection state

**Say:** “Notice that ‘which record’ is the critical question in both workflows. If the answer is ‘whatever row happens to be selected at the moment,’ that can still work, but only if the selected row carries the stable ID, not just a row number.”

### 3) Stable IDs: the core design choice

Tie this to the capstone architecture.

**Say:** “Your tracker should already have a service layer. That service layer should expose methods like `update_item(item_id, ...)` and `delete_item(item_id)`. The UI should not walk through a Python list guessing which object to mutate based on screen position. The service layer should receive an ID and decide what to do.”

A useful verbal contrast:

- fragile pattern: `records[selected_index] = ...`
- durable pattern: `service.update_item(selected_id, ...)`

Explain what makes an ID “stable”:

- it is created once when the record is created
- it does not change when the record is edited
- it does not depend on screen order
- it does not depend on list filtering
- it survives save/load cycles

If learners ask what form the ID should take, recommend a string UUID for simplicity.

### 4) Example domain model and service reminder

You do not need to spend the whole hour here, but it helps to show a small, consistent example. Read the code slowly and narrate what each layer owns.

```python
from __future__ import annotations

from dataclasses import dataclass, asdict
from uuid import uuid4


class ValidationError(Exception):
    pass


class NotFoundError(Exception):
    pass


@dataclass(slots=True)
class TrackerItem:
    item_id: str
    name: str
    category: str
    status: str
    notes: str = ""

    @classmethod
    def create(cls, name: str, category: str, status: str, notes: str = "") -> "TrackerItem":
        return cls(
            item_id=str(uuid4()),
            name=name,
            category=category,
            status=status,
            notes=notes,
        )


class TrackerService:
    def __init__(self) -> None:
        self._items: list[TrackerItem] = []

    def list_items(self) -> list[TrackerItem]:
        return list(self._items)

    def add_item(self, name: str, category: str, status: str, notes: str = "") -> TrackerItem:
        if not name.strip():
            raise ValidationError("Name is required.")
        item = TrackerItem.create(name=name.strip(), category=category.strip(), status=status.strip(), notes=notes.strip())
        self._items.append(item)
        return item

    def update_item(self, item_id: str, name: str, category: str, status: str, notes: str = "") -> TrackerItem:
        if not name.strip():
            raise ValidationError("Name is required.")
        item = self.get_item(item_id)
        item.name = name.strip()
        item.category = category.strip()
        item.status = status.strip()
        item.notes = notes.strip()
        return item

    def delete_item(self, item_id: str) -> None:
        item = self.get_item(item_id)
        self._items.remove(item)

    def get_item(self, item_id: str) -> TrackerItem:
        for item in self._items:
            if item.item_id == item_id:
                return item
        raise NotFoundError(f"No tracker item found for ID {item_id}.")
```

**Say:** “The GUI will not manipulate `_items` directly. It will ask the service to perform the action. That keeps validation, lookup, and error handling centralized.”

### 5) Update workflow: select -> load -> edit -> save update

Tell learners there are really two update moments:

1. **entering edit mode** by loading the selected record into the form
2. **committing the update** by saving changes back through the service layer

That distinction matters. A lot of buggy GUIs skip the explicit concept of “current selected ID” and later have no idea which record is being edited.

**Say:** “The UI needs one piece of state: the ID of the record currently being edited. Everything else can be derived.”

Recommended pattern:

- keep `self.selected_item_id: str | None = None`
- when the user selects a row, capture the hidden ID from the `Treeview`
- fetch the full record from the service layer
- populate form widgets
- when Update is clicked, call `service.update_item(self.selected_item_id, ...)`
- then refresh the list and clear edit state if desired

Demonstrate the selection handler.

```python
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


def on_item_selected(self, event: tk.Event | None = None) -> None:
    selection = self.tree.selection()
    if not selection:
        self.selected_item_id = None
        return

    row_id = selection[0]
    values = self.tree.item(row_id, "values")
    item_id = values[0]
    self.selected_item_id = item_id

    try:
        item = self.service.get_item(item_id)
    except NotFoundError as error:
        messagebox.showerror("Selection Error", str(error))
        self.refresh_items()
        self.clear_form()
        return

    self.name_var.set(item.name)
    self.category_var.set(item.category)
    self.status_var.set(item.status)
    self.notes_text.delete("1.0", tk.END)
    self.notes_text.insert("1.0", item.notes)
```

Explain why the first value in the row is the ID. You may hide the column visually later, but the important point is that the GUI still has access to the stable identifier.

Now show the update handler.

```python
def on_update(self) -> None:
    if self.selected_item_id is None:
        messagebox.showwarning("No Selection", "Please select a record to update.")
        return

    name = self.name_var.get()
    category = self.category_var.get()
    status = self.status_var.get()
    notes = self.notes_text.get("1.0", tk.END).strip()

    try:
        updated_item = self.service.update_item(
            item_id=self.selected_item_id,
            name=name,
            category=category,
            status=status,
            notes=notes,
        )
    except ValidationError as error:
        messagebox.showerror("Validation Error", str(error))
        return
    except NotFoundError as error:
        messagebox.showerror("Update Failed", str(error))
        self.refresh_items()
        self.clear_form()
        self.selected_item_id = None
        return

    self.refresh_items(selected_item_id=updated_item.item_id)
    self.set_status(f"Updated: {updated_item.name}")
```

Pause and emphasize what the callback does **not** do:

- it does not modify the internal list directly
- it does not assume the tree row order equals record order
- it does not suppress validation at the service layer

### 6) Delete workflow: confirm, delete by ID, refresh cleanly

**Say:** “Delete is where you protect the user from accidental loss. A good delete workflow is honest, deliberate, and reversible if you later add undo. Today our minimum standard is confirmation and safe refresh.”

Teach the delete pattern as a predictable checklist:

1. ensure a record is selected
2. optionally show the item name in the prompt
3. confirm with `messagebox.askyesno`
4. call `service.delete_item(selected_id)`
5. refresh the list
6. clear stale selection and stale form content
7. show status feedback

Example:

```python
def on_delete(self) -> None:
    if self.selected_item_id is None:
        messagebox.showwarning("No Selection", "Select a record to delete.")
        return

    try:
        item = self.service.get_item(self.selected_item_id)
    except NotFoundError as error:
        messagebox.showerror("Delete Failed", str(error))
        self.refresh_items()
        self.clear_form()
        self.selected_item_id = None
        return

    confirmed = messagebox.askyesno(
        title="Confirm Delete",
        message=f"Delete '{item.name}'? This action cannot be undone right now.",
    )
    if not confirmed:
        return

    try:
        self.service.delete_item(item.item_id)
    except NotFoundError as error:
        messagebox.showerror("Delete Failed", str(error))
        return

    self.refresh_items()
    self.clear_form()
    self.selected_item_id = None
    self.set_status(f"Deleted: {item.name}")
```

### 7) Graceful `NotFoundError` handling

The runbook specifically calls out handling `NotFoundError` gracefully. Give learners a scenario that makes it feel real rather than theoretical.

**Say:** “You might be wondering, ‘How could the record disappear between selection and update?’ In a one-user desktop app, that seems unlikely. But software design becomes stronger when we code for state drift anyway. Maybe the list refreshed after a file load. Maybe you removed the item in another part of the app. Maybe your code had a stale selected ID. Good software fails gently.”

Explain the student takeaway:

- `NotFoundError` is not necessarily a disaster
- it is feedback that the UI and current data state no longer match
- the right response is usually to tell the user, refresh, and reset selection

That pattern makes later work with SQLite or APIs easier because stale-state errors are common in larger systems.

### 8) What the list refresh should do

A refresh method is where instructors can reinforce thin UI design.

**Say:** “Any time the underlying data changes, the list display should be rebuilt from the source of truth. Don’t try to patch ten little visual details by hand if you can refresh from the service layer in one place.”

Sample refresh method:

```python
def refresh_items(self, selected_item_id: str | None = None) -> None:
    for row_id in self.tree.get_children():
        self.tree.delete(row_id)

    for item in self.service.list_items():
        inserted_id = self.tree.insert(
            "",
            tk.END,
            values=(item.item_id, item.name, item.category, item.status),
        )
        if selected_item_id == item.item_id:
            self.tree.selection_set(inserted_id)
            self.tree.focus(inserted_id)
```

Explain why a full refresh is acceptable here:

- the dataset is small in this capstone stage
- correctness and clarity matter more than micro-optimization
- a single refresh function reduces duplicated UI code

### 9) Live demo plan

Run the demo deliberately. Do not speed through it. Learners need to see state changes.

#### Demo sequence A: show the fragile pattern first

If time allows, briefly show the wrong approach.

**Say:** “I’m going to show you a bug on purpose.”

Use code that updates by list index. Rearrange or delete an earlier row. Then update what used to be another row. Show the wrong record changing.

**Say:** “This is exactly why list position is not identity.”

Then switch to the corrected version.

#### Demo sequence B: update flow

1. Click a record in the list.
2. Narrate: “Selection event fires; we capture the stable ID.”
3. Show the form auto-populate.
4. Change one or two fields.
5. Click Update.
6. Point to the status message.
7. Point to the refreshed row.
8. Optionally keep the same row selected after refresh to show a polished experience.

Narration prompt:

**Say:** “Notice how the callback collected values and then immediately delegated the real work to the service layer. That is intentional. If I later add file storage, a database, or an API, my UI does not need to become the source of truth.”

#### Demo sequence C: delete flow

1. Select a record.
2. Click Delete.
3. Read the confirmation dialog aloud.
4. Cancel once, then show nothing changes.
5. Repeat and confirm yes.
6. Show the list refresh and form clearing.

Narration prompt:

**Say:** “Canceling is part of correct behavior. A delete button without a safe pause is not complete.”

#### Demo sequence D: error path

Trigger or simulate a `NotFoundError`. One easy classroom trick is to manually alter the in-memory list in the debugger or quickly delete the selected item behind the scenes before pressing Update.

**Say:** “We did not crash. We told the user what happened, refreshed, and got the app back to a known good state.”

### 10) Guided practice prompt

After the demo, transition clearly.

**Say:** “Now you will wire update and delete into your own tracker. Your goal is not just to make the buttons do something. Your goal is to make them behave correctly and predictably.”

Core lab tasks:

1. Implement row selection so the form loads the selected record.
2. Track the selected record’s stable ID.
3. Add an Update button that sends changes to the service layer.
4. Add a Delete button with confirmation.
5. Refresh the list automatically after update and delete.
6. Handle `NotFoundError` and `ValidationError` with user-facing messages.

Stretch task:

- preserve selection after update
- clear selection after delete
- show a short status message such as “Updated record” or “Deleted record”

### 11) Instructor circulation notes during lab

When circulating, do not start by fixing code. Start with questions.

Ask:

- “Where do you store the selected record ID?”
- “What exactly does your Update callback do?”
- “If the list order changes, would your update still hit the right record?”
- “What happens after delete—does the form still show stale values?”
- “Where is validation happening?”

If a learner is stuck, guide them in this order:

1. confirm selection event wiring
2. confirm the selected ID is captured
3. confirm service `get/update/delete` methods work independently of the GUI
4. confirm refresh behavior
5. then refine user feedback

### 12) Quick debrief script

Bring the room back together with a few short questions.

**Ask:** “What bug becomes likely when you use list index instead of a stable ID?”

Expected answers:

- wrong record updated
- wrong record deleted
- bugs after sorting or filtering
- stale selection problems

**Ask:** “What should the UI do after a successful delete?”

Expected answers:

- refresh the list
- clear or reset form state
- clear stale selected ID
- show feedback

**Ask:** “Why keep callbacks thin?”

Expected answers:

- easier testing
- less duplication
- clearer architecture
- easier to switch persistence later

---

## Live demo reference implementation snippets

Use these snippets selectively rather than pasting all at once. Learners absorb more when you type and narrate small chunks.

### Suggested widget wiring

```python
self.tree = ttk.Treeview(
    self.root,
    columns=("id", "name", "category", "status"),
    show="headings",
)
self.tree.heading("id", text="ID")
self.tree.heading("name", text="Name")
self.tree.heading("category", text="Category")
self.tree.heading("status", text="Status")
self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)

self.update_button = ttk.Button(self.root, text="Update", command=self.on_update)
self.delete_button = ttk.Button(self.root, text="Delete", command=self.on_delete)
```

### Suggested clear form helper

```python
def clear_form(self) -> None:
    self.name_var.set("")
    self.category_var.set("")
    self.status_var.set("")
    self.notes_text.delete("1.0", tk.END)
```

### Suggested status helper

```python
def set_status(self, message: str) -> None:
    self.status_var_label.set(message)
```

Remind learners that helper functions reduce duplication and make GUI behavior more consistent.

---

## Practice / lab handout language

You may read the following directly to the class or paste it into chat:

### Lab: Update and Delete in the Tracker GUI

Build the remaining CRUD workflows in your tracker interface.

#### Required tasks

- Select a record in the list and load its data into the form.
- Store the selected record’s stable ID.
- Update the selected record through the service layer.
- Delete the selected record only after a confirmation dialog.
- Refresh the visible list after each successful change.
- Show a user-friendly message if no record is selected or if the selected record no longer exists.

#### Minimum definition of done

- update works on the correct record
- delete works on the correct record
- the list display stays in sync
- the form does not keep stale state after delete
- validation errors are shown clearly

#### Stretch ideas

- keep the updated item selected after refresh
- display the record name in the delete confirmation dialog
- add a simple “Clear Form” button
- add an undo-last-delete feature stored in memory only

---

## Common pitfalls to watch for

### Pitfall 1: using visible row order as identity

This is the biggest one. If learners say “I know row 2 means item 2,” interrupt that assumption immediately.

Instructor response:

**Say:** “That feels true only while the current screen never changes. Real interfaces change. Stable IDs are what survive change.”

### Pitfall 2: deleting while iterating over the same list

If learners implement delete by looping through the internal list and removing items during iteration, explain why that is fragile. The service layer should either find the item first or create a filtered replacement list.

### Pitfall 3: refreshing the screen but not selection state

A refresh that rebuilds the tree may invalidate row references. Remind learners that tree row IDs and domain item IDs are not the same thing.

### Pitfall 4: validation only in the GUI

The UI may prevent blank names, but the service layer still needs validation. Reinforce that business rules should not disappear when a future API or CLI uses the same service.

### Pitfall 5: update button creates a new record instead of editing the selected one

If learners call `add_item` from the Update button, discuss the semantic difference between create and update.

### Pitfall 6: stale form values after delete

A deleted record should not remain visible in the edit fields because it tells the user a lie about what currently exists.

---

## Instructor notes and coaching advice

- Keep the domain neutral. If the class chose expenses or contacts, adapt labels, not architecture.
- Encourage learners to test with three or more records. Single-record demos hide identity bugs.
- If someone insists on using the index temporarily, ask them to sort alphabetically or insert a record at the top. Let the bug expose itself.
- Celebrate small wins. Update/delete wiring is the moment many beginner GUI apps start to feel “real.”
- Keep reminding the room: “The UI is a customer of the service layer.” That phrase helps learners internalize separation of concerns before Session 7 introduces SQLite.

---

## Completion criteria for this hour

By the end of the hour, a learner is on track if they can demonstrate:

- selecting a record from the list
- editing the record through the form
- saving the update to the correct stable ID
- deleting the selected record with confirmation
- automatic list refresh after each change
- clear user feedback for validation or missing-record errors

If a learner has only partial completion, the priority order is:

1. correct selection and stable ID capture
2. working update
3. working delete with confirmation
4. polished feedback and selection behavior

---

## Quick check / exit ticket

Ask learners to answer verbally, in chat, or on a sticky note.

1. Why is a stable ID better than relying on list index in a GUI?
2. What are the steps in the edit workflow from selection to save?
3. Why should the service layer still validate data even if the form already checks inputs?
4. After a delete, what state should the UI reset or refresh?

A strong one-sentence answer to question 1 sounds like this:

> “A stable ID keeps update and delete correct even if the visible list order changes due to sorting, filtering, refreshes, or insertions.”

---

## Preview of the next hour

In the next hour, learners will refactor the GUI so it remains maintainable as features accumulate. Today’s wiring can become messy quickly if every widget and callback lives in global scope. Next we will introduce a cleaner `App` or controller class structure to prevent callback spaghetti and keep the UI readable.


---

## Detailed instructor walkthrough: minute-by-minute demo choreography

Use this section when you want a more explicit speaking plan than the earlier summary. It is especially useful if you are teaching this capstone hour for the first time or if you want tighter pacing during a live class.

### Minutes 0–5: reconnect to yesterday’s mental model

**Say:** “Yesterday, our GUI could collect and show data. Today we make it trustworthy. Think about your own experience with apps. If you cannot correct a typo or remove an outdated record safely, the app feels unfinished.”

Write these two statements where learners can see them:

- Screen position is not identity.
- Stable IDs make update/delete safe.

Then ask for an everyday analogy. Good examples include:

- a contact in your phone list
- a line item in a shopping app
- a support ticket in a queue

Explain that the visual order of those records may change, but the record itself still needs a stable identity.

### Minutes 5–12: whiteboard the state transition

Draw a small state diagram:

- no selection
- record selected
- form populated
- update committed
- list refreshed
- selection reset or preserved

Narrate each transition. This helps learners see that update is not one click. It is a controlled sequence. Then draw the delete flow beside it:

- record selected
- delete requested
- confirmation dialog
- delete committed
- list refreshed
- form cleared

**Say:** “A lot of GUI bugs come from skipping one of these transitions in our head. If we understand the state changes clearly, the code becomes easier to reason about.”

### Minutes 12–20: model the update path with deliberate narration

When live coding, narrate each micro-step.

1. “I am binding the selection event.”
2. “I am storing the stable ID, not the row number.”
3. “I am loading the selected object from the service layer.”
4. “I am filling the form widgets.”
5. “On update, I am collecting fresh form data.”
6. “Then I call the service, not the list directly.”
7. “Then I refresh the visible list from the source of truth.”

This style of narration slows learners down in a good way. It teaches them how to think, not just what to type.

### Minutes 20–30: model the delete path with user-trust framing

Tell learners that destructive actions require a higher standard of care.

**Say:** “Delete is not just the opposite of add. Delete removes information the user may not be able to easily recreate. Good software respects that.”

Then ask:

- “What should happen if no row is selected?”
- “What should happen if the user clicks Cancel?”
- “Should the app quietly delete without naming the record?”

Use the answers to reinforce usability:

- no selection should produce a calm warning
- cancel should make no changes
- the confirmation should mention the record name when possible

### Minutes 30–40: show the stale-state problem on purpose

A powerful teaching move is to create a bug intentionally.

For example:

- select a record
- clear or reorder internal data
- try to update using stale selection data

Then narrate:

**Say:** “This is why the `NotFoundError` path matters. The goal is not to pretend state never drifts. The goal is to recover gracefully when it does.”

### Minutes 40–50: guided build with checkpoints

Instead of saying “Go code,” break the lab into explicit checkpoints.

Checkpoint A:

- selecting a row populates the form
- current selected ID can be printed or inspected

Checkpoint B:

- update button changes the selected record
- list refreshes after update

Checkpoint C:

- delete confirmation appears
- delete removes the selected record
- stale form state is cleared

Checkpoint D:

- validation or not-found messages appear without crashing

Tell learners to stop and test after each checkpoint. This reduces the “I wrote a lot and now nothing works” problem.

### Minutes 50–60: debrief with principles, not only feature status

Ask learners to share one principle, not just one button they finished. Good answers include:

- stable IDs beat list indexes
- service methods should own validation
- refresh from the source of truth after change
- destructive actions need confirmation

If you hear these principles repeated back, the hour was successful even if some learners still need a few minutes to finish wiring.

---

## Troubleshooting guide for instructors

Use this section as a rapid-response reference during circulation.

### Symptom: the wrong record updates

Most likely causes:

- the code uses selected row index instead of stable ID
- the `Treeview` values do not include the real item ID
- selection state is not refreshed after list rebuild

What to ask:

- “Show me where the selected record ID is stored.”
- “When you refresh the tree, how do you reconnect that selection to the actual record?”
- “If you print the selected ID before update, does it match what you expected?”

### Symptom: delete appears to work, but the form still shows deleted data

Most likely causes:

- `clear_form()` is not called
- `selected_item_id` is not reset
- the app refreshes the list but not the edit state

What to say:

**Say:** “The screen should tell the truth about current data. If the record is gone, the edit form should no longer imply it still exists.”

### Symptom: update creates a duplicate record

Most likely causes:

- update button calls `add_item`
- service update method internally appends instead of mutating the matched record
- the learner copied add logic and only changed the button label

Instructional response:

**Say:** “Ask yourself: am I changing an existing identity, or am I creating a new identity? Update must preserve the original ID.”

### Symptom: selection breaks after refresh

Most likely causes:

- tree row IDs are confused with domain record IDs
- refresh deletes and recreates rows without restoring desired selection
- event callbacks fire during refresh unexpectedly

Possible quick fix:

- pass `selected_item_id` into `refresh_items()`
- re-select the matching inserted row if it still exists

### Symptom: no visible error message, only a console traceback

Most likely causes:

- callback exceptions are not caught
- service errors bubble up without user-friendly translation

Coaching tip:

Tell learners: “Tracebacks help developers. Dialogs help users. Good GUI programs often need both during development.”

---

## Differentiation and pacing notes

### If the class is moving more slowly

Focus on these minimums:

- selected stable ID captured correctly
- update works correctly
- delete works with confirmation
- refresh happens after change

Defer polish such as preserving selection after refresh or adding status messages.

### If the class is moving more quickly

Offer these challenge tasks:

- implement in-memory undo for the last delete
- disable Update/Delete buttons when nothing is selected
- visually highlight the selected row after update
- add a read-only ID display somewhere in the interface for debugging

### If some learners are anxious about refactoring later

Reassure them now:

**Say:** “Today’s goal is correctness first. If your code gets a little repetitive while you finish update/delete, that is okay. The next hour is specifically about architecture cleanup.”

This helps learners avoid feeling they must solve every structural concern at once.
