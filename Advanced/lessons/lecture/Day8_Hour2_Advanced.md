# Day 8, Hour 2: Integrate the Database into the App
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the architecture goal: 5 minutes  
- Direct instruction on repositories and service interfaces: 15 minutes  
- Live integration demo: 10 minutes  
- Guided wiring sprint: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain why the service layer should depend on an interface or behavior rather than a specific storage implementation
2. Replace in-memory or JSON persistence with a SQLite-backed repository while keeping the rest of the app stable
3. Identify what should and should not change when a storage backend is swapped
4. Verify persistence across restarts without creating two conflicting sources of truth
5. Use dependency injection in a practical, beginner-friendly way

---

## Instructor Prep Notes

- Use the same tracker app from earlier sessions
- Have one prior persistence implementation available, such as `JsonTrackerRepository`
- Have the SQLite repository prepared or mostly prepared so the focus stays on integration, not table design
- Keep repeating the phrase "same service contract, new storage engine"
- Prepare a before-and-after folder diagram to make the swap visible

---

## Section 1: The Architecture Goal (5 minutes)

### Opening Script

**[Instructor speaks:]**

This hour is where architecture stops being a buzzword and starts paying rent. Up to this point, some of you have stored records in memory, some in JSON, and some already in SQLite. What matters now is that the application should not care very much which storage mechanism is being used, as long as the service layer can still ask for the same behaviors.

That is the whole point of the repository idea. It is not there to make your folder tree look professional. It is there so you can change storage without rewriting your GUI, without rewriting your API, and without scattering SQL all over the project.

### The One Big Idea

**[Instructor speaks:]**

The one big idea is this: the service layer should depend on what the repository can do, not on how it does it.

That means the service layer should be able to say things like:

- add a record
- list records
- get a record by id
- update a record
- delete a record
- search records

Whether the repository stores data in a list, a JSON file, or a SQLite table is a separate concern.

---

## Section 2: Direct Instruction on Clean Wiring (15 minutes)

### Dependency Injection Without the Jargon Overload

**[Instructor speaks:]**

You may hear the phrase "dependency injection" in software discussions. That phrase can sound more complicated than it is. In our course, dependency injection just means we give the service the repository it should use rather than hard-coding the service to create one specific repository by itself.

Here is the version we want:

```python
repo = SQLiteTrackerRepository("data/tracker.db")
service = TrackerService(repo=repo)
```

Here is the version we are trying to avoid:

```python
class TrackerService:
    def __init__(self):
        self.repo = SQLiteTrackerRepository("data/tracker.db")
```

Why avoid the second version? Because it traps us. It makes the service harder to test. It makes it harder to switch persistence backends. It hides a choice that should be visible.

### What Should Stay Stable

**[Instructor speaks:]**

When we swap the storage layer, these things should stay stable:

- the model classes
- the service method names
- the validation logic
- the exceptions we raise
- the UI callbacks or API routes that call the service

These are the things that may change:

- repository implementation details
- connection setup
- SQL statements
- row mapping code
- initialization steps like `init_db()`

That distinction helps learners avoid panic. They realize they are not rebuilding the whole app. They are replacing one layer.

### The Risk of Two Sources of Truth

**[Instructor speaks:]**

One of the easiest ways to break a student project at this stage is to leave JSON writes active while also writing to SQLite. Then the learner changes one thing in the GUI, another thing in the database, and suddenly nobody knows what the "real" data is.

Say this clearly:

**[Instructor speaks:]**

Once SQLite becomes your source of truth, stop treating JSON as live storage. JSON can still be used for export and import, but not as a second hidden persistence path.

### Recommended Structure

You can show a simple project layout:

```text
src/
  tracker/
    models.py
    exceptions.py
    services.py
    repositories/
      base.py
      json_repo.py
      sqlite_repo.py
    db.py
gui/
  app.py
api/
  app.py
data/
  tracker.db
tests/
```

Then narrate:

**[Instructor speaks:]**

Your folders do not need to match this exactly, but your responsibilities should. The important thing is that the service imports the repository contract or expected behavior, and the GUI or API builds the service with the repository instance.

