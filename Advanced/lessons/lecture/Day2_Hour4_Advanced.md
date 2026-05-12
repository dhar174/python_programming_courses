# Day 2, Hour 4: Checkpoint 1: Domain + Service Layer Milestone

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 2, Hour 4 of 48, also Hour 8 in the Advanced runbook sequence
- **Focus**: Checkpoint 1 assessment for a reusable core tracker package: domain model, service layer, custom exceptions, serialization helper, and runnable demo.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 2, Hour 8.
- **Prerequisites**: Learners should have a tracker-style domain model from Day 2 Hour 1, callable or strategy-style thinking from Day 2 Hour 2, and readable class ergonomics from Day 2 Hour 3, including `__repr__`, `__str__`, light type hints, and `to_dict()`.
- **Advanced trajectory**: This hour stays in the PCAP-to-PCPP1 path. Learners are not building a GUI, API, database, or packaging workflow yet. They are proving that their domain and service code can stand on its own before later layers attach.
- **Instructor goal**: By the end of this hour, every learner has either passed Checkpoint 1 or has a precise next-step path for completing it. The target deliverable is a stable `src/` core library that runs through a small demo script and handles expected errors clearly.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge and checkpoint framing | 5 min | Connect Day 2 Hour 3 ergonomics to checkpoint grading and future reuse |
| Rubric walkthrough and expectations | 5 min | Make requirements concrete before learners code |
| Fast grading demo | 5 min | Show exactly how the instructor will run a demo, try invalid input, and try a missing record |
| Checkpoint build and grade lab | 40 min | Students finish the Core Tracker Library while the instructor circulates, checks, grades, and routes fast finishers |
| Exit ticket and wrap-up | 5 min | Capture design reflection and bridge to Day 3 project structure |

This is a one-hour checkpoint plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 5 + 40 + 5. The runbook notes that Checkpoint 1 work is 45-60 minutes; this hour protects 40 minutes for active checkpoint build and grading after 15 minutes of framing and demonstration. Keep the demo short. The checkpoint is the main event.

Recommended grading cadence:

1. Demonstrate briefly so everyone knows what "done" looks like.
2. Students work while you circulate with the checklist.
3. Grade stable submissions while students continue polishing.
4. Fast finishers attempt the tiny CLI wrapper extension only after passing the core checklist.
5. Incomplete students leave with a clear next-step path instead of a vague "keep working."

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain what "core tracker library" means: domain models plus service logic without UI, database, web routes, or interactive prompts inside the service layer.
2. Identify the minimum Checkpoint 1 requirements: two or more model classes, or one model plus one helper class; add/list/search/update/delete service functions; custom exceptions; `to_dict()` serialization; and a runnable demo.
3. Demonstrate a valid happy path using a small script that creates records, stores them through a service, lists them, searches them, updates them, deletes them, and serializes at least one record.
4. Demonstrate expected sad paths using invalid input and a missing record.
5. Use `ValidationError` for invalid data and `NotFoundError` for lookup/update/delete operations that target a record that does not exist.
6. Keep domain and service responsibilities separate from UI responsibilities.
7. Avoid global state by keeping record storage inside a service object or passing state explicitly.
8. Explain why stable core code makes later GUI, API, persistence, logging, and packaging work easier.
9. Reflect on one design decision they are proud of and explain why it helps the code.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 2, Hour 8 visible. The required outcome is a stable core package reusable by GUI/API layers. Required talk points are checkpoint expectations, rubric, and testing approach. Required demo is quick grading: run a script, try invalid input, and try a missing record.
- Keep the Day 2 Hour 1, Hour 2, and Hour 3 continuity in mind. Hour 1 used tracker vocabulary such as `TaskRecord`, `TrackerRecord`, `RecordFactory.from_dict()`, `ValidationError`, `title`, `owner`, `status`, `priority`, `estimate_minutes`, and `to_dict()`. Hour 2 used strategies over record dictionaries and callable behavior selection. Hour 3 used a simpler `Task` model and emphasized `__repr__`, `__str__`, type hints, and `to_dict()` as checkpoint preparation.
- Decide how learners should adapt names. The recommended message is: "You do not have to use my exact class names. If your project already uses `TaskRecord` instead of `Task`, keep that name. If you already have `TrackerRecord`, keep it. What matters is that the required responsibilities are present and easy to grade."
- Prepare the board with the rubric categories: models/helpers, service CRUD, custom exceptions, serialization, runnable demo, meaningful error handling.
- Open a terminal and be ready to run a copied demo script. The demo in this lecture is self-contained and deterministic.
- Decide whether you will grade live at each learner station or ask learners to call you over after their demo script passes. The suggested pattern is station grading: run their demo, ask one short design question, mark the checklist, and move on.
- Set expectations that partial progress is normal but must be precise. A learner who has a working model and add/list/search but no update/delete should know exactly what remains.

