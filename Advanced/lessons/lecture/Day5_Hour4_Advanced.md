# Day 5, Hour 4: Record List UI with `Listbox` or `Treeview` and Selection Events

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 5
- **Hour**: 4 of 4 for this session, corresponding to **Hour 20** in the 48-hour runbook
- **Focus**: Displaying records in a list/table, handling selection events, and refreshing data safely
- **Runbook alignment**: Compare `Listbox` and `Treeview`; bind selection callbacks; refresh list safely; add a details area; ensure the UI behaves correctly with no records or no selection
- **Prerequisites**:
  - Students can build a Tkinter GUI with basic layout
  - Students understand callbacks and service-layer separation
  - Students can work with lists of objects or dictionaries
- **Teaching goal**: Help students move from single-record forms to multi-record application thinking
- **Demo app theme**: A contact browser with a `Treeview`, details pane, and Refresh button
- **Key message to repeat**: “A record list is only useful if the app can respond safely to selection and refresh.”
- **Success criteria for the hour**:
  - Students can explain `Listbox` vs `Treeview`
  - Students can populate a list or table from in-memory data
  - Students can bind selection events to a callback
  - Students can refresh the UI without duplicating stale rows
  - Students can handle empty-state cases safely

---

## Timing Overview

| Segment | Time |
|---|---:|
| Recap and transition from forms to multi-record views | 5 minutes |
| List displays: `Listbox` vs `Treeview` and selection events | 12 minutes |
| Refreshing data safely and showing details on selection | 10 minutes |
| Live demo: `Treeview` with details pane and refresh button | 13 minutes |
| Hands-on lab: record list + details area | 15 minutes |
| Debrief, quick checks, exit ticket, wrap-up | 5 minutes |

**Total:** 60 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, students should be able to:

1. Explain the difference between `Listbox` and `Treeview`.
2. Display multiple records in a list or table-like interface.
3. Refresh a record view safely without duplicating stale rows.
4. Bind a selection event to a callback.
5. Show record details when a row is selected.
6. Handle the “no selection” case without crashing.
7. Keep list population logic and record retrieval logic separate from presentation code.

---

## Section 1: Recap and Transition (5 minutes)

### Quick Re-entry

**[Instructor speaks:]**

So far today, we have built forms, improved layout, and added validation. That gives us a working input side of the application.

But most useful applications do more than collect one record at a time. They also show collections of records and let the user inspect or choose one.

That is our focus for this final hour of Session 5.

### Framing the Hour

**[Instructor speaks:]**

We are moving from a single-record mindset to a multi-record mindset.

We want users to be able to:

- see what has already been saved
- refresh the display
- click or select one record
- view details for the selected item

The technical ideas underneath that are:

- choosing between `Listbox` and `Treeview`
- binding selection callbacks
- clearing and repopulating safely
- handling empty selections and empty data sets

---

## Section 2: Choosing the Right List Widget (12 minutes)

### `Listbox` vs `Treeview`

**[Instructor speaks:]**

Tkinter gives us more than one way to display collections.

A **`Listbox`** is simple and useful when:

- you only need one visible string per row
- the display is lightweight
- you are showing a single-column list

A **`Treeview`** from ttk is more structured and useful when:

- you want multiple columns
- you want a table-like display
- each record has several fields
- you may later add sorting or richer interaction

For this course, `Treeview` is often the better teaching choice once students are ready for multi-field record displays.

### Selection Events

**[Instructor speaks:]**

A list becomes much more useful when the UI can react to selection.

For `Treeview`, a common event binding is:

```python
self.tree.bind("<<TreeviewSelect>>", self.on_select)
```

That means when the selected row changes, Tkinter calls the callback.

### Guarding Against Empty Selection

**[Instructor speaks:]**

One of the most common beginner mistakes is assuming a selection always exists.

But what if:

- the list is empty?
- the user clicks Refresh and nothing exists?
- the current selection is cleared?
- the list changed and the old item is gone?

The callback must handle that safely.

### Refreshing Safely

**[Instructor speaks:]**

If we repopulate a list or table, we should almost always clear the old rows first. Otherwise we risk duplicate rows or stale data remaining visible.

A safe refresh pattern is:

1. clear the current widget contents
2. fetch the current records
3. insert the fresh rows
4. reset the details pane if needed

### Quick Check

**[Ask students:]**

Why is a Refresh button still meaningful even when there are zero records?

**Expected answer:** because “no data” is still a valid state, and the UI should remain stable and accurate.

---

## Section 3: Separation of Responsibilities (10 minutes)

### What the Service Layer Should Do

**[Instructor speaks:]**

The service layer should provide operations like:

- list records
- get one record by ID
- add or remove records

The service layer should **not** know about:

- `Treeview`
- row IDs on screen
- selection events
- label widgets

It should return plain Python data.

### What the UI Should Do

**[Instructor speaks:]**

The UI should:

- populate the visible list or table
- respond to selection
- update the details area
- show empty-state messages
- decide what to do after refresh

