# Advanced Day 5 — Session 5 (Hours 17–20)
Python Programming (Advanced) • GUI Foundations for the Tracker Capstone

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 5 overview (Hours 17–20); Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Instructor Notes -->

---

# Session 5 Overview

## Topics Covered Today
- Hour 17: GUI fundamentals with Tkinter / `ttk`
- Hour 18: Layout, spacing, and resizing
- Hour 19: Forms, validation, and user feedback
- Hour 20: Record lists, selection, and refresh

## Today's Capstone Milestone
- Move from CLI-style flow to event-driven desktop workflow
- Keep the **service layer** as the home for business rules
- Start building a tracker UI that can grow into CRUD workflows

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 5 overview (Hours 17–20); Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Section 1: Recap and Transition -->

---

## Homework + Quiz Emphasis

- Build one working GUI action first
- Use `grid()` intentionally for readable forms
- Show validation feedback without crashes
- Bind record selection to a **stable ID**, not display order

### Canonical quiz/contracts to recognize
- `Hour 17 | root window: tracker app`
- `Hour 18 | layout manager: grid`
- `Hour 19 | field read: title entry`
- `Hour 20 | list widget: treeview`

<!-- Sources: Advanced/assignments/Advanced_Day5_homework.ipynb — Part 1 through Part 4; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 17 through Hour 20 canonical contract questions -->

---

# Hour 17: GUI Fundamentals

## Learning Outcomes
- Explain why GUI programs are **event-driven**
- Create a small window with labels, entries, and buttons
- Wire a button to a callback
- Route validation through the service layer
- Show visible success/error feedback

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 17: GUI fundamentals (Tkinter/ttk): event loop, widgets, callbacks; Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Learning Outcomes for This Hour -->

---

## The Mental Model Shift

### CLI mindset
1. Start
2. Read input
3. Do work
4. Print output
5. Exit

### GUI mindset
- Open a window
- Wait for events
- React through callbacks
- Stay responsive until the user closes the app

**Key phrase**: The GUI handles interaction; the service layer handles rules.

<!-- Sources: Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Section 1: Recap and Transition; Section 2: The GUI Mental Model -->

---

## Core Building Blocks

- `mainloop()` keeps the app alive and listening
- `Label` shows text
- `Entry` captures user input
- `Button` triggers a callback
- `messagebox` gives simple popup feedback
- `StringVar` helps connect UI state to Python values

### Keep callbacks short
- Read form values
- Call the service
- Update the interface

<!-- Sources: Advanced/lessons/lecture/Day5_Hour1_Advanced.md — What mainloop() Does; Widgets and Callbacks; Demo Teaching Points to Repeat -->

---

## Thin Callback Pattern

```python
def on_add(self) -> None:
    try:
        record = self.service.add_record(
            self.name_var.get(),
            self.email_var.get(),
        )
    except ValidationError as exc:
        self.status_var.set(f"Error: {exc}")
        return

    self.status_var.set(f"Added {record.name}")
```

### Why this pattern works
- UI gathers input
- Service validates and stores
- UI presents the outcome

<!-- Sources: Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Section 3: Core Design Pattern for This Hour; Demo Code -->

---

## Demo: Hello GUI + Add Form

### Instructor flow
1. Create the service class first
2. Build a small `ContactApp` / tracker app class
3. Add two fields and an **Add** button
4. Wire `command=self.on_add`
5. Show one bad submission and one good submission
6. Point directly to `root.mainloop()`

### Watch for
- Where the widgets live
- Where the callback lives
- Where the validation rule lives

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Live demo (Hour 17); Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Demo Steps -->

---

## Lab: First Working GUI Action

**Time: 25–35 minutes**

### Tasks
- Create a Tkinter window for your tracker domain
- Add at least two inputs
- Add one working action button
- Show status or messagebox feedback
- Keep business rules outside the widget-building code

### Completion Criteria
✓ GUI launches reliably  
✓ One callback works end to end  
✓ Validation comes from a service/helper  
✓ User sees success or error clearly

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Hello GUI + Add form; Advanced/assignments/Advanced_Day5_homework.ipynb — Part 1: Hour 17 -->

---

## Common Pitfalls (Hour 17)

⚠️ Forgetting `mainloop()`  
⚠️ Writing `command=self.on_add()` instead of `command=self.on_add`  
⚠️ Burying business rules directly in callbacks  
⚠️ Clicking a button and giving the user no visible feedback

## Quick Check
**Question**: What does `mainloop()` do, and why should callbacks stay small?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 17 best practice and pitfall -->

---

# Hour 18: Layout and Usability

## Learning Outcomes
- Use `grid()` for form-style layouts
- Group related controls with frames
- Add consistent spacing and alignment
- Configure the layout to resize sensibly
- Avoid mixing geometry managers in the same parent

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 18: Layout and usability; Advanced/lessons/lecture/Day5_Hour2_Advanced.md — Learning Outcomes for This Hour -->

