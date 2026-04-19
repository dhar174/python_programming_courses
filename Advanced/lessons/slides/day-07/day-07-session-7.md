# Advanced Day 7 — Session 7 (Hours 25–28)
Python Programming (Advanced) • From Objects to Tables with SQLite

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 7 overview (Hours 25–28); Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Instructor Notes -->

---

# Session 7 Overview

## Topics Covered Today
- Hour 25: Schema thinking + repository boundary
- Hour 26: `sqlite3` CRUD with parameterized queries
- Hour 27: Row mapping back into domain objects
- Hour 28: Transactions, integrity, and `init_db()`

## Today's milestone
- Move from JSON-ready architecture to database-ready architecture
- Keep the service layer clean while the repository absorbs SQL details

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 7 overview (Hours 25–28); Advanced/lessons/lecture/Day7_Hour2_Advanced.md — Opening Script -->

---

## Homework + Quiz Emphasis

- Design the table from the domain model before coding
- Use parameter placeholders for every query with values
- Centralize row-to-object mapping
- Make startup safe with `init_db()` and meaningful constraints

### Canonical quiz/contracts to recognize
- `Hour 25 | table name: tasks`
- `Hour 26 | insert result: task-101 saved`
- `Hour 27 | row type: sqlite3.Row`
- `Hour 28 | init script: schema ready`

<!-- Sources: Advanced/assignments/Advanced_Day7_homework.ipynb — Part 1 through Part 4; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 25 through Hour 28 canonical contract questions -->

---

# Hour 25: Schema Thinking + Repository Idea

## Learning Outcomes
- Map object attributes to table columns
- Choose a stable primary key
- Decide what is required vs optional
- Name the CRUD operations before writing SQL
- Define a repository interface for the core record type

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 25: From objects to tables: schema thinking + repository idea; Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Learning Outcomes -->

---

## From Object Shape to Table Shape

### Python view
```python
@dataclass(slots=True)
class Expense:
    expense_id: int
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None
```

### Database view
- One object ≈ one row
- Attributes ≈ columns
- Collection ≈ table
- Stable ID ≈ primary key

<!-- Sources: Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Schema Thinking: From One Object to One Row -->

---

## Draft the Schema Before the CRUD Code

```sql
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    spent_on TEXT NOT NULL,
    notes TEXT
);
```

### Design questions to answer first
- Which fields are required?
- Which fields are optional?
- Which field is true identity?
- Which values are derived vs stored?

<!-- Sources: Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Table Design: Columns, Primary Keys, and Constraints -->

---

## Why a Repository Boundary Helps

- Service code should ask for behaviors, not write SQL directly
- Repository isolates DB details
- Later storage changes are less disruptive
- Tests can target repository or service behavior more cleanly

### Repository sketch
```python
class ExpenseRepository(Protocol):
    def add(self, item: NewExpense) -> Expense: ...
    def list_all(self) -> list[Expense]: ...
    def get_by_id(self, expense_id: int) -> Expense | None: ...
```

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Repository isolates DB details; Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Repository idea -->

---

## Lab: Design Schema + Interface

**Time: 25–35 minutes**

### Tasks
- Draft a schema for your tracker's main record
- Choose a stable ID type
- List the CRUD methods the app will need
- Write a repository interface or stub class

### Completion Criteria
✓ Schema draft exists  
✓ Repository methods are defined  
✓ Required vs optional fields are explicit  
✓ Update/delete are planned around IDs

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Design schema; Advanced/assignments/Advanced_Day7_homework.ipynb — Part 1: Hour 25 -->

---

## DB Quality Gate (Starts Now)

* All SQL uses `?` placeholders — no string concatenation  
* DB writes are committed via context manager or explicit `commit()`  
* Every table has a stable primary key  
* Update/delete always target IDs  
* Log or print the target ID during early debugging

## Quick Check
**Question**: Why is a repository useful even for a small project?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — DB Quality Gate; Quick check / exit ticket; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 25 explanation -->

---

# Hour 26: `sqlite3` CRUD with Parameterized Queries

## Learning Outcomes
- Create/connect to a database file
- Use `CREATE TABLE IF NOT EXISTS`
- Insert and list records safely
- Understand why `?` placeholders matter
- Debug missing commits and DB-path mistakes

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 26: sqlite3 CRUD with parameterized queries; Advanced/lessons/lecture/Day7_Hour2_Advanced.md — Learning Outcomes -->

---

## `sqlite3` Fundamentals

