# Day 3, Hour 2: Logging and Error Reporting (Practical)

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 3, Hour 2 of 48, also Hour 10 in the Advanced runbook sequence
- **Focus**: Using Python's built-in `logging` module to record useful diagnostics while keeping user-facing error messages friendly.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 3, Hour 10.
- **Prerequisites**: Learners should have completed Day 3 Hour 1 or have an equivalent project shape: `project_root/src/tracker/` contains package code, `src/tracker/demo.py` is the runnable demo module, and the project runs from the project root with `python -m src.tracker.demo` or `py -m src.tracker.demo` on Windows.
- **Advanced trajectory**: This hour stays on the PCAP-to-PCPP1 path. Learners are not adopting a logging framework, observability platform, JSON logging pipeline, or production security policy. The advanced step is learning to separate diagnostics from user communication and to place logging in the service layer without creating noise.
- **Instructor goal**: By the end of this hour, every learner has configured logging to write to `logs/app.log`, added at least three useful service-layer log calls, triggered one expected error, confirmed the log file is created and populated, and kept user-facing messages clean.

Important instructor positioning:

- Continue the Day 3 Hour 1 execution convention exactly. The package lives at `project_root/src/tracker/`. The demo lives at `src/tracker/demo.py`. Run from the project root with `python -m src.tracker.demo`; on Windows, `py -m src.tracker.demo` is also acceptable.
- Inside `src/tracker/`, use relative imports such as `from .exceptions import ValidationError, NotFoundError`, `from .models import Task`, `from .services import TaskService`, and `from .config import LOG_DIR, LOG_FILE`.
- Use consistent vocabulary: `Task`, `TaskService`, `ValidationError`, `NotFoundError`, `src/tracker/config.py`, `src/tracker/demo.py`, and `logs/app.log`. Tell learners to adapt names to their own checkpoint code while preserving responsibilities.
- Keep the distinction visible all hour: **logs are for developers; user messages are for users**.
- The live demo should show a log file being created, populated, and inspected. Do not only describe file logging; run it and show the file contents.
- Include stack details in logs when useful, but never dump raw tracebacks to end users. Demonstrate `logger.exception(...)` or `logger.error(..., exc_info=True)` as a developer diagnostic tool.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from project structure | 5 min | Connect Day 3 Hour 1 package structure to predictable log placement |
| Outcomes, vocabulary, and mental model | 5 min | Define diagnostics, user-facing messages, log records, logger names, and levels |
| Concept briefing: levels, formatting, and file logging | 10 min | Teach `DEBUG`, `INFO`, `WARNING`, `ERROR`, format strings, `logs/app.log`, and safe startup configuration |
| Live demo: add logging to `TaskService` | 10 min | Configure `logs/app.log`, add service-layer logs, log `ValidationError` and `NotFoundError`, and show output |
| Guided lab: add practical logging | 25 min | Learners configure logging, add at least three service-layer log calls, trigger one error, and confirm the log file |
| Exit ticket, pitfalls, and wrap-up | 5 min | Check `WARNING` vs `ERROR`, review common pitfalls, and bridge to context managers |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If discussion runs long, shorten instructor narration in the concept briefing rather than shrinking student practice. The required outcome is practical: `logs/app.log` exists, contains useful entries, and users still see friendly messages instead of raw stack traces.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain why `logging` is better than scattered `print()` statements for diagnostics in a growing project.
2. Use the built-in `logging` module to create module-level loggers with `logging.getLogger(__name__)`.
3. Choose practical logging levels: `DEBUG`, `INFO`, `WARNING`, and `ERROR`.
4. Configure logging near program startup to write to `logs/app.log`.
5. Create the `logs/` directory in code with `LOG_DIR.mkdir(parents=True, exist_ok=True)` before writing logs.
6. Add at least three meaningful log calls in the service layer without logging inside noisy tight loops.
7. Log expected application errors such as `ValidationError` and `NotFoundError`.
8. Use `logger.exception(...)` or `logger.error(..., exc_info=True)` to record developer stack details without printing them to the user.
9. Keep user-facing messages friendly, short, and actionable.
10. Inspect `logs/app.log` and explain whether each entry is helpful.
11. Recognize common pitfalls: forgotten `logs/` directory, vague log messages, logging everything as `ERROR`, and producing noisy logs.
12. Prepare for the next hour, where context managers and safer file operations will make persistence logging more important.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 3, Hour 10 visible. The required scope is practical logging and error reporting: logging levels, formatting, file logging, friendly user messages, and a lab that writes to `logs/app.log`.
- Open or review the Day 3 Hour 1 lecture conventions. This hour must continue the same import and execution pattern:

```text
project_root/
    src/
        tracker/
            __init__.py
            config.py
            exceptions.py
            models.py
            services.py
            demo.py
    logs/
        app.log
```

- Prepare a small working tracker core or be ready to type the code from the live demo. The demo assumes these responsibilities:
  - `Task` validates title data and can raise `ValidationError`.
  - `TaskService` stores tasks and raises `NotFoundError` when a requested task does not exist.
  - `src/tracker/demo.py` catches expected application errors and prints friendly messages.
- Decide how to handle learner naming differences. Use this sentence: "I will use `Task`, `TaskService`, `ValidationError`, and `NotFoundError`. If your checkpoint uses `TaskRecord`, `InventoryItem`, `ContactService`, or a different exception name, adapt the names while preserving the responsibilities."
- Prepare the board with the hour's central rule:

```text
Developer diagnostics go to logs/app.log.
Friendly user messages go to the terminal or UI.
Do not print raw stack traces to end users.
```

- Prepare a second board note for log levels:

```text
DEBUG   - detailed developer-only information
INFO    - normal important events
WARNING - unexpected but recoverable event
ERROR   - operation failed
```

- Be ready to explain one subtle configuration issue: `logging.basicConfig(...)` can be a no-op if logging has already been configured in a long-running interpreter session, notebook, test runner, or larger application. For this course script, place it near program startup in `src/tracker/demo.py`, before other code emits logs.
- Avoid naming any file `logging.py`. If a learner creates `logging.py`, it can shadow the standard library `logging` module and cause confusing import errors.

---

## Opening Bridge from Project Structure (5 minutes)

### Instructor talk track

"Welcome back. In the previous hour, we gave our tracker code a predictable home. Instead of keeping everything loose in the project root, we moved toward a structure like this."

Display:

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

"That structure was not just cleanup for cleanup's sake. It makes the next features easier. Today is the first payoff. Because our application code lives in `src/tracker/`, we can now decide where diagnostic output belongs. We are going to keep source code in `src/tracker/`, and we are going to write runtime logs to `logs/app.log`."

Display:

```text
project_root/
    src/tracker/      application code
    logs/app.log      diagnostic output
```

"This gives us a stable mental model. Code lives in one place. Logs live in another. Users do not need to read log files, but developers do. That separation matters as soon as an application has more than one file, more than one user action, or more than one possible failure."

"At the end of Day 2, your core tracker could already raise meaningful custom exceptions such as `ValidationError` and `NotFoundError`. That was good design. Today we add another layer: when those errors happen, how do we record enough detail for a developer without overwhelming the person using the program?"

Write:

```text
Logs are for developers.
Error messages are for users.
```

"Keep that sentence in mind. It is the whole hour in one line."

Pause and ask:

"Think about the last time you saw a giant error traceback. Did it help you as a user, or did it feel like the program was broken in a confusing way?"

Take two or three quick answers. Expect learners to mention long red tracebacks, file paths, line numbers, or messages they did not understand.

Affirm:

"Exactly. A traceback can be incredibly useful to a developer. It is usually not the right user interface. Our goal today is not to hide problems. Our goal is to route information to the right audience."

### Transition

"Let's define the vocabulary, then we will configure logging in the same package structure we created last hour."

---

## Outcomes, Vocabulary, and Mental Model (5 minutes)

### Instructor talk track

"By the end of this hour, your project should do three things it probably does not do yet."

Display:

```text
1. Create logs/app.log automatically.
2. Record meaningful service-layer events.
3. Keep user-facing errors friendly.
```

