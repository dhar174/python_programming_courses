# Day 3, Hour 4: Decorators for Timing, Toy Authorization, and Lightweight Validation

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 3, Hour 4 of 48, also Hour 12 in the Advanced runbook sequence
- **Focus**: Writing small decorators that wrap service functions without changing their behavior, especially a practical `@timed` decorator that logs execution duration.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 3, Hour 12.
- **Prerequisites**: Learners should have completed Day 3 Hours 1-3 or have equivalent project structure: package code under `src/tracker/`, logging configured from Day 3 Hour 2, and safe-save vocabulary from Day 3 Hour 3.
- **Advanced trajectory**: This hour stays on the PCAP-to-PCPP1 path. Learners are using decorators as a professional readability tool, not studying metaprogramming internals.
- **Instructor goal**: By the end of this hour, every learner can write and apply a simple decorator, explain `wrapper(*args, **kwargs)`, preserve the original return value, and verify timing messages in `logs/app.log`.

Important instructor positioning:

- Keep the decorator examples practical and small. The runbook scope is decorators for timing, toy authorization, and lightweight validation.
- The canonical `@timed` decorator in this hour uses `time.perf_counter()`, `logging.getLogger(__name__).info(...)`, returns the original function result, and uses `@wraps(func)` in the professional version.
- Tie the logging output directly back to Day 3 Hour 2. The point is not "print a benchmark to the terminal." The point is "record useful operational information in the same logging system, such as `logs/app.log`."
- Keep the Day 3 Hour 3 bridge visible: safe saves protect files; decorators help avoid repeated wrapper code around service behavior. Both are about making the project more reliable without cluttering the main business logic.
- Use the phrase **toy authorization** for `@requires_api_key`. It teaches the wrapper shape; it is not production security.
- Use keyword-only `api_key` in the toy authorization example. This avoids positional ambiguity and gives you a clean teaching point before Session 4 HTTP/API work.
- Mention validation as a lightweight example, but do not overbuild a validation framework.
- Protect the lab time. Learners need enough minutes to implement, apply, run, and inspect log output.

Explicitly out of scope today:

- decorator factories with arguments, such as `@timed(level=logging.DEBUG)`
- class decorators
- descriptors
- metaclasses
- async decorators
- framework authentication systems
- production security design
- replacing tests, logging, validation, or API security with one clever decorator

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from safe saves to reusable wrappers | 5 min | Connect Hour 3 safe persistence habits to reducing duplicated operational code |
| Outcomes, setup, and scope boundaries | 5 min | Name what learners will build and what is intentionally out of scope |
| Concept briefing: decorator anatomy and readability | 8 min | Explain functions wrapping functions, `wrapper(*args, **kwargs)`, return values, and small readable decorators |
| Live demo: professional `@timed` for service methods | 8 min | Build a logging-based timing decorator with `perf_counter`, `@wraps`, method support, and preserved return values |
| Live demo: toy `@requires_api_key` and validation discussion | 5 min | Show a second decorator shape with keyword-only `api_key`; position validation as lightweight and limited |
| Guided lab: timing decorator in the tracker project | 26 min | Learners implement `@timed`, apply it to two service functions, and verify timing logs in `logs/app.log` |
| Pitfalls, quick check, and Session 4 bridge | 3 min | Confirm return-value behavior, signature pass-through, and the connection to HTTP/API work |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 8 + 8 + 5 + 26 + 3 = 60. The guided lab is 26 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect that lab time. If discussion runs long, shorten the second demo and validation discussion rather than shrinking student practice. The required outcome is practical: the timing decorator works, does not change behavior, and writes timing output through the logging system.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain in plain language that a decorator takes a function, wraps it, and returns a new callable.
2. Write a simple decorator using an inner `wrapper(*args, **kwargs)` function.
3. Explain why `*args` and `**kwargs` help a wrapper work with ordinary functions and methods.
4. Preserve the original return value from a decorated function.
5. Apply a `@timed` decorator to at least two service functions.
6. Use `time.perf_counter()` for elapsed-time measurement.
7. Log timing output with `logging.getLogger(__name__).info(...)` so messages can appear in `logs/app.log`.
8. Use `functools.wraps` in the professional version to preserve metadata such as the function name.
9. Recognize how decorators reduce duplicated timing, authorization-style, or validation-style logic.
10. Explain why decorators should stay small and readable.
11. Identify common pitfalls: forgetting to return the result, breaking signatures, hiding too much logic, and using toy authorization as if it were production security.
12. Describe how these wrapper patterns prepare the project for Session 4 HTTP clients and API boundaries.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 3, Hour 12 visible. The required scope is decorators for timing, authorization, and validation.
- Open your Day 3 Hour 2 logging notes. You will reuse the idea that application behavior should be recorded through the logger, not scattered `print()` calls.
- Open your Day 3 Hour 3 safe-save notes. The bridge sentence is: "Safe saves kept file-writing details out of the main story; decorators keep repeated wrapper behavior out of the main story."
- Confirm learners know where their log file is. In this course, use `logs/app.log` when following the Day 3 Hour 2 logging setup.
- Prepare this board note:

```text
Decorator mental model:
original function -> wrapper adds behavior -> original result still comes back
```

- Prepare a second board note:

```text
Decorator checklist:
1. Accept func.
2. Define wrapper(*args, **kwargs).
3. Do small before/after behavior.
4. Call func(*args, **kwargs).
5. Return the result.
6. Return wrapper.
```

- Be ready to demonstrate the canonical professional `@timed` decorator:

```python
import logging
import time
from functools import wraps
from typing import Any, Callable


def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.getLogger(__name__).info(
            "%s completed in %.6f seconds",
            func.__name__,
            elapsed,
        )
        return result

    return wrapper
```

- If you demo in a real learner project, avoid timing functions that depend on network access. Keep the demonstration deterministic and Windows-friendly.
- If logging is not already configured in a learner's project, have them quickly configure it using their Day 3 Hour 2 pattern. Do not spend the hour redesigning logging.

---

## Opening Bridge from Safe Saves to Reusable Wrappers (5 minutes)

### Instructor talk track

"Welcome back. In the previous hour, we focused on safer file operations. We used `with`, wrote JSON to a temporary file, and replaced the real file only after the new content had been written successfully."

"That pattern had a bigger theme behind it: we want the main service code to stay focused on the main job. If the service is saving tasks, the service should not be cluttered with five different improvised versions of 'open this file, write this JSON, clean up after failure.' We moved that responsibility into a helper."

"Decorators continue the same theme. They help us move repeated around-the-edges behavior into one reusable place."

Display:

```text
Hour 2 logging: record what happened.
Hour 3 safe saves: avoid damaging data during writes.
Hour 4 decorators: avoid repeating wrapper logic around functions.
```

"Here is a common problem. Imagine we want to time several service operations: add a task, list tasks, search tasks, maybe save tasks. We could copy this pattern into every method."

```python
start = time.perf_counter()
result = do_the_real_work()
elapsed = time.perf_counter() - start
logging.getLogger(__name__).info("operation completed in %.6f seconds", elapsed)
return result
```

"That works once. But after the third or fourth copy, we have duplication. If we want to change the message format, we have to edit every copy. If one method forgets to return the original result, we introduce a bug. If one method uses `print()` instead of logging, our observability becomes inconsistent."

"A decorator lets us write that wrapping behavior once, then apply it with the `@` syntax."

Display:

```python
@timed
def list_tasks():
    ...
```

"The goal today is not to become decorator magicians. The goal is much more practical: use a small decorator to reduce duplicated logic while keeping behavior intact."

Pause and ask:

"If a function returns a list of tasks before decoration, what should it return after we add `@timed`?"

Expected answer:

"The same list of tasks. The decorator may add logging, but it should not change the function's meaning."

### Transition

"Let's name the outcomes and boundaries so we stay focused and do not wander into metaprogramming topics we do not need today."

---

## Outcomes, Setup, and Scope Boundaries (5 minutes)

### Instructor talk track

"By the end of this hour, you should be able to write and apply a decorator like this."

```python
@timed
def search_tasks(query: str) -> list[str]:
    ...
```

"When `search_tasks()` runs, the real search still happens. The return value still comes back. The extra behavior is that timing information is logged."

"We will use three examples today."

Display:

```text
Required practical example:
    @timed
    Logs execution time for service functions.

Second toy example:
    @requires_api_key
    Demonstrates authorization-shaped wrapping.

Lightweight discussion example:
    validation
    Shows where a small repeated check might fit.
```

