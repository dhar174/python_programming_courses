# Day 1, Hour 3: Properties, Invariants, and Custom Exceptions

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 1, Hour 3 of 48
- **Focus**: Properties, invariants, and custom exceptions in a tracker-domain model.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 1, Hour 3.
- **Prerequisites**: Learners should be able to define classes, write `__init__` methods, create instances, call methods, write simple service functions, and use basic `try`/`except` syntax.
- **Advanced trajectory**: This hour moves learners from PCAP-level object syntax toward PCPP1-style defensive domain design: objects protect their own valid state, services communicate domain failures clearly, and caller code handles expected errors without hiding unexpected bugs.
- **Instructor goal**: By the end of this hour, every learner has added at least one validated `@property`, defined `ValidationError` and `NotFoundError`, updated one service function to raise a domain exception, and written caller code that catches specific exceptions and prints user-friendly messages outside the model and service layer.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Hour 2 | 5 min | Connect class responsibilities to protecting valid object state |
| Outcomes and key vocabulary | 5 min | Define property, backing attribute, invariant, and domain exception |
| Concept briefing: controlled access and domain failures | 10 min | Explain why validation belongs at boundaries and why exceptions beat silent failure |
| Live demo: validated tracker model and service exception | 10 min | Build deterministic code using `@property`, `ValidationError`, and `NotFoundError` |
| Guided lab: validation and exceptions | 25 min | Learners add validation, custom exceptions, service raising, and caller handling |
| Quick check, completion criteria, and wrap-up | 5 min | Confirm specific-exception handling and preview Hour 4 |

This is a one-hour plan. The timed teaching headings above total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays within the runbook's required 25-35 minute lab range. If the room needs support, protect the guided lab by using prepared starter code and live-coding only the property setter, service exception, and caller handling. Do not weaken the required objectives by making validation, `ValidationError`, or `NotFoundError` optional; those are core outcomes for this hour.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain a property as controlled access to an attribute.
2. Use `@property` and a setter to validate assignment before data is stored.
3. Use a backing attribute such as `_title` or `_priority` to avoid recursive property calls.
4. Define an invariant as a rule that must always be true for a valid object.
5. Identify reasonable invariants for a tracker-domain model, such as a non-empty title or a priority inside an allowed range.
6. Define custom exceptions for domain errors, including `ValidationError` and `NotFoundError`.
7. Explain why returning `None` or `False` for domain failures can create silent bugs.
8. Update a service function so missing items raise a clear domain exception.
9. Write caller-level `try`/`except` code that catches specific custom exceptions and prints a user-friendly message outside the model and service.
10. Avoid broad `except Exception` handling except when explicitly discussing it as an anti-pattern.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 1, Hour 3 visible for yourself. The required scope is properties, invariants, custom exceptions, validation rules, service exceptions, caller handling, pitfalls, optional extensions, and a quick check about catching specific exceptions.
- Open the learner project from Hour 2, or prepare a clean `advanced_tracker` workspace with a `src/` directory.
- Prepare a blank file named `day1_hour3_validation_demo.py` for the live demo, or be ready to create it in front of the class.
- Confirm the terminal command for the environment. Use `python day1_hour3_validation_demo.py` if `python` works. If the lab requires `python3`, consistently say and show `python3 day1_hour3_validation_demo.py`.
- Prepare a board or shared note with these definitions:

```text
Property: controlled access to an attribute.
Backing attribute: the actual stored value, usually named with a leading underscore.
Invariant: a rule that must always be true for the object to be valid.
Domain exception: an error type that describes a meaningful problem in the application domain.
```

- Have the Hour 2 boundary idea ready: model objects represent domain state and behavior; service functions coordinate use cases; caller or UI code decides what to display.
- Be ready to correct two common mistakes early: assigning to the public property inside its own setter, and catching `Exception` broadly around code that should catch `ValidationError` or `NotFoundError` specifically.
- Decide whether learners may continue their Hour 2 tracker domain or use the task tracker shown here. Either is acceptable as long as they meet the completion criteria.