"Let's name a few terms."

"A **diagnostic** is information that helps a developer understand what the program did. For example, 'created task_id=3' or 'missing task_id=999' is diagnostic information."

"A **user-facing message** is what the person using the program sees. For example, 'Task 999 was not found.' That message should be clear, but it does not need a Python traceback, module path, or internal object representation."

"A **log record** is one entry written by the logging system. A useful log record usually answers at least one of these questions:"

- "When did this happen?"
- "How severe was it?"
- "Which module produced it?"
- "What operation was attempted?"
- "Which task, file, or ID was involved?"

"A **logger** is the object our code uses to emit log records. In a module, the standard pattern is:"

```python
import logging

logger = logging.getLogger(__name__)
```

"The `__name__` part is useful because it lets the log entry identify where it came from. If the log came from `src.tracker.services`, we want to know that. When projects grow, knowing the source module saves time."

"A **logging level** is the severity label. Today we will use four levels in practical ways: `DEBUG`, `INFO`, `WARNING`, and `ERROR`."

"One more important boundary: logging does not replace exceptions. If your service method cannot find a task, it can still raise `NotFoundError`. Logging records what happened. Exceptions still control program behavior."

Display:

```text
Logging records the event.
Exceptions control the flow.
User messages explain the result.
```

"That is the mental model. Now let's make it concrete."

---

## Concept Briefing: Levels, Formatting, and File Logging (10 minutes)

### Why `print()` is not enough

**Instructor talk track**

"Most of us start debugging with `print()`. That is normal. `print()` is simple, immediate, and useful while exploring. But as the application grows, `print()` starts to create problems."

List:

- "`print()` has no built-in severity level."
- "`print()` does not include timestamps unless we manually add them."
- "`print()` mixes developer diagnostics with user output."
- "`print()` is easy to forget in the middle of service logic."
- "`print()` usually disappears when the terminal closes."

"Imagine a service method prints this:"

```text
not found
```

"What was not found? Which ID? Which module printed it? Was the program able to continue? Was it a warning, or did an operation fail? The message might have helped for ten seconds while writing the code, but it is weak as a diagnostic."

"Logging lets us write something like this instead:"

```text
2026-01-14 10:03:22,442 WARNING src.tracker.services Missing task lookup task_id=999
```

"Now a future developer has more context. There is a time, a level, a module name, and a useful message."

### Practical logging levels

**Instructor talk track**

"Do not treat logging levels as trivia. Treat them as communication signals."

Display:

```text
DEBUG   - detailed developer-only information
INFO    - normal important events
WARNING - unexpected but recoverable event
ERROR   - operation failed
```

"Here is how I want you to think about them in this project."

"Use `DEBUG` for details that are useful while developing but too noisy for normal runs. For example, you might log which branch of a strategy was selected or how many candidate tasks were inspected. In today's default configuration, we will write `INFO` and above, so `DEBUG` messages will usually not appear unless we lower the threshold."

"Use `INFO` for normal important events. A service starting, a task being added, or a task being updated can be `INFO`. Do not log every tiny line of code. Log meaningful transitions."

"Use `WARNING` when something unexpected happened but the program can recover. A lookup for a missing task can often be a warning. It did not crash the whole program, but it is worth recording."

"Use `ERROR` when an operation failed. If validation prevents a task from being created, or saving data fails because the path is not writable, that is an error. The application may continue, but the requested operation did not succeed."

Use quick scenarios, but do not answer the exit-ticket question fully yet:

"If a task is created successfully, I would probably use `INFO`. If a lookup asks for task 999 and that task does not exist, I would consider `WARNING` in many applications. If task creation fails because required data is invalid, I would use `ERROR` for the failed operation."

"The exact level can depend on the application, but the reasoning should be clear."

### Formatting and file logging

**Instructor talk track**

"For this hour, our log target is concrete: `logs/app.log`. We want a file so the terminal does not become the only record. We also want a format that includes the optional extension from the runbook: timestamp and module name."

Show the target format:

```python
format="%(asctime)s %(levelname)s %(name)s %(message)s"
```

