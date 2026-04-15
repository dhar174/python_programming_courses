# Advanced Day 3, Hour 2: Logging and Error Reporting (Practical)

## Learning Objectives
- Use the built-in `logging` module for diagnostics instead of print statements.
- Configure safe, informative error logging without spamming end users.

## Instructor Script & Talk Points

**(10–20 min)**

Now that our project holds multiple modules in a `src/` directory, simply using `print()` for everything becomes chaotic. Where did the print come from? When did it happen? Is it an error, or just informational? To answer these, we use Python's built-in `logging` module.

**Logging Levels:**
We organize logs by severity.
- `DEBUG`: Exhaustive details for developers.
- `INFO`: Normal operational events (e.g., "Server started.").
- `WARNING`: Something unexpected happened, but the app can recover.
- `ERROR`: A serious issue. A function failed.
- `CRITICAL`: A fatal error. The program usually must crash.

**Formatting and File Logging:**
You don't want logs to just vanish when the terminal closes. We use `logging.basicConfig()` to pipe our logs directly into a file, appending logs over time. We can format these logs to include timestamps and module names natively.

**Do Not Print Stack Traces to End Users:**
End users shouldn't see massive block of Python error text when they use your app. They should see a friendly error message like "Sorry, we couldn't load your document." Meanwhile, your app should quietly write the ugly, detailed traceback to a log file where developers can find and fix it later.

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Open up the service layer from your capstone project.
2. At the top of the file, insert `import logging` and set up a basic logger: `logger = logging.getLogger(__name__)`.
3. In your main entry script, add the configuration:
   ```python
   logging.basicConfig(level=logging.INFO, filename='logs/app.log')
   ```
4. Find an area where a `ValidationError` or `NotFoundError` is raised. Replace any `print()` statements with `logger.error("Item not found", exc_info=True)` or `logger.warning("Invalid input received")`.
5. Run the app, trigger the error on purpose, and open up `logs/app.log` to demonstrate the resulting formatted log output.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Add Logging**

1. Ensure you have a `logs/` directory in your project root, or programmatically secure its creation.
2. Add `logging.basicConfig` to your main demo script, configured to write logs to `logs/app.log`.
3. Instantiate a logger in your service layer using `logger = logging.getLogger(__name__)`.
4. Add at least three log calls across your service layer. Think about adding an `INFO` log when a record is successfully created, and an `ERROR` (or `WARNING`) when an exception is raised.
5. Trigger one of your errors via your main script and open `logs/app.log` to confirm the log was cleanly recorded.

**Optional Extension:**
Add custom string formatting to your config so that your log lines automatically prepend the current localized timestamp and the name of the module that generated the log.

**Completion Criteria:**
- The `app.log` file is successfully created and populated.
- User-facing error messages remain friendly, while developer logs contain technical stack details.
# Day 3, Hour 2: Logging and Error Reporting (Practical)
**Python Programming Advanced - Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap and transition from package structure: 5 minutes
- Logging fundamentals and levels: 12 minutes
- Friendly errors vs developer diagnostics: 13 minutes
- Live demo (service-layer logging to `logs/app.log`): 10 minutes
- Hands-on lab (add logging to student projects): 15 minutes
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Explain why `logging` is better than scattering `print()` statements through production logic
2. Use logging levels such as DEBUG, INFO, WARNING, and ERROR intentionally
3. Configure file-based logging for a small Python project
4. Log useful diagnostic information from the service layer
5. Keep user-facing errors friendly while still recording detail for developers
6. Avoid noisy or misleading logs
7. Prepare your project for safer troubleshooting as it grows

---

## Section 1: Recap and Framing (5 minutes)

**(5 min)**

**Quick Check:** When should you log at `WARNING` versus `ERROR`?

*Expected answer:* `WARNING` is for when something unexpected happened but the application can safely proceed or recover (e.g., disk space is running somewhat low, or an API call took longer than expected). `ERROR` is when a specific operation actually failed and cannot finish its job.
### Why Logging Comes After Structure

**[Instructor speaks:]**

Last hour we cleaned up project structure. That matters because good logging also needs a place to live. If the project is one giant script, logging often becomes one more giant script problem.

