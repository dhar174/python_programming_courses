# Day 5, Hour 3: Forms + Validation Feedback Patterns (Advanced)

## Instructor script purpose and scope

This hour is the practical bridge between “a form exists” and “a form is trustworthy.”
Students already built layout structure in the previous hour. In this hour, they build form behavior that protects data quality and helps users recover quickly from mistakes.

Runbook source of truth for this hour: Hour 19 in `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`.

Core outcomes for this hour are explicit and non-negotiable:

- Validate input before saving.
- Display validation errors clearly.

Required talk points for this hour:

- Inline validation vs messagebox.
- Actionable error messages.
- Disable/enable buttons when needed.

Required live demo elements for this hour:

- Highlight invalid field + show message.
- Show trimming/normalizing input before validation.

Required lab outcomes for this hour:

- Add required-field checks (non-empty).
- Show validation feedback without crashing.
- Ensure service-layer errors are surfaced cleanly.

Required completion criteria for this hour:

- Invalid entries show clear feedback.
- Valid entries save successfully.

Required pitfalls to teach explicitly:

- Silent failure (button does nothing).
- Stack trace shown to user.

Required optional extension:

- Add a Clear form button.

Required quick-check concept:

- Good validation message vs bad validation message.

Anti-drift guardrail for instructor delivery:

- Do not re-teach Hour 18 layout mechanics (grid weight tuning, spacing deep dive, frame choreography).
- Do not drift into Hour 20 list/table selection patterns (Listbox, Treeview, selection events, detail pane sync).
- Keep this hour centered on form submission quality, validation feedback patterns, and a clean UI/service boundary.

## Timing plan (must total exactly 60 minutes)

Use this exact pacing unless class conditions require very minor adjustment:

- Recap/transition: 4 minutes
- Validation principles & feedback quality: 9 minutes
- UI/service responsibility design: 8 minutes
- Live demo: 8 minutes
- Hands-on lab: 26 minutes
- Debrief/quick check/exit: 5 minutes

Runbook talk-point window alignment (10-20 minutes):

- Required talk points are delivered across Segment 2 and the opening of Segment 3 (minute 4 through minute 21 total = 17 minutes).
- This keeps inline-vs-messagebox, actionable messaging, and disable/enable behavior inside the required 10-20 minute instruction window.

Arithmetic shown explicitly:

**4 + 9 + 8 + 8 + 26 + 5 = 60**

## Learning outcomes (student-facing)

By the end of this hour, students can:

1. Explain why validation must happen before save operations.
2. Normalize input values before applying validation rules.
3. Implement required-field checks for non-empty values.
4. Show clear, actionable inline validation feedback near fields.
5. Move focus to the first invalid field so correction starts immediately.
6. Disable and re-enable the Save button at appropriate points in the save flow.
7. Surface service-layer failures to users without exposing technical stack traces.
8. Verify both failure path and success path with explicit pass/fail checks.

## Instructor setup and delivery posture

Before class, prepare a starter GUI with three fields and one Save button:

- Name
- Email
- Role
- Save

Students should already be able to run a Tkinter app.
You are not teaching raw widget layout from scratch here.
You are teaching form behavior quality and architecture boundaries.

Delivery posture for this hour:

- Keep language practical and concrete.
- Repeat that validation is both technical and communicative.
- Treat every bad input path as an expected user journey, not as an edge case.
- Model calm language. The user is not “wrong”; the form needs to guide.

Short framing line to open the hour:

“Last hour we made the form look organized. This hour we make it reliable, kind, and hard to misuse.”

## Segment 1 (4 minutes): Recap and transition

Use this speaking flow nearly verbatim:

- “Quick recap: we have form controls on screen and a Save interaction.”
- “Today we add behavior quality: when input is invalid, the app should guide, not punish.”
- “A strong form does three things every time: normalize, validate, then communicate clearly.”
- “Our focus is not on visual polish only; our focus is on trust and recoverability.”

Ask two fast warm-up questions:

1. “If Save does nothing and gives no message, what does the user think happened?”
2. “If a traceback appears in front of a user, what confidence impact does that create?”

Expected responses:

- User confusion, repeated clicks, possible duplicate submissions.
- Reduced trust, anxiety, and no clear next step.

Transition line into next segment:

“Let’s define what good validation feedback sounds like and where it should appear.”

