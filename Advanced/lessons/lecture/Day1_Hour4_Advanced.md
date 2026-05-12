# Day 1, Hour 4: Composition vs Inheritance and Polymorphism

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 1, Hour 4 of 48
- **Focus**: Choosing composition or inheritance appropriately, using polymorphism to simplify branching, and recognizing when shared behavior does not require a shared parent class.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 1, Hour 4.
- **Prerequisites**: Learners should be able to define classes, create instances, call methods, pass objects into functions or constructors, use `if`/`elif` branching, and read simple tracebacks.
- **Advanced trajectory**: This hour moves learners from PCAP-level object syntax toward PCPP1-style design judgment. The goal is not "use more classes." The goal is to make code easier to change by choosing the smallest useful structure: inheritance for true **is-a** relationships, composition for **has-a** relationships, and polymorphism for calling different objects through the same expected behavior.
- **Instructor goal**: By the end of this hour, every learner has refactored a branching feature into at least two classes that share the same method name, used a composed object that stores one of those formatter or processor objects, and explained why the design uses composition and duck-typed polymorphism instead of unnecessary inheritance.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from Hour 3 | 5 min | Connect protected object state to object collaboration |
| Outcomes and vocabulary | 5 min | Define inheritance, composition, polymorphism, interface, and duck typing |
| Concept briefing: choosing the relationship | 10 min | Teach **is-a** vs **has-a** and how polymorphism removes branching |
| Live demo: refactor report export branching | 10 min | Show before-state `if`/`elif`, two shared-method classes, and a composed runner |
| Guided lab: refactor a branching feature | 25 min | Learners refactor into two classes with the same method and a composed caller |
| Quick checks, completion criteria, and wrap-up | 5 min | Verify design judgment and preview the next day |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 5 + 10 + 10 + 25 + 5. The guided lab is 25 minutes, which stays within the runbook's required 25-35 minute lab range. If the room needs support, protect the guided lab. Shorten the vocabulary discussion before shortening learner practice. Do not make composition, inheritance choice, or polymorphism optional; those are the required objectives for this hour.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain inheritance as an **is-a** relationship and give a reasonable example.
2. Explain composition as a **has-a** relationship and give a reasonable example.
3. Choose composition instead of inheritance when an object needs to use or hold another object.
4. Describe polymorphism as calling different objects through the same expected method name.
5. Explain Python duck typing: if an object provides the method the caller needs, the caller does not require a shared parent class.
6. Identify `if`/`elif` chains that are good candidates for polymorphic refactoring.
7. Refactor a deterministic branching exporter into at least two classes with the same method name.
8. Demonstrate a composed object that stores a formatter or processor and delegates work to it.
9. Keep printing or display logic in caller/demo code where appropriate while service/model objects return strings or data.
10. Avoid overengineering with too many tiny classes or mixing inheritance and composition without a clear reason.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 1, Hour 4 visible for yourself. The required scope is composition vs inheritance, polymorphism, a messy `if`/`elif` refactor, a composed object holding another object, a lab refactor exercise, completion criteria, common pitfalls, optional third implementation, and a quick check about composition being safer than inheritance.
- Open the learner project from Hour 3, or prepare a clean `advanced_tracker` workspace with a `src/` directory.
- Prepare a blank file named `day1_hour4_polymorphism_demo.py` for the live demo, or be ready to create it in front of the class.
- Confirm the terminal command for the environment. Use `python day1_hour4_polymorphism_demo.py` if `python` works. If the lab requires `python3`, consistently say and show `python3 day1_hour4_polymorphism_demo.py`.
- Prepare a board or shared note with these definitions:

```text
Inheritance: use when one type really is a specialized version of another type.
Composition: use when one object has or uses another object.
Polymorphism: different objects can be used through the same expected method.
Duck typing: Python cares more about available behavior than declared ancestry.
```

- Be ready to correct two common mistakes early. First, learners may create a base class because they think polymorphism always requires inheritance. It does not in Python. Second, learners may move the `if`/`elif` chain into a new class and believe they refactored. They have only relocated the branching; they have not simplified the design.
- Decide whether learners will use an exporter, checkout/payment, notification, or tracker report scenario for the lab. This script uses a report exporter because it connects naturally to tracker-style applications.

