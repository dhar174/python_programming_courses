# Day 2, Hour 2: Pattern: Strategy (Swap Behaviors Cleanly)

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 2, Hour 2 of 48, also Hour 6 in the Advanced runbook sequence
- **Focus**: Using the Strategy Pattern to select an algorithm at runtime without rewriting the core workflow.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 2, Hour 6.
- **Prerequisites**: Learners should be comfortable writing functions, passing functions as arguments, reading dictionaries and lists of dictionaries, using `sorted()`, writing simple validation functions, and understanding the Day 2 Hour 1 Factory idea.
- **Advanced trajectory**: This hour continues the PCAP-to-PCPP1 design path. Learners already know how to write control flow. The advanced step is deciding where behavior choices belong so a program stays open to new behavior without repeated edits to the same central code.
- **Instructor goal**: By the end of this hour, every learner has implemented two small strategies, selected one through a menu-like choice, passed the selected strategy into reusable core code, and verified that behavior changes while the core workflow remains stable.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Day 2 Hour 1 Factory | 5 min | Connect centralized creation choices to centralized behavior choices |
| Outcomes, setup, and vocabulary | 5 min | Define strategy, callable, algorithm, core workflow, and runtime selection |
| Concept briefing: why Strategy | 10 min | Explain selecting algorithms at runtime and why Python strategies can be lightweight functions |
| Live demos: sort keys, validation strategies, and callable class | 10 min | Show required demos with deterministic runnable examples |
| Guided lab: menu-selected strategies | 25 min | Learners implement two strategies and wire a menu option to choose behavior |
| Quick checks, completion criteria, and wrap-up | 5 min | Verify understanding, name pitfalls, and bridge to Pythonic class ergonomics |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If the concept discussion runs long, shorten instructor narration before the live demo rather than shrinking the lab. The required outcome is practical: strategy changes behavior without rewriting the core code, and results are clearly different and correct.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Define the Strategy Pattern as selecting an algorithm at runtime.
2. Explain that a Python strategy can be a function, lambda, method, or callable object, as long as it follows the expected input and output shape.
3. Use a sort-key strategy selected from user input to change record ordering without rewriting the display function.
4. Use validation strategies for different record types so one validation workflow can check tasks, contacts, or other records.
5. Implement a short class-based strategy, such as a callable class with constructor state.
6. Avoid duplicated sorting and filtering branches by extracting behavior into small named strategies.
7. Store strategies in a dictionary for explicit lookup and learner-safe unknown-choice errors.
8. Recognize when hard-coded branching still dominates and the code has not really benefited from Strategy.
9. Identify why strategies should not depend on hidden global variables.
10. Answer the quick check: how is a strategy different from an `if`/`elif` chain?

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 2, Hour 6 visible. The required scope is Strategy Pattern, swapping behaviors cleanly, strategies as callables or classes, sorting and filtering logic, sort-key selection by user choice, validation strategies for different record types, a lab with menu-selected behavior, pitfalls, and the quick check about Strategy versus `if`/`elif`.
- Open the Day 2 Hour 1 Factory lecture if you want the teaching style nearby. Use it as a bridge only. Hour 1 centralized object creation. This hour centralizes behavior choice.
- Prepare a clean file for the live demo, such as `day2_hour2_strategy_demo.py`, or use a notebook cell. The snippets below are self-contained and deterministic.
- Confirm that the room can run `python day2_hour2_strategy_demo.py` or `python3 day2_hour2_strategy_demo.py`.
- Prepare this board note before class:

```text
Factory centralizes: "How do we create a valid object?"
Strategy centralizes: "Which behavior should this workflow use?"

Strategy = algorithm selected at runtime.
In Python, a strategy can be a function or any callable object.
Core workflow receives the strategy and uses it.
```

