# Day 1, Hour 2: Designing Classes from Requirements

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 1, Hour 2 of 48
- **Focus**: Translating requirements into classes, responsibilities, and boundaries.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 1, Hour 2.
- **Prerequisites**: Learners should be able to write functions, define simple classes, instantiate objects, use lists and dictionaries, read basic tracebacks, and run a Python file from the terminal.
- **Advanced trajectory**: This hour moves learners from a PCAP-level "I can write a working script" mindset toward a PCPP1-style design mindset: objects have responsibilities, boundaries are intentional, business rules are testable, and user interface code is not mixed into the core model.
- **Instructor goal**: By the end of this hour, every learner has sketched 3 to 5 tracker-domain classes, identified what each class knows and does, implemented at least one working class, and written a small separate service function that uses the model without putting `input()` or `print()` inside the model object.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Hour 1 | 5 min | Connect setup and Git workflow to design work |
| Outcomes and design vocabulary | 5 min | Establish responsibilities, boundaries, and layers |
| Concept briefing: from requirements to classes | 10 min | Teach responsibility-driven design in plain language |
| Live demo: tracker domain model and service function | 10 min | Model class responsibilities and UI separation |
| Guided lab: domain modeling for learner tracker | 25 min | Learners sketch 3 to 5 classes and implement one |
| Debrief and troubleshooting review | 3 min | Surface common design issues before they harden |
| Quick check and wrap-up | 2 min | Confirm the main boundary lesson and preview Hour 3 |

This is a one-hour plan. If the room needs more support, protect the 25-minute guided lab. Shorten the concept briefing before shortening learner practice. Do not allow the live demo to grow into a full application build; the target is design thinking, not feature completion.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Translate a short requirements list into candidate classes for a tracker-style application.
2. Describe a class in terms of what it **knows** and what it **does**.
3. Explain why user interface actions such as `input()` and `print()` should stay outside domain model classes.
4. Identify reasonable boundaries between model objects, service functions, and presentation code.
5. Implement a small Python class with type hints, an initializer, and at least one behavior method.
6. Write a deterministic service function that uses model objects without mixing in terminal interaction.
7. Recognize common early design pitfalls, including overcomplicated inheritance and oversized classes.
8. State where validation and business rules should live in a small application.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Open the Hour 1 project workspace you used during the previous session, or prepare a clean `advanced_tracker` folder with a `src/` directory.
- Confirm the terminal command for the environment. Use `python day1_hour2_tracker_demo.py` if `python` works. If the lab requires `python3`, consistently say and show `python3 day1_hour2_tracker_demo.py`.
- Keep the runbook section for Session 1, Hour 2 visible for yourself. The required scope is class design from requirements, responsibilities and boundaries, a simple service layer function, and a domain modeling lab.
- Prepare a blank file named `day1_hour2_tracker_demo.py` for the live demo, or be ready to create it in front of the class.
- Prepare a whiteboard area or shared note with these three prompts:

```text
Requirement:
Class:
Knows:
Does:
Boundary:
```

- Be ready to stop learners who place `input()` or `print()` inside their model classes. Correct this gently and early. This is the central habit for the hour.
- Decide whether your lab examples will use tasks, inventory, contacts, or expenses. This script uses a task tracker. Learners may choose any tracker domain for their lab.

Suggested board note before the session starts:

```text
Day 1 Hour 2 goals:
1. Turn requirements into classes
2. Decide what each object knows and does
3. Keep UI separate from core logic
4. Implement one small testable model
5. Use a service function to coordinate objects
```

---

## Opening Bridge from Hour 1 (5 minutes)

**Instructor talk track**

"In Hour 1, we focused on readiness. We launched the lab, confirmed that files persist when saved properly, created a project workspace, and used Git as a checkpoint system. That work may have felt like setup, but it matters because advanced programming is not only about writing more Python. It is about building a reliable workflow around Python."

"Now we are going to shift from environment readiness to design readiness. In Basics, it was normal to write a script from top to bottom: ask the user a question, store an answer in a variable, put a few values in a dictionary, print a result, and move on. That is a good way to learn syntax. But as programs grow, that style becomes difficult to change."

