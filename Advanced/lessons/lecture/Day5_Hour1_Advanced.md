# Day 5, Hour 1: GUI Fundamentals with Tkinter and ttk

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 5
- **Hour**: 1 of 4 for this session, corresponding to **Hour 17** in the 48-hour runbook
- **Focus**: GUI fundamentals with Tkinter/ttk — event loop, widgets, callbacks
- **Runbook alignment**: Create a window and basic widgets; wire callbacks to service functions; introduce event-driven thinking; show messagebox feedback; keep business logic out of callbacks
- **Prerequisites**:
  - Students can write functions and basic classes
  - Students understand exceptions and basic validation
  - Students are comfortable with strings, lists, and dictionaries
  - Students have seen separation of concerns in previous sessions
- **Teaching goal**: Shift students from a command-line, top-to-bottom mental model into an event-driven GUI mental model without overwhelming them
- **Demo app theme**: A small contact-entry desktop app
- **Key message to repeat**: “The GUI handles interaction; the service layer handles rules.”
- **Environment note**: Tkinter ships with standard Python in most course environments; use `ttk` widgets for a cleaner, more modern default appearance
- **Success criteria for the hour**:
  - Students can explain what `mainloop()` does
  - Students can create a simple window with `Label`, `Entry`, and `Button`
  - Students can wire a callback to a button
  - Students can call service logic from the UI and show success/error feedback

---

## Timing Overview

| Segment | Time |
|---|---:|
| Recap and transition into GUI programming | 5 minutes |
| Event-driven programming and the Tkinter mental model | 12 minutes |
| Core widgets, the event loop, and callback design | 10 minutes |
| Live demo: minimal record-entry GUI with service layer | 13 minutes |
| Hands-on lab: Hello GUI + Add Record form | 15 minutes |
| Debrief, quick checks, exit ticket, wrap-up | 5 minutes |

**Total:** 60 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, students should be able to:

1. Explain what makes GUI programming event-driven.
2. Describe the role of `mainloop()` in a Tkinter application.
3. Create a simple window using Tkinter and themed ttk widgets.
4. Build a small form with labels, entry fields, a button, and a status area.
5. Connect a button click to a callback function.
6. Keep UI code separate from service or business logic.
7. Provide user feedback with a status label and a message box.

---

## Section 1: Recap and Transition (5 minutes)

### Quick Re-entry

**[Instructor speaks:]**

Up to this point in the advanced course, we have built and refined command-line Python programs. Those programs gave us strong habits: organize code into functions, design classes around responsibilities, validate inputs, and separate concerns. All of that still matters today.

What changes in this session is the way the user interacts with the program.

A command-line script usually has a simple flow:

1. start the script  
2. read input  
3. do work  
4. print output  
5. exit  

A graphical user interface, or GUI, behaves differently. The program opens a window and stays alive. The user clicks, types, resizes, selects, and expects the application to respond in real time.

That means we need a new mental model.

### Framing the Hour

**[Instructor speaks:]**

This hour is our entry point into desktop GUI programming. We are intentionally keeping the feature set small so the core ideas stay clear.

Today’s essential ideas are:

- a window
- widgets
- an event loop
- callbacks
- service-layer separation
- user feedback

If students leave this hour able to say, “I understand why a GUI is event-driven, I can create a small form, and I know where validation should live,” then the hour has succeeded.

### Transition Prompt

**[Ask students:]**

Where have you used desktop or web interfaces that respond to clicks and form input? What kinds of user actions are actually “events”?

**Expected examples:** button clicks, typing in a field, selecting a row, pressing Enter, resizing a window.

---

## Section 2: The GUI Mental Model (12 minutes)

### Event-Driven Programming

**[Instructor speaks:]**

The single most important concept in beginner GUI programming is this:

> A GUI is event-driven.

That means the application does not simply run top to bottom and finish. Instead, it creates an interface and then waits for events.

Examples of events include:

- the user clicking a button
- the user typing into a text field
- the user pressing Enter
- the user selecting an item
- the window being resized
- the user closing the application

In a command-line script, we often ask:

> “What does the next line of code do?”

In a GUI, we very often ask:

> “What should happen when the user does this?”

That is the shift.

### What `mainloop()` Does

**[Instructor speaks:]**

Tkinter needs something to keep the application alive and listening for those events. That is the job of `mainloop()`.

When you call `mainloop()`:

- the window appears and remains interactive
- Tkinter starts listening for user actions
- callbacks are invoked when those actions occur
- the application stays alive until the user closes it

Without `mainloop()`, the program may create window objects in memory, but it will not function as a live interactive application.

### Quick Check

**[Ask students:]**

If I build a Tkinter window object but never call `mainloop()`, what happens?

**Expected direction:** the program ends immediately or the interface never becomes a properly interactive GUI.

### Why Blocking Calls Matter

**[Instructor speaks:]**

There is another practical lesson hidden inside the event loop idea: **callbacks should stay reasonably small and fast**.

If a callback directly performs a long-running task, the interface may appear frozen. For example:

- `time.sleep(10)`
- a slow network request
- heavy file processing
- large database work done directly inside the button handler

