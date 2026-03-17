# Day 7, Hour 3: Row Mapping — Converting Database Rows Back into Objects (Course Hour 27)

## Instructor Notes

- **Course:** Python Programming (Advanced)
- **Session:** 7 (Day 7, Hour 3)
- **Course hour:** 27 – Row mapping: converting rows to objects
- **Runbook reference:** Python_Advanced_Instructor_Runbook_4hr_Days.md – Session 7, Course Hour 27 – Row mapping: converting rows to objects
- **Duration:** 60 minutes
- **Mode:** Instructor-led + live coding + guided lab
- **Audience:** Advanced Python learners who already have basic SQLite CRUD working and now need to return domain objects cleanly

> **Instructor note:** The central teaching goal this hour is architectural cleanliness. Learners have seen raw row tuples, but the rest of their application should not be forced to remember column order or stringly-typed dates. Teach row mapping as a boundary responsibility of the repository. Keep mapping code centralized, use modern Python dataclasses and type hints, and show how `sqlite3.Row` improves readability. The live demo should culminate in `get_by_id`, `update`, and `delete` methods that work with domain objects and clear missing-record behavior. Reinforce the runbook warning about mismatched column ordering and missing `WHERE` clauses.

---

## Instructor Deliverable Script (Use Largely Verbatim)

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain why returning raw row tuples from a repository creates friction for the rest of the application.
2. Use `sqlite3.Row` or a centralized mapping helper to convert database rows into dataclass objects.
3. Implement `get_by_id`, `update`, and `delete` repository methods that work with model objects.
4. Convert stored database values, such as ISO date strings, back into richer Python types.
5. Detect missing records and surface them through a service-layer exception such as `NotFoundError`.
6. Verify that an `UPDATE` query worked by checking the affected row count and re-reading the record."

---

## 1) Agenda + Timing

- **0:00–0:05** Recap: what raw row tuples gave us, and what they did not
- **0:05–0:15** Row mapping concept: keep storage translation inside the repository
- **0:15–0:25** `sqlite3.Row`, column names, and mapping helpers
- **0:25–0:40** Live demo: `from_row`, `get_by_id`, and `list_all`
- **0:40–0:50** Live demo: `update`, `delete`, and missing-record checks
- **0:50–0:57** Guided practice: finish CRUD with mapped objects
- **0:57–1:00** Checkpoint, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file named `hour27_row_mapping_demo.py`.
- Have the prior hour's working SQLite example available for copy/paste.
- Be ready to show one row tuple and ask learners why it is inconvenient.
- Be ready to compare two mapping approaches:
  - tuple unpacking by column order
  - dictionary-style access with `sqlite3.Row`
- Have a simple `NotFoundError` ready to define.
- Be ready to deliberately point out the danger of an `UPDATE` query without a `WHERE` clause.

**Say:** "This hour is less about learning new SQL verbs and more about protecting the rest of the application from database-shaped details. The repository should absorb that complexity for us."

---

## 3) Opening Script: Why Raw Rows Are Not Enough (~5 minutes)

**Say:**
"In the last hour, we made the persistence layer real. We connected to a database, created a table, inserted records, and selected them back out. That was an important milestone.

But we also saw something awkward. `sqlite3` gives us rows as tuples by default. A row might look like this:

```python
(1, 'Coffee beans', 18.5, 'Groceries', '2026-01-13', 'Medium roast')
```

That is useful for debugging, but it is not a great shape for the rest of the application.

Why not?

Because every caller now has to remember what index 0 means, what index 3 means, and which values need conversion. Is `spent_on` still a string? Is `notes` maybe `None`? Did the query select columns in the same order as last time?

Those are repository problems, not service-layer problems. The rest of the application wants to work with domain objects, not mystery tuples."

### 3.1 State the central design rule

**Say:**
"Here is the central rule for the hour: mapping between database rows and domain objects should happen in one place, close to the database code.

If row mapping is scattered everywhere, the code becomes fragile. If row mapping is centralized, the application becomes easier to reason about and easier to change."

---

## 4) Row Mapping Concept: Rows Are Storage Shape, Objects Are Domain Shape

### 4.1 Explain the two shapes

**Say:**
"A database row is storage-shaped. It reflects column names, SQL types, and the order selected in a query.

