# Advanced Day 6 — Session 6 (Hours 21–24)
Python Programming (Advanced) • GUI CRUD Wiring, Architecture, and Milestone Readiness

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 6 overview (Hours 21–24); Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Session context -->

---

# Session 6 Overview

## Topics Covered Today
- Hour 21: Update and delete workflows in the GUI
- Hour 22: Controller separation and callback cleanup
- Hour 23: JSON persistence and GUI polish
- Hour 24: Checkpoint 3 GUI milestone demo

## Day goal
- Turn a promising interface into a trustworthy mini-application
- Keep stable IDs as the bridge between UI state and domain operations

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 6 overview (Hours 21–24); Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Session context -->

---

## Homework + Quiz Emphasis

- Round-trip update/delete through the current source of truth
- Refactor into a controller-style app structure
- Add JSON load/save before the GUI checkpoint
- Practice the demo path, not just isolated screenshots

### Canonical quiz/contracts to recognize
- `Hour 21 | selected id: task-002`
- `Hour 22 | ui class: TrackerApp`
- `Hour 23 | persistence hook: save on demand`
- `Hour 24 | demo start: app opens cleanly`

<!-- Sources: Advanced/assignments/Advanced_Day6_homework.ipynb — Part 1 through Part 4; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 21 through Hour 24 canonical contract questions -->

---

# Hour 21: Update and Delete Workflows

## Learning Outcomes
- Use **select → load → edit → save update**
- Delete with confirmation
- Refresh after each change
- Handle missing-record cases cleanly
- Target records by **stable ID**, not list index

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 21: CRUD wiring in GUI: update and delete workflows; Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Learning objectives -->

---

## Why Update/Delete Are Harder Than Add

### Create
- Read form
- Validate
- Save new record
- Refresh

### Update/Delete
- Identify the correct record
- Keep selection state accurate
- Avoid stale widgets after refresh
- Recover if the record is already gone

> Display order is not identity. Stable IDs are.

<!-- Sources: Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Why add is easy and update/delete are trickier; Stable IDs: the core design choice -->

---

## Standard Update Flow

1. User selects a record
2. UI loads that record into the form
3. User edits fields
4. UI sends `selected_id` + form values to the service
5. Service updates the correct record
6. UI refreshes the list and resets state intentionally

```python
service.update_item(selected_id, name, category, status, notes)
```

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Editing pattern: select -> load into form -> save update; Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Implement the standard GUI update flow -->

---

## Delete Flow and Confirmation

### Delete path
- Detect a valid selection
- Ask for confirmation
- Delete by ID
- Refresh the list
- Clear stale form values and selection

### User-facing rule
- Destructive actions should be explicit
- “No selection” is a normal state to handle

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Confirm delete with messagebox; Delete workflow, step by step; Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Graceful error handling with `messagebox` -->

---

## Demo: Wiring Update + Delete

### Instructor flow
1. Select a record in `Treeview`
2. Load values into the form
3. Update one field
4. Refresh and prove the correct record changed
5. Delete another record with confirmation
6. Show `NotFoundError` or missing-record handling gracefully

### Watch for
- Which value is the true ID
- What refresh does after each operation

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: update flow and delete confirmation; Show handling NotFoundError gracefully; Advanced/lessons/lecture/Day6_Hour1_Advanced.md — Live demo guidance -->

---

## Lab: GUI Update/Delete Round Trip

**Time: 25–35 minutes**

### Tasks
- Implement Update using the selected record
- Implement Delete with confirmation
- Refresh the list after each change
- Clear or reset stale form state

### Completion Criteria
✓ Update works reliably  
✓ Delete works reliably  
✓ UI stays in sync after each change  
✓ Selection maps to a stable ID

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Update/Delete; Advanced/assignments/Advanced_Day6_homework.ipynb — Part 1: Hour 21 -->

---

## Common Pitfalls (Hour 21)

⚠️ Mutating stale widget state without reloading  
⚠️ Using list index as the real ID  
⚠️ Deleting while the UI still points at stale selection  
⚠️ Forgetting to refresh after update/delete

