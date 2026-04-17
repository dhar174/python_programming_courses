# Advanced Day 8 — Session 8 (Hours 29–32)
Python Programming (Advanced) • Data-Driven App Integration and Checkpoint 4

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 8 overview (Hours 29–32); Advanced/lessons/lecture/Day8_Hour1_Advanced.md — Instructor Prep Notes -->

---

# Session 8 Overview

## Topics Covered Today
- Hour 29: Deeper SQL practice, with ORM exposure as an optional extension
- Hour 30: Plug the SQLite repository into the app
- Hour 31: Search/filter + pagination patterns
- Hour 32: Checkpoint 4 data-driven app milestone

## Day goal
- Make SQLite the actual source of truth
- Add practical search
- Prove persistence end to end

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Session 8 overview (Hours 29–32); Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Opening Script -->

---

## Homework + Quiz Emphasis

- Default to deeper SQL practice for the required build path
- Treat ORM as optional exposure, not mandatory scope
- Keep the service contract stable during the storage swap
- Apply stable ordering before slicing pages
- Prove persistence-backed behavior at the checkpoint

### Canonical quiz/contracts to recognize
- `Hour 29 | chosen path: deeper SQL practice`
- `Hour 30 | repository plugged in: yes`
- `Hour 31 | search term: report`
- `Hour 32 | db path: data/tracker.db`

<!-- Sources: Advanced/assignments/Advanced_Day8_homework.ipynb — Part 1 through Part 4; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 29 through Hour 32 canonical contract questions -->

---

# Hour 29: Deeper SQL Practice First, ORM Optional

## Learning Outcomes
- Explain what an ORM does in plain language
- Compare ORM convenience vs SQL transparency
- Implement one practical extension safely
- Stay within the course scope

### Default class path
- **Required**: deeper SQL practice
- **Optional extension**: tiny SQLAlchemy slice if the environment supports it

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 29: Optional ORM slice (SQLAlchemy) OR deeper SQL practice; Advanced/assignments/Advanced_Day8_homework.ipynb — Part 1: Hour 29 - Deeper SQL practice (required) with ORM as an optional extension; Advanced/lessons/lecture/Day8_Hour1_Advanced.md — Learning Outcomes for This Hour -->

---

## The Real Tradeoff

### ORM advantages
- Less repetitive mapping code
- Object-style query API
- Useful abstraction for common patterns

### ORM disadvantages
- Extra dependency
- More abstraction to debug
- Hidden SQL can slow learning if the basics are still shaky

### SQL advantages
- Transparent
- Portable
- Great for small apps and practical summaries

<!-- Sources: Advanced/lessons/lecture/Day8_Hour1_Advanced.md — What an ORM Does; What Raw SQL Gives You; The Real Comparison -->

---

## Demo Path A vs Path B

### Path A — tiny ORM exposure
- One model class
- One session
- One query

### Path B — deeper SQL practice
- `GROUP BY`
- `COUNT(*)`
- Summary queries that answer real app questions

**Recommendation**: finish one path well; do not split your hour in half and complete neither.

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab (choose one); Advanced/lessons/lecture/Day8_Hour1_Advanced.md — Message to Learners; Live Demo -->

---

## Demo: SQL Summary Query

```python
def summarize_by_status(db_path: str) -> list[tuple[str, int]]:
    query = """
        SELECT status, COUNT(*) AS total
        FROM records
        GROUP BY status
        ORDER BY total DESC, status ASC
    """
```

### Why this path fits today
- No extra package install
- Learners still see real SQL
- The database answers the question directly

<!-- Sources: Advanced/lessons/lecture/Day8_Hour1_Advanced.md — Demo Track B: Deeper SQL Practice -->

---

## Lab: Choose One Depth Path

**Time: 25–35 minutes**

### Required baseline
- Complete the deeper SQL path first
- Add one safe summary or reporting query
- Explain one ORM tradeoff even if you stay with SQL

### Completion Criteria
✓ One path completed cleanly  
✓ Tradeoffs explained at a high level  
✓ Query or ORM slice remains small and readable  
✓ App stability is preserved

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Completion criteria (Hour 29); Advanced/assignments/Advanced_Day8_homework.ipynb — Part 1: Hour 29 -->

---

## Common Pitfalls (Hour 29)

⚠️ Adding ORM complexity before understanding the query shape  
⚠️ Switching approaches midstream  
⚠️ Treating “more abstraction” as “automatically better”  
⚠️ Letting this hour derail the milestone path

## Quick Check
**Question**: What is one advantage and one disadvantage of an ORM?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 29 explanation -->

