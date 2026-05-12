# Day 3, Hour 1: Project Structure, Packages, Imports, and Config

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 3, Hour 1 of 48, also Hour 9 in the Advanced runbook sequence
- **Focus**: Organizing the checkpointed model and service code into a beginner-safe package structure, using clean imports, and introducing light configuration constants.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 3, Hour 9.
- **Prerequisites**: Learners should have completed or nearly completed the Day 2 Hour 4 Checkpoint 1 core. They should have a tracker-style domain model, a service layer, custom exceptions such as `ValidationError` and `NotFoundError`, and a small demo that proves the core works.
- **Advanced trajectory**: This hour stays on the PCAP-to-PCPP1 path. Learners are not publishing packages, creating a full packaging configuration, or managing dependency tooling yet. The advanced step is learning how project shape affects imports, execution, maintainability, and future GUI/API layers.
- **Instructor goal**: By the end of this hour, every learner has moved `models.py` and `services.py` into `src/tracker/`, updated package-internal imports to use relative imports, and run the demo from the project root with `python -m src.tracker.demo`.

Important instructor positioning:

- Use one consistent convention for this hour: `project_root/src/tracker/` contains the package, and the demo module lives at `src/tracker/demo.py`.
- Inside `src/tracker/`, use package-relative imports such as `from .models import Task` and `from .exceptions import ValidationError`.
- Run from the project root with `python -m src.tracker.demo`. On Windows, `py -m src.tracker.demo` is also acceptable.
- Do not teach a shorter module path that treats `tracker` as already installed in this hour. Do not teach a root `demo.py` that imports `from tracker...` while the package is stored under `src/tracker/`. Without packaging or `PYTHONPATH`, that layout commonly fails. Later packaging or editable installs can make direct `tracker` imports work, but that is a future note, not today's target.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Checkpoint 1 | 5 min | Connect the working Day 2 core to professional project structure |
| Outcomes, setup, and vocabulary | 5 min | Define package, module, `src`, entry point, absolute import, relative import, and config |
| Concept briefing: structure, imports, and config | 12 min | Explain the beginner-safe `src/tracker/` convention, import rules, and light environment configuration |
| Live demo: move the core into `src/tracker/` | 10 min | Move model/service code, update imports, and run `python -m src.tracker.demo` |
| Guided lab: restructure your tracker | 25 min | Learners create the package, move files, update imports, run the exact demo command, and optionally add `config.py` |
| Quick checks, pitfalls, and wrap-up | 3 min | Verify understanding, name common failures, and bridge to logging and error reporting |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 12 + 10 + 25 + 3. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If discussion runs long, shorten examples in the concept briefing rather than shrinking the restructure practice. The required outcome is practical: the project still runs after restructure, and imports are clean and consistent.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain why a working checkpoint project often needs a cleaner package structure before adding logging, file operations, GUI, API, or persistence layers.
2. Describe the course convention for this hour: `project_root/src/tracker/` with `src/tracker/__init__.py`, `models.py`, `services.py`, `exceptions.py`, and `demo.py`.
3. Move existing `models.py` and `services.py` into `src/tracker/` without changing the domain behavior of `Task`, `TaskService`, `ValidationError`, `NotFoundError`, or `to_dict()`.
4. Use package-relative imports inside the package, such as `from .models import Task`.
5. Run the demo from the project root as a module with `python -m src.tracker.demo` or, on Windows, `py -m src.tracker.demo`.
6. Explain why running `python src/tracker/demo.py` is different from running `python -m src.tracker.demo`.
7. Identify common causes of `ModuleNotFoundError`: wrong working directory, wrong entry file, inconsistent import style, missing `__init__.py`, name collisions, or assuming packaging behavior that has not been configured.
8. Recognize and avoid circular imports between `models.py`, `services.py`, and `demo.py`.
9. Avoid naming project files after standard library modules such as `logging.py`, `json.py`, `email.py`, `pathlib.py`, or `sqlite3.py`.
10. Add a light optional `config.py` with constants such as `DATA_DIR` and `DB_PATH`, optionally reading an environment variable through `os.environ.get()`.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 3, Hour 9 visible. The required scope is project structure, packages, imports, and light config. The required lab is to create `src/tracker/`, move `models.py` and `services.py`, update imports, and confirm the demo still works.
- Review the Day 2 Hour 4 Checkpoint 1 expectations. Learners should already have a core model and service layer. Today's job is organization, not rebuilding the model from scratch.
- Prepare a small before-and-after folder sketch on the board:

