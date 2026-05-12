# Day 2, Hour 1: Pattern: Factory (Practical Creation + Validation)

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 2, Hour 1 of 48, also Hour 5 in the Advanced runbook sequence
- **Focus**: Using a factory to centralize object creation, normalization, required-field validation, optional defaults, and value validation.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 2, Hour 5.
- **Prerequisites**: Learners should be able to define classes, instantiate objects, use dictionaries, read simple tracebacks, write `try`/`except` blocks, and understand the Day 1 custom exception and validation concepts.
- **Advanced trajectory**: This hour moves learners from PCAP-level class construction toward PCPP1-style design discipline. The goal is not merely to write another `__init__` method. The goal is to decide where object creation rules belong so that valid objects are produced consistently across an application.
- **Instructor goal**: By the end of this hour, every learner has implemented a simple factory function or class method that creates a tracker-style model object from a dictionary, returns a fully valid object, or raises `ValidationError` with a clear message.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Day 1 Hour 4 | 5 min | Connect composition/polymorphism design judgment to creation design judgment |
| Outcomes, setup, and vocabulary | 5 min | Define factory, raw input, normalized input, required field, optional default, and caller boundary |
| Concept briefing: why factories | 10 min | Explain consistent creation, fewer duplicated rules, clean constructors, and fully valid objects |
| Live demo: `RecordFactory.from_dict()` | 10 min | Build and run a self-contained factory for hard-coded JSON-like dictionaries |
| Guided lab: tracker factory implementation | 25 min | Learners implement required-field checks, optional defaults, validation, and display of loaded objects |
| Quick checks, completion criteria, and wrap-up | 5 min | Verify understanding and preview the next design pattern hour |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If the room needs more support, shorten the vocabulary section or the amount of instructor narration during the concept briefing, but do not make the required factory behavior optional. The runbook objective is that the factory creates valid objects or raises `ValidationError`.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain why a factory is useful when raw data comes from JSON, dictionaries, user input, files, APIs, or forms.
2. Implement a simple factory class or factory function that creates a model object from a dictionary.
3. Keep the model constructor simple while the factory handles raw input parsing and validation.
4. Centralize required-field checks so missing required fields raise `ValidationError` instead of becoming silent `None` values.
5. Apply defaults only to optional fields, not required fields.
6. Normalize raw values such as whitespace, capitalization, and status labels before object creation.
7. Validate allowed values such as status or priority before returning an object.
8. Return fully valid objects from the factory or raise `ValidationError` before an invalid object escapes.
9. Load two sample records from hard-coded dictionaries and print or display the resulting objects.
10. Explain the main benefit of centralizing creation logic: consistent creation rules and fewer duplicated validation branches throughout the program.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 2, Hour 5 visible. The required scope is Factory Pattern, practical creation plus validation, `RecordFactory.from_dict()` for JSON or dictionary input, missing-field errors, a lab that loads two hard-coded records, completion criteria, pitfalls, optional `from_user_input()`, and a quick check about centralized creation logic.
- Open the Day 1 Hour 4 expanded lecture if you want the teaching style nearby. Use it as a model for pacing and structure, not as a source of content. Today's topic is creation logic, not composition versus inheritance.
- Prepare a clean file for the live demo, such as `day2_hour1_factory_demo.py`, or be ready to create a notebook cell. The code in this script is self-contained and deterministic.
- Confirm the terminal command for the room. Use `python day2_hour1_factory_demo.py` if `python` works. If your environment uses `python3`, consistently show `python3 day2_hour1_factory_demo.py`.
- Prepare the following vocabulary on the board or in a shared note:

```text
Factory: code whose job is to create objects using consistent rules.
Raw input: data before our program trusts it.
Normalization: converting input into a consistent shape.
Required field: data we must have; no silent default.
Optional field: data that may safely receive a default.
Caller boundary: the place where we catch and report validation errors.
```

- Decide whether learners will work in their existing tracker project or in a new practice file. If their projects vary widely, ask them to create a simple `TaskRecord` or `TrackerRecord` model for this hour so the lab stays focused.
- Be ready to correct two common mistakes early. First, learners may put all parsing and validation into `__init__`, making the constructor noisy and hard to reuse. Second, learners may default a missing required field to an empty string, which hides a data problem instead of reporting it.

Suggested board note before the session starts:

```text
Day 2 Hour 1 goals:
1. Keep the model constructor simple.
2. Put raw dict parsing in a factory.
3. Required fields: validate, do not silently default.
4. Optional fields: default intentionally.
5. Factory returns a valid object or raises ValidationError.
```

---

## Opening Bridge from Day 1 Hour 4 (5 minutes)

**Instructor talk track**

"Welcome back. At the end of Day 1, we practiced an important design habit: choosing the right relationship between objects. In Hour 4, we compared inheritance, composition, and polymorphism. The big lesson was that advanced Python is not about using the fanciest object-oriented feature every time. It is about putting responsibility in the right place."