```python
from pathlib import Path
import sqlite3

db_path = Path("data") / "expenses.db"
db_path.parent.mkdir(exist_ok=True)

with sqlite3.connect(db_path) as connection:
    print("Connected.")
```

### Key ideas
- SQLite is just a file on disk
- Use `pathlib` for paths
- Use a context manager for safer commit/rollback behavior

<!-- Sources: Advanced/lessons/lecture/Day7_Hour2_Advanced.md — sqlite3 Fundamentals -->

---

## Safe SQL: Use Parameters, Not String Building

### Avoid
```python
unsafe_sql = f"SELECT * FROM expenses WHERE title = '{user_title}'"
```

### Prefer
```python
safe_sql = "SELECT * FROM expenses WHERE title = ?"
rows = connection.execute(safe_sql, ("Lunch",)).fetchall()
```

### Why
- Safer quoting/escaping
- Lower injection risk
- More predictable query structure

<!-- Sources: Advanced/lessons/lecture/Day7_Hour2_Advanced.md — Parameterized Queries: The Safety Rule of the Hour -->

---

## Demo: First SQLite Repository Methods

### Demo flow
1. Create the DB file
2. Create the table with `IF NOT EXISTS`
3. Implement `add()`
4. Implement `list_all()`
5. Print the DB path and inserted result

**Quiz/homework cue**: `Hour 26 | insert result: task-101 saved`

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: create db file; create table; insert one row; select rows; Advanced/assignments/Advanced_Day7_homework.ipynb — Part 2: Hour 26; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 26 canonical contract -->

---

## Lab: First SQLite Integration

**Time: 25–35 minutes**

### Tasks
- Create a DB file in `data/`
- Create the table
- Implement `repo.add()`
- Implement `repo.list_all()`
- Print results to confirm real persistence

### Completion Criteria
✓ DB file created  
✓ Insert and list work  
✓ Queries use parameters  
✓ Writes are committed

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: First SQLite integration; Advanced/assignments/Advanced_Day7_homework.ipynb — Part 2: Hour 26 -->

---

## Common Pitfalls (Hour 26)

⚠️ Forgetting `commit()` / assuming the write stuck  
⚠️ String-formatting SQL  
⚠️ Writing to one DB file and reading from another  
⚠️ Skipping the DB path print during debugging

## Quick Check
**Question**: What does the `?` placeholder do in `sqlite3`?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 26 explanation -->

---

# Hour 27: Row Mapping Back into Objects

## Learning Outcomes
- Convert rows into dataclass/domain objects
- Use `sqlite3.Row` for readable mapping
- Implement `get_by_id`, `update`, and `delete`
- Convert stored text back into richer Python types
- Surface missing-record errors clearly

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 27: Row mapping: converting rows to objects; Advanced/lessons/lecture/Day7_Hour3_Advanced.md — Learning Outcomes -->

---

## Why Raw Rows Are Not Enough

```python
(1, "Coffee beans", 18.5, "Groceries", "2026-01-13", "Medium roast")
```

### Problems with raw tuples
- Callers must remember column order
- Type conversion gets repeated
- Storage details leak upward
- Small schema changes become fragile

### Better goal
Return domain objects from the repository.

<!-- Sources: Advanced/lessons/lecture/Day7_Hour3_Advanced.md — Opening Script: Why Raw Rows Are Not Enough -->

---

## Use `sqlite3.Row` + a Mapping Helper

```python
# from datetime import date  # required for date.fromisoformat()
connection.row_factory = sqlite3.Row

def from_row(row: sqlite3.Row) -> Expense:
    return Expense(
        expense_id=row["expense_id"],
        title=row["title"],
        amount=row["amount"],
        category=row["category"],
        spent_on=date.fromisoformat(row["spent_on"]),
        notes=row["notes"],
    )
```

### Rule
Keep mapping logic in one place.

<!-- Sources: Advanced/lessons/lecture/Day7_Hour3_Advanced.md — Mapping Options: Tuple Order versus Named Columns; Centralize the mapping helper -->

---

## Demo: Complete CRUD with Mapped Objects

### Demo flow
- Set `row_factory`
- Implement `list_all()` and `get_by_id()`
- Implement `update()` with a `WHERE` clause
- Implement `delete()`
- Re-read or check affected row count after update
- Raise `NotFoundError` at the service layer when needed

### Watch for
- Mismatched column names/order
- Missing `WHERE` in `UPDATE`

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: repo.get_by_id returns a model object; Show NotFoundError when no row; Advanced/lessons/lecture/Day7_Hour3_Advanced.md — Live Demo Part 1 -->