Now that we have a package shape, we can add logging in a way that feels intentional instead of improvised.

### The Big Idea

**[Instructor speaks:]**

Here is the line I want students to remember:

**Logs are for developers. Error messages are for users.**

Those two audiences overlap, but they are not the same.

If a user types bad input, they should get a clean message.

If the service layer hits a failure, the developer may need more detail:

- what operation failed
- which record ID was involved
- what exception occurred
- when it happened

Logging lets us preserve that detail without turning the user experience into a stack trace parade.

---

## Section 2: Logging Fundamentals and Levels (12 minutes)

### Why `print()` Is Not Enough

**[Instructor speaks:]**

Students love `print()` because it is immediate and familiar. That is fine during early exploration. But as the project grows, `print()` starts to show its limits:

- no severity levels
- no timestamps by default
- hard to redirect cleanly
- hard to separate developer output from user messaging
- easy to leave behind in messy ways

The `logging` module gives us structure.

### Log Levels in Practical Terms

**[Instructor speaks:]**

Use these levels in a practical, common-sense way:

- `DEBUG`: very detailed information for development
- `INFO`: normal important events, like a save or startup
- `WARNING`: something unexpected happened, but the program can continue
- `ERROR`: a meaningful failure occurred

Do not treat levels like trivia. Treat them like audience signals.

Examples:

- "created task 7" -> `INFO`
- "requested task 999 was missing" -> maybe `WARNING`
- "failed to save file due to permission error" -> `ERROR`

### Logging What Actually Helps

**[Instructor speaks:]**

Useful logs answer questions a future developer would ask:

- What was the application trying to do?
- Which record or file was involved?
- Did the operation succeed or fail?
- Can I correlate this event with another one?

Useless logs are vague, repetitive, or noisy:

- "here"
- "running"
- "got here again"
- ten thousand lines from a tight loop that bury the real issue

The goal is signal, not volume.

---

## Section 3: Friendly Errors vs Developer Diagnostics (13 minutes)

### Different Messages for Different Audiences

**[Instructor speaks:]**

Imagine this code path:

- a user requests a missing task
- the service raises `NotFoundError`
- the UI catches it

What should the user see?

Probably something like:

```text
Task 999 was not found.
```

What might the log record?

```text
2026-01-14 10:03:22,442 WARNING tracker.services Attempted lookup for missing task_id=999
```

Those messages serve different purposes, and that is exactly right.

### Logging Exceptions Without Spamming Users

**[Instructor speaks:]**

One anti-pattern I want students to avoid is printing raw exceptions straight to the user because they think "more detail is always better."

No. More detail is better for the developer, not necessarily for the person using the app.

The pattern we want is:

1. log the detailed event
2. surface a clean message to the user

That discipline becomes even more important once applications have GUIs, APIs, or shared users.

### File Logging

**[Instructor speaks:]**

For this hour, we are going to write logs to `logs/app.log`. That gives students something concrete they can inspect after running the program.

This also reinforces project structure:

- `src/` for application code
- `logs/` for diagnostic output
- user-facing behavior stays separate

---

## Section 4: Live Demo - Add Logging to the Service Layer (10 minutes)

### Demo Setup

**[Instructor speaks:]**

In this demo, I am adding logging to a package-based tracker project. Focus on three things:

1. where logging is configured
2. what gets logged
3. what does **not** get shown to the user

`src/tracker/config.py`

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"
```

`src/tracker/services.py`

```python
import logging

from tracker.exceptions import NotFoundError
from tracker.models import Task

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []
        logger.info("TaskService initialized with empty task list")

    def add_task(self, task: Task) -> None:
        self._tasks.append(task)
        logger.info("Added task_id=%s title=%r", task.task_id, task.title)

    def get_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.task_id == task_id:
                logger.debug("Retrieved task_id=%s", task_id)
                return task
        logger.warning("Attempted lookup for missing task_id=%s", task_id)
        raise NotFoundError(f"task {task_id} not found")
```

`demo.py`

```python
import logging