Recommended board note:

```text
Checkpoint 1 target:
Stable core first.
No GUI yet.
No database yet.
No API yet.
No service methods that call input().

Required:
models/helper + service CRUD + exceptions + to_dict() + runnable demo.
```

---

## Opening Bridge and Checkpoint Framing (5 minutes)

### Instructor talk track

"Welcome back. In the previous hour we made our classes easier to work with. We added readable `repr` output so developers can inspect objects. We talked about friendly `str` output for users. We added light type hints so a future reader can understand what each function expects and returns. We also treated `to_dict()` as checkpoint preparation, not as decoration."

"Today is where those choices start paying off."

"Checkpoint 1 is not a surprise feature request. It is a milestone. The goal is to prove that your core tracker code can stand on its own. When I say core tracker code, I mean the domain and service layer: the objects that represent the problem and the functions or methods that manage those objects."

Write or display:

```text
Domain model: What thing does the app manage?
Service layer: What operations can the app perform on those things?
UI/API/database: Later layers that should attach to the core, not live inside it.
```

"If you are building a task tracker, your domain object might be called `Task`, `TaskRecord`, or `TrackerRecord`. If you are building an inventory tracker, it might be `InventoryItem`. If you are building a contact tracker, it might be `Contact`. I will use `Task` and `TaskService` today because those names are easy to read, but you should adapt the names to your existing code. Do not rename a working project just to match my demo. Preserve the responsibilities."

"The stable core matters because later in the course we will add layers. Day 3 moves toward project structure, imports, logging, safer files, and decorators. Later sessions attach GUI and API layers. If your core logic already knows how to add, list, search, update, delete, validate, and serialize, those later layers mostly become adapters. If your core logic is tangled with `input()`, `print()`, global lists, GUI widgets, or web request objects, every later layer becomes harder."

Pause and ask:

"What did `to_dict()` prepare us for?"

Expected answers:

- Saving data later.
- Turning an object into a dictionary.
- JSON or API responses later.
- Easier checkpoint grading.

Affirm:

"Exactly. Today, `to_dict()` helps me grade quickly. Later, it helps you save to JSON, return API responses, and inspect data consistently."

Transition:

"Let's make the rubric explicit. Then I will show the exact style of fast demo I will use when grading."

---

## Rubric Walkthrough and Expectations (5 minutes)

### Instructor talk track

"Checkpoint grading should not feel mysterious. You should know what I am looking for before I look at your code. I am going to grade responsibilities, not fancy architecture."

"Here is the checklist. Use yes, partial, or not-yet. Points are optional; the important thing is that each row has evidence."

| Category | Yes evidence | Partial evidence | Not-yet evidence |
| --- | --- | --- | --- |
| Models/helpers | Has 2 or more model classes, or 1 model plus 1 helper class; constructors validate key fields; names match the learner's domain | Has a model but helper or second class is unclear; validation exists but is incomplete | Only raw dictionaries or disconnected variables; no clear model/helper responsibility |
| Service CRUD | Service layer supports add, list, search, update, and delete; operations are callable from a demo script | Some operations exist, but one or two are missing or only work through UI prompts | No service layer, or operations are scattered through global script code |
| Custom exceptions | Uses meaningful custom exceptions such as `ValidationError` and `NotFoundError`; expected errors are caught in the demo | Defines exceptions but uses them inconsistently, or catches broad `Exception` everywhere | Relies on generic crashes such as `KeyError`, `IndexError`, or unhandled `ValueError` |
| Serialization | Model has `to_dict()` at minimum; output includes enough fields to save or inspect the record later | `to_dict()` exists but omits important fields or returns inconsistent types | No serialization helper |
| Runnable demo | A small demo script runs end-to-end and proves happy path plus at least two sad paths | Demo runs partway or requires manual setup not explained | No runnable demo, or demo only works interactively |
| Meaningful error handling | Invalid input and missing records produce clear messages and do not crash the whole demo | Some errors are caught but messages are vague or one sad path crashes | Errors are not handled, or missing records are ignored silently |
| Separation of concerns | Model and service do not call `input()`; service returns values or raises exceptions; UI/printing stays in demo or optional wrapper | Some printing is mixed into service methods, but core operations can still be called | Service and UI are inseparable; grading requires typing through prompts |

