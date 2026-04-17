# Advanced Day 3 — Session 3 (Hours 9–12)
Python Programming (Advanced) • Packages, Logging, Safe Saves, and Decorators

---

# Session 3 Overview

## Topics Covered Today
- Hour 9: Project structure, packages, imports, and config
- Hour 10: Logging and error reporting (practical)
- Hour 11: Context managers + safer file operations
- Hour 12: Decorators (timing / authorization / validation)

### Source Alignment
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → `## Session 3 overview`
- `Advanced/lessons/lecture/Day3_Hour1_Advanced.md` → `# Advanced Day 3, Hour 1: Project Structure, Packages, Imports, and Config`
- `Advanced/lessons/lecture/Day3_Hour2_Advanced.md` → `# Day 3, Hour 2: Logging and Error Reporting (Practical)`
- `Advanced/lessons/lecture/Day3_Hour3_Advanced.md` → `# Day 3, Hour 3: Context Managers + Safer File Operations`
- `Advanced/lessons/lecture/Day3_Hour4_Advanced.md` → `# Day 3, Hour 4: Decorators (Timing / Authorization / Validation)`

---

# Session 3 Outcomes

- Package the core under `src/`
- Add logging that helps developers without spamming users
- Save JSON more safely with temp-then-replace thinking
- Use decorators for repeated edge behavior

---

# Scope Guardrails for Today

## In Scope
- Packaging and import hygiene
- File-based logging
- Context managers and safe saves
- Small, readable decorators

## Not Yet
- Full production config systems
- Secret-heavy deployment workflows
- Decorator metaprogramming tricks
- Database transactions

---

# Hour 9: Project Structure + Imports + Config

## Learning Outcomes
- Move from a loose script pile to a usable package layout
- Explain the role of `__init__.py`
- Avoid common import headaches
- Centralize simple configuration

---

## Why Structure Matters Now

- Yesterday's checkpoint core needs a cleaner home
- New layers are coming:
  - logging
  - persistence
  - APIs
  - tests
- Brittle imports slow every later step

---

## Practical `src/` Layout

```text
project_root/
    src/
        tracker/
            __init__.py
            models.py
            services.py
            exceptions.py
            config.py
    demo.py
    README.md
```

---

## Import Rules to Remember

- Relative imports can help **inside** a package
- Absolute imports are clearer **from outside** the package
- Run from the project root or use `python -m ...`

### Three Headaches to Avoid
1. Wrong entry file
2. Circular imports
3. Naming collisions like `json.py` or `logging.py`

---

## Demo: Clean Package Move

```python
from tracker.exceptions import ValidationError


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "medium") -> None:
        ...
```

- Move related files together
- Fix imports intentionally
- Re-run the demo after restructuring

---

## Light Configuration

- Move hard-coded paths into `config.py`
- Good early config values:
  - data directory
  - log path
  - default save filename
- Keep it small and practical

---

## Lab: Restructure the Core

**Time: 25–35 minutes**

### Tasks
- Create `src/tracker/`
- Add `__init__.py`
- Move models and services into the package
- Update imports
- Add a simple `config.py`
- Prove the demo still runs

---

## Completion Criteria (Hour 9)

✓ Package layout exists  
✓ Imports are consistent  
✓ Demo runs from the intended entry point  
✓ Config values are not scattered across random files

---

## Homework + Quiz Emphasis (Hour 9)

- Homework framing:
  - **Goal:** package layout + config module
  - **Best practice:** packages + dedicated settings module
  - **Pitfall:** relative imports everywhere without discipline
- Quiz/canonical contract marker:
  - `Hour 9 | package root: tracker_app`

### Source Alignment
- `Advanced/assignments/Advanced_Day3_homework.ipynb` → `## Part 1: Hour 9 - Project structure: packages, imports, and config`
- `Advanced/quizzes/Advanced_Day3_Quiz.html` → `QUIZ_DATA` questions 1–5

---

## Common Pitfalls (Hour 9)

⚠️ Running modules directly from inside the package  
⚠️ Circular imports between services and models  
⚠️ Shadowing standard library module names  
⚠️ Hard-coded paths in multiple files

---

## Quick Check

