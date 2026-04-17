# Advanced Day 2 — Session 2 (Hours 5–8)
Python Programming (Advanced) • Factory, Strategy, Ergonomics, and Checkpoint 1

---

# Session 2 Overview

## Topics Covered Today
- Hour 5: Pattern: Factory (practical creation + validation)
- Hour 6: Pattern: Strategy (swap behaviors cleanly)
- Hour 7: Pythonic class ergonomics (`repr` / `str` / equality) + light type hints
- Hour 8: Checkpoint 1: domain + service layer milestone

### Source Alignment
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → `## Session 2 overview`
- `Advanced/lessons/lecture/Day2_Hour1_Advanced.md` → `# Day 2, Hour 1: Pattern: Factory (practical creation + validation)`
- `Advanced/lessons/lecture/Day2_Hour2_Advanced.md` → `# Day 2, Hour 2: Pattern: Strategy (swap behaviors cleanly)`
- `Advanced/lessons/lecture/Day2_Hour3_Advanced.md` → `# Day 2, Hour 3: Pythonic Class Ergonomics`
- `Advanced/lessons/lecture/Day2_Hour4_Advanced.md` → `# Day 2, Hour 4: Checkpoint 1: Domain + Service Layer Milestone`

---

# Session 2 Outcomes

- Centralize creation rules with factories
- Swap behavior without rewriting callers
- Make models easier to inspect, print, and compare
- Deliver a clean headless core for Checkpoint 1

---

# Scope Guardrails for Today

## In Scope
- Validated object creation
- Strategy dispatch with functions or collaborators
- Readable object output and simple type hints
- Core-only checkpoint work

## Not Yet
- Database persistence
- GUI callbacks
- HTTP routes
- Heavy typing abstractions or framework ceremony

---

# Hour 5: Factory Pattern

## Learning Outcomes
- Move creation + normalization logic out of `__init__`
- Turn raw payloads into safe domain objects
- Raise validation errors before bad objects spread
- Explain why centralized creation improves consistency

---

## Why Factories Matter

- External data is messy
- Repeating validation in every caller causes drift
- `__init__` should initialize, not become a giant intake pipeline
- A factory can:
  - validate
  - normalize
  - apply defaults
  - return a ready-to-use object

---

## Demo: Factory from Raw Data

```python
class UserFactory:
    @classmethod
    def from_dict(cls, data):
        if "name" not in data:
            raise ValidationError("Missing required field: 'name'")

        name = data["name"].strip().title()
        role = data.get("role", "member").lower()
        return User(full_name=name, role=role)
```

---

## Factory Responsibilities

- Validate required fields
- Normalize messy input
- Supply safe defaults
- Reject unsupported values early

### Better Than
- every route validating differently
- every CLI prompt building objects ad hoc
- huge constructors full of branching

---

## Lab: Build a Validated Factory

**Time: 25–35 minutes**

### Tasks
- Create a `from_dict()` or `create_*()` factory
- Validate at least one required field
- Normalize one messy field
- Return a safe tracker record or raise `ValidationError`

---

## Completion Criteria (Hour 5)

✓ Factory builds valid objects from raw payloads  
✓ Missing or bad data fails clearly  
✓ Creation logic is not duplicated in multiple callers  
✓ The returned object is ready for service-layer use

---

## Homework + Quiz Emphasis (Hour 5)

- Homework framing:
  - **Goal:** validated factory for safe tracker records
  - **Best practice:** use a classmethod factory
  - **Pitfall:** duplicating validation logic in every caller
- Quiz/canonical contract marker:
  - `Hour 5 | factory title: Refactor auth flow`

### Source Alignment
- `Advanced/assignments/Advanced_Day2_homework.ipynb` → `## Part 1: Hour 5 - Pattern: Factory`
- `Advanced/quizzes/Advanced_Day2_Quiz.html` → `QUIZ_DATA` questions 1–5

---

## Common Pitfalls (Hour 5)

⚠️ Letting invalid objects exist "just for now"  
⚠️ Hiding normalization logic in random callers  
⚠️ Making `__init__` do everything  
⚠️ Using vague exceptions with vague messages

---

## Quick Check

**Question:** Why is a factory safer than repeating payload validation in five different places?

---

# Hour 6: Strategy Pattern

