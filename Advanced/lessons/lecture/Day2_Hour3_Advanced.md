# Day 2, Hour 3: Pythonic Class Ergonomics (`repr`/`str`/equality) + Light Type Hints

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 2, Hour 3 of 48, also Hour 7 in the Advanced runbook sequence
- **Focus**: Making model objects easier to debug, log, display, and prepare for serialization by using `__repr__`, `__str__`, light type hints, and a required checkpoint-prep `to_dict()` helper.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 2, Hour 7.
- **Prerequisites**: Learners should be comfortable defining classes, writing `__init__`, creating objects, reading simple tracebacks, using lists and dictionaries, and understanding the Day 2 Hour 1 Factory and Day 2 Hour 2 Strategy ideas.
- **Advanced trajectory**: This hour stays in the PCAP-to-PCPP1 path. Learners already know how to make classes. The advanced step is making classes pleasant and reliable to use in a larger application, especially when objects appear in logs, lists, debug output, UI text, and checkpoint review.
- **Instructor goal**: By the end of this hour, every learner has upgraded a model so objects print cleanly, debug output is useful, simple type hints document expected inputs and outputs, and a `to_dict()` or similar serialization helper is ready for the Day 2 Hour 4 checkpoint.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Day 2 Hour 2 Strategy | 5 min | Connect chosen behavior to readable and debuggable objects |
| Outcomes, setup, and vocabulary | 5 min | Define class ergonomics, `__repr__`, `__str__`, light type hints, and serialization readiness |
| Concept briefing: readable objects and light hints | 10 min | Explain developer-facing versus user-facing string output and why hints help humans and tools |
| Live demo: upgrade a model for debugging and display | 10 min | Add `__repr__`, `__str__`, type hints, and checkpoint-prep `to_dict()` to a small model |
| Guided lab: make your model pleasant to work with | 25 min | Learners upgrade their main model and prepare for the checkpoint |
| Quick checks, pitfalls, completion criteria, and wrap-up | 5 min | Verify when to use `repr` versus `str`, name pitfalls, and bridge to Checkpoint 1 |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If discussion runs long, shorten the concept examples rather than removing hands-on practice. The required outcome is practical: objects should print cleanly, type hints should be correct and should not change runtime behavior, and learners should leave ready for the Day 2 Hour 4 domain and service layer checkpoint.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain why the default custom-object display, such as `<__main__.Task object at 0x...>`, is not enough for a growing application.
2. Implement `__repr__(self) -> str` so developers can inspect objects in logs, tracebacks, debugger views, containers, and the Python REPL.
3. Implement `__str__(self) -> str` so users see a friendly display string in a CLI, UI label, report, or simple `print()` call.
4. Distinguish the purpose of `repr(obj)` from `str(obj)` without treating either one as decoration.
5. Add light type hints to a model constructor and at least three methods or functions using simple built-in annotations such as `str`, `int`, `bool`, `list[str]`, and `dict[str, object]`.
6. Explain that type hints help humans and tools, but do not automatically enforce types at runtime.
7. Avoid overcomplicated typing imports when simple annotations communicate enough for the current design.
8. Recognize the common bug where `__str__`, `__repr__`, or another value-returning method accidentally returns `None`.
9. Add or refine a `to_dict()` method as a checkpoint-prep serialization step for Day 2 Hour 4.
10. Keep equality comparison as a light sidebar or extension, including the caution that custom equality can affect hashability and set or dictionary-key behavior.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 2, Hour 7 visible. The required scope is Pythonic class ergonomics, `__repr__`, `__str__`, light type hints, a lab that improves the main model, completion criteria that objects print cleanly and hints do not break runtime, pitfalls around overcomplicated typing and unexpected `None`, and the quick check about `repr` versus `str`.
- Also keep the runbook section for Session 2, Hour 8 visible. Hour 8 requires a stable domain and service layer and specifically requires serialization helpers, with `to_dict` at minimum. This hour should prepare learners for that checkpoint rather than leaving serialization as a casual extra.
- Open the Day 2 Hour 2 Strategy lecture if you want the bridge nearby. Hour 2 taught that strategies choose behavior. Today teaches that the objects moving through those strategies must be readable when displayed and debuggable when something goes wrong.
- Prepare a clean file or notebook cell for the live demo. A suggested name is `day2_hour3_ergonomics_demo.py`. The demo code below is self-contained and deterministic.
- Confirm the terminal command for the room. Use `python day2_hour3_ergonomics_demo.py` if `python` works. If your environment uses `python3`, consistently show `python3 day2_hour3_ergonomics_demo.py`.
- Prepare this board note before class:

```text
Day 2 Hour 3 goals:
1. __repr__ = developer/debug string.
2. __str__ = user/display string.
3. Type hints = readable intent for humans and tools.
4. Keep hints simple.
5. to_dict() = checkpoint-prep serialization helper.
```

- Be ready to correct two common mistakes early. First, learners may write `print(...)` inside `__str__` or `__repr__` instead of returning a string. Second, learners may try to solve every possible type problem with advanced typing syntax. Keep the scope light: use simple built-in annotations and focus on readability.
- Decide how strict to be about `to_dict()` during lab. The recommended instruction is: "If you finish the main ergonomics work during lab, add `to_dict()` now. If you do not finish it during this hour, it becomes a must-finish item before the next checkpoint begins." This keeps the hour aligned with both Hour 7 and Hour 8.

---

## Opening Bridge from Day 2 Hour 2 Strategy (5 minutes)

**Instructor talk track**

"Welcome back. In the previous hour we worked with the Strategy Pattern. The important design idea was that strategies choose behavior. We had stable workflow code, and then we selected a sorting strategy, validation strategy, filtering strategy, or callable object to change how that workflow behaved."

"Today we stay in that same design neighborhood, but we focus on the objects that move through those workflows. A strategy can choose the right behavior, but when something goes wrong, the instructor, the developer, the tester, and the future maintainer still need to understand what object was involved."

"Here is the bridge sentence for this hour: **strategies choose behavior; class ergonomics make the chosen objects readable and debuggable.**"

Write or display:

```text
Strategy: Which behavior should we use?
Class ergonomics: Can we understand the objects while using that behavior?
```

"Imagine a tracker application. We have a `Task` object. Yesterday, we might have sorted tasks by title or priority using a strategy. That is useful. But now suppose the sorted output is wrong. You print the list of tasks and Python shows this:"

```text
[<__main__.Task object at 0x000001F2A8C4D910>, <__main__.Task object at 0x000001F2A8C4DA50>]
```

"That output technically identifies two objects, but it does not tell us the title, the status, the priority, or the identifier. It forces us to inspect each object manually. In a small script that is annoying. In a larger application it slows down debugging and makes logs nearly useless."

"Now imagine the same list prints like this:"

```text
[Task(task_id=101, title='Write tests', status='open', priority=2),
 Task(task_id=102, title='Review PR', status='blocked', priority=1)]
```

"That is a different experience. Suddenly we can see what data moved through the strategy. We can see whether the sort order makes sense. We can paste part of the output into a bug report. We can compare expected and actual results without opening the debugger."

Pause and ask:

"Where do you currently see objects in your tracker project? In `print()` calls? In lists? In logs? In error messages? In UI labels?"

Take two or three answers. Listen for CLI output, debugging lists, service-layer results, validation errors, and checkpoint demos. Then connect:

"Those are the places where Pythonic class ergonomics matter. We are not adding magic methods because they look fancy. We are adding them because they make real development work easier."

**Transition**

"Let's name the vocabulary, then we will upgrade a simple model live. We will keep the typing light. We are not doing advanced typing theory today. We are making code easier to read, easier to inspect, and ready for the checkpoint."

---

## Outcomes, Setup, and Vocabulary (5 minutes)

Use this section to make the hour practical. Learners should see that these methods are small but high-impact.

**Instructor talk track**

"By the end of this hour, your main model should be more pleasant to work with. Pleasant does not mean cute or clever. It means that when the object appears in the places objects naturally appear, the output helps you."

"First term: **class ergonomics**. Ergonomics is about how comfortable and effective something is to use. A chair can be technically a chair but uncomfortable to sit in. A class can technically store data but be uncomfortable to debug, print, log, or pass around. Today we improve the developer experience and the user-facing display experience of our classes."

"Second term: `__repr__`. Pronounce it 'dunder repr' or just 'repr'. This is the developer-facing representation of an object. In Python, `repr(obj)` asks the object, 'How should developers inspect you?' Lists and dictionaries use `repr()` for the objects inside them. The interactive Python prompt uses `repr()` when it displays expression results. Debuggers and logs often benefit from repr-style output."