"Today we begin the core Advanced habit: before we write a lot of code, we ask what responsibilities exist in the problem. Who owns the data? Who owns the behavior? Who coordinates the work? Who talks to the user? When we answer those questions clearly, our code becomes easier to test, easier to extend, and easier to explain."

Pause and ask:

"Think about a simple tracker app. It could track tasks, contacts, expenses, workouts, books, inventory items, or support tickets. What are two things such an app usually needs to remember?"

Take a few quick answers. Connect them to classes:

"Good. You are naming data: title, due date, status, price, email address, quantity, priority. Now the next design question is: what object should own that data, and what behavior belongs with it?"

"That question is the bridge from script writing to object-oriented design. We are not using classes just because classes look advanced. We use classes when they help us group related data and behavior behind a clear responsibility."

**Transition**

"The focus for this hour is not to build a complete app. The focus is to design the small core that a complete app could grow around."

---

## Outcomes and Design Vocabulary (5 minutes)

Use this section to make the vocabulary accessible before the demo.

**Instructor talk track**

"There are four terms I want us to use carefully today: requirement, responsibility, boundary, and service."

"A **requirement** is something the program must do or support. For example: users can create a task, mark a task complete, list pending tasks, or calculate how many tasks are overdue. Requirements are written from the outside view of the program."

"A **responsibility** is a job owned by a piece of code. In responsibility-driven design, we ask two questions about an object: what does it know, and what does it do?"

Write:

```text
Object responsibility:
- Knows: the data it owns
- Does: the behavior it can perform
```

"For example, a `Task` object might know its title, priority, and status. It might know whether it is complete. It might do things like mark itself complete or change its priority. That is different from saying the `Task` should ask the user what to type. Asking the user is a user interface responsibility, not a task responsibility."

"A **boundary** is a line between responsibilities. A healthy boundary lets one part of the program change without forcing every other part to change. If the model is separate from the terminal interface, then later we can add a web page, a desktop interface, or automated tests without rewriting the `Task` class."

"A **service function** is a small coordinating function. It uses one or more model objects to complete a use case. It is not necessarily a class. Sometimes a plain function is the clearest tool. For example, a function named `complete_task_by_title(project, title)` might search a project for a task and mark it complete. That function coordinates objects. The `Task` still owns the behavior of becoming complete."

**Instructor emphasis**

"This distinction is important for your capstone. Model objects should represent the domain. Service functions can coordinate the domain. UI code can collect input and display output. If those three concerns are tangled together, the project becomes harder to test and harder to grow."

**Short prediction prompt**

"Suppose I write a `Contact` class, and inside its `__init__` method I call `input('Email: ')`. What problem does that create?"

Expected learner answers:

- It is hard to create a contact in a test.
- It forces every contact to come from the terminal.
- It makes the model depend on the user interface.
- It makes the object less reusable.

Affirm:

"Exactly. The model should accept data. It should not be responsible for asking where the data came from."

---

## Concept Briefing: From Requirements to Classes (10 minutes)

**Instructor talk track**

"Let's practice the design process before writing code. We will use a task tracker because it is familiar, but the same process works for expenses, contacts, inventory, or any small capstone tracker."

Display this requirements list:

```text
Task tracker requirements:
1. A user can create tasks with a title and priority.
2. A task starts as pending.
3. A user can mark a task complete.
4. A project can contain multiple tasks.
5. The program can list pending tasks.
6. The program can count completed tasks.
7. The program can produce a simple summary for display.
```

"The first mistake many developers make is to turn every noun into a class immediately. Nouns are clues, not automatic classes. The words task, priority, project, user, program, and summary all appear here. Some may become classes; some may become attributes; some may just become functions."

"The second mistake is to make one giant manager object that does everything. A `TaskManager` that creates tasks, stores tasks, prints menus, reads input, writes files, calculates reports, validates priorities, sends emails, and formats tables is not a design. It is a junk drawer. Advanced design is partly about resisting the junk drawer."

"Here is a simple way to move from requirements to classes."

Write:

```text
Step 1: Underline important nouns and verbs.
Step 2: Group related data and behavior.
Step 3: Name candidate classes.
Step 4: For each class, list what it knows and does.
Step 5: Decide what does NOT belong in the class.
```

