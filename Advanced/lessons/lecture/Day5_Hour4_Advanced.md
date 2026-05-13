# Day 5 Hour 4 Advanced: Record List UI with Treeview or Listbox, Selection Callbacks, and Safe Refresh

## Instructor delivery context

- Audience: Advanced learners who already completed Day 5 Hour 3 forms and validation work.
- Hour alignment: This script is for Hour 20 in the Advanced runbook.
- Scope boundary for this hour:
  - In scope: record list/table display, selection callback behavior, details pane updates, refresh safety, empty-state handling, and a tightly scoped optional search/filter extension.
  - Out of scope: Day 6 architecture topics, broader testing frameworks, deployment, packaging, and backend persistence changes.
- Teaching posture: near-verbatim facilitation script with clear transitions, exact timing, mini-checkpoints, and observable pass/fail completion checks.

## Learning outcomes for Hour 20

By the end of this hour, learners will be able to:

1. Display records in a list or table widget.
2. React to user selection and show record details in a dedicated details area.
3. Explain Listbox versus Treeview and select the right widget for a given UI need.
4. Implement selection callbacks that do not fail when no row is selected.
5. Refresh list data safely by following the exact sequence:
   - clear existing rows or items
   - repopulate from source
   - handle selection state safely
6. Verify that refreshing does not create stale or duplicate rows.
7. Confirm empty-data states are rendered safely in both list and details areas.
8. Describe what can go wrong if a refresh operation does not clear existing rows first.

## Required talk points to hit explicitly

- Listbox vs Treeview and when each is appropriate.
- Selection callbacks and safe handling when selection is empty.
- Refreshing list content safely to avoid duplication and stale records.
- Live demo: Treeview shows records and selecting a row populates details pane.
- Hands-on lab: build list view for in-memory records, bind selection callback to details area, implement refresh with no duplicate/stale rows.
- Completion criteria:
  - list loads records
  - selecting shows details
  - refreshing does not duplicate rows
- Common pitfalls:
  - selection callback fails when no selection
  - stale or duplicate rows after refresh
- Optional extension:
  - simple search/filter field, only after core completion, and only in final 3 to 5 minutes.
- Quick check:
  - what can go wrong if you refresh without clearing existing rows?

## Exact 60-minute timing plan

- Recap and transition: 4 minutes
- Concepts and talk points: 9 minutes
- Architecture and safety patterns: 8 minutes
- Live demo: 8 minutes
- Hands-on lab: 26 minutes
- Debrief and quick check: 5 minutes

Arithmetic check: 4 + 9 + 8 + 8 + 26 + 5 = 60.

## Instructor setup checklist before class starts

- Open a working Tkinter project so you can code quickly without setup delay.
- Ensure you have an in-memory list of records ready in your editor.
- Ensure font size is readable for live coding.
- Keep a visible timer for segment discipline.
- Prepare to ask prediction questions before running code.
- Keep this hour tied to Day 5 continuity:
  - We used forms and validation last hour.
  - Now we add a record browser pattern around those forms.
- Do not re-teach deep validation internals from Hour 3.
- Keep terminology consistent:
  - list area
  - details pane
  - selection callback
  - refresh sequence
  - empty state
  - stale rows
  - duplicate rows

## Segment 1 script: recap and transition (4 minutes)

### Minute 0 to 1 opening

Instructor says:

Last hour we improved forms and validation feedback so users can enter data with fewer mistakes. That solved input quality, but a useful app also needs output visibility. Users need to see what already exists, select one item, and inspect details. In this hour, we complete that loop by building a record list UI.

### Minute 1 to 2 bridge from Hour 3

Instructor says:

Keep the continuity from Hour 3 simple: our form validates entries, and now this list view lets users browse existing records. We are not doing a deep validation redesign right now. We are focused on display, selection, and refresh safety.

### Minute 2 to 3 anchor question

Instructor asks:

If you have ten records, what is the user supposed to do without a list view?

Expected learner responses:

- They cannot tell what exists.
- They cannot choose one record to inspect.
- They may re-enter duplicates.
- The app feels incomplete.