Suggested board note before the session starts:

```text
Day 1 Hour 3 goals:
1. Protect model state with @property
2. Name always-true rules as invariants
3. Raise ValidationError for invalid domain data
4. Raise NotFoundError for missing domain objects
5. Catch specific exceptions at the caller boundary
```

---

## Opening Bridge from Hour 2 (5 minutes)

**Instructor talk track**

"In Hour 2, we practiced designing classes from requirements. We asked what an object knows, what it does, and where boundaries belong. We used a tracker-style domain because trackers are familiar: tasks, habits, expenses, inventory items, contacts, books, workouts, or support tickets. The exact domain can change, but the design questions stay the same."

"One of our most important conclusions was that a model object should own the rules about the thing it represents. A `Task` object should know what makes a task valid. A `Contact` object should know what makes a contact valid. A `BudgetItem` object should know what makes a budget item valid. The terminal interface should not be the only thing preventing bad data, because later we may have a web form, an API endpoint, a test, a file import, or another service function creating those same objects."

"Today we take the next step. In Hour 2, a class could hold data and expose behavior. In Hour 3, the class starts protecting itself. We are going to use properties to control access to attributes. We are going to name the rules that must always be true. Those rules are called invariants. And we are going to define custom exceptions so domain failures are clear, specific, and catchable."

Pause and ask:

"Imagine our task tracker says priority must be between 1 and 5. If I create `Task('Refactor report', priority=99)`, what should happen?"

Take two or three responses. Learners may say "print an error," "return False," "do not allow it," or "raise an exception." Use those answers to transition:

"The core idea is that the object should not quietly become invalid. If a task with priority 99 is not meaningful in our domain, then the model should refuse that value. It should refuse the value at the moment the value is assigned, not three screens later when another function finally notices something is wrong."

"This is a professional habit. Advanced code does not assume every caller will behave perfectly. Advanced code makes illegal states difficult or impossible to represent."

**Transition**

"Let's name the tools we will use, then we will live-code a small tracker model that enforces its own rules."

---

## Outcomes and Key Vocabulary (5 minutes)

Use this section to make the vocabulary concrete before showing syntax.

**Instructor talk track**

"The first term is **property**. In Python, a property lets an attribute look simple from the outside while still running code behind the scenes. From the caller's perspective, `task.priority = 3` still looks like normal assignment. But inside the class, that assignment can call a setter method that checks the value before storing it."

"The second term is **backing attribute**. When we use a property, we usually store the actual value in an attribute with a leading underscore, such as `_priority`. The underscore is a convention that says, 'This is internal. Use the property instead.' It is not the same as strict private visibility in some other languages, but it is an important Python signal."

Write:

```python
task.priority      # public property
task._priority     # internal backing attribute
```

"The third term is **invariant**. An invariant is a rule that must always be true for the object to be valid. Not just usually true. Not just true after the user interface cleans things up. Always true. For a task tracker, examples could be: the title is not empty, priority is from 1 to 5, status is one of a known set of statuses, or completed tasks have a completion timestamp. Today we will keep the invariant small and testable: title must be non-empty, and priority must be an integer from 1 to 5."

"The fourth term is **custom exception**. Python already has built-in exceptions such as `ValueError`, `KeyError`, and `TypeError`. Those are useful. But in application code, we often want errors that speak the language of our domain. `ValidationError` tells us a domain value failed validation. `NotFoundError` tells us a requested domain object does not exist. Those names are more meaningful than returning `None` and hoping the caller remembers to check."

**Short prediction prompt**

"If a function returns `None` when it cannot find a task, what might happen if the caller forgets to check for `None`?"

Expected learner answers:

- The program may fail later with a confusing error.
- The caller might treat `None` as a real value.
- The bug may be farther away from the real cause.

Respond:

"Exactly. Returning `None` can be appropriate in some designs, but for required domain operations, a specific exception often gives a clearer signal. It says: this use case failed, and here is the reason."

---

