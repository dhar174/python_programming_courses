# Day 5, Hour 3: Forms, Validation, and User Feedback Patterns

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 5
- **Hour**: 3 of 4 for this session, corresponding to **Hour 19** in the 48-hour runbook
- **Focus**: Form validation, inline feedback, actionable error messages, and clean UI/service responsibilities
- **Runbook alignment**: Validate input before saving; display validation errors clearly; discuss inline validation versus message boxes; trim/normalize input before validation; disable/enable buttons when useful
- **Prerequisites**:
  - Students can build a small Tkinter GUI
  - Students understand functions, exceptions, and service-layer separation
  - Students are comfortable with dictionaries and basic control flow
- **Teaching goal**: Show that validation is both a technical responsibility and a communication responsibility
- **Demo app theme**: Continue the contact form from the earlier hours
- **Key message to repeat**: “Good validation helps the user succeed.”
- **Success criteria for the hour**:
  - Students validate before saving
  - Students display field-specific or summary feedback clearly
  - Students avoid crashing or showing tracebacks to end users
  - Students can explain the difference between service-layer validation and UI presentation

---

## Timing Overview

| Segment | Time |
|---|---:|
| Recap and transition from layout to form quality | 5 minutes |
| Validation principles and good feedback patterns | 12 minutes |
| Designing UI and service responsibilities for validation | 10 minutes |
| Live demo: inline validation and clean error handling | 13 minutes |
| Hands-on lab: add actionable validation feedback | 15 minutes |
| Debrief, quick checks, exit ticket, wrap-up | 5 minutes |

**Total:** 60 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, students should be able to:

1. Validate form input before saving data.
2. Explain the difference between service-layer validation and UI feedback.
3. Trim and normalize user input before validating it.
4. Display clear, actionable error messages in a GUI.
5. Use inline validation feedback instead of relying only on message boxes.
6. Avoid exposing stack traces or raw exceptions to end users.
7. Disable or re-enable buttons appropriately during save actions when needed.

---

## Section 1: Recap and Transition (5 minutes)

### Quick Re-entry

**[Instructor speaks:]**

Last hour, we made our GUI cleaner. This hour, we make it safer and kinder.

A form is not complete just because it has text boxes and a Save button. A good form helps the user succeed. That means:

- checking input before saving
- explaining what is wrong
- pointing toward the next step
- staying stable after errors

### Framing the Hour

**[Instructor speaks:]**

Today’s central question is:

> When the user enters bad input, what should happen?

The wrong answers include:

- the app crashes
- nothing happens
- the user sees a traceback
- the message is vague, such as “Invalid input”

The better answer is:

- validate early
- normalize input first
- show specific feedback
- keep the app stable
- help the user recover immediately

---

## Section 2: Validation Principles (12 minutes)

### Validation Should Be Helpful, Not Punitive

**[Instructor speaks:]**

Validation is not there to scold the user. Validation is there to guide the user.

A good validation message is:

- specific
- actionable
- calm in tone
- tied to the relevant field or action

Examples:

**Bad:** `Invalid input.`  
**Better:** `Email is required.`  
**Best:** `Enter an email address such as name@example.com.`

### Normalize Before You Validate

**[Instructor speaks:]**

Users do not always type data in a perfectly clean format. Before validating, it is often useful to normalize.

Examples:

- strip surrounding spaces
- lowercase an email address
- collapse accidental extra whitespace
- standardize capitalization if appropriate

This is usually service logic, not layout logic.

### Inline Feedback vs Message Boxes

**[Instructor speaks:]**

Message boxes are useful, but they interrupt the user. For many predictable form mistakes, inline feedback is better.

Inline feedback might be:

- a small error label under a field
- a summary message near the Save button
- focus moved to the first invalid field

Message boxes are more appropriate for:

- save completed successfully
- delete confirmation
- serious unexpected failure

### Service Errors vs UI Errors

**[Instructor speaks:]**

The service layer should decide whether the data is valid.

The UI layer should decide how that result is presented.

That means the service might return:

- a saved object
- a dictionary of field errors
- or raise an exception for something unexpected

The UI then chooses how to display that outcome.

### Quick Check

**[Ask students:]**

Why is “Enter an email address such as name@example.com” better than “Invalid email”?

**Expected answer:** because it tells the user what to fix and gives a useful example.

---

## Section 3: A Clean Validation Pattern (10 minutes)

### Suggested Submission Flow

**[Instructor speaks:]**

A clean form-submission flow looks like this:

1. Read values from the UI.
2. Normalize them.
3. Validate them in the service layer.
4. If errors exist, return them without crashing.
5. The UI displays field-level and summary feedback.
6. If the data is valid, save it and reset the form.

### Why Structured Errors Help

**[Instructor speaks:]**

For predictable user mistakes, a structure like this is often easier to work with than generic exceptions:

```python
{
    "name": "Name is required.",
    "email": "Enter an email address such as name@example.com.",
}
```

That gives the UI something concrete to display next to the right fields.

### When Exceptions Still Make Sense

**[Instructor speaks:]**