Instructor reinforces:

Exactly. A record list is a usability feature and a correctness feature.

### Minute 3 to 4 preview of flow

Instructor says:

Our flow this hour is simple and practical:
- compare Listbox and Treeview
- bind a selection callback
- display selected record details
- refresh safely with no stale or duplicate rows
- verify empty and no-selection behavior with explicit acceptance checks

## Segment 2 script: concepts and talk points (9 minutes)

### Minute 4 to 7 Listbox vs Treeview

Instructor says:

Let us compare the two common widgets.

Listbox is best when:
- each row is a single string
- display is simple
- fields are compressed into one line
- you do not need multiple explicit columns

Treeview is best when:
- records have multiple fields
- table-like readability matters
- users benefit from column structure
- later you might add sorting, filtering, or richer row identity

Instructor prompt:

Given records with id, name, email, and status, which widget gives better clarity?

Expected answer:
- Treeview, because columns match fields directly.

Instructor says:

That is the default choice for this hour. We still mention Listbox because the design decision matters.

### Minute 7 to 10 selection callbacks

Instructor says:

Displaying rows is not enough. The interface must react when the user selects a row. In Tkinter ttk Treeview, we bind the selection event and call a function.

Instructor writes short concept snippet:

```python
self.tree.bind("<<TreeviewSelect>>", self.on_select)
```

Instructor says:

The callback must handle three states safely:
- one valid selection
- no selection
- selection points to a record that no longer exists in source data

If we do not protect these states, the callback can crash or show stale details.

### Minute 10 to 13 refresh safety talk point

Instructor says:

Refreshing is the most common source of duplicate rows in beginner UI code. The safe sequence is non-negotiable:

- clear existing rows or items
- repopulate from source
- handle selection state safely

Write this sequence on screen and repeat it twice.

Instructor says:

If you skip the clear step, you may stack old rows and new rows together. If you skip selection handling, your details pane may show old values that no longer match the visible list.

Instructor quick ask:

What can go wrong if refresh runs three times without clearing?

Expected answer:
- each run can add copies, row count inflates, details may mismatch, UI becomes misleading.

## Segment 3 script: architecture and safety patterns (8 minutes)

### Minute 13 to 17 responsibility boundaries for this hour

Instructor says:

We keep boundaries practical, not theoretical.

Data source responsibility:
- provide a list of records
- provide lookup by id

UI responsibility:
- render rows
- capture selection
- show details
- refresh view safely
- show fallback text for empty/no-selection states

Instructor says:

This is enough architecture for Hour 20. We are not doing Day 6 callback-spaghetti architecture deep dive today.

### Minute 17 to 19 no-selection and empty-data safety pattern

Instructor says:

Two acceptance checks are mandatory:

No-selection acceptance check:
- if nothing is selected, app throws no error
- details pane shows fallback text

Empty-data acceptance check:
- list area renders empty state safely
- details pane renders fallback safely
- refresh with empty source does not crash

Instructor asks:

What fallback text is clear and user-friendly?

Expected answer:
- No record selected
- No records available

Instructor says:

Yes. Clarity beats cleverness.

### Minute 19 to 21 repeated-refresh safety pattern

Instructor says:

We also require a repeated-refresh acceptance check:
- run refresh three consecutive times
- row count remains correct every time
- no stale rows
- no duplicate rows

Instructor says:

This check catches fragile refresh code quickly. We will use it in the lab pass/fail rubric.

## Segment 4 script: live demo (8 minutes)

### Demo objective

Build a compact Treeview-based record browser where:
- rows load from in-memory data
- selection updates details pane
- no-selection is safe
- empty-data is safe
- repeated refreshes do not duplicate rows

### Instructor narration before coding

Instructor says:

Watch for three patterns while I code:
- binding selection callback
- refresh sequence discipline
- fallback behavior for no selection and no data

### Live demo code

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass(slots=True)
class Record:
    record_id: int
    name: str
    email: str
    role: str


