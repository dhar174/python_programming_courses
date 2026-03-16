# Day 7, Hour 2: SQLite CRUD with Parameterized Queries (Course Hour 26)
**Python Programming (Advanced) – Session 7**

**Course:** Python Programming (Advanced)  
**Runbook alignment:** Session 7, Course Hour 26 – sqlite3 CRUD with parameterized queries  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Advanced Python learners ready to connect a repository design to a real SQLite database

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This hour is the learners' first concrete SQLite implementation in the advanced sequence. Keep the conversation practical and specific. The targets are: open a database file with `sqlite3`, create a table safely with `CREATE TABLE IF NOT EXISTS`, and run safe CRUD operations using `?` parameter placeholders. Reinforce the runbook quality gate repeatedly: no SQL string concatenation, every write is committed, and update/delete must be ID-based. Keep ORMs out of scope. The point is confidence with the standard library and visibility into what the application is actually doing.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Create and connect to an SQLite database file using Python's standard library.
2. Create a table with `CREATE TABLE IF NOT EXISTS` so initialization is safe to repeat.
3. Execute `INSERT`, `SELECT`, `UPDATE`, and `DELETE` statements with parameterized queries.
4. Explain why `?` placeholders are safer than building SQL with string formatting.
5. Implement the first working SQLite repository methods for adding and listing records.
6. Debug common early SQLite issues such as missing commits and incorrect database paths."

---

## 1) Agenda + Timing

- **0:00–0:05** Recap: schema and repository from Hour 25
- **0:05–0:15** `sqlite3` basics: connection, cursor, database file, commits
- **0:15–0:25** Safe SQL: parameterized queries and why string formatting is dangerous
- **0:25–0:40** Live demo: create database, create table, insert rows, list rows
- **0:40–0:50** Live demo extension: raw update and delete examples
- **0:50–0:57** Guided practice: implement `add()` and `list_all()` in a repository
- **0:57–1:00** Checkpoint and recap

---

## 2) Instructor Setup Checklist

- Open a clean file named `hour26_sqlite_crud_demo.py`.
- Make sure a `data/` directory exists or be prepared to create it during the demo using `pathlib`.
- Be ready to explain that an SQLite database is just a file on disk.
- Be ready to deliberately show one unsafe SQL example **without running untrusted data**, purely for teaching contrast.
- Be ready to show what happens when you forget to commit a write.
- Be ready to print the database path so learners can see exactly which file they are writing to.

**Say:** "This hour is about making the persistence layer real. We are moving from design to execution, but we are going to do it in a disciplined way. Every database action should feel understandable, inspectable, and safe."

---

## 3) Opening Script: From Design to a Real Database (~5 minutes)

**Say:**
"In the previous hour, we designed the shape of our persistence layer. We talked about objects, rows, columns, primary keys, and repository boundaries. That was intentionally conceptual.

Now we make it concrete.

Python ships with a database module called `sqlite3`. That matters because it means you can build a real data-driven application without installing anything extra. SQLite stores data in a normal file, which makes it excellent for local tools, prototypes, desktop apps, class projects, and many small-to-medium applications.

This hour is about basic database mechanics done correctly. Our goals are modest but important:

- create the database file
- create the table
- insert records
- read records back
- and understand how update and delete fit into the same pattern

The most important safety rule of the hour is this: if your SQL query includes data from the program, use placeholders. Do not build SQL by pasting values into strings."

---

## 4) sqlite3 Fundamentals

### 4.1 Explain the connection object

**Say:**
"The first thing to understand is the connection. A connection represents an active link to a database file. In SQLite, if the file does not exist yet, SQLite can create it for you when you connect.

That means connecting is often the moment where your database file comes into existence."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from pathlib import Path


project_root = Path.cwd()
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)

db_path = data_dir / "expenses.db"
print(f"Database file: {db_path.resolve()}")

with sqlite3.connect(db_path) as connection:
    print("Connected successfully.")