---

## Section 3: Live Demo of the Storage Swap (10 minutes)

### Demo Setup

**[Instructor speaks:]**

I am going to show a storage swap with the smallest amount of drama possible. First, here is a service that already works with a repository-like object.

```python
class TrackerService:
    def __init__(self, repo):
        self.repo = repo

    def add_record(self, title: str, category: str, status: str):
        record = Record(title=title, category=category, status=status)
        return self.repo.add(record)

    def list_records(self):
        return self.repo.list_all()

    def update_status(self, record_id: int, new_status: str):
        return self.repo.update_status(record_id, new_status)
```

Now the repository implementation:

```python
import sqlite3
from contextlib import closing


class SQLiteTrackerRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def init_db(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('open', 'done'))
            )
        """
        with closing(sqlite3.connect(self.db_path)) as connection:
            connection.execute(query)
            connection.commit()

    def add(self, record: Record) -> Record:
        query = """
            INSERT INTO records (title, category, status)
            VALUES (?, ?, ?)
        """
        with closing(sqlite3.connect(self.db_path)) as connection:
            cursor = connection.execute(
                query, (record.title, record.category, record.status)
            )
            connection.commit()
            record.id = cursor.lastrowid
        return record

    def list_all(self) -> list[Record]:
        query = """
            SELECT id, title, category, status
            FROM records
            ORDER BY id ASC
        """
        with closing(sqlite3.connect(self.db_path)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(query).fetchall()
        return [Record.from_row(row) for row in rows]
```

Now wire it into the application entry point:

```python
def build_service() -> TrackerService:
    repo = SQLiteTrackerRepository("data/tracker.db")
    repo.init_db()
    return TrackerService(repo=repo)
```

### Demo Debrief

After you run the app, add a record, close the app, reopen it, and show that the record persists.

Then say:

**[Instructor speaks:]**

The exciting part of this demo is not that SQLite exists. The exciting part is that the UI barely changed. That is architecture paying off.

### Show a Controlled Failure

If possible, intentionally break the database path and show the error handling or logs:

**[Instructor speaks:]**

I also want you to see a failure. If I point to a missing or wrong database path, the app should fail in a way we can diagnose. Logs matter. Clear errors matter. This is part of shipping, not a side concern.

---

## Section 4: Guided Wiring Sprint (25 minutes)

### Lab Brief

**[Instructor speaks:]**

During this lab, your mission is to replace your old persistence layer with SQLite as the true backing store. You are not trying to redesign every class. You are trying to preserve as much of the surface area as possible.

### Required Tasks

Learners should:

1. Confirm the SQLite repository implements the methods the service expects
2. Add `init_db()` or equivalent startup initialization
3. Update the app entry point to construct the service with the SQLite repository
4. Remove or disable the old JSON-as-primary-storage workflow
5. Prove that add, list, update, and delete still work
6. Prove persistence across restarts

### Suggested Coaching Sequence

When circulating, guide learners in this order:

1. Check the constructor wiring first
2. Check the repository method names second
3. Check row-to-object mapping third
4. Check commit behavior fourth
5. Check UI refresh or API response behavior last

This order matters because many students debug symptoms instead of causes. A stale UI list may be caused by missing commits, a mismatched method name, or the wrong database path.

### What to Say to Learners Who Want to Rewrite Everything

**[Instructor speaks:]**

If you are tempted to refactor every file at once, stop. This is one of those moments where restraint is a professional skill. Make the smallest change that proves the architecture works. Once the app is stable, then improve naming or structure if time remains.

### Common Integration Bugs to Watch For

- Method mismatch such as `list_all()` in one repository and `list_records()` in another
- Forgetting to call `commit()` after inserts, updates, or deletes
- Mapping SQLite rows into dictionaries when the rest of the app expects model objects
- Initializing the service before the database schema exists
- Pointing the GUI at one database file and the API or tests at another

### Mid-Lab Checkpoint Questions

Ask learners:

- If I removed SQLite and gave you a new repository object, what would your service care about?
- Where does validation happen now?
- What is your single source of truth?
- How do you prove the data survives restart?

If they cannot answer those questions, they may have code that works temporarily but an architecture they do not really understand yet.

### Stretch Direction

If a learner finishes early, suggest an export feature:

**[Instructor speaks:]**

Keep SQLite as your source of truth, but add a CSV or JSON export command. That is a useful extension because it adds value without breaking the architecture.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Let's close with the architectural lesson, not just the implementation detail. The goal was never "put data in SQLite" by itself. The goal was "put data in SQLite without turning the rest of the app into spaghetti." If your service interface stayed stable, that is a real design win.

### Share-Out Prompts

Invite learners to share:

- What changed the most during the storage swap?
- What changed the least?
- Where did you discover a hidden coupling?
- What would you refactor next if you had another hour?

### Exit Ticket

Ask:

1. What interface stayed the same when you swapped storage?
2. Why is it risky to keep JSON and SQLite as simultaneous live sources of truth?
3. What part of the integration felt most fragile?

### Transition to the Next Hour

**[Instructor speaks:]**

Next hour we build on this foundation by adding search, filter, and optional pagination patterns. That is where a data-driven app starts feeling genuinely useful instead of just technically correct.

---

## Instructor-Ready Deep Dive: Full Integration Walkthrough

Use this section if learners need a slower, more complete model of the hour's target architecture. It is intentionally written as a near-verbatim script so you can teach from it directly.

### Learning Outcomes Reinforcement

**[Instructor speaks:]**

Before we touch code, I want to restate the learning outcomes in practical language. By the end of this hour, you should be able to point to your service layer and say, "This is the stable public behavior my app uses." You should be able to point to your repository and say, "This is the storage implementation currently responsible for SQLite." You should also be able to restart the program and prove that the database, not a Python list and not an old JSON file, is the source of truth.

That language matters because many database bugs are not really SQL bugs. They are responsibility bugs. The application is writing to one place and reading from another place. The service is doing validation in one method and bypassing it in another. The UI is holding stale objects after the database has changed. Today's design is meant to make those bugs easier to spot.

### A Complete Minimal Example

**[Instructor speaks:]**

Here is a compact version of the pattern. This is not the only way to structure your project, but it demonstrates the responsibilities clearly. Notice that the service receives a repository object. It does not create its own SQLite connection, and it does not know the SQL strings.