"Notice what is not on this rubric. I am not grading a database. I am not grading a GUI. I am not grading Flask routes. I am not grading package publishing. Those are later. Today is core-domain readiness."

"Your testing approach is simple and practical: first run small examples, then run edge cases. A small example proves the happy path: create a valid task, add it, list it, search it, update it, delete it. Edge cases prove the sad path: missing title, invalid status, update a missing record, delete a missing record."

Use this short phrase:

```text
Small examples first. Edge cases second. Clear errors always.
```

"If you are unsure whether you are done, ask yourself: Could someone attach a GUI button to this service method later without rewriting the model? Could someone attach an API endpoint to this service method later without using `input()`? If yes, you are moving in the right direction."

Transition:

"Now I will show the grading demo. I will keep it short because your work time is the priority."

---

## Fast Grading Demo (5 minutes)

### Instructor setup

Tell learners:

"This is not the only acceptable design. It is a compact example of the responsibilities I am looking for. Your names may differ. You might use `TaskRecord` instead of `Task`, or `TrackerRecord` with a `RecordFactory.from_dict()`. That is fine. Preserve the responsibilities: model validation, service operations, custom exceptions, serialization, and a demo that proves both success and failure."

If using a file, call it something like `checkpoint_demo.py`. If showing it in a notebook or editor cell, explain that the same code can be placed in a plain Python script.

### Deterministic demo code

```python
from dataclasses import dataclass


class ValidationError(Exception):
    """Raised when task data does not satisfy the domain rules."""


class NotFoundError(Exception):
    """Raised when a requested task id does not exist."""


@dataclass
class Task:
    task_id: int
    title: str
    owner: str
    status: str = "todo"
    priority: int = 3
    estimate_minutes: int = 30

    VALID_STATUSES = {"todo", "doing", "done", "blocked"}

    def __post_init__(self) -> None:
        if self.task_id <= 0:
            raise ValidationError("task_id must be a positive integer")
        if not self.title.strip():
            raise ValidationError("title is required")
        if not self.owner.strip():
            raise ValidationError("owner is required")
        if self.status not in self.VALID_STATUSES:
            raise ValidationError(f"status must be one of {sorted(self.VALID_STATUSES)}")
        if not 1 <= self.priority <= 5:
            raise ValidationError("priority must be between 1 and 5")
        if self.estimate_minutes <= 0:
            raise ValidationError("estimate_minutes must be positive")

    def __str__(self) -> str:
        return f"{self.task_id}: {self.title} [{self.status}]"

    def to_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "owner": self.owner,
            "status": self.status,
            "priority": self.priority,
            "estimate_minutes": self.estimate_minutes,
        }


class TaskFactory:
    """Helper class that creates validated Task objects from dictionaries."""

    @staticmethod
    def from_dict(data: dict[str, object]) -> Task:
        try:
            return Task(
                task_id=int(data["task_id"]),
                title=str(data["title"]),
                owner=str(data["owner"]),
                status=str(data.get("status", "todo")),
                priority=int(data.get("priority", 3)),
                estimate_minutes=int(data.get("estimate_minutes", 30)),
            )
        except KeyError as exc:
            raise ValidationError(f"missing required field: {exc.args[0]}") from exc
        except ValueError as exc:
            raise ValidationError("task_id, priority, and estimate_minutes must be integers") from exc


class TaskService:
    """Service layer for managing Task objects without UI or database code."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}

    def add(self, task: Task) -> Task:
        if task.task_id in self._tasks:
            raise ValidationError(f"task id {task.task_id} already exists")
        self._tasks[task.task_id] = task
        return task

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def search(self, text: str) -> list[Task]:
        text = text.casefold()
        return [
            task
            for task in self._tasks.values()
            if text in task.title.casefold() or text in task.owner.casefold()
        ]

    def get(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError as exc:
            raise NotFoundError(f"task id {task_id} was not found") from exc

    def update(self, task_id: int, **changes: object) -> Task:
        current = self.get(task_id)
        updated_data = current.to_dict()
        updated_data.update(changes)
        updated = TaskFactory.from_dict(updated_data)
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> Task:
        task = self.get(task_id)
        del self._tasks[task_id]
        return task


def run_checkpoint_demo() -> None:
    print("--- Checkpoint 1 Demo ---")
    service = TaskService()

    print("\n1. Happy path: add, list, search, update, delete")
    first_task = TaskFactory.from_dict(
        {
            "task_id": 1,
            "title": "Write checkpoint demo",
            "owner": "Ari",
            "status": "todo",
            "priority": 2,
            "estimate_minutes": 45,
        }
    )
    second_task = TaskFactory.from_dict(
        {
            "task_id": 2,
            "title": "Review service layer",
            "owner": "Mina",
            "status": "doing",
            "priority": 1,
            "estimate_minutes": 30,
        }
    )

    service.add(first_task)
    service.add(second_task)
    print("All tasks:", [str(task) for task in service.list_all()])
    print("Search for 'review':", [task.to_dict() for task in service.search("review")])
    print("Updated:", service.update(1, status="done", estimate_minutes=50).to_dict())
    print("Deleted:", service.delete(2))
    print("Remaining:", [task.to_dict() for task in service.list_all()])

    print("\n2. Sad path: invalid input")
    try:
        TaskFactory.from_dict(
            {
                "task_id": 3,
                "title": "   ",
                "owner": "Ari",
                "status": "todo",
            }
        )
    except ValidationError as exc:
        print("Caught expected ValidationError:", exc)

    print("\n3. Sad path: missing record")
    try:
        service.update(999, status="done")
    except NotFoundError as exc:
        print("Caught expected NotFoundError:", exc)

    print("\nDemo completed.")


if __name__ == "__main__":
    run_checkpoint_demo()
```

