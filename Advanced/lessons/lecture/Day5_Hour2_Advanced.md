# Day 5, Hour 2: Layout and Usability with `grid`, `pack`, Spacing, and Resizing

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 5
- **Hour**: 2 of 4 for this session, corresponding to **Hour 18** in the 48-hour runbook
- **Focus**: Layout and usability — `grid()`, `pack()`, frames, spacing, alignment, resizing
- **Runbook alignment**: Use `grid()` for forms; introduce `sticky` and padding; group UI with frames; demonstrate `columnconfigure()` weight; refactor a messy UI into a cleaner layout
- **Prerequisites**:
  - Students can create a basic Tkinter window
  - Students have seen `Label`, `Entry`, `Button`, callbacks, and `mainloop()`
- **Teaching goal**: Move students from “it works” to “it is readable, intentional, and usable”
- **Demo app theme**: Continue the contact-entry app, but restructure its layout
- **Key message to repeat**: “A working layout is not automatically a good layout.”
- **Success criteria for the hour**:
  - Students can explain when `grid()` is preferable to `pack()`
  - Students can use frames to divide the interface into sections
  - Students can apply consistent padding and alignment
  - Students can explain why you should not mix `pack` and `grid` in the same parent

---

## Timing Overview

| Segment | Time |
|---|---:|
| Recap and transition from basic widgets to layout | 5 minutes |
| Layout managers: `pack` vs `grid` and when to use each | 12 minutes |
| Usability basics: grouping, spacing, alignment, resizing | 10 minutes |
| Live demo: refactor a messy GUI into frames with clean layout | 13 minutes |
| Hands-on lab: improve layout and resizing behavior | 15 minutes |
| Debrief, quick checks, exit ticket, wrap-up | 5 minutes |

**Total:** 60 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, students should be able to:

1. Explain the difference between `pack()` and `grid()`.
2. Use `Frame` and `LabelFrame` widgets to group related UI elements.
3. Build form layouts with `grid()` and consistent padding.
4. Use `sticky` effectively for alignment and resizing behavior.
5. Configure row and column weights for reasonable window resizing.
6. Avoid mixing `pack` and `grid` in the same parent container.
7. Apply a simple usability checklist to improve a basic GUI.

---

## Section 1: Recap and Transition (5 minutes)

### Quick Re-entry

**[Instructor speaks:]**

In the previous hour, we built a GUI that worked. That was the right first step. But a GUI can be technically correct and still feel awkward to use.

Students quickly notice this when:

- labels do not line up
- fields are cramped
- buttons float in odd positions
- resizing makes the interface look broken
- related content is not visually grouped

This hour is about making the interface feel deliberate.

### Framing the Hour

**[Instructor speaks:]**

Today is not about adding brand-new business features. Today is about improving structure and usability.

Our major tools are:

- frames for organization
- `grid()` for form layouts
- `padx` and `pady` for consistent spacing
- `sticky` for alignment
- row and column weights for sensible resizing

The goal is not perfection. The goal is to give students a reliable layout vocabulary they can use repeatedly.

---

## Section 2: Layout Managers and Parent Containers (12 minutes)

### `pack()` and `grid()`

**[Instructor speaks:]**

Tkinter gives us multiple geometry managers. The two most important for our course are:

- `pack()`
- `grid()`

A practical rule of thumb is:

- use `pack()` when you want simple stacking
- use `grid()` when you want rows and columns, especially in forms

### Why Forms Usually Prefer `grid()`

**[Instructor speaks:]**

Forms naturally want structure:

- label on the left
- input field on the right
- maybe an error label underneath
- buttons at the bottom
- status or summary line below

That is exactly what rows and columns are for. Trying to force a moderately complex form into `pack()` often becomes awkward and inconsistent.

### The Rule About Mixing Geometry Managers

**[Instructor speaks:]**

Here is the most important layout rule of the hour:

> Do not mix `pack()` and `grid()` in the same parent widget.

That means if `form_frame` contains widgets positioned with `grid()`, then the direct children of `form_frame` should all use `grid()`.

However, it is perfectly fine to use different geometry managers in different containers. For example:

- `main_frame.pack(...)`
- inside `main_frame`, use `grid()` for the form
- inside a nested `button_bar`, use `pack()` for the buttons

The restriction is about the **same parent**, not the entire application.

### Frames as Layout Boundaries

**[Instructor speaks:]**

Frames do more than group widgets visually. They also give us layout boundaries.

That means frames let us say:

- this area is the form
- this area is the list or preview
- this area is the button bar
- this area is the status section

That is valuable because good interfaces are divided into meaningful regions.

### Quick Check

**[Ask students:]**

If I `pack()` a main frame into the root window and then use `grid()` inside that frame, am I breaking the rule?

**Expected answer:** no, because the widgets with `grid()` are children of the frame, not direct children of the root.

---

## Section 3: Usability Principles for Basic Desktop GUIs (10 minutes)

### A Simple Usability Checklist

**[Instructor speaks:]**

Students do not need a full usability textbook today. They need a small, memorable checklist:

1. Are related items grouped together?
2. Are labels close to the fields they describe?
3. Is spacing consistent?
4. Is the primary action easy to find?
5. Does the interface resize sensibly?

That short checklist catches many beginner layout problems.

### `padx`, `pady`, and Breathing Room

**[Instructor speaks:]**

Padding matters more than students usually expect. Without padding, even correct layouts feel crowded and accidental.

Use:

- `padx` for horizontal spacing
- `pady` for vertical spacing

Consistency matters more than fancy numbers. If you choose `pady=6` or `pady=8`, reuse it across the form.

### `sticky` and Alignment

**[Instructor speaks:]**

With `grid()`, `sticky` controls how a widget sits inside its cell.

Common values:

- `sticky="w"` — align left
- `sticky="e"` — align right
- `sticky="ew"` — stretch horizontally
- `sticky="nsew"` — stretch in all directions

This is one of the keys to making forms line up and resize gracefully.

### Column Weights and Resizing

**[Instructor speaks:]**

If a window grows, the interface should know what to do with the extra space. That is where row and column weights come in.

Example:

```python
root.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
```

A weight of `1` means that column is allowed to grow.

Without weights, a resized window often leaves the content sitting awkwardly in a corner.

### Instructor Prompt

**[Ask students:]**

When the window gets wider, what do you usually want to expand in a form: the labels or the entry fields?

**Expected answer:** usually the entry field column.

---

## Section 4: Live Demo — Refactoring a Messy Layout (13 minutes)

### Demo Framing

**[Instructor speaks:]**

I am going to take a cramped, single-column interface and refactor it into a cleaner structure with two visual regions:

- a form frame
- a preview frame

Even though we are not fully building a record browser until the next hour, having a second panel makes the layout principles easier to see.

### Demo Code