This keeps responsibilities clean and prevents the GUI from leaking into the service layer.

### Empty-State Design

**[Instructor speaks:]**

A professional application behaves sensibly when there is no data.

If there are no records:

- the list should appear empty
- the details area should say something like “No record selected”
- clicking Refresh should not crash
- the user should not be left wondering whether the app is broken

That is not a small detail. That is part of usability.

---

## Section 4: Live Demo — Treeview with Selection and Details Pane (13 minutes)

### Demo Framing

**[Instructor speaks:]**

I will build an in-memory record browser with:

- a `Treeview` on the left
- a details pane on the right
- a Refresh button
- selection handling that updates the details pane
- safe behavior when no rows exist

Watch for the refresh flow and the selection callback.

### Demo Code

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass(slots=True)
class ContactRecord:
    record_id: int
    name: str
    email: str
    role: str


class ContactService:
    def __init__(self) -> None:
        self._records: list[ContactRecord] = [
            ContactRecord(1, "Ada Lovelace", "ada@example.com", "Analyst"),
            ContactRecord(2, "Grace Hopper", "grace@example.com", "Engineer"),
            ContactRecord(3, "Katherine Johnson", "katherine@example.com", "Scientist"),
        ]

    def list_records(self) -> list[ContactRecord]:
        return list(self._records)

    def get_record(self, record_id: int) -> ContactRecord | None:
        for record in self._records:
            if record.record_id == record_id:
                return record
        return None


