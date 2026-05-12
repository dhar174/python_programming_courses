# Day 5, Hour 1: GUI Fundamentals with Tkinter and ttk

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: 5
- **Hour**: 1 of 4 for this session, corresponding to **Hour 17** in the 48-hour Advanced runbook
- **Focus**: GUI fundamentals with Tkinter/ttk — event loop, widgets, callbacks, and service-layer wiring
- **Runbook alignment**: Create a window and basic widgets; wire callbacks to service functions; explain event-driven GUI behavior; avoid blocking calls; use `Label`, `Entry`, and `Button`; separate UI from service logic; build a minimal GUI that adds a record through a service layer; show `messagebox` feedback; run a Hello GUI + Add form lab
- **Prerequisites**:
  - Students can write functions and basic classes.
  - Students understand exceptions and basic validation.
  - Students are comfortable with strings, lists, and dictionaries.
  - Students have seen separation of concerns in previous sessions.
- **Teaching goal**: Shift students from a command-line, top-to-bottom mental model into an event-driven GUI mental model without overwhelming them.
- **Demo app theme**: A small contact-entry desktop app.
- **Key message to repeat**: “The GUI handles interaction; the service layer handles rules.”
- **Environment note**: Tkinter ships with standard Python in most course environments, including typical Windows Python installations. In a few Linux or managed lab environments, Tkinter may require an additional OS package or may not display if no graphical desktop is available. For this course hour, Tkinter availability is assumed; if one learner has an environment issue, pair them temporarily while the lab environment is corrected.
- **Scope guard**: Do not turn this hour into advanced layout, threading, async programming, databases, or a full MVC framework discussion. Those topics either come later or are intentionally out of scope for this first GUI hour.
- **Success criteria for the hour**:
  - Students can explain what `mainloop()` does.
  - Students can create a simple window with `Label`, `Entry`, and `Button`.
  - Students can wire a callback to a button.
  - Students can call service logic from the UI and show success/error feedback.
  - Students can identify why blocking work inside a callback freezes the interface.

---

## Timing Overview

| Segment | Time |
|---|---:|
| Recap | 4 minutes |
| GUI Mental Model | 9 minutes |
| Core Widget/Callback/Service Design | 8 minutes |
| Live Demo | 8 minutes |
| Hands-On Lab | 26 minutes |
| Debrief/Exit | 5 minutes |

**Total arithmetic:** 4 + 9 + 8 + 8 + 26 + 5 = 60 minutes exactly.

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
8. Recognize common first-GUI mistakes: missing `mainloop()`, blocking callbacks, layout mistakes that hide widgets, and business rules buried inside button handlers.

---

## Section 1: Recap (4 minutes)

### Purpose of This Opening

This section should be brief and energetic. The goal is to connect GUI programming to the design habits students have already practiced: functions, classes, exceptions, validation, and separation of concerns. Do not begin by explaining every Tkinter feature. Begin by reminding students that the same Python design discipline still applies, but the user interaction model changes.

### Instructor Script

**[Instructor speaks:]**

Welcome back. In the previous parts of the advanced course, we spent a lot of time building Python programs that were organized around responsibilities. We wrote functions that did one job, classes that represented a concept, exceptions that explained failure, and service code that handled rules instead of scattering rules everywhere.

Today we keep those habits, but we change the way the user talks to the program.

Most of the Python programs you have written so far have followed a command-line style. The script starts, asks for input or reads data, performs work, prints output, and ends. That style is direct and useful, but it is not how a graphical application feels to a user.

A graphical user interface, or GUI, opens a window and stays alive. The user decides what happens next by clicking, typing, pressing keys, or closing the window. The program is not simply marching from line one to the final line. It is waiting for user events and responding to them.

So this hour is not about making a beautiful application yet. It is about learning the core mechanics:

- create a window,
- place a few widgets,
- respond to a button click,
- call service logic,
- show feedback,
- and keep the interface responsive.

The key design message for today is: **the GUI handles interaction; the service layer handles rules.**

### Fast Warm-Up Prompt

**[Ask students:]**

Think of a desktop app, a web page, or a mobile app you used recently. What actions did you take that caused the interface to respond?

**Expected answers:** clicking a button, typing into a field, pressing Enter, choosing a menu item, selecting a row, closing a dialog, resizing a window.

**[Instructor continues:]**