```text
Before:
project_root/
    models.py
    services.py
    exceptions.py
    demo.py

After for this hour:
project_root/
    src/
        tracker/
            __init__.py
            exceptions.py
            models.py
            services.py
            demo.py
```

- Decide how to address learner naming differences. Use this sentence: "I will say `Task`, `TaskService`, `ValidationError`, `NotFoundError`, `to_dict()`, `models.py`, `services.py`, `exceptions.py`, and `config.py`. If your project uses `TaskRecord` or `TrackerRecord`, adapt the names while preserving the responsibilities."
- Confirm the terminal command for your room. Prefer `python -m src.tracker.demo`. If learners are on Windows and use the Python launcher, show `py -m src.tracker.demo` as a variant.
- Prepare to correct one subtle import issue early: `src/tracker/` is not the same as an installed package named `tracker`. Today we run through the `src.tracker.demo` module path because we have not introduced `pyproject.toml`, editable installs, or dependency packaging.
- If showing the optional environment variable, use Windows-friendly PowerShell syntax first:

```powershell
$env:TRACKER_DATA_DIR = "data"
python -m src.tracker.demo
$env:TRACKER_DATA_DIR = $null
```

You may briefly mention that macOS/Linux shells often use `export TRACKER_DATA_DIR=data`, but do not rely only on that syntax.

Suggested board note:

```text
Today's rule:
Run from project root:
python -m src.tracker.demo

Inside src/tracker/:
from .models import Task
from .exceptions import ValidationError

Do not run package modules as loose files.
```

---

## Opening Bridge from Checkpoint 1 (5 minutes)

**Instructor talk track**

"Welcome back. At the end of Day 2, you reached an important checkpoint. You proved that your core tracker logic can stand on its own. You have a model, such as `Task`, `TaskRecord`, or `TrackerRecord`. You have service behavior, such as add, list, search, update, and delete. You have custom exceptions such as `ValidationError` and `NotFoundError`. You have a `to_dict()` helper so objects can become plain dictionaries. And, most importantly, you have a small demo that proves the core works."

"That is a real milestone. Today we are not throwing that work away. We are giving it a professional home."

Write or display:

```text
Day 2 result: working core
Day 3 Hour 1 goal: organized core
```

"A working core is necessary, but it is not enough for a growing application. If all of our code sits in the project root, the next features become more fragile. In the next hours we will add logging, safer file operations, decorators, and eventually GUI, database, API, testing, and packaging work. Each of those layers needs to find the core code reliably."

"So today's question is not only, 'Does the code work?' The question is:"

```text
Can another part of the application import and use this code predictably?
```

"That is why project structure matters. Structure is not decoration. Structure is how we tell future readers, future tools, and future versions of ourselves where responsibilities live."

Pause and ask:

"Think about your checkpoint project. If I opened it right now, where would I find the model? Where would I find the service layer? Where would I find the demo? Would that be obvious to someone who did not write it?"

Take two or three answers. Expect variation. Some learners may have everything in one file. Some may already have separate files. Some may have a folder but uncertain imports.

Affirm:

"All of those starting points are normal. The goal today is not to shame early structure. Early code often starts flat because that helps us learn the behavior. The goal now is to move from a learning shape to a growth shape."

**Transition**

"Let's name the vocabulary first. Then I will show a careful restructure live. The important part is that the same demo still runs after the move."

---

## Outcomes, Setup, and Vocabulary (5 minutes)

Use this section to make the terms concrete. Keep the language pragmatic.

**Instructor talk track**

"By the end of this hour, you should be able to organize your tracker core into a package and run it without import confusion. The target result is not fancy. It is stable."

"Here is the vocabulary we need."

"First, a **module** is a Python file. `models.py` is a module. `services.py` is a module. `demo.py` is a module."