The GUI becomes unresponsive because the event loop cannot continue handling events smoothly.

Today, we will keep our callbacks short. They will gather input, call service logic, and update the interface.

### Widgets and Callbacks

**[Instructor speaks:]**

A **widget** is a UI element. Today’s core widgets are:

- `Label` — displays text
- `Entry` — accepts text input
- `Button` — triggers an action

A **callback** is a function Tkinter calls when an event occurs.

For example:

- “When the Add button is clicked, call `on_add()`.”

That is the central interaction pattern for today.

---

## Section 3: Core Design Pattern for This Hour (10 minutes)

### Keep UI and Service Logic Separate

**[Instructor speaks:]**

One of the fastest ways to make GUI code confusing is to put everything into one callback.

A beginner’s `on_add()` function often grows until it:

- reads the form
- validates every field
- transforms the data
- stores the record
- updates labels
- shows popups
- catches exceptions
- prints debug output

That kind of callback becomes difficult to test and difficult to maintain.

A cleaner pattern is:

1. the UI gathers input
2. the callback calls a service function or method
3. the service layer validates and applies business rules
4. the UI displays the result

### Instructor Board Sketch

**[Instructor action:]** Draw or describe the flow.

```text
Entry widgets -> callback -> service layer -> result -> UI feedback
```

**[Instructor speaks:]**

This simple flow is the backbone of our GUI work.

### Why This Matters

**[Instructor speaks:]**

If business rules live in the service layer, then later you can:

- reuse them in another interface
- test them without clicking through the GUI
- keep callbacks small and readable
- avoid duplicating validation in multiple buttons or screens

That is why GUI programming still benefits from all the software design discipline we used earlier in the course.

### Example Rule Set for the Demo

For our small contact-entry example:

- name is required
- email is required
- email must contain `@`

The UI should not invent those rules. The service should own them.

---

## Section 4: Live Demo — Minimal Record Entry GUI (13 minutes)

### Demo Framing

**[Instructor speaks:]**

I am going to build a very small desktop app that lets a user enter a contact name and email, click **Add Record**, and receive either success or error feedback.

As you watch, pay attention to four things:

1. where the widgets are created
2. where the callback lives
3. where the validation logic lives
4. where `mainloop()` appears

### Demo Code

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import messagebox, ttk


@dataclass(slots=True)
class ContactRecord:
    name: str
    email: str


class ValidationError(Exception):
    """Raised when contact data is invalid."""


class ContactService:
    def __init__(self) -> None:
        self._records: list[ContactRecord] = []

    def add_record(self, name: str, email: str) -> ContactRecord:
        clean_name = name.strip()
        clean_email = email.strip().lower()

        if not clean_name:
            raise ValidationError("Name is required.")

        if not clean_email:
            raise ValidationError("Email is required.")

        if "@" not in clean_email:
            raise ValidationError("Email must include '@'.")

        record = ContactRecord(name=clean_name, email=clean_email)
        self._records.append(record)
        return record

    def count_records(self) -> int:
        return len(self._records)


class ContactApp:
    def __init__(self, root: tk.Tk, service: ContactService) -> None:
        self.root = root
        self.service = service

        self.root.title("Contact Entry")
        self.root.geometry("420x240")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready to add a record.")

        self._build_ui()

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Name").pack(anchor="w")
        ttk.Entry(main_frame, textvariable=self.name_var).pack(fill="x", pady=(0, 10))

        ttk.Label(main_frame, text="Email").pack(anchor="w")
        ttk.Entry(main_frame, textvariable=self.email_var).pack(fill="x", pady=(0, 10))

        ttk.Button(main_frame, text="Add Record", command=self.on_add).pack(pady=(4, 10))

        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            foreground="navy",
            wraplength=360,
        ).pack(anchor="w")

    def on_add(self) -> None:
        try:
            record = self.service.add_record(
                self.name_var.get(),
                self.email_var.get(),
            )
        except ValidationError as exc:
            self.status_var.set(f"Error: {exc}")
            messagebox.showerror("Validation Error", str(exc))
            return

        self.status_var.set(
            f"Added {record.name} successfully. Total records: {self.service.count_records()}."
        )
        messagebox.showinfo("Success", f"Saved record for {record.name}.")
        self.name_var.set("")
        self.email_var.set("")