A domain object is business-shaped. It reflects the concepts your application uses and the types that make sense in Python.

The repository sits at the boundary between those shapes.

For our example:

- the database stores `spent_on` as text like `'2026-01-13'`
- the domain object wants `spent_on` as a `date`
- the database may return `notes` as `NULL`
- the domain object wants `notes` as `str | None`

That translation step is row mapping."

### 4.2 Show the model again for continuity

**Type and narrate:**

```python
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


@dataclass(slots=True)
class Expense(NewExpense):
    expense_id: int
```

**Say:**
"These dataclasses are the language of our application. The repository's job is to return these, not raw tuples."

---

## 5) Mapping Options: Tuple Order versus Named Columns

### 5.1 Tuple-order mapping works, but it is brittle

**Type:**

```python
row = (1, "Coffee beans", 18.50, "Groceries", "2026-01-13", "Medium roast")

expense = Expense(
    expense_id=row[0],
    title=row[1],
    amount=row[2],
    category=row[3],
    spent_on=date.fromisoformat(row[4]),
    notes=row[5],
)
```

**Say:**
"This works. But it is brittle because the mapping depends on the exact column order. If someone changes the `SELECT` clause or forgets the order, the mapping silently breaks.

That is why many developers prefer named access when possible."

### 5.2 Introduce `sqlite3.Row`

**Type and narrate:**

```python
import sqlite3

with sqlite3.connect("data/expenses.db") as connection:
    connection.row_factory = sqlite3.Row
    row = connection.execute(
        "SELECT expense_id, title, amount, category, spent_on, notes FROM expenses LIMIT 1"
    ).fetchone()

    if row is not None:
        print(row["title"])
        print(row["spent_on"])
```

**Say:**
"`sqlite3.Row` gives us a row object that behaves a lot like both a tuple and a dictionary. The key win is readability. Instead of `row[4]`, we can say `row['spent_on']`.

That makes mapping code easier to read and less likely to break from accidental column reordering."

### 5.3 Centralize the mapping helper

**Say:**
"No matter which row style you use, do not repeat the mapping logic in five different methods. Put it in one helper. That way, if you change the schema later, there is one place to update."

---

## 6) Live Demo Part 1: A Repository That Returns Expense Objects (~15 minutes)

**Say:**
"Let's build a repository that sets `row_factory`, defines a mapping helper, and uses it in `list_all` and `get_by_id`."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


class NotFoundError(Exception):
    """Raised when a requested record does not exist."""


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


@dataclass(slots=True)
class Expense(NewExpense):
    expense_id: int

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Expense":
        return cls(
            expense_id=int(row["expense_id"]),
            title=str(row["title"]),
            amount=float(row["amount"]),
            category=str(row["category"]),
            spent_on=date.fromisoformat(str(row["spent_on"])),
            notes=row["notes"],
        )


class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    expense_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    spent_on TEXT NOT NULL,
                    notes TEXT
                )
                """
            )

    def add(self, expense: NewExpense) -> int:
        with self._connect() as connection:
            cursor = connection.execute(
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
            return int(cursor.lastrowid)

    def list_all(self) -> list[Expense]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT expense_id, title, amount, category, spent_on, notes
                FROM expenses
                ORDER BY expense_id
                """
            ).fetchall()
        return [Expense.from_row(row) for row in rows]

    def get_by_id(self, expense_id: int) -> Expense:
        with self._connect() as connection:
            row = connection.execute(
                """
                SELECT expense_id, title, amount, category, spent_on, notes
                FROM expenses
                WHERE expense_id = ?
                """,
                (expense_id,),
            ).fetchone()

        if row is None:
            raise NotFoundError(f"Expense {expense_id} was not found.")

        return Expense.from_row(row)