"Step 5 matters. A good class definition is not only a list of what belongs. It is also a boundary against what does not belong."

### Sketching Candidate Classes

Walk through this sketch verbally.

```text
Candidate class: Task
Knows:
- title
- priority
- completed status
Does:
- mark itself complete
- report whether it is pending
- change priority, if allowed
Does not:
- ask the user for a title
- print itself to the screen as the only way to access its data
- save itself to a database during this hour
```

```text
Candidate class: Project
Knows:
- project name
- list of Task objects
Does:
- add a task
- return pending tasks
- count completed tasks
Does not:
- display a menu
- read from input()
```

```text
Candidate class: Tag
Knows:
- tag name
Does:
- normalize or compare tag names, if needed later
Does not:
- own the whole project
```

```text
Candidate class: TaskReport
Knows:
- maybe summary values, if reporting becomes complex
Does:
- format or calculate report data, if needed later
Does not:
- mutate tasks unless that is clearly part of the requirement
```

```text
Candidate class: TaskRepository
Knows:
- where tasks are stored, later
Does:
- save and load tasks, later
Does not:
- decide business rules such as what makes a valid priority
```

"Notice that we sketched five possible classes, but we do not have to implement all five today. Sketching is cheap. It helps us see the shape of the application. Implementation is more expensive, so we start with the smallest useful slice."

**Responsibility-driven design question**

"If you are unsure where a behavior belongs, ask: who has the information needed to do this job?"

"Who can mark a task complete? The `Task` can, because the completion status belongs to the task."

"Who can list all pending tasks in a project? The `Project` can, because it knows the list of tasks."

"Who can ask a human which task to complete? The UI layer can, because that is interaction with the outside world."

"Who can coordinate the use case 'complete the task named Write report'? A service function can, because it may need to search the project, find the correct task, and call the task's behavior."

**Transition to code**

"Now let's turn that sketch into a small deterministic Python demo. Deterministic means the output is predictable every time. There will be no `input()` in this demo. We want code that can be run in class, copied by learners, and later tested."

---

## Live Demo: Tracker Domain Model and Service Function (10 minutes)

**Instructor action cue**

Create a file named `day1_hour2_tracker_demo.py`. Use the same command later when running it:

```bash
python day1_hour2_tracker_demo.py
```

If the lab uses `python3`, say:

```bash
python3 day1_hour2_tracker_demo.py
```

Do not switch command names halfway through the demo. Consistency prevents avoidable learner errors.

### Demo Part 1: Model Objects Only

**Instructor talk track**

"First, I am going to write the model. The model is the core logic. It should not know whether it is being used by a terminal program, a web app, a notebook, or a test."

Type or paste:

```python
from __future__ import annotations


class Task:
    """A single task in a tracker project."""

    allowed_priorities = {"low", "medium", "high"}

    def __init__(self, title: str, priority: str = "medium") -> None:
        cleaned_title = title.strip()
        cleaned_priority = priority.strip().lower()

        if not cleaned_title:
            raise ValueError("Task title cannot be empty.")

        if cleaned_priority not in self.allowed_priorities:
            raise ValueError(
                f"Priority must be one of: {', '.join(sorted(self.allowed_priorities))}."
            )

        self.title = cleaned_title
        self.priority = cleaned_priority
        self.is_complete = False

    def mark_complete(self) -> None:
        self.is_complete = True

    def is_pending(self) -> bool:
        return not self.is_complete

    def change_priority(self, new_priority: str) -> None:
        cleaned_priority = new_priority.strip().lower()

        if cleaned_priority not in self.allowed_priorities:
            raise ValueError(
                f"Priority must be one of: {', '.join(sorted(self.allowed_priorities))}."
            )

        self.priority = cleaned_priority

    def __str__(self) -> str:
        status = "done" if self.is_complete else "pending"
        return f"{self.title} [{self.priority}, {status}]"


class Project:
    """A project that groups related tasks."""

    def __init__(self, name: str) -> None:
        cleaned_name = name.strip()

        if not cleaned_name:
            raise ValueError("Project name cannot be empty.")

        self.name = cleaned_name
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if task.is_pending()]

    def completed_count(self) -> int:
        return sum(1 for task in self.tasks if task.is_complete)
```

