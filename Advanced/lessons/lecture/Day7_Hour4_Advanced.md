# Day 7, Hour 4: Transactions, Integrity, and Initialization Patterns (Course Hour 28)

## Instructor Notes

- **Course:** Python Programming (Advanced)
- **Session:** 7
- **Hour:** 4 (Course Hour 28)
- **Runbook reference:** Session 7, Course Hour 28 – Transactions + integrity + initialization patterns

> **Instructor note:** This hour hardens the database layer. Keep it practical: grouped writes should succeed together or fail together, initialization should be safe to run every startup, and the database should enforce a small set of meaningful integrity rules. Do not let the session drift into heavy relational theory. Mention foreign keys lightly and accurately: SQLite supports them, but they require `PRAGMA foreign_keys = ON` per connection. The high-value outcomes are idempotent `init_db()`, sensible constraints, and a clear transaction example using a connection context manager. Learners should leave feeling that their persistence layer is no longer a fragile demo but the beginning of a dependable application component.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain what a transaction is in practical terms and why grouped changes should be committed together.
2. Use a connection context manager so successful operations commit and failed operations roll back.
3. Write an `init_db()` function that safely creates schema on startup and can be run repeatedly.
4. Add a small number of useful integrity constraints such as `NOT NULL` and `CHECK`.
5. Explain the SQLite foreign-key reminder: support exists, but it must be enabled with `PRAGMA foreign_keys = ON`.
6. Describe a clean initialization pattern for an application that depends on a database file."

---

## 1) Agenda + Timing

- **0:00–0:05** Recap: what we can do now, and why it is still fragile
- **0:05–0:15** Transactions in plain language
- **0:15–0:25** Integrity constraints and why the database should help protect data
- **0:25–0:40** Live demo: idempotent `init_db()` and transaction-based batch insert
- **0:40–0:50** Live demo: startup initialization pattern with `pathlib` and repository wiring
- **0:50–0:57** Guided practice: harden your own DB layer
- **0:57–1:00** Checkpoint and recap

---

## 2) Instructor Setup Checklist

- Open a clean file named `hour28_transactions_demo.py`.
- Be ready with the repository example from Hour 27.
- Be ready to show a deliberate failure inside a multi-step write so learners can observe rollback behavior.
- Be ready to explain the difference between application validation and database integrity constraints.
- Be ready to mention foreign keys lightly without turning the session into a normalization lecture.
- Be ready to show an `init_db()` call happening at startup before the repository is used.

**Say:** "The first version of database code often works in demos but breaks under repetition, failure, or startup edge cases. This hour is about making the database layer calmer, safer, and more repeatable."

---

## 3) Opening Script: From Working to Reliable (~5 minutes)

**Say:**
"At this point, we can create records, read them back, update them, delete them, and map rows into domain objects. That is already a real milestone.

But working once is not the same as being reliable.

A persistence layer becomes trustworthy when three things are true:

1. Startup is predictable — the schema exists when the app needs it.
2. Bad data is blocked — required fields and business-critical rules are enforced consistently.
3. Multi-step writes behave atomically — either the whole operation succeeds or none of it does.

That is where initialization patterns, integrity constraints, and transactions come in.

Today is not about cleverness. It is about removing fragility."

---

## 4) Transactions in Plain English

### 4.1 Give a non-jargon definition

**Say:**
"A transaction is a group of database operations that should be treated as one unit.

In plain language: either all of them happen, or none of them happen.

That is incredibly important anytime you have multiple related writes. If the first write succeeds and the second fails, you do not want the database left in a half-updated state unless partial success is truly acceptable."

### 4.2 Use a relatable example

**Say:**
"Imagine importing three expenses from a CSV file. If the first two insert successfully and the third one violates a rule, what should happen?

For many applications, the safest answer is: roll the whole batch back so the import can be fixed and retried cleanly.

That is the practical value of a transaction."

### 4.3 Explain connection context manager behavior

**Say:**
"In `sqlite3`, a connection used as a context manager already helps us here.

- If the block exits successfully, changes are committed.
- If an exception escapes the block, changes are rolled back.

That means the `with sqlite3.connect(...) as connection:` pattern is not just tidy syntax. It is part of our reliability story."

---

## 5) Integrity: Let the Database Enforce Structural Rules

### 5.1 Differentiate validation layers

**Say:**
"We already know how to validate data in Python. For example, a service layer might reject negative amounts or blank titles before trying to save.

That is good and necessary.