```

**Say:**
"This example shows several modern habits.

- We use `pathlib.Path` instead of raw string path manipulation.
- We make sure the directory exists before trying to create the database file.
- We use a connection context manager with `with`.

That `with` block matters. When the block exits, the connection is closed cleanly. Also, for write operations, the context manager helps manage commits and rollbacks more safely."

### 4.2 Explain cursor versus connection

**Say:**
"You will often hear about cursors. A cursor is the object you use to execute SQL statements and fetch results.

In small `sqlite3` programs, you will commonly see either of these styles:

1. `connection.execute(...)` directly
2. `cursor = connection.cursor()` followed by `cursor.execute(...)`

Both are valid. For short examples, `connection.execute(...)` is often clean enough. When you want to fetch results or reuse the cursor, making it explicit can help readability."

**Type:**

```python
with sqlite3.connect(db_path) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    print(cursor.fetchone())
```

**Say:**
"This prints a tuple like `(1,)`. That tiny experiment proves the connection is alive and the basic execution path works."

---

## 5) Creating the Table Safely

### 5.1 Show idempotent table creation

**Say:**
"The first real SQL in most applications is schema creation. We do not want startup to fail just because the table already exists, so we use `CREATE TABLE IF NOT EXISTS`."

**Type and narrate:**

```python
create_table_sql = """
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    spent_on TEXT NOT NULL,
    notes TEXT
)
"""

with sqlite3.connect(db_path) as connection:
    connection.execute(create_table_sql)

print("Table ensured.")
```

**Say:**
"This is called idempotent initialization. If the table is missing, it gets created. If it already exists, the statement is safe to run again.

That is a big engineering win because application startup should be dependable."

### 5.2 Connect table design back to the domain model

**Say:**
"Remember our Python dataclass used `date` for the spending date. The table stores `spent_on` as text. That is not inconsistency. That is translation across a boundary. We store the date as an ISO string because it is easy for SQLite to hold and easy for people to inspect."

---

## 6) Parameterized Queries: The Safety Rule of the Hour

### 6.1 Show the unsafe instinct

**Say:**
"Let me show you the instinct we want to avoid. Beginners often try to do this:"

**Type:**

```python
# Do not do this.
user_title = "Lunch"
unsafe_sql = f"SELECT * FROM expenses WHERE title = '{user_title}'"
print(unsafe_sql)
```

**Say:**
"At first glance, that looks convenient. But it has two problems.

First, it is brittle. Quotes inside the title can break the query.

Second, and much more important, it opens the door to SQL injection if untrusted input is inserted into the SQL string. Even if you trust your own test data, building the habit of string-formatting SQL is a bad habit.

The correct habit is parameterized SQL."

### 6.2 Show the safe pattern

**Type and narrate:**

```python
safe_sql = "SELECT * FROM expenses WHERE title = ?"
parameter = ("Lunch",)

with sqlite3.connect(db_path) as connection:
    rows = connection.execute(safe_sql, parameter).fetchall()
    print(rows)
```

**Say:**
"The SQL string stays fixed, and the values are passed separately.

That question mark is not a text replacement marker in the string-formatting sense. It is a placeholder that tells `sqlite3`, 'here comes a value parameter.' The database driver handles quoting and escaping correctly.

This is one of those rules I want you to internalize so deeply that unsafe SQL starts to feel physically uncomfortable."

### 6.3 Read the runbook quality gate aloud

**Say:**
"The runbook says it plainly: all SQL uses parameter placeholders, no string concatenation. I want that quality gate visible in every database file you write."

---

## 7) Live Demo Part 1: Insert and List Rows (~15 minutes)

**Say:**
"Now let's build the first working slice of the repository. We will create the database, ensure the table exists, insert a couple of expenses, and list them back out. For this hour, seeing raw rows is acceptable. Next hour we will map them back into rich objects."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            spent_on TEXT NOT NULL,
            notes TEXT
        )
        """
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(create_table_sql)

    def add(self, expense: NewExpense) -> int:
        insert_sql = """
        INSERT INTO expenses (title, amount, category, spent_on, notes)
        VALUES (?, ?, ?, ?, ?)
        """
        values = (
            expense.title,
            expense.amount,
            expense.category,
            expense.spent_on.isoformat(),
            expense.notes,
        )
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(insert_sql, values)
            return int(cursor.lastrowid)

    def list_all_rows(self) -> list[tuple]:
        select_sql = """
        SELECT expense_id, title, amount, category, spent_on, notes
        FROM expenses
        ORDER BY expense_id
        """
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(select_sql).fetchall()
        return rows


repo = SQLiteExpenseRepository(Path("data") / "expenses.db")
repo.init_db()

coffee_id = repo.add(
    NewExpense(
        title="Coffee beans",
        amount=18.50,
        category="Groceries",
        spent_on=date(2026, 1, 13),
        notes="Medium roast",
    )
)

bus_id = repo.add(
    NewExpense(
        title="Bus pass",
        amount=45.00,
        category="Transportation",
        spent_on=date(2026, 1, 14),
    )
)

print(f"Created expense IDs: {coffee_id}, {bus_id}")
for row in repo.list_all_rows():
    print(row)
```