"Second, a **package** is a directory of modules that Python can treat as one organized unit. In today's structure, `tracker` is our package because it contains files such as `models.py`, `services.py`, and `__init__.py`."

"Third, `__init__.py` is the file that marks `tracker` as a regular Python package for our purposes. It can be empty. That is fine. Do not turn it into a second application. Today, its job is simply to say, 'This directory is package code.'"

"Fourth, `src` is a project organization folder. It keeps application code separate from project files such as `README.md`, notes, data folders, and later tests. In professional Python projects, `src` layout also helps avoid accidental imports from the wrong place. Today we are using a beginner-safe stepping stone version of that idea."

Write or display:

```text
project_root/
    src/
        tracker/
            __init__.py
            models.py
            services.py
            exceptions.py
            demo.py
```

"Fifth, an **entry point** is the code we run to start the program. Today our entry point is the demo module, `src/tracker/demo.py`, but we do not run it as a loose file. We run it as a module from the project root:"

```powershell
python -m src.tracker.demo
```

"If you use the Windows Python launcher, this is also acceptable:"

```powershell
py -m src.tracker.demo
```

"Sixth, an **absolute import** names the full import path from a location Python knows how to search. Later, after packaging is configured, you may see imports like `from tracker.services import TaskService`. Today we are not doing that because we have not installed the package and we have not configured packaging."

"Seventh, a **relative import** uses dots to import from nearby modules inside the same package. Inside `src/tracker/services.py`, we can write:"

```python
from .models import Task
from .exceptions import NotFoundError
```

"The dot means 'from this package.' This is practical inside the package because `services.py`, `models.py`, and `exceptions.py` live together."

"Finally, **config** means values that guide the application but are not the main business logic. Examples include `DATA_DIR`, `DB_PATH`, a default file name, or a log directory. Today we keep config light: constants in `config.py`, with an optional environment variable for one value."

**Transition**

"Now let's connect those terms to the real decisions that prevent import errors."

---

## Concept Briefing: Structure, Imports, and Config (12 minutes)

### 1. Why use `src/tracker/`?

**Instructor talk track**

"A flat project can be perfectly fine for a one-file exercise. But our capstone is no longer a one-file exercise. It is becoming an application with layers."

"A clean structure gives each layer a place to live. The package name, `tracker`, tells us this is the application core. The module names tell us the responsibilities:"

```text
models.py      domain objects such as Task
services.py    operations such as add, list, update, delete
exceptions.py  custom exceptions such as ValidationError and NotFoundError
demo.py        small runnable proof that the package works
config.py      optional constants such as DATA_DIR and DB_PATH
```

"This organization helps humans first. A new reader can find the model without scanning a giant script. A future GUI can import the service without copying code. A future API can call the same service. A future test can target one module."

"The organization also helps Python tools. Tools such as linters, test runners, and packaging systems expect code to have a consistent location. We are not going deep into those tools today, but we are preparing for them."

### 2. The import rule for this hour

"Here is the safest import rule for today's project:"

```text
Inside src/tracker/, use relative imports.
Run the demo from the project root with python -m src.tracker.demo.
```

"For example, `services.py` should not need to guess where `models.py` is. They are siblings inside the same package. So `services.py` can say:"

```python
from .models import Task
```

"That is different from:"

```python
from models import Task
```

"The second version sometimes works when files are flat and you run from one exact folder. Then it breaks after the move because Python is no longer searching the same place in the same way. Beginner projects often accumulate imports that work only by accident. We want imports that work because the structure is clear."

"It is also different from:"

```python
from tracker.models import Task
```

"That import is common in installed packages, and later packaging work may make it appropriate. But in this hour, we are not introducing `pyproject.toml`, editable installs, or changing `PYTHONPATH`. If we store code in `src/tracker/` and have not installed it, a root script that says `from tracker.models import Task` often fails because Python does not automatically treat `src` as the top of installed packages. To avoid teaching a broken half-step, we will use `python -m src.tracker.demo` and relative imports inside the package."

### 3. Why `python -m` matters

