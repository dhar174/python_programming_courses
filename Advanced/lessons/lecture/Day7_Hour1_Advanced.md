# Day 7, Hour 1: From Objects to Tables — Schema Thinking + the Repository Idea (Course Hour 25)

## Instructor Notes

- **Course:** Python Programming (Advanced)
- **Session:** 7 (Hour 1 — Course Hour 25)
- **Runbook reference:** Session 7, Course Hour 25 – From objects to tables: schema thinking + repository idea
- **Duration:** 60 minutes
- **Mode:** Instructor-led + live coding + guided design lab
- **Audience:** Advanced Python learners who already have classes, service-layer logic, and basic file persistence experience

> **Instructor note:** This document is intentionally written as a read-aloud teaching guide. Your job this hour is not to turn learners into database administrators and not to jump ahead into ORM tooling. Keep the focus on a practical bridge: we already know how to model business concepts as Python objects, and now we need a reliable way to store those objects in a relational database. Emphasize schema thinking, stable IDs, the shape of CRUD operations, and the value of a repository as a boundary between business logic and SQL details. Learners should leave with a schema draft and a clean repository interface, even if the concrete SQLite implementation comes in the next hour.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain how a Python object maps to a database row and how object attributes map to table columns.

1. Explain how a Python object maps to a database row and how object attributes map to table columns.
2. Design a simple relational schema for a core domain object, including a primary key and sensible constraints.
3. Describe the CRUD operations your application will need before you write SQL.
4. Explain what a repository is and why it keeps your service layer cleaner.
5. Write a repository interface for a realistic domain model using modern Python type hints and dataclasses.
6. Make principled decisions about which fields are required, optional, or derived."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to prior work: objects, services, and the need for persistence
- **0:05–0:15** Schema thinking: moving from object attributes to table columns
- **0:15–0:25** Primary keys, data types, nullability, and practical constraints
- **0:25–0:35** CRUD planning before code
- **0:35–0:45** Repository idea: what it is, what it is not, and why it matters
- **0:45–0:55** Live design demo + repository interface walkthrough
- **0:55–1:00** Checkpoint, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file named `hour25_schema_design.py` for the live design portion.
- Have a second file ready named `hour25_repository_interface.py` in case you want to separate the dataclasses from the interface.
- Be ready to draw a simple table on the board or in a shared document with columns: `id`, `title`, `amount`, `category`, `spent_on`, `notes`.
- Be ready to compare two bad design choices:
  - using the title as the identifier
  - storing everything in one giant text blob
- Be ready to say out loud that we are **not** using an ORM today. You may mention ORMs briefly for contrast, but do not let the hour become a tooling survey.
- If possible, have a sample project tree visible:

```text
project/
├── data/
├── src/
│   ├── models.py
│   ├── services.py
│   └── repositories.py
└── tests/
```

**Say:** "Please keep your editor open and be ready to make design decisions before we write implementation code. Good database work starts with naming and structure, not with random SQL copied from memory."

---

## 3) Opening Script: Why We Need More Than In-Memory Objects (~5 minutes)

**Say:**
"Up to this point in the advanced course, we have spent a lot of time getting our Python objects and application structure into good shape. We designed classes from requirements. We added validation, custom exceptions, and service-layer methods. Some of you also built GUI workflows that create, update, and display records during a program run.

That is progress. But there is a problem. If the application closes, where does the data go?

If everything lives only in Python memory, it disappears when the process ends. That is fine for a quick demo, but it is not fine for a usable application. Real applications need persistence. They need data to survive across runs.

We already know one form of persistence: files. We can save JSON. We can write text. That is valuable and sometimes completely appropriate.

But once data becomes more structured and the application needs create, read, update, and delete workflows, databases become a better fit. A database gives us a durable place to store records, query them efficiently, and update specific rows instead of rewriting an entire file.

Today is the bridge from object thinking to table thinking. We are not abandoning good object design. We are extending it."

### 3.1 Frame the hour's core question

**Say:**
"The key question for this hour is this: if I already have a well-designed Python object, how do I store it in a table without turning my whole codebase into database soup?

That question has two parts:

1. How do I design the schema — the table, columns, types, and identifiers?
2. How do I isolate the storage details so my business logic is not full of SQL strings?

Those two parts lead us to schema thinking and the repository idea."

---

## 4) Schema Thinking: From One Object to One Row

### 4.1 Use a concrete domain model