But the database should also enforce a small set of structural truths. Why? Because bugs happen. Future code changes happen. A script may bypass part of your service layer. The database is the final guardrail for stored data.

Think of it this way:

- application validation improves user experience and gives friendly feedback
- database constraints protect storage integrity even if a bug slips through

Those two layers complement each other."

### 5.2 Show useful constraints for this level

**Say:**
"For this course, practical integrity constraints include:

- `NOT NULL` for required fields
- `CHECK(amount >= 0)` or `CHECK(amount > 0)` depending on the business rule
- a primary key for stable identity

We are keeping it small and understandable."

**Type and narrate:**

```sql
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    amount REAL NOT NULL CHECK(amount >= 0),
    category TEXT NOT NULL,
    spent_on TEXT NOT NULL,
    notes TEXT
)
```

**Say:**
"If your Python code accidentally tries to insert a negative amount, the database now has a chance to object. That is valuable."

### 5.3 Mention foreign keys lightly and accurately

**Say:**
"Foreign keys let one table reference another safely. For example, an `expense` row might reference a `category` row by ID.

We are not building a multi-table design in depth today, but I want you to know one SQLite-specific fact: foreign-key enforcement is not automatically on in every connection. If you use foreign keys, remember to enable them with:

```sql
PRAGMA foreign_keys = ON
```

That reminder saves a lot of confusion later."

---

## 6) Live Demo Part 1: An Idempotent init_db() Function (~15 minutes)

**Say:**
"Let's start by making startup safe and boring. 'Boring' is a compliment in infrastructure code."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class AppPaths:
    project_root: Path

    @property
    def data_dir(self) -> Path:
        return self.project_root / "data"

    @property
    def db_path(self) -> Path:
        return self.data_dir / "expenses.db"


def connect(db_path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    create_expenses_sql = """
    CREATE TABLE IF NOT EXISTS expenses (
        expense_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        amount REAL NOT NULL CHECK(amount >= 0),
        category TEXT NOT NULL,
        spent_on TEXT NOT NULL,
        notes TEXT
    )
    """

    with connect(db_path) as connection:
        connection.execute(create_expenses_sql)

    print(f"Database initialized at {db_path.resolve()}")
```

### 6.1 Narration points

**Say:**
"There are a few important patterns here.

- `init_db()` creates the parent directory if needed.
- It uses `CREATE TABLE IF NOT EXISTS`, so calling it multiple times is safe.
- The connection helper enables foreign keys every time a connection is opened.
- Startup code now has one explicit place to ensure the schema exists.

This is what the runbook means by idempotent initialization."

### 6.2 Explain why repeatable initialization matters

**Say:**
"If `init_db()` is safe to run repeatedly, your application startup becomes simpler. You do not need a complicated 'does it exist?' dance in five places. You just run initialization during startup and move on."

---

## 7) Live Demo Part 2: Transaction for Grouped Inserts (~15 minutes)

**Say:**
"Now let's look at transactions with a batch operation. We will insert several expenses together. Then we will trigger a failure to see what rollback looks like."

**Type and narrate:**

```python
@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


def add_many(db_path: Path, expenses: list[NewExpense]) -> None:
    insert_sql = """
    INSERT INTO expenses (title, amount, category, spent_on, notes)
    VALUES (?, ?, ?, ?, ?)
    """

    with connect(db_path) as connection:
        for expense in expenses:
            print(f"Inserting: {expense.title}")
            connection.execute(
                insert_sql,
                (
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.spent_on.isoformat(),
                    expense.notes,
                ),
            )
```

**Say:**
"At first glance, this just looks like a loop. But the transaction story comes from the connection context manager. All of these inserts are happening within one `with` block. If an exception escapes the block, the whole set of changes is rolled back."

### 7.1 Demonstrate success case

**Type:**

```python
paths = AppPaths(Path.cwd())
init_db(paths.db_path)

seed_expenses = [
    NewExpense("Coffee", 4.75, "Food", date(2026, 1, 13)),
    NewExpense("Parking", 12.00, "Transport", date(2026, 1, 13)),
    NewExpense("Notebook", 8.99, "Office", date(2026, 1, 14), "Ideas"),
]

add_many(paths.db_path, seed_expenses)
```

**Say:**
"That should succeed and commit all three rows together. Now let's intentionally create a failure."

### 7.2 Demonstrate rollback case

**Type and narrate:**

```python
def count_rows(db_path: Path) -> int:
    with connect(db_path) as connection:
        row = connection.execute("SELECT COUNT(*) AS total FROM expenses").fetchone()
    return int(row["total"])


before_count = count_rows(paths.db_path)
print(f"Rows before failed batch: {before_count}")

broken_batch = [
    NewExpense("Office chair", 120.00, "Office", date(2026, 1, 15)),
    NewExpense("Impossible refund", -15.00, "Office", date(2026, 1, 15)),
]

try:
    add_many(paths.db_path, broken_batch)
except sqlite3.IntegrityError as error:
    print(f"Integrity error: {error}")

after_count = count_rows(paths.db_path)
print(f"Rows after failed batch: {after_count}")
```

**Say:**
"Because the second insert violates `CHECK(amount >= 0)`, SQLite raises an integrity error. Since that exception escapes the `with` block, the transaction is rolled back. The new chair row does not remain half-committed. That is exactly the safety property we wanted."

### 7.3 Name the habit explicitly

**Say:**
"The habit is this: when multiple writes belong together, put them in one transaction. Do not commit halfway unless partial success is truly part of the business rule."

---

## 8) Live Demo Part 3: Clean Startup Wiring Pattern (~10 minutes)

**Say:**
"Let's finish with a simple initialization pattern that you can reuse in many projects."

**Type and narrate:**

```python
class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        return connect(self.db_path)

    def list_titles(self) -> list[str]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT title FROM expenses ORDER BY expense_id"
            ).fetchall()
        return [str(row["title"]) for row in rows]