### Instructor narration while running the demo

"When I grade quickly, I do not need a huge script. I need evidence. First I run the script. It should finish. Second I look for happy-path operations: add, list, search, update, delete. Third I look for invalid input. Here, a blank title raises `ValidationError` with a useful message. Fourth I look for a missing record. Here, updating task id 999 raises `NotFoundError` and the demo catches it."

"Also notice where the printing happens. The service does not print menu prompts. The service returns tasks or raises exceptions. The demo prints because the demo is the outer layer. Later a GUI could call `service.update(...)` and show the result in a label. Later an API endpoint could call `service.update(...)` and turn the result into JSON. The service itself stays reusable."

"Again, adapt names. If your existing code has `RecordFactory.from_dict()` instead of `TaskFactory.from_dict()`, keep it. If your model is `TaskRecord`, keep it. If your helper class is `TaskValidator`, that can also satisfy the model/helper requirement. The grading question is not 'Did you copy my names?' The grading question is 'Does your design have the required responsibilities?'"

Transition:

"Now you will build or finish your own Core Tracker Library. I will circulate with the checklist. When your demo passes, call me over."

---

## Checkpoint Build and Grade Lab (40 minutes)

### Student-facing lab prompt

"It is time to deliver Checkpoint 1: Build your Core Tracker Library."

"Your deliverable is a `src/` core that runs through a small demo script. It does not need a GUI. It does not need a database. It does not need a web API. It needs a stable domain and service layer that can be reused by those layers later."

Minimum requirements:

1. **Models/helpers**
   - Either two or more model classes, such as `Task` and `Project`, `TaskRecord` and `Owner`, or `InventoryItem` and `Category`.
   - Or one model plus one helper class, such as `Task` plus `TaskFactory`, `TrackerRecord` plus `RecordFactory`, or `TaskRecord` plus `TaskValidator`.
2. **Service layer**
   - Add a record.
   - List records.
   - Search records.
   - Update a record.
   - Delete a record.
3. **Custom exceptions**
   - At minimum, use a validation-style exception such as `ValidationError`.
   - Use a missing-record exception such as `NotFoundError` for lookups, updates, or deletes that cannot find a record.
