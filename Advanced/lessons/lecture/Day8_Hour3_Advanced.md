# Day 8, Hour 3: Search, Filter, and Pagination Patterns
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Problem framing and user need: 5 minutes  
- Direct instruction on search and paging patterns: 15 minutes  
- Live demo with safe SQL: 10 minutes  
- Guided implementation sprint: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Add a practical search feature to a SQLite-backed application
2. Use parameterized `LIKE` queries safely
3. Explain the purpose of `LIMIT` and `OFFSET` in basic pagination
4. Keep search and pagination logic in the repository layer instead of scattering it across the app
5. Recognize common usability and correctness issues that appear when data sets grow

---

## Instructor Prep Notes

- Seed the database with enough records to make search meaningful
- Prepare examples with multiple categories and statuses so filters return noticeably different results
- Decide whether learners will expose search through the GUI, a small script, or both
- Keep pagination simple; learners do not need fully polished page controls to meet the hour goal

---

## Section 1: Why Search Matters (5 minutes)

### Opening Script

**[Instructor speaks:]**

An application stops feeling like a toy when users can actually find what they need. Up until now, many of our demos have involved tiny lists where we can just show all records. That works for ten rows. It stops working when the data grows. Search, filtering, and pagination are not glamorous features, but they are exactly the features that make users trust an application.

### The Real User Story

**[Instructor speaks:]**

Imagine a task tracker with 300 records. A user wants all items in the "billing" category that are still "open." They do not want to scroll forever. They do not want to visually inspect every row. They want the app to answer a question quickly and safely.

That is our design lens today. We are not adding search because it is on a feature checklist. We are adding search because it reduces friction for the user and creates better access patterns for larger data sets.

---

## Section 2: Core Search and Pagination Concepts (15 minutes)

### Safe Search with `LIKE`

**[Instructor speaks:]**

The first pattern we need is a parameterized `LIKE` query. In SQLite, `LIKE` lets us match partial strings. The mistake beginners often make is building SQL like this:

```python
query = f"SELECT * FROM records WHERE title LIKE '%{term}%'"
```

That is exactly what we do not want. Even in a course project, get learners in the habit of separating SQL structure from user-provided values.

Instead, do this:

```python
term = f"%{search_term.strip().lower()}%"
query = """
    SELECT id, title, category, status, priority, created_at
    FROM records
    WHERE lower(title) LIKE ?
       OR lower(category) LIKE ?
    ORDER BY id ASC
"""
rows = connection.execute(query, (term, term)).fetchall()
```

Point out two things:

1. The wildcard characters are added to the parameter value, not concatenated into the SQL string structure
2. We normalize case so the search feels more forgiving

### Filtering vs Searching

**[Instructor speaks:]**

It is helpful to distinguish these terms:

- Search usually means partial text matching
- Filter usually means narrow by an exact field or a constrained set of values

For example:

- Search: title contains "invoice"
- Filter: status equals "open"
- Filter: category equals "finance"

Combining them is normal. A clean repository method might accept both:

```python
def search(
    self,
    term: str = "",
    status: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[Record]:
    ...
```

### Why Pagination Exists

**[Instructor speaks:]**

Pagination exists because returning everything all the time is inefficient and unpleasant. When the data set grows, users should not have to render every row just to see the first screen of results. Pagination also gives the UI or API a predictable chunk size.

The simplest version uses:

- `LIMIT` for how many rows you want
- `OFFSET` for how many rows to skip

Example:

```sql
SELECT id, title, category, status, priority, created_at
FROM records
ORDER BY id ASC
LIMIT 20 OFFSET 40;
```

That means: give me 20 rows starting after the first 40.

### What "Practical" Means in This Course

**[Instructor speaks:]**

We are not building infinite scroll, cursor-based pagination, or a dynamic search ranking engine. We are keeping this practical:

- one search box
- maybe one status filter
- a small page size such as 10 or 20
- optional next and previous controls

That is enough to teach the pattern and improve the app.

---

## Section 3: Live Demo (10 minutes)

### Repository Search Method

**[Instructor speaks:]**