- Have a simple capstone connection ready. Examples: task tracker sort by name versus created date, inventory filter active versus all, contact validation versus task validation, report output ordered by priority versus owner.
- Be ready to correct two mistakes early. First, learners may keep a giant `if`/`elif` chain inside the core workflow and only move the branch names around. Second, learners may create strategies that secretly read global variables instead of receiving everything they need as arguments.

Suggested board note for the lab:

```text
Lab success:
1. Two strategies exist as separate functions or callable classes.
2. A menu choice selects the strategy.
3. Core code receives the strategy.
4. Changing the selected strategy changes the result.
5. Unknown choices raise or report a clear error.
```

---

## Opening Bridge from Day 2 Hour 1 Factory (5 minutes)

**Instructor talk track**

"Welcome back. In the previous hour we worked with the Factory Pattern. The factory gave us a place to centralize object creation. We said: raw data comes in, the factory validates and normalizes it, and either a valid object comes out or a clear validation error is raised. That was a responsibility decision. We did not want object creation rules scattered across every feature."

"This hour uses a very similar design instinct, but the focus shifts from object creation to behavior choice. A factory asks, 'How do we build this object correctly?' A strategy asks, 'Which behavior should this workflow use right now?'"

"Here is the bridge sentence for today: **Factory centralizes object creation; Strategy centralizes behavior choice.**"

Write or display:

```text
Factory: choose how to create the object.
Strategy: choose how the object or workflow behaves.
```

"Imagine a tracker application. In one screen, users want records sorted by name. In another screen, they want records sorted by created date. Later, a stakeholder asks for sort by priority. A beginner implementation might put an `if`/`elif` chain in every display function. If the user selected `name`, sort one way. If the user selected `created_date`, sort another way. If the user selected `priority`, sort another way."

"That works once. But then the same sorting idea appears in the command-line view, the GUI list, the API response, and the report export. Now we have four places to update when the sorting rule changes. The duplication is not only annoying. It is a bug risk. One place sorts names case-sensitively, another place sorts case-insensitively, and now the app behaves inconsistently."

"The Strategy Pattern helps us pull the changing part out of the workflow. The core workflow says, 'I know how to display records once someone gives me a strategy.' The strategy says, 'I know how to choose the sort key,' or 'I know how to validate this kind of record,' or 'I know how to filter this list.'"

Pause and ask:

"Where have you already written code that chooses between two behaviors? Sorting? Filtering? Validation? Formatting? Calculating a fee?"

Take two or three answers. Connect them back:

"Those are all candidates. The pattern is not about making everything abstract. It is about noticing when the behavior varies and giving that variation a clean name."

**Transition**

"Let's define the vocabulary, then we will build three small demos: sort-key selection, validation strategies for different record types, and a short class-based strategy so we can see that strategies can be functions or classes."

---

## Outcomes, Setup, and Vocabulary (5 minutes)

Use this section to keep the pattern practical. Learners do not need a formal design-pattern diagram. They need a mental model they can apply in their capstone code.

**Instructor talk track**

"By the end of this hour, you should be able to say, 'This workflow is stable, but this behavior changes. I will pass in the behavior as a strategy.' That sentence is the practical value of the pattern."

"First term: **strategy**. A strategy is a replaceable algorithm. In this course, algorithm simply means a repeatable way to solve a small problem. Sorting by name is an algorithm. Sorting by created date is another algorithm. Validating a task record is an algorithm. Validating a contact record is another algorithm."

"Second term: **runtime selection**. Runtime means while the program is running. The strategy may be selected from a user menu, a configuration value, a button click, a command-line argument, or a route parameter. The important part is that the main workflow does not need to be rewritten every time the selected algorithm changes."

"Third term: **callable**. In Python, a callable is something you can call with parentheses. A normal function is callable. A lambda is callable. A method is callable. An object can also be callable if its class defines `__call__`. That is why Strategy can stay lightweight in Python. We do not need a large interface hierarchy for today's scope. A function is enough when it has the right shape."