Those actions are the center of GUI programming. We call them events. Today we will build just enough Tkinter to make that event-driven idea concrete.

---

## Section 2: GUI Mental Model (9 minutes)

### The Shift from Script Flow to Event Flow

**[Instructor speaks:]**

The most important concept in this hour is this:

> A GUI is event-driven.

Let’s unpack that carefully.

In a command-line script, you can often understand the program by reading from top to bottom. The program says, “Do this, then do this, then do this.” If you see an `input()` call, the program stops there and waits for the user. After the user types something, the program continues to the next line.

In a GUI, the program creates a window and gives control to the GUI toolkit. The toolkit listens for events: button clicks, key presses, mouse movement, text entry, window closing, and so on. When an event occurs, the toolkit calls a function that you registered for that event. That function is called a callback.

So the question changes from:

> What line runs next?

to:

> What should happen when the user does this?

That question is the GUI mental model.

### Tkinter, ttk, and the Window

**[Instructor speaks:]**

Tkinter is Python’s standard GUI toolkit. It is included with most Python installations, which makes it reliable for a course environment. The `ttk` module provides themed widgets. The basic behavior is the same as classic Tkinter widgets, but the default appearance is usually cleaner and more native-looking.

Today we will use:

- `tk.Tk()` for the main application window,
- `ttk.Label` to display text,
- `ttk.Entry` to accept typed text,
- `ttk.Button` to trigger an action,
- `tk.StringVar` to hold values connected to the interface,
- and `messagebox` for simple user feedback.

We are intentionally staying small. We are not building a complex layout system today. Hour 18 goes deeper into layout and usability. Today, if the window appears, the fields appear, the button works, and the callback calls the service layer, that is success.

### What `mainloop()` Does

**[Instructor speaks:]**

Every Tkinter application needs an event loop. In Tkinter, we start that event loop by calling:

```python
root.mainloop()
```

When `mainloop()` starts, Tkinter keeps the window alive and listens for events. If the user clicks the Add button, Tkinter notices the click and calls the callback connected to that button. If the user types in an entry field, Tkinter updates the widget state. If the user closes the window, Tkinter exits the event loop and the program can end.

Without `mainloop()`, you may create Python objects that represent a window and widgets, but the application will not behave like a live GUI. In many environments the window may flash and disappear, or nothing useful may appear at all, because the script reaches the end and exits.

**[Instructor board sketch:]**

```text
create widgets -> register callbacks -> start mainloop()
                                      |
                                      v
                         wait for events and respond
```

### Why Blocking Calls Matter

**[Instructor speaks:]**

The event loop also explains why we must avoid blocking calls inside callbacks.

Imagine the user clicks **Add**, and the callback does this:

```python
time.sleep(10)
```

For those ten seconds, the callback is busy. While it is busy, the GUI cannot smoothly process other events. The window may look frozen. Buttons may not respond. The user may think the app crashed.

The same problem can happen with long network calls, large file processing, slow database work, or heavy calculations placed directly in a button handler. Those topics require additional techniques, but not today. Today our rule is simple: callbacks should be short. They gather input, call service logic, and update feedback.

One important nuance: `messagebox.showinfo()` and `messagebox.showerror()` are modal dialogs. In plain language, **messagebox is modal**: the dialog briefly takes focus and blocks interaction with the main window until the user dismisses it. That is acceptable here because it is short, intentional user feedback. It is very different from putting a long sleep, a slow network request, or a large file operation inside a callback. A quick message box says, “Please acknowledge this result.” A long blocking task says, “The interface is stuck while Python works.” Those are not the same user experience.

### Quick Concept Check

**[Ask students:]**

If a GUI program is event-driven, who decides what happens next: the programmer’s top-to-bottom script flow, or the user’s actions?

**Expected answer:** the user’s actions trigger events; our code responds through callbacks.

**[Instructor reinforces:]**

Exactly. We still write the code, but the user drives the sequence.

---

## Section 3: Core Widget/Callback/Service Design (8 minutes)

### The Three-Part Pattern

**[Instructor speaks:]**

For this first GUI hour, we will use one simple design pattern repeatedly:

```text
widgets collect input -> callback responds -> service layer validates and stores
```

Then the callback updates the interface with success or error feedback.

Let’s define the pieces.

A **widget** is a visible user interface element. A label shows text. An entry field accepts text. A button can be clicked.