---

# Hour 30: Integrate the DB into the App

## Learning Outcomes
- Swap storage without rewriting the whole app
- Keep the service contract stable
- Use beginner-friendly dependency injection
- Avoid two conflicting sources of truth

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 30: Integrate DB into the app; Advanced/lessons/lecture/Day8_Hour2_Advanced.md — Learning Outcomes for This Hour -->

---

## Same Service Contract, New Storage Engine

### Stable pieces
- Model classes
- Validation logic
- Service method names
- UI callbacks / routes

### Pieces that change
- Repository implementation
- SQL statements
- Row mapping
- `init_db()` and connection setup

> The service should depend on what the repo can do, not how it stores data.

<!-- Sources: Advanced/lessons/lecture/Day8_Hour2_Advanced.md — The One Big Idea; What Should Stay Stable -->

---

## Beginner-Friendly Dependency Injection

```python
repo = SQLiteTrackerRepository("data/tracker.db")
service = TrackerService(repo=repo)
```

### Avoid
```python
class TrackerService:
    def __init__(self):
        self.repo = SQLiteTrackerRepository("data/tracker.db")
```

### Why
- Easier to test
- Easier to swap storage
- Cleaner architecture

<!-- Sources: Advanced/lessons/lecture/Day8_Hour2_Advanced.md — Dependency Injection Without the Jargon Overload -->

---

## One Source of Truth

### Once SQLite is live
- SQLite is the live persistence layer
- JSON can become export/import, not parallel truth

### Danger pattern
- GUI writes to JSON
- Search reads from SQLite
- Nobody knows which state is current

**Quiz/homework cue**: `Hour 30 | repository plugged in: yes`

<!-- Sources: Advanced/assignments/Advanced_Day8_homework.ipynb — Part 2: Hour 30; Advanced/lessons/lecture/Day8_Hour2_Advanced.md — The Risk of Two Sources of Truth; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 30 canonical contract -->

---

## Demo: Storage Swap With Minimal Drama

### Demo flow
1. Build the repo
2. Call `repo.init_db()`
3. Construct the service with that repo
4. Launch the app
5. Show that add/list/update/delete still work
6. Restart and verify persistence

### Success condition
- UI changes very little
- Storage changes a lot

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: service = TrackerService(repo=SQLiteRepo(...)); Show UI still works after swap; Advanced/lessons/lecture/Day8_Hour2_Advanced.md — Live Demo of the Storage Swap -->

---

## Lab: Wire the Repository Under the Service

**Time: 25–35 minutes**

### Tasks
- Replace JSON/in-memory persistence with SQLite
- Keep the service layer interface stable
- Confirm CRUD works after the swap
- Remove confusion about live storage

### Completion Criteria
✓ App persists via SQLite  
✓ UI/API still functions  
✓ One source of truth is clear  
✓ Restart behavior is verified

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Wire it up; Advanced/assignments/Advanced_Day8_homework.ipynb — Part 2: Hour 30 -->

---

## Common Pitfalls (Hour 30)

⚠️ UI calling `sqlite3` directly  
⚠️ JSON and SQLite both acting “live”  
⚠️ Forgetting to refresh after DB writes  
⚠️ Rebuilding more layers than necessary

## Quick Check
**Question**: What interface stayed the same when you swapped storage?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 30 explanation -->

---

# Hour 31: Search, Filter, and Pagination

## Learning Outcomes
- Add a practical search feature
- Use parameterized `LIKE` safely
- Understand `LIMIT` and `OFFSET`
- Keep paging logic in the repository layer
- Preserve stable ordering across pages

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 31: Search/filter + pagination patterns; Advanced/lessons/lecture/Day8_Hour3_Advanced.md — Learning Outcomes for This Hour -->

---

## Search vs Filter

### Search
- Partial text match
- e.g. title contains `"invoice"`

### Filter
- Narrow by exact or controlled value
- e.g. status equals `"open"`

### Practical method shape
```python
def search(term: str = "", status: str | None = None,
           limit: int = 20, offset: int = 0) -> list[Record]:
    ...
```

<!-- Sources: Advanced/lessons/lecture/Day8_Hour3_Advanced.md — Filtering vs Searching -->

---

## Safe `LIKE` + Stable Pagination

```python
wildcard = f"%{term.strip().lower()}%"
query = """
    SELECT id, title, category, status
    FROM records
    WHERE lower(title) LIKE ?
    ORDER BY id ASC
    LIMIT ? OFFSET ?
"""
```