class InMemoryRecordService:
    def __init__(self) -> None:
        self._records: list[Record] = [
            Record(1, "Ada Lovelace", "ada@example.com", "Analyst"),
            Record(2, "Grace Hopper", "grace@example.com", "Engineer"),
            Record(3, "Katherine Johnson", "katherine@example.com", "Scientist"),
        ]

    def list_records(self) -> list[Record]:
        return list(self._records)

    def get_record_by_id(self, record_id: int) -> Record | None:
        for item in self._records:
            if item.record_id == record_id:
                return item
        return None

    def clear_all(self) -> None:
        self._records.clear()

    def seed_default(self) -> None:
        self._records = [
            Record(1, "Ada Lovelace", "ada@example.com", "Analyst"),
            Record(2, "Grace Hopper", "grace@example.com", "Engineer"),
            Record(3, "Katherine Johnson", "katherine@example.com", "Scientist"),
        ]


class RecordBrowserApp:
    def __init__(self, root: tk.Tk, service: InMemoryRecordService) -> None:
        self.root = root
        self.service = service

        self.root.title("Hour 20 Record Browser")
        self.root.geometry("980x420")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.status_var = tk.StringVar(value="Ready")
        self.detail_name = tk.StringVar(value="No record selected")
        self.detail_email = tk.StringVar(value="-")
        self.detail_role = tk.StringVar(value="-")
        self.count_var = tk.StringVar(value="Rows: 0")

        self._build_ui()
        self.refresh_records()

    def _build_ui(self) -> None:
        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")
        main.columnconfigure(0, weight=3)
        main.columnconfigure(1, weight=2)
        main.rowconfigure(1, weight=1)

        controls = ttk.Frame(main)
        controls.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        controls.columnconfigure(0, weight=1)

        title = ttk.Label(controls, text="Records")
        title.grid(row=0, column=0, sticky="w")

        refresh_btn = ttk.Button(controls, text="Refresh", command=self.refresh_records)
        refresh_btn.grid(row=0, column=1, padx=(8, 0))

        clear_btn = ttk.Button(controls, text="Clear Source", command=self.clear_source_data)
        clear_btn.grid(row=0, column=2, padx=(8, 0))

        seed_btn = ttk.Button(controls, text="Seed Source", command=self.seed_source_data)
        seed_btn.grid(row=0, column=3, padx=(8, 0))

        count_label = ttk.Label(controls, textvariable=self.count_var)
        count_label.grid(row=0, column=4, padx=(12, 0))

        self.tree = ttk.Treeview(
            main,
            columns=("name", "email", "role"),
            show="headings",
            selectmode="browse",
            height=12,
        )
        self.tree.grid(row=1, column=0, sticky="nsew", padx=(0, 12))
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("role", text="Role")
        self.tree.column("name", width=180, anchor="w")
        self.tree.column("email", width=240, anchor="w")
        self.tree.column("role", width=130, anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        details = ttk.LabelFrame(main, text="Details", padding=10)
        details.grid(row=1, column=1, sticky="nsew")
        details.columnconfigure(1, weight=1)

        ttk.Label(details, text="Name").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Label(details, textvariable=self.detail_name).grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(details, text="Email").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(details, textvariable=self.detail_email).grid(row=1, column=1, sticky="w", pady=5)

        ttk.Label(details, text="Role").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(details, textvariable=self.detail_role).grid(row=2, column=1, sticky="w", pady=5)

        status = ttk.Label(main, textvariable=self.status_var)
        status.grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 0))

    def clear_details(self, message: str = "No record selected") -> None:
        self.detail_name.set(message)
        self.detail_email.set("-")
        self.detail_role.set("-")

    def refresh_records(self) -> None:
        existing = self.tree.get_children()
        if existing:
            self.tree.delete(*existing)

        records = self.service.list_records()

        for item in records:
            self.tree.insert(
                "",
                "end",
                iid=str(item.record_id),
                values=(item.name, item.email, item.role),
            )

        self.count_var.set(f"Rows: {len(records)}")

        if not records:
            self.clear_details("No records available")
            self.status_var.set("Refresh complete: 0 rows loaded")
            return

        selected = self.tree.selection()
        if not selected:
            self.clear_details("No record selected")
            self.status_var.set(f"Refresh complete: {len(records)} rows loaded")
            return

        selected_id_text = selected[0]
        try:
            selected_id = int(selected_id_text)
        except ValueError:
            self.clear_details("No record selected")
            self.status_var.set(f"Refresh complete: {len(records)} rows loaded")
            return

        record = self.service.get_record_by_id(selected_id)
        if record is None:
            self.clear_details("No record selected")
            self.status_var.set(f"Refresh complete: {len(records)} rows loaded")
            return

        self.show_details(record)
        self.status_var.set(f"Refresh complete: {len(records)} rows loaded")

    def on_select(self, _event: tk.Event) -> None:
        selected_items = self.tree.selection()
        if not selected_items:
            self.clear_details("No record selected")
            self.status_var.set("Selection cleared")
            return

        selected_id_text = selected_items[0]
        try:
            selected_id = int(selected_id_text)
        except ValueError:
            self.clear_details("No record selected")
            self.status_var.set("Selection parse issue handled safely")
            return

        record = self.service.get_record_by_id(selected_id)
        if record is None:
            self.clear_details("No record selected")
            self.status_var.set("Selected row no longer exists")
            return

        self.show_details(record)
        self.status_var.set(f"Selected id {record.record_id}")

    def show_details(self, record: Record) -> None:
        self.detail_name.set(record.name)
        self.detail_email.set(record.email)
        self.detail_role.set(record.role)

    def clear_source_data(self) -> None:
        self.service.clear_all()
        self.refresh_records()

    def seed_source_data(self) -> None:
        self.service.seed_default()
        self.refresh_records()