A **callback** is a Python function or method that Tkinter calls when an event happens. For a button, we connect the callback with the `command` option:

```python
ttk.Button(parent, text="Add", command=self.on_add)
```

Notice the important detail: `command=self.on_add`, not `command=self.on_add()`.

When we write `self.on_add`, we are passing the function itself so Tkinter can call it later. When we write `self.on_add()`, we call the function immediately while building the interface. That is one of the most common first-GUI bugs.

A **service layer** is ordinary Python code that owns business rules. In today’s contact-entry example, the service layer decides that a name is required, an email is required, and an email must include `@`. The UI should not invent those rules. The UI should ask the service to add a record, then display the result.

### Why We Separate UI from Service Logic

**[Instructor speaks:]**

One of the fastest ways to make GUI code hard to maintain is to put every rule inside the button callback.

A beginner’s callback often grows into one large function that:

- reads every field,
- validates every field,
- transforms text,
- creates a record,
- stores the record,
- updates labels,
- shows popups,
- clears the form,
- catches exceptions,
- and prints debug output.

That may work for a tiny script, but it becomes painful quickly. It is hard to test because you have to click through the GUI. It is hard to reuse because the rule is trapped inside a window class. It is hard to change because display code and business rules are tangled together.

The better pattern is:

1. The UI gathers raw input from widgets.
2. The callback passes that input to the service.
3. The service validates and performs the operation.
4. The service returns a result or raises a meaningful error.
5. The UI shows the success or error to the user.

### Minimal Example of the Separation

**[Instructor speaks:]**

Here is the shape without all the GUI details:

```python
class ContactService:
    def add_record(self, name: str, email: str) -> str:
        clean_name = name.strip()
        clean_email = email.strip().lower()

        if not clean_name:
            raise ValueError("Name is required.")
        if "@" not in clean_email:
            raise ValueError("Email must include '@'.")

        return clean_name
```

The service does not know about labels, buttons, `StringVar`, or message boxes. That is a feature, not a limitation.

The callback can stay small:

```python
def on_add(self) -> None:
    try:
        name = self.service.add_record(self.name_var.get(), self.email_var.get())
    except ValueError as exc:
        self.status_var.set(f"Error: {exc}")
        return

    self.status_var.set(f"Added {name}.")
```

This is the design habit we want to reinforce throughout the GUI unit. The callback coordinates. The service decides.

### Layout Caution for Today

**[Instructor speaks:]**

We will use simple `pack()` calls today because they are enough for a first form. Later we will compare `pack()` and `grid()` more carefully. For now, remember two practical rules:

- A widget does not appear until you place it with a layout manager such as `pack()` or `grid()`.
- Do not mix `pack()` and `grid()` in the same parent container.

That second rule is important. You can use `pack()` in one frame and `grid()` in a different frame, but do not use both inside the same parent. Mixing them in one parent commonly leads to layout errors or confusing results. Today we will keep the layout deterministic and Windows-friendly by using one main frame and `pack()` consistently.

---

## Section 4: Live Demo (8 minutes)

### Demo Framing

**[Instructor speaks:]**

I am going to build a small contact-entry GUI. The user will type a name and email, click **Add Record**, and receive either a success message or a validation error.

This demo is intentionally small and should take about 8 minutes. Watch for four things:

1. where the widgets are created,
2. where the callback is connected,
3. where validation lives,
4. and where `mainloop()` starts the event loop.

### Demo Code

Use this as the live-coding target. If time is tight, paste the class definitions and live-code the `_build_ui()` and `on_add()` methods.

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

        ttk.Button(
            main_frame,
            text="Add Record",
            command=self.on_add,
        ).pack(pady=(4, 10))

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
            f"Added {record.name} successfully. Total records: "
            f"{self.service.count_records()}."
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

### Demo Narration and Timing

**Minute 1: Service first.**

**[Instructor speaks while coding:]**

I am starting with the service layer because these rules are not GUI rules. A contact name is required whether the contact comes from a GUI, a command-line prompt, an API, or a file import. The service owns that rule.

**Minute 2: Record and validation.**

Point out `ContactRecord`, `ValidationError`, and `ContactService.add_record()`. Emphasize that the service returns a record on success and raises a meaningful exception on invalid input.

**Minute 3: Root window.**

Create `root = tk.Tk()`, set the title, and explain that this is the main application window. Mention that `geometry()` is used here only to keep the demo predictable on Windows classroom machines.

