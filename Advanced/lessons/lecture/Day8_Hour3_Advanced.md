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
    SELECT id, title, category, status, priority
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
SELECT id, title, category, status
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
def search_records(
    self,
    term: str = "",
    status: str | None = None,
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

    where_clause = ""
    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    query = f"""
        SELECT id, title, category, status, priority
        FROM records
        {where_clause}
        ORDER BY id ASC
        LIMIT ? OFFSET ?
    """
    parameters.extend([limit, offset])

    with sqlite3.connect(self.db_path) as connection:
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
    self.current_offset = 0
    records = self.service.search_records(term=term, status=status, limit=20, offset=0)
    self.populate_table(records)


def on_next_page(self):
    self.current_offset += 20
    records = self.service.search_records(
        term=self.search_var.get(),
        status=self.status_var.get() or None,
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

If you add sorting, do it carefully. Do not pass arbitrary column names directly from user input into SQL. Use a controlled mapping of allowed choices such as `"title"`, `"created_at"`, or `"priority"`.

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

## Shared Day 8 Instructor Reference

Reuse the shared day-level instructor support from `Day8_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 8 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