"Today we continue that same design theme, but we move from object relationships to object creation. Last time, we asked, 'Should this object inherit from another object, hold another object, or simply provide the method the caller expects?' Today we ask a different question: 'When raw data comes into our program, where should the rules for building a valid object live?'"

"This matters because most real programs do not create objects from perfect hand-written values. A tracker application might receive a record from JSON, a form, a file, a command-line prompt, a database row, or an API response. That raw data may have extra whitespace. It may use uppercase where our program expects lowercase. It may omit required fields. It may use a status value our application does not recognize."

"A beginner-friendly approach is often to put all of that logic directly into `__init__`. That works for a small example, but it can become a problem quickly. The constructor becomes a mix of storage, parsing, validation, defaulting, and error reporting. Other parts of the app may start duplicating small pieces of the same creation rules. One function strips whitespace. Another function forgets to strip whitespace. One route accepts `Done`, another route only accepts `done`. Bugs appear because object creation is inconsistent."

"The Factory Pattern gives us a practical solution. A factory is code whose job is to create objects. In Python, that might be a class method like `RecordFactory.from_dict()`, a class method on the model itself like `Record.from_dict()`, or a standalone function like `create_record_from_dict()`. The form matters less than the responsibility. The factory receives raw input, applies the rules, and either returns a fully valid object or raises a clear exception."

Pause and ask:

"Think about your tracker or record project. If three different parts of the application need to create a task from dictionary-like data, what could go wrong if all three parts write their own parsing rules?"

Take two or three answers. Listen for duplicated checks, inconsistent defaults, missing validation, and unclear errors. Then connect:

"Exactly. Today's pattern is about reducing that risk. We are going to centralize creation logic so there is one reliable path from raw data to valid object."

**Transition**

"Let's name the vocabulary, then we will build a small `RecordFactory.from_dict()` live. The demo will deliberately use hard-coded dictionaries so we can focus on the design pattern rather than file I/O or API details."

---

## Outcomes, Setup, and Vocabulary (5 minutes)

Use this section to make the pattern concrete. Keep the language practical and connect every term to the live demo.

**Instructor talk track**

"By the end of this hour, you should be able to implement a simple factory and explain why it belongs in the design. We are not trying to memorize a design-pattern diagram. We are learning a professional habit: raw data should pass through one trusted creation path before the rest of the program uses it."

"Here are the terms we will use."

"First, **factory**. A factory is code whose responsibility is to create an object. A real-world factory takes raw materials and produces finished goods. A software factory takes raw input and produces an object our program can trust. In Python, a factory can be very small. It does not have to be a large framework or a complex hierarchy."

"Second, **raw input**. Raw input is data before our program trusts it. A dictionary from JSON is raw input. A dictionary from a form is raw input. Strings typed by a user are raw input. Even if the data came from our own test case, the factory should treat it as something that must be checked."

"Third, **normalization**. Normalization means converting input into a consistent shape. For example, the raw status might be `' DONE '`, but our program may store it as `'done'`. The raw title might have extra spaces, so we strip it. The raw priority might be `'High'`, so we store `'high'`. Normalization does not mean accepting anything. It means converting reasonable representations into our program's standard representation."

"Fourth, **required field**. A required field is data we must have to create a meaningful object. In a tracker record, a title is required. An owner might be required. If a required field is missing, the factory should raise `ValidationError`. It should not quietly invent a required title like `'Untitled'` unless the product rule explicitly says that is allowed. For this hour, required fields must not receive silent defaults."

"Fifth, **optional field**. An optional field is data that can safely use a default. Status is a good example. If the incoming dictionary does not include status, we may decide that a new record starts as `'todo'`. Estimate minutes might default to `0`. These defaults should be intentional and visible in the factory."

"Sixth, **caller boundary**. This is the place where code calls the factory and decides what to do if validation fails. The factory raises `ValidationError`; the caller catches it and reports a clear message. That separation is important. The factory should not usually print the error itself. It should raise the error. The caller decides whether to print, log, show a UI message, or reject an API request."

Point learners to the working pattern:

```text
raw dict -> factory validates and normalizes -> valid model object
raw dict -> factory finds problem -> raises ValidationError
```

"That arrow is the core of today's hour."

---

## Concept Briefing: Why Factories (10 minutes)

**Instructor talk track**

"Let's start with the problem factories solve. Imagine we have a `TaskRecord` class. At minimum, a record might have a title, an owner, a status, a priority, and an estimate in minutes. The simplest constructor might look like this: `TaskRecord(title, owner, status, priority, estimate_minutes)`. That constructor is easy to understand. It takes values and stores values."

"But real input usually does not arrive as five perfect arguments. It arrives as a dictionary like this:"

```python
{
    "title": "  write tests  ",
    "owner": "maria",
    "status": "IN_PROGRESS",
    "priority": "High",
}
```