## Learning Outcomes
- Replace branch-heavy behavior selection
- Use functions or collaborators as strategies
- Dispatch dynamically from a small mapping
- Keep core orchestration stable while behavior changes

---

## Strategy in Plain English

- We have one job with multiple ways to do it
- We separate **what happens** from **how it happens**
- In Python, a strategy can just be a callable

### Typical Use Cases
- sorting
- filtering
- exporting
- notifications

---

## Demo: Dispatch Map

```python
def sort_by_name(record):
    return record["name"]


sorting_strategies = {
    "name": sort_by_name,
    "id": sort_by_id,
    "created": sort_by_date,
}
```

---

## Demo: Core Function Stays Simple

```python
def display_records_strategy(records, strategy_key):
    strategy_func = sorting_strategies.get(strategy_key, sort_by_id)
    sorted_records = sorted(records, key=strategy_func)
    for record in sorted_records:
        print(record)
```

- Caller does not need a giant `if/elif`
- New strategies are easier to add

---

## Lab: Strategy Selection

**Time: 25–35 minutes**

### Tasks
- Choose a behavior that varies:
  - filter active vs all
  - sort by name vs date
  - notify via email vs console
- Implement 2+ strategies
- Use a dictionary dispatcher or injected collaborator
- Run the same caller with multiple behaviors

---

## Completion Criteria (Hour 6)

✓ Two or more strategies exist  
✓ Behavior is selected dynamically  
✓ Caller logic stays small  
✓ A new strategy can be added without rewriting the main flow

---

## Homework + Quiz Emphasis (Hour 6)

- Homework framing:
  - **Goal:** switch behavior without rewriting the caller
  - **Best practice:** inject behavior objects or callables
  - **Pitfall:** burying every algorithm in one `if/elif` chain
- Quiz/canonical contract marker:
  - `Hour 6 | strategy selected: EmailNotifier`

### Source Alignment
- `Advanced/assignments/Advanced_Day2_homework.ipynb` → `## Part 2: Hour 6 - Pattern: Strategy`
- `Advanced/quizzes/Advanced_Day2_Quiz.html` → `QUIZ_DATA` questions 6–10

---

## Common Pitfalls (Hour 6)

⚠️ Calling a function instead of passing the function object  
⚠️ Keeping the big branch chain in the main routine  
⚠️ Naming strategies unclearly  
⚠️ Mixing strategy selection with unrelated UI complexity

---

## Quick Check

**Question:** What changes when you add a third strategy to a good strategy-based design?

---

# Hour 7: Pythonic Class Ergonomics

## Learning Outcomes
- Differentiate `__str__` from `__repr__`
- Implement value-based equality with `__eq__`
- Add light type hints that improve readability and tooling
- Prepare models for easier debugging and serialization

---

## Why Default Objects Are Not Enough

```python
print(task)
# <__main__.Task object at 0x...>
```

- Not useful for logs
- Not useful for debugging
- Not helpful in a CLI or demo script

---

## Demo: Friendly + Developer Views

```python
class Task:
    def __init__(self, t_id: int, title: str) -> None:
        self.id = t_id
        self.title = title

    def __repr__(self) -> str:
        return f"Task(t_id={self.id}, title='{self.title}')"

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
```

---

## Demo: Equality Matters, Too

```python
def __eq__(self, other: object) -> bool:
    if not isinstance(other, Task):
        return False
    return self.id == other.id and self.title == other.title
```

- Default equality checks identity
- Custom equality can check useful data equivalence

---

## Light Type Hinting Rules

- Keep it simple:
  - `int`
  - `str`
  - `list`
  - `dict`
  - `-> None`
- Use hints to document intent
- Do not turn this hour into typing wizardry

---

## Lab: Make the Model Pleasant to Work With

**Time: 25–35 minutes**

### Tasks
- Add `__repr__`
- Add `__str__`
- Add `__eq__` where value comparison helps
- Add type hints to `__init__` and 3+ methods/functions
- Optional: add `to_dict()`

---

## Completion Criteria (Hour 7)

✓ Model prints helpfully for users and developers  
✓ Equality behavior is intentional  
✓ Type hints improve readability without overcomplication  
✓ `__str__` and `__repr__` return strings, not `print()`

---

## Homework + Quiz Emphasis (Hour 7)

- Homework framing:
  - **Goal:** string output and equality that support debugging and testing
  - **Best practice:** implement `repr`, `str`, and equality clearly
  - **Pitfall:** unreadable model output