### Rules to keep
- Add `%` to the **parameter value**
- Normalize case for a friendlier search
- Sort before paginating

**Quiz/homework cue**: `Hour 31 | search term: report`

<!-- Sources: Advanced/lessons/lecture/Day8_Hour3_Advanced.md — Safe Search with `LIKE`; Why Pagination Exists; Advanced/assignments/Advanced_Day8_homework.ipynb — Part 3: Hour 31; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 31 canonical contract -->

---

## Demo: Search Repository + Optional UI Hook

### Demo flow
- Add `search_records(term, status, limit, offset)`
- Reset page to zero on a new search
- Add optional Next/Prev buttons
- Repopulate the visible table from fresh results

### Usability guardrails
- Empty result sets are valid
- Clear stale rows before repopulating
- Do not hand-build SQL with user values

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Demo: repo.search(q, limit, offset); Demo: next/prev buttons in UI (optional); Advanced/lessons/lecture/Day8_Hour3_Advanced.md — Live Demo -->

---

## Lab: Practical Search Feature

**Time: 25–35 minutes**

### Tasks
- Add a search box or script input
- Implement a repository search method
- Optional: add paging with limit 20 and Next/Prev
- Keep results predictable with stable ordering

### Completion Criteria
✓ Search returns correct results  
✓ No SQL injection risk  
✓ Paging does not reorder records unpredictably  
✓ Empty search results behave cleanly

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Lab: Search feature; Advanced/assignments/Advanced_Day8_homework.ipynb — Part 3: Hour 31 -->

---

## Common Pitfalls (Hour 31)

⚠️ Building SQL with string concatenation  
⚠️ Forgetting wildcards in `LIKE`  
⚠️ Paginating unsorted results  
⚠️ Leaving stale UI rows after search

## Quick Check
**Question**: Where should wildcard `%` be added: in the SQL string or the parameter value?

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Common pitfalls to watch for / Quick check; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 31 explanation -->

---

# Hour 32: Checkpoint 4 — Data-Driven App Milestone

## Required deliverables
- SQLite repo with CRUD
- `init_db()` on startup
- Database as source of truth
- Basic search feature
- Demo proving persistence across restarts

<!-- Sources: Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md — Hour 32: Checkpoint 4: Data-driven app milestone; Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Clarify the Deliverables -->

---

## Fast-Grade Demo Workflow

1. Launch the app
2. Create a record
3. Search for it
4. Close the app
5. Reopen the app
6. Confirm the record still exists
7. Update it
8. Delete it

### Why this works
- It reveals path issues fast
- It reveals stale in-memory state fast
- It proves SQLite is really live

<!-- Sources: Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Show the Fast-Grade Workflow -->

---

## Validation Checklist

```text
[ ] Database file exists in the expected path
[ ] init_db runs safely on startup
[ ] Add creates a new row in SQLite
[ ] List reads from SQLite, not stale in-memory data
[ ] Search returns expected results
[ ] Update targets the correct record ID
[ ] Delete removes the intended record
[ ] Restart proves persistence
[ ] Common errors do not crash the app
```

**Quiz/homework cue**: `Hour 32 | db path: data/tracker.db`

<!-- Sources: Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Validation Checklist for Learners; Advanced/quizzes/Advanced_Day8_Quiz.html — Hour 32 canonical contract -->

---

## Common Failure Modes to Triage

### Data disappears after restart
- Check commit behavior
- Check DB path
- Check whether the UI still reads cached objects

### Wrong record changes
- Print the target ID
- Verify the `WHERE` clause
- Check stale selected state

### Search returns odd results
- Test the repo method by itself first
- Check wildcard placement
- Check row clearing in the UI

<!-- Sources: Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Coaching Notes for Common Failure Modes -->

---

# Session 8 Wrap-Up

## What Success Looks Like
- SQLite is now the real source of truth
- Storage swaps did not break the service contract
- Search is practical and safe
- The checkpoint demo is honest and repeatable

## Scope Guardrails
✓ Stable milestone first  
✓ Practical search and persistence  
✓ Small optional ORM exposure only if environment allows  
✓ Clear repo/service/UI boundaries

✗ Not required: fancy joins, migrations, or advanced ORM topics

<!-- Sources: Advanced/lessons/lecture/Day8_Hour1_Advanced.md — Scope Guardrails; Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Stability is the priority -->

---

# Thank You!

Next milestone after Day 8:
- refine architecture
- expand data features carefully
- keep reliability ahead of novelty

<!-- Sources: Advanced/lessons/lecture/Day8_Hour4_Advanced.md — Opening Script; Reflection and exit ticket framing -->