"Notice the small problems. The title has extra whitespace. The status uses uppercase. The priority is capitalized. The estimate is missing. None of these is unusual. This is what raw input often looks like."

"One option is to make the constructor handle all of it. The constructor could check if keys exist, strip strings, default missing values, validate status, convert estimate to an integer, and then store the final values. That seems convenient at first. But it has a cost: the constructor becomes responsible for too many things."

"A clean constructor is usually about receiving already meaningful values and assigning them to the object. It may still protect core invariants, especially in production code, but we do not want it to become a raw-data parser for every possible source. Dictionary input, command-line input, web form input, database input, and user prompt input may all need slightly different parsing. If all of that goes into `__init__`, the constructor turns into a traffic jam."

"A factory gives us a better place for that traffic. The factory can say, 'I know how to create a `TaskRecord` from a dictionary.' Another factory method could say, 'I know how to create a `TaskRecord` from user input.' The model constructor remains simple. The creation rules are centralized."

Write or display:

```text
Constructor:
    Store clean values on the object.

Factory:
    Accept raw input.
    Check required fields.
    Normalize values.
    Apply optional defaults.
    Validate allowed values.
    Return a fully valid object or raise ValidationError.
```

"This split is a design decision. It is also a testing decision. A factory is easy to test because you can give it dictionaries and check whether it returns objects or raises errors. You can test missing title, missing owner, unknown status, invalid priority, and non-numeric estimate. The tests focus on creation rules without needing the rest of the app."

"Now let's talk about the phrase **fully valid object**. This is one of the most important ideas today. A factory should not return an object that is half-created, missing required data, or waiting for someone else to fix it later. If the factory returns an object, the rest of the program should be able to use it with confidence. If the input cannot produce a valid object, the factory should stop and raise `ValidationError`."

"That does not mean factories prevent all possible bugs. It means they establish a clear boundary. Before the factory, data is untrusted. After the factory returns, the object has passed the creation rules."

Ask:

"Which fields in a tracker record should be required? Which fields could reasonably have defaults?"

Guide toward:

- Required: `title`, `owner`
- Optional defaults: `status='todo'`, `priority='normal'`, `estimate_minutes=0`

"The exact product rule can vary. In one app, owner might be optional. In another, it is required. For today's lesson, we will require title and owner because we want to practice missing-field errors. The principle is what matters: required fields fail loudly; optional fields default intentionally."

"Factories also reduce duplication. If every feature creates records through `RecordFactory.from_dict()`, then every feature gets the same whitespace handling, same status rules, same missing-field errors, and same defaults. When the business rule changes, we update one place. That is the central benefit of the pattern."

"Finally, factories help us avoid a subtle pitfall: silent defaults that hide mistakes. A default is helpful when the missing value is truly optional. A default is dangerous when it covers up a required missing value. If the input lacks a title and our code silently uses an empty string, the error may not appear until much later, maybe when a report prints blank rows or a search feature behaves strangely. We want failure near the cause. Missing required field? Raise `ValidationError` right there."

**Transition**

"Let's build this now. We will create a simple model, then a `RecordFactory.from_dict()` method that takes a dictionary, validates it, normalizes it, applies optional defaults, and returns a valid object."

---

## Live Demo: `RecordFactory.from_dict()` (10 minutes)

The live demo should be typed or revealed in small chunks. Keep the pace brisk. The goal is a credible 10-minute demo, not a full architecture lecture. Use one file and avoid external dependencies.

### Demo Step 1: Define a local exception and simple model

**Instructor talk track**

"First, I want the exception to be local in this demo so the file is self-contained. Yesterday we talked about custom exceptions for validation. Today we will reuse that idea. Our exception is intentionally small."

"Next, I will define the model. Notice what the constructor does and does not do. It stores clean values. It is not reading a dictionary. It is not deciding defaults. It is not stripping raw strings. That is the factory's job."

```python
class ValidationError(Exception):
    """Raised when raw input cannot produce a valid record."""


class TaskRecord:
    def __init__(
        self,
        title: str,
        owner: str,
        status: str,
        priority: str,
        estimate_minutes: int,
    ) -> None:
        self.title = title
        self.owner = owner
        self.status = status
        self.priority = priority
        self.estimate_minutes = estimate_minutes

    def __str__(self) -> str:
        return (
            f"{self.title} | owner={self.owner} | status={self.status} | "
            f"priority={self.priority} | estimate={self.estimate_minutes}m"
        )
```

Say:

"This constructor is deliberately boring. Boring constructors are often a good sign. They are easy to read, easy to instantiate in tests, and easy to reason about. The important creation rules are coming next."

### Demo Step 2: Add the factory skeleton

**Instructor talk track**

"Now we create `RecordFactory`. A factory does not need instance state here, so we will use a `@classmethod`. You could also use `@staticmethod` or a standalone function. I am using `@classmethod` because it gives us a clean namespace: `RecordFactory.from_dict(data)` reads nicely."