"Timing is the one you must implement in the lab. The API-key decorator is a toy pattern. It is deliberately not production security. Real authentication and authorization involve protocols, storage, secrets, framework integration, threat modeling, transport security, rotation, auditing, and more. We are not doing that in five minutes. We are using a tiny example to practice the decorator shape."

"Validation is also lightweight today. A decorator can sometimes check inputs before calling a function, but validation can easily become business logic. If the validation is central to the behavior, it may belong inside the function, the model, or the service. We will mention it, not build a validation framework."

"Here is what we are explicitly not doing today: decorator factories with arguments, class decorators, descriptors, metaclasses, async decorators, framework auth, or production security. Those are real topics, but they are not needed for the runbook outcome."

"Our project convention remains the same as the previous hours. Source code lives under `src/tracker/`. Logging can write to `logs/app.log`. Run demos from the project root so relative paths behave predictably on Windows, macOS, and Linux."

### Quick setup check

Ask:

"Where should timing messages go if we are following the Day 3 Hour 2 logging setup?"

Expected answer:

"Through logging, into the configured logs such as `logs/app.log`, not just printed to the terminal."

### Transition

"Now let's build the mental model. Decorators can feel mysterious because the syntax is compact. We will slow it down and show the plain function shape first."

---

## Concept Briefing: Decorator Anatomy and Readability (8 minutes)

### Part 1: A decorator is a function that returns a function

**Instructor talk track**

"The shortest useful definition is this: a decorator is a function that takes a function, wraps it, and returns a replacement callable."

Display:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
```

"This example does not add behavior yet. It only shows the shape."

"The outer function, `my_decorator`, receives the original function. The inner function, `wrapper`, is what will run when someone calls the decorated function. Inside the wrapper, we usually call the original function. Then we return the original function's result."

"The `@` syntax is a friendly way to apply that wrapping."

```python
@my_decorator
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

"This is roughly equivalent to writing this after the function definition."

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


greet = my_decorator(greet)
```

"The name `greet` now refers to the wrapped version. That is why the wrapper must be careful. If the wrapper does not call the original function, the original work does not happen. If the wrapper does not return the original result, callers may receive `None` even though the original function produced a value."

### Part 2: Why `wrapper(*args, **kwargs)` matters

**Instructor talk track**

"The wrapper often uses `*args` and `**kwargs`. This is not decoration magic. It is ordinary Python argument forwarding."

Display:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```

"`*args` collects positional arguments. `**kwargs` collects keyword arguments. Passing them into `func(*args, **kwargs)` forwards the call to the original function."

"This matters for methods. When we decorate an instance method, Python still passes `self` as the first positional argument. The wrapper does not need to know that the first positional argument is named `self`. It simply forwards all positional and keyword arguments to the original function."

Display:

```python
class TaskService:
    @timed
    def list_titles(self) -> list[str]:
        return ["Write tests", "Review logs"]
```

"When `service.list_titles()` runs, `self` is still passed through. The wrapper receives it in `args`, forwards it to the original method, and returns the list. That is how a method decorator preserves normal method behavior."

### Part 3: Keep decorators small and readable

**Instructor talk track**

"Decorators are powerful, so our readability rule matters."

Display:

```text
Use a decorator when:
- the extra behavior repeats
- the wrapper stays small
- the original function becomes easier to read

Avoid a decorator when:
- it hides the main business rule
- it creates surprising side effects
- it makes debugging harder than the duplication did
```

"For this hour, timing is a good decorator because it is cross-cutting. Timing can apply to many functions without becoming the main purpose of those functions."

"Authorization-style checks can also be cross-cutting, but today's API-key example is intentionally small and artificial. In real applications, authorization deserves serious design."

"Validation is mixed. A tiny repeated check may be fine. But if validation rules are the core business logic, hiding them in a decorator can make the code harder to understand."

### Transition

"Now we will live-code the practical version: `@timed` that logs through the Day 3 logging setup and preserves method behavior."

---

## Live Demo: Professional `@timed` for Service Methods (8 minutes)

### Demo framing

**Instructor talk track**

"We are going to build the professional version first. That means we will not use `print()` for timing. We will use `logging.getLogger(__name__).info(...)` so the timing message flows through the same logging setup we introduced in Day 3 Hour 2."