"A useful rule is: `__repr__` is for developers. It should be specific. It should include the important fields that help us understand the object's state. For simple model objects, it often looks like a constructor call."

"Third term: `__str__`. This is the user-facing or friendly string version of an object. `print(obj)` prefers `str(obj)`. A CLI menu, status message, UI label, or report line should usually use `__str__` because users do not need every internal detail."

"A useful rule is: `__str__` is for users. It should be readable. It can be shorter and more polished than `__repr__`."

"Fourth term: **type hints**. A type hint is an annotation that documents what kind of value a variable, parameter, or return value is expected to have. Type hints help humans understand the contract. They help IDEs autocomplete and warn. They help static tools if a team chooses to use them. But in normal Python execution, a hint does not automatically block the wrong value at runtime."

Show this tiny example:

```python
def summarize_title(title: str) -> str:
    return title.strip().title()
```

"This says `title` should be a string and the function should return a string. That is enough for today's scope."

"Fifth term: **serialization readiness**. Serialization means converting an object into a form that can be saved or sent, such as a dictionary that later becomes JSON. In the next hour, Checkpoint 1 requires serialization helpers, `to_dict` at minimum. So today we will treat `to_dict()` as checkpoint preparation, not as a random optional nice-to-have."

**Transition**

"Now let's talk about how these pieces behave in Python, and then we will code the upgrade."

---

## Concept Briefing: Readable Objects and Light Hints (10 minutes)

### 1. Why the default object display is not enough

**Instructor talk track**

"When we create a custom class and do nothing special, Python still gives it a representation. That representation usually includes the class name and a memory address. For example:"

```text
<__main__.Task object at 0x000001F2A8C4D910>
```

"This is not wrong. Python is telling us: this is a `Task` object, and here is where it lives in memory. The problem is that the memory address is rarely the information we need during application debugging. We usually need the object's meaningful state: id, title, status, priority, owner, or created date."

"When a bug report says 'sorting is wrong', a memory address does not help. When a checkpoint reviewer runs your demo and prints your service-layer list, memory addresses do not show that your data is correct. When a log line says a record failed validation, a memory address does not explain which record failed."

"So we give our class a better developer representation by implementing `__repr__`."

### 2. `__repr__` is for developers

Write or display:

```python
def __repr__(self) -> str:
    return (
        "Task("
        f"task_id={self.task_id!r}, "
        f"title={self.title!r}, "
        f"status={self.status!r}, "
        f"priority={self.priority!r}"
        ")"
    )
```

"Notice a few choices. First, it returns a string. It does not print. Python expects `__repr__` to return a string. If it returns `None`, Python will raise an error like `TypeError: __repr__ returned non-string (type NoneType)`."

"Second, the output includes field names. Field names make debug output easier to read than a plain tuple of values."

"Third, the example uses `!r` inside the f-string. That means use `repr()` for the individual value. For strings, it includes quotes, so the output is clearer. Compare `title=Write tests` with `title='Write tests'`. The second one makes it obvious that the title is a string. It also makes empty strings and extra spaces easier to notice."

"For a simple domain model, a good `__repr__` often looks like code you could use to recreate the object. It does not have to be perfect for every class, but it should be unambiguous enough for debugging."

### 3. `__str__` is for users

Write or display:

```python
def __str__(self) -> str:
    return f"#{self.task_id} {self.title} [{self.status}]"
```

"This output is shorter and friendlier. It is what we might show in a CLI list or a simple UI line. It does not include every internal detail. It chooses what the user needs."

"The most important contrast is this:"

```text
repr(task) -> Task(task_id=101, title='Write tests', status='open', priority=2)
str(task)  -> #101 Write tests [open]
```

"Neither is universally better. They serve different audiences. If I am debugging a failed sort or inspecting a list in the REPL, I want `repr`. If I am printing a user-facing menu, I want `str`."

### 4. How Python chooses between them

"Python uses these methods in predictable ways."

```python
task = Task(101, "Write tests", "open", 2)

print(task)        # Uses str(task), which calls task.__str__()
print(str(task))   # Also user-facing
print(repr(task))  # Developer-facing
print([task])      # The list uses repr(task) for the item inside
```