```python
class RecordFactory:
    REQUIRED_FIELDS = ("title", "owner")
    ALLOWED_STATUSES = {"todo", "in_progress", "done"}
    ALLOWED_PRIORITIES = {"low", "normal", "high"}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TaskRecord:
        """Create a fully valid TaskRecord from JSON-like dictionary data."""
        # We will fill this in one rule at a time.
        raise NotImplementedError
```

Ask:

"Before I write the body, what should be the first thing this method checks?"

Guide them to required fields. If someone says status or priority, affirm that those matter but remind them that missing required fields are the first gate.

### Demo Step 3: Required-field checks

**Instructor talk track**

"The first rule is required fields. Title and owner must be present. If either key is missing, the factory raises `ValidationError`. I am also checking for blank strings after stripping, because a string of spaces is not a meaningful title."

```python
class RecordFactory:
    REQUIRED_FIELDS = ("title", "owner")
    ALLOWED_STATUSES = {"todo", "in_progress", "done"}
    ALLOWED_PRIORITIES = {"low", "normal", "high"}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TaskRecord:
        """Create a fully valid TaskRecord from JSON-like dictionary data."""
        for field_name in cls.REQUIRED_FIELDS:
            if field_name not in data:
                raise ValidationError(f"Missing required field: {field_name}")

        raw_title = data["title"]
        raw_owner = data["owner"]

        if not isinstance(raw_title, str):
            raise ValidationError("Field 'title' must be text")
        if not isinstance(raw_owner, str):
            raise ValidationError("Field 'owner' must be text")

        title = raw_title.strip()
        owner = raw_owner.strip().lower()

        if not title:
            raise ValidationError("Field 'title' cannot be blank")
        if not owner:
            raise ValidationError("Field 'owner' cannot be blank")

        # More rules will be added next.
        return TaskRecord(
            title=title,
            owner=owner,
            status="todo",
            priority="normal",
            estimate_minutes=0,
        )
```

Say:

"At this point, the required fields are enforced. Notice that I did not write `data.get('title', 'Untitled')`. That would be a silent default for a required field. Today's rule is clear: required fields must be supplied."

### Demo Step 4: Optional defaults, normalization, and value validation

**Instructor talk track**

"Now we add optional fields. Status, priority, and estimate can have defaults. But after defaulting, we still validate them. A default does not mean anything goes."

```python
class RecordFactory:
    REQUIRED_FIELDS = ("title", "owner")
    ALLOWED_STATUSES = {"todo", "in_progress", "done"}
    ALLOWED_PRIORITIES = {"low", "normal", "high"}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TaskRecord:
        """Create a fully valid TaskRecord from JSON-like dictionary data."""
        for field_name in cls.REQUIRED_FIELDS:
            if field_name not in data:
                raise ValidationError(f"Missing required field: {field_name}")

        raw_title = data["title"]
        raw_owner = data["owner"]

        if not isinstance(raw_title, str):
            raise ValidationError("Field 'title' must be text")
        if not isinstance(raw_owner, str):
            raise ValidationError("Field 'owner' must be text")

        title = raw_title.strip()
        owner = raw_owner.strip().lower()

        if not title:
            raise ValidationError("Field 'title' cannot be blank")
        if not owner:
            raise ValidationError("Field 'owner' cannot be blank")

        status = str(data.get("status", "todo")).strip().lower()
        priority = str(data.get("priority", "normal")).strip().lower()

        if status not in cls.ALLOWED_STATUSES:
            allowed = ", ".join(sorted(cls.ALLOWED_STATUSES))
            raise ValidationError(
                f"Invalid status '{status}'. Expected one of: {allowed}"
            )

        if priority not in cls.ALLOWED_PRIORITIES:
            allowed = ", ".join(sorted(cls.ALLOWED_PRIORITIES))
            raise ValidationError(
                f"Invalid priority '{priority}'. Expected one of: {allowed}"
            )

        try:
            estimate_minutes = int(data.get("estimate_minutes", 0))
        except (TypeError, ValueError) as error:
            raise ValidationError("Field 'estimate_minutes' must be an integer") from error

        if estimate_minutes < 0:
            raise ValidationError("Field 'estimate_minutes' cannot be negative")

        return TaskRecord(
            title=title,
            owner=owner,
            status=status,
            priority=priority,
            estimate_minutes=estimate_minutes,
        )
```

Say:

"Now the factory has the full creation pipeline: required checks, normalization, optional defaults, value validation, and object creation. If it returns a `TaskRecord`, that record is valid according to our rules."

### Demo Step 5: Run valid and invalid hard-coded dictionaries

Now present the complete deterministic script. It should be copy/paste-able and runnable as one file.