"This format says: include the time, the severity level, the logger name, and the message. It is short enough to read and useful enough to debug."

"We also need to create the `logs/` directory before writing the file. Forgetting this is one of today's required pitfalls. The logging system will not magically create every missing parent directory for us. So in our `config.py`, we define paths, and in our startup code we create the directory."

Show:

```python
LOG_DIR.mkdir(parents=True, exist_ok=True)
```

"That line is safe to run repeatedly. If the directory already exists, it does not fail."

### Configuration near startup

**Instructor talk track**

"The configuration step belongs near program startup. In this hour, that means `src/tracker/demo.py`, before we create services or run operations that might log."

Show:

```python
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
```

"One instructor note and one real-world note: `logging.basicConfig(...)` configures the root logging setup only if logging has not already been configured. In a long-running session, a notebook, a test runner, or a larger app, calling it later may do nothing. For this course script, run it near startup before other logging happens. That keeps the behavior deterministic for today's project."

"We are not going deeper into handlers, logger hierarchy, JSON logs, or observability platforms today. Those are real topics, but not today's target. Today we need practical, readable logs in a file and clean messages for users."

### Stack traces: developer detail, not user output

**Instructor talk track**

"Now let's talk about stack traces. A traceback is not bad. It is a developer tool. The mistake is showing raw tracebacks to end users as if they are normal messages."

"When an unexpected exception happens, or when you are intentionally capturing developer details, logging can store stack information in the log file. Two common patterns are:"

```python
logger.exception("Failed to create task from demo input")
```

"Use `logger.exception(...)` inside an `except` block. It logs at `ERROR` level and automatically includes the traceback."

```python
logger.error("Failed to create task from demo input", exc_info=True)
```

"This is similar. `exc_info=True` tells logging to attach exception details. The point is not that users should see that traceback. The point is that developers can inspect `logs/app.log` later."

"In a moment, we will trigger both a validation error and a missing-task error. The user will see friendly messages. The log file will contain the developer detail."

---

## Live Demo: Add Logging to `TaskService` (10 minutes)

### Demo framing

**Instructor talk track**

"In this demo, we are going to add logging to the same package shape from last hour. Watch for three things."

Display:

```text
1. Configure logging once near startup.
2. Put useful log calls in the service layer.
3. Catch expected errors in `src/tracker/demo.py` and print friendly messages.
```

"We are not going to build a new application. We are improving the diagnostic behavior of the project we already have."

### Step 1: Add logging paths in `src/tracker/config.py`

**Instructor action**

Open `src/tracker/config.py`. If it does not exist, create it. Type or adapt:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"
```

**Instructor explanation**

"This file gives us named paths. `Path(__file__).resolve()` starts from the current file, which is `src/tracker/config.py`. `parents[2]` walks up to the project root in this course layout."

Sketch:

```text
project_root/
    src/
        tracker/
            config.py
```

"From `config.py`, parent 0 is `tracker`, parent 1 is `src`, and parent 2 is the project root. That is why `LOG_DIR` becomes `project_root/logs` and `LOG_FILE` becomes `project_root/logs/app.log`."

"If your project structure is different, adapt this carefully. The responsibility is what matters: configuration should point to a predictable log path."

### Step 2: Add a logger and service-layer log calls in `src/tracker/services.py`

**Instructor action**

Open `src/tracker/services.py`. Use relative imports inside the package. Type or adapt:

```python
import logging

from .exceptions import NotFoundError, ValidationError
from .models import Task

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        logger.info("TaskService initialized")

    def add(self, task: Task) -> None:
        if task.task_id in self._tasks:
            logger.warning("Rejected duplicate task_id=%s", task.task_id)
            raise ValidationError(f"Task {task.task_id} already exists.")

        self._tasks[task.task_id] = task
        logger.info("Added task_id=%s title=%r", task.task_id, task.title)

    def get(self, task_id: int) -> Task:
        try:
            task = self._tasks[task_id]
        except KeyError as exc:
            logger.warning("Missing task lookup task_id=%s", task_id)
            raise NotFoundError(f"Task {task_id} was not found.") from exc

        logger.debug("Retrieved task_id=%s", task_id)
        return task