"Fourth term: **core workflow**. The core workflow is the stable part of the code. For sorting, the core workflow might be: receive records, sort them using the selected key function, print the result. For validation, the core workflow might be: receive records, call the selected validator, collect errors, print pass or fail."

"Fifth term: **strategy registry**. This is often just a dictionary that maps user choices to strategies. For example, `'1'` maps to `sort_by_name`, and `'2'` maps to `sort_by_created_date`. The dictionary is not magic. It is an explicit lookup table. It helps us avoid scattering hard-coded branches throughout the program."

Point learners to the working pattern:

```text
choice -> strategy lookup -> core workflow receives strategy -> result changes
```

"Notice the direction. The core workflow should not secretly decide everything. It should receive the selected strategy. That is what makes the behavior easy to swap."

---

## Concept Briefing: Why Strategy (10 minutes)

**Instructor talk track**

"Let's start with the problem Strategy solves. Suppose we have a list of records. Each record has a name, created date, active flag, and record type. We need to display those records in different orders. The first version many of us would write looks like this:"

```python
def display_records(records, sort_choice):
    if sort_choice == "name":
        ordered = sorted(records, key=lambda record: record["name"].lower())
    elif sort_choice == "created":
        ordered = sorted(records, key=lambda record: record["created_date"])
    elif sort_choice == "priority":
        ordered = sorted(records, key=lambda record: record["priority"])
    else:
        raise ValueError(f"Unknown sort choice: {sort_choice}")

    for record in ordered:
        print(record)
```

"This code is not evil. It is understandable. In fact, a small `if` statement is often perfectly fine. Strategy becomes useful when the choices grow, when the same choices are repeated in more than one place, or when the core workflow becomes hard to read because the branching dominates the business logic."

"Look at the function name: `display_records`. What should this function mostly be about? Displaying records. But the first half of it is becoming a sorting-choice dispatcher. If every new sort rule requires editing this function, then the function is not closed against change. Again, we are not chasing theory for its own sake. We are trying to reduce repeated edits and inconsistent behavior."

"The Strategy version separates the stable workflow from the variable behavior. We write small functions such as `sort_by_name(record)` and `sort_by_created_date(record)`. Those functions become our strategies. Then the display workflow accepts a strategy function. It does not care which sort key was selected. It simply calls `sorted(records, key=sort_key_strategy)`."

Write:

```text
Variable part:
    How do we compute the sort key?

Stable part:
    Sort records, then display them.
```

"That separation is the heart of Strategy."

"Python makes this especially natural because functions are first-class values. That means we can store a function in a variable, pass a function as an argument, return a function from another function, and store functions in dictionaries. We have already used this idea indirectly with `key=` in `sorted()`. The `key` parameter is a strategy slot. It asks, 'What function should I call to decide each item's sort value?'"

"The same idea applies to filtering. A filter strategy can be a function that receives a record and returns `True` or `False`. `is_active(record)` is one strategy. `include_all(record)` is another strategy. The display workflow can say: keep records where `filter_strategy(record)` is true. The workflow does not need to know whether the selected rule means active only, overdue only, high priority only, or all records."

"Validation is another useful example. In Day 2 Hour 1, the factory validated raw data before creating an object. In a real app, different record types may have different rules. A task might require `title` and `status`. A contact might require `name` and a valid email. An inventory item might require `sku` and a non-negative quantity. We can write one validation runner that receives a validator strategy. The validator is the changing part."

"Now, an important caution: Strategy does not mean 'no `if` statements anywhere.' We still need a boundary where a user choice is interpreted. A menu selection must become a strategy somehow. A dictionary lookup is a clean boundary. What we are avoiding is hard-coded branching dominating the core workflow. The selection can happen once near the edge of the program. After that, the selected strategy is passed into reusable code."