```python
from __future__ import annotations

import sqlite3
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(slots=True)
class Record:
    title: str
    category: str
    status: str = "open"
    priority: int = 3
    created_at: str | None = None
    record_id: int | None = None

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Record":
        return cls(
            record_id=row["id"],
            title=row["title"],
            category=row["category"],
            status=row["status"],
            priority=row["priority"],
            created_at=row["created_at"],
        )


class RecordRepository(Protocol):
    def init_db(self) -> None:
        ...

    def add(self, record: Record) -> Record:
        ...

    def list_all(self) -> list[Record]:
        ...

    def update_status(self, record_id: int, status: str) -> Record:
        ...

    def delete(self, record_id: int) -> None:
        ...


class SQLiteRecordRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def init_db(self) -> None:
        create_table = """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('open', 'done')),
                priority INTEGER NOT NULL DEFAULT 3,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """
        with closing(self._connect()) as connection:
            connection.execute(create_table)
            connection.commit()

    def add(self, record: Record) -> Record:
        insert_record = """
            INSERT INTO records (title, category, status, priority)
            VALUES (?, ?, ?, ?)
        """
        select_record = """
            SELECT id, title, category, status, priority, created_at
            FROM records
            WHERE id = ?
        """
        with closing(self._connect()) as connection:
            cursor = connection.execute(
                insert_record,
                (record.title, record.category, record.status, record.priority),
            )
            new_id = cursor.lastrowid
            row = connection.execute(select_record, (new_id,)).fetchone()
            connection.commit()
        return Record.from_row(row)

    def list_all(self) -> list[Record]:
        select_records = """
            SELECT id, title, category, status, priority, created_at
            FROM records
            ORDER BY id ASC
        """
        with closing(self._connect()) as connection:
            rows = connection.execute(select_records).fetchall()
        return [Record.from_row(row) for row in rows]

    def update_status(self, record_id: int, status: str) -> Record:
        update_record = """
            UPDATE records
            SET status = ?
            WHERE id = ?
        """
        select_record = """
            SELECT id, title, category, status, priority, created_at
            FROM records
            WHERE id = ?
        """
        with closing(self._connect()) as connection:
            connection.execute(update_record, (status, record_id))
            row = connection.execute(select_record, (record_id,)).fetchone()
            connection.commit()

        if row is None:
            raise ValueError(f"No record found with id {record_id}")
        return Record.from_row(row)

    def delete(self, record_id: int) -> None:
        delete_record = """
            DELETE FROM records
            WHERE id = ?
        """
        with closing(self._connect()) as connection:
            connection.execute(delete_record, (record_id,))
            connection.commit()


class RecordService:
    def __init__(self, repo: RecordRepository) -> None:
        self.repo = repo

    def add_record(self, title: str, category: str, priority: int = 3) -> Record:
        clean_title = title.strip()
        clean_category = category.strip()
        if not clean_title:
            raise ValueError("Record title is required.")
        if not clean_category:
            raise ValueError("Record category is required.")
        return self.repo.add(
            Record(title=clean_title, category=clean_category, priority=priority)
        )

    def list_records(self) -> list[Record]:
        return self.repo.list_all()

    def mark_done(self, record_id: int) -> Record:
        return self.repo.update_status(record_id=record_id, status="done")

    def delete_record(self, record_id: int) -> None:
        self.repo.delete(record_id)


def build_service() -> RecordService:
    repository = SQLiteRecordRepository(Path("data/tracker.db"))
    repository.init_db()
    return RecordService(repo=repository)
```

Pause after showing this and ask learners to identify each responsibility. The model represents one tracker record with the same fields used across the Day 8 examples. The repository owns persistence and SQL. The service owns application rules such as title and category validation. The builder function wires the pieces together. That is dependency injection in a small, practical form. Also point out `closing(self._connect())`: `closing` releases the connection explicitly, while the explicit `connection.commit()` calls are what persist write operations in this pattern.

### Demo steps

Use these exact steps for the live demo. If you are teaching from a GUI app, translate "run script" into "launch the app," but keep the same evidence trail.

1. Open the old app entry point and identify the existing repository construction. It may be a JSON repository, an in-memory repository, or a hard-coded list.
2. Show learners the current service interface. Read method names aloud: `add_record`, `list_records`, `mark_done`, and `delete_record`.
3. Say: **"These method names are the contract the UI already knows."**
4. Create or open the SQLite repository implementation.
5. Confirm that `init_db()` creates the needed table with `CREATE TABLE IF NOT EXISTS`.
6. Confirm that each SQL statement uses `?` placeholders for values.
7. Change only the composition root or app startup code so it builds `SQLiteRecordRepository` and passes it into `RecordService`.
8. Run the app.
9. Add a record named `Restart proof record`.
10. List records and point out the new database ID.
11. Close the app completely. Do not merely refresh the screen.
12. Reopen the app using the same database path.
13. List records again and show that `Restart proof record` is still present.
14. Update that record to `done`.
15. Delete the record.
16. Close by saying: **"The service interface stayed stable; the storage implementation changed."**

### Instructor narration for the demo

**[Instructor speaks:]**

I want you to watch what I do not change. I am not rewriting the button callback. I am not rewriting the whole service. I am not teaching the UI to speak SQL. I am changing the object that fulfills the repository role. That is the architecture boundary doing useful work.

When I call `repository.init_db()`, I am making startup reliable. The first run should create the schema. The second run should not crash just because the table already exists. That is why `CREATE TABLE IF NOT EXISTS` is the right pattern for this level of the course.

When I close and reopen the program, I am proving persistence in the simplest honest way. If data disappears after restart, then I probably wrote to memory, failed to commit, used the wrong database path, or never reloaded from the database.