**Instructor explanation**

"Let's pause. We have two classes. `Task` knows its title, priority, and completion status. `Task` can mark itself complete, answer whether it is pending, change priority, and provide a friendly string representation."

"`Project` knows its name and a list of `Task` objects. It can add a task, return pending tasks, and count completed tasks."

"Notice what is missing. There is no `input()` here. There is no menu. There is no `print()` inside `mark_complete`. That is deliberate. These classes are usable from a terminal program, a test file, a web route, or a notebook because they are not tied to one interface."

"Also notice that validation is close to the data it protects. A task title cannot be empty, so the `Task` initializer checks that. A project name cannot be empty, so the `Project` initializer checks that. Priority must be one of a small allowed set, so the `Task` class owns that rule."

**Mini-prediction**

"What do you think happens if I try `Task('', 'high')`?"

Expected answer:

"It raises a `ValueError` because the title is empty."

Affirm:

"Correct. The model protects its own core rules."

### Demo Part 2: A Service Function

**Instructor talk track**

"Now we will add a service function. The service function coordinates a use case. It does not replace the model. It uses the model."

Add below the classes:

```python
def complete_task_by_title(project: Project, title: str) -> bool:
    """Mark the first pending task with this title complete.

    Returns True if a task was found and completed.
    Returns False if no matching pending task was found.
    """
    target_title = title.strip().lower()

    for task in project.pending_tasks():
        if task.title.lower() == target_title:
            task.mark_complete()
            return True

    return False


def build_project_summary(project: Project) -> str:
    """Format summary text without printing inside the model."""
    total_tasks = len(project.tasks)
    completed_tasks = project.completed_count()
    pending_tasks = total_tasks - completed_tasks

    lines = [
        f"Project: {project.name}",
        f"Total tasks: {total_tasks}",
        f"Completed tasks: {completed_tasks}",
        f"Pending tasks: {pending_tasks}",
        "Pending task list:",
    ]

    for task in project.pending_tasks():
        lines.append(f"- {task}")

    return "\n".join(lines)
```

**Instructor explanation**

"The function `complete_task_by_title` is a service function. It coordinates a use case: given a project and a title, find a pending task with that title and complete it. The function does not directly set `task.is_complete = True`. Instead, it calls `task.mark_complete()`. That keeps the task's behavior inside the task."

"The function returns `True` or `False`. It does not print success or failure. Why? Because printing is a display decision. A terminal UI may print. A web app may return JSON. A test may assert the boolean value. Returning data gives the caller choices."

"The function `build_project_summary` is a formatter/report helper, not the service layer. It prepares display text, but it still does not print by itself. This makes it easy to test. A test can compare the returned string or check that it contains expected lines."

### Demo Part 3: Deterministic Demo Block

**Instructor talk track**

"Finally, we need a small demo block. This is the only part that prints, and it lives outside the model. In a larger project, this might be in a separate `main.py` file. For today's demonstration, keeping it at the bottom is fine."

Add:

```python
def main() -> None:
    project = Project("Day 1 Tracker")
    project.add_task(Task("Sketch tracker classes", "high"))
    project.add_task(Task("Implement one model", "medium"))
    project.add_task(Task("Separate UI from logic", "high"))

    was_completed = complete_task_by_title(project, "Implement one model")

    print(f"Completed requested task: {was_completed}")
    print()
    print(build_project_summary(project))


if __name__ == "__main__":
    main()
```

Run:

```bash
python day1_hour2_tracker_demo.py
```

Expected output:

```text
Completed requested task: True

Project: Day 1 Tracker
Total tasks: 3
Completed tasks: 1
Pending tasks: 2
Pending task list:
- Sketch tracker classes [high, pending]
- Separate UI from logic [high, pending]
```

**Instructor explanation**

"This output is deterministic. Everyone should see the same result. The task named `Implement one model` is completed, so it no longer appears in the pending task list."

"Now let's inspect the boundary. Where is validation? The model validates titles, names, and priorities. Where is coordination? The service function searches the project and calls the task behavior. Where is output? The `main()` function prints. That gives us three layers, even in a small file."

Write:

```text
Model: Task, Project
Service/use case: complete_task_by_title()
Report/formatter: build_project_summary()
Presentation/demo: main() and print()
```

"Do not worry if those layer names feel formal. The habit is the important part: keep the core logic independent from the way humans interact with it."

### Demo Part 4: Show the Anti-Pattern Briefly

Do not spend long here. Show only enough to make the pitfall visible.

**Instructor talk track**

"Here is what I do not want in the model."

```python
# Avoid this pattern inside a domain model:
class BadTask:
    def __init__(self) -> None:
        self.title = input("Task title: ")

    def mark_complete(self) -> None:
        self.is_complete = True
        print("Task completed!")
```

"This looks convenient in a tiny script, but it creates hidden costs. I cannot create a `BadTask` in an automated test without pretending to type at the terminal. I cannot reuse it in a web app without rewriting it. I cannot mark it complete silently if another part of the program needs that. The model has become tangled with the UI."

"The better pattern is: collect input elsewhere, pass clean values into the model, let the model enforce business rules, and let the caller decide how to display results."

---

## Guided Lab: Domain Modeling for a Tracker (25 minutes)

**Instructor setup**

"Now you will design your own tracker domain. You do not need to build a complete application. Your goal is to practice the design process. By the end of the lab, you should have a short requirements list, 3 to 5 candidate classes, and at least one working class with a behavior method."

Give learners this prompt:

```text
Choose one tracker domain:
- Tasks
- Inventory
- Contacts
- Expenses
- Books or media
- Workouts
- Support tickets
- Your own small tracker idea
```

### Step 1: Pick a Theme and Write Requirements

**Instructor talk track**

"First, choose a theme. Then write 5 to 8 requirements. Keep them small. A good requirement for today is not 'build a complete business platform.' A good requirement is something like 'an expense has an amount and category' or 'an inventory item can be restocked.'"

Examples:

```text
Expense tracker requirements:
1. An expense has a description, amount, and category.
2. The amount must be greater than zero.
3. An expense can be marked reimbursed.
4. A report can calculate total unreimbursed expenses.
5. A tracker can hold multiple expenses.
```

```text
Inventory tracker requirements:
1. An item has a name, quantity, and reorder level.
2. Quantity cannot be negative.
3. An item can be restocked.
4. An item can be sold or used.
5. The tracker can list items below reorder level.
```

"If you are stuck, use tasks. The goal is design practice, not having the most original idea."

### Step 2: Sketch 3 to 5 Classes

Ask learners to use this template:

```text
Class name:
Knows:
-
-
Does:
-
-
Does not:
-
```

**Instructor talk track**

"For each class, use plain English first. Do not start with code. If you cannot explain the class in plain English, the code will probably become confusing."

"Your class list should be small. Three to five classes is enough. If you have ten classes after five minutes, you are probably designing too far ahead. If you have only one class that does everything, look for responsibilities that can be separated."

Suggested class patterns:

```text
Task tracker:
- Task
- Project
- Tag
- TaskReport
- TaskRepository later
```

```text
Inventory tracker:
- InventoryItem
- Inventory
- Supplier
- ReorderRule
- InventoryReport
```

```text
Expense tracker:
- Expense
- ExpenseCategory
- ExpenseTracker
- ReimbursementReport
- ExpenseRepository later
```

```text
Contact tracker:
- Contact
- AddressBook
- ContactGroup
- DuplicateContactPolicy
- ContactReport
```

"The word 'later' is useful. It means you can name a future responsibility without implementing it today. Advanced design includes restraint."

### Step 3: Choose One Class to Implement

**Instructor talk track**

"Now choose one class to implement. Pick the class with the clearest data and behavior. Usually that is the central object: `Task`, `InventoryItem`, `Expense`, or `Contact`."

Minimum implementation:

```text
Your class must include:
1. __init__
2. At least two attributes
3. At least one behavior method
4. At least one simple validation rule if it fits the domain
5. A separate service function that uses the class
```

Provide a starter shape without solving every domain:

```python
class InventoryItem:
    def __init__(self, name: str, quantity: int, reorder_level: int) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if reorder_level < 0:
            raise ValueError("Reorder level cannot be negative.")

        self.name = name.strip()
        self.quantity = quantity
        self.reorder_level = reorder_level

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self.quantity += amount

    def needs_reorder(self) -> bool:
        return self.quantity <= self.reorder_level
```