def build_repository(project_root: Path) -> SQLiteExpenseRepository:
    paths = AppPaths(project_root)
    init_db(paths.db_path)
    return SQLiteExpenseRepository(paths.db_path)


repository = build_repository(Path.cwd())
print(repository.list_titles())
```

**Say:**
"This pattern is small but powerful.

- `build_repository()` becomes the startup composition function.
- It ensures the schema exists before the repository is used.
- The rest of the application can ask for a ready-to-use repository.

This is the beginning of dependency wiring. It is simple, explicit, and testable."

---

## 9) Common Pitfalls to Surface Explicitly

### 9.1 Schema drift and manual edits

**Say:**
"One danger in small projects is ad hoc manual edits to the database file or schema. If the schema changes but the code does not, confusion follows quickly. Keep initialization logic in code so the expected structure is visible and repeatable."

### 9.2 Assuming foreign keys are on automatically

**Say:**
"In SQLite, foreign-key support exists, but enforcement must be enabled per connection with `PRAGMA foreign_keys = ON`. If you forget that, your schema may look correct while constraints silently do less than you expect."

### 9.3 Too many constraints too early

**Say:**
"Constraints are good, but there is a balance. Add meaningful rules that reflect real invariants. Do not turn the schema into a puzzle box on day one."

### 9.4 Not testing failure paths

**Say:**
"A transaction strategy is not real until you have seen the failure path. Deliberately trigger one safe error during development and confirm the rollback behavior."

---

## 10) Guided Practice: Harden Your Database Layer (~7 minutes)

**Say:**
"Now you will harden your own repository. The focus is initialization, constraints, and one grouped write."

### 10.1 Practice prompt

Update your project so that it includes:

1. An `init_db(db_path)` function that creates the parent directory and ensures the main table exists.
2. At least one useful integrity constraint beyond the primary key, such as `NOT NULL` or `CHECK`.
3. A connection helper or repository helper that uses a context manager consistently.
4. One grouped-write function that inserts or updates more than one row inside a single transaction.
5. A short test or manual demonstration showing what happens when one operation in the group fails.

### 10.2 Coaching prompts while learners work

- "If your app starts twice, does initialization still succeed?"
- "Which rule belongs in Python validation, and which also belongs in the schema?"
- "If one of three inserts fails, what should happen to the other two?"
- "If you add foreign keys later, where will you enable them?"

### 10.3 Stretch extension

Add a `seed_demo_data()` function that populates the database only if the main table is empty. Emphasize that this is optional and for learners who finish early.

---

## 11) Checkpoint Discussion (~3 minutes)

**Ask:**

1. "Why should `init_db()` be safe to run multiple times?"
2. "In practical terms, what does a transaction protect you from?"
3. "Why is it useful for the database to enforce a rule like `amount >= 0` even if your Python code already validates it?"
4. "What SQLite-specific reminder should you remember if you start using foreign keys?"

### 11.1 Reinforcement answers

**Say:**
"A strong answer to the first question is: safe repeated initialization simplifies startup and avoids fragile existence checks spread throughout the codebase.

A strong answer to the third question is: database constraints protect stored data even if a bug bypasses the application validation layer."

---

## 12) Recap Script (~3 minutes)

**Say:**
"This hour moved our database layer from merely functional to meaningfully safer. We learned that transactions group related writes so they succeed or fail together. We used an idempotent `init_db()` function to make startup predictable. We added integrity constraints so the database helps enforce structural truth. And we introduced a small but effective startup wiring pattern that ensures the repository is ready before the rest of the application uses it.

At this point, learners should have a persistence layer that is not just a demo but a solid foundation for the next phase of the course, where the service layer and user-facing application features rely on it more heavily."

---

## 13) Exit Ticket

Ask learners to answer these in one or two sentences:

1. Why is `init_db()` designed to be safe to run repeatedly?
2. What does a transaction guarantee when an exception occurs halfway through a multi-step write?
3. What is one integrity rule you added to your schema, and why does it matter?

---

## 14) Optional Instructor Reference: Runnable End-of-Hour Example

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class AppPaths:
    project_root: Path

    @property
    def data_dir(self) -> Path:
        return self.project_root / "data"

    @property
    def db_path(self) -> Path:
        return self.data_dir / "expenses.db"


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


def connect(db_path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0),
                category TEXT NOT NULL,
                spent_on TEXT NOT NULL,
                notes TEXT
            )
            """
        )


def add_many(db_path: Path, expenses: list[NewExpense]) -> None:
    with connect(db_path) as connection:
        for expense in expenses:
            connection.execute(
                """
                INSERT INTO expenses (title, amount, category, spent_on, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.spent_on.isoformat(),
                    expense.notes,
                ),
            )


def count_rows(db_path: Path) -> int:
    with connect(db_path) as connection:
        row = connection.execute("SELECT COUNT(*) AS total FROM expenses").fetchone()
    return int(row["total"])


paths = AppPaths(Path.cwd())
init_db(paths.db_path)
add_many(
    paths.db_path,
    [
        NewExpense("Coffee", 4.75, "Food", date(2026, 1, 13)),
        NewExpense("Notebook", 8.99, "Office", date(2026, 1, 14), "Ideas"),
    ],
)
print(count_rows(paths.db_path))
```

