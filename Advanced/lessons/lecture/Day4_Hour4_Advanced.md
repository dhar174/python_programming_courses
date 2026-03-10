# Day 4, Hour 4: Checkpoint 2 – Persistence-Ready Core + JSON Save/Load
**Python Programming Advanced – Session 4**

---

## Timing Overview
**Total Time:** 60 minutes  
- Checkpoint framing and grading focus: 5 minutes
- Persistence-ready architecture and package layout under `src/`: 12 minutes
- Safe JSON save/load, logging, and exception strategy: 13 minutes
- Live Demo (save -> restart -> load): 10 minutes
- Hands-On Checkpoint Build: 15 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Organize an application package under `src/` so the core domain and persistence logic are clearly separated
2. Save application state to JSON using a safe-save pattern rather than a fragile direct overwrite
3. Load JSON data back into application objects and restore useful state across runs
4. Handle missing files, invalid JSON, and validation failures without crashing the entire application
5. Use custom exceptions to communicate domain and persistence problems clearly
6. Configure logging to a file so important events and failures are captured for debugging
7. Demonstrate persistence with a simple save -> restart -> load workflow
8. Explain why JSON persistence now prepares the codebase for future database integration later

---

## Section 1: Checkpoint Framing and Grading Focus (5 minutes)

### What This Checkpoint Proves

**[Instructor speaks:]**

Checkpoint 2 is where you prove that your project has a real core and that the core can survive beyond a single run. This is a deceptively important transition.

Before persistence, a project can look functional while still being fragile. It may perform a few actions in memory, print nice output, and then lose everything the moment the process ends. That is not yet a reliable application foundation.

This checkpoint asks you to cross an architectural threshold:

- the code is organized as a package under `src/`
- state can be serialized to JSON
- state can be loaded back in
- save/load failures are handled intentionally
- logging records meaningful events
- custom exceptions still communicate domain-specific problems

### Grading Lens

**[Instructor speaks:]**

The runbook is very clear about the grading focus: correctness, structure, error handling, and logging. That means a small, clean, reliable solution should score better than a flashy, sprawling, fragile one.

State this explicitly to students: if they are tempted to add more features right now, the safest move is usually to make the existing core more trustworthy.

**[Ask students:]** If your program can create great data but loses it after restart, what milestone is still incomplete?

[Pause. Students should say persistence.]

Exactly.

---

## Section 2: Persistence-Ready Architecture and Package Layout under `src/` (12 minutes)

### Why `src/` Layout Matters

**[Instructor speaks:]**

Packaging under `src/` helps separate project code from top-level scripts and encourages clean imports. It also nudges students toward thinking of their application as a reusable package instead of a single giant file.

A sample layout for this checkpoint might look like this:

```text
project_root/
├── demo_persistence.py
├── logs/
│   └── app.log
├── data/
│   └── state.json
└── src/
    └── reading_tracker/
        ├── __init__.py
        ├── errors.py
        ├── logging_config.py
        ├── models.py
        ├── persistence.py
        └── services.py
```

This layout does several useful things:

- `models.py` defines structured domain data
- `services.py` handles business rules
- `persistence.py` handles JSON save/load
- `errors.py` centralizes custom exceptions
- `logging_config.py` keeps logging setup tidy
- `demo_persistence.py` becomes a clear demonstration script

### Protecting Separation of Concerns

**[Instructor speaks:]**

Students should not dump JSON file code into every part of the application. Saving and loading should be handled in a persistence layer. The service layer should not care whether data is stored in JSON today or in a database tomorrow. That separation is what makes the system “persistence-ready” rather than “accidentally tied to one file format.”

In other words:

- models represent the data
- services enforce the rules
- persistence translates between Python objects and storage

That architecture makes future database integration possible because the rest of the app is not married to file I/O details.

### Example Domain Model

**[Instructor speaks:]**

Use a small, concrete domain for the demo. Here is a reading-tracker example using dataclasses and type hints.

```python
from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class Book:
    title: str
    author: str
    pages_read: int = 0


@dataclass(slots=True)
class ReadingState:
    books: list[Book] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {"books": [asdict(book) for book in self.books]}

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "ReadingState":
        raw_books = data.get("books", [])
        books = [Book(**book_data) for book_data in raw_books]
        return cls(books=books)
```

Point out that serialization works because the model gives us a clear path to and from dictionaries. JSON understands primitive structures like dicts, lists, strings, and numbers. It does not understand arbitrary Python objects by magic.

---