Not every problem is just a field-level validation issue. Some failures are unexpected:

- file I/O problems
- network issues
- database errors
- corrupted external input

Those are good candidates for exceptions. But even then, the UI should catch them and present a calm message instead of a traceback.

### Disabling and Re-Enabling Buttons

**[Instructor speaks:]**

Even in a simple form, disabling a button temporarily can prevent accidental double-clicks or repeated submissions.

The flow can be:

- disable Save
- run validation/save logic
- re-enable Save
- show result

This pattern becomes even more useful when saving later involves slower work.

---

## Section 4: Live Demo — Inline Validation and Actionable Feedback (13 minutes)

### Demo Framing

**[Instructor speaks:]**

I will build a contact form that:

- trims and normalizes input
- validates required fields
- shows field-specific errors
- shows a summary status message
- keeps service logic separate from UI logic

Watch for the division of responsibilities between the service and the UI.

### Demo Code

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass(slots=True)
class ContactRecord:
    name: str
    email: str
    role: str


class ContactFormService:
    def __init__(self) -> None:
        self._records: list[ContactRecord] = []

    def validate_and_save(
        self,
        name: str,
        email: str,
        role: str,
    ) -> tuple[ContactRecord | None, dict[str, str]]:
        clean_name = name.strip()
        clean_email = email.strip().lower()
        clean_role = role.strip()

        errors: dict[str, str] = {}

        if not clean_name:
            errors["name"] = "Name is required."

        if not clean_email:
            errors["email"] = "Email is required."
        elif "@" not in clean_email:
            errors["email"] = "Enter an email address such as name@example.com."

        if not clean_role:
            errors["role"] = "Role is required."

        if errors:
            return None, errors

        record = ContactRecord(
            name=clean_name,
            email=clean_email,
            role=clean_role,
        )
        self._records.append(record)
        return record, {}


class ContactFormApp:
    def __init__(self, root: tk.Tk, service: ContactFormService) -> None:
        self.root = root
        self.service = service

        self.root.title("Validated Contact Form")
        self.root.geometry("540x320")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Enter contact information.")

        self.error_vars = {
            "name": tk.StringVar(),
            "email": tk.StringVar(),
            "role": tk.StringVar(),
        }

        self.entry_widgets: dict[str, ttk.Entry] = {}

        self._build_ui()

    def _build_ui(self) -> None:
        style = ttk.Style()
        style.configure("Error.TLabel", foreground="firebrick")
        style.configure("Status.TLabel", foreground="navy")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(1, weight=1)

        self._add_field(main_frame, "Name", "name", self.name_var, 0)
        self._add_field(main_frame, "Email", "email", self.email_var, 2)
        self._add_field(main_frame, "Role", "role", self.role_var, 4)

        self.save_button = ttk.Button(
            main_frame,
            text="Save Contact",
            command=self.on_save,
        )
        self.save_button.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(12, 8))

        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            style="Status.TLabel",
            wraplength=460,
        ).grid(row=7, column=0, columnspan=2, sticky="w")

    def _add_field(
        self,
        parent: ttk.Frame,
        label_text: str,
        field_name: str,
        variable: tk.StringVar,
        row: int,
    ) -> None:
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky="w", pady=(0, 2))

        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=(0, 2))
        self.entry_widgets[field_name] = entry

        ttk.Label(
            parent,
            textvariable=self.error_vars[field_name],
            style="Error.TLabel",
        ).grid(row=row + 1, column=1, sticky="w", pady=(0, 8))

    def clear_errors(self) -> None:
        for error_var in self.error_vars.values():
            error_var.set("")

    def on_save(self) -> None:
        self.clear_errors()
        self.save_button.state(["disabled"])

        try:
            record, errors = self.service.validate_and_save(
                self.name_var.get(),
                self.email_var.get(),
                self.role_var.get(),
            )
        except Exception as exc:
            # In a real app you might log this to a file; for the demo, console is enough.
            print(f"Unexpected error while saving contact: {exc!r}")
            self.status_var.set(
                "Something went wrong while saving. Please try again, "
                "or contact support if the problem persists."
            )
            return
        finally:
            self.save_button.state(["!disabled"])

        if errors:
            for field_name, message in errors.items():
                self.error_vars[field_name].set(message)

            first_field = next(iter(errors))
            self.entry_widgets[first_field].focus_set()
            self.status_var.set("Please correct the highlighted fields and try again.")
            return

        assert record is not None
        self.status_var.set(f"Saved contact for {record.name}.")
        self.name_var.set("")
        self.email_var.set("")
        self.role_var.set("")
        self.entry_widgets["name"].focus_set()