Suggested board note before the session starts:

```text
Day 1 Hour 4 goals:
1. Inheritance = is-a
2. Composition = has-a
3. Polymorphism = same call, different objects
4. Refactor if/elif into shared-method classes
5. Use a runner/service that has-a formatter
```

---

## Opening Bridge from Hour 3 (5 minutes)

**Instructor talk track**

"In Hour 3, we focused on objects protecting their own valid state. We used properties, invariants, and custom exceptions to make invalid data difficult to store. That was a big step toward professional object-oriented code. A class was no longer just a bag of attributes. It became a place where important rules live."

"Now we are going to look at the next design question: once we have more than one object, how should those objects relate to each other? Should one class inherit from another? Should one object hold another object? Should a function choose behavior with `if` and `elif`, or can it call a method on an object and let the object decide how to do the work?"

"These choices matter because code grows. Early in a program, one `if` statement feels harmless. Then a second case is added. Then a third format is needed. Then one branch needs validation, another branch needs a different output structure, and another branch needs a special field. Soon the function becomes a long control center that knows too much about every variation. At that point, a small change in one feature can accidentally break another feature."

Pause and ask:

"Think about a feature like exporting a report. Maybe it can export plain text, a dictionary for an API, or CSV later. Where have you seen code that says something like `if format_type == 'text'`, `elif format_type == 'json'`, `elif format_type == 'csv'`?"

Take a few short answers. Connect them:

"Exactly. That style is common. It is not evil. Branching is a normal programming tool. But today we learn when branching is becoming a design smell. If the branches represent different kinds of objects that all do the same conceptual job, polymorphism may let us simplify the caller."

"The key phrase for this hour is: same request, different object. We want the caller to say, 'format this report,' without caring whether it received a text formatter or a dictionary formatter. That is polymorphism."

**Transition**

"Let's name the vocabulary first, then we will refactor a small report exporter. The demo will start with working code that uses `if` and `elif`, because in real life we often refactor from working code. Then we will move toward a design that is easier to extend."

---

## Outcomes and Vocabulary (5 minutes)

Use this section to make the vocabulary practical. Keep it concrete and repeat the relationship language several times.

**Instructor talk track**

"There are four vocabulary items we need today: inheritance, composition, polymorphism, and duck typing."

"First, **inheritance**. Inheritance means one class is based on another class. A subclass receives behavior or structure from a parent class. The design question is not, 'Can Python technically do this?' Python can do many things. The design question is, 'Does this relationship mean the subclass really **is a** kind of the parent?'"

Write or display:

```text
Inheritance test:
Can I honestly say "A ___ is a ___"?
```

"For example, if we had a general `Report` class and a `SalesReport` class, we might say, 'A sales report is a report.' That might be a reasonable inheritance relationship. We would still need to think carefully, but the sentence at least makes sense."

"Second, **composition**. Composition means one object contains, stores, receives, or uses another object. The relationship is **has-a** or **uses-a**. If a `ReportRunner` has a formatter, the runner should not inherit from the formatter. A report runner is not a formatter. It uses a formatter."

Write or display:

```text
Composition test:
Can I honestly say "A ___ has a ___" or "A ___ uses a ___"?
```

"Third, **polymorphism**. The word means many forms. In code, it means different objects can respond to the same kind of request. A text formatter and a dictionary formatter can both have a method named `format`. The caller does not need to know the internal details. It calls `formatter.format(report)` either way."

"Fourth, **duck typing**. Python often cares more about what an object can do than what it inherits from. You may have heard the phrase, 'If it walks like a duck and quacks like a duck, treat it like a duck.' In our code, if an object has the method we need, such as `format(report)`, then the caller can use it. The object does not have to inherit from a shared base class just to be useful."

"That does not mean inheritance is bad. Inheritance is powerful when the relationship is real and stable. It does mean inheritance is not required for every shared method name."

**Instructor emphasis**

"A very common early advanced mistake is to think, 'These two classes both have a `format` method, so I must create a parent class.' Not necessarily. In Python, shared behavior at the call site can be enough. Later in the course, when we discuss protocols, abstract base classes, and larger architecture, we will see more formal tools. For this hour, the important habit is simpler: choose the relationship intentionally."