**Question:** What usually causes `ModuleNotFoundError` right after a student "cleans up" project structure?

---

# Hour 10: Logging and Error Reporting

## Learning Outcomes
- Use `logging` instead of scattered `print()` debugging
- Choose practical levels: DEBUG, INFO, WARNING, ERROR
- Keep user messages separate from developer diagnostics
- Write logs to `logs/app.log`

---

## Big Idea

**Logs are for developers. Error messages are for users.**

- Users need calm, clear feedback
- Developers need timestamps, context, and failure detail
- More output is not the same as better diagnostics

---

## Practical Log Levels

- `DEBUG` → detailed development tracing
- `INFO` → normal important events
- `WARNING` → something odd happened, but recovery is possible
- `ERROR` → an operation failed

### Example Signals
- "created task 7" → INFO
- "task 999 missing" → WARNING
- "failed to save file" → ERROR

---

## Demo: Configure Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="logs/app.log",
)
```

```python
logger = logging.getLogger(__name__)
```

---

## Demo: Friendly User Message, Richer Log

```python
try:
    service.get_task(999)
except NotFoundError:
    logger.warning("Attempted lookup for missing task_id=%s", 999)
    print("Task 999 was not found.")
```

- Same event
- Different audiences

---

## Lab: Add Logging

**Time: 25–35 minutes**

### Tasks
- Create `logs/`
- Configure file logging
- Add at least three log calls
- Trigger one failure on purpose
- Inspect `logs/app.log`

---

## Completion Criteria (Hour 10)

✓ `app.log` is created  
✓ Logs show useful events, not noise  
✓ User-facing messages stay readable  
✓ Failures leave a developer trail

---

## Homework + Quiz Emphasis (Hour 10)

- Homework framing:
  - **Goal:** structured log messages for service events and failures
  - **Best practice:** use logging levels instead of `print()` debugging
  - **Pitfall:** dumping raw secrets or stack noise into ordinary logs
- Quiz/canonical contract marker:
  - `Hour 10 | logger name: tracker.service`

### Source Alignment
- `Advanced/assignments/Advanced_Day3_homework.ipynb` → `## Part 2: Hour 10 - Logging and error reporting`
- `Advanced/quizzes/Advanced_Day3_Quiz.html` → `QUIZ_DATA` questions 6–10

---

## Common Pitfalls (Hour 10)

⚠️ Using logs as a substitute for clear code  
⚠️ Logging too little or too much  
⚠️ Showing full tracebacks to end users  
⚠️ Forgetting to create the log directory

---

## Quick Check

**Question:** When should you log at `WARNING` instead of `ERROR`?

---

# Hour 11: Context Managers + Safer File Operations

## Learning Outcomes
- Explain what a context manager really guarantees
- Use `with` for safer resource handling
- Understand why naive overwrites can corrupt data
- Apply a write-temp-then-replace save pattern

---

## The Mental Model for `with`

- setup on entry
- cleanup on exit
- cleanup still happens if an exception occurs

### Common Uses
- files
- locks
- database connections
- temporary resources

---

## Why Direct Overwrites Are Risky

```python
with open("tasks.json", "w") as file:
    file.write(json_text)
```

- Better than manual close
- Still risky if the write fails midway
- Can leave a good file half-written or corrupted

---

## Safe Save Pattern

1. Resolve the real target path
2. Make sure the parent directory exists
3. Write new content to a temp file
4. Close it successfully
5. Replace the original file

---

## Demo: `save_json_safe`

```python
from pathlib import Path
import json


def save_json_safe(path: str | Path, data: list[dict]) -> None:
    target_path = Path(path)
    temp_path = target_path.with_suffix(target_path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")
    temp_path.replace(target_path)
```

---

## Lab: Safe Save Utility

**Time: 25–35 minutes**

### Tasks
- Implement `save_json_safe(path, data)`
- Use `with`
- Write a `.tmp` file next to the real file
- Replace only after success
- Simulate a failure and compare outcomes

---

## Completion Criteria (Hour 11)

✓ File work uses context managers  
✓ Save logic writes to temp first  
✓ Replace happens after success  
✓ Student can explain why the pattern is safer