def main() -> None:
    root = tk.Tk()
    service = InMemoryRecordService()
    RecordBrowserApp(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Demo facilitation script by minute

Minute 21 to 23:
- Create dataclass Record and service list_records and get_record_by_id.
- Say: service returns plain Python records, no widget knowledge.

Minute 23 to 25:
- Build Treeview and Details panel.
- Say: Treeview gives column clarity for multi-field records.

Minute 25 to 26:
- Bind selection event.
- Say: callback must survive empty selection state.

Minute 26 to 28:
- Implement refresh_records with strict sequence:
  - clear existing rows
  - repopulate from source
  - handle selection state safely
- Say this sequence aloud while typing.

Minute 28 to 29:
- Show no-selection fallback text by clicking empty area.
- Confirm no error occurs.

Minute 29:
- Trigger repeated refresh manually three times.
- Ask class to watch row count label.
- Confirm row count remains stable, no duplicates, no stale rows.

### Demo acceptance checks to model in front of students

- No-selection acceptance check:
  - Action: ensure nothing selected.
  - Expected: no exception, details pane shows fallback text.
- Empty-data acceptance check:
  - Action: clear source then refresh.
  - Expected: list empty, details fallback shows no records available, no exception.
- Repeated-refresh acceptance check:
  - Action: refresh three consecutive times.
  - Expected: row count unchanged and correct, no duplicate or stale rows.

## Segment 5 script: hands-on lab (26 minutes)

### Lab statement for learners

Build a list-and-details interface using in-memory records where:
- list area loads records
- selecting a row shows details
- refresh operation does not duplicate or stale rows
- no-selection and empty-data states are safe

You may use Treeview or Listbox. Treeview is recommended for multi-field records.

### Explicit lab technical requirement

Your refresh function must follow this exact wording and sequence:
- clear existing rows or items
- repopulate from source
- handle selection state safely

### Lab mini-budget with minute control

- Minute 29 to 33: scaffold UI layout
- Minute 33 to 39: load records into list area
- Minute 39 to 45: bind selection callback and details pane
- Minute 45 to 51: implement refresh safety and acceptance checks
- Minute 51 to 55: instructor circulation and focused fixes
- Optional extension only in final 3 to 5 minutes if core is complete

### Starter scaffold you can provide verbally or paste for class

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass(slots=True)
class Contact:
    contact_id: int
    name: str
    email: str
    city: str


class ContactService:
    def __init__(self) -> None:
        self._contacts: list[Contact] = [
            Contact(1, "Lin", "lin@example.com", "Boston"),
            Contact(2, "Mina", "mina@example.com", "Austin"),
            Contact(3, "Diego", "diego@example.com", "Seattle"),
        ]

    def list_contacts(self) -> list[Contact]:
        return list(self._contacts)

    def get_contact(self, contact_id: int) -> Contact | None:
        for item in self._contacts:
            if item.contact_id == contact_id:
                return item
        return None


class App:
    def __init__(self, root: tk.Tk, service: ContactService) -> None:
        self.root = root
        self.service = service

        self.name_var = tk.StringVar(value="No record selected")
        self.email_var = tk.StringVar(value="-")
        self.city_var = tk.StringVar(value="-")

        self._build_ui()
        self.refresh_contacts()

    def _build_ui(self) -> None:
        main = ttk.Frame(self.root, padding=10)
        main.grid(row=0, column=0, sticky="nsew")
        main.columnconfigure(0, weight=3)
        main.columnconfigure(1, weight=2)
        main.rowconfigure(1, weight=1)

        ttk.Button(main, text="Refresh", command=self.refresh_contacts).grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )

        self.tree = ttk.Treeview(main, columns=("name", "email", "city"), show="headings")
        self.tree.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("city", text="City")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        details = ttk.LabelFrame(main, text="Details", padding=8)
        details.grid(row=1, column=1, sticky="nsew")
        details.columnconfigure(1, weight=1)

        ttk.Label(details, text="Name").grid(row=0, column=0, sticky="w")
        ttk.Label(details, textvariable=self.name_var).grid(row=0, column=1, sticky="w")
        ttk.Label(details, text="Email").grid(row=1, column=0, sticky="w")
        ttk.Label(details, textvariable=self.email_var).grid(row=1, column=1, sticky="w")
        ttk.Label(details, text="City").grid(row=2, column=0, sticky="w")
        ttk.Label(details, textvariable=self.city_var).grid(row=2, column=1, sticky="w")

    def clear_details(self, message: str = "No record selected") -> None:
        self.name_var.set(message)
        self.email_var.set("-")
        self.city_var.set("-")

    def refresh_contacts(self) -> None:
        children = self.tree.get_children()
        if children:
            self.tree.delete(*children)

        contacts = self.service.list_contacts()

        for item in contacts:
            self.tree.insert(
                "",
                "end",
                iid=str(item.contact_id),
                values=(item.name, item.email, item.city),
            )

        if not contacts:
            self.clear_details("No records available")
            return

        self.clear_details("No record selected")

    def on_select(self, _event: tk.Event) -> None:
        selected = self.tree.selection()
        if not selected:
            self.clear_details("No record selected")
            return

        try:
            contact_id = int(selected[0])
        except ValueError:
            self.clear_details("No record selected")
            return

        contact = self.service.get_contact(contact_id)
        if contact is None:
            self.clear_details("No record selected")
            return

        self.name_var.set(contact.name)
        self.email_var.set(contact.email)
        self.city_var.set(contact.city)