## Concept Briefing: Controlled Access and Domain Failures (10 minutes)

**Instructor talk track**

"Let's connect this to our Hour 2 boundary model. We had three rough layers. The model represents the domain object. The service function coordinates a use case. The caller, which could later become a command-line interface or web route, decides how to communicate with a human."

Write:

```text
Model: protects valid state
Service: coordinates a use case
Caller/UI: catches expected errors and displays messages
```

"A common beginner pattern is to validate only in the user interface. For example, the program asks for a priority, checks whether it is between 1 and 5, and then creates a `Task`. That is a useful first step, but it is not enough for advanced design. Why? Because the user interface is not the only caller. A test can create a task. A file import can create a task. Another service function can create a task. A future API endpoint can create a task. If the rule matters to the domain, the model should enforce it."

"That does not mean we never validate anywhere else. In real systems, validation can happen at multiple boundaries. A web form may validate early to give fast feedback. An API may validate request data. But the model should still protect its own invariants. The model is the last line of defense for its own validity."

"Here is the syntax pattern we will use."

```python
class Task:
    def __init__(self, priority: int) -> None:
        self.priority = priority

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int) -> None:
        if value < 1:
            raise ValidationError("Priority must be at least 1.")
        self._priority = value
```

"Notice something subtle and important in `__init__`: we assign to `self.priority`, not directly to `self._priority`. That means object creation uses the same validation path as later assignment. If someone creates a task with a bad priority, the setter rejects it. If someone later changes the priority to a bad value, the same setter rejects it."

"Also notice what the setter does at the end: `self._priority = value`. Inside the setter, we store the value in the backing attribute. If we wrote `self.priority = value` inside the setter, the setter would call itself again, and again, and again, until Python raises a recursion error. That is one of today's main pitfalls."

**Instructor emphasis**

"The property is not about hiding data for the sake of hiding data. It is about making one safe doorway into a piece of state. When every assignment goes through the same doorway, every assignment gets the same validation."

"Now let's talk about exceptions. Suppose a service function searches a list of tasks by title. If the task is missing, we have choices. We could return `None`. We could return `False`. We could print a message inside the service. Or we could raise `NotFoundError`."

Write:

```text
Returning None/False:
- Caller might forget to check
- Failure can travel silently
- Error meaning may be ambiguous

Raising a custom exception:
- Failure is explicit
- Error type communicates meaning
- Caller can catch the exact problem it knows how to handle
```

"The service should not print the user-facing message, because we are still keeping our boundaries clean. The service should raise the domain error. The caller catches that specific error and decides how to present it. Today, our caller will just print a friendly message. Later, that caller could be a menu, a GUI, an API response, or a test assertion."

"One more point: do not catch `Exception` broadly around everything. If you catch every exception, you can accidentally hide real programming mistakes. For example, a misspelled variable name raises `NameError`. A broken method call may raise `AttributeError`. If you catch all of those and print 'Something went wrong,' you have made debugging harder. Catch the specific errors you expect and know how to handle: `ValidationError` and `NotFoundError` today."

**Transition**

"Let's build the small version. Watch for three things: the backing attribute, the model raising `ValidationError`, and the service raising `NotFoundError`."

---

## Live Demo: Validated Tracker Model and Service Exception (10 minutes)

The live demo is deterministic and self-contained. Use prepared starter code for the full file if needed, then live-code the property setter, service exception, and caller handling so learners can predict the output without losing lab time. The domain is a task tracker, building directly from Hour 2's model and service boundary ideas.

**Instructor setup**

"Create a file named `day1_hour3_validation_demo.py`. We are not building a full application. We are building the domain core and a tiny caller script that proves the behavior."

### Step 1: Define domain exceptions

**Instructor talk track**

"First, we define the exception types. These are small classes, but they matter because they let the rest of the program distinguish expected domain failures from unexpected programming bugs."

```python
class ValidationError(Exception):
    """Raised when tracker data violates a domain rule."""


class NotFoundError(Exception):
    """Raised when a requested tracker item does not exist."""
```