"The `-m` flag tells Python: run this module by its import path, not as a random loose file. That matters for relative imports."

"When we run:"

```powershell
python -m src.tracker.demo
```

"from the project root, Python understands that `demo.py` belongs to the `src.tracker` package path. Then `demo.py` can use imports such as:"

```python
from .services import TaskService
from .exceptions import ValidationError
```

"If we instead run:"

```powershell
python src/tracker/demo.py
```

"Python treats `demo.py` more like a standalone script. The package context can be missing, and relative imports may fail with a message like 'attempted relative import with no known parent package.' The file did not become bad. We ran it the wrong way."

Use this phrase:

```text
Package modules should be run as package modules.
```

### 4. Common import pitfalls

"There are three big pitfalls I want you to notice before they happen."

"First, **circular imports**. A circular import happens when two modules depend on each other during import time. For example, `models.py` imports `TaskService`, and `services.py` imports `Task`. Python begins loading `models.py`, then jumps to `services.py`, then jumps back to a half-loaded `models.py`. The result can be confusing errors."

"A good rule is: models should usually not import services. Models define the data and validation rules. Services use models. The dependency should mostly point one way:"

```text
services.py -> models.py
services.py -> exceptions.py
models.py -> exceptions.py
demo.py -> services.py
demo.py -> exceptions.py
```

"Second, **running the wrong entry file**. If relative imports fail, check the command before rewriting all the code. Are you in the project root? Did you run `python -m src.tracker.demo` exactly?"

"Third, **naming collisions**. Do not name your files after standard library modules. A file named `logging.py`, `json.py`, `email.py`, `pathlib.py`, or `sqlite3.py` can shadow the real standard library module. Then imports fail in surprising ways."

### 5. Light configuration

"Configuration is another small cleanup. If `services.py` hard-codes a path such as `'C:/Users/MyName/Desktop/tracker/data/tasks.json'`, the project will probably fail on someone else's computer. Even a relative string like `'data/tasks.json'` can become duplicated in several files."

"A light `config.py` gives those values one home:"

```python
from pathlib import Path

DATA_DIR = Path("data")
DB_PATH = DATA_DIR / "tracker.db"
```

"If we want a little flexibility, we can read an environment variable:"

```python
import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("TRACKER_DATA_DIR", "data"))
DB_PATH = DATA_DIR / "tracker.db"
```

"On Windows PowerShell, setting that environment variable for the current terminal looks like this:"

```powershell
$env:TRACKER_DATA_DIR = "data"
python -m src.tracker.demo
```

"This is intentionally light. We are not building a secrets manager or deployment system. We are learning the habit of centralizing values that multiple modules need."

**Transition**

"Now I will do the restructure live. Watch for two things: I move files first, then I update imports, then I run the exact module command from the project root."

---

## Live Demo: Move the Core into `src/tracker/` (10 minutes)

### Demo framing

**Instructor talk track**

"I am going to start from the checkpoint shape. Your exact project may differ, but the responsibilities should look familiar. I have a model called `Task`, a service called `TaskService`, custom exceptions, and a demo. If your code uses `TaskRecord` or `TrackerRecord`, adapt the names. Do not rename good code just to match mine."

"The before shape is:"

```text
project_root/
    exceptions.py
    models.py
    services.py
    demo.py
```

"The after shape for this hour is:"

```text
project_root/
    src/
        tracker/
            __init__.py
            exceptions.py
            models.py
            services.py
            demo.py
```

"The behavior should not change. We are changing the address of the code and the imports that connect it."

### Step 1: Create the package folders

Narrate while creating the folders in the editor or terminal:

```powershell
mkdir src
mkdir src\tracker
New-Item -ItemType File src\tracker\__init__.py
```

If a learner uses macOS/Linux syntax later, they can use `mkdir -p src/tracker` and `touch src/tracker/__init__.py`, but keep the live demo Windows-friendly if the room is Windows-based.

Say:

"The `__init__.py` file can be empty. Empty is not a problem. Empty means the package exists and we are not adding surprise behavior at import time."

### Step 2: Move the core files

Move:

```text
exceptions.py -> src/tracker/exceptions.py
models.py     -> src/tracker/models.py
services.py   -> src/tracker/services.py
demo.py       -> src/tracker/demo.py
```

Say:

"I am moving the demo inside the package for this hour because that lets us use one consistent execution command: `python -m src.tracker.demo`. Later in a fully packaged project, you might have a root command, console script, or installed package import. Not today."

### Step 3: Update `exceptions.py`

Show a compact version:

```python
class ValidationError(Exception):
    """Raised when task data violates a domain rule."""


class NotFoundError(Exception):
    """Raised when a requested task does not exist."""
```

Say:

"Exceptions usually do not need imports from the rest of the package. That makes them safe to import from both models and services."

### Step 4: Update `models.py`

Show:

```python
from .exceptions import ValidationError


class Task:
    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self, task_id: int, title: str, priority: str = "medium") -> None:
        cleaned_title = title.strip()
        cleaned_priority = priority.strip().lower()

        if not cleaned_title:
            raise ValidationError("Task title cannot be empty.")

        if cleaned_priority not in self.VALID_PRIORITIES:
            raise ValidationError(
                f"Priority must be one of: {sorted(self.VALID_PRIORITIES)}"
            )

        self.task_id = task_id
        self.title = cleaned_title
        self.priority = cleaned_priority
        self.completed = False

    def mark_complete(self) -> None:
        self.completed = True

    def to_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
        }

    def __repr__(self) -> str:
        return (
            "Task("
            f"task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"priority={self.priority!r}, "
            f"completed={self.completed!r}"
            ")"
        )
```

Say:

"Notice the import: `from .exceptions import ValidationError`. The dot matters. It tells Python that `exceptions.py` is a sibling module in the same package. I am not writing `from exceptions import ValidationError` anymore because this is no longer flat script code."

### Step 5: Update `services.py`

Show:

```python
from .exceptions import NotFoundError, ValidationError
from .models import Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def add(self, task: Task) -> None:
        if task.task_id in self._tasks:
            raise ValidationError(f"Task {task.task_id} already exists.")
        self._tasks[task.task_id] = task

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise NotFoundError(f"Task {task_id} was not found.") from exc

    def mark_complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.mark_complete()
        return task
```

Say:

"Again, the imports are relative because these modules live together. Also notice the dependency direction: service imports model; model does not import service. That helps avoid circular imports."

### Step 6: Update `demo.py`

Show:

```python
from .exceptions import NotFoundError, ValidationError
from .models import Task
from .services import TaskService


def run_demo() -> None:
    service = TaskService()

    service.add(Task(1, "Organize project", "high"))
    service.add(Task(2, "Add logging next", "medium"))
    service.mark_complete(1)

    print("Current tasks:")
    for task in service.list_all():
        print(task.to_dict())

    try:
        service.get(99)
    except NotFoundError as exc:
        print(f"Expected missing task error: {exc}")

    try:
        service.add(Task(3, "   ", "low"))
    except ValidationError as exc:
        print(f"Expected validation error: {exc}")


if __name__ == "__main__":
    run_demo()
```

Say:

"This demo proves the package still works. It uses the model, the service, both custom exceptions, and `to_dict()`. It also catches expected errors at the caller boundary. The service raises; the demo decides how to print."

### Step 7: Run from the project root

Show and run:

```powershell
python -m src.tracker.demo
```

Windows launcher variant:

```powershell
py -m src.tracker.demo
```

Expected output will be similar to:

```text
Current tasks:
{'task_id': 1, 'title': 'Organize project', 'priority': 'high', 'completed': True}
{'task_id': 2, 'title': 'Add logging next', 'priority': 'medium', 'completed': False}
Expected missing task error: Task 99 was not found.
Expected validation error: Task title cannot be empty.
```

Say:

"The validation instruction is simple: run this exact command from the project root. If it fails, read the error before changing code. The first questions are: Am I in the project root? Did I use `-m`? Are the imports inside the package relative? Is `__init__.py` present in `src/tracker/`?"

### Optional live add-on: `config.py`

If time allows, add:

```python
import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("TRACKER_DATA_DIR", "data"))
DB_PATH = DATA_DIR / "tracker.db"
```