Let me show a repository method that stays readable and safe.

```python
import sqlite3
from contextlib import closing


def search(
    self,
    term: str = "",
    status: str | None = None,
    category: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[Record]:
    conditions = []
    parameters: list[object] = []

    if term.strip():
        wildcard = f"%{term.strip().lower()}%"
        conditions.append("(lower(title) LIKE ? OR lower(category) LIKE ?)")
        parameters.extend([wildcard, wildcard])

    if status:
        conditions.append("status = ?")
        parameters.append(status)

    if category:
        conditions.append("category = ?")
        parameters.append(category)

    where_clause = ""
    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    query = f"""
        SELECT id, title, category, status, priority, created_at
        FROM records
        {where_clause}
        ORDER BY id ASC
        LIMIT ? OFFSET ?
    """
    parameters.extend([limit, offset])

    with closing(sqlite3.connect(self.db_path)) as connection:
        rows = connection.execute(query, tuple(parameters)).fetchall()

    return [Record.from_row(row) for row in rows]
```

Narrate what matters:

**[Instructor speaks:]**

The SQL structure is still visible. The values remain parameterized. We only add conditions that are needed. The method returns model objects so the service and UI stay consistent.

### Optional UI Hook

Then show a tiny GUI or script hook:

```python
def on_search(self):
    term = self.search_var.get()
    status = self.status_var.get() or None
    category = self.category_var.get() or None
    self.current_offset = 0
    records = self.service.search_records(
        term=term, status=status, category=category, limit=20, offset=0
    )
    self.populate_table(records)


def on_next_page(self):
    self.current_offset += 20
    records = self.service.search_records(
        term=self.search_var.get(),
        status=self.status_var.get() or None,
        category=self.category_var.get() or None,
        limit=20,
        offset=self.current_offset,
    )
    self.populate_table(records)
```

Then caution learners:

**[Instructor speaks:]**

Notice that page state belongs in the UI layer, but query logic belongs in the service and repository layers. That separation keeps the design understandable.

### Demo Debrief

Ask:

**[Instructor speaks:]**

What would break if I moved the SQL into the button callback? The answer is not just "it would look messy." The deeper answer is that the logic would be harder to test, harder to reuse, and harder to expose later through an API.

---

## Section 4: Guided Implementation Sprint (25 minutes)

### Lab Brief

**[Instructor speaks:]**

Your mission is to make your app easier to use when the number of records grows. At minimum, add a search capability backed by the repository. If you have time, add a simple filter and next/previous paging.

### Minimum Success Criteria

Learners must:

1. Add a repository search method
2. Use parameterized SQL
3. Return correct results for at least one search scenario
4. Keep the logic outside the GUI callback or route handler

### Stronger Submission Criteria

If time allows, learners should also:

1. Add an exact-match status filter
2. Add `LIMIT` and `OFFSET`
3. Add a next/previous page pattern
4. Show a "no results" state clearly

### Suggested Lab Sequence

1. Start in the repository with a fixed search term hard-coded in a tiny script
2. Confirm the query returns the expected rows
3. Move the method into the service layer if needed
4. Connect the search term from the GUI or script input
5. Add pagination only after search works

This sequence reduces cognitive overload. Learners who attempt search, filter, paging, sorting, and UI polish all at once usually lose the thread.

### Coaching Prompts During Circulation

Ask questions like:

- What does this query return if the term is empty?
- Where are you adding the wildcard characters?
- What happens if there are zero matching results?
- How will the user know what page they are on?
- Are you ordering the results deterministically?

That last question is important. Pagination without deterministic ordering creates strange behavior. If page one and page two are based on an unstable order, users may see duplicates or missing rows.

### Common Bugs to Catch Early

- String-concatenated SQL with user input
- Search only checks one field when the learner intended multiple
- Offset increases forever without reset when a new search starts
- Previous page can go negative
- Empty term returns no rows when the learner expected "show all"
- UI does not clear stale rows before displaying new results

### Instructor Recovery Script for Overwhelmed Learners

**[Instructor speaks:]**