**Say:**
"I want a domain model that is simple enough to reason about but realistic enough to feel like application code. We will use an expense tracker example. Even if your capstone is not an expense tracker, the ideas transfer directly to inventory items, tasks, contacts, notes, or bookings."

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
"Pause and notice what these classes communicate.

- `NewExpense` represents data before the database assigns an ID.
- `Expense` represents a persisted record that already has a stable primary key.
- We are using `dataclass` because these are data-carrying objects.
- We are using type hints because clarity matters and static tools can help us.
- We are using `date` for the domain model because a spending date is conceptually a date, not just a string.

Now let's translate that into database terms."

### 4.2 Show the mapping explicitly

**Say while drawing or listing on screen:**

| Python concept | Database concept |
| --- | --- |
| `Expense` object | one row in a table |
| `expenses` collection | table |
| `expense_id` attribute | primary key column |
| `title`, `amount`, `category`, `spent_on`, `notes` | regular columns |
| `list[Expense]` returned by the app | result set returned by a query |

**Say:**
"A relational table is not some mystical new world. In many beginner-friendly cases, a row is just a stored record, and a record is very close to an object.

The one place where people get tripped up is this: the database does not store Python objects directly. It stores scalar values in columns. So our job is to decide how each attribute should be represented in the table."

### 4.3 Ask learners to map fields

**Ask:**
"If `title` in Python is a string, what should it become in SQLite?"

Wait for: `TEXT`.

**Ask:**
"If `amount` is a Python float, what is the natural SQLite type?"

Wait for: `REAL`.

**Ask:**
"If `spent_on` is a Python `date`, what are our options?"

Guide them toward: store it as ISO text, or as an integer timestamp, or use adapters. Then say:

**Say:**
"For this course, the most readable choice is usually ISO-formatted text, like `2026-01-13`. It is easy to inspect, sort, and debug. So our domain model uses `date`, but our table will likely store `spent_on` as `TEXT`. That is a normal and healthy boundary conversion."

---

## 5) Table Design: Columns, Primary Keys, and Constraints

### 5.1 Draft the schema together

**Type and narrate:**

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

**Say:**
"This is a first draft, not holy scripture. But it is already telling a strong story.

- `expense_id` is the primary key.
- The fields our application requires are marked `NOT NULL`.
- `notes` is optional, so it can be null.
- The schema reflects the structure of our domain object.

Now let me explain the design decisions, because copying SQL without understanding the decisions is how bugs get baked in."

### 5.2 Why a stable primary key matters

**Say:**
"The most important column in the table is the primary key.

A primary key gives every row a stable identity. Without that, update and delete operations become fragile. If we try to update rows by title, what happens when two expenses are both called `Lunch`? If we delete by amount, what happens when several purchases cost `12.50`? We need a field whose job is identity.

That is why `INTEGER PRIMARY KEY` is such a common and practical choice in SQLite. It is stable. It is simple. It is efficient. The database can generate it for us.

In some applications, a text ID is appropriate — for example, a UUID or a business-defined code. But the rule is the same: every row needs a stable, unique identity, and update/delete operations should target that identity."

### 5.3 Required versus optional fields

**Say:**
"A schema also forces us to be explicit about what is truly required.

This is a design strength, not a nuisance. When you create a table, you have to decide:

- Is `title` required? Usually yes.
- Is `amount` required? Absolutely.
- Is `category` required? In our example, yes, because categorization matters.
- Is `notes` required? Probably not.

This is the same kind of thinking we already used when designing dataclasses and validation rules. A good schema mirrors business rules."

### 5.4 Explain data integrity at the design level

**Say:**
"At the table level, constraints protect data quality. Today we are keeping constraints practical and light. You have already seen `NOT NULL`. Later we may add checks like `amount >= 0` or foreign keys that connect one table to another.

What matters now is the mindset: if a value must be present or must follow a rule, the database can help enforce that. Databases are not just storage boxes. They are also guardians of structural integrity."

---

## 6) CRUD Planning Before SQL

### 6.1 Name the operations first

**Say:**
"Before we implement anything, I want us to name the operations the application needs. This is a very practical design habit. If you know the workflows, you can design the repository around them.

CRUD stands for:

- **Create**: add a new record
- **Read**: fetch one record or many records
- **Update**: change an existing record
- **Delete**: remove a record

For our expense tracker, the first version probably needs these operations:

1. Add a new expense
2. List all expenses
3. Get one expense by ID
4. Update an expense by ID
5. Delete an expense by ID

Maybe later we add search by category or date range, but these five are the baseline."

### 6.2 Connect CRUD to real user actions

**Say:**
"Do not think of CRUD as a database vocabulary quiz. Think of it as user intent.

- When a user submits a form, that is usually Create.
- When a UI screen loads records, that is usually Read.
- When a user edits a record and clicks Save, that is usually Update.
- When a user confirms removal, that is Delete.

This matters because it keeps database design tied to actual application behavior."

### 6.3 Remind learners of the quality gate

**Say:**
"From the runbook, there are four quality rules I want you to start internalizing right now:

1. All SQL should use parameter placeholders — question marks in SQLite — not string concatenation.
2. Writes must be committed, either explicitly or via a connection context manager.
3. Every table needs a stable primary key.
4. Update and delete operations should target IDs.

We are not running SQL yet in this hour, but these quality gates shape the design."

---

## 7) The Repository Idea

### 7.1 Give a plain-language definition

**Say:**
"A repository is a layer whose job is to store and retrieve domain objects.

That is the plain-English definition.

A repository sits between your service layer and the database. Your service logic says things like:

- add this expense
- get expense 42
- update this record
- delete that record

The repository knows how to turn those requests into SQL and how to turn database rows back into domain objects."

### 7.2 Why not call sqlite3 everywhere?

**Say:**
"A common early mistake is to scatter database code all over the application. A GUI callback opens a connection. A service function runs a query directly. Another file builds SQL with f-strings. Another deletes a record in a totally different style.

That approach works for about ten minutes and then becomes painful.

The repository helps because it centralizes persistence logic. It gives us:

- one place to change SQL
- one place to handle row mapping
- one place to manage connection details
- cleaner service methods
- easier testing, because you can replace the concrete repository with a fake or mock

So the repository is not magic. It is a boundary. It is an organizational decision that keeps responsibilities separated."

### 7.3 What the repository is not

**Say:**
"A repository is not the same thing as an ORM.

An ORM, or object-relational mapper, is a framework that automatically maps objects to tables and often generates SQL for you. Tools like SQLAlchemy can be useful, but today we are staying closer to the metal so you understand what is happening.

We are writing plain Python and plain SQLite queries. The repository pattern is the design idea. SQLite is the storage technology. An ORM is optional tooling that can come later."

### 7.4 Explain dependency direction

**Say:**
"In a well-structured application, the service layer should depend on a repository interface, not on hard-coded SQLite details.

That means the service layer can say, 'I need something that can add and fetch expenses.' It does not need to know if the data is stored in SQLite, JSON, memory, or something else.

That is a powerful design idea because it keeps your code flexible without making it abstract for the sake of abstraction."

---

## 8) Live Coding Demo: Dataclasses + Repository Interface (~10 minutes)

**Say:**
"Now I am going to write the shape of the persistence boundary before I write the persistence code itself. This is a very intentional design move."

**Type and narrate:**

```python
from __future__ import annotations

from abc import ABC, abstractmethod
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


@dataclass(slots=True)
class Expense(NewExpense):
    expense_id: int


class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense: NewExpense) -> int:
        """Store a new expense and return its generated ID."""

    @abstractmethod
    def get_by_id(self, expense_id: int) -> Expense:
        """Return one stored expense or raise if it is missing."""

    @abstractmethod
    def list_all(self) -> list[Expense]:
        """Return all stored expenses, usually ordered by ID."""

    @abstractmethod
    def update(self, expense: Expense) -> None:
        """Persist changes to an existing expense."""

    @abstractmethod
    def delete(self, expense_id: int) -> None:
        """Remove an expense by stable ID."""


@dataclass(slots=True)
class AppPaths:
    project_root: Path

    @property
    def data_dir(self) -> Path:
        return self.project_root / "data"

    @property
    def database_file(self) -> Path:
        return self.data_dir / "expenses.db"
```

**Say:**
"There are several useful design choices here.

First, the repository interface speaks in domain terms, not SQL terms. The caller asks for `Expense` objects, not rows and cursors.

Second, the methods align directly with CRUD.

Third, we distinguish between a new expense and a persisted expense. That prevents awkward code like passing `None` around as a pretend ID unless we truly want to.

Fourth, notice that I already brought in `pathlib.Path` through `AppPaths`. We are not even connecting to the database yet, but we are designing the file location in a modern, readable way.