"If you use this starter, write your own small service function. A demo block may call the service function, but it does not replace it. Do not put `print()` inside `restock()` or `needs_reorder()`."

### Step 4: Add a Small Service Function

**Instructor talk track**

"After one class works, write a small function outside the class that uses it. This helps you practice boundaries."

Example:

```python
def restock_if_needed(item: InventoryItem, amount: int) -> bool:
    if item.needs_reorder():
        item.restock(amount)
        return True

    return False
```

"This function coordinates a use case. It asks the item whether it needs reorder. If yes, it calls the item's behavior. It returns a boolean instead of printing. That means another caller can decide what to do with the result."

### Instructor Circulation Checklist

As learners work, circulate with these questions:

- "What is the central object in your tracker?"
- "What does this object know?"
- "What does this object do?"
- "What does this object not do?"
- "Where would user input happen?"
- "Could you create this object in a test without typing at the terminal?"
- "Is this method small enough that you can explain it in one sentence?"
- "Are you using inheritance because you need it, or because it feels advanced?"

Use these correction prompts:

- If a learner puts `input()` in a class: "Let's move the input outside. The class should receive values; it should not ask for them."
- If a learner puts `print()` in every method: "Let's return a value or update state here. Printing can happen in a demo block."
- If a learner creates too many classes: "Which one class do you need to implement today? Mark the others as future design notes."
- If a learner creates one giant class: "Can we separate the item being tracked from the collection that holds many items?"
- If a learner writes a method longer than the whole class sketch: "What is the one job of this method? Can part of it become a helper or service function?"

---

## Troubleshooting During the Lab

Use this section when learners hit predictable issues.

### Issue: "My class works, but nothing prints."

Response:

"That may be correct. The model class should not necessarily print. Add a small demo block outside the class if you want to display the result."

Example:

```python
item = InventoryItem("Notebook", 3, 5)
was_restocked = restock_if_needed(item, 10)
print(f"Restocked: {was_restocked}")
print(f"Current quantity: {item.quantity}")
```

### Issue: "I do not know whether this should be a class or a function."

Response:

"Ask whether you have related data and behavior that belong together. If yes, a class may help. If you are simply coordinating existing objects, a function may be clearer."

Use this quick rule:

```text
Class: owns state plus behavior.
Function: performs an action or coordinates objects.
```

### Issue: "I want to use inheritance."

Response:

"Inheritance is useful later, but today we prefer simple composition. First design one clear object and one clear collection. If you cannot explain why a subclass is necessary, do not add it yet."

### Issue: "Where should validation go?"

Response:

"Validation that protects the truth of the object belongs in the model. For example, an expense amount should not be negative, so the `Expense` class should reject negative amounts. Formatting an error message for the user belongs in the UI. Coordinating a multi-object rule may belong in a service function."

### Issue: "Should my service function print?"

Response:

"For today's design, prefer returning data. A service function can return `True`, `False`, a number, a list, or a string. The demo block can print that result."

---

## Completion Criteria

By the end of the lab, each learner should have:

1. A selected tracker domain.
2. A short requirements list with 5 to 8 bullets.
3. A sketch of 3 to 5 classes.
4. For each sketched class, notes for what it knows and what it does.
5. At least one implemented class with `__init__` and one behavior method.
6. No `input()` calls inside the model class.
7. No required `print()` calls inside the model class behavior.
8. A separate service function that uses the class. A demo block may call it, but it does not replace it.
9. A successful run of the Python file with deterministic output.

If learners finish only the sketch and one working class, that is enough for this hour. Do not push them into persistence, databases, APIs, or GUI work yet. Those topics have their own course moments.

---

## Common Pitfalls to Watch For

### Pitfall 1: Putting I/O Inside Domain Objects

The most important correction for this hour is keeping I/O out of domain models.

Avoid:

```python
class Expense:
    def __init__(self) -> None:
        self.amount = float(input("Amount: "))
```

Prefer:

```python
class Expense:
    def __init__(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.amount = amount
```

The UI can collect the amount. The model can validate it.