---

## Concept Briefing: Choosing the Relationship (10 minutes)

**Instructor talk track**

"Let's use a tracker-style example. Imagine our application stores a small project report. The report has a title and a few metrics. We want to export it as readable text for a person, and as a dictionary for another part of a program. Later, we might add CSV."

"A beginner-friendly first version might use one function with a format string."

```python
def export_report(report: dict[str, object], format_type: str) -> object:
    if format_type == "text":
        return "some text"
    elif format_type == "dict":
        return {"some": "data"}
    else:
        raise ValueError("Unknown format")
```

"That works. It is not automatically wrong. But notice the direction of change. Every time we add a new format, we reopen this function. We add another branch. We risk breaking an existing branch. The caller also has to pass a string that might be misspelled. The function becomes a traffic controller for every variation."

"Now ask a different question. Are text formatting and dictionary formatting two different **kinds of behavior** that share the same conceptual request? Yes. Both answer the request, 'format this report.' That suggests polymorphism."

"Should `TextReportFormatter` inherit from `DictReportFormatter`? No. A text formatter is not a dictionary formatter. Should both inherit from `ReportRunner`? No. A formatter is not a runner. Should `ReportRunner` inherit from a formatter so it can format reports? Also no. A runner has or uses a formatter. That is composition."

Write this mapping:

```text
TextReportFormatter and DictReportFormatter:
    same method name: format(report)
    relationship to caller: polymorphism

ReportRunner:
    has a formatter
    relationship: composition

No inheritance needed:
    neither formatter is a specialized kind of the other
    the runner is not a formatter
```

"This is the design judgment we want. We are not trying to eliminate every `if` statement from every program. We are trying to notice when branching is selecting between interchangeable behaviors. When that happens, one clean option is to move each behavior into its own object and let the caller use the same method name."

**Ask a prediction question**

"If both formatter classes define a method named `format`, what does the caller need to know before it can use a formatter?"

Expected answers:

- "It needs to know that the object has a `format` method."
- "It needs to know what argument to pass."
- "It needs to know what the method returns."

Respond:

"Good. That is the practical interface. The interface here is not a formal Python base class. It is the shared expectation: this object can format this report when I call `format(report)`."

**Clarify return values and printing**

"One more design habit before the demo. The formatter should return a value. It should not usually print directly. Printing is a display decision. Returning strings or data makes the code easier to test and reuse. In the demo, the caller code will print the result so we can see it. The formatter classes will return strings or dictionaries."

"That boundary connects to Hour 2 and Hour 3. In Hour 2, we kept `print()` out of the model when possible. In Hour 3, we kept domain validation inside the object and user-friendly display at the caller boundary. Today we keep formatting behavior inside formatter objects, while display remains in demo or caller code."

**Relationship examples**

"Let's do a few quick relationship checks."

1. "`Checkout` and `PaymentProcessor`: A checkout has a payment processor. Composition."
2. "`EmailNotifier` and `SmsNotifier`: One is not a special kind of the other. They may share a `send` method. Polymorphism."
3. "`SavingsAccount` and `BankAccount`: A savings account is a bank account. Inheritance might be reasonable if the shared rules are stable."
4. "`Task` and `Logger`: A task is not a logger. If a task needs logging, it has or uses a logger. Composition."
5. "`ReportRunner` and `TextReportFormatter`: A runner is not a formatter. It has a formatter. Composition."

"When learners start using classes heavily, it is tempting to make elaborate family trees. Resist that urge. A shallow design that uses composition is often easier to change than a deep inheritance hierarchy."

**Transition to demo**

"Now we will start from a working but branching exporter. Then we will refactor in small steps. Watch for three things: the before-state branch, the two classes with the same method name, and the composed runner that stores a formatter object."

---

## Live Demo: Refactor Report Export Branching (10 minutes)

Create or open `day1_hour4_polymorphism_demo.py`. Explain that the file is self-contained and deterministic. There is no user input, no file system dependency, and no randomness.

### Step 1: Start with a working before-state

**Instructor talk track**