---

## Homework + Quiz Emphasis (Hour 11)

- Homework framing:
  - **Goal:** safe file operation flow that writes and reads tracker data
  - **Best practice:** wrap file work in context managers
  - **Pitfall:** opening files without `with`
- Quiz/canonical contract marker:
  - `Hour 11 | file mode: context manager used`

### Source Alignment
- `Advanced/assignments/Advanced_Day3_homework.ipynb` → `## Part 3: Hour 11 - Context managers + safer file operations`
- `Advanced/quizzes/Advanced_Day3_Quiz.html` → `QUIZ_DATA` questions 11–15

---

## Common Pitfalls (Hour 11)

⚠️ Writing directly to the final file first  
⚠️ Putting temp files in unrelated locations  
⚠️ Forgetting to create the parent directory  
⚠️ Teaching "it probably works" instead of failure simulation

---

## Quick Check

**Question:** What is the main advantage of writing to a temporary file first?

---

# Hour 12: Decorators

## Learning Outcomes
- Explain decorators in plain language
- Build a wrapper with `*args` and `**kwargs`
- Add timing or authorization behavior without rewriting core functions
- Use `functools.wraps`

---

## Decorator Idea

- A decorator takes a function
- Wraps it
- Returns a new function

### Good Course Use Cases
- timing
- logging entry/exit
- toy auth checks
- lightweight validation

---

## Demo: Essential Shape

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

- Accept the function
- Pass through arguments
- Return the result

---

## Demo: `@timed`

```python
import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.6f} seconds")
        return result
    return wrapper
```

---

## Readability Rule

- Decorators should handle repeated edge behavior
- They should stay small
- They should not hide the main business story

### Stop If...
- the wrapper is longer than the function it decorates
- the decorator becomes a black box of business logic

---

## Lab: Decorator Practice

**Time: 25–35 minutes**

### Tasks
- Build a `@timed` decorator
- Attach it to 2 service methods
- Log the timing result
- Preserve metadata with `@wraps`
- Optional: sketch a toy auth or validation decorator

---

## Completion Criteria (Hour 12)

✓ Decorated functions still return the right result  
✓ Timing or validation behavior is visible  
✓ `@wraps` preserves helpful metadata  
✓ Core function purpose remains clear

---

## Homework + Quiz Emphasis (Hour 12)

- Homework framing:
  - **Goal:** decorated service function with reusable wrappers
  - **Best practice:** use decorators for cross-cutting concerns
  - **Pitfall:** stuffing business logic into decorators
- Quiz/canonical contract marker:
  - `Hour 12 | timing decorator: add_task took 0.002s`

### Source Alignment
- `Advanced/assignments/Advanced_Day3_homework.ipynb` → `## Part 4: Hour 12 - Decorators`
- `Advanced/quizzes/Advanced_Day3_Quiz.html` → `QUIZ_DATA` questions 16–20

---

## Common Pitfalls (Hour 12)

⚠️ Forgetting to `return result`  
⚠️ Ignoring `*args` / `**kwargs` pass-through  
⚠️ Losing function metadata without `@wraps`  
⚠️ Hiding too much logic in the decorator

---

## Quick Check

**Question:** What breaks if the wrapper forgets to return the original function result?

---

# Session 3 Wrap-Up

## What We Added Today
- Package structure under `src/`
- Real logging habits
- Safer JSON save patterns
- Reusable wrappers through decorators

### Key Rule
**Operational habits are part of software design, not an afterthought.**

---

## Day 3 Homework / Study Checklist

- Run the project from the intended entry point
- Inspect `logs/app.log`
- Test a simulated save failure
- Re-run a decorated service call
- Match canonical labels where the notebook expects them

### Source Alignment
- `Advanced/assignments/Advanced_Day3_homework.ipynb` → `## Submission Checklist`

---

## Next Session Preview

### Session 4 (Hours 13–16)
- HTTP clients with `requests`
- Environment-variable and secrets habits
- Capstone planning workshop
- Checkpoint 2: persistence-ready core + JSON save/load

---

# Thank You!

Package it cleanly.  
Log what matters.  
Save data safely.  
Keep the wrappers readable.