Then mention:

"This does not connect to a database yet. `DB_PATH` is just a central constant we can use later. The value lives in one place instead of being copied through the code."

Show PowerShell syntax:

```powershell
$env:TRACKER_DATA_DIR = "data"
python -m src.tracker.demo
$env:TRACKER_DATA_DIR = $null
```

**Transition**

"Now it is your turn. Your lab goal is not to copy my exact `Task` class. Your lab goal is to move your working core into the package shape and prove the demo still runs."

---

## Guided Lab: Restructure Your Tracker (25 minutes)

### Lab prompt

**Instructor talk track**

"For the next 25 minutes, restructure your checkpoint project. Start with your working code. If your code was not fully complete at the checkpoint, still use the best current version. The focus is package structure and imports."

"Your target structure is:"

```text
project_root/
    src/
        tracker/
            __init__.py
            exceptions.py
            models.py
            services.py
            demo.py
```

"Adapt names if needed. If your project uses `TaskRecord` instead of `Task`, keep it. If your service is called `TrackerService` instead of `TaskService`, keep it. The required responsibilities are model, service, exceptions, and runnable demo."

### Required lab steps

1. Create the package folder.

```powershell
mkdir src
mkdir src\tracker
New-Item -ItemType File src\tracker\__init__.py
```

If the files or folders already exist, learners can skip or use the editor to create missing pieces.

2. Move existing files into the package.

```text
models.py -> src/tracker/models.py
services.py -> src/tracker/services.py
exceptions.py -> src/tracker/exceptions.py
demo.py -> src/tracker/demo.py
```

If learners currently have one large file, give this adaptation:

"Move the model class into `models.py`, the service class or service functions into `services.py`, custom exceptions into `exceptions.py`, and the runnable example into `demo.py`. Do not perfect every design detail during this lab. Make the responsibilities visible first."

3. Update package-internal imports.

Examples:

```python
from .models import Task
from .services import TaskService
from .exceptions import ValidationError, NotFoundError
```

Common replacements:

```text
from models import Task
becomes
from .models import Task

from exceptions import ValidationError
becomes
from .exceptions import ValidationError
```

4. Confirm dependency direction.

Use this quick map:

```text
models.py should not import services.py
services.py may import models.py
models.py and services.py may import exceptions.py
demo.py may import models.py, services.py, and exceptions.py
```

5. Run the demo from the project root.

Required validation command:

```powershell
python -m src.tracker.demo
```

Windows launcher variant:

```powershell
py -m src.tracker.demo
```

Tell learners:

"Do not validate this lab by running `python src/tracker/demo.py`. That may fail even when your package is correct, because it runs the file outside the package context. Use the exact module command."

6. Confirm the demo behavior.

Minimum evidence:

- At least one valid `Task` or equivalent model is created.
- The service adds and lists records.
- At least one `to_dict()` result is shown or inspected.
- A missing record path raises or catches `NotFoundError`.
- An invalid input path raises or catches `ValidationError`.
- The demo command exits without an import error.

### Optional extension: add `config.py`

If learners finish early, ask them to add:

```python
import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("TRACKER_DATA_DIR", "data"))
DB_PATH = DATA_DIR / "tracker.db"
```

Then import it where useful:

```python
from .config import DATA_DIR, DB_PATH
```

Suggested light use in `demo.py`:

```python
from .config import DATA_DIR, DB_PATH


def show_config() -> None:
    print(f"Data directory: {DATA_DIR}")
    print(f"Database path: {DB_PATH}")
```

Keep the extension limited:

"Do not build a database layer right now. Do not add deployment settings. Do not introduce a config framework. The extension is only to centralize constants."

### Instructor circulation guide

As learners work, circulate with these prompts:

- "Show me the command you are using to run the demo."
- "Which file imports `Task`?"
- "Does `models.py` import `services.py`? If yes, can we reverse that dependency?"
- "Is `__init__.py` present in `src/tracker/`?"
- "Are you importing with `from .models import ...` inside the package?"
- "Did any file get named `logging.py`, `json.py`, `email.py`, `pathlib.py`, or `sqlite3.py`?"
- "What changed: behavior, or only structure and imports?"