## Section 3: Safe JSON Save/Load, Logging, and Exception Strategy (13 minutes)

### Why Not Just `json.dump()` Straight to the Final File?

**[Instructor speaks:]**

Students often write the simplest possible save operation:

```python
with open("state.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
```

That can work, but it has a risk. If the process crashes halfway through writing, the final file may be left partially written or corrupted.

A safer pattern is to write to a temporary file first and then replace the target file atomically. This is what we mean by a **safe save pattern**.

### Custom Exceptions

**[Instructor speaks:]**

Keep custom exceptions in play. The checkpoint explicitly expects them.

Example:

```python
class AppError(Exception):
    """Base application error."""


class ValidationError(AppError):
    """Raised when domain validation fails."""


class PersistenceError(AppError):
    """Raised when save/load operations fail."""
```

These make code more communicative. A `PersistenceError` tells us much more than a vague crash somewhere in file-handling code.

### Logging to File

**[Instructor speaks:]**

Logging matters because persistence bugs are often easier to diagnose after the fact than during the exact moment they happen. A log file gives us a trace.

Show a simple file-based configuration:

```python
from __future__ import annotations

import logging
from pathlib import Path


def configure_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
```

Reinforce that logs should contain useful events such as:

- save started
- save succeeded
- load started
- file missing, using default state
- invalid JSON encountered
- validation failed

### Safe Save Pattern with `pathlib`

**[Instructor speaks:]**

Here is a strong example students can adapt:

```python
from __future__ import annotations

import json
import logging
from pathlib import Path

from reading_tracker.errors import PersistenceError
from reading_tracker.models import ReadingState

logger = logging.getLogger(__name__)


class JSONStateStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def save(self, state: ReadingState) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")

        try:
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(state.to_dict(), file, indent=2)
            temp_path.replace(self.path)
            logger.info("State saved to %s", self.path)
        except OSError as error:
            logger.exception("Failed to save state")
            raise PersistenceError("Could not save application state") from error

    def load(self) -> ReadingState:
        if not self.path.exists():
            logger.info("State file missing at %s; starting with default state", self.path)
            return ReadingState()

        try:
            with self.path.open("r", encoding="utf-8") as file:
                raw_data = json.load(file)
        except json.JSONDecodeError as error:
            logger.exception("State file contains invalid JSON")
            raise PersistenceError("State file is corrupted or invalid JSON") from error
        except OSError as error:
            logger.exception("Failed to load state")
            raise PersistenceError("Could not load application state") from error

        if not isinstance(raw_data, dict):
            raise PersistenceError("State file must contain a JSON object at the top level")

        try:
            state = ReadingState.from_dict(raw_data)
        except (TypeError, KeyError, ValueError) as error:
            logger.exception("State data failed validation")
            raise PersistenceError("State data structure was invalid") from error

        logger.info("State loaded from %s", self.path)
        return state
```

This code captures the checkpoint priorities very well:

- `src/`-friendly modular design
- `pathlib` instead of raw string paths
- safe-save temp-file replacement
- `JSONDecodeError` handling
- validation after loading
- logging to file
- custom exceptions on failure

### Teaching Note on JSON Limits

**[Instructor speaks:]**

JSON is a great checkpoint storage format because it is human-readable and easy to inspect. It is not a magical database. Students should understand both its strengths and its limits.

Strengths:

- simple
- readable
- portable
- easy to demo

Limits:

- weak for concurrency
- not ideal for large-scale querying
- requires explicit serialization rules for custom objects

That is exactly why this checkpoint is called persistence-ready, not persistence-finished.

---

## Section 4: Live Demo – Save -> Restart -> Load (10 minutes)

### Demo Goal

**[Instructor speaks:]**

The runbook specifically asks for a demo procedure that includes save, restart, load, and validation-related behavior. I recommend narrating this as a fast grading workflow. If I can verify these steps quickly, I know the project is on solid ground.

### Demo Script

