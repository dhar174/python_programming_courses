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
class SQLiteTrackerRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def add(self, record: Record) -> Record:
        query = """
            INSERT INTO records (title, category, status)
            VALUES (?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as connection:
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
        with sqlite3.connect(self.db_path) as connection:
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

## Shared Day 8 Instructor Reference

Reuse the shared day-level instructor support from `Day8_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 8 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