## Lab prompt

**[Instructor speaks:]**

Your lab is to wire your existing app to a SQLite repository while preserving the service interface as much as possible. Start from the app you already have. Do not chase a redesign. Your target is a stable storage swap.

Complete these tasks in order:

1. Find the place where your app currently creates the service or repository.
2. Confirm the service method names your GUI, CLI, or API already calls.
3. Implement or reuse a SQLite repository with `init_db()`, add, list, update, and delete methods.
4. Use dependency injection: create the repository first, initialize it, then pass it into the service.
5. Disable JSON or in-memory storage as the live source of truth.
6. Add a record, close the app, reopen the app, and confirm the record persists.
7. Update and delete records by stable database ID, not by visible list position.

If your project has both a GUI and a small script, use the script first for faster feedback. Once the repository works, reconnect the GUI.

## Completion criteria

Learners meet the target for this hour when they can demonstrate all of the following:

- The app creates or opens a SQLite database on startup.
- `init_db()` can run more than once without destroying existing data.
- The service receives a repository object instead of constructing a hard-coded storage backend internally.
- Add, list, update, and delete still work through the service layer.
- A record created before closing the app is still available after reopening the app.
- JSON, CSV, or in-memory lists are not being used as a second live source of truth.
- SQL statements use parameterized values rather than string-concatenating user input.
- The instructor or learner can explain which interface stayed stable during the swap.

## Common pitfalls

Watch for these issues as you circulate:

- **Two live stores:** The UI reads from SQLite but writes to JSON, or the reverse. Ask, "Which file is the source of truth right now?"
- **Service creates its own repository:** This makes tests and future swaps harder. Encourage passing the repository into the service.
- **Missing `init_db()`:** The first run fails because the table does not exist.
- **Destructive initialization:** Learners use `DROP TABLE` during startup and accidentally delete their own data.
- **Wrong database path:** The app writes to `data/tracker.db` from one working directory and reads from another path later.
- **Row shape mismatch:** The repository returns tuples or dictionaries while the service expects model objects.
- **ID confusion:** Update and delete use list index rather than database ID.
- **Stale UI state:** The database changed, but the visible table was not refreshed.

When you see a pitfall, coach with questions before giving the answer. For example: **"What object owns this responsibility?"** and **"Can we prove which storage path the app is using?"**

## Optional Extensions

If learners finish the core integration early, offer one of these extensions without moving beyond the hour's purpose:

- Add an export command that reads from SQLite and writes a CSV or JSON file.
- Add a tiny smoke-test script that builds the service, adds a record, lists records, and deletes the test record.
- Add a log message at startup showing the resolved database path with `Path.resolve()`.
- Add a repository protocol or abstract base class if the project already has multiple repository implementations.

Make the boundary clear: export/import is allowed as an extra feature, but SQLite remains the source of truth.

## Quick Check

Ask learners to answer these without looking at notes:

1. What interface stayed the same when you swapped storage?
2. Why is it useful for the service to receive a repository instead of creating one internally?
3. What does `init_db()` protect us from on first run?
4. How do you prove the database is the source of truth after restart?
5. Why is keeping JSON and SQLite as simultaneous live storage dangerous?

Expected answer themes: the service method names and repository behaviors stayed stable; dependency injection keeps the service testable and flexible; `init_db()` creates the schema safely; restart proof demonstrates persistence; two live stores create conflicting realities.

## Facilitation Notes for a 60-Minute Delivery

For a mixed-pace class, protect the middle of the hour. Faster learners may want to add features, while slower learners may still be discovering where their app is wired. Keep bringing everyone back to a single sentence: **"Same service contract, SQLite-backed repository."**

During the first 20 minutes, do not let the class disappear into unrelated refactors. During the lab, ask learners to show evidence rather than describe intentions. Evidence includes a database file at the expected path, a visible record after restart, and a service constructor that accepts a repository. In the debrief, celebrate small architectural wins: a UI callback that did not change, a test that can still use an in-memory fake, or a repository method that cleanly maps rows into model objects.