```python
from __future__ import annotations

import logging
from pathlib import Path

from reading_tracker.errors import PersistenceError, ValidationError
from reading_tracker.logging_config import configure_logging
from reading_tracker.models import Book
from reading_tracker.persistence import JSONStateStore
from reading_tracker.services import ReadingService


def main() -> None:
    configure_logging()
    store = JSONStateStore(Path("data/state.json"))

    try:
        initial_state = store.load()
    except PersistenceError as error:
        print(f"Could not load state: {error}")
        initial_state = None

    service = ReadingService(initial_state)

    try:
        service.add_book(Book(title="Deep Work", author="Cal Newport", pages_read=25))
        service.add_book(Book(title="Clean Code", author="Robert C. Martin", pages_read=10))
        store.save(service.state)
        print("State saved. Simulating restart...")
    except (ValidationError, PersistenceError) as error:
        print(f"Operation failed: {error}")
        return

    # Simulated restart: create a new store-backed service instance.
    restarted_store = JSONStateStore(Path("data/state.json"))

    try:
        reloaded_state = restarted_store.load()
    except PersistenceError as error:
        print(f"Reload failed: {error}")
        return

    restarted_service = ReadingService(reloaded_state)
    print("Reloaded books:")
    for book in restarted_service.list_books():
        print(f"- {book.title} by {book.author} ({book.pages_read} pages read)")


if __name__ == "__main__":
    main()
```

### Demo Narration

**[Instructor speaks:]**

Call out the restart simulation explicitly. We are proving that the second service instance can reconstruct meaningful state from the saved JSON. That is the checkpoint.

Then show quick failure cases if time allows:

- missing file on first load → default state
- corrupted JSON → `PersistenceError` plus log entry
- invalid book data → validation-related failure path

**[Prediction prompt:]** If I manually break the JSON file by deleting a brace, what should happen in a good solution?

[Pause.]

The answer we want is: it should not crash with a cryptic traceback in front of the user. It should handle `JSONDecodeError`, log the details, and communicate a clear failure.

### Fast Grade Checklist

**[Instructor speaks:]**

Model a fast evaluator mindset:

- Can it run?
- Can it load with no file present?
- Can it save valid state?
- Can it restart and load the same state?
- Are failures handled?
- Is logging meaningful?

This gives students a practical review process they can use on their own projects.

---

## Section 5: Hands-On Checkpoint Build (15 minutes)

### Student Task

**[Instructor speaks:]**

Students now build or refine their own persistence-ready core.

**Checkpoint 2: Persistence-ready Core**

Required elements:

- package layout under `src/`
- JSON save/load
- safe save pattern
- logging to file
- custom exceptions still used
- demo script showing save -> restart -> load
- handling of invalid JSON with `JSONDecodeError`

### Completion Criteria

A student solution is complete when:

- application state persists across runs
- missing or invalid storage is handled without uncontrolled crashing
- logs contain meaningful entries about save/load behavior
- the package layout is clear and not all in one file
- persistence code is separated from core service logic
- a demo path exists that proves save -> restart -> load

### Circulation Notes

**[Circulate:]**

Prioritize these checks while moving through the room:

1. Is there actually a `src/` package layout, or is everything still top-level?
2. Are they trying to dump raw objects directly to JSON without converting them?
3. Do they overwrite the final file directly instead of using a temp file?
4. Do they catch `JSONDecodeError` specifically?
5. Are logs written to a file, or only printed to screen?
6. Are custom exceptions still used meaningfully?
7. Can they explain how they would swap JSON storage for a database later?

If a student is stuck, help them narrow the steps:

- first, define `to_dict()` and `from_dict()`
- second, save clean JSON to disk
- third, load it back
- fourth, add safe-save behavior
- fifth, add logging
- sixth, add error handling

That sequence keeps the checkpoint from feeling overwhelming.

### Common Pitfalls to Watch For

- Dumping Python objects directly to JSON without serialization.
- Corrupting the JSON file and not handling `JSONDecodeError`.
- Logging too little to diagnose failures.
- Letting persistence code leak all over the service layer.
- Building a beautiful demo without a real restart/load proof.
- Ignoring missing-file behavior.
- Using bare `except:` and hiding the root cause.

### Optional Extensions

If time remains and the foundation is solid, students may:

- add a `version` field to the JSON for future migration support
- record save timestamps in logs
- add a backup file before replacement
- write a small test covering save/load round-trips

These are worthwhile only after the required checkpoint behavior is dependable.

---


### Persistence Debugging Walkthrough

**[Instructor speaks:]**

Persistence bugs can look scary because the symptom often appears long after the original mistake. A file gets saved incorrectly now, and the failure only becomes obvious when the app restarts later. That delay is why I want to explicitly teach a debugging sequence.

When a student says, “My load function is broken,” I want to ask the following questions in order:

1. What exactly was written to disk?
2. Is the JSON file valid syntax?
3. Does the top-level shape match what `from_dict()` expects?
4. Are required fields present for each object?
5. Did the load function handle missing files separately from invalid files?
6. Did a domain validation rule fail after the file was parsed successfully?

That sequence matters because “it failed on load” can hide several very different problems.