### Pitfall 2: Overcomplicated Inheritance Early

Learners may want `WorkTask`, `HomeTask`, `UrgentTask`, `OptionalTask`, and `RecurringTask` immediately. Encourage them to start with attributes before subclasses.

Say:

"Before creating five subclasses, ask whether one `Task` class with a priority, category, or recurrence field would be clearer for now."

### Pitfall 3: One Giant Manager Class

If a class knows everything and does everything, it becomes hard to test.

Say:

"Let's separate the object being tracked from the collection that holds many objects. An `Expense` is one record. An `ExpenseTracker` or `ExpenseBook` can hold many records."

### Pitfall 4: Methods That Do Not Belong to the Object

If an object does not have the information needed for a behavior, the behavior may belong elsewhere.

Example:

"A single `Task` should not calculate the completion rate for the whole project because it does not know all project tasks. The `Project` or a report function can do that."

### Pitfall 5: Misleading State Labels

Be precise with state names. If a task has `is_complete = False`, call it pending. Do not label it "done" in one place and "open" in another unless those words are intentionally defined. Inconsistent state language creates bugs and confusion.

---

## Optional Extensions for Fast Finishers

Offer these only after the required completion criteria are met:

1. Add type hints to method parameters and return values.
2. Add a `__str__` method for friendly display.
3. Add one more validation rule that protects the model.
4. Add a small collection class, such as `Inventory`, `Project`, `AddressBook`, or `ExpenseTracker`.
5. Add a service function that returns a list of matching objects.
6. Add a tiny set of `assert` statements in the same file to check expected behavior.

Example optional assertions:

```python
item = InventoryItem("Pen", 2, 5)
assert item.needs_reorder() is True
item.restock(10)
assert item.quantity == 12
assert item.needs_reorder() is False
```

Make clear:

"Assertions are not the full testing lesson yet. They are a lightweight way to check our thinking. We will do more formal testing later."

---

## Debrief (3 minutes)

**Instructor talk track**

"Let's hear two examples. Tell us your tracker domain, one class you sketched, and one responsibility that class owns."

After each share, ask one boundary question:

- "Does that class collect user input, or does it receive data?"
- "Does that method change object state, return a value, or display output?"
- "What is one thing you intentionally kept out of that class?"

Use the debrief to reinforce:

"The design skill is not just naming classes. The design skill is assigning responsibility. When responsibility is clear, the code becomes easier to test and easier to change."

---

## Quick Checks and Exit Ticket (2 minutes)

Ask learners to answer verbally, in chat, or on a note card:

1. "In responsibility-driven design, what two questions do we ask about an object?"
   - Expected answer: "What does it know? What does it do?"

2. "Where should `input()` usually live: inside a domain model, or outside it?"
   - Expected answer: "Outside it, in UI or application code."

3. "Where should validation live: UI layer, service layer, or model?"
   - Expected answer: "Business-rule validation should live in the model when it protects one object's valid state, or in a service layer when it coordinates multiple objects. The UI can display validation messages, but it should not be the only place that enforces core business rules."

4. "Why might a service function return `True` or `False` instead of printing?"
   - Expected answer: "Returning data keeps it testable and lets different callers decide how to display or use the result."

---

## Wrap-Up and Bridge to Hour 3

**Instructor talk track**

"Today we practiced a design habit that will show up throughout the Advanced course. We started with requirements, identified candidate classes, described what each object knows and does, and kept user interaction separate from the model."

"That separation is not academic. It is what lets us test core logic without clicking through screens or typing into prompts. It is what lets a terminal program become a web program later. It is what lets a small capstone grow without turning into one large script."

"In the next hour, we will tighten the model further. We will look at properties, invariants, and custom exceptions. In plain language, that means we will learn how objects protect themselves from invalid state after they have already been created. Today we checked values in `__init__` and methods. Next, we will make those rules more robust and expressive."

"Before we move on, make sure your file runs, your design notes are saved, and your current work is in a safe place. If you are using Git after this session, this is a good moment for a small checkpoint commit with a message such as `Add Day 1 Hour 2 domain model sketch`."

Final reminder:

"Advanced Python is not about making code look complicated. It is about making code easier to reason about. Clear responsibilities are the first step."