---

## `pack()` vs `grid()`

### Use `pack()` when
- You want simple stacking

### Use `grid()` when
- You need rows + columns
- You are building a form
- Labels and inputs should line up cleanly

> Do not mix `pack()` and `grid()` in the same parent widget.

<!-- Sources: Advanced/lessons/lecture/Day5_Hour2_Advanced.md — `pack()` and `grid()`; The Rule About Mixing Geometry Managers -->

---

## Layout Rules That Matter

- Use frames as layout boundaries
- Add consistent `padx` / `pady`
- Use `sticky="w"` or `sticky="ew"` intentionally
- Give growing columns a weight

```python
main_frame.columnconfigure(1, weight=1)
ttk.Entry(form_frame).grid(row=0, column=1, sticky="ew")
```

### Usability checklist
1. Are related items grouped?
2. Is spacing consistent?
3. Is the main action easy to find?
4. Does resize behavior make sense?

<!-- Sources: Advanced/lessons/lecture/Day5_Hour2_Advanced.md — Usability Principles for Basic Desktop GUIs; Column Weights and Resizing -->

---

## Demo: Refactor a Messy Layout

### Demo target
- One main frame
- Two visual regions
  - Form area
  - Preview/list area
- `grid()` for the form
- Safe nested `pack()` only inside a different parent such as a button bar

### Success signal
- The app looks intentional
- Resize behavior is acceptable

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Live demo (Hour 18); Advanced/lessons/lecture/Day5_Hour2_Advanced.md — Live Demo — Refactoring a Messy Layout -->

---

## Lab: Improve Layout and Resizing

**Time: 25–35 minutes**

### Tasks
- Rebuild the GUI using at least one frame
- Convert the form area to `grid()`
- Add consistent spacing
- Test the window at more than one size

### Completion Criteria
✓ UI is readable and aligned  
✓ Resizing does not break the layout  
✓ One layout strategy per container  
✓ Main action stays obvious

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Improve layout; Advanced/assignments/Advanced_Day5_homework.ipynb — Part 2: Hour 18 -->

---

## Common Pitfalls (Hour 18)

⚠️ Mixing `pack` and `grid` in the same container  
⚠️ Forgetting `sticky`, so fields do not align or stretch  
⚠️ Inconsistent padding  
⚠️ Never testing resize behavior

## Quick Check
**Question**: Why is `grid()` usually a better fit for forms?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 18 canonical contract and pitfall -->

---

# Hour 19: Forms, Validation, and Feedback

## Learning Outcomes
- Validate before saving
- Normalize input before checking rules
- Show friendly, actionable feedback
- Keep predictable validation out of crash paths
- Separate service validation from UI presentation

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 19: Forms + validation feedback patterns; Advanced/lessons/lecture/Day5_Hour3_Advanced.md — Learning Outcomes for This Hour -->

---

## Good Validation Helps the User Succeed

### Weak message
`Invalid input`

### Better message
`Email is required`

### Best message
`Enter an email address such as name@example.com`

### Normalize first
- `strip()` whitespace
- lowercase email-like fields
- clean obvious formatting noise before validation

<!-- Sources: Advanced/lessons/lecture/Day5_Hour3_Advanced.md — Validation Should Be Helpful, Not Punitive; Normalize Before You Validate -->

---

## Service vs UI Responsibilities

### Service layer
- Decides whether data is valid
- Returns structured errors or raises the right exception

### UI layer
- Places messages near the right field
- Moves focus to the first invalid control
- Clears old errors
- Resets the form after success

```python
errors = {
    "name": "Name is required.",
    "email": "Enter an email address such as name@example.com.",
}
```

<!-- Sources: Advanced/lessons/lecture/Day5_Hour3_Advanced.md — Service Errors vs UI Errors; A Clean Validation Pattern -->

---

## Demo: Validated Tracker Form

### Demo highlights
- Inline field-level errors
- Summary status message
- Disabled/re-enabled Save button during submit
- Focus moved to the first invalid field
- App stays stable after bad input

### Instructor prompt
Ask learners to identify:
1. Where `.strip()` happens
2. Where errors are structured
3. Why inline feedback often beats a popup

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Live demo (Hour 19); Advanced/lessons/lecture/Day5_Hour3_Advanced.md — Live Demo — Inline Validation and Actionable Feedback -->

---

## Lab: Validation Feedback Without Crashing

**Time: 25–35 minutes**

### Tasks
- Add required-field checks
- Normalize user input
- Display at least one inline error
- Add a summary status message
- Keep the app available for immediate correction