**Minute 4: Variables and widgets.**

Create `StringVar` objects, labels, entries, and the button. As each widget is created, call `.pack()` so students see that creating a widget and displaying a widget are separate ideas.

**Minute 5: Callback wiring.**

Pause at `command=self.on_add`.

**[Ask students:]**

Why is this `self.on_add` instead of `self.on_add()`?

**Expected answer:** because Tkinter needs the function to call later, not the result of calling it now.

**Minute 6: Callback calls service.**

Show `self.name_var.get()` and `self.email_var.get()`. Explain that the UI gathers strings, but it does not validate all rules itself. It asks the service.

**Minute 7: Feedback.**

Show both feedback paths: status label and message box. Remind students that the message box is modal and briefly blocks the main window until dismissed, which is acceptable for short feedback.

**Minute 8: Run and test.**

Run three cases:

1. blank name,
2. email without `@`,
3. valid contact such as `Ada Lovelace` and `ada@example.com`.

Point to `root.mainloop()` and close by saying:

**[Instructor speaks:]**

This is a small app, but it already has the essential structure: window, widgets, callback, service, validation, feedback, and event loop.

### Demo Questions

Use these questions during or immediately after the demo:

- Where is the rule that email must contain `@`?
- What connects the Add button to the callback?
- What happens if we forget `.pack()` on a widget?
- What does the UI do after the service raises `ValidationError`?
- Why is a short message box acceptable, but a long sleep inside the callback is not?

---

## Section 5: Hands-On Lab (26 minutes)

### Lab Goal

**[Instructor speaks:]**

Now you will build your own small GUI. The lab has two parts. First, you will make a Hello GUI to prove that your environment and event loop work. Second, you will build an Add form that sends input through a service layer and shows success or error feedback.

The goal is not visual polish. The goal is a reliable event-driven flow:

```text
user types -> user clicks Add -> callback runs -> service validates -> UI shows feedback
```

### Lab Mini-Budget

Use this mini-budget to keep the 26-minute lab on track:

| Lab activity | Time |
|---|---:|
| Part A: Hello GUI launches | 5 minutes |
| Part B: Add form widgets | 7 minutes |
| Part C: Service validation and callback wiring | 8 minutes |
| Part D: Test, fix, and optional extension | 6 minutes |

**Lab arithmetic:** 5 + 7 + 8 + 6 = **26 minutes**.

### Part A: Hello GUI Launches

Create a file named something simple such as `hello_gui.py` or use the course lab file if one has been provided. Start with this minimal program:

```python
import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Hello GUI")

    ttk.Label(root, text="Hello from Tkinter!").pack(padx=16, pady=16)

    root.mainloop()


if __name__ == "__main__":
    main()
```

**Expected result:** a small window opens with the text “Hello from Tkinter!”.

**Instructor circulation prompts:**

- Does the window launch?
- Can you point to the line that starts the event loop?
- What happens if you comment out `root.mainloop()` and run again?

If a learner’s Tkinter environment fails, confirm they are using the expected Python interpreter. In this course hour we assume Tkinter is available, but some managed environments may need instructor support.

### Part B: Add Form Widgets

Expand the app into a small Add form. Students may use contacts, tasks, inventory items, or notes. To preserve the demo theme, contacts are recommended.

Minimum fields:

- record name,
- record detail such as email, owner, category, or note,
- Add button,
- status area.

Starter shape:

```python
import tkinter as tk
from tkinter import ttk


class RecordService:
    def __init__(self) -> None:
        self._records: list[tuple[str, str]] = []

    def add_record(self, name: str, detail: str) -> int:
        clean_name = name.strip()
        clean_detail = detail.strip()

        if not clean_name:
            raise ValueError("Name is required.")

        if not clean_detail:
            raise ValueError("Detail is required.")

        self._records.append((clean_name, clean_detail))
        return len(self._records)


def main() -> None:
    root = tk.Tk()
    root.title("Add Record")
    root.geometry("420x240")

    service = RecordService()
    name_var = tk.StringVar()
    detail_var = tk.StringVar()
    status_var = tk.StringVar(value="Ready.")

    main_frame = ttk.Frame(root, padding=16)
    main_frame.pack(fill="both", expand=True)

    ttk.Label(main_frame, text="Name").pack(anchor="w")
    ttk.Entry(main_frame, textvariable=name_var).pack(fill="x", pady=(0, 10))

    ttk.Label(main_frame, text="Detail").pack(anchor="w")
    ttk.Entry(main_frame, textvariable=detail_var).pack(fill="x", pady=(0, 10))

    def on_add() -> None:
        try:
            count = service.add_record(name_var.get(), detail_var.get())
        except ValueError as exc:
            status_var.set(f"Error: {exc}")
            return

        status_var.set(f"Added record. Total records: {count}.")
        name_var.set("")
        detail_var.set("")

    ttk.Button(main_frame, text="Add", command=on_add).pack(pady=(4, 10))
    ttk.Label(main_frame, textvariable=status_var, wraplength=360).pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()
```