"We will also use `time.perf_counter()`. This is the right tool for measuring elapsed time because it gives us a high-resolution performance counter suitable for durations."

"Finally, we will use `@wraps(func)` from `functools`. `wraps` preserves useful metadata from the original function, such as the name and docstring. Without it, tools may think every decorated function is named `wrapper`."

### Live-code the decorator

Type or display:

```python
import logging
import time
from functools import wraps
from pathlib import Path
from typing import Any, Callable


def configure_logging() -> None:
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename=Path("logs") / "app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.getLogger(__name__).info(
            "%s completed in %.6f seconds",
            func.__name__,
            elapsed,
        )
        return result

    return wrapper
```

### Narrate each important line

**Instructor talk track**

"The `configure_logging()` helper is here only to make the standalone demo runnable. If your project already configures logging from Hour 2, use your existing setup instead of copying this exact helper everywhere."

"`logging.getLogger(__name__).info(...)` sends the timing message through the named logger for this module. This is the same logging family we used in the logging lesson, and it lets log records include the module name."

"`def timed(func: Callable[..., Any]) -> Callable[..., Any]` says this decorator accepts a callable and returns a callable. The type hints are intentionally broad because the decorator can wrap many different function signatures."

"`@wraps(func)` goes above the wrapper. This is the professional version. It helps keep the wrapped function's identity visible to logs, debuggers, documentation tools, and tests."

"`start = time.perf_counter()` captures the start time. After the original function runs, we call `time.perf_counter()` again and subtract."

"The most important behavior line is `result = func(*args, **kwargs)`. That is where the original function actually runs."

"The most important preservation line is `return result`. Without that line, the wrapper changes the behavior."

### Add a deterministic service-method example

Type or display:

```python
class TaskService:
    def __init__(self) -> None:
        self._titles: list[str] = []

    @timed
    def add_task(self, title: str) -> int:
        self._titles.append(title)
        return len(self._titles)

    @timed
    def list_titles(self) -> list[str]:
        return list(self._titles)


def main() -> None:
    configure_logging()

    service = TaskService()
    first_id = service.add_task("Review safe saves")
    second_id = service.add_task("Add timing decorator")
    titles = service.list_titles()

    print(first_id)
    print(second_id)
    print(titles)


if __name__ == "__main__":
    main()
```

Expected terminal output:

```text
1
2
['Review safe saves', 'Add timing decorator']
```

Expected log shape in `logs/app.log`:

```text
INFO __main__ add_task completed in 0.000123 seconds
INFO __main__ add_task completed in 0.000045 seconds
INFO __main__ list_titles completed in 0.000030 seconds
```

The exact duration will differ by machine. That is expected. The deterministic part is that the return values still match the original method behavior.

On Windows, learners can inspect recent log lines with:

```powershell
Get-Content logs/app.log -Tail 20
```

### Method behavior callout

**Instructor talk track**

"Notice that `add_task` and `list_titles` are instance methods. They depend on `self`. We did not write special code for `self` in the decorator. The wrapper receives `self` as part of `args` and forwards it to the original method."

"Also notice the return values. `add_task` still returns the new task count. `list_titles` still returns a list. The decorator adds timing logs, but it does not change the meaning of the method."

### Transition

"Now that the main timing decorator is clear, let's look at a second small example: a toy API-key check. This helps you see that the same wrapper shape can appear around authorization-style behavior, while still making clear that real security is out of scope today."

---

## Live Demo: Toy `@requires_api_key` and Validation Discussion (5 minutes)

### Toy authorization demo

**Instructor talk track**

"This next example is intentionally a toy. It is not production authentication or authorization. It does not store secrets safely. It does not rotate keys. It does not integrate with a framework. It is only here to show another decorator shape."

"The important design choice is that the decorated function accepts `api_key` as a keyword-only argument. The `*` in the function signature means callers must write `api_key='demo-key'`. That avoids positional ambiguity."

Type or display:

```python
from functools import wraps
from typing import Any, Callable


def requires_api_key(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        api_key = kwargs.get("api_key")
        if api_key != "demo-key":
            raise PermissionError("invalid API key")
        return func(*args, **kwargs)

    return wrapper


@requires_api_key
def fetch_remote_task_titles(*, api_key: str) -> list[str]:
    return ["Plan API client", "Document JSON contract"]
```

Then show the calls:

```python
try:
    fetch_remote_task_titles(api_key="wrong-key")
except PermissionError as error:
    print(f"Access denied in toy demo: {error}")

print(fetch_remote_task_titles(api_key="demo-key"))
```

Expected output:

```text
Access denied in toy demo: invalid API key
['Plan API client', 'Document JSON contract']
```

**Instructor talk track**

"The wrapper looks inside `kwargs` for `api_key`. Because the function requires keyword-only `api_key`, we do not have to guess whether the first positional argument might be the key, the query, the user id, or something else."

"Again: this is a teaching example. In Session 4, when we start HTTP and API work, we will talk more concretely about request errors, JSON contracts, and boundaries. Do not treat this toy decorator as a security system."

### Lightweight validation mention

**Instructor talk track**

"Validation can use the same idea, but we need restraint. A tiny repeated check might be reasonable."

Display:

```python
def ensure_non_empty_title(title: str) -> None:
    if not title.strip():
        raise ValueError("title must not be empty")
```

"A decorator could wrap several functions with a small repeated validation rule, but we are not building that today. If validation is the main business rule, make it visible in the service or model. Do not hide important decisions in clever wrappers."

### Transition

"Now you will implement the required piece: `@timed` that logs execution time and applies to two service functions."

---

## Guided Lab: Timing Decorator in the Tracker Project (26 minutes)

### Lab purpose

**Instructor talk track**

"Your lab is to build one useful decorator: `@timed`. It should log execution time, preserve the original return value, and work on at least two service functions."

"This lab connects directly to Day 3 Hour 2. If your logging setup writes to `logs/app.log`, your timing messages should appear there. If your logging setup is slightly different, use your project's existing logger configuration, but keep the decorator's logging call in the professional style."

"This lab also connects back to Hour 3. Safe saves helped us avoid repeating risky file-write steps. Decorators help us avoid repeating timing code around multiple service methods."

### Student prompt

Implement `@timed` in a suitable existing module in your tracker project. Apply it to at least two service functions or methods, such as:

- `add_task(...)`
- `list_tasks(...)`
- `search_tasks(...)`
- `save_tasks(...)`
- `load_tasks(...)`

Your decorator must:

1. Accept the original function.
2. Define `wrapper(*args, **kwargs)`.
3. Use `time.perf_counter()` before and after the original call.
4. Call the original function with `func(*args, **kwargs)`.
5. Store and return the original result.
6. Log the elapsed time with `logging.getLogger(__name__).info(...)`.
7. Use `@wraps(func)` in the professional version.

### Lab timing checklist

| Lab step | Suggested time | Done when |
| --- | ---: | --- |
| Locate two service functions | 4 min | Learner chooses two functions or methods that already work |
| Implement `@timed` | 7 min | Decorator uses `perf_counter`, `logging.getLogger(__name__).info`, `@wraps`, and returns `result` |
| Apply the decorator | 4 min | Two service functions have `@timed` above their definitions |
| Run behavior checks | 5 min | Decorated functions still return the same values as before |
| Verify log output | 4 min | `logs/app.log` or configured log destination shows timing messages |
| Reflect and clean up | 2 min | Learner can explain `wrapper(*args, **kwargs)` and remove noisy experiments |

Total lab time: 4 + 7 + 4 + 5 + 4 + 2 = 26 minutes.

### Starter code

Offer this if learners need scaffolding:

```python
import logging
import time
from functools import wraps
from typing import Any, Callable


def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.getLogger(__name__).info(
            "%s completed in %.6f seconds",
            func.__name__,
            elapsed,
        )
        return result

    return wrapper
```

### Example application to service methods

If learners need a concrete model, show:

```python
class TaskService:
    def __init__(self) -> None:
        self._titles: list[str] = []

    @timed
    def add_task(self, title: str) -> int:
        self._titles.append(title)
        return len(self._titles)

    @timed
    def search_tasks(self, query: str) -> list[str]:
        normalized_query = query.casefold()
        return [
            title
            for title in self._titles
            if normalized_query in title.casefold()
        ]
```

Then show a deterministic behavior check:

```python
service = TaskService()
assert service.add_task("Write timing decorator") == 1
assert service.add_task("Review timing logs") == 2
assert service.search_tasks("timing") == [
    "Write timing decorator",
    "Review timing logs",
]
```

