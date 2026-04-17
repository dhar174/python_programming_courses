# Advanced Day 1 — Session 1 (Hours 1–4)
Python Programming (Advanced) • Kickoff, Class Design, Validation, and Composition

---

# Session 1 Overview

## Topics Covered Today
- Hour 1: Advanced kickoff + baseline diagnostic + Git workflow
- Hour 2: Designing classes from requirements
- Hour 3: Properties, invariants, and custom exceptions
- Hour 4: Composition vs inheritance + polymorphism

### Source Alignment
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → `## Session 1 overview`
- `Advanced/lessons/lecture/Day1_Hour1_Advanced.md` → `# Day 1, Hour 1: Advanced Kickoff, Baseline Diagnostic, and Git Workflow`
- `Advanced/lessons/lecture/Day1_Hour2_Advanced.md` → `# Day 1, Hour 2: Designing Classes from Requirements`
- `Advanced/lessons/lecture/Day1_Hour3_Advanced.md` → `# Day 1, Hour 3: Properties, Invariants, and Custom Exceptions`
- `Advanced/lessons/lecture/Day1_Hour4_Advanced.md` → `# Day 1, Hour 4: Composition vs Inheritance + Polymorphism`

---

# Session 1 Outcomes

- Set up an advanced-course capstone workspace
- Use Git for frequent, understandable progress commits
- Translate requirements into domain models + service boundaries
- Protect object state with validation and specific exceptions
- Prefer composition when collaborator behavior may change

---

# Scope Guardrails for Today

## In Scope
- Project scaffold and workflow habits
- Responsibility-driven design
- Properties, invariants, and custom exceptions
- Lightweight polymorphism and composition

## Not Yet
- Database persistence
- GUI or HTTP layers
- Production auth/security systems
- Overengineered inheritance hierarchies

---

# Hour 1: Advanced Kickoff + Baseline Diagnostic

## Learning Outcomes
- Confirm the lab environment is ready for advanced work
- Create the standard capstone folder layout
- Initialize Git and make a first meaningful commit
- Prove baseline readiness with a tiny diagnostic script

---

## Why Day 1 Starts Here

- Advanced Python is about **structure**, not just syntax
- We will build a capstone across the course
- Frequent saves and small commits reduce recovery pain
- The goal is a repeatable workflow before bigger architecture work

### Source Alignment
- `Advanced/lessons/lecture/Day1_Hour1_Advanced.md` → `## 1. Advanced Kickoff (10 minutes)`
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `## Part 1: Setup, Diagnostic Thinking, and Git Workflow`

---

## Standard Capstone Scaffold

```text
project_root/
├── src/
├── tests/
├── data/
└── reports/
```

- Keep course work inside one repo/workspace
- Save files normally; use lab suspend for longer breaks
- Build the habit now before the project gets bigger

---

## Demo: Workspace + Git Baseline

```bash
mkdir capstone_tracker
cd capstone_tracker
git init
python --version
git status
```

- Start in a clean project folder
- Confirm interpreter selection early
- Commit after a working checkpoint, not after a mystery pile of edits

---

## Demo: Readiness Script

```python
class Hello:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print(f"Hello, {self.name}!")


data = {"status": "ready"}
```

- Include a class
- Touch a dictionary
- Show exception handling
- Demonstrate file-aware thinking

---

## Lab: Environment + Diagnostic Check

**Time: 25–35 minutes**

### Tasks
- Create the project folders: `src`, `tests`, `data`, `reports`
- Initialize a Git repo
- Write a short diagnostic script that:
  - defines a class
  - uses a dictionary
  - catches a specific error
  - ends with `Diagnostic status: ready`

---

## Completion Criteria (Hour 1)

✓ `python --version` succeeds  
✓ `git init` completed in the project folder  
✓ Diagnostic script runs cleanly  
✓ Learner can explain **commit vs push**  
✓ Folder layout matches the course scaffold

---

## Homework + Quiz Emphasis (Hour 1)

- Homework asks for:
  - `Student: ...`
  - `Goal: ...`
  - `Python Version: ...`
  - `Project folders: src, tests, data, reports`
  - `Git workflow: clone -> pull -> status -> add -> commit -> push`
- Quiz focus:
  - save vs suspend
  - `git init`
  - commit vs push
  - diagnostic skill mix

### Source Alignment
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `### Exercise 1.1`, `### Exercise 1.2`, `### Exercise 1.3`
- `Advanced/quizzes/Advanced_Day1_Quiz.html` → `QUIZ_DATA` questions 1–6

---

## Common Pitfalls (Hour 1)

⚠️ Confusing file save with lab session save  
⚠️ Waiting too long between commits  
⚠️ Skipping the readiness script and discovering issues later  
⚠️ Treating Git as backup instead of workflow