```

**Instructor explanation**

"The first thing to notice is the import style. Inside `src/tracker/`, we use relative imports: `from .exceptions import NotFoundError, ValidationError` and `from .models import Task`. That continues the Day 3 Hour 1 convention."

"The second thing to notice is the module-level logger:"

```python
logger = logging.getLogger(__name__)
```

"This does not configure the file. It creates a named logger for this module. Configuration happens once in the startup module."

"Now look at the log calls. We have at least three useful service-layer log calls: service initialized, task added, duplicate rejected, missing lookup, and debug retrieval. We do not need all of these in every learner project, but this shows the pattern."

"Notice that the service still raises exceptions. Logging did not replace `ValidationError` or `NotFoundError`. The service logs the event and raises the appropriate application exception."

"Also notice that we are not logging inside a loop. If we had thousands of tasks and logged every comparison while searching, the log file would become noisy. We log the meaningful outcome."

### Step 3: Configure logging and keep friendly messages in `src/tracker/demo.py`

**Instructor action**

Open `src/tracker/demo.py`. Type or adapt:

```python
import logging

from .config import LOG_DIR, LOG_FILE
from .exceptions import NotFoundError, ValidationError
from .models import Task
from .services import TaskService


def configure_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting tracker logging demo")

    service = TaskService()

    try:
        service.add(Task(task_id=1, title="Write logging notes"))
        service.get(999)
    except NotFoundError as exc:
        logger.warning("Demo requested a missing task: %s", exc)
        print("That task was not found. Please check the task ID and try again.")

    try:
        service.add(Task(task_id=1, title="Duplicate logging notes"))
    except ValidationError:
        logger.exception("Demo could not add task because validation failed")
        print("That task could not be saved. Please check the task details.")

    print(f"Demo complete. Developer log written to {LOG_FILE}")


if __name__ == "__main__":
    main()
```

**Instructor explanation**

"This file is the startup point for today's demo. We create the logs directory in code with `LOG_DIR.mkdir(parents=True, exist_ok=True)`. That avoids the common failure where `logs/` does not exist."

"We configure logging before creating the service. That matters because the service logs during initialization."

"Look at the two `except` blocks. For `NotFoundError`, we use a warning-level log because the demo intentionally requested a missing task and then recovered with a friendly message."

"For `ValidationError`, I used `logger.exception(...)`. This is a concrete example of storing developer stack details in the log. The user still sees only:"

```text
That task could not be saved. Please check the task details.
```

"The traceback belongs in `logs/app.log`, not in the user's face."

"If you prefer the explicit style, this line would also record exception information inside an `except` block:"

```python
logger.error("Demo could not add task because validation failed", exc_info=True)
```

"Today, I am showing `logger.exception(...)` because it is concise and common inside `except` blocks."

### Step 4: Run from the project root

**Instructor action**

In the terminal, make sure the current directory is `project_root`, not `src/tracker`. Run:

```powershell
python -m src.tracker.demo
```

If the room uses the Windows Python launcher, also show:

```powershell
py -m src.tracker.demo
```

**Instructor explanation**

"This command is not optional trivia. It is part of the import convention from last hour. We are running the demo as a module from the project root. We are not running the package file as a loose script, and we are not teaching a shortened installed-package module path in this hour."

"If a learner gets an import error, first check the working directory and the command. Then check relative imports."

Expected terminal output:

```text
That task was not found. Please check the task ID and try again.
That task could not be saved. Please check the task details.
Demo complete. Developer log written to C:\...\logs\app.log
```

"Your path will differ, but the important part is that the user sees friendly messages."

### Step 5: Show `logs/app.log`

**Instructor action**

Open `logs/app.log` in the editor or display it in the terminal. The exact timestamps and paths will differ, but the log should resemble:

```text
2026-01-14 10:03:22,442 INFO __main__ Starting tracker logging demo
2026-01-14 10:03:22,443 INFO src.tracker.services TaskService initialized
2026-01-14 10:03:22,443 INFO src.tracker.services Added task_id=1 title='Write logging notes'
2026-01-14 10:03:22,443 WARNING src.tracker.services Missing task lookup task_id=999
2026-01-14 10:03:22,443 WARNING __main__ Demo requested a missing task: Task 999 was not found.
2026-01-14 10:03:22,444 WARNING src.tracker.services Rejected duplicate task_id=1
2026-01-14 10:03:22,444 ERROR __main__ Demo could not add task because validation failed
Traceback (most recent call last):
  ...