## Segment 2 (9 minutes): Validation principles and feedback quality

### 2.1 Inline validation vs messagebox (required talk point)

Teach this contrast clearly:

Inline validation strengths:

- Keeps user attention in context.
- Connects each error to the exact field.
- Reduces interruption and cognitive reset.
- Supports correction flow without modal popups.

Messagebox strengths:

- Useful for major state changes (success confirmations in some apps, destructive actions, severe failures).
- Useful when one global action failed for a reason not tied to a single field.
- Useful when you must force acknowledgement for safety reasons.

Instructor emphasis:

“For expected input mistakes, inline is usually better. For major cross-form or system-level issues, messagebox may be appropriate.”

Practical rule for students:

- Field-level problems -> inline field message + focus behavior.
- App-level unexpected failure -> concise global status or controlled popup, never raw traceback.

### 2.2 Actionable error messages (required talk point)

Define “actionable”:

A message is actionable when it tells the user exactly what to do next.

Bad examples:

- “Invalid input.”
- “Error.”
- “Email wrong.”

Good examples:

- “Email is required.”
- “Enter an email like name@example.com.”
- “Role is required before saving.”

Even better examples include context and expected format:

- “Name is required. Use at least 2 letters.”
- “Email must include @ and a domain, for example name@example.com.”

Teach message design checklist:

- Specific field reference.
- Clear correction action.
- Neutral tone.
- No blame.
- No developer jargon.

### 2.3 Disable/enable buttons when needed (required talk point)

State this as behavior, not decoration:

- Save button should disable when save process begins.
- Save button should re-enable when processing ends, including failure path.
- This prevents accidental duplicate actions and creates clear interaction state.

Common student mistake:

- Disabling Save but forgetting to re-enable on exception path.

Instructor line:

“If you disable a control, you own re-enabling it on every path. `finally` is your safety net.”

### 2.4 Feedback stack: what user should see

When a user clicks Save with invalid input, they should see all of this:

- Clear summary feedback near Save or status area.
- Inline message under each invalid field.
- Focus moved to first invalid field.
- No crash, no console-only message as primary user signal.

Rubber Duck critique integration (required behavior):

- “Highlight invalid field” must be explicit and testable:
  - Move focus to first invalid field.
  - Show visible indication (focus + inline error text).

### 2.5 Micro-practice prompt (1 minute inside this segment)

Ask class:

“Which is better and why?”

A: “Invalid email.”
B: “Enter an email like name@example.com.”

Expected answer:

B is better because it names the expected format and gives an example.

Transition line:

“Now let’s separate responsibilities so your code stays maintainable.”

## Segment 3 (8 minutes): UI/service responsibility design

### 3.1 Why this boundary matters

If validation logic is scattered directly across button handlers and widget callbacks, code becomes fragile:

- Rules duplicated in multiple places.
- Inconsistent behavior across screens.
- Harder testing.
- Harder migration to other interfaces later.

Architecture target for this hour:

- UI layer handles interaction and presentation.
- Service layer handles normalization + validation + persistence decision.
- UI displays returned validation errors and catches service exceptions for user-friendly output.

### 3.2 Recommended service contract

Teach one clear contract:

- Input: raw strings from UI.
- Service normalizes values (trim, normalize case where appropriate).
- Service validates required fields and format rules.
- If validation fails: returns structured error map.
- If validation passes: saves and returns success payload.
- If unexpected infra/system issue: raises service exception.

Structured error map example:

```python
{
    "name": "Name is required.",
    "email": "Enter an email like name@example.com."
}
```

UI then:

- Clears old errors.
- Applies new field errors.
- Moves focus to first invalid field.
- Sets summary status line.
- Keeps app responsive.

### 3.3 Responsibility matrix to speak through

- UI owns:
  - Reading field values.
  - Clearing old UI error state.
  - Disabling/enabling Save control.
  - Rendering inline errors and summary messages.
  - Focus management.
- Service owns:
  - Input normalization.
  - Validation rule decisions.
  - Persistence call.
  - Raising controlled service errors for unexpected conditions.

### 3.4 Guardrail against drift

Say this explicitly:

“We are not doing list/table selection in this hour. That belongs to the next hour.
We are also not redoing layout fundamentals from the previous hour.
This hour is about form submission quality and clear user feedback.”

Transition line:

“Let’s implement the complete pattern end to end.”

## Segment 4 (8 minutes): Live demo (required elements included)

Demo objective:

Build a form flow that validates before save, surfaces errors clearly, highlights first invalid field through focus + inline message, normalizes input before validation, and requires Save button disable/enable behavior.

### 4.1 Demo code (runnable)

```python
from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


class ServiceSaveError(Exception):
    pass


@dataclass(slots=True)
class Contact:
    name: str
    email: str
    role: str


@dataclass(slots=True)
class ValidationResult:
    ok: bool
    errors: dict[str, str]
    record: Contact | None = None


class ContactService:
    def __init__(self) -> None:
        self._records: list[Contact] = []
        self._simulate_failure = False

    def set_failure_mode(self, enabled: bool) -> None:
        self._simulate_failure = enabled

    def validate_and_save(self, name: str, email: str, role: str) -> ValidationResult:
        clean_name = " ".join(name.strip().split())
        clean_email = email.strip().lower()
        clean_role = " ".join(role.strip().split())

        errors: dict[str, str] = {}

        if not clean_name:
            errors["name"] = "Name is required."
        elif len(clean_name) < 2:
            errors["name"] = "Name must contain at least 2 letters."

        if not clean_email:
            errors["email"] = "Email is required."
        elif "@" not in clean_email or "." not in clean_email.split("@")[-1]:
            errors["email"] = "Enter an email like name@example.com."

        if not clean_role:
            errors["role"] = "Role is required."

        if errors:
            return ValidationResult(ok=False, errors=errors)

        if self._simulate_failure:
            raise ServiceSaveError("Storage service unavailable")

        record = Contact(name=clean_name, email=clean_email, role=clean_role)
        self._records.append(record)
        return ValidationResult(ok=True, errors={}, record=record)

    def count(self) -> int:
        return len(self._records)


class ContactFormApp:
    def __init__(self, root: tk.Tk, service: ContactService) -> None:
        self.root = root
        self.service = service

        self.root.title("Hour 19 Validation Demo")
        self.root.geometry("620x390")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Fill the form, then select Save.")
        self.failure_var = tk.BooleanVar(value=False)

        self.error_vars: dict[str, tk.StringVar] = {
            "name": tk.StringVar(value=""),
            "email": tk.StringVar(value=""),
            "role": tk.StringVar(value=""),
        }

        self.entries: dict[str, ttk.Entry] = {}

        self._build_ui()
        self._wire_live_validation_state()

    def _build_ui(self) -> None:
        style = ttk.Style()
        style.configure("Error.TLabel", foreground="#b00020")
        style.configure("Status.TLabel", foreground="#1a237e")

        container = ttk.Frame(self.root, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        ttk.Label(container, text="Contact Form").grid(row=0, column=0, columnspan=3, sticky="w")

        self._add_field(container, row=1, label="Name", field_key="name", variable=self.name_var)
        self._add_field(container, row=3, label="Email", field_key="email", variable=self.email_var)
        self._add_field(container, row=5, label="Role", field_key="role", variable=self.role_var)

        self.save_btn = ttk.Button(container, text="Save", command=self.on_save)
        self.save_btn.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(10, 6))

        self.clear_btn = ttk.Button(container, text="Clear", command=self.on_clear)
        self.clear_btn.grid(row=7, column=2, sticky="ew", pady=(10, 6), padx=(8, 0))

        ttk.Checkbutton(
            container,
            text="Simulate service failure",
            variable=self.failure_var,
            command=self._on_toggle_failure_mode,
        ).grid(row=8, column=0, columnspan=3, sticky="w", pady=(4, 6))

        ttk.Label(
            container,
            textvariable=self.status_var,
            style="Status.TLabel",
            wraplength=580,
        ).grid(row=9, column=0, columnspan=3, sticky="w")

    def _add_field(
        self,
        parent: ttk.Frame,
        row: int,
        label: str,
        field_key: str,
        variable: tk.StringVar,
    ) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w")
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, columnspan=2, sticky="ew", pady=(0, 2))
        self.entries[field_key] = entry

        ttk.Label(
            parent,
            textvariable=self.error_vars[field_key],
            style="Error.TLabel",
            wraplength=420,
        ).grid(row=row + 1, column=1, columnspan=2, sticky="w", pady=(0, 8))

    def _wire_live_validation_state(self) -> None:
        for var in (self.name_var, self.email_var, self.role_var):
            var.trace_add("write", lambda *args: self._update_save_enabled_state())
        self._update_save_enabled_state()

    def _update_save_enabled_state(self) -> None:
        has_any_text = any(
            value.strip() for value in (self.name_var.get(), self.email_var.get(), self.role_var.get())
        )
        if has_any_text:
            self.save_btn.state(["!disabled"])
        else:
            self.save_btn.state(["disabled"])

    def _on_toggle_failure_mode(self) -> None:
        self.service.set_failure_mode(self.failure_var.get())

    def _clear_inline_errors(self) -> None:
        for var in self.error_vars.values():
            var.set("")

    def _focus_first_invalid(self, errors: dict[str, str]) -> None:
        if not errors:
            return
        order = ["name", "email", "role"]
        for key in order:
            if key in errors:
                self.entries[key].focus_set()
                return

    def on_save(self) -> None:
        self._clear_inline_errors()
        self.status_var.set("Saving...")
        self.save_btn.state(["disabled"])

        try:
            result = self.service.validate_and_save(
                name=self.name_var.get(),
                email=self.email_var.get(),
                role=self.role_var.get(),
            )
        except ServiceSaveError:
            self.status_var.set(
                "We could not save right now due to a service issue. Please try again in a moment."
            )
            return
        finally:
            self._update_save_enabled_state()

        if not result.ok:
            for field, message in result.errors.items():
                self.error_vars[field].set(message)
            self._focus_first_invalid(result.errors)
            self.status_var.set("Please fix the highlighted fields, then select Save again.")
            return

        assert result.record is not None
        self.status_var.set(
            f"Saved {result.record.name}. Total saved records in this run: {self.service.count()}."
        )
        self.on_clear(move_focus=False)
        self.entries["name"].focus_set()

    def on_clear(self, move_focus: bool = True) -> None:
        self.name_var.set("")
        self.email_var.set("")
        self.role_var.set("")
        self._clear_inline_errors()
        self.status_var.set("Form cleared. Enter values and select Save.")
        self._update_save_enabled_state()
        if move_focus:
            self.entries["name"].focus_set()


def main() -> None:
    root = tk.Tk()
    service = ContactService()
    ContactFormApp(root, service)
    root.mainloop()


if __name__ == "__main__":
    main()
```