---

## Quick Check

**Question:** What does a commit do that a push does not?

---

# Hour 2: Designing Classes from Requirements

## Learning Outcomes
- Turn a requirements list into candidate classes
- Separate what an object **knows** from what it **does**
- Keep UI concerns out of domain models
- Introduce a coordinating service layer

---

## Responsibility-Driven Design

- Ask first:
  - What does this object know?
  - What does this object do?
- Keep methods small and testable
- Let the model protect its own state
- Let the service layer coordinate workflows

---

## From Requirements to Classes

### Example Tracker Domain
- `Task`
  - knows: title, description, priority, status
  - does: complete(), update_priority()
- `TaskService` or `TaskManager`
  - knows: collection of tasks
  - does: add_task(), get_pending_tasks(), search()

---

## Boundary Rule

## Keep These Separate
- **Model**: domain state + invariant-friendly behavior
- **Service layer**: orchestration + use cases
- **UI layer**: `print()`, `input()`, menus, prompts

### Smell to Fix
- A `Task` class that asks for user input directly

---

## Demo: Small but Clean Model

```python
class Task:
    def __init__(self, title: str, description: str, priority: str = "Medium") -> None:
        self.title = title
        self.description = description
        self.priority = priority
        self.is_complete = False

    def complete(self) -> None:
        self.is_complete = True
```

---

## Demo: Outside-the-Class Summary

```python
def display_task_summary(task: Task) -> None:
    status = "Done" if task.is_complete else "Pending"
    print(f"[{status}] {task.title} (Priority: {task.priority})")
```

- Logic stays in the model
- Presentation stays outside the model

---

## Lab: Domain Modeling

**Time: 25–35 minutes**

### Tasks
- Pick one tracker domain:
  - tasks
  - contacts
  - inventory
  - notes
  - expenses
- Write 5–8 requirements
- Design 3–5 classes
- Implement at least:
  - one domain class
  - one coordinating class

---

## Completion Criteria (Hour 2)

✓ Requirements map clearly to classes  
✓ Attributes and methods are distinct  
✓ No `input()` / `print()` inside domain logic  
✓ Demo block creates an object and shows a summary externally

---

## Homework + Quiz Emphasis (Hour 2)

- Homework expects:
  - requirement bullets
  - 3–5 classes
  - one domain class + one coordinating class
  - a clear boundary rule
- Quiz focus:
  - what an object knows vs does
  - what belongs in a service layer
  - where validation should live

### Source Alignment
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `## Part 2: Designing Classes from Requirements`
- `Advanced/quizzes/Advanced_Day1_Quiz.html` → `QUIZ_DATA` questions 7–12

---

## Common Pitfalls (Hour 2)

⚠️ Putting UI prompts into model methods  
⚠️ Designing around globals instead of collaborators  
⚠️ Making classes vague helper buckets  
⚠️ Jumping to inheritance before clarifying responsibilities

---

## Quick Check

**Question:** Where should business validation live: UI, service/model, or Git history?

---

# Hour 3: Properties, Invariants, and Custom Exceptions

## Learning Outcomes
- Define an invariant for a real domain object
- Use `@property` to control attribute access
- Raise specific exceptions for domain problems
- Catch errors in the driver/UI layer instead of inside the model

---

## Core Idea: Valid Objects Stay Valid

- An **invariant** is a rule that must remain true
- Examples:
  - title must not be blank
  - amount must be positive
  - priority must be an integer in range
- A model that accepts invalid state becomes harder to trust later

---

## Demo: Custom Exception + Property

```python
class ValidationError(Exception):
    pass


class Task:
    def __init__(self, title: str, priority: int = 1) -> None:
        self.title = title
        self.priority = priority
```

---

## Demo: Validated Setter

```python
    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int) -> None:
        if not isinstance(value, int) or value < 1:
            raise ValidationError("Priority must be an integer >= 1")
        self._priority = value
```

- Backing field uses `_priority`
- Setter guards the invariant

---

## Catching Specific Errors

```python
try:
    task = Task("Clean Desk", priority=-1)
except ValidationError as error:
    print(f"ValidationError: {error}")
```

- Specific beats broad
- Avoid `except Exception:` for expected domain failures

---

## Lab: Validation + Exceptions

**Time: 25–35 minutes**

### Tasks
- Convert one important attribute to a validated property
- Add at least two custom exceptions:
  - `ValidationError`
  - `NotFoundError`
- Show:
  - invalid data raises `ValidationError`
  - missing lookup raises `NotFoundError`

---

## Completion Criteria (Hour 3)

✓ A real invariant is enforced  
✓ The setter uses a backing field  
✓ Specific exceptions are raised intentionally  
✓ Friendly handling happens in a driver/demo block

---