```python
from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class ContactLayoutApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Contact Manager Layout Demo")
        self.root.geometry("760x340")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self._build_ui()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        form_frame = ttk.LabelFrame(main_frame, text="Add Contact", padding=12)
        form_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        preview_frame = ttk.LabelFrame(main_frame, text="Preview Area", padding=12)
        preview_frame.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        form_frame.columnconfigure(1, weight=1)

        ttk.Label(form_frame, text="Name").grid(row=0, column=0, sticky="w", pady=6)
        ttk.Entry(form_frame).grid(row=0, column=1, sticky="ew", pady=6)

        ttk.Label(form_frame, text="Email").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Entry(form_frame).grid(row=1, column=1, sticky="ew", pady=6)

        ttk.Label(form_frame, text="Role").grid(row=2, column=0, sticky="w", pady=6)
        ttk.Entry(form_frame).grid(row=2, column=1, sticky="ew", pady=6)

        button_bar = ttk.Frame(form_frame)
        button_bar.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        ttk.Button(button_bar, text="Add").pack(side="left")
        ttk.Button(button_bar, text="Clear").pack(side="left", padx=(8, 0))

        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)

        preview = tk.Listbox(preview_frame)
        preview.grid(row=0, column=0, sticky="nsew")

        for item in ["Ada Lovelace", "Grace Hopper", "Katherine Johnson"]:
            preview.insert("end", item)


def main() -> None:
    root = tk.Tk()
    ContactLayoutApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Demo Steps

1. Start with the root window and a single `main_frame`.
2. Configure the root and frame to resize.
3. Split the interface into two labeled frames.
4. Use `grid()` in the form frame.
5. Use consistent `pady` values.
6. Configure the entry column with weight so fields stretch.
7. Show a nested `button_bar` using `pack()` safely.
8. Resize the window and point out what grows and what stays fixed.

### Demo Narration

**[Instructor speaks while coding:]**

Notice that I am using one geometry manager per parent.

Inside `main_frame`, I use `grid()`.

Inside `form_frame`, I also use `grid()`.

Inside `button_bar`, I use `pack()` for the buttons. That is allowed because `button_bar` is a different parent.

Also notice that the form’s second column has `weight=1`. That means the entry fields get more space when the window expands.

### Live Questions to Ask During the Demo

**[Ask students:]**

Why did I choose `grid()` for the form rather than `pack()`?

**Expected answer:** because the form has aligned labels and fields across rows and columns.

**[Ask students:]**

Am I breaking the no-mixing rule by using `pack()` in `button_bar`?

**Expected answer:** no, because `button_bar` is a separate parent.

**[Ask students:]**

What would happen if I forgot `sticky="ew"` on the entries?

**Expected answer:** the entries would not stretch horizontally as the window grows.

---

## Section 5: Hands-On Lab — Improve the Layout (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Take the simple GUI from Hour 1 and improve the layout so it looks intentional and behaves reasonably when resized.

This is not cosmetic busywork. Clean layout directly affects whether users understand the interface.

### Student Task

Update your GUI so that it includes:

- at least one `Frame` or `LabelFrame`
- form fields laid out with `grid()`
- consistent padding
- at least one row or column configured to expand
- a clearly separated second area such as preview, status, or list placeholder

### Hands-On Lab Guidance

**[Instructor speaks:]**

Work in layers:

1. create one main frame
2. split the screen into sections
3. put the form in its own frame
4. convert the form to `grid()`
5. add consistent spacing
6. test resizing

Resize the window on purpose. Do not assume the layout works just because it looks okay at the starting size.

### Completion Criteria

A strong minimum solution should:

1. Avoid cramped widget placement.
2. Use `grid()` for the form area.
3. Use consistent padding values.
4. Resize acceptably without overlapping widgets.
5. Keep geometry management consistent within each parent widget.

### Circulation Prompts

**[Circulate and ask:]**

1. Which parent contains these widgets?
2. Are you mixing `pack()` and `grid()` in that same parent?
3. Which column should stretch on resize?
4. Does the main action button remain easy to find?
5. If the window gets wider, what changes visually?

### Common Pitfalls During the Lab

#### Pitfall 1: Mixing geometry managers in the same parent
Encourage students to add an intermediate frame if needed.

#### Pitfall 2: Forgetting `sticky`
Without alignment rules, widgets may look oddly centered or too small.

#### Pitfall 3: Inconsistent padding
A layout can be technically correct and still feel broken if spacing changes randomly.

#### Pitfall 4: Ignoring resize behavior
If the UI wastes available space, check `columnconfigure()` and `rowconfigure()`.

### Optional Extensions

- Add a toolbar frame with **Add**, **Delete**, and **Refresh**
- Add a larger status area on the right
- Add keyboard focus testing with Tab
- Create a more obvious primary action button placement

---

## Section 6: Debrief, Quick Checks, Exit Ticket, and Wrap-Up (5 minutes)

### Group Debrief

**[Instructor speaks:]**

This hour was about making the interface readable and usable. A strong GUI is not only functional. It is organized, aligned, and predictable.

### Quick Checks

**Prompt:** Why is `grid()` often a better fit for forms?  
**Expected answer:** because forms naturally align labels and inputs in rows and columns.

**Prompt:** What is the purpose of `sticky="ew"`?  
**Expected answer:** it allows a widget to stretch horizontally within its grid cell.

### Exit Ticket

**Prompt 1:** Why should you not mix `pack()` and `grid()` in the same parent?  
**Expected answer:** because the geometry managers conflict inside the same container and can produce unpredictable layout behavior.

**Prompt 2:** What does `weight=1` help with?  
**Expected answer:** it allows rows or columns to grow when extra space is available.

**Prompt 3:** What role do frames play in a GUI layout?  
**Expected answer:** they group related widgets and create layout boundaries.

### Common Pitfalls Recap

- mixing geometry managers within one parent
- forgetting `sticky`
- inconsistent padding
- no resizing configuration
- not grouping related controls

### Wrap-Up

**[Instructor speaks:]**

We now have GUIs that not only work but are beginning to feel structured. In the next hour, we will make them more user-friendly by validating form input and giving feedback that helps the user recover instead of guessing what went wrong.

Frames divide, `grid()` aligns, padding creates breathing room, and weights control resizing. Those four ideas take students a long way.

---

## Optional Instructor Reference Notes

### Quick Reminder Phrase
Use frames to divide, `grid()` to align, padding to breathe, and weights to resize.

### If Students Finish Early
Invite them to:

- build a title area above the form
- right-align a button row
- compare poor spacing versus good spacing
- sketch what should expand on resize before changing code

---