"A custom exception can be as small as a class that inherits from `Exception`. The class name carries meaning. Later, in the optional extension, we can add an attribute for structured error messages. For now, the message passed when raising the exception is enough."

### Step 2: Create a model with validated properties

**Instructor talk track**

"Now we create a `Task` model. It has a title, a priority, and a completed flag. We will validate title and priority with properties. The title must not be empty after trimming whitespace. Priority must be an integer from 1 to 5."

```python
class Task:
    """A task in a small tracker application."""

    def __init__(self, title: str, priority: int = 3) -> None:
        self.title = title
        self.priority = priority
        self.completed = False

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValidationError("Task title must be text.")
        normalized = value.strip()
        if not normalized:
            raise ValidationError("Task title cannot be empty.")
        self._title = normalized

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int) -> None:
        if type(value) is not int:
            raise ValidationError("Task priority must be an integer.")
        if value < 1 or value > 5:
            raise ValidationError("Task priority must be between 1 and 5.")
        self._priority = value

    def mark_complete(self) -> None:
        self.completed = True

    def summary(self) -> str:
        status = "complete" if self.completed else "open"
        return f"{self.title} | priority={self.priority} | {status}"
```

Pause and point to these lines:

- `self.title = title`
- `self.priority = priority`
- `self._title = normalized`
- `self._priority = value`

**Instructor explanation**

"The initializer assigns through the public properties. That means the object cannot be created in an invalid state. The setters store in the backing attributes. That means the setters do not call themselves recursively."

"The title setter also shows a small normalization step: it strips whitespace. If someone gives us `'  Write report  '`, the stored title becomes `'Write report'`. If someone gives us only spaces, stripping produces an empty string, and we raise `ValidationError`."

"This is a good place to say something about validation consistency. If the constructor strips title whitespace but later assignment does not, the rule is inconsistent. Properties help because creation and later assignment share the same rule."

### Step 3: Add a service function that raises `NotFoundError`

**Instructor talk track**

"Next we need one service function. In Hour 2, we separated services from the model. The model knows how to become complete. The service coordinates finding the right task and asking it to become complete."

```python
def complete_task_by_title(tasks: list[Task], title: str) -> Task:
    """Find a task by title and mark it complete."""
    normalized_title = title.strip()
    for task in tasks:
        if task.title.casefold() == normalized_title.casefold():
            task.mark_complete()
            return task
    raise NotFoundError(f"No task found with title: {title!r}")
```

"Notice that the service raises `NotFoundError` when the requested task is missing. It does not print. It does not return `False`. It does not return `None`. It raises a domain-specific exception. That gives the caller a clear, catchable signal."

"Also notice that invalid task data is still handled by the model. This service function does not need to re-check whether a task priority is valid, because a real `Task` object already protects that invariant. Services should not duplicate every model rule. They should rely on model validation where the model owns the rule."

### Step 4: Add caller-level handling with specific exceptions

**Instructor talk track**

"Finally, we write a tiny caller script. Think of this as the future command-line menu or UI boundary. This is where we catch expected domain errors and print user-friendly messages."

```python
def main() -> None:
    tasks = [
        Task("Write project outline", priority=2),
        Task("Review pull request", priority=4),
    ]

    print("Initial tasks:")
    for task in tasks:
        print(f"- {task.summary()}")

    print("\nCompleting one existing task:")
    try:
        completed_task = complete_task_by_title(tasks, "review pull request")
    except NotFoundError as error:
        print(f"Could not complete task: {error}")
    else:
        print(f"Completed: {completed_task.summary()}")

    print("\nTrying invalid model data:")
    try:
        Task("   ", priority=2)
    except ValidationError as error:
        print(f"Could not create task: {error}")

    print("\nTrying missing task:")
    try:
        complete_task_by_title(tasks, "Submit invoice")
    except NotFoundError as error:
        print(f"Could not complete task: {error}")

    print("\nFinal tasks:")
    for task in tasks:
        print(f"- {task.summary()}")


if __name__ == "__main__":
    main()
```