"Another caution: we want explicit unknown-choice handling. You may see code that silently falls back to a default strategy when a choice is unknown. That can be convenient in a user interface, but it can also hide mistakes. For teaching and for many data workflows, prefer a clear error: `Unknown strategy choice: x`. If you intentionally choose a default, say so in the code and in the user message. Today we will teach the safer explicit error path."

"Finally, strategies should not depend on hidden global variables. If `sort_by_name()` secretly reads a global setting called `CASE_SENSITIVE`, the strategy becomes harder to reason about and test. Give strategies the data they need through parameters or constructor state. Later in the demo, we will use a callable class with constructor state for a prefix rule. That is a clean way to carry configuration without relying on globals."

**Transition**

"Let's code. I will start with sorting because Python's `sorted(..., key=...)` already uses a strategy-shaped parameter. Then we will do validation strategies, and then a tiny callable class."

---

## Live Demos: Sort Keys, Validation Strategies, and Callable Class (10 minutes)

The live demo should be typed or revealed in small chunks. Keep it deterministic. Do not use `input()` during the main demo unless your group is comfortable with interactive runs. The snippets simulate choices with variables so the output is repeatable.

### Demo Step 1: Sort-key selection strategy based on user selection

**Instructor talk track**

"First we need some sample records. They are deliberately small dictionaries. In a larger project, these might be objects, but dictionaries keep the pattern visible."

```python
from typing import Callable

Record = dict[str, object]
SortKey = Callable[[Record], object]

records: list[Record] = [
    {
        "name": "Charlie",
        "created_date": "2026-01-02",
        "priority": 2,
        "active": True,
        "type": "task",
        "title": "Write tests",
        "status": "pending",
    },
    {
        "name": "Alice",
        "created_date": "2026-01-10",
        "priority": 1,
        "active": False,
        "type": "task",
        "title": "Archive notes",
        "status": "done",
    },
    {
        "name": "Bob",
        "created_date": "2026-01-08",
        "priority": 3,
        "active": True,
        "type": "contact",
        "email": "bob@example.com",
    },
]


def sort_by_name(record: Record) -> str:
    return str(record["name"]).lower()


def sort_by_created_date(record: Record) -> str:
    return str(record["created_date"])


def sort_by_priority(record: Record) -> int:
    return int(record.get("priority", 999))


SORT_STRATEGIES: dict[str, SortKey] = {
    "1": sort_by_name,
    "2": sort_by_created_date,
    "3": sort_by_priority,
}

SORT_LABELS: dict[str, str] = {
    "1": "name",
    "2": "created date",
    "3": "priority",
}


def choose_sort_strategy(choice: str) -> SortKey:
    try:
        return SORT_STRATEGIES[choice]
    except KeyError as error:
        valid_choices = ", ".join(sorted(SORT_STRATEGIES))
        raise ValueError(
            f"Unknown sort choice {choice!r}. Choose one of: {valid_choices}."
        ) from error


def display_records(records: list[Record], sort_key: SortKey, label: str) -> None:
    print(f"\nSorted by {label}:")
    for record in sorted(records, key=sort_key):
        print(f"- {record['name']} | {record['created_date']} | priority {record.get('priority', '-')}")


for choice in ["1", "2", "3"]:
    strategy = choose_sort_strategy(choice)
    display_records(records, strategy, SORT_LABELS[choice])
```

**Narration after running**

"We ran the same `display_records()` function three times. The function did not change. What changed was the strategy passed into it. When the strategy is `sort_by_name`, Alice appears first. When the strategy is `sort_by_created_date`, the oldest created date appears first. When the strategy is `sort_by_priority`, the lowest priority number appears first."

"Notice the explicit error in `choose_sort_strategy()`. We did not silently default to name. If the user enters an unknown option, the program says which choices are valid. That is safer for learners and safer for debugging."

Ask:

"Where is the behavior selected? Where is the behavior used?"

Guide toward:

- Selected in `choose_sort_strategy()`.
- Used in `display_records()` through `sorted(records, key=sort_key)`.

### Demo Step 2: Validation strategies for different record types

**Instructor talk track**

"Now let's use the same idea for validation. A task record and a contact record have different required fields. I do not want to write three separate validation runners. I want one runner that receives a validation strategy."

```python
Validator = Callable[[Record], list[str]]


def validate_task(record: Record) -> list[str]:
    errors: list[str] = []
    if not str(record.get("title", "")).strip():
        errors.append("task requires a non-empty title")
    if record.get("status") not in {"pending", "doing", "done"}:
        errors.append("task status must be pending, doing, or done")
    return errors


def validate_contact(record: Record) -> list[str]:
    errors: list[str] = []
    if not str(record.get("name", "")).strip():
        errors.append("contact requires a non-empty name")
    email = str(record.get("email", "")).strip()
    if "@" not in email:
        errors.append("contact requires an email containing @")
    return errors


VALIDATION_STRATEGIES: dict[str, Validator] = {
    "task": validate_task,
    "contact": validate_contact,
}


def choose_validator(record_type: str) -> Validator:
    try:
        return VALIDATION_STRATEGIES[record_type]
    except KeyError as error:
        valid_types = ", ".join(sorted(VALIDATION_STRATEGIES))
        raise ValueError(
            f"Unknown record type {record_type!r}. Choose one of: {valid_types}."
        ) from error


def report_validation(record: Record, validator: Validator) -> None:
    errors = validator(record)
    if errors:
        print(f"\n{record.get('name', '<unnamed>')} failed validation:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"\n{record.get('name', '<unnamed>')} passed validation.")


for record in records:
    record_type = str(record["type"])
    validator = choose_validator(record_type)
    report_validation(record, validator)
```

**Narration after running**

"Again, the runner is stable. `report_validation()` does not know the difference between task rules and contact rules. It only knows that it can call the validator and receive a list of error messages. That expected shape is the contract."

"This is a good moment to use the word contract. A strategy contract answers: what inputs does the strategy receive, and what output does it return? For our validators, the contract is: receive one record dictionary and return a list of strings. Empty list means valid. One or more strings means invalid."

### Demo Step 3: Short class-based strategy with constructor state

**Instructor talk track**

"Functions are the simplest Python strategies, and we should prefer them when they are enough. Sometimes a strategy needs a little configuration. We could use a closure or a class. Here is a short callable class. It carries constructor state without relying on global variables."

```python
class NamePrefixFilter:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix.lower()

    def __call__(self, record: Record) -> bool:
        return str(record["name"]).lower().startswith(self.prefix)


def include_all(record: Record) -> bool:
    return True


def filter_records(records: list[Record], keep: Callable[[Record], bool]) -> list[Record]:
    return [record for record in records if keep(record)]


starts_with_a = NamePrefixFilter("A")
print("\nAll records:")
for record in filter_records(records, include_all):
    print(f"- {record['name']}")

print("\nNames starting with A:")
for record in filter_records(records, starts_with_a):
    print(f"- {record['name']}")
```

**Narration after running**

"The object `starts_with_a` is callable because the class defines `__call__`. The strategy has state: the prefix. It does not read a global variable. It receives the record and uses its own configured prefix. This supports today's outcome that strategies can be callables or classes."

"We do not need abstract base classes for this hour. Later, in larger codebases, teams may add protocols or abstract base classes to document strategy shape. For today, keep it lightweight: functions work, and callable classes work when you need state."

**Transition**

"Now it is your turn. The lab will use the same pattern: create two strategies, select one from a menu, pass it into stable core code, and show that the results are different and correct."

---

## Guided Lab: Menu-Selected Strategies (25 minutes)

### Lab prompt for students

"In your tracker-style project, or in a new practice file if your project is not ready, implement Strategy selection for sorting or filtering records. Your goal is not to build a large menu system. Your goal is to prove that the selected strategy changes behavior without rewriting the core display code."