This starter uses a function callback instead of an app class. That is acceptable for the lab. The design requirement is not “must use a class.” The design requirement is “do not bury business rules directly inside the callback.” The service still validates and stores the record.

### Part C: Add Messagebox Feedback

After the basic status label works, add `messagebox` feedback:

```python
from tkinter import messagebox, ttk
```

Inside the error path:

```python
messagebox.showerror("Validation Error", str(exc))
```

Inside the success path:

```python
messagebox.showinfo("Success", "Record added successfully.")
```

**Instructor note:** remind students again that message boxes are modal. They briefly block interaction with the main window until dismissed. For short success or error feedback, that is fine. For long work, do not simulate progress by freezing the GUI with `sleep()`.

### Part D: Test Cases Students Must Try

Students should run all of these cases before calling the lab complete:

1. Launch the GUI.
2. Click **Add** with both fields blank.
3. Fill only the first field and click **Add**.
4. Fill both fields and click **Add**.
5. Confirm the status area changes after each attempt.
6. Confirm success or error feedback appears.
7. Close and relaunch the GUI to confirm it starts reliably.

For a contact form, add one domain-specific validation rule:

```python
if "@" not in clean_detail:
    raise ValueError("Email must include '@'.")
```

Only add that rule if the detail field is email. If the learner chose task owner or category, choose a simple rule that fits the domain, such as “category is required.” Keep the validation deterministic and local. Do not introduce files, databases, web requests, random values, or external services.

### Completion Criteria

A complete lab submission for this hour should:

1. GUI launches reliably as a Tkinter application.
2. Show a window with at least two record fields.
3. Include `Label`, `Entry`, and `Button` widgets.
4. Include a visible status area.
5. Wire the Add button to a callback.
6. Validate through a service function or service class.
7. Add action works and shows feedback when the record is valid.
8. Add action works and shows feedback when the record is invalid.
9. Keep long-running or blocking work out of the callback.
10. Include `root.mainloop()` exactly where the app is ready to start handling events.

### Instructor Circulation Prompts

Use these prompts while walking the room:

- Show me the line where your window is created.
- Show me where your widgets are placed on the screen.
- Show me the callback connected to the Add button.
- Is your button using `command=on_add` or accidentally using `command=on_add()`?
- Show me where validation happens.
- If the user enters bad data, what message appears?
- If the user enters good data, what message appears?
- What line starts the event loop?
- Are all widgets in this same parent using the same layout manager?

### Common Pitfalls During the Lab

#### Pitfall 1: Business logic inside the callback

If students put all validation rules directly inside the button handler, the app may still run, but the design is moving in the wrong direction. Coach them to move the rules into a helper function or service class.

Use this phrase:

**[Instructor speaks:]**

The callback should coordinate the interaction. The service should decide whether the record is valid.

#### Pitfall 2: Forgetting `mainloop()`

If the script appears to do nothing or the window flashes and disappears, check for `root.mainloop()`. It should be called after widgets and callbacks are set up.

#### Pitfall 3: Callback called immediately

If the callback runs before the button is clicked, look for this:

```python
command=on_add()
```

It should be:

```python
command=on_add
```

The first version calls the function during setup. The second passes the function for Tkinter to call later.

#### Pitfall 4: Widget not displayed due to layout mistakes

If a label, entry, button, or status area does not appear, check whether the student created the widget but forgot to place it with `.pack()` or `.grid()`.

Also check parent containers. A widget placed in a frame appears only if the frame itself is placed. For example, if `main_frame` is never packed, the labels inside it will not be visible either.

#### Pitfall 5: Mixing `pack()` and `grid()` in the same parent