class ContactBrowserApp:
    def __init__(self, root: tk.Tk, service: ContactService) -> None:
        self.root = root
        self.service = service

        self.root.title("Contact Browser")
        self.root.geometry("860x360")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.detail_vars = {
            "name": tk.StringVar(value="No record selected"),
            "email": tk.StringVar(value="-"),
            "role": tk.StringVar(value="-"),
        }

        self._build_ui()
        self.refresh_records()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(1, weight=1)

        ttk.Label(
            main_frame,
            text="Saved Contacts",
            font=("TkDefaultFont", 11, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        ttk.Button(main_frame, text="Refresh", command=self.refresh_records).grid(
            row=0,
            column=1,
            sticky="e",
            pady=(0, 8),
        )

        self.tree = ttk.Treeview(
            main_frame,
            columns=("name", "email", "role"),
            show="headings",
            selectmode="browse",
        )
        self.tree.grid(row=1, column=0, sticky="nsew", padx=(0, 12))

        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("role", text="Role")

        self.tree.column("name", width=160, anchor="w")
        self.tree.column("email", width=220, anchor="w")
        self.tree.column("role", width=120, anchor="w")

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        details_frame = ttk.LabelFrame(main_frame, text="Details", padding=12)
        details_frame.grid(row=1, column=1, sticky="nsew")

        details_frame.columnconfigure(1, weight=1)

        ttk.Label(details_frame, text="Name").grid(row=0, column=0, sticky="w", pady=6)
        ttk.Label(details_frame, textvariable=self.detail_vars["name"]).grid(
            row=0, column=1, sticky="w", pady=6
        )

        ttk.Label(details_frame, text="Email").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Label(details_frame, textvariable=self.detail_vars["email"]).grid(
            row=1, column=1, sticky="w", pady=6
        )

        ttk.Label(details_frame, text="Role").grid(row=2, column=0, sticky="w", pady=6)
        ttk.Label(details_frame, textvariable=self.detail_vars["role"]).grid(
            row=2, column=1, sticky="w", pady=6
        )

    def refresh_records(self) -> None:
        for item_id in self.tree.get_children():
            self.tree.delete(item_id)

        records = self.service.list_records()

        for record in records:
            self.tree.insert(
                "",
                "end",
                iid=str(record.record_id),
                values=(record.name, record.email, record.role),
            )

        self.clear_details()

    def clear_details(self) -> None:
        self.detail_vars["name"].set("No record selected")
        self.detail_vars["email"].set("-")
        self.detail_vars["role"].set("-")

    def on_select(self, event: tk.Event) -> None:
        selected_items = self.tree.selection()
        if not selected_items:
            self.clear_details()
            return

        record_id = int(selected_items[0])
        record = self.service.get_record(record_id)

        if record is None:
            self.clear_details()
            return

        self.detail_vars["name"].set(record.name)
        self.detail_vars["email"].set(record.email)
        self.detail_vars["role"].set(record.role)


def main() -> None:
    root = tk.Tk()
    service = ContactService()
    ContactBrowserApp(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Demo Steps

1. Define the record model and in-memory service.
2. Build the main layout with a list area and details area.
3. Create the `Treeview` with headings.
4. Bind `<<TreeviewSelect>>` to `on_select`.
5. Add a Refresh button and implement `refresh_records()`.
6. Clear old rows before inserting new ones.
7. Add a safe empty-state details view.
8. Select different rows and watch the details pane update.
9. Explain what happens if there are no records or no selection.

### Demo Narration

**[Instructor speaks while coding:]**

Notice the separation again:

- `ContactService` owns the data
- `ContactBrowserApp` owns widgets and interaction
- `refresh_records()` clears and reloads the visible list
- `on_select()` safely handles both selected and unselected cases

Also notice that I use the record ID as the row `iid`. For a small teaching example, that makes it easy to map a selected row back to a record.

### Live Questions to Ask During the Demo

**[Ask students:]**

What could go wrong if I refresh the table without deleting old rows first?

**Expected answer:** duplicate or stale rows could appear.

**[Ask students:]**

What should happen if `selection()` returns an empty tuple?

**Expected answer:** the UI should clear or keep a safe empty-state message and avoid crashing.

**[Ask students:]**

Why doesn’t the service know anything about the `Treeview` widget?

**Expected answer:** because the service should remain independent of UI details.

---

## Section 5: Hands-On Lab — Record List + Details View (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Now extend your app so it feels more like a real desktop tool. Add a record list and a details area.

Students may use `Treeview` or `Listbox`, but `Treeview` is recommended if multiple fields are involved.

### Student Task

Build or extend your GUI so that it includes:

- a list area displaying saved records
- a details pane showing the currently selected record
- a selection callback
- a Refresh button
- safe behavior when no records exist or no record is selected

### Hands-On Lab Guidance

**[Instructor speaks:]**

Work in this order:

1. create the visual layout
2. populate the list with hard-coded or in-memory records
3. add a Refresh button
4. clear old rows before reloading
5. bind selection
6. show details for the selected record
7. handle the empty-state case safely

If you are short on time, it is better to build a stable two-column browser than to chase advanced styling.

### Suggested Minimum Design

- left side: `Treeview` with 2 to 3 columns
- right side: details frame with labels
- top or bottom: Refresh button

### Completion Criteria

A strong minimum solution should:

1. Display at least two records from in-memory data.
2. Refresh the list without duplicating old rows.
3. Update a details pane on selection.
4. Avoid crashing when no selection exists.
5. Show a clear empty-state message if there are no records.

### Circulation Prompts

**[Circulate and ask:]**

1. Where do you clear old rows before reloading?
2. What happens if the tree has no selection?
3. How do you map a selected row back to a record?
4. Where does record retrieval logic live?
5. What does Refresh do when there are zero records?

### Common Pitfalls During the Lab

#### Pitfall 1: Not clearing old rows before repopulating
This causes duplicate display rows.

#### Pitfall 2: Assuming a selection always exists
If students index into an empty selection without checking, the app can crash.

#### Pitfall 3: UI logic buried inside the service layer
The service should not know about widget-specific details.

#### Pitfall 4: Details panel shows stale information after refresh
A safe refresh usually clears the details panel until a new selection is made.

### Optional Extensions

- Auto-select the first record after refresh
- Add a record-count label
- Add a Delete button and refresh after deletion
- Add clickable column sorting later as a stretch goal

---

## Section 6: Debrief, Quick Checks, Exit Ticket, and Wrap-Up (5 minutes)

### Group Debrief

**[Instructor speaks:]**

This hour completes an important transition. Students now have the building blocks of a small desktop CRUD-style interface:

- form input
- validation
- a list view
- selection-based detail display

That is a meaningful architectural step.

### Quick Checks

**Prompt:** What is one key difference between `Listbox` and `Treeview`?  
**Expected answer:** `Listbox` is simpler and usually single-column text; `Treeview` supports structured multi-column display.

**Prompt:** Why clear the details panel during refresh?  
**Expected answer:** to avoid stale information when the visible list changes.

### Exit Ticket

**Prompt 1:** Why should a refresh operation clear old rows first?  
**Expected answer:** to avoid duplicate or stale data in the visible list.

**Prompt 2:** What should happen if the user clicks Refresh when there are no records?  
**Expected answer:** the UI should remain stable, show an empty list, and show a safe empty-state message instead of crashing.

**Prompt 3:** What is the role of the selection callback?  
**Expected answer:** it reacts to the selected row and updates the rest of the interface, such as a details pane.

### Common Pitfalls Recap

- not clearing old rows
- crashing on empty selection
- stale details after refresh
- coupling service logic to widget details
- unclear empty-state behavior

### Wrap-Up

**[Instructor speaks:]**

Today’s session introduced the core of desktop GUI thinking:

- events
- layout
- validation
- record display

Students do not need a giant application yet. They need a clear mental model, and this session gives them one.

A strong GUI application is structured. The UI handles presentation and interaction. The service layer handles business rules and data access. The application remains stable even when the user gives bad input, no input, or no data exists at all.

---

## Optional Instructor Reference Notes

### Strong Student Solution Characteristics
Look for solutions where:

- the list reload is deliberate and safe
- the selection callback handles empty states
- the details area is readable and clearly labeled
- the service layer returns plain Python data, not widget objects

### If Students Finish Early
Invite them to:

- auto-refresh the list after saving a new record
- add a status bar showing total record count
- switch between `Listbox` and `Treeview` and discuss tradeoffs
- sketch how update/delete workflows might connect in the next session