ValidationError: Task 1 already exists.
```

**Instructor explanation**

"This is the contrast I want everyone to see. The terminal output stayed friendly. The log file contains developer detail. The traceback is not gone; it is in the right place."

"Also notice the logger names. We can tell which records came from `src.tracker.services`. The startup module appears as `__main__` here because we ran `src.tracker.demo` with `python -m`; that is normal for an entry module. This is why `logging.getLogger(__name__)` is helpful, and it is also why the exact name of the entry logger may differ from package modules."

### Demo debrief

Ask:

"Which log entries would help you debug a learner project tomorrow?"

Listen for:

- "The missing task ID is included."
- "The validation failure is recorded."
- "The module names show where the messages came from."
- "The traceback is available in the file, not printed to the user."

Affirm:

"Exactly. Useful logs are specific, readable, and placed where a developer can find them."

---

## Guided Lab: Add Practical Logging (25 minutes)

### Lab framing

**Instructor talk track**

"Now you will add the same idea to your own checkpoint project. Your goal is not to create as many log lines as possible. Your goal is to add a small number of useful log lines at meaningful points."

"Work in your existing Day 3 package structure if you have it. If your project is still catching up, use the target structure from last hour and adapt your names."

Display:

```text
Required lab result:
1. Configure logging to write to logs/app.log.
2. Add at least 3 log calls in the service layer.
3. Trigger one error.
4. Confirm the error appears in logs/app.log.
5. Keep user-facing messages friendly.
```

### Student task checklist

Give learners this checklist:

1. In `src/tracker/config.py`, define `LOG_DIR` and `LOG_FILE`.

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"
```

2. In `src/tracker/demo.py`, configure logging near startup.

```python
import logging

from .config import LOG_DIR, LOG_FILE


def configure_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
```

3. In `src/tracker/services.py`, create a module-level logger.

```python
import logging

logger = logging.getLogger(__name__)
```

4. Add at least three useful service-layer log calls. Good candidates:

- `logger.info(...)` when the service initializes.
- `logger.info(...)` when a task is created, updated, or deleted.
- `logger.warning(...)` when a requested task is missing.
- `logger.error(...)` when validation rejects an operation.
- `logger.debug(...)` for a low-level detail that should usually stay hidden.

5. Trigger one expected error, such as:

- creating a `Task` with invalid data,
- adding a duplicate task ID,
- requesting a task ID that does not exist,
- updating or deleting a missing task.

6. Catch the expected exception in `src/tracker/demo.py` and print a friendly message.

```python
try:
    service.get(999)
except NotFoundError as exc:
    logger.warning("User requested missing task during demo: %s", exc)
    print("That task was not found. Please check the task ID and try again.")
```

7. For at least one caught exception, record developer stack details without printing them to the user.

```python
try:
    service.add(Task(task_id=1, title="Duplicate logging notes"))
except ValidationError:
    logger.exception("Could not add task because validation failed")
    print("That task could not be saved. Please check the task details.")
```

8. Run from the project root.

```powershell
python -m src.tracker.demo
```

Windows launcher option:

```powershell
py -m src.tracker.demo
```

9. Open `logs/app.log` and confirm it contains useful entries.

### Lab timing guidance for instructor

Use the 25 minutes intentionally:

- **Minutes 0-3**: Learners copy or adapt `config.py` and logging configuration.
- **Minutes 3-8**: Learners add `logger = logging.getLogger(__name__)` and the first two service-layer log calls.
- **Minutes 8-13**: Learners add a missing-record or validation log call.
- **Minutes 13-18**: Learners update `src/tracker/demo.py` to catch expected errors and print friendly messages.
- **Minutes 18-22**: Learners run `python -m src.tracker.demo`, inspect `logs/app.log`, and fix import/path mistakes.
- **Minutes 22-25**: Learners mark completion criteria and prepare one log line to explain during debrief.