### 4.2 Live demo narration script (minute by minute)

Minute 0-1:

- “I start with a service method called `validate_and_save`.”
- “Notice normalization first: trim whitespace and normalize email case.”
- “Validation decisions live here, not in the widget layout code.”

Minute 1-2:

- “Required field checks are explicit: name, email, role.”
- “Errors come back as a dictionary keyed by field.”
- “The UI can map each field to a visible inline label.”

Minute 2-3:

- “Now in `on_save`, I clear old errors first.”
- “Then I disable Save immediately.”
- “This is required behavior, not optional polish.”

Minute 3-4:

- “I call service in a `try` block.”
- “Unexpected service failure is caught and translated into a calm user message.”
- “No traceback shown to users.”

Minute 4-5:

- “In `finally`, I restore Save state using centralized logic.”
- “If no text remains in the form, Save can stay disabled. If text exists, it re-enables.”

Minute 5-6:

- “If validation fails, I set inline messages and move focus to the first invalid field.”
- “This is our explicit ‘highlight invalid field’ behavior: focus plus inline error.”

Minute 6-7:

- “If validation passes, record saves, status confirms success, and form resets cleanly.”
- “User gets immediate confirmation and can continue.”

Minute 7-8:

- “I show failure mode toggle to simulate service outage.”
- “Notice the app still behaves cleanly: user sees understandable message and app does not crash.”

### 4.3 Required demo test steps (visible, explicit, testable)

Run these in front of class:

1. Leave all fields blank, click Save.
   - Expected:
     - Inline messages appear under required fields.
     - Focus moves to Name.
     - Status tells user to fix highlighted fields.
2. Enter only spaces in Name and Role, invalid email text in Email.
   - Expected:
     - Trimming catches non-empty illusion.
     - Email format message appears with actionable example.
3. Enter valid Name, Email, Role.
   - Expected:
     - Save succeeds.
     - Success status shown.
     - Form clears.