"This is why learners sometimes think their `__str__` is broken. They print a list of objects and see the `__repr__` output. That is expected. Containers such as lists and dictionaries use `repr()` for their contents because container output is usually developer-facing."

### 5. Type hints are lightweight documentation

"Now let's add type hints, but keep them light. The point today is not to master every feature in the `typing` module. The point is to make our intent obvious."

Show:

```python
class Task:
    def __init__(self, task_id: int, title: str, status: str, priority: int) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority
```

"The constructor returns `None` because constructors initialize the object; they do not return a separate result. For normal methods, annotate the return value based on what the method returns."

```python
def is_complete(self) -> bool:
    return self.status == "done"

def to_dict(self) -> dict[str, object]:
    return {
        "task_id": self.task_id,
        "title": self.title,
        "status": self.status,
        "priority": self.priority,
    }
```

"The return type `dict[str, object]` means the keys are strings and the values may be different simple types. In this dictionary, some values are integers and some are strings. `object` is a simple way to say 'values can be mixed' without introducing advanced typing. That is enough for this course moment."

"Important: type hints do not replace validation. If your constructor says `priority: int`, Python will still let someone call `Task(101, 'Write tests', 'open', 'high')` unless your code checks it. Type hints document intent and help tools. Validation enforces rules at runtime. We have already practiced validation in earlier hours."

### 6. Equality is a sidebar, not the main lesson

"The file title for this hour includes equality because equality is part of Pythonic class ergonomics. We will keep it light today because the runbook emphasis is `repr`, `str`, and type hints."

"By default, two custom objects compare equal only if they are the same object in memory. Sometimes you want two different `Task` objects with the same id to count as equal. That is when `__eq__` can help."

```python
def __eq__(self, other: object) -> bool:
    if not isinstance(other, Task):
        return False
    return self.task_id == other.task_id
```

"But there is a real footgun: when you define equality on a mutable class, Python may make the object unhashable. That affects use in sets and as dictionary keys. That behavior protects you from bugs where an object changes after it has been placed in a hash-based collection. For today, treat equality as an optional extension. If your project needs it, keep it simple and test it. Do not let equality take over the hour."

**Transition**

"Let's now code the required pieces. Watch how the object becomes easier to inspect after only a few small methods."

---

## Live Demo: Upgrade a Model for Debugging and Display (10 minutes)

The live demo is deterministic and runnable as plain Python. Type it in stages so learners can predict each output before you run it. If time is tight, paste the final version but still pause at the key questions.

### Step 1: Start with a baseline model

**Instructor talk track**

"First I will create a small `Task` model with no string methods. This is similar to many beginner classes: it stores data correctly, but it does not explain itself well when printed."

```python
class Task:
    def __init__(self, task_id, title, status, priority):
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority


tasks = [
    Task(101, "Write tests", "open", 2),
    Task(102, "Review PR", "blocked", 1),
]

print(tasks[0])
print(tasks)
```

Ask:

"What do you expect this to print? Will we see the task title?"

Run it. The exact memory address will differ, but the shape will be similar:

```text
<__main__.Task object at 0x000001F2A8C4D910>
[<__main__.Task object at 0x000001F2A8C4D910>, <__main__.Task object at 0x000001F2A8C4DA50>]
```

"That is the problem we are solving. The object exists, but the display does not help us."

### Step 2: Add type hints and `__repr__`

**Instructor talk track**

"Now I will add light type hints to the constructor and add `__repr__`. The type hints communicate expected values. The `__repr__` method improves developer-facing output."

```python
class Task:
    def __init__(self, task_id: int, title: str, status: str, priority: int) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority

    def __repr__(self) -> str:
        return (
            "Task("
            f"task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r}, "
            f"priority={self.priority!r}"
            ")"
        )


tasks = [
    Task(101, "Write tests", "open", 2),
    Task(102, "Review PR", "blocked", 1),
]

print(tasks[0])
print(tasks)
```

Ask before running:

"We added `__repr__`, but not `__str__`. What should `print(tasks[0])` use?"

Expected answer:

"If `__str__` is missing, Python falls back to `__repr__` for a direct `print()` call."

Run it:

```text
Task(task_id=101, title='Write tests', status='open', priority=2)
[Task(task_id=101, title='Write tests', status='open', priority=2), Task(task_id=102, title='Review PR', status='blocked', priority=1)]
```