```python
class ValidationError(Exception):
    """Raised when raw input cannot produce a valid record."""


class TaskRecord:
    def __init__(
        self,
        title: str,
        owner: str,
        status: str,
        priority: str,
        estimate_minutes: int,
    ) -> None:
        self.title = title
        self.owner = owner
        self.status = status
        self.priority = priority
        self.estimate_minutes = estimate_minutes

    def __str__(self) -> str:
        return (
            f"{self.title} | owner={self.owner} | status={self.status} | "
            f"priority={self.priority} | estimate={self.estimate_minutes}m"
        )

    def to_dict(self) -> dict[str, object]:
        """Convert the custom object to plain data before JSON serialization."""
        return {
            "title": self.title,
            "owner": self.owner,
            "status": self.status,
            "priority": self.priority,
            "estimate_minutes": self.estimate_minutes,
        }


class RecordFactory:
    REQUIRED_FIELDS = ("title", "owner")
    ALLOWED_STATUSES = {"todo", "in_progress", "done"}
    ALLOWED_PRIORITIES = {"low", "normal", "high"}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TaskRecord:
        """Create a fully valid TaskRecord from JSON-like dictionary data."""
        for field_name in cls.REQUIRED_FIELDS:
            if field_name not in data:
                raise ValidationError(f"Missing required field: {field_name}")

        raw_title = data["title"]
        raw_owner = data["owner"]

        if not isinstance(raw_title, str):
            raise ValidationError("Field 'title' must be text")
        if not isinstance(raw_owner, str):
            raise ValidationError("Field 'owner' must be text")

        title = raw_title.strip()
        owner = raw_owner.strip().lower()

        if not title:
            raise ValidationError("Field 'title' cannot be blank")
        if not owner:
            raise ValidationError("Field 'owner' cannot be blank")

        status = str(data.get("status", "todo")).strip().lower()
        priority = str(data.get("priority", "normal")).strip().lower()

        if status not in cls.ALLOWED_STATUSES:
            allowed = ", ".join(sorted(cls.ALLOWED_STATUSES))
            raise ValidationError(
                f"Invalid status '{status}'. Expected one of: {allowed}"
            )

        if priority not in cls.ALLOWED_PRIORITIES:
            allowed = ", ".join(sorted(cls.ALLOWED_PRIORITIES))
            raise ValidationError(
                f"Invalid priority '{priority}'. Expected one of: {allowed}"
            )

        try:
            estimate_minutes = int(data.get("estimate_minutes", 0))
        except (TypeError, ValueError) as error:
            raise ValidationError("Field 'estimate_minutes' must be an integer") from error

        if estimate_minutes < 0:
            raise ValidationError("Field 'estimate_minutes' cannot be negative")

        return TaskRecord(
            title=title,
            owner=owner,
            status=status,
            priority=priority,
            estimate_minutes=estimate_minutes,
        )


def load_records(raw_records: list[dict[str, object]]) -> list[TaskRecord]:
    loaded_records: list[TaskRecord] = []

    for index, raw_record in enumerate(raw_records, start=1):
        try:
            record = RecordFactory.from_dict(raw_record)
        except ValidationError as error:
            print(f"Record {index} rejected: {error}")
        else:
            loaded_records.append(record)
            print(f"Record {index} loaded: {record}")

    return loaded_records


sample_records = [
    {
        "title": "  write factory tests  ",
        "owner": "MARIA",
        "status": "IN_PROGRESS",
        "priority": "High",
        "estimate_minutes": "45",
    },
    {
        "title": "Document validation rules",
        "owner": "jamal",
    },
    {
        "title": "Missing owner should fail",
        "status": "todo",
    },
]

records = load_records(sample_records)

print()
print("Display loaded records:")
for record in records:
    print(f"- {record}")

print()
print("Plain data for serialization:")
for record in records:
    print(record.to_dict())
```

Expected output:

```text
Record 1 loaded: write factory tests | owner=maria | status=in_progress | priority=high | estimate=45m
Record 2 loaded: Document validation rules | owner=jamal | status=todo | priority=normal | estimate=0m
Record 3 rejected: Missing required field: owner

Display loaded records:
- write factory tests | owner=maria | status=in_progress | priority=high | estimate=45m
- Document validation rules | owner=jamal | status=todo | priority=normal | estimate=0m

Plain data for serialization:
{'title': 'write factory tests', 'owner': 'maria', 'status': 'in_progress', 'priority': 'high', 'estimate_minutes': 45}
{'title': 'Document validation rules', 'owner': 'jamal', 'status': 'todo', 'priority': 'normal', 'estimate_minutes': 0}
```

**Instructor emphasis**

"Look carefully at where the error is caught. `RecordFactory.from_dict()` raises `ValidationError`. The caller boundary is `load_records()`, where we decide to print `Record 3 rejected`. That means the factory does not need to know whether the application is a terminal script, a web API, or a GUI. It simply enforces the creation rule."