4. Enable simulated service failure and enter valid data.
   - Expected:
     - User sees clean service issue message.
     - No crash.
     - No stack trace in UI.
5. Verify Save button behavior.
   - Expected:
     - Save disabled while processing.
     - Save state returns appropriately after processing.

Instructor line after test steps:

“If your class implementation does not pass these five checks, it is not complete yet.”

## Segment 5 (26 minutes): Hands-on lab (required 25-35, set to 26)

### 5.1 Lab objective statement for students

“Add validation behavior to your form so that invalid input is guided clearly, valid input saves successfully, and service-layer failures are surfaced cleanly without crashing.”

### 5.2 Lab constraints and required deliverables

Students must implement all of the following:

1. Required-field checks for non-empty values.
2. Input normalization before validation (at least trim whitespace).
3. Inline validation feedback near invalid fields.
4. Focus movement to first invalid field.
5. Save button disable/enable behavior in submission flow.
6. User-friendly handling of service-layer error conditions.
7. No user-facing stack traces.
8. Demonstrable valid save path.

### 5.3 Lab timeline inside the 26-minute block

- Minute 0-3: Read lab goal, open starter app, identify save flow location.
- Minute 3-9: Implement service normalization + required validation.
- Minute 9-14: Add UI inline error mapping and summary status line.
- Minute 14-18: Implement focus-to-first-invalid behavior.
- Minute 18-21: Add Save disable/enable behavior with safe restoration.
- Minute 21-24: Add service failure handling path with clean message.
- Minute 24-26: Run pass/fail checklist and prepare one-minute share.

### 5.4 Lab starter architecture guidance (say aloud while circulating)

- “If your Save handler is too long, split helper functions.”
- “Keep rule decisions in service, display decisions in UI.”
- “Return structured errors when input is fixable.”
- “Raise controlled service exception for infrastructure issues.”
- “Catch service exception in UI and convert to user-safe message.”

### 5.5 Instructor circulation checklist

As you move through the room, verify these quickly:

- Are they trimming strings before required checks?
- Are blank-space-only values rejected?
- Do messages mention the field and next action?
- Does first invalid field receive focus?
- Do inline messages disappear on subsequent successful save?
- Is Save state restored after both success and failure?
- Is there any path where button click appears to do nothing?
- Is any traceback visible to user-facing UI?

### 5.6 Required lab acceptance tests (students must run)

Students should execute these exact tests:

Test A: Invalid path (empty fields)

- Action: Leave fields empty, click Save.
- Required result:
  - Clear feedback appears.
  - First invalid field is focused.
  - Save does not crash app.
  - Save button state follows input rules and re-enables immediately after user enters valid correction input.

Test B: Invalid path (whitespace and malformed email)

- Action: Name = spaces, Email = “abc”, Role = spaces, click Save.
- Required result:
  - Whitespace is trimmed then rejected.
  - Email message gives actionable format guidance.
  - UI remains stable.

Test C: Valid path

- Action: Name = “Ava Stone”, Email = “Ava.Stone@Example.com”, Role = “Data Lead”, click Save.
- Required result:
  - Save succeeds.
  - Normalized value behavior is applied where implemented.
  - Success feedback appears.
  - Inline errors are cleared.

Test D: Service error path

- Action: Trigger service failure mode and submit valid data.
- Required result:
  - User sees clean service failure message.
  - No stack trace shown in UI.
  - App remains interactive.

Test E: Save control behavior

- Action: Click Save during processing path.
- Required result:
  - Save disables while processing.
  - Save re-enables correctly when done.

### 5.7 Explicit pass/fail completion checklist (required by critique)

Use this exact checklist at the end of lab.

#### Invalid-path checklist (must all pass)

- Pass/Fail: Invalid entries show clear feedback.
- Pass/Fail: Inline error appears for each invalid required field.
- Pass/Fail: Focus moves to first invalid field.
- Pass/Fail: Summary status explains next action.
- Pass/Fail: Save button behavior is correct (disabled during processing, enabled appropriately after).
- Pass/Fail: App does not crash on invalid input.
- Pass/Fail: No silent failure (button does nothing).

#### Valid-path checklist (must all pass)

- Pass/Fail: Valid entries save successfully.
- Pass/Fail: Success message is visible and specific.
- Pass/Fail: Prior error messages are cleared.
- Pass/Fail: Form state is ready for next entry.
- Pass/Fail: Save control returns to correct enabled state.