Use this intervention when a learner has a `ModuleNotFoundError`:

1. Ask them not to change code yet.
2. Ask them to show the current working directory.
3. Ask them to show the exact command.
4. Ask them to show the failing import line.
5. Decide whether the problem is command context, missing file, missing `__init__.py`, spelling/case mismatch, or inconsistent import style.

Say:

"Import errors are feedback about how Python is finding code. Do not randomly add folders to `sys.path`. First make the structure and command consistent."

### Completion criteria

Learners are done when:

- `src/tracker/__init__.py` exists.
- `models.py` and `services.py` are inside `src/tracker/`.
- Custom exceptions are available from `src/tracker/exceptions.py` or an equivalent package module.
- Imports inside `src/tracker/` are clean and consistent, preferably relative imports.
- The project runs after restructure using `python -m src.tracker.demo` from the project root.
- The demo still proves the core behavior from Checkpoint 1.
- No module is named after a standard library package.
- Optional: `config.py` contains simple constants such as `DATA_DIR` and `DB_PATH`.

### If learners finish early

Give one of these small extensions:

1. Add `config.py` with `DATA_DIR` and `DB_PATH`.
2. Add a short package comment to `__init__.py`, such as a one-line docstring.
3. Improve the demo output so it clearly labels happy path and expected error path.
4. Add one more deterministic service operation to the demo, such as mark complete or delete.

Do not let fast finishers jump into publishing packages, full packaging metadata, dependency managers, or deployment. Keep the hour scoped.

---

## Quick Checks, Pitfalls, and Wrap-Up (3 minutes)

### Quick check

Ask:

"What usually causes `ModuleNotFoundError` in student projects when they start restructuring?"

Expected answers:

- Running from the wrong directory.
- Running the wrong entry file, such as `python src/tracker/demo.py` instead of `python -m src.tracker.demo`.
- Using flat imports like `from models import Task` after files moved into a package.
- Forgetting `src/tracker/__init__.py`.
- Spelling or capitalization mismatch in file names or package names.
- Naming a module after a standard library module.
- Assuming `from tracker...` works even though the package has not been installed and packaging has not been configured.

Affirm:

"Good. The big habit is to check the command, the working directory, and the import style before rewriting the application."

### Pitfall review

Use this table quickly:

| Pitfall | Symptom | Fix for this hour |
| --- | --- | --- |
| Circular imports | Partially initialized module errors or imports that fail unpredictably | Keep dependencies one-way: services use models; models do not use services |
| Running the wrong entry file | Relative import error or no known parent package | Run from project root with `python -m src.tracker.demo` |
| Flat imports after moving files | `ModuleNotFoundError: No module named 'models'` | Use `from .models import Task` inside `src/tracker/` |
| Standard library name collision | `import logging` or `import json` behaves strangely | Rename local files that shadow standard library modules |
| Over-scoping config | Learners start building deployment settings or secret systems | Keep `config.py` to constants such as `DATA_DIR` and `DB_PATH` |

### Closing bridge to Day 3 Hour 2

**Instructor talk track**

"Today we did a quiet but important professional move. We did not add a flashy new feature. We made the existing core easier to find, easier to import, and easier to grow. That matters because the next hour adds logging and error reporting."

"Logging works best when the project has a predictable shape. If services live in `services.py`, we know where service logs belong. If custom exceptions live in `exceptions.py`, we know what errors we are reporting. If the demo runs as a module, we can trigger success and failure paths consistently."

"So the bridge is:"

```text
Clean structure makes clean diagnostics possible.
```

"Next hour, we will add practical logging. We will use levels such as DEBUG, INFO, WARNING, and ERROR. We will log service events and expected errors without dumping confusing stack traces on end users. The structure you created today gives that logging work a stable place to attach."

### Exit ticket

Ask learners to write or say one sentence:

"What import or structure rule will you check first the next time you see `ModuleNotFoundError`?"

Collect two or three answers if time allows. End with:

"For now, your validation command is still the same: from the project root, run `python -m src.tracker.demo`. If that works, you have completed the core restructure for this hour."