"First, we need a small report. I am using a dictionary so we can focus on design relationships rather than data modeling. In a larger project, this could be a dataclass or a validated model class. Today the relationship pattern is the main point."

Type or paste:

```python
from typing import Any


Report = dict[str, Any]


def export_report(report: Report, format_type: str) -> object:
    if format_type == "text":
        lines = [
            f"Report: {report['title']}",
            f"Completed: {report['completed']}",
            f"Pending: {report['pending']}",
        ]
        return "\n".join(lines)
    elif format_type == "dict":
        total = int(report["completed"]) + int(report["pending"])
        return {
            "title": report["title"],
            "completed": report["completed"],
            "pending": report["pending"],
            "total": total,
        }
    else:
        raise ValueError(f"Unknown report format: {format_type}")


def run_before_demo() -> None:
    report = {
        "title": "Day 1 Tracker",
        "completed": 7,
        "pending": 3,
    }

    text_output = export_report(report, "text")
    dict_output = export_report(report, "dict")

    print("BEFORE: text export")
    print(text_output)
    print()
    print("BEFORE: dict export")
    print(dict_output)


run_before_demo()
```

Run it:

```bash
python day1_hour4_polymorphism_demo.py
```

Expected output:

```text
BEFORE: text export
Report: Day 1 Tracker
Completed: 7
Pending: 3

BEFORE: dict export
{'title': 'Day 1 Tracker', 'completed': 7, 'pending': 3, 'total': 10}
```

**Instructor talk track**

"This code works. That is important. Refactoring usually starts from working code. We are not refactoring because the output is wrong. We are refactoring because the shape of the code makes future change harder than it needs to be."

"What is the smell? The `export_report` function knows every format. If we add CSV, we edit this function. If we add HTML, we edit this function again. If the text format changes, we risk touching code near the dictionary format. Also, the format type is a string, which can be misspelled."

"The branches represent interchangeable behavior. Both branches answer the same request: format this report. That means we can try polymorphism."

### Step 2: Refactor into two classes with the same method name

Replace the file with the refactored version, or comment out the before-state and add the after-state below it. If time is tight, paste the after-state and narrate each part.

```python
from typing import Any


Report = dict[str, Any]


class TextReportFormatter:
    def format(self, report: Report) -> str:
        lines = [
            f"Report: {report['title']}",
            f"Completed: {report['completed']}",
            f"Pending: {report['pending']}",
        ]
        return "\n".join(lines)


class DictReportFormatter:
    def format(self, report: Report) -> dict[str, Any]:
        total = int(report["completed"]) + int(report["pending"])
        return {
            "title": report["title"],
            "completed": report["completed"],
            "pending": report["pending"],
            "total": total,
        }


class ReportRunner:
    def __init__(self, formatter: Any) -> None:
        self.formatter = formatter

    def build_output(self, report: Report) -> object:
        return self.formatter.format(report)


def run_after_demo() -> None:
    report = {
        "title": "Day 1 Tracker",
        "completed": 7,
        "pending": 3,
    }

    text_runner = ReportRunner(TextReportFormatter())
    dict_runner = ReportRunner(DictReportFormatter())

    print("AFTER: text export")
    print(text_runner.build_output(report))
    print()
    print("AFTER: dict export")
    print(dict_runner.build_output(report))


run_after_demo()
```

Run it again:

```bash
python day1_hour4_polymorphism_demo.py
```

Expected output:

```text
AFTER: text export
Report: Day 1 Tracker
Completed: 7
Pending: 3

AFTER: dict export
{'title': 'Day 1 Tracker', 'completed': 7, 'pending': 3, 'total': 10}
```

**Instructor talk track**

"Now look at what changed. The text-specific logic lives in `TextReportFormatter`. The dictionary-specific logic lives in `DictReportFormatter`. Both classes have a method named `format`. That shared method name is what lets the caller treat them polymorphically."

"The `ReportRunner` demonstrates composition. It has a formatter. The formatter is stored in `self.formatter`. The runner does not inherit from either formatter. It is not a text formatter. It is not a dictionary formatter. It is an object that uses a formatter to build output."

"This line is the composition moment:"