def main() -> None:
    root = tk.Tk()
    root.title("Lab Starter")
    root.geometry("900x380")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    App(root, ContactService())
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Lab facilitation script, near-verbatim

Minute 29 to 31:

Instructor says:

Start with your visual structure only. Do not jump to extra features. Build one frame for list area and one frame for details pane. Add the refresh button now so you keep workflow visible from the beginning.

Minute 31 to 33:

Instructor says:

Set the details pane with default fallback text first. That way empty and no-selection states are already safe before callbacks are wired.

Minute 33 to 36:

Instructor says:

Now populate your list from in-memory records. If you use Treeview, keep columns simple. If you use Listbox, display one clear summary line per record.

Minute 36 to 39:

Instructor says:

Implement refresh sequence exactly in this order:
- clear existing rows or items
- repopulate from source
- handle selection state safely

If your order differs, correct it now before proceeding.

Minute 39 to 42:

Instructor says:

Bind your selection event and fetch the selected record by id. Do not assume selection exists. Guard the empty case first, then process valid selection.

Minute 42 to 45:

Instructor says:

Update details pane on valid selection. Keep fallback text for invalid or missing selection. This is where many crashes happen if guard logic is missing.

Minute 45 to 48:

Instructor says:

Run acceptance checks:
- no-selection acceptance check
- empty-data acceptance check
- repeated-refresh acceptance check with three consecutive refreshes