Close with this line:

**[Instructor speaks:]**

Today you made the database part of the application without letting the database take over the application. That is the professional habit we are practicing.

## Additional Instructor Script: Diagnosing the Integration Boundary

Use this optional teaching block if learners finish the basic wiring but still cannot explain why the design matters.

**[Instructor speaks:]**

Let's slow down and name the boundary. The service layer is where our application language lives. In a tracker app, that language might be "add a record," "complete a record," "list open records," or "delete a record." The repository layer is where storage language lives. In a SQLite repository, that language is `INSERT`, `SELECT`, `UPDATE`, and `DELETE`. Good design does not mean those languages never meet. It means they meet in a controlled place.

When the service calls `repo.add(record)`, that is the meeting point. The service does not know whether `repo.add()` writes to SQLite, a JSON file, or a test double. The repository does not decide whether an empty title is acceptable. Each layer has a job.

Here is a useful board diagram to draw:

```text
User action
   ↓
UI / API / CLI
   ↓ calls stable service method
Service layer
   ↓ validates and coordinates
Repository interface
   ↓ implemented by
SQLite repository
   ↓ parameterized SQL
SQLite database file
```

After drawing it, ask learners to point to the place where the storage swap happened. They should identify the repository implementation and the startup wiring. If they point to the UI, pause and clarify: the UI may need to refresh after data changes, but it should not be responsible for the storage strategy.

### Instructor-Led Debugging Drill

Run this as a five-minute verbal exercise:

**Scenario 1:** A learner adds a record, sees it immediately, closes the app, reopens it, and the record is gone.

Ask: "Which layer do we inspect first?" The answer is not automatically the UI. Start with the source of truth. Is the app writing to SQLite? Is it committing? Is the database path the same on restart? Is startup deleting the data?

**Scenario 2:** A learner adds a record and gets an error that the `records` table does not exist.

Ask: "What contract did startup fail to honor?" The likely answer is `init_db()` did not run before repository methods were used, or it ran against a different database path. This is why initialization belongs in the application composition step, before the service is used.

**Scenario 3:** A learner's test used to pass with the JSON repository but now fails after switching to SQLite.

Ask: "Did the service interface change?" If the service method names or return types changed, the storage swap leaked through the boundary. The fix may be to make the SQLite repository match the existing expected behavior instead of forcing every caller to adapt.

### Teaching the "Composition Root" Without Overloading Learners

**[Instructor speaks:]**

Professional developers sometimes use the phrase "composition root." You do not need to memorize that phrase for the checkpoint, but the idea is helpful. It means there should be one obvious place where the app wires major objects together. In a small app, that might be `main.py`, `app.py`, or a `build_service()` function.

This is a clean startup pattern:

```python
def main() -> None:
    service = build_service()
    launch_gui(service)
```

This is a less clean pattern:

```python
def on_add_button_click() -> None:
    repo = SQLiteRecordRepository(Path("data/tracker.db"))
    repo.init_db()
    service = RecordService(repo)
    service.add_record(title_entry.get(), category_entry.get())
```

The second version creates and initializes storage inside a button click. That makes the program harder to reason about and easier to break. We want storage wiring to happen once at startup, then ordinary user actions should call the already-built service.

### More Evidence Learners Can Show

When grading or coaching, ask for proof in small pieces:

- "Show me the database path in code."
- "Show me the `CREATE TABLE IF NOT EXISTS` statement."
- "Show me the service constructor."
- "Show me one repository method with placeholders."
- "Show me a record after restart."
- "Show me where JSON is no longer used as live storage."

These prompts are intentionally concrete. They prevent vague answers like "I think it saves" and replace them with observable evidence.

### Final Reinforcement

**[Instructor speaks:]**

A stable service interface is a gift to your future self. Today it let you swap storage. Next session it may let you expose the same behavior through an API. Later it may let you write tests without launching the GUI. The point is not to add layers for decoration. The point is to keep changes local. When SQLite becomes the source of truth, the repository changes the most, startup wiring changes a little, and the rest of the app should remain recognizable.