This is what good software design looks like: even the boundaries are explicit."

### 8.1 Show how the service layer would use the interface

**Type:**

```python
class ExpenseService:
    def __init__(self, repository: ExpenseRepository) -> None:
        self.repository = repository

    def record_expense(self, expense: NewExpense) -> int:
        if expense.amount <= 0:
            raise ValueError("amount must be positive")
        return self.repository.add(expense)
```

**Say:**
"Notice what the service does not do. It does not open a database file. It does not build SQL. It does not know about cursors.

That is exactly the point. The service layer focuses on business rules. The repository handles persistence. Separation of concerns is not just a slogan. It produces cleaner code."

---

## 9) Design Walkthrough: Turning the Model into a Table Plan

### 9.1 Build a schema decision table with learners

**Say:**
"When you design a table, ask the same questions for every field."

| Field | Python type | SQLite storage choice | Required? | Notes |
| --- | --- | --- | --- | --- |
| `expense_id` | `int` | `INTEGER PRIMARY KEY` | yes | database-generated identity |
| `title` | `str` | `TEXT` | yes | short human-readable label |
| `amount` | `float` | `REAL` | yes | practical for this course |
| `category` | `str` | `TEXT` | yes | could later become related table |
| `spent_on` | `date` | `TEXT` | yes | store as ISO format |
| `notes` | `str | None` | `TEXT` | no | optional free text |

**Say:**
"This little table is valuable. It exposes assumptions before code gets written. If learners can produce a table like this for their own project, they are doing strong engineering work."

### 9.2 Mention derived and nested data

**Say:**
"Two design warnings before we move to practice.

First, not every property on an object should automatically become a stored column. Some values are **derived**. If you can calculate them from other stored values, maybe you do not need to store them.

Second, nested objects require a plan. If your object contains a list or another custom object, do not just panic and turn the whole thing into one text blob. Stop and think. Should this be another table? Should it be serialized? Should the model be simplified?

The runbook warns us specifically about trying to store nested objects without a plan. That warning is there because it is a very common trap."

---

## 10) Guided Practice: Schema Draft + Repository Contract (~10 minutes)

**Say:**
"Now it is your turn. I want you to do two things.

1. Draft the schema for your main application record.
2. Draft a repository interface with CRUD method stubs.

If you are following along with the expense example, use that. If you already have a capstone domain, use your own domain model."

### 10.1 Prompt to display or read aloud

**Guided Practice Prompt**

Create a short design document or Python file that includes:

1. A domain dataclass for a new record and a persisted record.
2. A table plan with field names, SQLite types, and whether each field is required.
3. A repository interface with at least these methods:
   - `add(...) -> int`
   - `get_by_id(...) -> ...`
   - `list_all() -> list[...]`
   - `update(...) -> None`
   - `delete(...) -> None`
4. One sentence explaining why you chose your primary key.

### 10.2 Coaching notes while learners work

- If a learner wants to use a name or title as the primary key, ask: "What happens if two rows share the same name?"
- If a learner stores dates as custom objects in the schema draft, ask: "What is the database actually storing on disk?"
- If a learner tries to mix service rules and repository methods together, ask: "Which layer should know business policy, and which should know storage mechanics?"
- If a learner is overcomplicating the design with ten tables, remind them: "One strong table is better than five speculative tables you do not yet need."

---

## 11) Checkpoint Discussion (~5 minutes)

**Ask these questions aloud:**

1. "Why is a stable primary key more trustworthy than updating by title or amount?"
2. "What is the relationship between a Python object and a database row?"
3. "Why does the repository return domain objects instead of raw SQL cursors?"
4. "What is one field in your design that should be optional, and why?"
5. "What is one field that should definitely be `NOT NULL`, and why?"

### 11.1 Ideal answers to reinforce

**Say:**
"A strong answer to the first question sounds like this: a stable primary key gives each row unique identity, so update and delete operations are precise and do not rely on changeable or duplicate business data.

A strong answer to the repository question sounds like this: the repository keeps database details isolated so the rest of the app can work in terms of domain concepts rather than SQL mechanics."

---

## 12) Recap Script (~3 minutes)

**Say:**
"Let's close the hour by naming what we accomplished.

We started with a Python object model and translated it into table language. We identified columns, types, nullability, and the need for a stable primary key. We named the CRUD operations the application needs. Then we introduced the repository as a boundary that keeps SQL details out of higher-level business logic.