---

## 15) Instructor Expansion: Making Transactions Feel Concrete

**Say:**
"Transactions can sound abstract until learners connect them to consequences. So I like to frame the conversation in terms of damage prevention.

Ask learners to imagine these situations:

- a batch import of ten records where record seven is invalid
- a transfer of inventory from one location to another that requires two updates
- a create-and-log workflow where a main record and an audit entry should either both exist or both fail

In each case, partial success can leave the application in a confusing state. Transactions are how we prevent that confusion."

### 15.1 Short phrase to repeat

**Say:**
"A transaction answers the question: what belongs together?"

That sentence is simple, and learners remember it.

---

## 16) Worked Example: Create-and-Log in One Transaction

**Say:**
"To make grouped writes feel more realistic, let's extend our example slightly. We will create an `expense_audit` table and write both the main expense and an audit message in one transaction. This is still advanced-scope appropriate because the code stays small and the idea is valuable."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


def connect(db_path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0),
                category TEXT NOT NULL,
                spent_on TEXT NOT NULL,
                notes TEXT
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expense_audit (
                audit_id INTEGER PRIMARY KEY,
                expense_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (expense_id) REFERENCES expenses(expense_id)
            )
            """
        )


def add_expense_with_audit(db_path: Path, expense: NewExpense) -> int:
    with connect(db_path) as connection:
        expense_cursor = connection.execute(
            """
            INSERT INTO expenses (title, amount, category, spent_on, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                expense.title,
                expense.amount,
                expense.category,
                expense.spent_on.isoformat(),
                expense.notes,
            ),
        )
        expense_id = int(expense_cursor.lastrowid)

        connection.execute(
            """
            INSERT INTO expense_audit (expense_id, message, created_at)
            VALUES (?, ?, ?)
            """,
            (
                expense_id,
                f"Created expense {expense.title}",
                datetime.now().isoformat(timespec="seconds"),
            ),
        )

        return expense_id