Instructor instruction:

“A solution is complete only when both invalid-path and valid-path checklists pass.”

### 5.8 Required lab checklist item for Save button behavior

State this explicitly during lab kickoff:

“Disabling and re-enabling Save is required in this lab. It is not optional and not only a discussion point.”

### 5.9 Service-layer error surfacing pattern (student coaching script)

If a student asks, “Should I just `print(e)` and move on?” answer:

- Print can help developers during development.
- User still needs a clear on-screen message.
- The UI must never expose raw technical exceptions as user feedback.
- Use concise phrasing:
  - “We could not save right now. Please try again.”
  - Add more detail only if it helps user action.

### 5.10 Common student implementation traps during lab

Trap 1: Validation in too many places

- Symptom: one rule in UI, another in service.
- Risk: inconsistent outcomes.
- Fix: put canonical rule in service; UI displays results.

Trap 2: Old errors remain after success

- Symptom: success message appears but old field errors still visible.
- Fix: clear inline errors at start of save and on success.

Trap 3: Button lockout bug

- Symptom: Save stays disabled forever after exception.
- Fix: restore state in `finally` or centralized state updater.

Trap 4: Missing normalization

- Symptom: “  Ava  ” accepted as odd formatting or blank spaces accepted as non-empty.
- Fix: normalize first, validate second.

Trap 5: Non-actionable feedback

- Symptom: “Invalid value.”
- Fix: include field and correction guidance.

### 5.11 Optional extension for early finishers (required runbook extension)

Optional extension:

- Add a **Clear form** button.

Extension success criteria:

- Clears all field values.
- Clears inline errors.
- Resets summary status.
- Returns focus to first field.
- Recomputes Save enabled state.

## Segment 6 (5 minutes): Debrief, quick check, exit

### 6.1 Debrief talking points

Use this concise summary:

- “Validation before save protects data integrity.”
- “Feedback quality protects user confidence.”
- “Service decides rules; UI decides presentation.”
- “A complete feature includes invalid path and valid path.”

Reinforce anti-drift closure:

“Next hour we move to record list/table selection behavior. That is separate from this hour’s form validation responsibility.”

### 6.2 Quick check (required prompt included)

Ask this required question:

“Give me a good validation message and a bad validation message for email.”

Expected answers:

- Bad: “Invalid email.”
- Good: “Enter an email like name@example.com.”

Follow-up prompt:

“What makes the good one better?”

Expected:

- Specific.
- Actionable.
- Gives example format.

### 6.3 Exit ticket (fast verbal or written)

Prompt 1:

“Where should normalization and validation rules live by default in this app architecture?”

Expected:

- Service layer.

Prompt 2:

“What are the two required completion truths for this hour?”

Expected exact ideas:

- Invalid entries show clear feedback.
- Valid entries save successfully.

Prompt 3:

“What is one behavior that proves your UI highlights invalid field in a testable way?”

Expected:

- Focus moves to first invalid field and inline error is visible.

## Instructor reference: concise rubric for grading in-class implementations

Use this rubric when evaluating student submissions during or right after class.

### Category A: Validation correctness

- Required checks exist for non-empty fields.
- Trimming/normalization occurs before validation.
- Invalid path does not write data.
- Valid path writes data.

### Category B: Feedback clarity

- Inline field error messages visible.
- Summary status line communicates what to do next.
- Messages are actionable, not generic.
- Tone is neutral and user-centered.

### Category C: Interaction quality

- Focus moves to first invalid field.
- Save button disable/enable behavior works correctly.
- App remains responsive after failures.
- Old errors cleared on subsequent attempts.

### Category D: Error handling boundary

- Service-layer failures are caught and surfaced cleanly.
- No stack trace shown to user.
- No silent failure path.

Pass recommendation:

- All items in A and C pass.
- At least 3 of 4 in B pass.
- All items in D pass.

## Extended speaking notes for deeper instructor confidence

Use these notes if students ask “why not just validate in the UI directly?”

Answer structure:

1. UI-level validation alone is brittle.
2. Service-level validation is reusable and testable.
3. Another interface can reuse same service rules.
4. UI still plays critical role by communicating errors clearly.

If students ask “why show both summary and inline errors?”:

- Summary gives global state and next action.
- Inline gives precise field correction.
- Together they reduce confusion and speed recovery.

If students ask “should we validate on every keystroke?”:

- Not required for this hour.
- Start with submit-time validation.
- Add real-time validation later when it clearly improves UX and avoids noisy feedback.
- Keep rules and messages consistent across modes.

If students ask “can we just use messagebox for everything?”:

- You can, but it often hurts flow for predictable field errors.
- Inline keeps context and supports quick correction.
- Reserve modal interruptions for cases where interruption is useful.

If students ask “how strict should validation be?”:

- Be strict enough to protect data quality.
- Be lenient enough to avoid blocking valid user intent unnecessarily.
- Keep rules explicit and predictable.
- Provide examples in messages for format-sensitive fields.

## Practical language bank for instructor and students

Helpful phrases to model during class:

- “Please fix the highlighted fields, then save again.”
- “Email is required.”
- “Enter an email like name@example.com.”
- “Name must contain at least 2 letters.”
- “We could not save right now. Please try again.”

Phrases to avoid:

- “Invalid input.”
- “Something broke.”
- “Bad value.”
- Technical internals as user feedback.

## Required pitfalls section (must be spoken and shown)

### Silent failure (button does nothing)

What it looks like:

- User clicks Save.
- No message appears.
- No visible change in UI.
- User cannot tell if action happened.

Why it is harmful:

- User retries unpredictably.
- Trust drops.
- Duplicate attempts may occur.
- Support load increases.

How to prevent:

- Always set status text after Save attempt.
- Always show inline errors for invalid fields.
- Always handle catch path with user-visible message.

### Stack trace shown to user

What it looks like:

- Raw exception details appear in UI.
- Technical file paths or traceback lines visible.

Why it is harmful:

- Confusing and alarming for users.
- Leaks technical details.
- Does not help correction.

How to prevent:

- Catch known service exceptions in UI.
- Convert to clean, user-centered message.
- Keep technical logging separate from user presentation.

## Scripted mini walk-through of good vs bad messaging (2-minute insert if needed)

Say:

“I will show two versions of the same outcome.”

Version 1:

- Status: “Error.”
- Field: none highlighted.
- Result: user confusion.

Version 2:

- Email inline: “Enter an email like name@example.com.”
- Focus moved to email field.
- Status: “Please fix the highlighted fields, then select Save again.”
- Result: user knows exactly what to do.

Ask:

“Which version reduces retries and support requests?”

Expected:

- Version 2.

## Reinforcement of required behaviors for this hour

Before ending class, restate these as checklist truths:

- Validation happens before save.
- Errors are shown clearly and actionably.
- First invalid field gets focus and inline message.
- Save button disables/enables correctly during save flow.
- Service-layer failures are surfaced cleanly.
- Invalid entries show clear feedback.
- Valid entries save successfully.

If any student solution misses one of these, coach revision immediately.

## Anti-drift closing note for instructor planning

For lesson continuity:

- End this hour after form validation and feedback quality are working.
- Do not begin table/list selection mechanics here.
- Carry forward saved data concepts only as context, not as new list UI implementation.

Bridge sentence to next hour:

“Now that form input is reliable, next we will show saved records in list/table views and react to selection events.”

## Compact one-page delivery checklist (for your podium notes)

- Time arithmetic visible: 4 + 9 + 8 + 8 + 26 + 5 = 60
- Talk points covered:
  - Inline validation vs messagebox
  - Actionable messages
  - Disable/enable buttons
- Demo includes:
  - Trim/normalize before validate
  - Focus first invalid field + inline message
  - Save disable/enable behavior
  - Clean service-error surfacing
- Lab includes:
  - Required-field checks
  - Non-crashing invalid path
  - Service-layer error handling
  - Required Save button state behavior
  - Pass/fail checklist for invalid and valid path
- Completion criteria spoken:
  - Invalid entries show clear feedback
  - Valid entries save successfully
- Pitfalls spoken:
  - Silent failure (button does nothing)
  - Stack trace shown to user
- Optional extension offered:
  - Clear form button
- Quick check asked:
  - Good validation message vs bad validation message

This completes Hour 19 delivery with strict runbook alignment and explicit, testable validation behavior.

(agent_id: issue297-hour3-rewrite — use write_agent to send follow-up messages)