**Expected output**

Show or run the file. The output should be deterministic:

```text
Initial tasks:
- Write project outline | priority=2 | open
- Review pull request | priority=4 | open

Completing one existing task:
Completed: Review pull request | priority=4 | complete

Trying invalid model data:
Could not create task: Task title cannot be empty.

Trying missing task:
Could not complete task: No task found with title: 'Submit invoice'

Final tasks:
- Write project outline | priority=2 | open
- Review pull request | priority=4 | complete
```

**Instructor discussion**

"Let's identify the boundary decisions. The `Task` model raises `ValidationError` when its own data is invalid. The `complete_task_by_title` service raises `NotFoundError` when it cannot complete the requested use case. The caller catches those specific exceptions and prints messages for a human."

"This is the pattern you are about to practice. It is small, but it scales. In a larger program, the model might be in `models.py`, the service might be in `services.py`, and the caller might be a command-line menu, a web route, or a test. The same responsibilities apply."

**Explicit anti-pattern callout**

"Here is what we are not doing today."

```python
# Anti-pattern for today's lab: too broad.
try:
    complete_task_by_title(tasks, "Submit invoice")
except Exception:
    print("Something went wrong.")
```

"This catches too much. It would catch our expected `NotFoundError`, but it would also catch unrelated bugs. If I misspelled a variable name or called a method that does not exist, this block would hide the real problem behind a vague message. In advanced code, broad exception handling is not a default habit. Catch the errors you can actually handle."

---

## Guided Lab: Validation and Exceptions (25 minutes)

The lab is required practice, not an optional extension. Learners may continue the model they designed in Hour 2 or use the task tracker model from the demo. The minimum required scope is one validated property, two custom exception classes, one service function that raises a domain exception, and caller code that handles expected errors with user-friendly messages.

### Lab prompt for students

"Now you will bulletproof one part of your tracker model. Choose a model from Hour 2 or create a small `Task`, `Contact`, `InventoryItem`, `Expense`, `Workout`, or `Ticket` model. Add a rule that must always be true. Enforce that rule with a property. Then define custom exceptions and update one service function so domain errors are explicit."

Display these requirements:

```text
Required lab work:
1. Add at least one validated @property to a model.
2. Use a backing attribute such as _title, _amount, or _priority.
3. Define ValidationError and NotFoundError.
4. Raise ValidationError when model data violates a rule.
5. Update one service function to raise NotFoundError for a missing item.
6. Catch specific custom exceptions in caller code.
7. Print user-friendly messages only at the caller/UI boundary.
```

### Suggested student starting point

If learners need a scaffold, offer this reduced version. Tell them to adapt the names and rules to their own domain.

```python
class ValidationError(Exception):
    """Raised when domain data violates a rule."""


class NotFoundError(Exception):
    """Raised when a requested item cannot be found."""


class TrackerItem:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValidationError("Name must be text.")
        normalized = value.strip()
        if not normalized:
            raise ValidationError("Name cannot be empty.")
        self._name = normalized

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if type(value) is not int:
            raise ValidationError("Score must be an integer.")
        if value < 0:
            raise ValidationError("Score cannot be negative.")
        self._score = value
```

Then add a service function:

```python
def find_item_by_name(items: list[TrackerItem], name: str) -> TrackerItem:
    normalized_name = name.strip()
    for item in items:
        if item.name.casefold() == normalized_name.casefold():
            return item
    raise NotFoundError(f"No item found with name: {name!r}")
```

And caller handling:

```python
def main() -> None:
    items = [TrackerItem("Daily reading", 10)]

    try:
        TrackerItem("   ", 5)
    except ValidationError as error:
        print(f"Cannot create item: {error}")

    try:
        found_item = find_item_by_name(items, "daily reading")
    except NotFoundError as error:
        print(f"Cannot find item: {error}")
    else:
        print(f"Found: {found_item.name}")

    try:
        find_item_by_name(items, "Weekly planning")
    except NotFoundError as error:
        print(f"Cannot find item: {error}")


if __name__ == "__main__":
    main()
```