```python
text_runner = ReportRunner(TextReportFormatter())
```

"We are passing one object into another object. Then the `ReportRunner` stores it. That is a **has-a** relationship."

"This line is the polymorphism moment:"

```python
return self.formatter.format(report)
```

"The runner does not ask, 'Are you a text formatter? Are you a dictionary formatter?' It simply calls the method it expects. If the formatter object has a compatible `format` method, this works."

**Important type-hint note**

"You may notice I used `formatter: Any` in the constructor for now. `Any` keeps the Day 1 example simple while avoiding a misleading `object` annotation that would hide the expected `format` method from static checkers. Later in the course, we can make this more precise with protocols or abstract base classes. Today, we are learning the design idea: shared method name, duck typing, and composition. The object must provide the behavior the runner needs."

If learners ask whether this is unsafe, respond:

"It is flexible, but the caller is responsible for passing the right kind of object. In production code, we may add tests, protocols, abstract base classes, or runtime validation. But do not jump to those tools too early. First understand the relationship."

### Step 3: Explain why inheritance is not needed

**Instructor talk track**

"Should we create a parent class named `ReportFormatter`? Maybe later, maybe not. For this demo, we do not need it. Why? Because neither formatter needs inherited code from a parent. We do not have shared state. We do not have shared behavior. We only have a shared method name. Python's duck typing handles that nicely."

"If I wrote `class TextReportFormatter(DictReportFormatter)`, that would be wrong. A text formatter is not a dictionary formatter. If I wrote `class ReportRunner(TextReportFormatter)`, that would also be wrong. A report runner is not a text formatter. These would be examples of using inheritance because it feels advanced rather than because the relationship is true."

"Professional design often means saying no to a tool. We know inheritance exists. We choose not to use it when composition and polymorphism express the design more clearly."

### Step 4: Optional quick extension if the demo is ahead of schedule

If you are ahead by two minutes, add a third formatter to show extension without modifying `ReportRunner`.

```python
class SummaryReportFormatter:
    def format(self, report: Report) -> str:
        total = int(report["completed"]) + int(report["pending"])
        return f"{report['title']}: {report['completed']} of {total} complete"
```

Then add:

```python
summary_runner = ReportRunner(SummaryReportFormatter())
print()
print("AFTER: summary export")
print(summary_runner.build_output(report))
```

Expected additional output:

```text
AFTER: summary export
Day 1 Tracker: 7 of 10 complete
```

**Instructor talk track**

"Notice what we did not edit. We did not edit `ReportRunner`. We did not add another branch inside `build_output`. We created one more object with the same expected method. That is the payoff."

Do not let this optional extension consume lab time. If the room is moving slowly, skip the third formatter and proceed to the lab.

---

## Guided Lab: Refactor a Branching Feature (25 minutes)

**Lab framing**

"Now you will do the same kind of refactor. Start with a feature that works using `if` and `elif`. Then refactor into two classes that share the same method name. Finally, create a composed object that stores one of those objects and calls it through the shared interface."

"You may use the report exporter scenario below, or you may adapt it to checkout/payment processors, notifications, or another tracker-related feature. The completion criteria are the same either way."

### Required lab scenario

Learners should begin with this starter code or an equivalent branching feature:

```python
from typing import Any


Report = dict[str, Any]


def export_summary(report: Report, format_type: str) -> object:
    if format_type == "text":
        return (
            f"{report['title']}\n"
            f"Owner: {report['owner']}\n"
            f"Open items: {report['open_items']}"
        )
    elif format_type == "dict":
        return {
            "title": report["title"],
            "owner": report["owner"],
            "open_items": report["open_items"],
            "status": "needs attention" if report["open_items"] else "clear",
        }
    else:
        raise ValueError(f"Unsupported format: {format_type}")


def main() -> None:
    report = {
        "title": "Refactor Lab",
        "owner": "Data Team",
        "open_items": 4,
    }

    print(export_summary(report, "text"))
    print(export_summary(report, "dict"))


main()
```

### Lab tasks

Ask learners to complete these tasks in order:

1. Run the starter code and confirm the before-state works.
2. Create a `TextSummaryFormatter` class with a method named `format`.
3. Create a `DictSummaryFormatter` class with the same method name, `format`.
4. Move the text branch logic into `TextSummaryFormatter.format`.
5. Move the dictionary branch logic into `DictSummaryFormatter.format`.
6. Create a composed object named `SummaryExporter`, `ReportRunner`, or similar.
7. Give that object an `__init__` method that accepts a formatter object and stores it on `self`.
8. Give the composed object a method such as `export(report)` or `build_output(report)` that calls `self.formatter.format(report)`.
9. Update `main()` so it creates one runner with `TextSummaryFormatter()` and one runner with `DictSummaryFormatter()`.
10. Print the returned output in `main()`, not inside the formatter classes.

### Lab success shape

Learner solutions may vary, but they should resemble this structure:

```python
from typing import Any


Report = dict[str, Any]


class TextSummaryFormatter:
    def format(self, report: Report) -> str:
        return (
            f"{report['title']}\n"
            f"Owner: {report['owner']}\n"
            f"Open items: {report['open_items']}"
        )


class DictSummaryFormatter:
    def format(self, report: Report) -> dict[str, Any]:
        return {
            "title": report["title"],
            "owner": report["owner"],
            "open_items": report["open_items"],
            "status": "needs attention" if report["open_items"] else "clear",
        }


class SummaryExporter:
    def __init__(self, formatter: Any) -> None:
        self.formatter = formatter

    def export(self, report: Report) -> object:
        return self.formatter.format(report)


def main() -> None:
    report = {
        "title": "Refactor Lab",
        "owner": "Data Team",
        "open_items": 4,
    }

    text_exporter = SummaryExporter(TextSummaryFormatter())
    dict_exporter = SummaryExporter(DictSummaryFormatter())

    print("Text output:")
    print(text_exporter.export(report))
    print()
    print("Dictionary output:")
    print(dict_exporter.export(report))


main()
```

Expected output:

```text
Text output:
Refactor Lab
Owner: Data Team
Open items: 4

Dictionary output:
{'title': 'Refactor Lab', 'owner': 'Data Team', 'open_items': 4, 'status': 'needs attention'}
```

### Instructor circulation plan

Use the first 5 minutes to make sure everyone has a working before-state. Say:

"Do not refactor code you have not run. First prove the starting behavior. Refactoring means changing structure while preserving behavior."

Use the next 10 minutes to look for the shared method name. Ask:

"What method name did you choose for both classes?"

If a learner has `to_text` in one class and `to_dict` in another, guide them:

"Those names describe the output type, but they do not give the caller one common request. For polymorphism, the caller should be able to make the same call on either object. Try using `format(report)` on both, or use `export(report)` on both."

Use the next 5 minutes to check composition. Ask:

"Where is one object stored inside another object?"

Expected learner answer:

"The exporter stores the formatter on `self.formatter`."

If they only have standalone formatter classes and no composed runner, prompt:

"You have the polymorphic classes. Now add an object that has one of those classes. Its job is to receive a formatter in `__init__`, store it, and call the shared method."

Use the final 5 minutes for completion checks, optional extensions, and one or two quick student explanations.

### Required completion criteria

By the end of the lab, each learner should be able to show:

- The original feature started with `if`/`elif` branching.
- The refactor reduced or removed the format-selection branching from the main export path.
- There are at least two classes with the same method name.
- The shared method accepts the same kind of input.
- The caller can use both objects through the same interface.
- There is a composed object that stores another object, such as `self.formatter`.
- The feature still works and produces equivalent useful output.
- The resulting code is easier to read because each class owns one variation.

---

## Troubleshooting During the Lab

### Problem: The learner created classes but kept the entire `if`/`elif`

**Symptom**

The code now has a class named `Exporter`, but inside it there is still a long method:

```python
def export(self, report: Report, format_type: str) -> object:
    if format_type == "text":
        ...
    elif format_type == "dict":
        ...
```

**Instructor response**

"This is a common first step, but it is not the refactor we are aiming for. You moved the branch into a class, but the class still knows every format. Try creating one class per format. Then the caller chooses the object once, and the export method no longer needs to ask which format it is."

### Problem: The learner used inheritance without an is-a relationship