```

### 6.1 Narration points during coding

**Say:**
"I want you to notice four design choices.

First, `_connect()` centralizes connection setup, including the row factory.

Second, `Expense.from_row()` centralizes row-to-object conversion.

Third, `get_by_id()` returns a domain object, not a tuple.

Fourth, the missing-row case is explicit. We do not return a half-broken fake object. We raise a clear exception."

### 6.2 Ask for prediction

**Ask:**
"If `row['spent_on']` is stored as text, what do you think `date.fromisoformat(...)` gives us back?"

Wait for: a `date` object.

**Say:**
"Exactly. That is the essence of mapping — taking storage-friendly values and turning them into domain-friendly values."

---

## 7) Live Demo Part 2: Update and Delete with Object-Centered Design (~10 minutes)

**Say:**
"Now we will complete the CRUD shape for the repository. The important details are the `WHERE` clause and the confirmation that a row was actually affected."

**Type and narrate:**

```python
class SQLiteExpenseRepository:
    # ... keep previous methods here ...

    def update(self, expense: Expense) -> None:
        with self._connect() as connection:
            cursor = connection.execute(
                """
                UPDATE expenses
                SET title = ?, amount = ?, category = ?, spent_on = ?, notes = ?
                WHERE expense_id = ?
                """,
                (
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.spent_on.isoformat(),
                    expense.notes,
                    expense.expense_id,
                ),
            )

        if cursor.rowcount == 0:
            raise NotFoundError(f"Expense {expense.expense_id} was not found.")

    def delete(self, expense_id: int) -> None:
        print(f"Deleting expense_id={expense_id}")
        with self._connect() as connection:
            cursor = connection.execute(
                "DELETE FROM expenses WHERE expense_id = ?",
                (expense_id,),
            )

        if cursor.rowcount == 0:
            raise NotFoundError(f"Expense {expense_id} was not found.")
```

**Say:**
"`rowcount` is useful here. If the target ID does not exist, zero rows are affected, and that is a signal we should not ignore.

Also notice the `WHERE expense_id = ?` clause. I want to say this dramatically because it matters: never write an update query in a hurry and forget the `WHERE` clause. Without it, you can update every row in the table. That is one of the most painful beginner mistakes in SQL."

### 7.1 Show an end-to-end usage example

**Type:**

```python
repo = SQLiteExpenseRepository(Path("data") / "expenses.db")
repo.init_db()

new_id = repo.add(
    NewExpense(
        title="Team lunch",
        amount=24.00,
        category="Meals",
        spent_on=date(2026, 1, 15),
        notes="Sprint planning day",
    )
)

expense = repo.get_by_id(new_id)
print(expense)

updated = Expense(
    expense_id=expense.expense_id,
    title="Team lunch with client",
    amount=expense.amount,
    category=expense.category,
    spent_on=expense.spent_on,
    notes=expense.notes,
)
repo.update(updated)
print(repo.get_by_id(new_id))

repo.delete(new_id)
print(repo.list_all())
```

**Say:**
"This is much nicer than pushing tuples through the application. The caller works with `Expense` objects, and the repository manages translation."

---

## 8) Service Layer Responsibility: Where Does NotFoundError Belong?

### 8.1 Clarify repository versus service choices

**Say:**
"Different teams make slightly different choices about where a missing-row condition becomes a domain-level error. In our course, a practical pattern is:

- the repository detects missing data cleanly
- the service layer decides how that error should be handled in the broader application

That might mean the repository raises `NotFoundError` directly, as we did here, or it could return `None` and let the service raise the error. The key is consistency.

The runbook says the service layer should handle missing records. The most important part is that the application gets a clear, intentional signal rather than silently failing."

### 8.2 Show one service example

**Type:**

```python
class ExpenseService:
    def __init__(self, repository: SQLiteExpenseRepository) -> None:
        self.repository = repository

    def rename_expense(self, expense_id: int, new_title: str) -> Expense:
        expense = self.repository.get_by_id(expense_id)
        updated = Expense(
            expense_id=expense.expense_id,
            title=new_title,
            amount=expense.amount,
            category=expense.category,
            spent_on=expense.spent_on,
            notes=expense.notes,
        )
        self.repository.update(updated)
        return self.repository.get_by_id(expense_id)