from tracker import Task, TaskService
from tracker.config import LOG_DIR, LOG_FILE
from tracker.exceptions import NotFoundError

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

service = TaskService()
service.add_task(Task(1, "Write outline", "high"))

try:
    service.get_task(999)
except NotFoundError:
    print("Task 999 was not found.")
```

### Demo Narration

**[Instructor speaks:]**

The log file receives the operational detail. The user sees a clean message.

This is a small example, but it teaches a professional habit:

- record the event for debugging
- keep the UI or user output readable

Also notice that we are not logging everything under the sun. We log meaningful transitions and failures.

### Teaching Notes During the Demo

- Show the generated `logs/app.log` file after running the script.
- Explain why `__name__` is useful in logger naming.
- Point out that logging inside a tight loop can produce useless noise.
- Remind students that a missing directory should be created explicitly before file logging.

---

## Section 5: Hands-On Lab - Add Logging (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Your lab is to make your project easier to debug without making it louder or uglier.

That means the goal is not "insert logging everywhere." The goal is "insert helpful logging at the right points."

### Student Task

1. Create `logs/` if it does not exist.
2. Configure logging to write to `logs/app.log`.
3. Add at least three log calls in your service layer.
4. Trigger one meaningful error and confirm it appears in the log.
5. Keep the user-facing message clean.

### Good Candidate Events to Log

- service initialization
- record creation
- record update
- missing record lookup
- failed validation or save path

### Completion Criteria

Students are done when:

- `logs/app.log` exists
- logs contain useful, readable entries
- user-facing messages remain friendly
- the service layer logs meaningful events rather than random noise

### Circulation Notes

- If a student uses only `print()`, help them convert one or two places first.
- If a student logs every variable in every method, ask what question each log line is answering.
- If a student forgets to create `logs/`, point them toward `mkdir(parents=True, exist_ok=True)`.
- If a student logs an exception but still dumps the raw traceback to the user, help them separate those concerns.

### Common Pitfalls to Watch For

- logging inside tight loops and flooding the file
- forgetting to create the logs directory
- using `ERROR` for every normal event
- writing vague log messages with no identifiers or context

### Optional Extensions

- Add timestamp and module name formatting if not already present
- Add a debug-level log for one internal branch
- Add logging around future save/load helpers if the student is thinking ahead

---

## Section 6: Logging Review Scenarios (Optional Extension Window)

### Fast Scenarios for Instructor Callouts

**[Instructor speaks:]**

If time remains, use quick scenarios to reinforce judgment:

- A user asks for task 999 and it does not exist.  
  Likely level: `WARNING`

- The application starts successfully and creates the log file.  
  Likely level: `INFO`

- Saving data fails because the directory is not writable.  
  Likely level: `ERROR`

- You want to inspect the internal branch chosen by a strategy during development.  
  Likely level: `DEBUG`

These small scenarios help students treat log levels as communication tools rather than memorization trivia.

### Sample Misconceptions and How to Respond

- "If it is important to me, it should be `ERROR`."  
  Response: Severity should describe the event, not your feelings about it.

- "I should log the same message in three different layers just to be safe."  
  Response: Repetition creates noise. Log where the event is most meaningful.

- "Users should see the same detailed message that goes into the log."  
  Response: Users need clarity, not internal debugging context.

- "If I add logging, I can stop raising exceptions."  
  Response: Logging records the event. Exceptions still control program behavior.

### Strong Log Characteristics to Praise

- includes record IDs or filenames when relevant
- uses clear verbs such as added, updated, missing, failed
- avoids noise
- helps a future developer reconstruct what happened

---

## Section 7: Debrief and Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

I want one volunteer to show both sides of the pattern:

- the log entry for developers
- the clean message for users

That contrast is the whole lesson.

### Exit Ticket

Ask students:

**When should you log at WARNING vs ERROR?**

Expected ideas:

- `WARNING` when something unexpected happened but the program can continue
- `ERROR` when an operation meaningfully failed and needs attention

### Instructor Closing Line

**[Instructor speaks:]**

Excellent. Your project can now tell developers what happened without yelling at users. Next hour we will make your file operations safer with context managers and a write-temp-then-replace save pattern.