"This is already much better. The list output is readable because lists use each item's `repr()`."

### Step 3: Add `__str__` for user-facing display

**Instructor talk track**

"Now I will add `__str__`. The user does not need every field in constructor style. The user needs a clean summary."

```python
class Task:
    def __init__(self, task_id: int, title: str, status: str, priority: int) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority

    def __repr__(self) -> str:
        return (
            "Task("
            f"task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r}, "
            f"priority={self.priority!r}"
            ")"
        )

    def __str__(self) -> str:
        return f"#{self.task_id} {self.title} [{self.status}, priority {self.priority}]"


task = Task(101, "Write tests", "open", 2)
tasks = [
    task,
    Task(102, "Review PR", "blocked", 1),
]

print(task)
print(repr(task))
print(tasks)
```

Run it:

```text
#101 Write tests [open, priority 2]
Task(task_id=101, title='Write tests', status='open', priority=2)
[Task(task_id=101, title='Write tests', status='open', priority=2), Task(task_id=102, title='Review PR', status='blocked', priority=1)]
```

"Now we can see the split clearly. `print(task)` is user-friendly. `repr(task)` and list output are developer-friendly."

### Step 4: Add hints to a couple methods and checkpoint-prep `to_dict()`

**Instructor talk track**

"The runbook for the next hour requires serialization helpers, `to_dict` at minimum. So I want to model that now. This is not a deep serialization lesson yet. It is a readiness step. A domain object should know how to expose its simple data in a dictionary shape that a service layer, JSON writer, API response, or test can use."

```python
class Task:
    def __init__(self, task_id: int, title: str, status: str, priority: int) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority

    def __repr__(self) -> str:
        return (
            "Task("
            f"task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r}, "
            f"priority={self.priority!r}"
            ")"
        )

    def __str__(self) -> str:
        return f"#{self.task_id} {self.title} [{self.status}, priority {self.priority}]"

    def is_complete(self) -> bool:
        return self.status == "done"

    def rename(self, new_title: str) -> None:
        self.title = new_title.strip()

    def to_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
        }


def format_task_for_log(task: Task) -> str:
    return f"Saving {task!r}"


task = Task(101, "Write tests", "open", 2)

print(str(task))
print(repr(task))
print(task.is_complete())
print(format_task_for_log(task))
print(task.to_dict())

task.rename("Write focused tests")
print(str(task))
```

Expected output:

```text
#101 Write tests [open, priority 2]
Task(task_id=101, title='Write tests', status='open', priority=2)
False
Saving Task(task_id=101, title='Write tests', status='open', priority=2)
{'task_id': 101, 'title': 'Write tests', 'status': 'open', 'priority': 2}
#101 Write focused tests [open, priority 2]
```

"Notice a few things. `is_complete` returns a `bool`. `rename` returns `None` because it changes the object in place. `to_dict` returns a dictionary. The helper function `format_task_for_log` receives a `Task` and returns a string. These hints are not advanced, but they clarify intent."

"Also notice `task!r` in the logging helper. Inside an f-string, `!r` asks for `repr(task)`. That is a nice way to say, 'Use the developer-facing representation here.'"

### Step 5: Show the common `None` pitfall quickly

**Instructor talk track**

"Here is the mistake to watch for during lab."

```python
def __str__(self) -> str:
    print(f"#{self.task_id} {self.title}")
```

"This looks reasonable at first glance, but it is wrong. It prints inside the method and then returns `None` by default. Python requires `__str__` to return a string. The correct version is:"

```python
def __str__(self) -> str:
    return f"#{self.task_id} {self.title}"
```

"Remember: `__str__`, `__repr__`, `to_dict`, and any method annotated as returning a value must actually return that value."

**Transition**

"Now it is your turn. You will upgrade your main model. Keep it simple, run it frequently, and check both developer-facing and user-facing output."

---

## Guided Lab: Make Your Model Pleasant to Work With (25 minutes)

### Lab goal

Upgrade the main model in your tracker project so it is easier to debug, easier to display, lightly type-hinted, and ready for the Day 2 Hour 4 checkpoint.

**Instructor framing**

"This lab is not about adding a lot of new application behavior. It is about making your existing model easier to use correctly. The model should explain itself in debug output, display cleanly for a user, and expose a dictionary shape for tomorrow's checkpoint work."

### Required lab tasks

Ask learners to complete these tasks in order:

1. **Choose your main model.**
   - Examples: `Task`, `Contact`, `InventoryItem`, `Expense`, `Note`, or `TrackerRecord`.
   - If your project has more than one model, choose the one that appears most often in service-layer output.

2. **Add or improve `__repr__(self) -> str`.**
   - Include the fields that matter for debugging.
   - Prefer field names in the output.
   - Use `!r` for values where quotes or exact representation help.
   - Example shape:

```python
def __repr__(self) -> str:
    return (
        "Task("
        f"task_id={self.task_id!r}, "
        f"title={self.title!r}, "
        f"status={self.status!r}"
        ")"
    )
```

3. **Add or improve `__str__(self) -> str`.**
   - Make it short and friendly.
   - Aim for CLI, UI, report, or menu readability.
   - Do not include every internal detail unless the user genuinely needs it.
   - Example shape:

```python
def __str__(self) -> str:
    return f"#{self.task_id} {self.title} [{self.status}]"
```

4. **Add type hints to at least three methods or functions.**
   - Include the constructor if it does not already have hints.
   - Include both parameters and return values.
   - Keep hints simple. Use `str`, `int`, `bool`, `float`, `list[str]`, and `dict[str, object]` where useful.
   - Good examples:

```python
def __init__(self, task_id: int, title: str, status: str) -> None:
    ...

def is_complete(self) -> bool:
    ...

def rename(self, new_title: str) -> None:
    ...
```

5. **Checkpoint-prep requirement: add or refine `to_dict(self) -> dict[str, object]`.**
   - This is required for checkpoint readiness even if you do not finish it inside the 25-minute lab.
   - If you finish early, complete it now.
   - If time runs out, mark it as a must-finish before Day 2 Hour 4 begins.
   - The next hour's checkpoint requires serialization helpers, `to_dict` at minimum.
   - Example:

```python
def to_dict(self) -> dict[str, object]:
    return {
        "task_id": self.task_id,
        "title": self.title,
        "status": self.status,
    }
```

6. **Run a small output check.**
   - Instantiate at least two objects.
   - Print one object directly.
   - Print `repr(one_object)`.
   - Print a list containing both objects.
   - Print `one_object.to_dict()`.
   - Confirm the output is readable in both logs and UI-style display.

### Suggested learner test snippet

Learners can adapt this snippet to their model names and fields:

```python
item_one = Task(101, "Write tests", "open", 2)
item_two = Task(102, "Review PR", "blocked", 1)

print("User display:")
print(item_one)

print("\nDeveloper display:")
print(repr(item_one))

print("\nList/debug display:")
print([item_one, item_two])

print("\nSerialization shape:")
print(item_one.to_dict())
```

Expected qualities:

- The user display is clean and short.
- The developer display includes class name and important fields.
- The list display is useful, not memory-address noise.
- The dictionary contains stable keys for the next checkpoint.

### Instructor circulation checklist

As learners work, circulate with these checks:

- "Show me `print(your_object)`. Is that what a user should see?"
- "Show me `repr(your_object)`. Is that enough for you to debug a failed service-layer operation?"
- "Show me a list of two objects. Does the list output help?"
- "Show me three type hints. Are they simple and correct?"
- "Show me one method annotated with `-> None`. Does it really return nothing?"
- "Show me one method annotated with a value such as `-> str`, `-> bool`, or `-> dict[str, object]`. Does it actually return that value?"
- "Show me `to_dict()`. Are the keys stable and predictable?"

### Lab pacing

Use this pacing guide:

- Minutes 0-5: Learners choose the model and add `__repr__`.
- Minutes 5-9: Learners add `__str__`.
- Minutes 9-15: Learners add simple type hints to at least three methods or functions.
- Minutes 15-20: Learners add or refine `to_dict()` for checkpoint readiness.
- Minutes 20-25: Learners run output checks and fix any `None` or formatting mistakes.

### If learners finish early

Offer one optional extension, keeping equality light:

**Option A: Add equality comparison.**

```python
def __eq__(self, other: object) -> bool:
    if not isinstance(other, Task):
        return False
    return self.task_id == other.task_id
```

Tell learners:

"If you add equality, test it. Also know the footgun: custom equality on mutable objects can affect hashability, which affects using instances in sets or as dictionary keys. That is why equality is an extension today, not the center of the lab."