### Instructor circulation plan

Use the first 5 minutes of lab time to check that everyone has chosen a model and one invariant.

Ask each learner or pair:

- "What object are you protecting?"
- "What rule must always be true?"
- "Which property setter enforces that rule?"
- "What exception is raised when the rule is violated?"

Use the next 10 minutes to inspect property implementations.

Look for:

- A getter decorated with `@property`.
- A setter decorated with `@property_name.setter`.
- The initializer assigning through the property, such as `self.amount = amount`.
- The setter storing in a backing attribute, such as `self._amount = value`.
- A clear `ValidationError` message when invalid input is rejected.

Use the next 10 minutes to inspect service and caller boundaries.

Look for:

- A service function that searches, updates, or retrieves a domain object.
- `raise NotFoundError(...)` when the service cannot find the requested item.
- No `print()` inside the model or service for expected domain errors.
- Caller code that catches `ValidationError` and `NotFoundError` specifically.

Use the final 5 minutes to run files and ask the quick check. If many learners are still debugging, keep the quick check verbal while they continue working.

### Lab validation examples

Encourage learners to test both successful and failing paths. Give them a checklist like this:

```text
Successful path:
- Create a valid object.
- Update the validated property with a valid value.
- Use the service function to find or update an existing item.

Validation failure:
- Try an empty name, negative amount, out-of-range priority, or other invalid value.
- Confirm ValidationError is raised.
- Confirm the caller prints a friendly message.

Missing item failure:
- Search for an item that does not exist.
- Confirm NotFoundError is raised.
- Confirm the caller prints a friendly message.
```

**Instructor talk track while circulating**

"If your invalid input does not raise an exception, the model is not protecting itself yet. Go back to the property setter and make sure all assignments go through that setter."

"If your program prints an error from inside the model, move that message to the caller. The model should report the problem by raising an exception. The caller decides what to say to a person."

"If your service returns `None` for a required item, decide whether that creates ambiguity. For today's lab, the runbook requires a custom exception for missing items, so use `NotFoundError`."

"If your `except` block says `except Exception`, narrow it. Catch `ValidationError` or `NotFoundError`. If there are two expected failures, use two `except` blocks. That helps future readers know exactly what the caller is prepared to handle."

---

## Troubleshooting Guide

Use these explanations when learners get stuck. Keep the tone calm and evidence-based: read the traceback, identify the line, and connect the error to the design rule.

### Problem: RecursionError in a property setter

Likely cause:

```python
@priority.setter
def priority(self, value: int) -> None:
    self.priority = value
```

Explanation:

"Inside the `priority` setter, assigning to `self.priority` calls the `priority` setter again. That repeats until Python stops with `RecursionError`. Store the accepted value in the backing attribute instead."

Correct pattern:

```python
@priority.setter
def priority(self, value: int) -> None:
    if value < 1:
        raise ValidationError("Priority must be at least 1.")
    self._priority = value
```

### Problem: AttributeError for missing backing attribute

Likely cause:

```python
class Task:
    @property
    def priority(self) -> int:
        return self._priority
```

But `self.priority = priority` was never called during initialization, or the setter did not store `_priority`.

Explanation:

"The getter returns the backing attribute. That backing attribute only exists after the setter stores it. Make sure the initializer assigns through the property and the setter stores the accepted value."

### Problem: Validation only works during object creation

Likely cause:

```python
def __init__(self, priority: int) -> None:
    if priority < 1:
        raise ValidationError("Priority must be at least 1.")
    self.priority = priority
```

But there is no property setter.

Explanation:

"This validates the constructor argument, but it does not protect later assignment. If someone writes `task.priority = -10` after creation, the object can become invalid. A property setter protects both creation and later assignment when `__init__` assigns through the property."

### Problem: Service prints instead of raising

Likely cause:

```python
def complete_task_by_title(tasks: list[Task], title: str) -> None:
    for task in tasks:
        if task.title == title:
            task.mark_complete()
            return
    print("Task not found")
```

Explanation:

"Printing inside the service ties the service to one presentation style. Raise `NotFoundError` instead. The caller can print today, return an API response later, or assert the exception in a test."

Correct pattern:

```python
def complete_task_by_title(tasks: list[Task], title: str) -> Task:
    for task in tasks:
        if task.title.casefold() == title.strip().casefold():
            task.mark_complete()
            return task
    raise NotFoundError(f"No task found with title: {title!r}")
```

### Problem: Broad exception handling hides the real cause

Anti-pattern:

```python
try:
    task = Task("Report", priority="high")
except Exception:
    print("Invalid task")
```

Explanation:

"This catches `ValidationError`, but it also catches unrelated bugs. If the constructor had a typo inside it, the caller would still print `Invalid task`, and debugging would be harder. Catch the exception you expect."

Better:

```python
try:
    task = Task("Report", priority="high")
except ValidationError as error:
    print(f"Invalid task: {error}")
```

---

## Completion Criteria

By the end of the lab, each learner should be able to show the following working evidence:

1. A model class with at least one validated `@property`.
2. A backing attribute used by the property setter.
3. At least one explicit invariant, such as non-empty name, positive amount, valid priority range, or allowed status.
4. A `ValidationError` class and a `NotFoundError` class.
5. Invalid model input triggering a clear `ValidationError`.
6. One service function raising `NotFoundError` when a requested item is missing.
7. Caller-level `try`/`except` code catching specific custom exceptions.
8. User-friendly messages printed only by caller or UI-style code, not inside the model or service.

If a learner has all eight items, they have met the Hour 3 core objective.

---

## Common Pitfalls to Watch For

### Pitfall 1: Treating properties as decoration instead of control

Some learners will add `@property` but still assign directly to the backing attribute from outside the class. Redirect them:

"If outside code writes `task._priority = -5`, it bypasses the validation doorway. In normal application code, use `task.priority = value`. The leading underscore tells us the attribute is internal."

### Pitfall 2: Catching `Exception` broadly

Reinforce this repeatedly:

"Catching `Exception` broadly can hide the cause. It is like covering every warning light on a dashboard with one sticker that says 'car problem.' For today's lab, catch `ValidationError` and `NotFoundError` specifically."

### Pitfall 3: Validation rules that are too strict

Examples:

- Rejecting all lowercase titles even though lowercase titles are meaningful.
- Requiring a description to be 100 characters long when the tracker only needs a brief note.
- Rejecting names with hyphens or apostrophes without a domain reason.

Instructor phrasing:

"A validation rule should protect a real domain requirement, not personal preference. If the rule makes valid real-world data impossible, it is too strict."

### Pitfall 4: Validation rules that are inconsistent

Examples:

- Constructor strips whitespace, but later assignment does not.
- One service accepts case-insensitive names, while another requires exact case.
- A priority of 0 is allowed in one place and rejected in another.

Instructor phrasing:

"Inconsistent validation is dangerous because users and developers cannot predict what the program accepts. Put the rule in one owner whenever possible. For object state, that owner is usually the model property."

### Pitfall 5: Returning `None` or `False` for required domain failures

For optional lookups, returning `None` can be a deliberate design. But today's runbook objective is explicit domain exceptions.

Instructor phrasing:

"If the use case requires an item to exist, a missing item is not just a negative answer. It is a failed domain operation. Raise `NotFoundError` so the caller must handle it."

### Pitfall 6: Printing from the model or service

Learners may be used to printing wherever the problem occurs. Connect back to Hour 2 boundaries:

"The model and service should be usable from a terminal app, a web app, or a test. Printing inside them forces one kind of user interface. Raise an exception and let the caller decide how to communicate."

---

## Optional Extensions for Fast Finishers

These extensions stay inside the Advanced scope. They should not replace the required lab criteria.

### Extension 1: Add an error message attribute to `ValidationError`