## Quick Check
**Question**: Why is a stable ID better than relying on a visual row index?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 21 best practice and pitfall -->

---

# Hour 22: GUI Architecture and Controller Separation

## Learning Outcomes
- Recognize callback spaghetti
- Refactor toward an `App` / controller class
- Keep callbacks thin
- Separate widget creation from service logic
- Manage selection and status state clearly

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 22: GUI architecture; Advanced/lessons/lecture/Day6_Hour2_Advanced.md — Learning objectives -->

---

## What Callback Spaghetti Looks Like

- Top-level functions with unclear ownership
- Globals for widgets and selection state
- Duplicate form-reading code
- Duplicate refresh code
- Business rules embedded directly in callbacks
- Fragile bugs when state changes in one place but not another

### Smell test
If adding one button means editing scattered unrelated code, structure is the problem.

<!-- Sources: Advanced/lessons/lecture/Day6_Hour2_Advanced.md — What callback spaghetti looks like -->

---

## Target Architecture

### Model / domain
- `TrackerItem`
- Exceptions

### Service layer
- Add, update, delete, list, get by ID

### UI / controller class
- Builds widgets
- Reads form values
- Calls the service
- Refreshes the screen
- Owns selection + status state

```text
widgets -> App/controller -> service -> model
```

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Thin UI callbacks call service layer; Advanced/lessons/lecture/Day6_Hour2_Advanced.md — The target structure for this capstone -->

---

## Demo: Refactor into `TrackerApp`

### Refactor target methods
- `build_ui()`
- `refresh()`
- `on_add()`
- `on_update()`
- `on_delete()`
- `load_selected_record()`

### Key rule
- Change one boundary at a time
- Preserve working behavior while cleaning structure

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Refactor to an App class with methods: build_ui(), refresh(), on_add(), on_delete(); Advanced/lessons/lecture/Day6_Hour2_Advanced.md — Refactoring into an `App` controller class -->

---

## Lab: Refactor Without Breaking Behavior

**Time: 25–35 minutes**

### Tasks
- Create an `App` class that owns the UI
- Move service calls out of widget construction code
- Keep callbacks small and readable
- Verify that behavior is unchanged after the refactor

### Completion Criteria
✓ Code is easier to read  
✓ Functionality is preserved  
✓ State ownership is clearer  
✓ Circular imports are avoided

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Refactor GUI; Advanced/assignments/Advanced_Day6_homework.ipynb — Part 2: Hour 22 -->

---

## Common Pitfalls (Hour 22)

⚠️ Over-refactoring midstream and breaking working code  
⚠️ Callback spaghetti hidden inside a class instead of removed  
⚠️ Circular imports between UI and service modules  
⚠️ Letting the controller become the business brain

## Quick Check
**Question**: What is one sign that your GUI code needs refactoring?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 22 explanation -->

---

# Hour 23: Persistence + Polish Sprint

## Learning Outcomes
- Load JSON on startup
- Save after add/update/delete
- Handle missing or invalid JSON gracefully
- Add one small usability improvement
- Prepare for a confident checkpoint demo

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 23: GUI mini-project sprint: persistence + polish; Advanced/lessons/lecture/Day6_Hour3_Advanced.md — Learning objectives -->

---

## Why JSON Is the Right Milestone Here

- JSON is transparent and easy to inspect
- JSON is portable and simple to debug
- JSON is enough for **this** milestone
- SQLite comes next session

### Sequencing matters
- Good architecture today makes the storage swap easier tomorrow
- Stability beats novelty in a checkpoint week

<!-- Sources: Advanced/lessons/lecture/Day6_Hour3_Advanced.md — Why JSON now instead of SQLite now -->

---

## Persistence Hook Pattern

### Minimum behavior
- Load on startup
- Save after add
- Save after update
- Save after delete

### Optional polish
- File menu
- About/help dialog
- Status bar message
- Save shortcut such as `Ctrl+S`