Minute 48 to 51:

Instructor says:

If repeated refresh produces duplicates, inspect your clear step first. If details pane shows stale content after refresh, inspect your selection-state handling.

Minute 51 to 55:

Instructor says:

Polish only after core completion criteria are fully green. If core is still unstable, spend this time on safety and clarity, not on visual styling.

### Lab pass/fail checks for instructor circulation

Mark pass only when all core checks are true.

Core check 1:
- list loads records from source
- pass evidence: visible rows match source count

Core check 2:
- selecting a row shows corresponding details
- pass evidence: details values update correctly for at least two different selections

Core check 3:
- refreshing does not duplicate rows
- pass evidence: after three consecutive refreshes, row count remains correct and stable

Core check 4:
- no-selection behavior is safe
- pass evidence: no exception and fallback text is visible when nothing is selected

Core check 5:
- empty-data behavior is safe
- pass evidence: with empty source, list shows zero rows and details pane shows safe fallback

### Common pitfalls and correction prompts

Pitfall:
- selection callback fails when no selection exists

Correction prompt:
- Show me where you handle empty tuple from selection.

Pitfall:
- stale or duplicate rows after refresh

Correction prompt:
- Show me clear step before insert loop.

Pitfall:
- details pane still shows old record after source was emptied

Correction prompt:
- After refresh, where do you reset details fallback state.

Pitfall:
- row id parsing crash

Correction prompt:
- Where do you handle conversion failure safely.

Pitfall:
- logic order drift in refresh

Correction prompt:
- Say the sequence out loud and match your code order exactly.

### Optional extension policy and timebox

Optional extension is allowed only if all core checks are passing and only during final 3 to 5 minutes of lab time.

Extension:
- add simple search/filter field for in-memory records

Guardrails:
- do not rework architecture
- do not add persistence
- do not add unrelated features
- do not break refresh sequence discipline

Optional extension snippet for fast finishers:

```python
self.filter_var = tk.StringVar(value="")
entry = ttk.Entry(controls, textvariable=self.filter_var, width=20)
entry.grid(row=0, column=5, padx=(8, 0))
ttk.Button(controls, text="Apply Filter", command=self.refresh_records).grid(row=0, column=6, padx=(8, 0))
```

```python
def refresh_records(self) -> None:
    existing = self.tree.get_children()
    if existing:
        self.tree.delete(*existing)

    query = self.filter_var.get().strip().lower()
    records = self.service.list_records()

    if query:
        records = [
            r for r in records
            if query in r.name.lower() or query in r.email.lower() or query in r.role.lower()
        ]

    for item in records:
        self.tree.insert("", "end", iid=str(item.record_id), values=(item.name, item.email, item.role))

    if not records:
        self.clear_details("No records available")
        return

    self.clear_details("No record selected")
```

Instructor says:

If you start this extension before your core checks pass, pause and return to core behavior first.

## Segment 6 script: debrief and quick check (5 minutes)

### Minute 55 to 57 group debrief

Instructor says:

Today we completed the missing half of a usable GUI workflow. Forms let users create or edit records. List views let users browse existing records. Selection callbacks connect the two experiences.

Instructor says:

The strongest submissions are not the fanciest ones. The strongest submissions are stable under edge cases:
- no selection
- empty data
- repeated refreshes

### Minute 57 to 59 quick check prompts

Prompt 1:

What can go wrong if you refresh without clearing existing rows?

Expected answer:

Rows can duplicate, stale records remain visible, row count becomes inaccurate, and details may no longer represent current source data.

Prompt 2:

What must happen when no row is selected?