"These assertions focus on behavior. If they passed before decoration, they should still pass after decoration. The decorator adds logging; it should not change what the service returns."

### Log verification

Ask learners to run their normal demo or tests from the project root. On Windows, a common command shape is:

```powershell
py -m src.tracker.demo
Get-Content logs/app.log -Tail 20
```

If their project uses `python` instead of `py`, use:

```powershell
python -m src.tracker.demo
Get-Content logs/app.log -Tail 20
```

Expected log shape:

```text
INFO src.tracker.services add_task completed in 0.000080 seconds
INFO src.tracker.services search_tasks completed in 0.000050 seconds
```

The exact module name and duration may differ. The required evidence is that two decorated functions produce timing log records and still behave correctly.

### Completion criteria

Students are done when:

- `@timed` is implemented with `wrapper(*args, **kwargs)`.
- `@timed` uses `time.perf_counter()`.
- `@timed` logs with `logging.getLogger(__name__).info(...)`.
- The wrapper calls the original function.
- The wrapper returns the original result.
- At least two service functions or methods are decorated.
- The decorated functions still produce the same return values or side effects as before.
- Timing messages appear in `logs/app.log` or the project's configured log destination.
- The code remains small and readable.

### Instructor circulation notes

- If a learner says, "My function now returns `None`," inspect the wrapper for a missing `return result`.
- If a learner says, "My method says it is missing `self` or an argument," inspect whether the wrapper accepts and forwards `*args` and `**kwargs`.
- If a learner logs with `print()`, acknowledge that it can help while debugging, then redirect them to the logging requirement so the output lands in `logs/app.log`.
- If a learner uses `time.time()`, explain that it often works for timestamps, but `time.perf_counter()` is preferred for measuring elapsed durations.
- If a learner wants to decorate every function in the project, slow them down. The requirement is two service functions. Quality and explanation matter more than coverage.
- If a learner starts building decorator factories, class decorators, or authorization frameworks, remind them those topics are explicitly out of scope today.
- If logging does not appear, check whether logging was configured before the decorated functions were called. Then check the current working directory and the expected location of `logs/app.log`.

### Stretch options only after completion

Offer these only if the required lab is complete:

- Compare `service.add_task.__name__` with and without `@wraps(func)`.
- Add timing to a safe-save helper and confirm that both success and failure paths are still visible through logs.
- Add one tiny validation helper or decorator for a clearly repeated check, such as a non-empty title, but keep it small and readable.

Do not let stretch work consume the required lab or turn into production security design.

---

## Pitfalls, Quick Check, and Session 4 Bridge (3 minutes)

### Common pitfalls recap

**Instructor talk track**

"Let's close by naming the mistakes that matter most."

Display:

```text
Decorator pitfalls:
1. Forgetting to return the original result.
2. Forgetting to forward *args and **kwargs.
3. Timing with print instead of the logging system.
4. Losing metadata by omitting functools.wraps.
5. Hiding major business logic in a decorator.
6. Treating a toy API-key example as production security.
```

"The first two are behavior bugs. If you forget to return the result, callers may receive `None`. If you break argument forwarding, methods and functions may stop accepting the arguments they accepted before."

"The logging issue is a project consistency issue. Day 3 Hour 2 gave us a logging system. Use it."

"The metadata issue is why we use `@wraps(func)` in the professional version."

"The last two are design issues. Decorators should reduce duplication and improve readability. They should not hide the main story of the program."

### Quick check / exit ticket

Ask:

"What happens if your wrapper calls the original function but forgets to return the result?"

Expected answer:

"The original function may still run, but the decorated function returns `None` unless the wrapper returns the original result. That changes behavior and can break calling code."

Ask one follow-up:

"Why do we use `wrapper(*args, **kwargs)` instead of naming one fixed parameter list?"

Expected answer:

"It lets the decorator forward whatever arguments the original function or method expects, including `self` for methods and keyword arguments."

### Wrap-up and bridge to Session 4

**Instructor closing line**

"Today you added a small professional tool to the project: a decorator that can wrap service behavior without changing what the service means. That prepares us for Session 4, where HTTP clients and JSON API contracts introduce more repeated edge behavior: timing calls, logging failures, handling request errors, and keeping core functions readable. The same discipline applies there: keep wrappers small, keep behavior explicit, and use logs to make the program observable."