- Quiz/canonical contract marker:
  - `Hour 7 | repr: Task(title='Write tests', priority='medium')`

### Source Alignment
- `Advanced/assignments/Advanced_Day2_homework.ipynb` → `## Part 3: Hour 7 - Pythonic class ergonomics`
- `Advanced/quizzes/Advanced_Day2_Quiz.html` → `QUIZ_DATA` questions 11–15

---

## Common Pitfalls (Hour 7)

⚠️ `__str__` uses `print()` instead of returning a string  
⚠️ Overcomplicating hints with unnecessary imports  
⚠️ Equality based on the wrong fields  
⚠️ Forgetting that `repr()` serves developers first

---

## Quick Check

**Question:** When would you inspect `repr(obj)` instead of `str(obj)`?

---

# Hour 8: Checkpoint 1 — Domain + Service Layer Milestone

## Learning Outcomes
- Deliver a stable, headless core package
- Demonstrate happy-path and sad-path flows
- Show service-layer CRUD behavior
- Prepare the codebase for packaging and persistence next

---

## What Checkpoint 1 Proves

- Models are real, not placeholder shells
- Services coordinate use cases cleanly
- Exceptions communicate invalid operations
- Objects can serialize to dictionaries
- The core works without a GUI, DB, or API layer

---

## Rubric Snapshot

### Expect to Show
- at least 2 model/helper classes
- add, list, search, update, delete behaviors
- custom exceptions
- `to_dict()` or similar serialization helper
- a small demo script that proves the design

---

## Demo Shape for Grading

```python
print("--- Starting Checkpoint 1 Demo ---")
print("1. Happy Path: Adding valid records...")
print("2. Sad Path: Missing required fields...")
print("3. Sad Path: Updating a missing record...")
print("4. Serialization Check...")
```

- Make grading easy
- Prove both success and failure paths deliberately

---

## Lab: Checkpoint 1 Build

**Time: 45–60 minutes**

### Tasks
- Review model and service separation
- Fill missing CRUD operations
- Confirm exceptions are raised intentionally
- Add or refine `to_dict()`
- Build a demo script that shows:
  - valid creation
  - invalid data handling
  - missing record handling
  - serialization output

---

## Completion Criteria (Hour 8)

✓ Headless core runs end to end  
✓ Service layer does real work  
✓ Sad paths fail cleanly  
✓ Demo script proves the rubric without digging through the whole codebase

---

## Homework + Quiz Emphasis (Hour 8)

- Homework framing:
  - **Goal:** milestone that adds, validates, and lists tracker records
  - **Best practice:** keep domain logic in the service layer
  - **Pitfall:** letting UI or raw dicts bypass the service layer
- Quiz/canonical contract marker:
  - `Hour 8 | checkpoint records: 2`

### Source Alignment
- `Advanced/assignments/Advanced_Day2_homework.ipynb` → `## Part 4: Hour 8 - Checkpoint 1`
- `Advanced/quizzes/Advanced_Day2_Quiz.html` → `QUIZ_DATA` questions 16–20

---

## Common Pitfalls (Hour 8)

⚠️ UI prompts inside service methods  
⚠️ Global state everywhere  
⚠️ Missing-record crashes turning into `IndexError` noise  
⚠️ Demo scripts that show only the happy path

---

## Quick Check

**Question:** Why is a clean core milestone more valuable right now than adding a flashy interface?

---

# Session 2 Wrap-Up

## What We Extended Today
- Safer creation with factories
- Cleaner behavior swaps with strategies
- Better debugging ergonomics
- A checkpointed service-layer core

### Key Rule
**Make the core trustworthy before adding more surfaces.**

---

## Day 2 Homework / Study Checklist

- Re-run your factory with good and bad payloads
- Add one more strategy
- Confirm `repr`, `str`, and equality behavior
- Verify the checkpoint demo proves both happy and sad paths
- Match required labels exactly where autograding expects them

### Source Alignment
- `Advanced/assignments/Advanced_Day2_homework.ipynb` → `## Submission Checklist`

---

## Next Session Preview

### Session 3 (Hours 9–12)
- Package structure under `src/`
- Logging and developer diagnostics
- Context managers and safe save patterns
- Decorators for timing, auth, and validation

---

# Thank You!

Save the notebook.  
Commit the checkpoint.  
Come back ready to package the core properly.