**Symptom**

The code says something like:

```python
class DictSummaryFormatter(TextSummaryFormatter):
    ...
```

**Instructor response**

"Read that relationship out loud. Is a dictionary formatter a text formatter? Not really. They are siblings in behavior, not parent and child. They can share a method name without inheriting from each other. Remove the inheritance for now and let both classes stand independently."

### Problem: The composed object is missing

**Symptom**

The learner directly calls:

```python
TextSummaryFormatter().format(report)
DictSummaryFormatter().format(report)
```

**Instructor response**

"That demonstrates polymorphism, but we also need composition today. Add a small `SummaryExporter` or `ReportRunner` that receives a formatter object in `__init__`, stores it, and delegates to it. The important line will look like `self.formatter = formatter`."

### Problem: The classes print instead of returning values

**Symptom**

The formatter method contains `print(...)` and returns `None`.

**Instructor response**

"For this design, make the formatter return the formatted value. Then `main()` can print it. Returning values keeps the formatter easier to test and reuse. If tomorrow we send the output to a file, an API, or a GUI, a returned value is more flexible than a print statement buried inside the formatter."

### Problem: The shared method names do not match

**Symptom**

One class has `to_text`; another has `to_dict`; the runner has to branch or know which one to call.

**Instructor response**

"Those method names are descriptive, but they force the caller to know the concrete type. For polymorphism, choose one shared method name, such as `format` or `export`. The object decides how to satisfy that request."

### Problem: AttributeError appears

**Symptom**

The terminal shows:

```text
AttributeError: 'Something' object has no attribute 'format'
```

**Instructor response**

"This is duck typing feedback. The runner expected an object with a `format` method, but the object it received did not provide that method name. Check the object you passed into the runner. Check the spelling of the method. Check whether you called `format_report` in one place and `format` in another."

### Problem: The learner created many tiny classes

**Symptom**

There is a class for the title line, a class for the owner line, a class for the open-items line, and a class for every small expression.

**Instructor response**

"This is overengineering. Advanced design does not mean every line gets its own class. A class should own a meaningful responsibility. In this lab, one formatter class per output variation is enough."

---

## Common Pitfalls to Watch For

1. **Using inheritance because it looks advanced**

   Inheritance should communicate a real **is-a** relationship. If the sentence sounds false, avoid the inheritance. A `Checkout` is not a `PaymentProcessor`. A `ReportRunner` is not a `TextFormatter`. A `Task` is not a `Logger`.

2. **Confusing shared method names with shared ancestry**

   In Python, two classes can both define `format` without inheriting from the same parent. That is often enough for simple duck-typed polymorphism.

3. **Moving branching instead of reducing branching**

   A class that contains the same large `if`/`elif` chain may not be an improvement. The goal is to let different objects own different behavior so the caller does not need to know every case.

4. **Mixing inheritance and composition without a reason**

   A design can use both tools, but each relationship needs a reason. If an object has another object, use composition. If one type truly is a specialized version of another type, inheritance may fit. Do not combine them because the diagram looks more impressive.

5. **Printing inside service or formatter code too early**

   Printing makes demos visible, but it also couples logic to the terminal. Prefer returning strings or data from formatter and service objects. Print at the caller boundary.

6. **Creating too many tiny classes**

   Polymorphism is useful when there are meaningful interchangeable behaviors. It is not useful if every small line of code becomes a new class. Keep the design as simple as the problem allows.

7. **Letting type strings leak everywhere**

   A string such as `"text"` or `"dict"` can be useful at a boundary, such as command-line input or an API request. But once the program has chosen a formatter object, the deeper code should not keep branching on the same string.

---

## Optional Extensions

Offer these only after learners have met the required completion criteria.

### Extension 1: Add a third implementation

Add a `CsvSummaryFormatter` or `SummaryLineFormatter` with the same method name:

```python
class CsvSummaryFormatter:
    def format(self, report: Report) -> str:
        return (
            "title,owner,open_items\n"
            f"{report['title']},{report['owner']},{report['open_items']}"
        )
```

Then demonstrate:

```python
csv_exporter = SummaryExporter(CsvSummaryFormatter())
print(csv_exporter.export(report))
```