def main() -> None:
    root = tk.Tk()
    service = ContactFormService()
    ContactFormApp(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### Demo Steps

1. Define the data model.
2. Build the service method so it normalizes input and returns structured errors.
3. Create `StringVar` values for the fields and status line.
4. Add inline error labels beneath each field.
5. Wire the Save button to `on_save()`.
6. Clear old errors before each attempt.
7. Disable and re-enable the Save button during submission.
8. On error, populate field-specific messages and move focus to the first invalid field.
9. On success, clear the form and show a confirmation message in the status line.

### Demo Narration

**[Instructor speaks while coding:]**

Notice that predictable validation problems do not crash the program. Instead, the service returns structured information, and the UI shows that information where it is useful.

Also notice that the UI is responsible for presentation details:

- clearing previous errors
- placing messages near the right fields
- moving focus
- resetting the form after success

That work belongs in the GUI layer.

### Live Questions to Ask During the Demo

**[Ask students:]**

Why do we call `.strip()` before validating?

**Expected answer:** to remove accidental surrounding spaces so validation uses the intended value.

**[Ask students:]**

Why is inline feedback often better than a popup for common form mistakes?

**Expected answer:** because it keeps the user in context and points directly to the problem.

**[Ask students:]**

Why is the Save button disabled and then re-enabled?

**Expected answer:** to control the interaction flow and prevent accidental repeat actions during submission.

### Important Instructor Note

If students ask about changing entry field colors directly, explain that ttk widget styling can vary by platform and theme. For a course-friendly, portable approach, inline error labels, summary text, and focus placement are excellent validation patterns.

---

## Section 5: Hands-On Lab — Add Validation Feedback Without Crashing (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Now enhance your own form so that bad input is handled gracefully and helpfully.

The guiding rule for this lab is:

> No silent failure, and no traceback shown to the user.

### Student Task

Update your GUI so that it:

- checks required fields before saving
- normalizes input where appropriate
- displays at least one inline field-level error
- displays a summary status message
- keeps the application running after invalid input
- surfaces service-layer errors cleanly

### Hands-On Lab Guidance

**[Instructor speaks:]**

Do not start by adding lots of edge cases. First, handle one or two clear rules well.

A good minimum is:

- one required text field
- one required email-like field
- one summary message
- one service method that returns errors

Then improve the user experience:

- clear old errors before new validation
- move focus to the first invalid field
- leave the form available for correction

### Completion Criteria

A strong minimum solution should:

1. Reject missing required data.
2. Show clear validation messages.
3. Avoid crashing on bad input.
4. Keep business rules out of widget layout code.
5. Let the user correct the form and try again immediately.

### Circulation Prompts

**[Circulate and ask:]**

1. Which errors are predictable user mistakes?
2. Are you trimming input before validating?
3. Is your error message actionable?
4. What does the user see if validation fails?
5. What changes visibly after a successful save?

### Common Pitfalls During the Lab

#### Pitfall 1: Silent failure
If the button is clicked and nothing changes, the user cannot tell what happened.

#### Pitfall 2: Stack trace shown to the user
Predictable form mistakes should become user-friendly feedback, not raw technical output.

#### Pitfall 3: Vague messages
“Invalid field” is too broad. The user needs a direct next step.

#### Pitfall 4: Old errors remain after success
Students should clear previous error messages before applying new ones.

### Optional Extensions

- Add a **Clear Form** button
- Disable Save until at least one field contains text
- Add a duplicate-email rule in the service layer
- Add a short error-summary banner at the top of the form

---

## Section 6: Debrief, Quick Checks, Exit Ticket, and Wrap-Up (5 minutes)

### Group Debrief

**[Instructor speaks:]**

A usable form does not just collect data. It teaches the user how to succeed.

Validation is both technical and communicative:

- the code checks correctness
- the interface explains the result

### Quick Checks

**Prompt:** What makes a validation message good?  
**Expected answer:** it is specific, actionable, and helps the user fix the issue.

**Prompt:** Why is normalization often done before validation?  
**Expected answer:** because it removes accidental formatting issues like extra spaces and gives cleaner input to validate.

### Exit Ticket

**Prompt 1:** What is the difference between service-layer validation and UI feedback?  
**Expected answer:** the service decides whether the data is valid; the UI decides how to show that result.

**Prompt 2:** What is a better validation message: `Invalid email` or `Enter an email address such as name@example.com`? Why?  
**Expected answer:** the second one, because it is more specific and actionable.

**Prompt 3:** Why should predictable user mistakes usually not appear as raw exceptions to the user?  
**Expected answer:** because users need guidance, not developer diagnostics.

### Common Pitfalls Recap

- silent failure
- vague messages
- showing technical errors to users
- validating without normalizing
- forgetting to clear prior errors

### Wrap-Up

**[Instructor speaks:]**

We now have forms that look better and behave better. In the next hour, we will make the app feel more complete by displaying multiple records in a list or table and reacting to user selection.

A strong pattern to carry forward is:

- normalize
- validate in the service layer
- return structured results
- present field-level feedback in the UI
- keep the application stable

---

## Optional Instructor Reference Notes

### Strong Student Solution Characteristics
Look for solutions where:

- service methods return structured validation results
- the UI visibly responds to errors
- focus moves to the first invalid field
- the feedback language is polite and specific

### If Students Finish Early
Invite them to:

- add duplicate-record detection
- add a reset button that clears errors too
- disable Save until required fields are non-empty
- compare a popup-only approach with an inline approach

---
