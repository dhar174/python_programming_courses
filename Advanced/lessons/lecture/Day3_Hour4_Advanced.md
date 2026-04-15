# Advanced Day 3, Hour 4: Decorators (Timing / Authorization / Validation)

## Learning Objectives
- Write and implement a Python decorator pattern to decouple shared functionality.
- Recognize when decorators reduce boilerplate and duplicated logic.

## Instructor Script & Talk Points

**(10–20 min)**

We've explored several patterns like Factories and Strategies. Today, we'll talk about *Decorators*. Decorators are a design pattern that allows us to modify or extend the behavior of a function or class without permanently modifying its source code. In Python, we invoke them with the `@` symbol right above a function declaration.

**Decorator Anatomy:**
A typical decorator is essentially a higher-order function: a function that takes *another* function as its argument and returns a new function (the "wrapper"). 
Inside a decorator, you define a `wrapper(*args, **kwargs)` function. This wrapper can execute code before and after calling the original function. The wrapper simply ends up passing through `args` and `kwargs` flexibly so you don't even have to rewrite the argument names.

**Keeping it Readable:**
Decorators should augment generic behavior. A common use is measuring benchmarking (timing how long a function runs), ensuring a user is logged in, or logging arguments. By doing this in a decorator, you don't muddy your service layer code with repetitive `start = time.time()` code in every single method. Keep decorators thin and readable!

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Create a slow function by importing the `time` module and calling `time.sleep(2)`.
2. Write a `@timed` decorator manually.
   ```python
   def timed(func):
       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           print(f"[{func.__name__}] took {time.time() - start:.3f}s")
           return result
       return wrapper
   ```
3. Stack the `@timed` above your slow function, and show how Python transparently runs the wrapper to calculate the duration.
4. Show a pseudo-code toy example of `@requires_api_key` to restrict access to a command layer.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Decorator Practice**

1. Inside your Capstone project, build your own `@timed` decorator.
2. Inside your `wrapper(*args, **kwargs)`, use your new `logging` setup from previous hours to log the execution duration alongside the `func.__name__` at the `INFO` or `DEBUG` level safely.
3. Attach this `@timed` decorator to at least two of your core service layer methods (such as retrieving your entire dataset or searching).
4. Make sure your `wrapper` properly executes `func` and explicitly `return`s the result. Run the scripts to review your `app.log` and verify the timing output is present and calculated dynamically. 

**Optional Extension:**
You'll notice that logging `func.__name__` gives you `wrapper` instead of the real name. Import `from functools import wraps`. Decorate your wrapper function natively with `@wraps(func)` to preserve the actual underlying function name correctly.

**Completion Criteria:**
- The decorator functions gracefully without breaking any methods, leaving the signatures transparently intact.
- The logger specifically outputs `INFO` execution benchmarks.
# Day 3, Hour 4: Decorators (Timing / Authorization / Validation)
**Python Programming Advanced - Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap and transition from safe saves: 5 minutes
- Decorator anatomy and use cases: 12 minutes
- Common mistakes and readability rules: 13 minutes
- Live demo (`@timed` and toy `@requires_api_key`): 10 minutes
- Hands-on lab (decorator practice): 15 minutes
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Explain what a decorator does in plain language
2. Write a small wrapper using `*args` and `**kwargs`
3. Preserve original function behavior while adding cross-cutting logic
4. Implement a practical timing decorator
5. Understand a toy authorization or validation decorator example
6. Use `functools.wraps` appropriately
7. Recognize when decorators improve readability and when they make code harder to understand

---

## Section 1: Recap and Framing (5 minutes)

**(5 min)**

**Quick Check:** Inside the inner `wrapper` function, what specifically happens if your wrapper forgets to `return` the final result?

*Expected answer:* Any caller of the decorated function will unexpectedly receive `None`. The original function executes normally, but its original return value is thrown away because the wrapper swallowed it.
### Why Decorators Belong Here

**[Instructor speaks:]**

Over the last two sessions, we have been steadily removing duplication:

- factories reduced duplicated creation rules
- strategies reduced duplicated branching
- packaging reduced structural chaos
- logging and safe saves reduced improvised operational behavior

Decorators continue that theme. They let us add repeated behavior around a function call without rewriting the same wrapper logic everywhere.

### The Big Idea

**[Instructor speaks:]**

A decorator is a function that takes a function, wraps it, and returns a new function.

That sentence sounds abstract until you translate it into practical examples:

- measure how long a service call takes
- check an API key before running a function
- validate arguments before continuing

The decorator handles the repeated "around the edges" behavior. The original function stays focused on its main job.

---

## Section 2: Decorator Anatomy and Use Cases (12 minutes)

### The Wrapper Shape

**[Instructor speaks:]**

The essential decorator shape looks like this:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

There are three important parts students must not miss:

- accept the original function
- call it with `*args` and `**kwargs`
- return its result

That last point matters a lot. If the wrapper forgets to return the result, the decorated function may quietly break.

### Practical Use Cases

**[Instructor speaks:]**

For this course, the best decorator examples are practical and small:

- timing a service operation
- logging entry/exit
- toy authorization checks
- lightweight validation

I do **not** want students disappearing into decorator metaprogramming acrobatics. We are teaching a useful technique, not summoning advanced wizardry for its own sake.

### Readability Rule

**[Instructor speaks:]**

If the decorator makes the code harder to understand than the original duplication, it is not helping.

Use decorators when:

- the cross-cutting behavior repeats
- the wrapper stays small
- the core function becomes clearer as a result

Do not use decorators to hide major application logic.

---

## Section 3: Common Mistakes and How to Avoid Them (13 minutes)

### Mistake 1: Forgetting to Return the Result

**[Instructor speaks:]**

This is the classic bug:

```python
def timed(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper
```

If the original function returns something important, that value is now lost.

The fix is simple:

```python
result = func(*args, **kwargs)
return result
```

### Mistake 2: Breaking the Function Signature Mentally

**[Instructor speaks:]**

Students sometimes forget why `*args` and `**kwargs` are there. They are there so the wrapper can pass through whatever arguments the original function expects.

This is not just syntactic noise. It preserves generality.

### Mistake 3: Losing Metadata

**[Instructor speaks:]**

Without `functools.wraps`, the wrapped function can lose useful metadata such as its name and docstring.

That may not seem important in a tiny classroom demo, but it becomes more important for debugging, help output, and tooling.

So the professional version of the pattern usually includes:

```python
from functools import wraps
```

and

```python
@wraps(func)
```

### Mistake 4: Hiding Too Much Logic

**[Instructor speaks:]**

If your decorator becomes a black box full of major business rules, stop and reconsider. Decorators are best for repeated edge behavior, not for hiding the main story of the application.

Keep them small and readable.

---

## Section 4: Live Demo - `@timed` and a Toy `@requires_api_key` (10 minutes)

### Demo Setup

**[Instructor speaks:]**

We are going to start with the safest, most practical example: timing.

Then I will show a toy authorization-style decorator so you can see the same structure in a second context.

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


def requires_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = kwargs.get("api_key")
        if api_key != "demo-key":
            raise PermissionError("invalid API key")
        return func(*args, **kwargs)

    return wrapper


class TaskService:
    def __init__(self) -> None:
        self._tasks = []

    @timed
    def add_task(self, task) -> None:
        self._tasks.append(task)

    @timed
    def list_tasks(self):
        return list(self._tasks)


@requires_api_key
def fetch_remote_tasks(*, api_key):
    return ["task-a", "task-b"]


service = TaskService()
service.add_task("Write outline")
print(service.list_tasks())

try:
    print(fetch_remote_tasks(api_key="wrong-key"))
except PermissionError as exc:
    print(f"Handled cleanly: {exc}")