Fast finishers can make the exception store a clear message attribute.

```python
class ValidationError(Exception):
    """Raised when tracker data violates a domain rule."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
```

Caller code still works:

```python
try:
    Task("", priority=2)
except ValidationError as error:
    print(f"Validation failed: {error.message}")
```

Instructor note:

"This is useful when caller code wants structured access to the message. In larger systems, you might store a field name, an error code, or a dictionary of field errors. Keep it simple today."

### Extension 2: Add a helper for normalization

Fast finishers can extract normalization into a helper function or method.

```python
def normalize_title(value: str) -> str:
    if not isinstance(value, str):
        raise ValidationError("Task title must be text.")
    return value.strip()
```

Then use it in the setter:

```python
@title.setter
def title(self, value: str) -> None:
    normalized = normalize_title(value)
    if not normalized:
        raise ValidationError("Task title cannot be empty.")
    self._title = normalized
```

Instructor note:

"Normalization means making input consistent before validation or storage. Common examples are trimming whitespace, normalizing case for comparisons, or converting repeated internal spaces to a single space. Do not over-normalize in a way that changes meaningful user data."

### Extension 3: Add a second invariant

Fast finishers can add a second validated property, such as status:

```python
@property
def status(self) -> str:
    return self._status

@status.setter
def status(self, value: str) -> None:
    allowed_statuses = {"open", "blocked", "complete"}
    normalized = value.strip().casefold()
    if normalized not in allowed_statuses:
        raise ValidationError("Status must be open, blocked, or complete.")
    self._status = normalized
```

Instructor note:

"This is useful practice, but remind learners not to add ten rules before the first rule works. Advanced design grows in small tested steps."

---

## Quick Checks and Exit Ticket (5 minutes)

Use these during the final minutes or while circulating during the lab.

### Quick check 1

Question:

"Why do we assign `self.priority = priority` in `__init__` instead of assigning directly to `self._priority`?"

Expected answer:

"Assigning through `self.priority` calls the property setter, so object creation uses the same validation as later assignment."

### Quick check 2

Question:

"What is an invariant?"

Expected answer:

"An invariant is a rule that must always be true for an object to be valid."

### Quick check 3

Question:

"Why is catching `ValidationError` or `NotFoundError` specifically better than catching everything with `except Exception`?"

Expected answer:

"Specific catches handle the domain errors we expect without hiding unrelated programming bugs. Broad catches can make debugging harder by covering up the real cause."

### Quick check 4

Question:

"Where should the user-friendly message be printed in today's design: inside the model, inside the service, or in caller/UI code?"

Expected answer:

"In caller or UI code. The model and service raise domain exceptions; the caller decides what to display."

### Exit ticket prompt

"Write one sentence naming an invariant in your model and one sentence naming the exception raised when that invariant is violated."

Examples:

```text
Invariant: A task priority must be an integer from 1 to 5.
Exception: The Task priority setter raises ValidationError when priority is invalid.
```

---

## Wrap-Up

**Instructor talk track**

"Today we made our tracker models more trustworthy. In Hour 2, we asked what each object knows and does. In Hour 3, we made sure an object cannot quietly hold data that violates its own rules."

"The main pattern is simple but powerful. A property gives controlled access. A backing attribute stores the accepted value. An invariant names the rule that must remain true. A custom exception communicates a domain failure clearly. A caller catches the specific exception and chooses a user-friendly message."

"This design keeps responsibilities separated. The model protects itself. The service coordinates use cases and reports domain failures. The caller or UI communicates with people. That separation is part of the move from PCAP-level syntax toward PCPP1-level design judgment."

"In the next hour, we will continue shaping the tracker design by looking at composition and inheritance decisions. The validation work from this hour will still matter. Once objects protect their own state, we can combine them with more confidence."

**Final instructor reminder**

"Before you leave this hour, make sure your file runs in both success and failure cases. A validation rule is not complete until you have seen it accept good data and reject bad data with a clear, specific exception."