That is the conceptual foundation for the next several hours. In the next hour, we will take this design and connect it to a real SQLite database using the standard library `sqlite3` module. We will create the database file, create the table, and run parameterized queries safely.

If today felt less flashy than a demo-heavy hour, that is okay. Good persistence code begins with good thinking. Schema design is part of programming, not paperwork."

---

## 13) Exit Ticket

**Prompt learners to answer in one or two sentences:**

1. Why is a repository useful even in a small project?
2. Which field in your schema is your primary key, and why did you choose it?
3. Which one of your fields is optional, and what made you decide that?

---

## 14) Optional Instructor Reference: Minimal Complete Design Example

Use this if you want a single, clean example to leave on screen at the end of the hour.

```python
from __future__ import annotations

from abc import ABC, abstractmethod
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


@dataclass(slots=True)
class Expense(NewExpense):
    expense_id: int


class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense: NewExpense) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, expense_id: int) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> list[Expense]:
        raise NotImplementedError

    @abstractmethod
    def update(self, expense: Expense) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, expense_id: int) -> None:
        raise NotImplementedError


@dataclass(slots=True)
class AppPaths:
    root: Path

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def db_path(self) -> Path:
        return self.data_dir / "expenses.db"
```

**Suggested closing sentence:**
"If you can explain this file clearly, you are ready for the first SQLite implementation." 

---

## 15) Additional Instructor Talking Points: How to Coach Schema Decisions in Real Time

**Say:**
"I want to give you a few extra schema-design questions that professional developers ask all the time. When learners get stuck, these questions help them move from vague object thinking to precise table thinking."

### 15.1 Question set to model aloud

**Say:**
"For each field, ask:

- What is this field's job?
- Is it identity, description, classification, or optional context?
- Should it always be present?
- Can it change later?
- Will users search or update by this field?
- Is it a primitive value, or is it secretly another entity hiding inside the object?

If learners start answering those questions well, their schema quality improves immediately."

### 15.2 Example coaching conversation

**Say:**
"Imagine a learner has a task tracker object with fields like `title`, `status`, `assigned_to`, and `comments`.

I might ask:

- Is `title` identity? No. It is descriptive.
- Can two tasks have the same title? Yes. Then it should not be the primary key.
- Is `assigned_to` just a string for now, or is it really a user entity? If it is just a string today, that is fine. If users become their own table later, we can redesign deliberately.
- Are `comments` a single text field, or is this actually a one-to-many relationship? If each task can have many comments, one comments text blob may be a temporary shortcut, but it is good to name that tradeoff honestly.

This kind of conversation teaches design judgment, not just syntax."

### 15.3 Remind learners that version one can be simple

**Say:**
"There is another important coaching point here: version one does not need to model the whole universe.

A lot of advanced learners become ambitious and try to predict every future feature before writing a single table. That usually leads to complexity that has not earned its place yet.

A simpler rule is this:

- model the core record well
- give it a stable ID
- make required data required
- keep optional data clearly optional
- and leave room to extend later

That is not under-designing. That is responsible scoping."

---

## 16) Suggested Whiteboard Sequence for the Hour

If you prefer to structure this hour visually, here is a reliable sequence.

1. Draw one Python object with labeled attributes.
2. Draw one table row with labeled columns.
3. Draw a primary-key badge next to the ID column.
4. List the five CRUD operations in plain English.
5. Draw a box labeled `Service Layer` and another labeled `Repository`.
6. Draw an arrow from service to repository, and a separate arrow from repository to database.

**Say:**
"The visual story is simple: business logic talks to repositories, repositories talk to tables, and the model is translated across that boundary. If you teach that picture clearly, learners are much less likely to dump SQL into random parts of the application."

---

## 17) Optional Mini-Challenge for Fast Finishers

**Prompt:**

Take the expense schema from this hour and propose one realistic extension, but do it carefully.

Choose one:

1. Add a `merchant` column.
2. Add a `payment_method` column.
3. Add a separate `categories` table and explain what foreign key you would eventually need.

For whichever option you choose, answer these questions:

- Why does this field or table exist?
- Is it required or optional?
- Would it change the repository interface right away?
- Would the service layer need any new validation?

**Instructor debrief note:** Fast finishers often want to jump straight into coding. Make them explain the design implications first. That keeps the extension aligned with the learning target instead of turning into feature sprawl.