Let's reduce scope. First, search only by title. Then confirm it works. After that, search by title or category. Then, and only then, consider adding a filter. Pagination is optional until the core search path is correct.

### Stretch Extension

Advanced learners can add sorting:

**[Instructor speaks:]**

If you add sorting, do it carefully. Do not pass arbitrary column names directly from user input into SQL. Use a controlled mapping of allowed choices such as `"title"`, `"category"`, or `"status"`.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Search and pagination are great examples of features that look small on the surface but reveal the quality of your architecture. If your repository is clean, these features are straightforward. If your data access is tangled with the UI, these features become frustrating very quickly.

### Share-Out Questions

Invite learners to respond:

- What field did you search by?
- Did you add a filter, pagination, or both?
- Where did you keep your query logic?
- What bug did you hit that taught you something useful?

### Exit Ticket

1. Where should the `%` wildcard be added: the SQL string or the parameter value?
2. Why should paginated queries have a stable `ORDER BY`?
3. What should happen in the interface when a search returns zero rows?

### Transition to the Next Hour

**[Instructor speaks:]**

Next hour is Checkpoint 4. You will use everything from today and yesterday to demonstrate a genuine data-driven app: SQLite-backed CRUD, initialization, search, and architecture that still makes sense under pressure.

---

## Instructor-Ready Deep Dive: Search, Filters, and Paging Without Losing the Architecture

This section expands the hour into a near-verbatim instructor script. Use it when learners need a full demonstration of how search belongs in the repository while page state belongs in the interface or controller.

### Learning Outcomes Reinforcement

**[Instructor speaks:]**

By the end of this hour, you should be able to add search without smuggling SQL into the button callback. You should be able to add a filter without trusting user input as SQL structure. You should be able to explain `LIMIT` and `OFFSET` in plain language. Most importantly, you should be able to separate two different responsibilities: the repository knows how to query data, and the UI knows what page the user is currently viewing.

That last distinction is subtle but important. A repository method can accept `limit` and `offset`, but it should not know about a "Next" button or a text entry widget. The UI can remember that the current page is page 3, but it should not build the SQL string. When we keep those responsibilities separate, the same search can later be reused from a command-line script, a GUI, or a Flask route.

### Repository-Owned Safe Search

**[Instructor speaks:]**

Let's look at a complete, safe repository method. The user provides values: a text term, a status filter, and page information. The repository owns the query. The wildcard is part of the parameter value, not something we paste into the SQL structure with user text.

```python
from __future__ import annotations

import sqlite3
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Record:
    record_id: int
    title: str
    category: str
    status: str
    priority: int = 3
    created_at: str | None = None

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


class SQLiteRecordRepository:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def search(
        self,
        term: str = "",
        status: str | None = None,
        category: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Record]:
        if limit < 1 or limit > 100:
            raise ValueError("limit must be between 1 and 100")
        if offset < 0:
            raise ValueError("offset cannot be negative")

        conditions: list[str] = []
        parameters: list[object] = []

        clean_term = term.strip().lower()
        if clean_term:
            wildcard = f"%{clean_term}%"
            conditions.append(
                "(lower(title) LIKE ? OR lower(category) LIKE ?)"
            )
            parameters.extend([wildcard, wildcard])

        if status:
            conditions.append("status = ?")
            parameters.append(status)

        if category:
            conditions.append("category = ?")
            parameters.append(category)

        where_clause = ""
        if conditions:
            where_clause = "WHERE " + " AND ".join(conditions)

        query = f"""
            SELECT id, title, category, status, priority, created_at
            FROM records
            {where_clause}
            ORDER BY id ASC
            LIMIT ? OFFSET ?
        """
        parameters.extend([limit, offset])

        with closing(self._connect()) as connection:
            rows = connection.execute(query, tuple(parameters)).fetchall()

        return [Record.from_row(row) for row in rows]
```

**[Instructor speaks:]**

There is a small dynamic part here: we build a `WHERE` clause from known internal fragments. We are not inserting raw user input into the SQL structure. User-provided values still travel through placeholders. That is the rule I want you to remember: values are parameters. SQL structure is controlled by our code.