## Homework + Quiz Emphasis (Hour 3)

- Homework expects both `ValidationError` and `NotFoundError`
- Canonical outputs include:
  - `Priority set to: 3`
  - `ValidationError: title cannot be empty`
  - `NotFoundError: task 404 was not found`
- Quiz focus:
  - invariant meaning
  - why `@property` helps
  - why specific exceptions beat `except Exception:`

### Source Alignment
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `## Part 3: Properties, Invariants, and Custom Exceptions`
- `Advanced/quizzes/Advanced_Day1_Quiz.html` → `QUIZ_DATA` questions 13–18

---

## Common Pitfalls (Hour 3)

⚠️ Setter assigns to `self.priority` recursively  
⚠️ Returning `False` instead of surfacing a real error  
⚠️ Catching every exception and hiding unrelated bugs  
⚠️ Validating only in the UI and not in the model/service

---

## Quick Check

**Question:** Why is `ValidationError` usually better than returning `False` from validation code?

---

# Hour 4: Composition vs Inheritance + Polymorphism

## Learning Outcomes
- Distinguish **is-a** from **has-a**
- Use composition when collaborator behavior may vary
- Reduce branchy code with shared method names
- Explain duck typing in practical terms

---

## Inheritance vs Composition

### Use Inheritance for
- real **is-a** relationships
- stable shared behavior

### Use Composition for
- **has-a** relationships
- swappable collaborators
- cleaner extension without deep class trees

---

## Demo: Branchy Export Smell

```python
def export_data(data, format_type):
    if format_type == "json":
        ...
    elif format_type == "csv":
        ...
    else:
        raise ValueError("Unknown format")
```

- Works at first
- Scales badly as new behaviors appear

---

## Demo: Polymorphic Exporters

```python
class JSONExporter:
    def export(self, data):
        return {"data": data}


class CSVExporter:
    def export(self, data):
        return f"data,{data}"
```

---

## Demo: Composition in the Caller

```python
class ReportService:
    def __init__(self, exporter) -> None:
        self.exporter = exporter

    def generate(self, data):
        return self.exporter.export(data)
```

- Caller depends on a compatible collaborator
- New exporter types do not require new caller branches

---

## Lab: Refactor a Branchy Design

**Time: 25–35 minutes**

### Tasks
- Start with a branching scenario:
  - exporting
  - notifications
  - payments
- Create 2+ implementations with the same method name
- Add a class that **has a** collaborator
- Swap collaborators without changing caller structure

---

## Completion Criteria (Hour 4)

✓ A large `if/elif` chain is reduced or removed  
✓ Two or more implementations share one method name  
✓ Composition is visible in the caller  
✓ A third implementation could be added with minimal change

---

## Homework + Quiz Emphasis (Hour 4)

- Homework expects:
  - a branchy design replaced
  - composition shown clearly
  - optional third implementation
- Canonical output references:
  - `Composed notifier sent: Task created`
  - `Export text: TASK-101 | Draft syllabus`
  - `Export dict: {'id': 'TASK-101', 'title': 'Draft syllabus'}`
- Quiz focus:
  - is-a vs has-a
  - duck typing
  - caller stability when new implementations appear

### Source Alignment
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `## Part 4: Composition vs Inheritance + Polymorphism`
- `Advanced/quizzes/Advanced_Day1_Quiz.html` → `QUIZ_DATA` questions 19–24

---

## Common Pitfalls (Hour 4)

⚠️ Moving the `if/elif` chain into a new class instead of removing it  
⚠️ Inheriting when the relationship is really has-a  
⚠️ Forgetting that duck typing cares about behavior, not ancestry  
⚠️ Hard-coding collaborator choice inside the caller

---

## Quick Check

**Question:** What is the practical benefit of giving the caller any object with a compatible `export()` method?

---

# Session 1 Wrap-Up

## What We Built Today
- A stable workspace + Git baseline
- Cleaner domain boundaries
- Validated models with specific exceptions
- Composition-friendly architecture

### Key Day 1 Rule
**Professional Python starts with trustworthy structure.**

---

## Day 1 Homework / Study Checklist

- Re-run the diagnostic script
- Refine your requirements list
- Enforce one invariant with a property
- Add two specific custom exceptions
- Refactor one branch-heavy workflow into collaborators

### Source Alignment
- `Advanced/assignments/Advanced_Day1_homework.ipynb` → `## Reflection and Submission Checklist`

---

## Next Session Preview

### Session 2 (Hours 5–8)
- Factory pattern for validated creation
- Strategy pattern for swappable behavior
- `__repr__`, `__str__`, equality, and light type hints
- Checkpoint 1: domain + service layer milestone

---

# Thank You!

Save your work.  
Commit the latest good state.  
Be ready to extend the core tomorrow.