Learners may choose one of these paths:

1. **Sorting path**: implement `sort_by_name` and `sort_by_created_date`.
2. **Filtering path**: implement `filter_active` and `filter_all`.
3. **Combined path for fast finishers**: choose both one sort strategy and one filter strategy.

### Starter code

Offer this starter if learners need a common base:

```python
from typing import Callable

Record = dict[str, object]
SortKey = Callable[[Record], object]
RecordFilter = Callable[[Record], bool]

records: list[Record] = [
    {"name": "Inventory cleanup", "created_date": "2026-01-01", "active": True},
    {"name": "Budget review", "created_date": "2026-01-12", "active": False},
    {"name": "Client follow-up", "created_date": "2026-01-09", "active": True},
]


def sort_by_name(record: Record) -> str:
    return str(record["name"]).lower()


def sort_by_created_date(record: Record) -> str:
    return str(record["created_date"])


def filter_all(record: Record) -> bool:
    return True


def filter_active(record: Record) -> bool:
    return bool(record["active"])


SORT_STRATEGIES: dict[str, SortKey] = {
    "1": sort_by_name,
    "2": sort_by_created_date,
}

FILTER_STRATEGIES: dict[str, RecordFilter] = {
    "1": filter_all,
    "2": filter_active,
}


def choose_strategy(choice: str, strategies: dict[str, Callable]) -> Callable:
    try:
        return strategies[choice]
    except KeyError as error:
        valid_choices = ", ".join(sorted(strategies))
        raise ValueError(
            f"Unknown strategy choice {choice!r}. Choose one of: {valid_choices}."
        ) from error


def display_records(
    records: list[Record],
    sort_key: SortKey,
    keep_record: RecordFilter,
) -> None:
    visible_records = [record for record in records if keep_record(record)]
    ordered_records = sorted(visible_records, key=sort_key)

    for record in ordered_records:
        active_label = "active" if record["active"] else "inactive"
        print(f"- {record['name']} | {record['created_date']} | {active_label}")


sort_choice = "1"      # Replace with input("Sort by 1=name, 2=created date: ")
filter_choice = "2"    # Replace with input("Show 1=all, 2=active only: ")

selected_sort = choose_strategy(sort_choice, SORT_STRATEGIES)
selected_filter = choose_strategy(filter_choice, FILTER_STRATEGIES)
display_records(records, selected_sort, selected_filter)
```

### Required lab tasks

Students should complete these steps:

1. Create or reuse a list of at least three records. Each record should have fields that make the two strategies visibly different. For sorting, names and created dates should not already be in the same order. For filtering, at least one record should be inactive.
2. Implement two strategies. Examples:
   - `sort_by_name(record) -> str`
   - `sort_by_created_date(record) -> str`
   - `filter_active(record) -> bool`
   - `filter_all(record) -> bool`
3. Store strategies in a dictionary for lookup, such as `{"1": sort_by_name, "2": sort_by_created_date}`.
4. Wire a menu option or simulated choice to choose a strategy.
5. Pass the selected strategy into a stable display or processing function.
6. Run the program twice with different choices and confirm that the results are clearly different and correct.
7. Handle unknown choices explicitly. A clear `ValueError` or a clear user-facing message is acceptable. Silent fallback is not the preferred teaching path today unless the learner explains the tradeoff.

### Instructor circulation script

At minute 1 of lab:

"Start by choosing sorting or filtering. Do not try to redesign your whole capstone. We need two strategies and one stable workflow."

At minute 5:

"Check your data. If both strategies produce the same output, the code may be correct but the demo will not prove the pattern. Adjust sample data so the difference is visible."

At minute 10:

"Find your core workflow. It might be called `display_records`, `list_tasks`, or `show_inventory`. Ask: does this function receive a strategy, or is it still deciding everything inside a long branch?"