```

**Say:**
"Again, the service is expressing business intent. It is not assembling rows."

---

## 9) Common Pitfalls to Surface Explicitly

### 9.1 Mismatched column ordering

**Say:**
"If you map using tuple positions, changing the `SELECT` column order can silently corrupt your mapping logic. Named access with `sqlite3.Row` reduces that risk."

### 9.2 Missing `WHERE` clause

**Say:**
"The scariest SQL bug of the hour is an update query without `WHERE`. Say it with me: update queries must target IDs."

### 9.3 Forgetting conversion back to domain types

**Say:**
"If you store dates as text and forget to convert them back to `date`, your service layer may start mixing strings and dates. That creates subtle bugs. Boundary conversion should be deliberate."

### 9.4 Copy-paste mapping in multiple places

**Say:**
"If you repeat mapping code in three methods, you now have three places to fix when the schema changes. Centralize it."

---

## 10) Guided Practice: Finish CRUD with Mapped Objects (~7 minutes)

**Say:**
"Now you will take your repository from the previous hour and teach it to return model objects instead of raw tuples."

### 10.1 Practice prompt

Update your repository so that it:

1. Uses a centralized connection helper.
2. Uses `sqlite3.Row` for named column access.
3. Defines a mapping helper, such as `from_row()` on the dataclass or `_row_to_model()` in the repository.
4. Implements `get_by_id()` returning one model object.
5. Implements `update()` with a `WHERE id = ?` clause.
6. Implements `delete()` with a `WHERE id = ?` clause.
7. Detects missing IDs and surfaces a clear error.

### 10.2 Coaching prompts while learners work

- "Where is your row mapping logic located?"
- "If the `spent_on` column is text, where do you convert it back to a `date`?"
- "How can you prove your update actually worked?"
- "What happens if `rowcount` is zero?"

### 10.3 Stretch extension if someone finishes early

Add an `updated_at` text column and update it when the row changes. Emphasize that this is optional and only for learners who are already finished with the core task.

---

## 11) Checkpoint Discussion (~3 minutes)

**Ask:**

1. "Why is centralized row mapping better than converting values in every caller?"
2. "What is the fastest way to confirm your `UPDATE` query worked?"
3. "Why is `sqlite3.Row` often nicer than relying on tuple positions?"
4. "What should your code do if `get_by_id(9999)` finds nothing?"

### 11.1 Reinforcement answers

**Say:**
"A strong answer to the update question is: check `rowcount` and then re-query the record.

A strong answer to the missing-record question is: raise or propagate a clear, intentional error like `NotFoundError`; do not let the failure stay ambiguous."

---

## 12) Recap Script (~3 minutes)

**Say:**
"This hour completed the bridge between database storage and object-oriented application code. We took raw rows and mapped them back into dataclass objects. We used `sqlite3.Row` to make mapping safer and clearer. We implemented `get_by_id`, `update`, and `delete` with explicit missing-record behavior.

The deeper lesson is architectural: the repository protects the rest of the codebase from database-shaped complexity.

Next hour we will harden the database layer further by looking at transactions, integrity constraints, and safe initialization patterns so startup and multi-step writes behave predictably."

---

## 13) Exit Ticket

Have learners answer these quickly:

1. Why should row mapping live in one centralized place?
2. What problem does `sqlite3.Row` help solve?
3. What is one sign that an `UPDATE` or `DELETE` targeted a missing record?

---

## 14) Optional Instructor Reference: Runnable End-of-Hour Example

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


class NotFoundError(Exception):
    pass


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


@dataclass(slots=True)
class Expense(NewExpense):
    expense_id: int

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Expense":
        return cls(
            expense_id=int(row["expense_id"]),
            title=str(row["title"]),
            amount=float(row["amount"]),
            category=str(row["category"]),
            spent_on=date.fromisoformat(str(row["spent_on"])),
            notes=row["notes"],
        )


class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    expense_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    spent_on TEXT NOT NULL,
                    notes TEXT
                )
                """
            )

    def add(self, expense: NewExpense) -> int:
        with self._connect() as connection:
            cursor = connection.execute(
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
            return int(cursor.lastrowid)

    def get_by_id(self, expense_id: int) -> Expense:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT expense_id, title, amount, category, spent_on, notes FROM expenses WHERE expense_id = ?",
                (expense_id,),
            ).fetchone()
        if row is None:
            raise NotFoundError(f"Expense {expense_id} not found")
        return Expense.from_row(row)

    def list_all(self) -> list[Expense]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT expense_id, title, amount, category, spent_on, notes FROM expenses ORDER BY expense_id"
            ).fetchall()
        return [Expense.from_row(row) for row in rows]

    def update(self, expense: Expense) -> None:
        with self._connect() as connection:
            cursor = connection.execute(
                """
                UPDATE expenses
                SET title = ?, amount = ?, category = ?, spent_on = ?, notes = ?
                WHERE expense_id = ?
                """,
                (
                    expense.title,
                    expense.amount,
                    expense.category,
                    expense.spent_on.isoformat(),
                    expense.notes,
                    expense.expense_id,
                ),
            )
        if cursor.rowcount == 0:
            raise NotFoundError(f"Expense {expense.expense_id} not found")

    def delete(self, expense_id: int) -> None:
        with self._connect() as connection:
            cursor = connection.execute(
                "DELETE FROM expenses WHERE expense_id = ?",
                (expense_id,),
            )
        if cursor.rowcount == 0:
            raise NotFoundError(f"Expense {expense_id} not found")
```