The important rule: do not edit `SummaryExporter` to add a CSV branch. The extension is successful only if the composed runner can use the new formatter through the same method call.

### Extension 2: Boundary mapping from strings to objects

If learners ask how a real app chooses the formatter from user input, show a small boundary-level mapping:

```python
formatters = {
    "text": TextSummaryFormatter(),
    "dict": DictSummaryFormatter(),
    "csv": CsvSummaryFormatter(),
}

chosen_formatter = formatters["text"]
exporter = SummaryExporter(chosen_formatter)
```

Emphasize:

"A small dictionary at the boundary is different from scattering `if`/`elif` logic throughout the application. The boundary chooses an object. The rest of the code uses the shared interface."

### Extension 3: Checkout/payment variation

Fast finishers may refactor a checkout example instead:

```python
class CreditCardProcessor:
    def process(self, amount: float) -> str:
        return f"Charged ${amount:.2f} to credit card"


class GiftCardProcessor:
    def process(self, amount: float) -> str:
        return f"Used ${amount:.2f} from gift card balance"


class Checkout:
    def __init__(self, processor: Any) -> None:
        self.processor = processor

    def complete(self, amount: float) -> str:
        return self.processor.process(amount)
```

Ask:

"Which relationship is composition here?"

Expected answer:

"Checkout has a processor."

Ask:

"Which part demonstrates polymorphism?"

Expected answer:

"Both processors have `process(amount)`, and `Checkout.complete` calls that method without branching."

---

## Quick Checks, Completion Criteria, and Wrap-up (5 minutes)

### Quick check 1: Composition safer than inheritance

Ask:

"Name one scenario where composition is safer or more flexible than inheritance."

Expected answers:

- "When an object needs to use a helper, such as a report runner using a formatter."
- "When behavior may change at runtime, such as swapping a payment processor."
- "When the relationship is has-a instead of is-a."
- "When a class would otherwise inherit from something it is not, such as a task inheriting from a logger."

Reinforce:

"Good. Composition is safer when we want to plug in or swap behavior without claiming one class is a subtype of another."

### Quick check 2: Identify the relationship

Read each prompt and ask learners to answer "inheritance," "composition," or "polymorphism."

1. "`Checkout` stores a `CreditCardProcessor` object."
   Expected: "Composition."

2. "`TextFormatter` and `DictFormatter` both have `format(report)` and the caller uses either one."
   Expected: "Polymorphism."

3. "`AdminUser` is a specialized kind of `User`."
   Expected: "Inheritance may be appropriate."

4. "`ReportRunner` inherits from `TextFormatter` so it can use text formatting."
   Expected: "Probably wrong. Use composition."

### Completion criteria for the hour

Before ending, make sure learners can show or explain:

- They know inheritance is for **is-a** relationships.
- They know composition is for **has-a** or **uses-a** relationships.
- They can describe polymorphism as using the same method call with different objects.
- They refactored a branching feature into at least two shared-method classes.
- They used a composed object that stores another object.
- The feature still works after refactoring.
- The code is easier to read because each variation has a clear home.

### Wrap-up script

"Today closes Day 1 of Advanced Python. We started the day by setting up the environment and Git workflow. Then we moved into object-oriented design: first identifying responsibilities, then protecting valid state with properties and exceptions, and now choosing relationships between objects."

"The big lesson from this hour is not that inheritance is bad. Inheritance is useful when the relationship is truly **is-a**. The lesson is that inheritance should not be our default tool for every relationship. If one object needs another object, use composition. If several objects can answer the same request, use polymorphism. In Python, that polymorphism can often be simple duck typing: the object has the method the caller needs."

"As you continue into the next sessions, keep asking three design questions. First: what responsibility does this code own? Second: is this relationship **is-a** or **has-a**? Third: am I branching because I truly have different logic in this moment, or because I should be passing in a different object with the same method?"

"Those questions are part of the move from writing scripts that work once to designing programs that can grow."

End with:

"Before you leave, make sure your Hour 4 lab file is saved. If you are using Git, make a checkpoint commit with a message such as `Refactor exporter with composition and polymorphism`. We will build on these design habits in the next session."