At minute 15:

"Run one choice. Then run the other choice. You should not need to edit the body of the core workflow. You should only change the selected strategy or the menu input."

At minute 20:

"Add explicit unknown-choice handling. If the user enters `9`, what happens? A clear error is better than a surprising default."

At minute 23:

"Prepare to show your result to a neighbor. Explain which part is the strategy and which part is the stable workflow."

### Completion criteria

Use these checks before calling the lab complete:

- Strategy changes behavior without rewriting core code.
- Results are clearly different and correct.
- At least two strategies exist as separate functions or callable objects.
- A menu option, simulated choice, or dictionary lookup selects the strategy.
- The core display or processing function receives and uses the selected strategy.
- Unknown choices are handled explicitly.

### Optional extension

For fast finishers:

- Add a third strategy and store or register strategies in a dictionary for lookup.
- Combine one filter strategy with one sort strategy.
- Convert one function strategy into a callable class with constructor state, such as `CreatedAfterFilter("2026-01-07")` or `NamePrefixFilter("B")`.

Keep the extension small. Do not turn this into a plugin system, decorator exercise, dependency injection framework, or abstract base class lesson. Those are future growth topics, not the goal of this hour.

---

## Troubleshooting and Common Pitfalls

Use this section during lab support and the final debrief.

### Pitfall 1: Strategies that depend on global variables

**Symptom**

A learner writes a strategy that works only because it reads a global variable:

```python
selected_prefix = "A"


def filter_by_prefix(record):
    return record["name"].startswith(selected_prefix)
```

**Instructor response**

"This works in a tiny script, but the strategy has a hidden dependency. If another part of the program changes `selected_prefix`, the strategy changes without anyone passing it new information. That makes tests harder and bugs more surprising."

Prefer passing data through parameters or constructor state:

```python
class PrefixFilter:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix.lower()

    def __call__(self, record: dict[str, object]) -> bool:
        return str(record["name"]).lower().startswith(self.prefix)
```

### Pitfall 2: Hard-coded branching still dominates

**Symptom**

A learner creates strategy functions but still writes the full behavior branch inside the core workflow:

```python
def display_records(records, choice):
    if choice == "1":
        ordered = sorted(records, key=sort_by_name)
    elif choice == "2":
        ordered = sorted(records, key=sort_by_created_date)
    else:
        ordered = records
    for record in ordered:
        print(record)
```

**Instructor response**

"You have named the strategies, which is a good first step. Now move the selection to the edge of the program. Let `display_records()` receive the selected strategy. That way the display function is stable."

```python
def display_records(records, sort_key):
    for record in sorted(records, key=sort_key):
        print(record)
```

### Pitfall 3: Accidentally calling the function during registration

**Symptom**

The dictionary stores the result of calling a function instead of the function itself:

```python
SORT_STRATEGIES = {
    "1": sort_by_name(),  # incorrect
}
```

**Instructor response**

"In the strategy dictionary, store the callable itself. Do not add parentheses until the core workflow calls it with a record."

```python
SORT_STRATEGIES = {
    "1": sort_by_name,  # correct
}
```

### Pitfall 4: Silent invalid strategy fallback

**Symptom**

The program defaults to a strategy when the user typed something invalid:

```python
strategy = SORT_STRATEGIES.get(choice, sort_by_name)
```

**Instructor response**

"A default can be a reasonable product decision, but it should be intentional and visible. Today we prefer learner-safe explicit errors because they reveal mistakes. If you choose to default, print or return a message that tells the user what happened."

Preferred teaching version:

```python
if choice not in SORT_STRATEGIES:
    raise ValueError(f"Unknown sort choice: {choice}")
strategy = SORT_STRATEGIES[choice]
```

### Pitfall 5: Strategies with different shapes

**Symptom**

One strategy expects a record, another expects a list, and the core workflow cannot call them consistently.

**Instructor response**