**Option B: Add a small logging helper.**

```python
def format_task_for_log(task: Task) -> str:
    return f"Processing {task!r}"
```

Tell learners:

"This is a good place to practice `!r` in an f-string. Logs usually want developer-facing output."

Do not introduce dataclasses, pydantic, mypy configuration, abstract base classes, protocols, or advanced generic typing in this lab. Those may be useful in other contexts, but they are outside today's runbook scope.

---

## Troubleshooting and Common Pitfalls

Use these notes during the lab and the final wrap-up.

### Pitfall 1: `__str__` or `__repr__` prints instead of returns

Problem:

```python
def __str__(self) -> str:
    print(self.title)
```

Why it fails:

- `print()` returns `None`.
- Python expects `__str__` to return a string.
- The annotation says `-> str`, but the method does not return a string.

Fix:

```python
def __str__(self) -> str:
    return self.title
```

Instructor language:

"String methods should answer Python's question, not do Python's job. Python asks, 'What string should represent you?' Your method should return the answer."

### Pitfall 2: Overcomplicated typing

Problem:

```python
from typing import Any, Callable, Iterable, Mapping, MutableMapping, Optional, Protocol, TypeVar
```

Why it is a problem today:

- These tools can be useful, but they distract from the required skill.
- Learners may spend the lab fighting syntax instead of improving the model.
- The runbook says light type hints.

Fix:

```python
def to_dict(self) -> dict[str, object]:
    ...
```

Instructor language:

"If a simple built-in annotation explains the method, use the simple annotation. Advanced typing is not the goal today. Readability is the goal."

### Pitfall 3: Hints treated as runtime validation

Problem:

```python
def __init__(self, priority: int) -> None:
    self.priority = priority

task = Task("high")
```

Why it is a problem:

- Python does not automatically reject `"high"` just because the hint says `int`.
- If the value must be enforced, write validation.

Fix:

```python
def __init__(self, priority: int) -> None:
    if not isinstance(priority, int):
        raise TypeError("priority must be an integer")
    self.priority = priority
```

Instructor language:

"Hints communicate. Validation enforces. We often use both, but they are not the same tool."

### Pitfall 4: `__repr__` hides important state

Problem:

```python
def __repr__(self) -> str:
    return "Task()"
```

Why it is a problem:

- The output no longer shows enough data to debug.
- A list of different tasks will look like `[Task(), Task(), Task()]`.

Fix:

```python
def __repr__(self) -> str:
    return f"Task(task_id={self.task_id!r}, title={self.title!r}, status={self.status!r})"
```

Instructor language:

"A good `repr` earns its place by helping you inspect state. Include the fields that explain the object's identity and current condition."

### Pitfall 5: `__str__` becomes too technical

Problem:

```python
def __str__(self) -> str:
    return (
        f"Task(task_id={self.task_id!r}, title={self.title!r}, "
        f"status={self.status!r}, priority={self.priority!r}, "
        f"created_at={self.created_at!r}, updated_at={self.updated_at!r})"
    )
```

Why it is a problem:

- The user-facing display is too noisy.
- It duplicates the role of `__repr__`.

Fix:

```python
def __str__(self) -> str:
    return f"#{self.task_id} {self.title} [{self.status}]"
```

Instructor language:

"If the output is for a user, make a choice. What does the user need at a glance?"

### Pitfall 6: Equality grows beyond the hour

Problem:

Learners spend most of the lab designing complicated equality rules.

Why it is a problem:

- The runbook emphasis is `__repr__`, `__str__`, and type hints.
- Equality can be useful, but it has consequences for hashability and collection behavior.

Fix:

- Keep equality as an optional extension.
- If used, compare one stable identifier or a small set of meaningful fields.
- Test `a == b` and `a != b`.
- Avoid making mutable objects dictionary keys unless the design is deliberate.

Instructor language:

"Equality is a real Pythonic ergonomics topic, but today it is a sidebar. Do not let it steal time from readable objects and checkpoint readiness."

---

## Quick Checks, Completion Criteria, and Wrap-Up (5 minutes)

### Quick check 1: `repr` versus `str`

Ask:

"When would you look at `__repr__` output versus `__str__` output?"

Expected answer:

"Use `__repr__` output when debugging, inspecting logs, looking at objects inside lists or dictionaries, using the Python REPL, or trying to understand exact object state. Use `__str__` output when displaying a friendly message to a user, such as a CLI menu item, UI label, report line, or normal `print()` meant for people using the app."

Follow-up if time allows:

"If you print a list of objects, which representation does Python usually use for the items?"

Expected answer:

"The list uses `repr()` for its items."

### Quick check 2: Type hints

Ask:

"Do type hints automatically stop bad values at runtime?"

Expected answer:

"No. They help humans and tools. Runtime validation still needs explicit code."

### Completion criteria

Before learners leave, ask them to verify:

- Their main model has `__repr__(self) -> str`.
- Their main model has `__str__(self) -> str`.
- Objects print cleanly for user-facing output.
- Lists or logs of objects show useful developer-facing output.
- At least three methods or functions have simple, correct type hints.
- Hints do not break runtime behavior.
- Methods annotated as returning a value actually return that value.
- Methods annotated as `-> None` are intentionally used for side effects.
- `to_dict(self) -> dict[str, object]` exists or is clearly marked as a must-finish before the next checkpoint.

### Closing bridge to Day 2 Hour 4 Checkpoint 1

**Instructor talk track**

"Today we made the model easier to work with. That may sound small, but it has a direct checkpoint purpose. In the next hour, Checkpoint 1 asks for a stable domain and service layer. A stable core is not just code that exists. It is code that can be demonstrated, inspected, and reused by later GUI or API layers."

"When the checkpoint reviewer runs your small demo script, clean `__str__` output makes the application easier to understand. When something fails, useful `__repr__` output makes debugging faster. When another developer reads your method signatures, light type hints explain what values are expected. And when we move toward persistence, APIs, or JSON, `to_dict()` gives the object a predictable serialization shape."

"So the bridge is this: **Hour 7 made objects readable and debuggable; Hour 8 checks that the domain and service layer are stable and serialization-ready.**"

"Before the next hour begins, make sure your main model has the required ergonomics and a `to_dict()` helper. If you did not finish `to_dict()` during lab, treat it as checkpoint preparation homework, not as optional polish."

### Final instructor note

"Praise small improvements here. A learner who changes unreadable object output into clear `repr`, clear `str`, and a simple dictionary shape has made a professional-quality improvement. Keep reinforcing that advanced Python is often about making code easier to reason about, not making code more complicated."

---

## Instructor Reference: Complete Demo Code

Use this complete snippet if you need a clean reference during class.

```python
class Task:
    def __init__(self, task_id: int, title: str, status: str, priority: int) -> None:
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority

    def __repr__(self) -> str:
        return (
            "Task("
            f"task_id={self.task_id!r}, "
            f"title={self.title!r}, "
            f"status={self.status!r}, "
            f"priority={self.priority!r}"
            ")"
        )

    def __str__(self) -> str:
        return f"#{self.task_id} {self.title} [{self.status}, priority {self.priority}]"

    def is_complete(self) -> bool:
        return self.status == "done"

    def rename(self, new_title: str) -> None:
        self.title = new_title.strip()

    def to_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
        }


def format_task_for_log(task: Task) -> str:
    return f"Saving {task!r}"


def main() -> None:
    task = Task(101, "Write tests", "open", 2)
    tasks = [
        task,
        Task(102, "Review PR", "blocked", 1),
    ]

    print("User display:")
    print(task)

    print("\nDeveloper display:")
    print(repr(task))

    print("\nList/debug display:")
    print(tasks)

    print("\nCompletion check:")
    print(task.is_complete())

    print("\nLog message:")
    print(format_task_for_log(task))

    print("\nSerialization shape:")
    print(task.to_dict())

    task.rename("Write focused tests")
    print("\nAfter rename:")
    print(task)


if __name__ == "__main__":
    main()
```

Expected output:

```text
User display:
#101 Write tests [open, priority 2]

Developer display:
Task(task_id=101, title='Write tests', status='open', priority=2)

List/debug display:
[Task(task_id=101, title='Write tests', status='open', priority=2), Task(task_id=102, title='Review PR', status='blocked', priority=1)]

Completion check:
False

Log message:
Saving Task(task_id=101, title='Write tests', status='open', priority=2)

Serialization shape:
{'task_id': 101, 'title': 'Write tests', 'status': 'open', 'priority': 2}

After rename:
#101 Write focused tests [open, priority 2]
```