### Completion criteria

Learners are done when:

- `logs/app.log` is created under the project root.
- `logs/app.log` is populated after running `python -m src.tracker.demo`.
- The service layer contains at least three meaningful log calls.
- At least one `ValidationError` or `NotFoundError` path is triggered and recorded.
- At least one log entry includes useful context such as a task ID, title, or operation name.
- User-facing terminal output remains friendly and does not print a raw traceback.
- The project still uses the Day 3 package convention: demo at `src/tracker/demo.py`, package-internal relative imports, and module execution from the project root.

### Instructor circulation prompts

Use these questions while circulating:

- "What question will this log line help you answer later?"
- "Is this message for the user or for a developer?"
- "If this log line appeared 500 times, would it still be useful?"
- "Does the log include the task ID or operation that failed?"
- "Are you logging the event and still raising or handling the exception appropriately?"
- "Are you running from the project root with `python -m src.tracker.demo`?"
- "Did your code create `logs/` before logging to `logs/app.log`?"

### Common learner situations and coaching moves

#### Situation: The log file is not created

Check:

- Did they call `configure_logging()`?
- Did they create the directory with `LOG_DIR.mkdir(parents=True, exist_ok=True)`?
- Are they running the correct demo module?
- Did logging happen before `basicConfig(...)`?
- Are they looking in the project root `logs/` folder, not inside `src/tracker/`?

Coaching line:

"Let's verify the startup order. Logging configuration should happen before the service starts logging, and the directory should exist before the file handler opens."

#### Situation: Imports fail

Check:

- Are they inside `src/tracker/` using relative imports?
- Are they running from the project root?
- Did they accidentally run `python src/tracker/demo.py`?
- Did they rename or omit `__init__.py`?

Coaching line:

"This is the same import rule from last hour. Inside the package, use relative imports. From the project root, run the module with `python -m src.tracker.demo`."

#### Situation: User sees a traceback

Check:

- Is the exception caught in `src/tracker/demo.py`?
- Are they using `logger.exception(...)` inside the `except` block instead of letting the exception escape?
- Are they printing `traceback.format_exc()` or using `raise` after printing a friendly message?

Coaching line:

"A traceback can go in the log file. The user message should be a sentence they can act on."

#### Situation: Every event is logged as `ERROR`

Check:

- Is a successful operation being labeled as failure?
- Is a recoverable missing lookup being treated the same as a failed save?

Coaching line:

"Severity should describe what happened, not how important logging feels. A successful add is `INFO`; a recoverable missing lookup may be `WARNING`; a failed operation is `ERROR`."

#### Situation: Logs are noisy

Check:

- Are they logging inside a tight loop?
- Are they logging every field of every object repeatedly?
- Are they duplicating the same message in multiple layers?

Coaching line:

"The goal is signal, not volume. A useful log line should earn its place."

### Optional extension

If learners finish early, ask them to improve formatting or inspect logger names.

Required extension option from the runbook:

```python
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
```

Challenge questions:

- "Can you include a timestamp?"
- "Can you include the module name?"
- "Can you identify which log lines came from `src.tracker.services` and which came from the entry module (`__main__` when run with `python -m`)?"

Keep the extension small. Do not expand into handler hierarchies, rotating files, JSON logs, multiprocessing logging, pytest `caplog`, or external logging services today.

---

## Exit Ticket, Pitfalls, and Wrap-Up (5 minutes)

### Quick debrief

**Instructor talk track**

"Let's bring it back together. I want one volunteer to describe a log entry they created. Tell us the level, the message, and why it belongs in the log rather than as a user-facing print."

Take one or two examples. Praise specificity:

- "Good: it includes the task ID."
- "Good: it distinguishes the developer log from the user message."
- "Good: it logs the failed operation without dumping the traceback to the terminal."

### Required quick check / exit ticket