### 7.1 Narration points while live coding

**Say:**
"Notice the patterns we are repeating.

- The SQL statement is a normal multi-line string.
- The values are a separate tuple.
- Dates are converted to strings at the database boundary.
- We use `lastrowid` to capture the generated primary key.
- Listing rows returns tuples because SQLite does not know about our dataclasses yet.

This is enough to prove the repository can store and retrieve real data."

### 7.2 Pause for output prediction

**Ask:**
"Before I run this, what do you expect the listed rows to look like? Will `spent_on` come back as a `date` object or a string?"

Wait for predictions.

**Say after running:**
"Exactly — the row contains stored database values, so `spent_on` comes back as a string for now. That is fine. Next hour we will teach the repository how to map rows back into objects."

---

## 8) Live Demo Part 2: Raw UPDATE and DELETE Examples (~10 minutes)

**Say:**
"The runbook for this hour includes CRUD, so I want you to see update and delete as well. We will keep them simple and raw for now. The point is the query pattern."

**Type and narrate:**

```python
def rename_expense(db_path: Path, expense_id: int, new_title: str) -> None:
    update_sql = """
    UPDATE expenses
    SET title = ?
    WHERE expense_id = ?
    """
    print(f"Updating expense_id={expense_id}")
    with sqlite3.connect(db_path) as connection:
        connection.execute(update_sql, (new_title, expense_id))


def delete_expense(db_path: Path, expense_id: int) -> None:
    delete_sql = "DELETE FROM expenses WHERE expense_id = ?"
    print(f"Deleting expense_id={expense_id}")
    with sqlite3.connect(db_path) as connection:
        connection.execute(delete_sql, (expense_id,))


rename_expense(Path("data") / "expenses.db", coffee_id, "Coffee beans - large bag")
for row in repo.list_all_rows():
    print(row)

delete_expense(Path("data") / "expenses.db", bus_id)
for row in repo.list_all_rows():
    print(row)
```

**Say:**
"There are two habits I want you to notice.

First, update and delete target the stable ID, not a descriptive field.

Second, during early development, it is smart to print or log the target ID before executing the write. That matches the runbook quality gate and makes it easier to catch mistakes before you accidentally update the wrong row."

### 8.1 Explain rowcount briefly

**Say:**
"A practical debugging trick is to inspect `cursor.rowcount` after an update or delete. If it is zero, that often means the target ID did not exist. We will use that signal more formally in the next hour when we add error handling and row mapping."

---

## 9) Common Pitfalls to Teach Explicitly

### 9.1 Forgetting commit

**Say:**
"One classic beginner mistake is forgetting to commit writes. In our examples, using `with sqlite3.connect(...) as connection:` helps because the connection context manager commits when the block exits successfully and rolls back if an exception occurs.

If you write code without that pattern, you may run an insert, close the program, and then wonder why your row is missing."

### 9.2 Path confusion

**Say:**
"Another classic issue is path confusion. SQLite happily creates a new database file if the path points somewhere else. That means a typo in the file path can result in a perfectly valid but totally wrong empty database.

This is why I strongly recommend printing `db_path.resolve()` during early development. If your query returns no data, first confirm you are looking at the file you think you are using."

### 9.3 Unsafe SQL habits

**Say:**
"The third major pitfall is building SQL with f-strings or string concatenation. Even if the code seems to work during a demo, it is not the right pattern. Build safe habits now."

### 9.4 Silent updates and deletes

**Say:**
"Finally, do not assume an update or delete worked just because no exception was raised. Check the target ID. Check `rowcount`. Re-query the table. Practical debugging beats wishful thinking."

---

## 10) Guided Practice: First SQLite Integration (~7 minutes)

**Say:**
"Now you will build the first working SQLite slice yourself. Stay close to the pattern we just used. The goal is not originality. The goal is correctness."

### 10.1 Practice prompt

Create a file that does the following:

1. Uses `Path("data") / "tracker.db"` or a similarly named database file.
2. Creates the parent directory if needed.
3. Creates a table for your main record using `CREATE TABLE IF NOT EXISTS`.
4. Implements `add()` using an `INSERT` statement with `?` placeholders.
5. Implements `list_all()` or `list_all_rows()` using `SELECT`.
6. Inserts at least two sample records and prints the results.

### 10.2 Constraints to read aloud

- Do **not** use string formatting to insert values into SQL.
- Use a context manager for each database operation.
- Print the resolved database path at least once.
- If your domain uses dates, convert them to strings on the way into the database.

### 10.3 Coaching prompts while learners work

- "Where is your commit happening?"
- "Which query uses a placeholder, and where are the parameter values passed?"
- "If the table already exists, will your startup still work?"
- "How will you verify you are writing to the correct database file?"

---

## 11) Checkpoint Discussion (~3 minutes)

**Ask:**

1. "What does the `?` placeholder do in `sqlite3`?"
2. "Why is `CREATE TABLE IF NOT EXISTS` a good startup habit?"
3. "What is the safest field to use in a `WHERE` clause for update and delete?"
4. "If your insert appears to work but no row is there later, what is one thing you should check immediately?"

### 11.1 Reinforcement answers

**Say:**
"A strong answer to the first question is: the placeholder keeps SQL structure separate from data values and lets the driver safely bind parameters.

A strong answer to the fourth question is: check whether the write was committed and confirm the database path is the file you expected."

---

## 12) Recap Script (~3 minutes)

**Say:**
"This hour turned our repository design into something real. We connected to an SQLite database file, created a table safely, inserted data with parameterized queries, listed rows back out, and looked at the basic shape of update and delete.

More importantly, we built safe habits:

- use `pathlib`
- use context managers
- use placeholders
- target stable IDs
- verify results instead of guessing

In the next hour, we will take the next architectural step: instead of returning raw row tuples, we will map rows back into dataclass objects so the rest of the application can continue speaking the language of the domain."

---

## 13) Exit Ticket

Ask learners to answer quickly in writing or verbally:

1. Why is parameterized SQL safer than f-string SQL?
2. What is one benefit of using a connection context manager?
3. If you run `SELECT` and get an empty result unexpectedly, what is one debugging step you would try first?

---

## 14) Optional Instructor Reference: Runnable End-of-Hour Example

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.db_path) as connection:
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
        with sqlite3.connect(self.db_path) as connection:
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

    def list_all_rows(self) -> list[tuple]:
        with sqlite3.connect(self.db_path) as connection:
            return connection.execute(
                """
                SELECT expense_id, title, amount, category, spent_on, notes
                FROM expenses
                ORDER BY expense_id
                """
            ).fetchall()


repo = SQLiteExpenseRepository(Path("data") / "expenses.db")
repo.init_db()
repo.add(NewExpense("Coffee", 4.75, "Food", date(2026, 1, 13)))
repo.add(NewExpense("Notebook", 8.99, "Office", date(2026, 1, 14), "Project ideas"))

for row in repo.list_all_rows():
    print(row)
```

---

## 15) Deepening the Teaching: Reading SQL as a Sentence

**Say:**
"One practical teaching move that helps learners enormously is to read SQL aloud as if it were a sentence. A lot of learners freeze because SQL looks like a foreign language, but it becomes far less intimidating when we narrate it plainly."

### 15.1 Model the reading process

**Put this on screen:**

```sql
SELECT expense_id, title, amount
FROM expenses
WHERE category = ?
ORDER BY expense_id
```

**Say:**
"I read that as:

- select the `expense_id`, `title`, and `amount` columns
- from the `expenses` table
- only for rows whose category matches a parameter value
- order the results by `expense_id`

That is all. SQL is often more readable than people expect once it is spaced and spoken clearly."

### 15.2 Connect SQL readability to debugging

**Say:**
"When a query is not working, read it line by line.

- Am I selecting the columns I think I am selecting?
- Am I querying the table I think I am querying?
- Is my `WHERE` clause correct?
- Did I pass the right number of parameters?
- Is the ordering or filter hiding what I expected to see?

That habit prevents the common beginner move of staring at the whole query as one giant blob."

---

## 16) Worked Example: Add a Search Query Safely

**Say:**
"The runbook lists search as an optional extension, and it is a good one because it reinforces placeholders and result inspection without introducing too much new complexity."

**Type and narrate:**

```python
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class NewExpense:
    title: str
    amount: float
    category: str
    spent_on: date
    notes: str | None = None


class SQLiteExpenseRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.db_path) as connection:
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
        with sqlite3.connect(self.db_path) as connection:
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

    def search_by_category(self, category: str) -> list[tuple]:
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(
                """
                SELECT expense_id, title, amount, category, spent_on, notes
                FROM expenses
                WHERE category = ?
                ORDER BY expense_id
                """,
                (category,),
            ).fetchall()
        return rows
```

**Say:**
"This is deliberately simple. We are not using `LIKE` yet. We are just reinforcing the exact pattern:

- keep SQL fixed
- pass values separately
- fetch rows
- inspect the result

If learners understand this version, adding a `LIKE ?` pattern later is much easier."

### 16.1 Prediction prompt

**Ask:**
"If I search for a category that does not exist, should this method return an exception or an empty list?"

Guide them toward: an empty list is often appropriate for search results.

**Say:**
"That distinction matters. Not every absence is an error. `get_by_id` missing a record may be exceptional. A search returning zero matches is often normal."

---

## 17) Debugging Walkthrough: Three Early sqlite3 Problems

### 17.1 Problem one: wrong number of parameters

**Say:**
"A very common `sqlite3` error is a mismatch between placeholders and provided values. For example:"

```python
sql = "INSERT INTO expenses (title, amount) VALUES (?, ?)"
values = ("Coffee",)
```

**Say:**
"That will fail because there are two placeholders and only one value.

The debugging approach is straightforward:

1. Count the placeholders.
2. Count the values in the tuple.
3. Confirm the order matches the SQL columns.

This sounds basic, but it solves a lot of real bugs."

### 17.2 Problem two: database path confusion

**Say:**
"Another common issue is accidentally creating a second empty database in a different directory.

The fix is practical, not magical:

- print `db_path.resolve()`
- confirm the directory exists
- confirm the file timestamp changes when you expect it to
- if necessary, temporarily print row counts after inserts

Do not debug invisible files by guesswork."

### 17.3 Problem three: forgetting to create the table first

**Say:**
"If learners see an error like 'no such table: expenses', the debugging question is not 'what obscure SQLite setting is wrong?' The first question is: did `init_db()` run before the insert? Did it run against the same database path?"

### 17.4 Encourage minimal reproducible checks

**Say:**
"When stuck, shrink the problem.

- connect
- run `SELECT 1`
- run `CREATE TABLE IF NOT EXISTS`
- run one insert
- run one select

If those four steps work, the core pipeline is alive. Then you can add your application logic back in."

---

## 18) Additional Guided Practice Option: CRUD Query Cards

If the group needs more repetition, put learners in pairs and assign each pair one query type.

### 18.1 Pair task

Each pair writes one query and explains it:

- Pair 1: `INSERT`
- Pair 2: `SELECT ... WHERE id = ?`
- Pair 3: `UPDATE ... WHERE id = ?`
- Pair 4: `DELETE ... WHERE id = ?`

Each pair must answer:

1. What values are parameters?
2. What should be returned or checked after execution?
3. What is one mistake a beginner might make with this query?

### 18.2 Debrief script

**Say:**
"When you explain a query to another person, you expose whether you truly understand the structure. If a learner can explain where the placeholders go and why the `WHERE` clause matters, they are building the right mental model."

---

## 19) Troubleshooting Script You Can Use Verbatim

**Say:**
"If your code is not behaving the way you expect, here is the debugging order I want you to use:

1. Confirm the database file path.
2. Confirm `init_db()` has run.
3. Print the SQL statement if necessary, but never by injecting values unsafely.
4. Confirm the parameter tuple has the right number of values.
5. Re-run the smallest possible query.
6. Query the table again after a write to verify the result.

That process is much stronger than random code changes."

---

## 20) Short Debrief Extension for Stronger Classes

If time allows, ask learners to compare these two repository method signatures:

```python
def list_all_rows(self) -> list[tuple]:
    ...
```

versus

```python
def list_all(self) -> list[Expense]:
    ...
```

**Ask:**
"Which one is easier for the rest of the application to use, and why?"

Let them answer briefly.

**Say:**
"That question points directly to the next hour. Today we proved the database integration works. Next we make the interface cleaner by converting storage rows back into model objects."