"Also notice the `to_dict()` method. This connects to one of today's pitfalls. If you later serialize records to JSON, do not assume that a custom object can be serialized directly. Convert custom objects to plain dictionaries first. The factory moves from plain input to custom object. A `to_dict()` method moves from custom object back to plain output."

"This demo uses three dictionaries because it helps us show two successful loaded records and one missing-field failure. In the lab, the minimum requirement is two sample records from hard-coded dictionaries, and your factory must create valid objects or raise `ValidationError`."

---

## Guided Lab: Tracker Factory Implementation (25 minutes)

The lab is the center of this hour. Learners need time to type, make mistakes, read error messages, and repair their code. Keep the prompt focused. Do not expand into file loading, JSON parsing from disk, databases, or web requests unless learners finish the required work.

### Lab Goal

Implement a factory that creates a tracker-style model object from a dictionary. The factory must:

- accept raw dictionary input,
- check required fields,
- normalize string fields,
- apply defaults only to optional fields,
- validate allowed values,
- return a fully valid object, or
- raise `ValidationError` with a clear message.

Loaded objects must be printable or displayable.

### Learner Prompt

**Build a `TrackerRecord` or `TaskRecord` factory.**

Create one Python file for this lab. You may use the names below or adapt them to your tracker project:

- `ValidationError`
- `TrackerRecord`
- `RecordFactory`
- `RecordFactory.from_dict()`

Your model should have at least these fields:

- `title` - required
- `owner` - required
- `status` - optional, default `"todo"`
- `priority` - optional, default `"normal"`

You may add `estimate_minutes`, `category`, `created_by`, or another tracker field if your project already uses one.

### Required Steps

1. Define `ValidationError` locally in the lab file.
2. Define a simple model class such as `TrackerRecord`.
3. Keep the model constructor simple. It should receive clean values and store them.
4. Define `RecordFactory.from_dict(data)`.
5. In the factory, check that required fields are present.
6. Reject blank required fields after stripping whitespace.
7. Normalize strings, such as trimming whitespace and converting status to lowercase.
8. Apply defaults only for optional fields.
9. Validate allowed values, such as status and priority.
10. Create two valid hard-coded dictionaries and load them through the factory.
11. Include one invalid hard-coded dictionary with a missing required field and show the caught `ValidationError`.
12. Print or display the successfully loaded objects.

### Suggested Starter Code

Offer this if learners need a starting point. If the class is moving quickly, ask them to write it from scratch and keep this as a rescue scaffold.

```python
class ValidationError(Exception):
    """Raised when raw input cannot produce a valid tracker record."""


class TrackerRecord:
    def __init__(self, title: str, owner: str, status: str, priority: str) -> None:
        self.title = title
        self.owner = owner
        self.status = status
        self.priority = priority

    def __str__(self) -> str:
        return (
            f"{self.title} | owner={self.owner} | "
            f"status={self.status} | priority={self.priority}"
        )


class RecordFactory:
    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TrackerRecord:
        # Add required-field checks.
        # Add normalization.
        # Add defaults for optional fields only.
        # Add value validation.
        # Return TrackerRecord(...)
        raise NotImplementedError
```

Remind learners:

"Do not leave `NotImplementedError` in the final lab. It is only a marker for where your implementation belongs."

### Instructor Circulation Plan

For the first five minutes, let learners attempt the structure. Watch for whether they understand the separation between constructor and factory. If someone immediately writes `def __init__(self, data):` and starts reading dictionary keys inside the constructor, pause and ask:

"Which part of the code is responsible for raw dictionary parsing in today's pattern?"

Guide them back to:

```python
record = RecordFactory.from_dict(raw_data)
```

For minutes five through fifteen, look for required-field handling. The most important check is not just `data.get("title")`; learners need to distinguish between missing and blank. A strong solution handles both:

```python
if "title" not in data:
    raise ValidationError("Missing required field: title")

raw_title = data["title"]
if not isinstance(raw_title, str):
    raise ValidationError("Field 'title' must be text")

title = raw_title.strip()
if not title:
    raise ValidationError("Field 'title' cannot be blank")
```

If a learner writes:

```python
title = data.get("title", "Untitled")
```

say:

"That is a useful pattern for optional fields, but title is required in this lab. If the source forgot to send a title, we want to know immediately. Silent defaults are one of today's pitfalls."

For minutes fifteen through twenty, check normalization and allowed values. Learners should have something like:

```python
status = str(data.get("status", "todo")).strip().lower()
if status not in {"todo", "in_progress", "done"}:
    raise ValidationError(f"Invalid status: {status}")
```

If learners ask whether they can support `"in progress"` with a space, that is a good extension only after the required version works. The required lab can use exact allowed values after normalization.

For the final five minutes, ensure everyone has hard-coded sample records and a caller boundary that catches errors:

```python
raw_records = [
    {"title": "Fix login bug", "owner": "Ava", "priority": "high"},
    {"title": "Write release notes", "owner": "Noah", "status": "DONE"},
    {"title": "Missing owner example"},
]

for raw_record in raw_records:
    try:
        record = RecordFactory.from_dict(raw_record)
    except ValidationError as error:
        print(f"Rejected record: {error}")
    else:
        print(f"Loaded record: {record}")
```

This satisfies the runbook: two sample records from hard-coded dictionaries are loaded, invalid input raises `ValidationError`, and loaded objects can be printed or displayed.

### Lab Completion Criteria

A lab is complete when:

- `RecordFactory.from_dict()` or an equivalent factory exists.
- The factory creates a model object from a dictionary.
- Required fields are checked before object creation.
- Missing required fields raise `ValidationError`.
- Blank required fields raise `ValidationError`.
- Optional fields use intentional defaults.
- Status, priority, or another meaningful value is validated.
- At least two hard-coded sample dictionaries produce printable/displayable objects.
- At least one invalid hard-coded dictionary is caught at the caller boundary and produces a clear error message.
- The model constructor remains simple and does not become the main raw-dictionary parser.

### If Learners Finish Early

Ask fast finishers to strengthen the required solution before adding features:

1. Add an `estimate_minutes` field with a default of `0`.
2. Convert `estimate_minutes` to an integer in the factory.
3. Reject negative estimates with `ValidationError`.
4. Add a `to_dict()` method to the model so custom objects can be converted back to plain data before JSON serialization.

Then offer the runbook's optional extension:

```python
@classmethod
def from_user_input(
    cls,
    title: str,
    owner: str,
    status: str = "todo",
    priority: str = "normal",
):
    raw_data = {
        "title": title,
        "owner": owner,
        "status": status,
        "priority": priority,
    }
    return cls.from_dict(raw_data)
```

Emphasize:

"The optional `from_user_input()` method should reuse `from_dict()` rather than duplicate all the validation rules. If it copies and pastes the same checks, we have recreated the duplication problem the factory was meant to solve."

---

## Troubleshooting Guide

Use this section while circulating or during a short pause if many learners hit the same issue.

### Problem: `KeyError` appears instead of `ValidationError`

Likely cause: the code reads `data["owner"]` before checking whether `"owner"` exists.

Coach with:

"Read the traceback. Which line accessed the missing key? The factory should check required fields before indexing into the dictionary. We want a domain-specific error message, not a raw `KeyError`."

Repair pattern:

```python
if "owner" not in data:
    raise ValidationError("Missing required field: owner")

raw_owner = data["owner"]
if not isinstance(raw_owner, str):
    raise ValidationError("Field 'owner' must be text")

owner = raw_owner.strip().lower()
```

### Problem: Missing title becomes `"Untitled"`

Likely cause: the learner used `.get("title", "Untitled")` for a required field.

Coach with:

"Defaults are not bad. Silent defaults for required fields are bad. Is title required for a meaningful tracker record? If yes, the factory should raise an error when it is missing."

Repair pattern:

```python
if "title" not in data:
    raise ValidationError("Missing required field: title")
```

### Problem: The constructor is doing all the parsing

Likely cause: the learner wrote `TrackerRecord(data)` and put dictionary logic in `__init__`.

Coach with:

"That can work technically, but it misses today's design goal. The constructor should receive clean values. The factory should turn raw data into clean values."

Repair pattern:

```python
record = TrackerRecord(
    title=title,
    owner=owner,
    status=status,
    priority=priority,
)
```

### Problem: Objects print as memory addresses

Likely cause: the learner did not define `__str__` or `__repr__`.

Coach with:

"The object may be valid, but it is not display-friendly yet. Add a simple `__str__` method so the completion criterion 'loaded objects can be printed/displayed' is easy to verify."

Repair pattern:

```python
def __str__(self) -> str:
    return f"{self.title} ({self.status}) assigned to {self.owner}"
```

### Problem: JSON serialization fails for custom objects

Likely cause: the learner tries to serialize `TrackerRecord` instances directly.

Coach with:

"The factory converts plain data into custom objects. Serialization usually needs the reverse: convert custom objects back into plain data. Add a `to_dict()` method or build a list of dictionaries before serializing."

Repair pattern:

```python
def to_dict(self) -> dict[str, str]:
    return {
        "title": self.title,
        "owner": self.owner,
        "status": self.status,
        "priority": self.priority,
    }
```

### Problem: Invalid status is accepted

Likely cause: the learner normalized the status but forgot to validate it against allowed values.

Coach with:

"Normalization makes values consistent. Validation decides whether the value is allowed. We need both."

Repair pattern:

```python
allowed_statuses = {"todo", "in_progress", "done"}
if status not in allowed_statuses:
    raise ValidationError(f"Invalid status: {status}")
```

---

## Common Pitfalls to Watch For

### Pitfall 1: Treating the factory as unnecessary ceremony