```

### 16.1 Narration points

**Say:**
"This is a nice teaching example because two related writes now belong together:

- the main expense insert
- the audit insert

If the second insert fails for some reason, we do not want a main expense row without its audit row if the business expects both. The transaction makes that all-or-nothing behavior possible."

### 16.2 Link back to foreign keys accurately

**Say:**
"Notice the foreign key in `expense_audit`. Because our connection helper enables `PRAGMA foreign_keys = ON`, SQLite will enforce that the audit row references a real expense row."

---

## 17) Initialization Patterns Beyond One Function

### 17.1 Minimal startup pattern

**Say:**
"The smallest useful startup pattern is:

1. compute paths
2. run `init_db()`
3. build the repository
4. start the rest of the app

That pattern is often enough for class projects and many internal tools."

### 17.2 Example startup function

**Type:**

```python
def bootstrap_application(project_root: Path) -> SQLiteExpenseRepository:
    paths = AppPaths(project_root)
    init_db(paths.db_path)
    return SQLiteExpenseRepository(paths.db_path)
```

**Say:**
"This function is tiny, but it communicates a lot. It gives the application one obvious place to begin."

### 17.3 Why explicit startup is better than hidden side effects

**Say:**
"One anti-pattern to avoid is hiding schema creation inside random repository methods. If `list_all()` secretly creates the table the first time it runs, debugging becomes harder because initialization is no longer explicit.

Initialization belongs at startup. Hidden side effects make code surprising."

---

## 18) Debugging Transactions and Integrity Errors

### 18.1 Teach learners to read the exception name first

**Say:**
"When a grouped write fails, the first thing to read is the exception type. If you see `sqlite3.IntegrityError`, that usually points toward a constraint issue, such as a `NOT NULL`, `CHECK`, or foreign-key violation."

### 18.2 Suggested debugging order

**Say:**
"Here is a disciplined debugging order for transaction problems:

1. Read the exception class and message.
2. Identify which statement in the transaction failed.
3. Check the schema constraint that was violated.
4. Re-run with a smaller batch if needed.
5. Confirm the rollback by querying row counts after the failure.

That process is much more effective than deleting the database file immediately every time something goes wrong."

### 18.3 Remind learners that failure demos are healthy

**Say:**
"Do not be afraid to create one intentional failure while developing. If you have never seen your rollback behavior work, you are trusting code you have not really verified yet."

---

## 19) Additional Guided Practice Option: Seed Data Safely

If learners finish early, give them a seed-data extension.

### 19.1 Prompt

Write a function `seed_demo_data(db_path: Path) -> None` that:

1. checks whether the main table is empty
2. if it is empty, inserts two or three demo records in one transaction
3. if it is not empty, does nothing
4. prints a short message explaining what happened

### 19.2 Debrief note

**Say:**
"This extension reinforces idempotent thinking. Good startup helpers can be run multiple times without causing duplicate chaos."

---

## 20) Discussion Prompts for a Stronger Debrief

Use these if you have an engaged group and an extra few minutes.

1. "What rule belongs only in the Python service layer, and what rule also belongs in the schema?"
2. "What operations in your own capstone clearly belong in one transaction?"
3. "What would be risky about relying only on UI validation and not adding database constraints?"
4. "Why is explicit startup wiring easier to reason about than hidden initialization side effects?"

**Instructor note:** These questions help learners connect the database layer to the rest of the application architecture rather than treating it as an isolated technical trick.

---

## 21) Optional Closing Story: Why This Matters in Real Projects

**Say:**
"In real projects, bugs around persistence are rarely exciting algorithm bugs. They are usually reliability bugs.

A row gets partly updated. A startup script assumes a table already exists. A negative number sneaks into the database because one code path skipped validation. A foreign key was declared but never enforced because the pragma was forgotten.

Those bugs are frustrating because they make systems feel untrustworthy.

The good news is that the practices from this hour are not glamorous, but they are powerful. Safe initialization, transactions, and integrity constraints are exactly the kinds of habits that make software feel solid."

---

## 22) Final Reinforcement Script Before the Break or Dismissal

**Say:**
"The reliable version of a database layer is not the one with the most features. It is the one that starts predictably, rejects structurally bad data, and behaves sensibly when something fails halfway through.

That is what transactions, integrity constraints, and initialization patterns give us. They turn persistence from 'it usually works on my machine' into something the rest of the application can trust."

## 23) Optional Reflection Prompt for Learners

Have learners answer these quickly:

1. Name one operation in your own project that clearly belongs inside a transaction.
2. Name one integrity rule your database should enforce even if your UI already validates it.
3. Why is explicit initialization at startup easier to maintain than hidden side effects inside repository methods?

**Instructor note:** These reflection questions help learners connect the technical mechanics to maintainability and long-term application health.