4. **Serialization helper**
   - Implement `to_dict()` at minimum on the main model.
   - Include enough fields that a later JSON save or API response would be meaningful.
5. **Runnable demo**
   - Run your core from a small demo script.
   - Show a valid operation.
   - Show invalid input.
   - Show a missing record.
   - Catch expected errors and print clear messages.

### Suggested file organization

This checkpoint is not primarily about package structure yet. Day 3 will go deeper on packages, imports, and config. For today, choose a simple organization that your environment can run:

```text
src/
  models.py
  services.py
  exceptions.py
demo.py
```

or:

```text
src/
  tracker/
    __init__.py
    models.py
    services.py
    exceptions.py
demo.py
```

"If imports are slowing you down, keep the structure simple and ask for help. Do not spend the whole checkpoint fighting package imports. The core responsibilities matter most today."

### Practical lab timeline inside the 40-minute block

| Lab minute | Instructor action | Student action |
| --- | --- | --- |
| 0-5 | Ask students to run their current demo or smallest example immediately | Run what exists; write down the first failure |
| 5-15 | Circulate for architecture checks: model/service separation, no global state everywhere, no UI inside service | Fill missing model/helper, exception, or `to_dict()` pieces |
| 15-25 | Start grading early finishers; ask incomplete students to prioritize missing CRUD and error handling | Complete add/list/search/update/delete and rerun demo |
| 25-35 | Continue grading; route fast finishers to optional tiny CLI wrapper | Polish demo, fix invalid input and missing record cases |
| 35-40 | Final pass: mark yes/partial/not-yet and assign next steps | Save work, note what passed and what remains |

### Instructor circulation script

Use short, repeatable questions:

1. "Show me your main model. What fields define a valid record?"
2. "Where does validation happen?"
3. "Show me the service method that updates a record."
4. "What happens if I update an id that does not exist?"
5. "Show me `to_dict()`."
6. "Can I call your service without typing into `input()`?"
7. "Run your demo from a clean terminal."

If a learner is stuck, diagnose by responsibility:

- If there is no model, say: "First create the object that represents one record. Do not start with menus."
- If there is no service, say: "Now create the object or functions that manage a collection of records."
- If errors crash mysteriously, say: "Convert expected failures into custom exceptions with clear messages."
- If the demo is too large, say: "Shrink it. One valid record, one invalid record, one missing id."
- If they are building a UI, say: "Pause the UI. The UI is later. Prove the service first."

### Grading checklist for live use

Use this checklist while circulating. You can mark each row as Yes, Partial, or Not Yet.

| Requirement | Yes | Partial | Not Yet | Notes |
| --- | --- | --- | --- | --- |
| Has required model/helper structure |  |  |  | 2+ models or 1 model + 1 helper |
| Main model validates important fields |  |  |  | Title/owner/status/priority/estimate or domain equivalents |
| Main model has useful `__repr__` or `__str__` |  |  |  | From Hour 3; not the main checkpoint item, but helpful |
| Main model has `to_dict()` |  |  |  | Must return a dictionary |
| Service adds records |  |  |  | Should reject duplicate ids if ids are used |
| Service lists records |  |  |  | Should return data, not only print |
| Service searches records |  |  |  | Search can be by title, owner, status, category, etc. |
| Service updates records |  |  |  | Should validate updated result |
| Service deletes records |  |  |  | Should handle missing ids |
| Uses `ValidationError` or equivalent |  |  |  | Expected invalid input should not become a mystery crash |
| Uses `NotFoundError` or equivalent |  |  |  | Missing record should be explicit |
| Demo runs end-to-end |  |  |  | Start from command line or equivalent run button |
| Demo shows invalid input |  |  |  | Must catch and display meaningful error |
| Demo shows missing record |  |  |  | Must catch and display meaningful error |
| Core is separate from UI |  |  |  | No required `input()` inside service methods |

### What to say when grading a complete submission

"Good. Your demo runs end-to-end. I can see a model/helper structure, a service with add/list/search/update/delete, custom exceptions, `to_dict()`, and clear error handling. You have passed the core checkpoint. If you want a stretch task, add a tiny CLI wrapper that calls your service, but do not move business logic into the wrapper."

### What to say when grading a partial submission

