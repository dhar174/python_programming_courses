# Advanced Day 3, Hour 1: Project Structure, Packages, Imports, and Config

## Learning Objectives
- Organize code into a proper Python package structure.
- Understand and avoid common import pitfalls (like circular imports).
- Configure applications using constants and lightweight environment variables.

## Instructor Script & Talk Points

**(10–20 min)**

Welcome to Day 3! Today, we take a major step forward in professional software development: organizing our work. As our project grows, throwing everything into one or two files just doesn't scale. 

**The `src` Layout Basics:** 
A professional Python application usually puts its core packages inside a `src/` directory. For example, `src/tracker/`. Why do we do this? It isolates your code and prevents accidental import shadowing. It keeps your repository root clean for meta-files like `README.md`, `tests/`, and `.gitignore`.

**Relative vs Absolute Imports:** 
- *Absolute imports* (`from tracker.models import Item`) reference the package from the very top level.
- *Relative imports* (`from .models import Item`) refer to relative locations within the same package.
- *Tip:* Use relative imports inside your package to keep modules tightly coupled and location-independent. Use absolute imports from the outside (like in `tests/` or a root entry script).
- *Pitfall:* If you try to run your module directly (e.g., `python src/tracker/models.py`), Python will complain about relative imports. Always run your code from the root of the project as a top-level script, or use the `-m` flag (e.g., `python -m src.tracker.demo`).

**Configuration:**
Don't hardcode absolute file paths or secrets. Manage configuration via a centralized `config.py` file for constants (like `DATA_DIR`), or use light environment variables via `os.environ.get('DATA_DIR', 'default_path')`.

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Start with `models.py` and `services.py` existing at the root of a folder.
2. Create the `src/` directory, and inside it, a `tracker/` directory.
3. Add a blank `__init__.py` inside `tracker/` to designate it as a package.
4. Move `models.py` and `services.py` into `src/tracker/`.
5. Adjust the imports. If `services.py` needs `models.py`, show how `from .models import ...` works.
6. Create an `app.py` at the root and run the package: `from src.tracker.services import TrackerService`. 
7. Run the `app.py` script to prove everything is wired up correctly. Alternatively, demonstrate the `python -m` execution model.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Restructure**

1. Create a `src/tracker/` package inside your repository, complete with an `__init__.py`.
2. Move your existing capstone files (`models.py`, `services.py`, etc.) into this package.
3. Update imports inside the files. Confirm they correctly import from one another without raising errors.
4. Update your main demo script to import from your new package structure.
5. Confirm the demo script still works as perfectly as it did before.

**Optional Extension:**
Add a `config.py` for defining simple, constant variables like `DATA_DIR` or `DB_PATH`, and update your services to pull from this config instead of hardcoded strings.

**Completion Criteria:**
- The project runs cleanly after the restructure.
- Dependencies between modules are resolved, and imports are clean and consistent.

## Section 1: Recap and Why Structure Matters (5 minutes)

**(5 min)**

**Quick Check:** What usually causes `ModuleNotFoundError` in student projects when they start restructuring?

*Expected answer:* Running the wrong entry file (running a script from inside a package directly instead of from the project root), creating circular imports, or naming a module the same name as a built-in standard library package.
### From Working Code to Maintainable Code

**[Instructor speaks:]**

At the end of Session 2, you had a checkpointed core. That was important. But many of those checkpoint projects still live in a shape like this:

- one large file
- maybe a second helper file
- a demo block stuck at the bottom
- imports that only work if you run the exact same file from the exact same folder

That is normal for early-stage code. It is also exactly the moment where structure starts to matter.

The question today is not "does the code work?" It is:

**Can the code keep working as the project grows?**

### Framing the Hour

**[Instructor speaks:]**

Structure matters now because the next parts of the course will keep adding layers:

- logging
- safer file operations
- persistence
- APIs
- tests

If everything stays in one unstable file with brittle imports, each new layer gets harder than it needs to be.

Today we are going to package the core cleanly so future growth has somewhere sane to land.

---

## Section 2: Packages, Imports, and Config Fundamentals (12 minutes)

### A Practical `src/` Layout

**[Instructor speaks:]**

For this course, I want students to hear a very practical message:

`src/` is not magic. It is a container that helps separate the application package from miscellaneous project files.

A clean starter shape might look like this:

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

Why is this better than one giant script?

- related code lives together
- import paths are more intentional
- responsibilities become visible
- later additions such as storage or API modules have a natural home

### What `__init__.py` Does

**[Instructor speaks:]**

Students sometimes treat `__init__.py` like a mysterious ceremony file. For today, keep the explanation simple:

- it marks a directory as a Python package
- it can expose common imports for convenience
- it can stay tiny

Do not turn `__init__.py` into a giant second application. The main job is to make the package real and sometimes provide a nice import surface.

### Common Import Problems

**[Instructor speaks:]**

I want to name the three import headaches students hit most often:

1. **Running the wrong entry file**  
   The code works from one directory but fails from another because execution context changed.

2. **Circular imports**  
   `models.py` imports `services.py`, which imports `models.py`, and suddenly Python is trying to assemble a bicycle while you are still attaching the wheels.

3. **Naming collisions**  
   Students create a file called `json.py`, `logging.py`, or `email.py`, then wonder why standard library imports break.

If we avoid those three problems, project life gets significantly calmer.

### Light Configuration

**[Instructor speaks:]**

Config should also move out of random hard-coded string literals scattered across the codebase.

Examples:

- data directory path
- log file path
- default save filename
- environment-dependent values

At this stage, a simple `config.py` is enough. We are not building a full enterprise config system. We are teaching students to stop hard-coding paths in six different files.