print(fetch_remote_tasks(api_key="demo-key"))
```

### Demo Narration

**[Instructor speaks:]**

Notice how the core functions stay focused:

- `add_task` adds a task
- `list_tasks` lists tasks
- `fetch_remote_tasks` does the fetch work

The repeated edge behavior lives in the decorator.

Also notice that both wrappers return the original function result. That keeps behavior intact.

The authorization decorator here is intentionally a toy example. Its purpose is to teach the pattern, not to claim we built real security in ten lines. Later sessions on HTTP clients and APIs will revisit these concerns more realistically.

### Teaching Notes During the Demo

- Ask what would break if `wrapper` did not return `result`.
- Show that `func.__name__` remains useful because of `@wraps`.
- Emphasize that timing is a realistic use case students can adopt immediately.
- Clarify that the API-key example is pedagogical, not production-grade auth.

---

## Section 5: Hands-On Lab - Decorator Practice (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Your lab is to build one small decorator that meaningfully reduces duplication in your project. If you want the most straightforward path, build `@timed`.

If you are feeling comfortable, you may add a second toy decorator for validation or authorization-style checks.

### Student Task

1. Implement `@timed`.
2. Apply it to at least two service functions.
3. Confirm the original function behavior still works.
4. Confirm timing output appears when those functions run.
5. If time remains, add `@wraps`.
6. Optional: create a second decorator for a small repeated check.

### Suggested Starter Shape

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

### Completion Criteria

Students are done when:

- the decorator works
- the wrapped functions still return the correct values
- timing output appears for at least two functions
- the wrapper uses `*args` and `**kwargs`
- the code remains readable

### Circulation Notes

- If a student forgets to return the result, help them fix that first.
- If a student decorates a function and it stops accepting arguments, inspect the wrapper signature.
- If a student tries to hide major business logic in the decorator, steer them back toward a small cross-cutting concern.
- If a learner gets stuck, reduce scope to one tiny function plus timing output.

### Common Pitfalls to Watch For

- forgetting to return the original function result from the wrapper
- accidentally breaking arguments or function behavior
- omitting `@wraps` once the basic version works
- choosing a decorator use case that is too ambitious for the hour

### Optional Extensions

- log timing output instead of printing it
- create a validation decorator for non-empty titles
- create a toy permission check for a future API function

---

## Section 6: Decorator Misconceptions and Teaching Notes (Optional Extension Window)

### Questions to Ask When a Decorator Confuses Students

**[Instructor speaks:]**

If a student feels lost, bring them back to three questions:

1. What is the original function supposed to do?
2. What extra behavior is happening before or after that function runs?
3. Does the wrapper still pass arguments through and return the original result?

Those three questions cut through most decorator confusion.

### Sample Misconceptions and How to Respond

- "Decorators are only for advanced libraries, not normal application code."  
  Response: Small decorators like timing or lightweight validation are perfectly normal when they reduce repetition.

- "If I decorate a function, the wrapper replaces the original function completely."  
  Response: It wraps the original behavior; it should usually still call the original function.

- "If the decorator prints something, returning the result no longer matters."  
  Response: Output and return value are separate concerns. Most decorated functions still need to return what callers expect.

- "A decorator is better than a helper function by default."  
  Response: Not always. Use it only when wrapping repeated cross-cutting behavior actually improves clarity.

### Transition Note Toward Session 4

**[Instructor speaks:]**

This is a good moment to point ahead. Timing, wrapping, permission-style checks, and reusable helper layers all show up again once code starts interacting with HTTP clients and APIs. Session 4 will make those needs feel much more concrete.

---

## Section 7: Debrief and Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

I want one student to explain, in plain language, what the wrapper is doing before and after the original function call. If they can explain that clearly, they understand decorators at a practical level.

### Exit Ticket

Ask students:

**What happens if your wrapper forgets to return the original function result?**

Expected ideas:

- the decorated function may start returning `None`
- calling code may break or behave incorrectly
- the decorator has changed behavior instead of just adding around-the-edges logic

### Instructor Closing Line

**[Instructor speaks:]**

Excellent work. You have now prepared the project structurally and operationally for the next phase of the course. In Session 4, we start working with HTTP clients and JSON contracts, where clean packages, good logs, safe persistence habits, and small reusable wrappers all start paying off immediately.