---

## 15) Instructor Expansion: Why Mapping Improves the Entire Codebase

**Say:**
"I want to make the architectural payoff explicit. Row mapping is not just a convenience. It changes the texture of the whole application.

Without mapping, every consumer of the repository needs to know database trivia:

- which index contains the ID
- which index contains the date string
- which fields may be null
- what order the `SELECT` statement used

With mapping, callers can think in domain language:

- `expense.title`
- `expense.amount`
- `expense.spent_on`
- `expense.notes`

That is a big reduction in cognitive load. It also makes autocomplete, type hints, testing, and refactoring much more pleasant."

### 15.1 Connect to previous object-oriented work

**Say:**
"Notice how this hour connects back to earlier advanced topics. We spent many hours making our object design cleaner. If we abandon that cleanliness the moment data crosses the database boundary, we lose a lot of the benefit.

A repository that returns proper objects lets the application remain object-oriented even while the storage layer remains relational."

---

## 16) Worked Example: Separate Mapper Function versus Dataclass Classmethod

**Say:**
"There is more than one good place to put mapping logic. The important thing is centralization and consistency. Let me show two respectable options."

### 16.1 Option A: `from_row()` on the dataclass

**Type:**

```python
@dataclass(slots=True)
class Expense:
    expense_id: int
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Expense":
        return cls(
            expense_id=int(row["expense_id"]),
            title=str(row["title"]),
            amount=float(row["amount"]),
            category=str(row["category"]),
            spent_on=date.fromisoformat(str(row["spent_on"])),
            notes=row["notes"],
        )
```

**Say:**
"This option is nice because the model owns the knowledge of how to construct itself from a row."

### 16.2 Option B: private repository mapper

**Type:**

```python
class SQLiteExpenseRepository:
    def _row_to_expense(self, row: sqlite3.Row) -> Expense:
        return Expense(
            expense_id=int(row["expense_id"]),
            title=str(row["title"]),
            amount=float(row["amount"]),
            category=str(row["category"]),
            spent_on=date.fromisoformat(str(row["spent_on"])),
            notes=row["notes"],
        )
```

**Say:**
"This option keeps database-specific translation inside the repository. That can also be a good choice.

Which is better? In this course, either is acceptable if you are consistent. The more important lesson is: do not duplicate mapping logic in multiple methods."

### 16.3 Help learners decide

**Say:**
"If learners ask which one to choose, here is a good answer: if the mapping is tightly tied to one storage representation, a private repository helper is fine. If the model naturally supports construction from several data sources, a classmethod like `from_row()` can be very elegant."

---

## 17) Handling Optional and Missing Data Carefully

### 17.1 Optional columns are normal

**Say:**
"A row mapper should handle optional data intentionally. `notes` is a good example. In SQLite, the column may be `NULL`. In Python, that usually becomes `None`.

That is not a problem; it is part of the type contract."

### 17.2 Example with `None`

**Type:**

```python
row_notes = row["notes"]
notes: str | None = None if row_notes is None else str(row_notes)
```

**Say:**
"Often, `sqlite3` already gives `None` for SQL null values, which is convenient. But it is still good to think about the mapping explicitly so you know the resulting type."

### 17.3 Missing row versus optional field

**Say:**
"There is also an important distinction between a missing field and a missing row.