### Completion Criteria
✓ Missing data is rejected clearly  
✓ Errors are actionable  
✓ No raw traceback shown to the user  
✓ Valid entries save successfully

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Add validation UI; Advanced/assignments/Advanced_Day5_homework.ipynb — Part 3: Hour 19 -->

---

## Common Pitfalls (Hour 19)

⚠️ Silent failure after bad input  
⚠️ Vague messages with no next step  
⚠️ Treating predictable validation as a crash-worthy exception  
⚠️ Forgetting to clear old errors before the next save

## Quick Check
**Question**: Why is “Enter an email address such as name@example.com” better than “Invalid email”?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 19 best practice and pitfall -->

---

# Hour 20: Record Lists and Selection

## Learning Outcomes
- Show multiple records in a list or table
- Use `Treeview` or `Listbox` appropriately
- Refresh safely without duplicate stale rows
- React to selection events
- Map selection to a stable record ID

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 20: Record list UI; Advanced/lessons/lecture/Day5_Hour4_Advanced.md — Learning Outcomes for This Hour -->

---

## `Listbox` vs `Treeview`

### `Listbox`
- Lightweight
- Good for one visible string per row

### `Treeview`
- Better for multi-column records
- Good fit for tracker-style data
- Easier to grow into sorting and richer browsing

### Selection rule
Selection should lead to a **record ID**, not just a row position.

<!-- Sources: Advanced/lessons/lecture/Day5_Hour4_Advanced.md — Choosing the Right List Widget; Advanced/assignments/Advanced_Day5_homework.ipynb — Part 4: Hour 20 -->

---

## Safe Refresh Pattern

1. Clear existing rows
2. Fetch current records
3. Insert fresh rows
4. Reset or refresh the details pane

```python
self.tree.delete(*self.tree.get_children())
for record in records:
    self.tree.insert("", "end", iid=str(record.record_id), values=(...))
```

### Why this matters
- No duplicated rows
- No stale details
- No “selection points at the wrong thing” bug

<!-- Sources: Advanced/lessons/lecture/Day5_Hour4_Advanced.md — Refreshing Safely; Demo Code -->

---

## Demo: List + Details Browser

### Demo flow
- Add a `Treeview`
- Bind `<<TreeviewSelect>>`
- Show details for the selected record
- Add a Refresh button
- Handle empty-state cases safely

### Empty-state behavior
- Empty list is still a valid state
- No selection should clear or reset details

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: Treeview showing records; Advanced/lessons/lecture/Day5_Hour4_Advanced.md — Live Demo — Treeview with Selection and Details Pane -->

---

## Lab: Record Browser

**Time: 25–35 minutes**

### Tasks
- Add a list area for saved records
- Add a details pane
- Bind selection to a callback
- Add Refresh
- Show safe behavior when there are no records

### Completion Criteria
✓ List populates and updates  
✓ Details follow the selected record  
✓ No crash on empty selection  
✓ Refresh clears stale rows first

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: List + details; Advanced/assignments/Advanced_Day5_homework.ipynb — Part 4: Hour 20 -->

---

## Common Pitfalls (Hour 20)

⚠️ Using display order as identity  
⚠️ Not clearing old rows before refresh  
⚠️ Crashing when no selection exists  
⚠️ Leaving stale details visible after the list changes

## Quick Check
**Question**: What should happen if the user clicks Refresh when there are zero records?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 20 best practice and pitfall -->

---

# Session 5 Wrap-Up

## What We Built Toward
- Event-driven thinking instead of CLI-only flow
- A cleaner form layout with `grid()` and frames
- Validation that helps users recover
- A record browser that is safe to refresh and select

## Capstone checkpoint coming next
- Update + delete workflows
- Cleaner controller architecture
- JSON persistence + polish

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 5 overview; Advanced/lessons/lecture/Day5_Hour4_Advanced.md — Wrap-Up -->

---

## Scope Guardrails

### Stay in scope today
✓ Tkinter / `ttk` fundamentals  
✓ Small, maintainable callbacks  
✓ Service-layer validation  
✓ Stable IDs for selection

### Not today's goal
✗ Fancy theming  
✗ Framework switching  
✗ ORM/database work  
✗ Big “all-features-at-once” refactors

### Homework / quiz prep
- Be able to explain **why** `mainloop()` matters
- Be able to justify `grid()` for forms
- Be able to show a friendly validation path
- Be able to explain why stable IDs beat list positions

<!-- Sources: Advanced/lessons/lecture/Day5_Hour1_Advanced.md — Wrap-Up; Advanced/quizzes/Advanced_Day5_Quiz.html — Hour 17 through Hour 20 explanations -->

---

# Thank You!

Session 6 next:
- Update + delete through the GUI
- Controller cleanup
- JSON persistence and checkpoint demo

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 6 overview (Hours 21–24) -->