Also notice the deterministic `ORDER BY id ASC`. Pagination without a stable order is a bug waiting to happen. The database is allowed to return rows in different physical orders unless we tell it exactly how to order them. If page one and page two are not ordered consistently, users may see duplicates or miss records.

### Demo steps

Use these steps for the live demonstration:

1. Seed the database with at least 30 records. Include repeated statuses such as `open`, `blocked`, and `done`.
2. Show a plain list view first so learners understand the starting point.
3. Add a repository `search()` method that accepts `term`, optional `status` and `category` filters, `limit`, and `offset`.
4. Demonstrate a text search for a term that appears in several titles.
5. Demonstrate an exact status filter, such as `status="open"`.
6. Demonstrate search plus filter together.
7. Set `limit=5` and `offset=0`; show the first five matching rows.
8. Set `limit=5` and `offset=5`; show the next five matching rows.
9. Point to `ORDER BY id ASC` and explain why it is not optional for predictable pages.
10. Connect the method through the service layer.
11. Connect the service to the UI or script input.
12. Reset the UI offset to zero whenever the search term or filter changes.
13. Show a no-results state with a term that does not match anything.
14. Ask learners to identify which code owns query logic and which code owns current page state.

### Instructor narration for the safe SQL moment

**[Instructor speaks:]**

This is the sentence I want burned into your brain: do not put the user's text directly into the SQL string. If the user searches for `invoice`, `invoice` is a value. It belongs in the parameters. If we want partial matching, we build the wildcard parameter value in Python: `"%invoice%"`. The SQL still says `LIKE ?`.

Now compare that to this unsafe habit:

```python
query = f"SELECT * FROM records WHERE title LIKE '%{term}%'"
```

The danger is not only malicious input. The danger is also ordinary input that contains punctuation, quotes, or percent characters that behave differently than you expected. Parameterized queries give the database driver the job of treating the value as data.

### Keeping Page State Separate

**[Instructor speaks:]**

Here is a small service and UI-style controller example. The repository does the query. The controller remembers the current term, filters, and offset.

```python
class RecordService:
    def __init__(self, repo: SQLiteRecordRepository) -> None:
        self.repo = repo

    def search_records(
        self,
        term: str = "",
        status: str | None = None,
        category: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> list[Record]:
        return self.repo.search(
            term=term,
            status=status,
            category=category,
            limit=limit,
            offset=offset,
        )


class RecordSearchController:
    def __init__(self, service: RecordService) -> None:
        self.service = service
        self.term = ""
        self.status: str | None = None
        self.category: str | None = None
        self.page_size = 20
        self.offset = 0

    def new_search(
        self, term: str, status: str | None, category: str | None
    ) -> list[Record]:
        self.term = term
        self.status = status
        self.category = category
        self.offset = 0
        return self._load_current_page()

    def next_page(self) -> list[Record]:
        self.offset += self.page_size
        return self._load_current_page()

    def previous_page(self) -> list[Record]:
        self.offset = max(0, self.offset - self.page_size)
        return self._load_current_page()

    def _load_current_page(self) -> list[Record]:
        return self.service.search_records(
            term=self.term,
            status=self.status,
            category=self.category,
            limit=self.page_size,
            offset=self.offset,
        )
```

Point out that this controller could be a GUI class, a CLI helper, or a route helper. The principle is the same: page state is interface state; query execution is repository behavior.

## Lab prompt

**[Instructor speaks:]**

Your lab is to add practical search to your SQLite-backed app. Start with a repository method. Do not start with the button layout. The query must work before the interface can make it useful.

Minimum required work:

1. Add a repository search method that accepts a text term.
2. Use `LIKE ?` with the wildcard inside the parameter value.
3. Return model objects, not raw database rows, unless the rest of your app already uses dictionaries consistently.
4. Call the repository method through the service layer.
5. Connect the search to a GUI input, CLI prompt, or small script.
6. Show correct behavior when there are no matches.

Recommended additional work:

1. Add one exact-match filter such as status, then add category if your interface has a category selector.
2. Add `LIMIT` and `OFFSET`.
3. Reset the offset to zero when the search term or filter changes.
4. Add Previous and Next actions, keeping the previous page from going below offset zero.
5. Keep `ORDER BY` deterministic.

## Completion criteria

Learners meet the target for this hour when they can demonstrate:

- A search term returns the expected matching records.
- A filter narrows the result set when implemented.
- SQL uses placeholders for user-provided values.
- The wildcard for `LIKE` is added to the parameter value, such as `f"%{term}%"`.
- Paginated results use `LIMIT`, `OFFSET`, and a deterministic `ORDER BY`.
- The service or repository owns search behavior; the UI does not contain SQL.
- Page state such as current offset is reset when the user starts a new search.
- The app handles zero matching rows without showing stale results.

## Common pitfalls

Use these as active coaching checkpoints:

- **Unsafe SQL construction:** Learners build a query with an f-string containing user text. Redirect them to placeholders.
- **Wildcard in the wrong place:** Learners write `LIKE '%?%'`, which does not work as intended. The placeholder should represent the whole value, including `%`.
- **No stable ordering:** Learners paginate without `ORDER BY`, causing duplicate or missing rows between pages.
- **Offset not reset:** A learner searches on page 4, enters a new term, and sees no results because the old offset is still high.
- **Negative previous page:** Previous subtracts from offset without `max(0, ...)`.
- **UI owns SQL:** The button callback builds the database query. Move that logic into the repository.
- **Stale table rows:** The UI appends new results under old results instead of clearing first.
- **Over-building filters:** Learners try to build a full query builder. Keep the scope to one or two filters.

### Debugging Script for Search Bugs

**[Instructor speaks:]**

When search behaves strangely, isolate it. First call the repository directly with known values. If that fails, the problem is the query or data. If that works, call the service. If that works, the problem is probably in the UI state or display refresh. Debug from the data layer outward.

Here is a tiny manual check:

```python
repo = SQLiteRecordRepository(Path("data/tracker.db"))
results = repo.search(term="invoice", status="open", limit=5, offset=0)
for record in results:
    print(f"{record.record_id}: {record.title} [{record.status}]")
```

If this produces the correct rows, the SQL is not the first suspect anymore. Now look at the service call, selected status value, page offset, and table refresh code.

## Optional Extension

Offer these only after the core search works:

- Add a controlled sort option using a dictionary of allowed columns already present in the Day 8 schema, such as `{"title": "title ASC", "category": "category ASC", "priority": "priority DESC, id ASC", "created": "created_at DESC, id ASC"}`.
- Add a total-count method so the UI can display "Page 2 of 5."
- Add a "clear search" action that resets term, filter, and offset.
- Add an index on a commonly filtered column such as `status` after explaining that indexing is a performance topic, not a requirement for today's milestone.

If learners implement sorting, emphasize that values can be parameterized but column names cannot be passed as placeholders. Therefore, column names must come from a safe allow-list controlled by the program.

## Quick Check

Ask:

1. Where should the `%` wildcard be added: inside the SQL string or inside the parameter value?
2. Why should a paginated query include `ORDER BY`?
3. What should happen to `offset` when the user enters a new search term?
4. Why should SQL stay out of the UI callback?
5. What is the difference between a search term and an exact-match filter?

Expected answer themes: wildcard belongs in the parameter value; `ORDER BY` makes pages deterministic; offset resets to zero; SQL belongs in the repository for safety and reuse; search is partial text matching while filters narrow by specific fields.

## Facilitation Notes for a 60-Minute Delivery

This hour has a predictable trap: learners want to start with widgets. Redirect them to the repository. A search box that calls a broken query only creates a more confusing bug. The fastest path is repository first, service second, UI third.

For learners who move quickly, challenge them to explain the boundary rather than merely add features. Ask, **"Could your search work from a Flask route next week without rewriting the SQL?"** If the answer is yes, they are on the right path.

Close with this reminder:

**[Instructor speaks:]**