### Instructor-Facing Recovery Scenarios

**[Instructor speaks:]**

Here are the scenarios I would deliberately test, either in a demo or while circulating:

**Scenario 1: First run, no file exists yet.**

Desired behavior: the program recognizes the missing file, logs that a default state is being used, and continues without crashing.

**Scenario 2: File exists and contains valid JSON, but the top-level type is wrong.**

For example, the file contains a list when the loader expects a dictionary. Desired behavior: raise a controlled `PersistenceError`, log the mismatch, and communicate clearly.

**Scenario 3: File exists but contains invalid JSON syntax.**

Desired behavior: catch `JSONDecodeError`, log the exception, and surface a readable failure path.

**Scenario 4: JSON parses successfully, but the contents violate domain assumptions.**

Example: `pages_read` is a string instead of an integer, or a required `title` field is missing. Desired behavior: fail validation intentionally rather than letting strange bugs spread through the rest of the app.

**Scenario 5: Save partially completes and is interrupted.**

This is why the safe-save temp-file pattern matters. Even if students do not simulate a crash in class, they should understand the design reason for writing to a temporary file and replacing the final file only when the write succeeds.

### Instructor Mini-Conference Questions During Checkpoint Work

**[Circulate:]**

Use short questions that reveal architecture quality quickly:

- “Where is your `to_dict()` logic?”
- “Where is your `from_dict()` logic?”
- “What happens if the state file is missing?”
- “What happens if the JSON is corrupt?”
- “Where is your log file configured?”
- “What does your custom persistence exception buy you over a generic crash?”
- “If you switched to a database later, what module would change the most?”

The final question is especially useful because it reveals whether the student actually separated persistence from services.

### Strong Solution Characteristics to Call Out Publicly

**[Instructor speaks:]**

When highlighting good work, praise design decisions that create reliability:

- models know how to convert to and from serializable data
- persistence code is centralized
- logs tell a useful story of save/load behavior
- the demo script proves a restart path instead of merely printing in-memory data
- errors are translated into custom exceptions with understandable meaning

This tells the room that clean architecture is a success criterion, not an optional extra.

### Common Student Misconceptions and Response Scripts

**Misconception 1: “If `json.dump()` ran once, persistence is done.”**

**[Instructor response:]**

Saving once is only half the job. Persistence means the program can later reconstruct working application state from that saved representation.

**Misconception 2: “If load fails, I should just ignore the error and continue.”**

**[Instructor response:]**

Sometimes a missing file is normal, but corrupted data is different. Good software distinguishes first-run conditions from broken-state conditions.

**Misconception 3: “I can put file I/O directly inside service methods and that’s simpler.”**

**[Instructor response:]**

It is simpler in the very short term and more painful in the medium term. Separate persistence now so your service logic can be reused, tested, and swapped to another storage mechanism later.

**Misconception 4: “Printing messages is enough; I do not need logging.”**

**[Instructor response:]**

Console output helps in the moment. Logging helps after the moment, when you need to understand what happened across runs.

### Fast Evaluation Routine Students Can Reuse

**[Instructor speaks:]**

Give students a lightweight self-check they can run every time they touch persistence code:

1. Delete or move the state file and run the app.
2. Confirm the app handles the missing file sensibly.
3. Create or update some state.
4. Save and inspect the JSON file manually.
5. Restart the app and verify the data returns.
6. Deliberately break the JSON syntax.
7. Verify the app handles the failure clearly and logs it.

This routine is simple, but it turns persistence into something they can verify systematically instead of hoping it works.

### Reflection Prompt if Time Remains

**[Instructor speaks:]**

Ask students to write a short answer to this question:

> If your project had to move from JSON storage to a database next week, what parts of your codebase would stay the same, and what parts would change?

A thoughtful answer usually sounds like this: the models and service rules should mostly stay the same, while the persistence module would change the most. That is exactly the architectural separation we want.


### Final Reinforcement Before Debrief

**[Instructor speaks:]**

Checkpoint 2 is not glamorous, but it is foundational. A project with persistence, logging, and clean structure is a project that can grow. A project without those things may still look impressive for one demo, but it is much harder to trust.

Before we close, I want students to connect today’s checkpoint to the bigger picture of software design. The persistence layer they built today is teaching them three durable ideas:

- state should be translated deliberately between memory and storage
- failures should be named and logged clearly
- architecture choices now determine how easily the project can evolve later

That is why this checkpoint matters so much.

### Short Reflection Prompt if Time Remains