Expected answer:

No error should occur, and details pane should show fallback text.

Prompt 3:

How do you confirm refresh safety quickly?

Expected answer:

Run refresh three consecutive times and verify row count remains correct with no duplicates or stale rows.

### Minute 59 to 60 close and handoff

Instructor says:

Before we finish, verify your app meets the three core completion criteria:
- list loads records
- selecting shows details
- refreshing does not duplicate rows

Then verify both safety checks:
- no-selection safe fallback
- empty-data safe fallback

If all are true, your Hour 20 objective is complete.

## Full instructor talk track reference

Use this extended script when you want near-verbatim pacing support across the full hour.

### Opening narrative

Instructor says:

Welcome to Hour 20. In this segment we build record list behavior that users depend on every day in real applications. We already practiced form inputs. Now we make records visible, selectable, and refreshable without instability. The skill target is not just to make rows appear once. The target is to make the interaction reliable under normal use and edge cases.

Instructor says:

When users click refresh, they trust the app to show current truth. If old rows remain mixed with new rows, the interface lies. If a no-selection state crashes callback logic, users lose trust immediately. So today is a quality and reliability hour, not only a widget hour.

### Concept reinforcement narrative

Instructor says:

Treeview and Listbox are both valid tools. The right tool depends on your data shape and readability needs. If each row is one short label, Listbox is enough. If each row needs multiple visible fields, Treeview is usually better. For our records today, we want clear columns and deterministic selection identity, so Treeview is our default.

Instructor says:

The callback pattern is event driven. A selection event triggers function execution. The callback reads selection state, validates it, then updates details pane. That sounds simple, but the safety details matter:
- selection may be empty
- selected id may parse badly
- selected id may no longer exist in source data
- source data may be empty right now

Instructor says:

If your callback handles those states calmly, your app feels professional even when data changes quickly.

### Safety pattern reinforcement narrative

Instructor says:

Say this with me:
- clear existing rows
- repopulate from source
- handle selection state safely

Repeat it again:
- clear existing rows
- repopulate from source
- handle selection state safely

Instructor says:

This sequence protects your UI from duplication and stale rendering. It also protects your details pane from presenting mismatched information.

Instructor says:

One more requirement for this hour is repeated-refresh confidence. We do not stop at one click that happens to work. We test three consecutive refresh actions and confirm row count stability. That reveals hidden duplication quickly.

### Lab coaching narrative for mixed learner pace

Instructor says:

If you are moving fast, do not rush into optional features yet. First prove your app survives the acceptance checks. If you are stuck, focus on one path:
- render rows
- bind selection
- show details
- pass safety checks

Instructor says:

When debugging callback failures, inspect from top to bottom:
- is event bound
- does selection exist
- can selected id parse
- can source resolve selected id
- does details pane update on success
- does fallback text update on failure

Instructor says:

When debugging duplicate rows:
- inspect refresh function order
- verify clear call runs before insertion
- verify you are not inserting in both constructor and refresh unintentionally
- verify refresh is not bound multiple times accidentally

### Rubric language for learner confidence

Instructor says:

Passing this hour does not require a perfect visual design. Passing this hour requires stable behavior and correct flow. If your styling is simple but your selection and refresh logic are robust, that is a strong result.

Instructor says:

You can show mastery by demonstrating these five behaviors in under one minute:
- load list
- click a row and see details
- clear selection and show fallback
- refresh three times with stable row count
- empty source and show safe empty state

### Verbal checklist before class exit

Instructor says:

Do this quick final checklist in your own project:
- My list loads records from in-memory source.
- My selected row populates details pane.
- My refresh follows clear then repopulate then selection-safe handling.
- My no-selection state never crashes and shows fallback text.
- My empty-data state never crashes and shows fallback text.
- My three refresh test keeps correct row count with no duplicates.

Instructor says:

If all items are true, you achieved Hour 20 outcomes and are ready to carry this pattern into your larger application.

## Learner-facing handout text you can read aloud

Use this as a concise statement to keep students aligned.