**Quiz/homework cue**: `Hour 23 | persistence hook: save on demand`

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Load data on startup; save after changes; Advanced/assignments/Advanced_Day6_homework.ipynb — Part 3: Hour 23; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 23 canonical contract -->

---

## Demo: Load → Change → Save → Restart

### Instructor flow
1. Start the app and load records
2. Add or update one record
3. Save automatically or on demand
4. Restart the app
5. Prove data persisted
6. Show a calm error path for malformed JSON

### Design takeaway
- Persistence is part of user trust

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: start app -> load -> add -> save -> restart -> load; Advanced/lessons/lecture/Day6_Hour3_Advanced.md — Opening: why persistence changes the feel of an app -->

---

## Lab: Mini-Project Sprint

**Time: 25–35 minutes**

### Tasks
- Add load on startup and save after CRUD
- Handle missing/corrupt JSON without crashing
- Add one usability improvement
- Prepare a short milestone demo path

### Completion Criteria
✓ GUI persists data across runs  
✓ User feedback is clear  
✓ Core workflow works before visual polish  
✓ Restart behavior is demonstrable

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: GUI milestone sprint; Advanced/assignments/Advanced_Day6_homework.ipynb — Part 3: Hour 23 -->

---

## Common Pitfalls (Hour 23)

⚠️ Polishing visuals before save/load actually works  
⚠️ Forgetting to save after update/delete  
⚠️ Crashing on malformed JSON  
⚠️ Treating JSON as “temporary” and never testing restart behavior

## Quick Check
**Question**: What usability improvement did you add that you would want in a real tool?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 23 explanation -->

---

# Hour 24: Checkpoint 3 — GUI Milestone Demo

## Checkpoint outcome
- Launch the GUI
- Perform CRUD through the interface
- Prove JSON persistence across restart
- Explain where the service layer lives
- Explain how the app finds the correct record for update/delete

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 24: Checkpoint 3: GUI milestone demo; Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Learning objectives -->

---

## Required Demo Path

### Part A — Launch and orient
- Open the app cleanly
- Point out form, list, and feedback area

### Part B — CRUD
- Add a record
- Update the correct record
- Delete a record with confirmation

### Part C — Persistence
- Save if needed
- Close and reopen
- Show that records reload

<!-- Sources: Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Concrete learner demo prompt; Advanced/quizzes/Advanced_Day6_Quiz.html — Hour 24 canonical contract -->

---

## What the Checkpoint Rubric Rewards

- GUI works reliably
- Persistence works reliably
- Errors are handled reasonably
- Callbacks are not doing all the business logic
- Stable IDs are used instead of list positions
- Learner can explain one next improvement

### Best practice reminder
Checkpoint the **full path**, not isolated screenshots.

<!-- Sources: Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Concrete grading rubric; Advanced/assignments/Advanced_Day6_homework.ipynb — Part 4: Hour 24 -->

---

## Common Failure Modes to Triage

### If restart loses data
- Check save path
- Check JSON write timing
- Check that list reloads from saved data

### If update/delete hits the wrong record
- Print the selected ID
- Verify the service method uses that ID
- Confirm the UI cleared stale selection after refresh

### If the demo feels fragile
- Simplify the path
- Stabilize the required features first

<!-- Sources: Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Common failure modes and triage guidance -->

---

# Session 6 Wrap-Up

## What We Strengthened
- Real update/delete workflows
- Cleaner GUI architecture
- Persistence that survives restart
- A concrete checkpoint story

## Scope Guardrails
✓ Stable CRUD path  
✓ JSON persistence for this milestone  
✓ Clean UI/service boundary  
✓ Demo-ready behavior

✗ Not yet: database backend swap  
✗ Not required: heavy visual theming

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 6 overview; Advanced/lessons/lecture/Day6_Hour4_Advanced.md — Debrief and next-step reflection -->

---

# Thank You!

Session 7 next:
- From objects to tables
- SQLite CRUD with safe queries
- Row mapping and database hardening

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 7 overview (Hours 25–28) -->