---

## Section 3: Live Demo - Move the Core into `src/tracker/` (13 minutes)

### Demo Setup

**[Instructor speaks:]**

I am going to take a checkpointed core and give it a cleaner home.

Target structure:

```text
src/
    tracker/
        __init__.py
        exceptions.py
        models.py
        services.py
        config.py
demo.py
```

### Demo Code Sketch

`src/tracker/exceptions.py`

```python
class ValidationError(Exception):
    pass


class NotFoundError(Exception):
    pass
```

`src/tracker/models.py`

```python
from tracker.exceptions import ValidationError


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "medium") -> None:
        title = title.strip()
        if not title:
            raise ValidationError("title must not be blank")
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.is_complete = False

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "is_complete": self.is_complete,
        }
```

`src/tracker/services.py`

```python
from tracker.exceptions import NotFoundError
from tracker.models import Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self._tasks.append(task)

    def get_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        raise NotFoundError(f"task {task_id} not found")
```

`src/tracker/config.py`

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
DEFAULT_DATA_FILE = DATA_DIR / "tasks.json"
```

`src/tracker/__init__.py`

```python
from tracker.exceptions import NotFoundError, ValidationError
from tracker.models import Task
from tracker.services import TaskService
```

`demo.py`

```python
from tracker import Task, TaskService

service = TaskService()
service.add_task(Task(1, "Write outline", "high"))
print(service.get_task(1).to_dict())
```

### Demo Narration

**[Instructor speaks:]**

Notice what changed.

- exceptions moved into their own focused module
- models and services are separate
- config values have one obvious home
- the import story is cleaner and more predictable

Also notice what did **not** change: the core logic itself. Good restructuring reduces confusion without forcing a redesign of every behavior.

### Run-As-Module Discussion

**[Instructor speaks:]**

If helpful, this is a good moment to mention package execution:

```bash
python -m tracker
```

You may or may not use that today, but students should at least hear that package-aware execution exists. The larger teaching goal is that how you run code affects how imports resolve.

### Teaching Notes During the Demo

- Explain absolute imports first; they are easier for most students to reason about.
- Keep relative imports out of the spotlight unless there is a specific need.
- Point out that `config.py` is for stable values, not arbitrary business logic.
- Ask students what file they would add next week for persistence work. The structure should make that answer obvious.

---

## Section 4: Hands-On Lab - Restructure the Tracker Project (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Your lab is to take the project you checkpointed and move it into a layout that future-you will not resent.

If your project is still tiny, this should feel like tidying. If it is already messy, this will feel like relief.

### Student Task

1. Create `src/tracker/`.
2. Add `__init__.py`.
3. Move your model code into `models.py`.
4. Move your service-layer code into `services.py`.
5. Move custom exceptions into `exceptions.py`.
6. If you have path-like constants, place them in `config.py`.
7. Update imports and confirm your demo script still runs.

### Completion Criteria

Students are done when:

- the project still runs after restructure
- imports are clean and consistent
- model, service, and exception responsibilities are separated
- no file shadows a standard library module
- there is an obvious place to add future modules

### Circulation Notes

Coach toward calm, incremental changes:

- move one category at a time
- rerun after each move
- do not refactor everything simultaneously
- if imports break, inspect names and execution context before guessing wildly

### Common Pitfalls to Watch For

- circular imports
- running the wrong entry file from the wrong directory
- naming a module `logging.py`, `json.py`, or something else that collides with stdlib
- mixing configuration constants back into random files after creating `config.py`

### Optional Extensions

- Add a tiny `storage.py` placeholder if the student is already thinking ahead to persistence
- Add a package-level import surface in `__init__.py`
- Add a `tests/` directory if the student is ahead and wants a place for future pytest work

---

## Section 5: Import Troubleshooting Playbook (Optional Extension Window)

### Fast Questions to Ask When Imports Break

**[Instructor speaks:]**

When a student says, "My imports are broken," do not start by editing random lines. Ask these in order:

1. What file are you running?
2. From what directory are you running it?
3. What is the exact module name you are trying to import?
4. Did you recently rename a file to something that conflicts with the standard library?
5. Do two files import each other?

These questions turn import debugging from superstition into process.

### Sample Misconceptions and How to Respond

- "If I move code into packages, Python will automatically know what I mean."  
  Response: Structure helps, but imports still depend on execution context and correct module paths.

- "Circular imports mean Python is buggy."  
  Response: They usually mean responsibilities are coupled in a way the structure has exposed.

- "`config.py` is where I can put any code I do not know where to place."  
  Response: No. `config.py` is for configuration values, not miscellaneous business logic.

- "Running whichever file is closest to the code should work."  
  Response: Entry points matter. Project structure and execution style affect import resolution.

### Public Reflection If Time Remains

**[Instructor speaks:]**

Ask the room:

"If we add database storage in a later session, what new module would you create, and where would it live?"

This helps students see structure as a growth tool, not just cleanup work.

---

## Section 6: Debrief and Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

I want students to share one import bug they avoided or fixed today, because import errors often feel mystical until you name the pattern.

Good structure does not eliminate all bugs, but it makes bugs easier to reason about.

### Exit Ticket

Ask students:

**What usually causes `ModuleNotFoundError` in student projects?**

Expected ideas:

- wrong working directory or wrong entry point
- missing package structure
- incorrect import path
- file naming collisions

### Instructor Closing Line

**[Instructor speaks:]**

Great progress. You now have a cleaner package structure instead of a checkpoint bundle held together by hope. Next hour we will add logging so the project can report what it is doing for developers without spamming end users.