- Build list and details behavior first.
- Keep refresh sequence strict.
- Protect callback against empty selection.
- Verify empty-data behavior.
- Verify repeated-refresh stability.
- Only add search/filter in final 3 to 5 minutes and only if core is fully stable.

## Troubleshooting script bank for instructor use

### Case 1: callback raises index error

Instructor says:

Your code is reading selected item zero before checking whether a selection exists. Add an early guard:
- if not selected, show fallback and return.

### Case 2: duplicate rows after refresh

Instructor says:

Your clear call is missing or runs after inserts. Move clear to the top of refresh before any insertion loop.

### Case 3: details pane still shows old data after source emptied

Instructor says:

After repopulation, if list is empty, explicitly set details fallback text and return early.

### Case 4: selected id conversion fails

Instructor says:

Use a protected conversion path. If conversion fails, fallback and return safely.

### Case 5: row count keeps growing after refresh

Instructor says:

Your refresh may be called repeatedly by multiple triggers or clear step may not target current widget children. Inspect clear logic and event binding duplicates.

### Case 6: learner used Listbox and cannot map to full record

Instructor says:

Store id alongside display text or maintain a mapping dictionary from list index to record id. Then callback can resolve the selected record reliably.

## Advanced facilitation cues for strong groups

- Ask learners to explain why fallback text is a user experience feature, not just an error guard.
- Ask learners to predict behavior before each acceptance check.
- Ask learners to identify one line that enforces refresh safety and one line that enforces callback safety.
- Ask learners to describe how this pattern integrates with the Hour 3 form workflow.
- Ask learners to identify where stale state can enter and how their code removes it.

## Reinforcement examples for concept transfer

Use these short scenario prompts to help transfer beyond the current app.

Scenario A:
- Inventory tool with columns item, location, quantity.
- Ask: Treeview or Listbox and why.
- Expected: Treeview for multi-column clarity.

Scenario B:
- Notes app with one title string per note.
- Ask: Listbox acceptable.
- Expected: yes, if one-line display is enough.

Scenario C:
- Source data becomes empty after user action.
- Ask: what should details pane show.
- Expected: safe empty fallback text.

Scenario D:
- User clicks refresh rapidly.
- Ask: what verifies correctness.
- Expected: repeated-refresh row count stability.

Scenario E:
- Selection disappears after refresh.
- Ask: callback behavior.
- Expected: no crash, fallback text displayed.

## Completion rubric for grading or checkoff

Use this rubric during final 5 minutes or after class.

### Required criteria

Criterion 1:
- list loads records
- pass if visible row count matches source length

Criterion 2:
- selecting shows details
- pass if two different selections correctly update details

Criterion 3:
- refreshing does not duplicate rows
- pass if three consecutive refreshes preserve correct row count with no duplicates

Criterion 4:
- no-selection acceptance check
- pass if no exception and fallback text shown

Criterion 5:
- empty-data acceptance check
- pass if empty list and safe details fallback shown after source emptied and refresh executed

### Common fail signals

- callback assumes selection always exists
- refresh inserts without clearing
- details pane retains stale data after source change
- empty source triggers exception
- repeated refresh inflates row count

### Recovery path if learner fails one criterion

- isolate failing function
- run only one acceptance check at a time
- patch guard condition first
- rerun full five-criterion check

## End-of-hour reflection prompts

Ask one or two based on time.

- What changed in your code after you added no-selection guards?
- Where exactly do you clear old rows in refresh?
- How did you prove rows are not duplicated after repeated refreshes?
- What fallback messages did you choose and why?
- Why is a stable empty state important for user trust?

## Final instructor summary paragraph

This hour establishes a practical desktop pattern that learners will reuse often: list records clearly, react to selection safely, and refresh without duplicating or staling the visible state. The key discipline is the refresh sequence and defensive callback handling. If learners can demonstrate stable behavior for no selection, empty data, and three consecutive refreshes with accurate row count, they have met Hour 20 outcomes in a way that is production-minded, user-friendly, and immediately transferable to larger GUI workflows.

(agent_id: issue298-hour4-rewrite — use write_agent to send follow-up messages)