"You are close, and here is the exact next step. You have the model and add/list/search. The missing checkpoint items are update/delete and missing-record handling. Finish those before adding any UI or persistence. Your next demo should show `service.update(missing_id, ...)` raising and catching `NotFoundError`."

or:

"You have working operations, but they are all inside a menu loop. Extract the core logic into a service method that I can call directly. The menu can call the service, but the service should not depend on the menu."

or:

"Your model can serialize with `to_dict()`, but invalid data still crashes as a generic `KeyError`. Add a custom `ValidationError` and catch it in the demo."

### Completion criteria

A learner is complete when:

- The core runs end-to-end through a small demo.
- The required model/helper structure is present.
- The service layer can add, list, search, update, and delete.
- Invalid input raises a meaningful validation-style custom exception.
- Missing records raise a meaningful not-found custom exception.
- The demo catches expected errors appropriately.
- The main model can serialize through `to_dict()`.
- Service logic is not trapped inside UI prompts or global script flow.

If a learner has only 5 minutes remaining and is incomplete, choose the shortest path to a valid partial:

1. Stop adding features.
2. Make the demo run the pieces that exist.
3. Add one clear custom exception.
4. Add a note in their own comments or README-style notes listing the missing checkpoint rows.
5. Ask them to finish the missing rows before the next session begins.

---

## Troubleshooting and Pitfalls

### Pitfall 1: Global state everywhere

Symptom:

```python
tasks = []

def add_task(task):
    global tasks
    tasks.append(task)
```

Instructor response:

"A tiny global list can work in a tiny script, but it becomes painful when a GUI, API, or test wants its own clean state. Prefer a service object that owns its records."

Better direction:

```python
class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
```

"This gives each `TaskService` instance its own storage. A demo can create a fresh service. A future test can create a fresh service. A future GUI can own one service instance. That is more reusable."

### Pitfall 2: No separation between model and UI

Symptom:

```python
class TaskService:
    def add_task(self):
        title = input("Title: ")
        print("Added task")
```

Instructor response:

"This method is hard to grade quickly because I cannot pass values directly. It is also hard to reuse from a GUI or API because it requires terminal input. Move `input()` and `print()` to the outer layer. Let the service accept arguments, return values, and raise exceptions."

Better direction:

```python
class TaskService:
    def add(self, task: Task) -> Task:
        self._tasks[task.task_id] = task
        return task
```

"A CLI can still exist later. It will call `service.add(task)`. The service should not become the CLI."

### Pitfall 3: No handling for missing records

Symptom:

```python
def delete(task_id):
    del tasks[task_id]
```

or:

```python
def update(task_id, title):
    task = tasks[task_id]
    task.title = title
```

Instructor response:

"A missing record is not a weird technical accident. It is an expected business case. Users type the wrong id. Records get deleted. Search results go stale. Your core should report that clearly."

Better direction:

```python
class NotFoundError(Exception):
    pass


def get(self, task_id: int) -> Task:
    try:
        return self._tasks[task_id]
    except KeyError as exc:
        raise NotFoundError(f"task id {task_id} was not found") from exc
```

"Now a GUI could show a friendly message, an API could return a 404-style response later, and a demo can prove the behavior."

### Pitfall 4: Updating without validation

Symptom:

```python
def update(self, task_id, changes):
    task = self._tasks[task_id]
    task.status = changes["status"]
```

Instructor response:

"If creation validates status but update does not, invalid records can sneak in after creation. A common pattern is to convert the current task to a dictionary, apply changes, and rebuild through the same factory or model validation."

Better direction:

```python
def update(self, task_id: int, **changes: object) -> Task:
    current = self.get(task_id)
    updated_data = current.to_dict()
    updated_data.update(changes)
    updated = TaskFactory.from_dict(updated_data)
    self._tasks[task_id] = updated
    return updated
```

"That pattern keeps creation and update rules aligned."

### Pitfall 5: Demo proves only the happy path

Symptom:

"The demo adds one valid record and prints it, but never tries invalid input or a missing id."

Instructor response:

"Happy path is necessary, but not enough. The runbook specifically calls for trying invalid input and a missing record. Add two small try/except blocks. Keep them deterministic."

Minimum sad-path demo shape:

```python
try:
    TaskFactory.from_dict({"task_id": 3, "title": "", "owner": "Sam"})
except ValidationError as exc:
    print("Caught expected validation error:", exc)

try:
    service.delete(999)
except NotFoundError as exc:
    print("Caught expected missing record:", exc)
```

---

## Optional Extension: Tiny CLI Wrapper

This extension is explicitly optional. Offer it only to learners who have passed the core checklist.

Instructor wording:

"If your core is done and graded, you may add a tiny CLI wrapper. Keep it tiny. The CLI is allowed to call `input()` and `print()`. The service layer should still not call `input()`."

Acceptable tiny wrapper shape:

```python
def print_tasks(service: TaskService) -> None:
    for task in service.list_all():
        print(task)


def main() -> None:
    service = TaskService()
    while True:
        command = input("Command (list/quit): ").strip().casefold()
        if command == "quit":
            break
        if command == "list":
            print_tasks(service)
        else:
            print("Unknown command")
```

"This wrapper is intentionally small. It is not a replacement for the checkpoint demo, and it is not permission to move validation or CRUD logic into the menu. It is just a thin layer around the service."

---

## Quick Checks During Lab

Use these questions when students ask whether they are done:

1. "Can your demo run from top to bottom without manual typing?"
2. "Where is your `ValidationError` raised?"
3. "Where is your `NotFoundError` raised?"
4. "Can I call your service methods from a GUI later?"
5. "What does `to_dict()` return?"
6. "If I update a task to an invalid status, what happens?"
7. "If I delete id 999, what happens?"

For a whole-class check at the 30-minute mark, ask:

"Raise your hand if your demo currently proves invalid input. Keep it up if it also proves a missing record."

Then say:

"If your hand went down, that tells you exactly what to add next. Do not add new features until those expected errors are covered."

---

## Exit Ticket and Wrap-up (5 minutes)

### Quick check question

Ask every learner to answer in a sentence, either aloud, in chat, or in their notes:

"What part of your design are you happiest with, and why?"

If time allows, have two learners share. Listen for answers like:

- "I am happy that update reuses the same validation as create."
- "I am happy that the service has no `input()` calls."
- "I am happy that `to_dict()` makes the demo and future saving easier."
- "I am happy that missing ids raise `NotFoundError` instead of crashing."
- "I am happy that my model names match my domain."

Affirm design reasoning, not just completion:

"That is the right kind of answer because it connects a code choice to a maintenance benefit."

### Closing bridge to Day 3

"Today you proved the foundation. A stable core comes first. Once the core can create, validate, manage, serialize, and report expected errors, the next layers have something reliable to call."

"In the next session we move into project structure, packages, imports, and config. That means we will take code like this and organize it more professionally. After that, logging and safer file operations become much easier because the core responsibilities are already clear. Later still, GUI and API layers can attach to the same service layer instead of duplicating business rules."

"If you passed today, your next job is to preserve this separation as the project grows. If you are partial, your next job is not to add a GUI or database. Your next job is to finish the missing checkpoint rows: service CRUD, custom exceptions, `to_dict()`, runnable demo, and meaningful error handling."

Final sentence:

"Stable core first. Fancy layers later."

---

## Instructor Notes After Class

After the hour, record common patterns you saw:

- Which requirement most learners missed?
- Did learners understand the difference between service methods and UI prompts?
- Did missing-record handling appear consistently?
- Did learners reuse validation during update, or only during creation?
- Did `to_dict()` include enough fields for later persistence?
- Did imports or folder layout consume too much checkpoint time?

Use those notes to tune Day 3. If many learners struggled with imports, keep Day 3 Hour 1 very practical. If many learners mixed UI and service code, keep returning to the rule: outer layers handle interaction; core layers handle domain rules.

Suggested instructor summary to post after class:

```text
Checkpoint 1 recap:
- Core tracker library first.
- Model/helper responsibilities must be clear.
- Service supports add/list/search/update/delete.
- ValidationError handles invalid data.
- NotFoundError handles missing records.
- to_dict() prepares us for persistence and APIs.
- Demo proves happy path plus edge cases.
```

This checkpoint is an assessment, but it is also scaffolding. The better the core is now, the less rewriting learners will do when the course adds structure, logging, files, GUI, APIs, testing, and packaging.