Some learners will say, "Why not just call the class directly?" That is a fair question. Answer it in terms of duplicated rules:

"If every call site already has clean values, direct construction is fine. But when raw dictionaries enter the program from multiple places, we need one trusted path. The factory is not ceremony when it prevents three different versions of the same validation rule."

### Pitfall 2: Moving messy code without improving responsibility

A learner may move all messy creation code into `RecordFactory` but still leave duplicated validation branches elsewhere. Remind them:

"The factory should be the central creation path. If other parts of the program still create records from raw dictionaries manually, the duplication problem remains."

### Pitfall 3: Silent defaults for required fields

This is the major required pitfall from the runbook. Use strong language:

"A silent default for a required field hides a mistake. If owner is required and owner is missing, do not invent an owner. Raise `ValidationError`."

### Pitfall 4: No caller boundary

If a learner lets the program crash without catching `ValidationError`, the factory may still be correct, but the demo is incomplete. The runbook asks learners to show the error on missing fields. They should catch the error where records are loaded and print a clear message.

### Pitfall 5: Serializing custom objects directly

This is the second required pitfall from the runbook. A `TaskRecord` is useful inside Python, but JSON and many storage layers need plain dictionaries, strings, numbers, lists, booleans, and `None`. When moving back out, use a conversion method such as `to_dict()`.

### Pitfall 6: Confusing normalization with validation

Normalization:

```python
status = status.strip().lower()
```

Validation:

```python
if status not in {"todo", "in_progress", "done"}:
    raise ValidationError(...)
```

Both are needed. Normalization without validation may accept nonsense. Validation without normalization may reject reasonable input such as `"DONE"`.

---

## Optional Extensions

Offer these only after the required factory works.

1. **`from_user_input()` factory**

   Add a factory method that accepts separate strings from a prompt or form and normalizes them by reusing `from_dict()`.

   ```python
   @classmethod
   def from_user_input(
       cls,
       title: str,
       owner: str,
       status: str = "todo",
       priority: str = "normal",
    ):
        return cls.from_dict(
           {
               "title": title,
               "owner": owner,
               "status": status,
               "priority": priority,
           }
       )
   ```

   Instructor note: The important design point is reuse. `from_user_input()` should not copy the required-field and allowed-value checks. It should route through the central factory logic.

2. **Input aliases**

   Support human-friendly status input such as `"in progress"` by translating it to `"in_progress"` before validation.

3. **Batch loading result summary**

   Count how many records loaded and how many were rejected, then print a summary.

4. **Plain-data export**

   Add `to_dict()` to the model and build `list[dict[str, object]]` from the loaded objects. This prepares learners for later persistence and serialization work.

---

## Quick Checks, Completion Criteria, and Wrap-Up (5 minutes)

Use this final segment to verify the required concept before moving on.

### Quick Check Questions

Ask:

"What is the main benefit of centralizing creation logic in a factory?"

Expected answer:

"It gives the application one consistent place to check required fields, normalize input, apply optional defaults, validate values, and create valid objects. That reduces duplicated rules and inconsistent object creation."

Ask:

"Should a required field like title receive a silent default?"

Expected answer:

"No. If title is required and missing or blank, the factory should raise `ValidationError`. Defaults are for optional fields."

Ask:

"If the factory returns an object, what should the rest of the program be able to assume?"

Expected answer:

"The object is valid according to the factory's creation rules."

Ask:

"Where should the missing-field error be caught in our demo?"

Expected answer:

"At the caller boundary, such as the loop or function that is loading raw records. The factory raises `ValidationError`; the caller catches and reports it."

### Completion Criteria for the Hour

Before ending, make sure learners can point to:

- a simple model constructor,
- a factory method or function,
- required-field checks,
- optional defaults,
- normalization,
- value validation,
- `ValidationError` being raised for invalid input,
- at least two loaded records from hard-coded dictionaries,
- a caught missing-field error, and
- printed or displayed loaded objects.

### Wrap-Up Talk Track

"Today we learned the Factory Pattern in its most practical Python form. We did not build a complicated framework. We built a reliable creation path. Raw dictionaries came in. The factory checked required fields, normalized strings, applied defaults only where defaults were safe, validated allowed values, and then returned a model object."

"The professional habit is this: do not let raw input leak all over your program. Decide where raw input becomes trusted object state. A factory is one clean way to make that boundary visible."

"This connects directly to the PCPP1 trajectory. At the PCAP level, you can define a class and create an instance. At the PCPP1 level, you think about where responsibilities belong, how to reduce duplication, and how to make invalid states harder to represent. Factories help with all three."

"Next hour, we will continue with another pattern that affects how behavior changes at runtime. Now that we can reliably create valid records, we can start asking how those records should be processed, displayed, filtered, or handled by interchangeable strategies."

End with:

"Exit ticket: in one sentence, explain why a factory is better than copying dictionary parsing code into three different parts of an application."