"Strategies in the same registry need the same shape. For sort keys, each strategy receives one record and returns a sortable value. For filters, each strategy receives one record and returns `True` or `False`. For validators, each strategy receives one record and returns a list of error messages."

---

## Quick Checks, Completion Criteria, and Wrap-up (5 minutes)

### Quick check questions

Ask these verbally or use them as an exit ticket:

1. "What is the Strategy Pattern?"
   - Expected answer: "Selecting an algorithm at runtime," or "Passing in the behavior the workflow should use."
2. "In Python, does a strategy have to be a class?"
   - Expected answer: "No. It can be a function or any callable. A class is useful when the strategy needs state."
3. "How is a strategy different from an `if`/`elif` chain?"
   - Expected answer: "An `if`/`elif` chain keeps the behavior choices embedded in one branching block. Strategy extracts each behavior into a named callable and lets the core workflow receive the selected behavior. Selection may still happen once at the edge, but the workflow is no longer dominated by hard-coded branches."
4. "Why should strategies avoid hidden global variables?"
   - Expected answer: "Hidden globals make the strategy harder to test and reason about because behavior can change without passing new input."
5. "What should happen for an unknown strategy choice?"
   - Expected answer: "Raise or report a clear error, unless the program intentionally teaches and documents a default fallback."

### Debrief prompts

Ask two learners to show or describe:

- The two strategies they implemented.
- The menu choice or dictionary lookup that selected the strategy.
- The core function that stayed the same while behavior changed.

As they answer, reinforce the pattern:

"That is the important part: the workflow did not need to know every detail. It accepted a callable and used it."

### Wrap-up talk track

"Today we took another step toward professional Python design. We did not learn Strategy as a memorized diagram. We learned it as a practical move: when one workflow needs interchangeable behavior, extract each behavior into a strategy and pass the selected strategy into the workflow."

"The required phrase from the runbook is: Strategy means selecting an algorithm at runtime. In Python, that can stay lightweight. Functions work. Callable classes work when you need state. A dictionary is often enough to map user choices to strategies."

"The two big warnings are worth repeating. First, do not let hard-coded branching continue to dominate the core function. If the workflow still contains every branch, the strategy extraction is incomplete. Second, do not make strategies depend on hidden global variables. A strategy should be easy to call, test, and reason about."

"You also practiced explicit unknown-choice handling. Silent fallback can hide mistakes. In user-facing software, a default might be appropriate if the product intentionally wants it, but the program should make that choice visible. For today's design habit, clear errors are safer."

"In the next hour, we move from behavior selection to Pythonic class ergonomics. We will make our objects easier to inspect, print, compare, and type-read. That means `repr`, `str`, equality, and light type hints. Strategy helped us make behavior swappable. Next, Pythonic class methods will help our objects communicate clearly to developers, users, tests, and tools."

---

## Instructor Notes for Adaptation

- If learners are newer to first-class functions, slow down at the point where a function is stored in a dictionary. Ask them to predict whether `sort_by_name` or `sort_by_name()` belongs in the registry.
- If learners are comfortable, ask them to identify strategy-shaped parameters they already know. Good examples include `sorted(..., key=...)`, `list.sort(key=...)`, and callbacks in GUI programming.
- Keep examples within scope. Do not introduce plugin discovery, decorators, dependency injection containers, or abstract base classes as part of the main lesson. A brief future-growth mention is fine, but the lab must remain about functions, callable classes, dictionaries, and clean behavior selection.
- For capstone alignment, encourage learners to apply Strategy where a user chooses a view: active tasks versus all tasks, sort by owner versus due date, validate task versus contact, report by priority versus created date.
- If time is short, keep only two live demo runs for sorting and one validation run, then move to lab. The lab is the higher-value part of the hour.
- If time remains after lab, ask learners to refactor one existing `if`/`elif` chain in their capstone into a small strategy dictionary.