- A missing optional field is normal.
- A missing row when you asked for a specific ID is usually exceptional.

Those are different situations and your code should treat them differently."

---

## 18) Verification Patterns After UPDATE and DELETE

**Say:**
"The runbook asks a very practical question: what is the fastest way to confirm your `UPDATE` query worked?

There are two strong answers.

1. Check `cursor.rowcount`.
2. Re-query the record and inspect the result.

`rowcount` tells you whether a row was affected. Re-querying tells you whether the data now looks the way you expected. In early development, I recommend doing both."

### 18.1 Example verification helper

**Type and narrate:**

```python
def rename_and_verify(repo: SQLiteExpenseRepository, expense_id: int, new_title: str) -> Expense:
    current = repo.get_by_id(expense_id)
    updated = Expense(
        expense_id=current.expense_id,
        title=new_title,
        amount=current.amount,
        category=current.category,
        spent_on=current.spent_on,
        notes=current.notes,
    )
    repo.update(updated)
    return repo.get_by_id(expense_id)
```

**Say:**
"That re-read step is a powerful debugging habit. It turns an assumed success into a confirmed success."

---

## 19) Debugging Script: When Mapping Goes Wrong

**Say:**
"If your mapped object looks wrong, I want you to debug the boundary in this order:

1. Print the raw row.
2. Confirm the selected column names.
3. Confirm the mapping code uses the same names.
4. Confirm type conversions, especially dates and optional values.
5. Re-run with one record, not twenty.

That debugging order matters because many mapping bugs are simple mismatches hiding in plain sight."

### 19.1 Example of a subtle mismatch

**Say:**
"Suppose your SQL says `SELECT id, title, amount FROM expenses`, but your mapping code expects `expense_id`. If you use named access, you will get a clear key error. That is actually a gift. Silent bugs are worse than loud bugs."

### 19.2 Encourage explicit `SELECT` lists

**Say:**
"Another practical tip: during teaching and early development, prefer explicit column lists over `SELECT *` when mapping matters. It forces you to think about the shape you are returning and keeps the contract visible."

---

## 20) Additional Guided Practice Option: Build a Service Method on Top of the Repository

If the group finishes quickly, give them this extension.

### 20.1 Prompt

Write a service method named `change_category(expense_id: int, new_category: str) -> Expense` that:

1. Uses `get_by_id()` to fetch the current object.
2. Creates an updated `Expense` object.
3. Calls `update()`.
4. Returns the refreshed object.
5. Lets missing-record behavior remain explicit.

### 20.2 Why this extension is useful

**Say:**
"This exercise shows the payoff of row mapping. Service methods become much cleaner when the repository gives them domain objects instead of tuples."

---

## 21) Instructor Debrief Notes for Common Learner Questions

### 21.1 "Why not just return dictionaries?"

**Suggested response:**
"Returning dictionaries is better than raw tuples in some cases, but dataclass objects give stronger structure, better type hints, clearer attribute access, and a model that matches the rest of the application."

### 21.2 "Why not let sqlite3 convert types automatically?"

**Suggested response:**
"Some automatic conversion is possible, but in a course like this, explicit conversion teaches the boundary clearly and keeps the data flow understandable."

### 21.3 "Is this basically what an ORM does?"

**Suggested response:**
"Yes, conceptually an ORM automates a lot of this translation. But learning the manual version first helps you understand the responsibility and spot issues when higher-level tools behave unexpectedly."

---

## 22) One-Minute Reinforcement Script You Can Use Before Dismissal

**Say:**
"If you remember only one architectural idea from this hour, remember this: rows are for storage, objects are for application behavior, and the repository is responsible for translating between them.

That one sentence explains why mapping matters.

If your service layer has to remember that `row[4]` is the date and `row[5]` is the notes field, the storage layer is leaking into the rest of the app. If your service layer receives an `Expense` object with meaningful attributes, the repository is doing its job well."

## 23) Optional Reflection Prompt for Learners

Ask learners to write two short answers:

1. What specific bug becomes less likely when you centralize row mapping?
2. Which mapping choice do you prefer for your project — `from_row()` on the dataclass or a private repository helper — and why?

**Instructor note:** This reflection helps learners move from mechanical coding to architectural reasoning, which is exactly the goal of the hour.