Ask learners to answer in one or two sentences:

**When should you log at `WARNING` vs `ERROR`?**

Expected answer:

- Use `WARNING` when something unexpected happened but the application can recover or continue, such as a missing optional record lookup that is handled cleanly.
- Use `ERROR` when an operation meaningfully failed, such as validation preventing a save, a file write failing, or a required operation not completing.

Follow-up if needed:

"The difference is not whether you personally care about the event. The difference is what happened to the operation."

### Pitfalls to name explicitly

Review:

1. **Logging inside tight loops/noise**
   - "If a loop runs 10,000 times, a log call inside that loop can bury the important event. Log the summary or the meaningful outcome unless you are deliberately debugging at `DEBUG` level."

2. **Forgetting to create `logs/`**
   - "Use `LOG_DIR.mkdir(parents=True, exist_ok=True)` before configuring file logging."

3. **Printing stack traces to end users**
   - "Use `logger.exception(...)` or `logger.error(..., exc_info=True)` for developer detail. Print a friendly message for the user."

4. **Configuring logging too late**
   - "For this course script, configure logging near startup before other modules emit logs. Remember that `basicConfig(...)` can be a no-op if logging is already configured in a long-running environment."

5. **Breaking the import convention**
   - "Continue using `src/tracker/demo.py`, relative imports inside `src/tracker/`, and `python -m src.tracker.demo` from the project root."

### Final wrap-up

**Instructor closing line**

"Today your tracker learned how to leave a useful trail. That trail is not for the user to read during normal use. It is for future debugging, future maintenance, and future you."

"The most important pattern is this:"

```text
Raise or handle the exception so the program behaves correctly.
Log enough detail so a developer can diagnose it.
Show the user a friendly message they can understand.
```

"Next hour we move into context managers and safer file operations. That will connect directly to today's logging. When file reads and writes become more important, logs help us understand what was saved, what failed, and where to look when something goes wrong."

---

## Instructor Reference: Minimal Demo Files

Use this reference only if you need a compact version during class. Adapt to learner code rather than forcing exact names when their responsibilities are correct.

### `src/tracker/config.py`

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"
```

### `src/tracker/services.py`

```python
import logging

from .exceptions import NotFoundError, ValidationError
from .models import Task

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        logger.info("TaskService initialized")

    def add(self, task: Task) -> None:
        if task.task_id in self._tasks:
            logger.warning("Rejected duplicate task_id=%s", task.task_id)
            raise ValidationError(f"Task {task.task_id} already exists.")

        self._tasks[task.task_id] = task
        logger.info("Added task_id=%s title=%r", task.task_id, task.title)

    def get(self, task_id: int) -> Task:
        try:
            task = self._tasks[task_id]
        except KeyError as exc:
            logger.warning("Missing task lookup task_id=%s", task_id)
            raise NotFoundError(f"Task {task_id} was not found.") from exc

        logger.debug("Retrieved task_id=%s", task_id)
        return task
```

### `src/tracker/demo.py`

```python
import logging

from .config import LOG_DIR, LOG_FILE
from .exceptions import NotFoundError, ValidationError
from .models import Task
from .services import TaskService


def configure_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting tracker logging demo")

    service = TaskService()

    try:
        service.add(Task(task_id=1, title="Write logging notes"))
        service.get(999)
    except NotFoundError as exc:
        logger.warning("Demo requested a missing task: %s", exc)
        print("That task was not found. Please check the task ID and try again.")

    try:
        service.add(Task(task_id=1, title="Duplicate logging notes"))
    except ValidationError:
        logger.exception("Demo could not add task because validation failed")
        print("That task could not be saved. Please check the task details.")

    print(f"Demo complete. Developer log written to {LOG_FILE}")


if __name__ == "__main__":
    main()
```

Run from the project root:

```powershell
python -m src.tracker.demo
```

Windows launcher option:

```powershell
py -m src.tracker.demo
```

Expected result:

- The terminal shows friendly messages.
- `logs/app.log` is created and populated.
- The log file contains timestamped records with module names.
- The validation error records developer exception details without printing a raw traceback to the user.