**[Instructor speaks:]**

Ask students to complete this sentence:

> The strongest part of my persistence design right now is ________, and the part I most want to improve next is ________.

This gives them a constructive way to end the checkpoint with ownership and next steps.


### Serialization Design Notes Students Should Hear Explicitly

**[Instructor speaks:]**

A subtle but important lesson in this checkpoint is that persistence is not the same thing as “dumping memory to disk.” Students are designing a translation layer.

Inside the running app, objects may have methods, invariants, and relationships. In JSON, we only get plain data structures. That means the persistence layer must answer questions like:

- Which fields are essential to reconstruct the object later?
- Which defaults should exist if older files are missing a field?
- Which values need validation before becoming trusted objects again?
- How can we keep storage format simple without losing important meaning?

Saying this out loud helps students understand why `to_dict()` and `from_dict()` are not just boilerplate. They are the explicit bridge between runtime objects and stored representation.

### Suggested Manual Verification Checklist

**[Instructor speaks:]**

If students ask, “How do I know my persistence layer is actually good enough?” give them this manual checklist:

- Open the saved JSON file and confirm it is readable.
- Verify the top-level shape matches the loader expectations.
- Restart the app and confirm the same entities come back.
- Check that the log file records save and load events.
- Corrupt the JSON deliberately and confirm the app responds clearly.
- Remove the JSON file and confirm first-run behavior still works.

This checklist helps students think like testers and maintainers, not only authors.

### Instructor Note on Future Database Migration

**[Instructor speaks:]**

Finally, connect today’s work to future architecture growth. A student who keeps services independent from JSON storage is already preparing for a database, even if the database never appears in this course. That is the meaning of persistence-ready: the design can evolve because responsibilities were separated early.


### Final Instructor Checklist for Checkpoint Review

**[Instructor speaks:]**

A rapid checkpoint review should let me answer these questions quickly:

- Is the code organized under `src/`?
- Can the app save valid JSON?
- Can it restart and reload state?
- Does it handle missing files cleanly?
- Does it handle invalid JSON through `JSONDecodeError` and a controlled error path?
- Are log entries meaningful?
- Are custom exceptions still visible in the design?

If the answer is yes across that list, the project has crossed an important quality threshold.


### Instructor Summary Phrase to Repeat Aloud

**[Instructor speaks:]**

If students remember one sentence from this checkpoint, let it be this: **persistence is not just writing data once; it is proving that state can be saved safely, loaded reliably, and understood clearly when something goes wrong.**

Add one more reminder if time allows: good persistence design helps the next version of the project, not just the current demo. That is why package structure, logging, and deliberate serialization matter here.


Add a final practical note for students: if a reviewer can follow the save path, inspect the JSON, restart the app, and see the same state restored, the checkpoint has real evidence behind it instead of optimistic assumptions.


That is also a useful standard for students to reuse later: if persistence cannot survive a simple manual verification loop, it is probably not ready to support the rest of the application yet. Reliable software earns trust through repeatable checks.

## Section 6: Debrief & Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

This checkpoint is one of the most important architectural moments in the course. Students who succeed here have something far more valuable than “I wrote more code.” They have a core that can survive restart, surface failures clearly, and evolve later.

Re-emphasize the engineering lessons:

- package your work under `src/`
- separate models, services, persistence, and logging
- serialize deliberately
- save safely
- load carefully
- log what matters
- use exceptions to name failures clearly

**[Ask students:]** If you started your persistence layer again from scratch, what is one design choice you would keep and one you might change?

This reflection helps them internalize architecture rather than treating it as a checklist only.

### Exit Ticket

**[Instructor asks:]**

1. Why is a safe-save temp-file pattern better than writing directly to the final JSON file?
2. What should happen if the JSON file is missing?
3. What should happen if the JSON file exists but contains invalid JSON?
4. Why is the code called persistence-ready rather than database-complete?
5. What is one design decision you would change if you started over?

**[Expected direction of answers:]**

- Safe save reduces the risk of leaving a partially written corrupted final file.
- Missing files should usually lead to a default state or a controlled first-run path.
- Invalid JSON should be caught, logged, and surfaced through a clear error path.
- JSON persistence prepares the architecture, but does not provide full database capabilities.
- The final answer should reveal thoughtful reflection on structure, validation, or logging.

### Instructor Closing Line

**[Instructor speaks:]**

Session 4 has now connected external services, basic security habits, capstone planning, and persistence architecture. That combination is powerful because it moves students from writing isolated Python code to designing maintainable applications.