def main() -> None:
    root = tk.Tk()
    service = ContactService()
    ContactApp(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Demo Steps

1. Create the service class first.
2. Explain that the service owns validation and record storage.
3. Create the `ContactApp` class.
4. Add `StringVar` objects for form state and the status line.
5. Build the widgets with ttk.
6. Wire the button using `command=self.on_add`.
7. Show the callback calling the service.
8. Demonstrate a bad submission and the validation popup.
9. Demonstrate a valid submission and the success message.
10. Point to `root.mainloop()` and explain that it keeps the GUI alive.

### Demo Narration

**[Instructor speaks while coding:]**

Notice that `ContactService` is plain Python. It has no knowledge of windows, buttons, or labels. That is good design.

Now look at `ContactApp`. This class owns the UI state and user interaction.

Finally, look at `on_add()`. It is short. It does not decide the email rule. It asks the service to do the domain work, then the UI decides how to present the result.

That is exactly the separation we want.

### Live Questions to Ask During the Demo

**[Ask students:]**

Where is the rule that email must contain `@`?

**Expected answer:** in `ContactService.add_record()`.

**[Ask students:]**

Where does the app clear the form after a successful add?

**Expected answer:** in `ContactApp.on_add()`.

**[Ask students:]**

What connects the Add button to the callback?

**Expected answer:** `command=self.on_add`.

### Demo Teaching Points to Repeat

- `StringVar` is convenient for connecting UI values to Python state.
- Callbacks should be small and readable.
- The service layer handles validation rules.
- `messagebox` is useful for simple feedback.
- `mainloop()` starts the event loop.

---

## Section 5: Hands-On Lab — Hello GUI + Add Record Form (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Now it is your turn to build a small GUI. The goal is not to build a full application yet. The goal is to become comfortable with the mechanics:

- create a window
- place widgets
- wire a button
- call service logic
- show feedback

### Student Task

Create a Tkinter app that includes:

- a window title
- at least two input fields
- an **Add** button
- a status message area
- a service class or service function for validation
- success or error feedback after clicking **Add**

### Suggested Record Options

Students may build one of these:

- contact name + contact email
- task title + task owner
- item name + item category

### Suggested Starter Shape

```python
from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class RecordService:
    def add_record(self, field_one: str, field_two: str) -> str:
        raise NotImplementedError


def main() -> None:
    root = tk.Tk()
    root.title("My First GUI")
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Hands-On Lab Guidance

**[Instructor speaks:]**

Start small. First make the window appear. Then add one label. Then one entry. Then the second entry. Then the button. Then wire the callback. Then add validation.

Do not try to perfect the layout yet. The important thing in this hour is understanding the event loop and the callback flow.

### Completion Criteria

A strong minimum solution should:

1. Launch without crashing.
2. Show at least one label, two entry fields, and one button.
3. Trigger a callback when the button is clicked.
4. Validate input through a service function or class.
5. Show success or error feedback in the interface.

### Circulation Prompts

**[Circulate and ask:]**

1. Show me where your callback starts.
2. Show me where your validation rules live.
3. What happens if the user clicks Add with blank fields?
4. Where does the status message get updated?
5. Where is `mainloop()`?

### Common Pitfalls During the Lab

#### Pitfall 1: Business logic inside the callback
If students put all validation rules directly inside the button handler, encourage them to move those rules into a helper method or service class.

#### Pitfall 2: Forgetting `mainloop()`
The app may appear not to work at all if the event loop is missing.

#### Pitfall 3: Callback not wired correctly
A common mistake is writing `command=self.on_add()` instead of `command=self.on_add`. The first calls the function immediately during setup.

#### Pitfall 4: No visible feedback
If the button is clicked and nothing visible changes, the user has no idea what happened.

### Optional Extensions

- Clear the form after a successful add
- Bind the Enter key to submit
- Add a small “record count” label
- Add a second button labeled **Clear**

---

## Section 6: Debrief, Quick Checks, Exit Ticket, and Wrap-Up (5 minutes)

### Group Debrief

**[Instructor speaks:]**

Let’s name the big ideas from the hour:

- GUI programs are event-driven
- widgets are the visible building blocks
- callbacks respond to user actions
- `mainloop()` keeps the app alive and listening
- service logic should stay separate from UI code

### Quick Checks

**Prompt:** What is the difference between a widget and a callback?  
**Expected answer:** a widget is a UI element; a callback is a function that runs in response to an event.

**Prompt:** Why is it helpful to keep validation out of the widget-building code?  
**Expected answer:** clearer responsibilities, easier testing, easier maintenance.

### Exit Ticket

**Prompt 1:** What does `mainloop()` do?  
**Expected answer:** it starts Tkinter’s event loop and keeps the application responsive to events.

**Prompt 2:** What is a callback in a Tkinter application?  
**Expected answer:** a function that runs when a user action or GUI event occurs.

**Prompt 3:** Why should business rules stay in a service layer instead of directly in the callback?  
**Expected answer:** to keep code organized, reusable, and easier to test.

### Common Pitfalls Recap

- putting business rules inside callbacks
- forgetting `mainloop()`
- calling the callback immediately instead of passing it as a command
- giving no visible user feedback
- writing a callback that tries to do everything

### Wrap-Up

**[Instructor speaks:]**

This hour was about getting the window alive and making the event-driven model feel concrete. In the next hour, we will take the same kinds of widgets and organize them into cleaner, more usable layouts using frames, `grid()`, spacing, and resizing rules.

A GUI is not magic. It is a Python program that waits for events, reacts through callbacks, and benefits from the same design discipline as any other application.

---

## Optional Instructor Reference Notes

### One-Sentence Summary
Tkinter apps are event-driven programs where the UI gathers input, callbacks respond to user actions, and service logic should remain separate from presentation code.

### If Students Finish Early
Invite them to:

- add a third field
- add a record counter
- add an Enter key binding
- compare feedback in a status label versus a message box

---