Search and pagination make the app feel useful, but the deeper lesson is ownership. The repository owns safe data access. The service owns application behavior. The interface owns user state. When those boundaries stay clear, new features are less frightening.

## Additional Instructor Script: Building Search One Layer at a Time

Use this block when learners are tempted to implement the whole feature at once.

**[Instructor speaks:]**

Search feels like a UI feature because the user experiences it through a search box. But implementation-wise, search is a data access feature first. If the repository cannot return the right records for a known term, a prettier search box will not help. So our build order is deliberate: repository, service, interface.

Let's rehearse that order.

First, in the repository, we prove the query:

```python
records = repo.search(term="invoice", status="open", limit=10, offset=0)
```

Second, in the service, we preserve the app's language:

```python
records = service.search_records(term="invoice", status="open", limit=10, offset=0)
```

Third, in the UI or CLI, we collect user state:

```python
term = search_box_value.strip()
status = selected_status or None
category = selected_category or None
records = service.search_records(
    term=term, status=status, category=category, limit=20, offset=0
)
```

Notice that only the last layer knows about the search box. Only the first layer knows SQL. The service connects the user intent to the data operation without becoming a database dumping ground.

### A Safe Sorting Aside

If learners ask about sorting, teach it as a controlled extension. Values can be parameters, but SQL identifiers such as column names cannot be parameterized with `?`. That means we never trust arbitrary user text as a column name.

Show this pattern:

```python
ALLOWED_SORTS = {
    "title": "title ASC, id ASC",
    "category": "category ASC, id ASC",
    "status": "status ASC, id ASC",
    "priority": "priority DESC, id ASC",
    "created": "created_at DESC, id ASC",
}

sort_clause = ALLOWED_SORTS.get(sort_choice, "id ASC")
query = f"""
    SELECT id, title, category, status, priority, created_at
    FROM records
    ORDER BY {sort_clause}
    LIMIT ? OFFSET ?
"""
```

Then say:

**[Instructor speaks:]**

This f-string is acceptable only because `sort_clause` comes from our own allow-list, not directly from the user. If `sort_choice` is invalid, we fall back to a safe default. That is the same design idea we used with filters: user choices are translated into program-controlled SQL fragments.

### Pagination Mental Model

**[Instructor speaks:]**

Here is a simple way to think about offset. If the page size is 20, then:

- page 1 starts at offset 0
- page 2 starts at offset 20
- page 3 starts at offset 40

The formula is:

```python
offset = (page_number - 1) * page_size
```

However, many beginner apps do not need to store a page number at all. They can store the current offset and add or subtract the page size. The important thing is to reset the offset when the search conditions change. A new term means a new result set. Page 4 of the old result set has no meaningful relationship to page 4 of the new result set.

### No-Results State Script

**[Instructor speaks:]**

Do not treat zero results as an error. Zero results is a valid answer to a search question. The interface should communicate it clearly. In a CLI, print "No matching records." In a GUI, clear the table and show a small label. What we must not do is leave the old rows visible, because then the user thinks the old rows are the search result.

Ask learners to test these four cases:

1. Empty term with no filter.
2. Term that matches several records.
3. Term plus status filter.
4. Term that matches nothing.

If all four behave predictably, the feature is much more trustworthy.

### Mini Whiteboard Check

Draw three boxes labeled UI State, Service Call, Repository Query. Ask the class where each item belongs:

- current offset
- selected status
- `LIKE ?`
- wildcard parameter
- table refresh
- row-to-object mapping
- no-results message
- deterministic `ORDER BY`

Expected placement: current offset, selected status, table refresh, and no-results message live in UI state or interface logic; the service call coordinates the request; `LIKE ?`, wildcard parameter creation, row mapping, and `ORDER BY` live in or near the repository query. If learners debate selected status, clarify that the selected value originates in the UI, but the repository receives it as a filter value.

### Final Reinforcement

**[Instructor speaks:]**

A search feature is successful when it is safe, predictable, and reusable. Safe means parameterized values. Predictable means deterministic order and clear page behavior. Reusable means the query is not trapped inside one button callback. That is the professional version of this feature.