Do not mix `pack()` and `grid()` inside the same parent container. For example, do not call `.pack()` on one child of `main_frame` and `.grid()` on another child of `main_frame`. That can cause Tkinter layout errors or confusing behavior.

It is okay to use `pack()` in one frame and `grid()` in a different frame, but that is more than we need today. For this lab, use `pack()` consistently unless the instructor explicitly provides a different starter.

#### Pitfall 6: No visible feedback

If the button works internally but the screen does not change, the user cannot tell what happened. Require at least a status label. A message box is also useful for this hour.

### Optional Extensions

Offer these only after the minimum criteria are working:

1. Clear the form after a successful add.
2. Add a small record-count label.
3. Add a **Clear** button that clears fields and resets the status message.
4. Bind the Enter key to submit.

For the Enter key extension, make it implementable. If using the function-style starter, bind Enter on the root window after `on_add()` is defined:

```python
root.bind("<Return>", lambda event: on_add())
```

If using the `ContactApp` class from the demo, bind Enter in `__init__()` after `_build_ui()`:

```python
self.root.bind("<Return>", lambda event: self.on_add())
```

If students want to focus a specific entry after clearing the form, keep a reference to that entry:

```python
name_entry = ttk.Entry(main_frame, textvariable=name_var)
name_entry.pack(fill="x", pady=(0, 10))
name_entry.focus()
```

Do not require the Enter binding for completion. It is an extension for students who finish early.

---

## Section 6: Debrief/Exit (5 minutes)

### Debrief

**[Instructor speaks:]**

Let’s name what we accomplished. We created a real desktop window. We added basic widgets. We connected a button to a callback. We sent the user’s input through service logic. We displayed feedback. Most importantly, we practiced the event-driven mental model.

In a command-line script, the program often controls the sequence. In a GUI, the user’s events control the sequence, and our callbacks respond.

### Quick Check

**Prompt:** What does mainloop() do?

**Expected answer:** It starts Tkinter’s event loop, keeps the window alive, listens for user events, and runs callbacks until the application closes.

### Additional Exit Questions

Use these if time allows:

1. What is a widget?
   - **Expected answer:** a visible UI element such as a label, entry, or button.
2. What is a callback?
   - **Expected answer:** a function that runs in response to a GUI event.
3. Why should validation live in a service layer?
   - **Expected answer:** it keeps business rules reusable, testable, and separate from display code.
4. Why should we avoid long blocking work inside callbacks?
   - **Expected answer:** it can freeze the GUI because the event loop cannot process other events smoothly.

### Pitfalls Recap

**[Instructor speaks:]**

As you continue, watch for these common mistakes:

- putting business logic directly inside callbacks,
- forgetting `mainloop()`,
- writing `command=on_add()` instead of `command=on_add`,
- creating widgets but not displaying them with a layout manager,
- mixing `pack()` and `grid()` in the same parent,
- showing no success or error feedback,
- and doing long blocking work inside a callback.

### Wrap-Up

**[Instructor speaks:]**

This hour was about getting the GUI alive and understanding how interaction flows. The big idea is not “memorize Tkinter methods.” The big idea is that a GUI is a Python program that waits for events, responds through callbacks, and still benefits from clean separation of concerns.

In the next hour, we will focus on layout and usability. We will take the same basic widgets and arrange them more intentionally with frames, spacing, resizing behavior, and clearer form structure. For now, if your app launches, accepts input, calls service logic, and shows feedback, you have the foundation.

---

## Optional Instructor Reference Notes

### One-Sentence Summary

Tkinter apps are event-driven programs where widgets gather input, callbacks respond to user actions, service logic owns validation rules, and `mainloop()` keeps the application alive and listening.

### If Students Finish Early

Invite them to:

- add a third field,
- add a record counter,
- add an Enter key binding with `root.bind("<Return>", lambda event: on_add())`,
- compare feedback in a status label versus a message box,
- or refactor a function-style solution into a small app class without adding new features.

### Instructor Reminders for Scope

- Keep the live demo between 5 and 10 minutes; this script budgets 8 minutes.
- Keep the lab between 25 and 35 minutes; this script budgets 26 minutes.
- Do not introduce database persistence yet.
- Do not introduce background threads or async techniques yet.
- Do not turn layout into the main topic; Hour 18 owns layout depth.
- Keep examples deterministic and Windows-friendly.