---

## Lab: Finish Repo CRUD

**Time: 25–35 minutes**

### Tasks
- Implement `get_by_id`
- Implement `update`
- Implement `delete`
- Ensure service code handles missing records clearly

### Completion Criteria
✓ CRUD repository methods are complete  
✓ Row mapping is centralized  
✓ Service layer handles missing IDs  
✓ Update/delete target the correct row

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Implement get/update/delete; Advanced/assignments/Advanced_Day7_homework.ipynb — Part 3: Hour 27 -->

---

## Common Pitfalls (Hour 27)

⚠️ Leaking raw tuples to the rest of the app  
⚠️ Mismatched column ordering/names  
⚠️ `UPDATE` without `WHERE`  
⚠️ Forgetting to verify that the intended row changed

## Quick Check
**Question**: What is the fastest safe way to confirm your `UPDATE` query worked?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 27 explanation -->

---

# Hour 28: Transactions, Integrity, and `init_db()`

## Learning Outcomes
- Explain transactions in practical terms
- Use context-manager commits/rollbacks
- Write an idempotent `init_db()`
- Add a small set of meaningful constraints
- Remember the SQLite foreign key reminder

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 28: Transactions + integrity + initialization patterns; Advanced/lessons/lecture/Day7_Hour4_Advanced.md — Learning Outcomes -->

---

## Reliability Means More Than “It Worked Once”

### A trustworthy DB layer has:
1. Predictable startup
2. Structural guardrails against bad data
3. Multi-step writes that succeed together or fail together

### Plain-language transaction rule
Either **all** related writes happen, or **none** of them do.

<!-- Sources: Advanced/lessons/lecture/Day7_Hour4_Advanced.md — Opening Script: From Working to Reliable; Transactions in Plain English -->

---

## Safe Initialization Pattern

```python
def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as connection:
        connection.execute(create_table_sql)
```

### Why `init_db()` matters
- Startup becomes predictable
- Schema creation is safe to repeat
- New environments require less manual setup

### Integrity examples
- `NOT NULL`
- `CHECK(amount >= 0)`
- Stable primary key

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: init_db() function and calling it once at startup; Add basic constraints (NOT NULL for required fields); Advanced/lessons/lecture/Day7_Hour4_Advanced.md — Live Demo Part 1 -->

---

## Demo: Hardening the DB Layer

### Demo flow
- Create `connect()` helper
- Enable `PRAGMA foreign_keys = ON`
- Run `init_db()` on startup
- Show one grouped transaction
- Demonstrate rollback on failure

**Quiz/homework cue**: `Hour 28 | init script: schema ready`

<!-- Sources: Advanced/lessons/lecture/Day7_Hour4_Advanced.md — Mention foreign keys lightly and accurately; Live Demo Part 1; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 28 canonical contract -->

---

## Lab: Hardening Sprint

**Time: 25–35 minutes**

### Tasks
- Write `init_db(db_path)`
- Ensure it is safe to run more than once
- Add basic constraints
- Test one failure path in a grouped write

### Completion Criteria
✓ DB initializes reliably  
✓ Constraints protect storage  
✓ Grouped writes behave predictably  
✓ Startup is calmer and more repeatable

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Hardening DB layer; Advanced/assignments/Advanced_Day7_homework.ipynb — Part 4: Hour 28 -->

---

## Common Pitfalls (Hour 28)

⚠️ Partially applied writes  
⚠️ Schema drift after code changes  
⚠️ Assuming foreign keys are on automatically  
⚠️ Manual setup steps hidden outside startup

## Quick Check
**Question**: Why should `init_db()` be safe to run multiple times?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day7_Quiz.html — Hour 28 explanation -->

---

# Session 7 Wrap-Up

## What We Added
- Table-first thinking
- Safe `sqlite3` CRUD
- Clean row mapping
- More dependable startup and writes

## Scope Guardrails
✓ Standard-library SQLite  
✓ Parameterized SQL  
✓ Repository boundary  
✓ Practical constraints and transactions

✗ Not today: ORM migration frameworks  
✗ Not required: multi-table deep design

<!-- Sources: Advanced/lessons/lecture/Day7_Hour1_Advanced.md — Instructor note; Advanced/lessons/lecture/Day7_Hour4_Advanced.md — Instructor note -->

---

# Thank You!

Session 8 next:
- Deeper SQL or tiny ORM exposure
- Plug SQLite into the app
- Search, pagination, and the data-driven checkpoint

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 8 overview (Hours 29–32) -->
