# Day 11 Hour 4 (Hour 44): Exception Handling — Full Basics Treatment Instructor Script

## Instructor intent and alignment

This hour is the capstone of Session 11. In Hours 41–43, learners built file and JSON workflow confidence. In Hour 44, we harden that workflow so student programs can survive bad input and bad files without crashing. This script is designed to be read nearly verbatim while you teach.

Runbook alignment for Hour 44 is fully covered in this lesson:

- Outcomes: use `try/except` for runtime errors; catch specific exceptions when practical.
- Talk points (10–15 min): `try/except/else/finally`; `ValueError`; `FileNotFoundError` + `json.JSONDecodeError`.
- Live demo (5–10 min): numeric input + file loading wrapped with friendly error messages.
- Lab (25–35 min): add specific `try/except` around numeric conversion and JSON load; on error show friendly message and continue.
- Completion criteria: continue after bad input; handle missing/corrupt file gracefully.
- Common pitfalls: broad `Exception` everywhere; swallowing errors silently.
- Optional extension: simple error logging to a text file.
- Quick check: explain why specific catches are better than catch-all.

## Hour flow at a glance

Use this pacing guide to keep the hour tight:

1. **Warm open + objective framing (2–3 min)**
2. **Instructor talk points (10–15 min)**
3. **Live demo with deterministic scenarios (5–10 min)**
4. **Hands-on hardening lab (25–35 min)**
5. **Debrief + quick check exit ticket (3–5 min)**

If learners are stuck during lab, shorten independent time by 5 minutes and run a guided fix pass.

## Outcomes to state out loud

Say this near the beginning:

“By the end of this hour, you can do two professional things. First, you can wrap risky code in `try/except` so your program handles runtime errors instead of crashing. Second, you can catch specific exceptions—like `ValueError`, `FileNotFoundError`, and `json.JSONDecodeError`—so users get clear feedback and you still keep bugs visible during development.”

Then add:

“Today is not about hiding errors. Today is about handling expected errors gracefully and leaving unexpected errors visible so we can debug them.”

## Prerequisites and setup check

Learners should already be comfortable with:

- `input()`, `int()`, `float()`
- loops (`while`, `for`)
- function basics
- reading JSON via `json.load()`
- file paths with `pathlib.Path`

Before teaching, confirm these files and folders:

- Working folder: `day11_hour4_exception_lab/`
- Data folder: `day11_hour4_exception_lab/data/`
- File 1 (valid): `day11_hour4_exception_lab/data/class_settings_valid.json`
- File 2 (corrupt): `day11_hour4_exception_lab/data/class_settings_corrupt.json`

Create deterministic file contents exactly as shown:

`class_settings_valid.json`

```json
{
  "course_name": "Python Basics",
  "max_students": 24,
  "lab_mode": true
}
```

`class_settings_corrupt.json`

```json
{
  "course_name": "Python Basics",
  "max_students": 24,
  "lab_mode": true
```

The corrupt file is intentionally missing the closing `}`.

## Vocabulary and concept framing (speak these explicitly)

- **Syntax error**: Python cannot parse the code at all. The program does not start.
- **Runtime error (exception)**: code is syntactically valid but fails during execution.
- **Exception handling**: controlled response to a runtime error.
- **Specific exception**: a narrow, expected error type, like `ValueError`.
- **Friendly error message**: clear language for users, not raw traceback dumps.

Say:

“Syntax errors are like a broken key that does not fit the lock. Runtime errors are like a key that fits, but the door is blocked. Exception handling is how we react safely when we find the door blocked.”

## Instructor talk points (10–15 minutes)

### 1) Exceptions vs syntax errors (2–3 minutes)

Script:

“If I type `print('hello'` with a missing parenthesis, Python throws a syntax error before running anything. That is not what `try/except` is for. `try/except` is for errors that happen while running valid code—like converting `abc` to an integer or opening a file that is not there.”

Optional micro-demo:

```python
print("This line is valid")
broken_example = "print('Missing quote)"  # syntax error example captured as text
```

Then:

“We do not catch syntax errors with `try/except`. We fix syntax errors in code.”

### 2) `try/except` as a control pattern (3 minutes)

Teach the mental model:

1. Put risky code in `try`.
2. Put recovery code in `except`.
3. Keep the exception type specific.
4. Continue the program where reasonable.

Minimal example:

```python
user_text = input("Enter a whole number: ")

try:
    count = int(user_text)
except ValueError:
    print("Please enter digits only, such as 12.")
else:
    print(f"Thanks. You entered {count}.")
```

Narration:

- “If conversion fails, `except ValueError` runs.”
- “If conversion succeeds, `else` runs.”
- “The `else` block helps us separate success logic from error logic.”

### 3) Why specific exceptions matter (2–3 minutes)

Say:

“Specific catches are better because they document intent and reduce accidental bug hiding. If I only expect conversion failures, I should catch `ValueError`, not every possible exception.”

Compare good vs bad quickly:

```python
try:
    value = int("abc")
except ValueError:
    print("Not a valid integer.")
```

```python
try:
    value = int("abc")
except Exception:
    print("Something went wrong.")
```

Instructor note: be explicit that broad catch-all is discouraged in this course. Do not normalize it as standard practice.

### 4) `try/except/else/finally` pattern (3–4 minutes)

Explain each block:

- `try`: risky operation.
- `except SomeError`: specific response when that error occurs.
- `else`: run only if no exception occurred.
- `finally`: always run (cleanup/logging marker).

Demonstration snippet:

```python
from pathlib import Path

target = Path("data/class_settings_valid.json")

try:
    text = target.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Could not find file: {target}")
else:
    print(f"Loaded {len(text)} characters.")
finally:
    print("Load attempt finished.")
```

Key line to say:

“`finally` runs no matter what, so it is perfect for ‘always do this’ actions. In real systems that can be cleanup, metrics, or a closing status message.”

### 5) Core expected exceptions for this hour (2 minutes)

You must explicitly name and define:

- `ValueError`: wrong value shape/type for conversion, e.g., `int("five")`.
- `FileNotFoundError`: target file path does not exist.
- `json.JSONDecodeError`: file exists, but JSON syntax is invalid.

Say:

“Notice these are all predictable in user-facing CLI apps. That is why they are first-class catches for today.”

### 6) Common pitfalls to call out before demo (1 minute)

Say this directly:

- “Pitfall one: `except Exception` everywhere. That masks bugs.”
- “Pitfall two: silent failure with `pass`. If the user sees no message, they do not know what to fix.”

## Transition line into demo

Use:

“Now let’s harden a tiny script with two fragile points: numeric input and JSON file loading. We will make it resilient while keeping exception handling specific.”

## Live demo (5–10 minutes): numeric input + JSON loading with friendly errors

### Demo objective

Students should see that:

- bad numeric input does not crash the program,
- missing or corrupt JSON is handled gracefully,
- the script prints clear, friendly messages,
- program flow continues after recoverable errors.

### Demo script file

Create `day11_hour4_exception_lab/demo_hour44.py` with this exact code:

```python
from __future__ import annotations

import json
from pathlib import Path


DATA_DIR = Path("data")
VALID_FILE = DATA_DIR / "class_settings_valid.json"
CORRUPT_FILE = DATA_DIR / "class_settings_corrupt.json"
MISSING_FILE = DATA_DIR / "class_settings_missing.json"


def prompt_positive_int(prompt: str) -> int:
    """Prompt until user enters a positive integer."""
    while True:
        raw_value = input(prompt).strip()
        try:
            number = int(raw_value)
        except ValueError:
            print("Friendly error: please type digits only, such as 3 or 15.")
            continue

        if number <= 0:
            print("Friendly reminder: the number must be greater than zero.")
            continue

        return number


def load_settings(file_path: Path) -> dict[str, object] | None:
    """Load JSON settings file with specific exception handling."""
    print(f"\nLoading settings from: {file_path}")
    try:
        with file_path.open("r", encoding="utf-8") as handle:
            settings = json.load(handle)
    except FileNotFoundError:
        print("Friendly error: settings file was not found. Continuing with defaults.")
        return None
    except json.JSONDecodeError:
        print("Friendly error: settings file is not valid JSON. Continuing with defaults.")
        return None
    else:
        print("Settings loaded successfully.")
        return settings
    finally:
        print("File load attempt completed.")


def main() -> None:
    print("=== Hour 44 Exception Handling Demo ===")

    student_count = prompt_positive_int("Enter the number of students attending today: ")
    print(f"Thanks. You entered: {student_count}")

    settings_valid = load_settings(VALID_FILE)
    settings_missing = load_settings(MISSING_FILE)
    settings_corrupt = load_settings(CORRUPT_FILE)

    print("\nSummary:")
    print(f"- valid file loaded: {settings_valid is not None}")
    print(f"- missing file loaded: {settings_missing is not None}")
    print(f"- corrupt file loaded: {settings_corrupt is not None}")
    print("\nProgram completed without crashing.")


if __name__ == "__main__":
    main()
```

### Demo run sequence

Run 1 input sequence:

1. At prompt, enter `five`.
2. Then enter `-2`.
3. Then enter `12`.

Expected console output pattern (allow path differences but keep message content):

```text
=== Hour 44 Exception Handling Demo ===
Enter the number of students attending today: five
Friendly error: please type digits only, such as 3 or 15.
Enter the number of students attending today: -2
Friendly reminder: the number must be greater than zero.
Enter the number of students attending today: 12
Thanks. You entered: 12

Loading settings from: data\class_settings_valid.json
Settings loaded successfully.
File load attempt completed.

Loading settings from: data\class_settings_missing.json
Friendly error: settings file was not found. Continuing with defaults.
File load attempt completed.

Loading settings from: data\class_settings_corrupt.json
Friendly error: settings file is not valid JSON. Continuing with defaults.
File load attempt completed.

Summary:
- valid file loaded: True
- missing file loaded: False
- corrupt file loaded: False

Program completed without crashing.
```

### Narration script during demo

Use this flow:

1. “I typed `five` and got a friendly message. The program did not crash.”
2. “I typed `-2`. This is not a conversion error, but still invalid for our rule, so we handle it with normal `if` logic.”
3. “Now valid input passes and we continue.”
4. “Valid JSON loads through `else`.”
5. “Missing file triggers `FileNotFoundError` catch.”
6. “Corrupt JSON triggers `json.JSONDecodeError` catch.”
7. “`finally` prints every time, so we can clearly see each load attempt ended.”

Ask prediction questions:

- “What do you think happens first, `else` or `finally` on success?”
- “If the file is missing, does `else` run?”

Answers:

- On success: `else`, then `finally`.
- On failure: matching `except`, then `finally`; `else` is skipped.

## Structured debrief after demo (2 minutes)

Say:

“Two places were hardened: conversion and file read. We used specific catches and user-friendly messages. The program kept running and reported what happened. That is the exact professional behavior we want in basic CLI tools.”

Then connect to lab:

“Now you will take a fragile starter program and add this same resilience.”

## Hands-on lab (25–35 minutes): Harden your program

### Lab prompt (student-facing)

“You are given a small script with two fragile operations:

1. numeric conversion from user input,
2. JSON loading from a path.

Your job is to add specific exception handling so the program does not crash on common errors. On failure, show a friendly message and continue running.”

### Starter file (intentionally fragile)

Create `day11_hour4_exception_lab/lab_start.py` with this code:

```python
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    print("=== Enrollment Tool (Starter) ===")

    raw_count = input("How many students are registering? ")
    student_count = int(raw_count)

    raw_fee = input("What is the lab fee per student? ")
    fee = float(raw_fee)

    file_name = input("Enter JSON settings file name (example: class_settings_valid.json): ").strip()
    path = Path("data") / file_name

    with path.open("r", encoding="utf-8") as handle:
        settings = json.load(handle)

    total = student_count * fee
    print(f"Course: {settings['course_name']}")
    print(f"Total estimated fees: ${total:.2f}")


if __name__ == "__main__":
    main()
```

### Required lab tasks

Students must complete all:

1. Add `try/except` around `int()` and `float()` conversion points.
2. Keep catches specific:
   - `ValueError` for conversion.
   - `FileNotFoundError` and `json.JSONDecodeError` for JSON load.
3. On invalid numeric input, display a friendly message and keep prompting.
4. On missing/corrupt JSON file, display a friendly message and continue program (for example, by using default settings dictionary).
5. Ensure the program reaches a final summary print even after recoverable errors.

### Instructor constraints to repeat out loud

- “Do not use bare `except:`.”
- “Do not wrap your entire program in one giant catch-all.”
- “Do not hide errors with `pass`.”

### Suggested scaffold hints (release progressively)

Hint 1 (early):

“Use a `while True` loop for each conversion prompt. `continue` on `ValueError`, `return` after valid conversion.”

Hint 2 (mid):

“Create a helper like `load_settings(path: Path) -> dict[str, object]` that returns defaults when file load fails.”

Hint 3 (late):

“`else` is a clean place to print success messages after `json.load()` succeeds.”

### Reference lab solution (for instructor walkthrough/debrief)

Use this solution after most students have attempted independently:

```python
from __future__ import annotations

import json
from pathlib import Path


DEFAULT_SETTINGS: dict[str, object] = {
    "course_name": "Python Basics (Default)",
    "max_students": 20,
    "lab_mode": False,
}


def prompt_int(message: str) -> int:
    while True:
        raw_value = input(message).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Friendly error: please enter a whole number (example: 10).")
            continue
        else:
            return value


def prompt_float(message: str) -> float:
    while True:
        raw_value = input(message).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Friendly error: please enter a number (example: 49.99).")
            continue
        else:
            return value


def load_settings(file_path: Path) -> dict[str, object]:
    try:
        with file_path.open("r", encoding="utf-8") as handle:
            settings = json.load(handle)
    except FileNotFoundError:
        print(f"Friendly error: '{file_path.name}' was not found. Using default settings.")
        return DEFAULT_SETTINGS.copy()
    except json.JSONDecodeError:
        print(f"Friendly error: '{file_path.name}' has invalid JSON. Using default settings.")
        return DEFAULT_SETTINGS.copy()
    else:
        print(f"Loaded settings from '{file_path.name}'.")
        return settings


def main() -> None:
    print("=== Enrollment Tool (Hardened) ===")

    student_count = prompt_int("How many students are registering? ")
    while student_count <= 0:
        print("Friendly reminder: student count must be greater than zero.")
        student_count = prompt_int("How many students are registering? ")

    fee = prompt_float("What is the lab fee per student? ")
    while fee < 0:
        print("Friendly reminder: fee cannot be negative.")
        fee = prompt_float("What is the lab fee per student? ")

    file_name = input(
        "Enter JSON settings file name (class_settings_valid.json / "
        "class_settings_corrupt.json / class_settings_missing.json): "
    ).strip()
    settings_path = Path("data") / file_name

    settings = load_settings(settings_path)

    total = student_count * fee
    course_name = str(settings.get("course_name", "Unknown Course"))

    print("\nSummary:")
    print(f"- Course: {course_name}")
    print(f"- Student count: {student_count}")
    print(f"- Fee per student: ${fee:.2f}")
    print(f"- Total estimated fees: ${total:.2f}")
    print("Program completed successfully.")


if __name__ == "__main__":
    main()
```

### Deterministic test cases for completion check

Run these three tests in class:

#### Test A: bad numeric input then recovery

Inputs:

- `ten`
- `12`
- `free`
- `15.5`
- `class_settings_valid.json`

Expected behavior:

- Shows friendly `ValueError` messages for `ten` and `free`.
- Re-prompts without crashing.
- Loads valid JSON and prints summary.

#### Test B: missing settings file

Inputs:

- `10`
- `20`
- `class_settings_missing.json`

Expected behavior:

- Friendly file-not-found message.
- Uses defaults.
- Still prints summary and completes.

#### Test C: corrupt JSON settings file

Inputs:

- `8`
- `30`
- `class_settings_corrupt.json`

Expected behavior:

- Friendly JSON-corrupt message.
- Uses defaults.
- Still prints summary and completes.

### Lab completion criteria (must all be true)

Check each learner/group against these:

1. Program continues after bad numeric input.
2. Program handles missing file gracefully (`FileNotFoundError` path).
3. Program handles corrupt JSON gracefully (`json.JSONDecodeError` path).
4. Friendly messages are displayed; no silent failure.
5. Exception handling remains specific, not broad catch-all everywhere.

If a student solution uses `except Exception` for everything, mark as incomplete until revised.

## Instructor coaching guide during lab

### Common student issue 1: giant catch-all block

Student pattern:

```python
try:
    # entire program
except Exception:
    print("Error")
```

Coach response:

“This hides too much. Narrow your `try` block to one risky operation, then catch only the expected exception type. Keep debugging visibility.”

### Common student issue 2: silent swallow with `pass`

Student pattern:

```python
except ValueError:
    pass
```

Coach response:

“Users need feedback. Replace `pass` with a clear instruction: what failed and what input format is expected.”

### Common student issue 3: confusing validation with exceptions

Clarify:

- `ValueError` catch handles conversion failure.
- Business rule checks (like `number <= 0`) are regular `if` logic.

Say:

“Not every invalid case is an exception. Exceptions are for runtime failures in operations like conversion and file parsing.”

### Common student issue 4: forgetting to continue flow

If program exits too early after an error:

“The runbook goal says continue after bad input and handle missing/corrupt files gracefully. Use loops for input retries and defaults for file fallback.”

## Deepening understanding: specific vs broad exception handling

Use this mini-teaching segment if time allows:

Imagine this bug inside load code:

```python
print(course_nam)  # typo: should be course_name
```

If code uses broad `except Exception`, the typo may be hidden under a generic “something went wrong,” and debugging takes longer. If code catches only `FileNotFoundError` and `json.JSONDecodeError`, then a typo like `NameError` remains visible, which is exactly what we want during development.

Teaching phrase:

“Catch expected errors. Expose unexpected errors.”

## Optional extension (stay in Basics scope): simple error logging to text file

This extension is optional and should only start after core criteria are complete.

### Why this extension matters

Friendly console messages help users now, but logs help developers later. A simple append-only text log is enough at Basics level.

### Extension implementation pattern

Add this helper:

```python
from pathlib import Path


def log_error(message: str) -> None:
    log_path = Path("error_log.txt")
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(f"{message}\n")
```

Integrate into specific handlers:

```python
except FileNotFoundError:
    friendly = f"Friendly error: '{file_path.name}' was not found. Using defaults."
    print(friendly)
    log_error(f"FileNotFoundError on {file_path}")
    return DEFAULT_SETTINGS.copy()
except json.JSONDecodeError:
    friendly = f"Friendly error: '{file_path.name}' has invalid JSON. Using defaults."
    print(friendly)
    log_error(f"JSONDecodeError on {file_path}")
    return DEFAULT_SETTINGS.copy()
```

### Expected log file sample

`error_log.txt`

```text
FileNotFoundError on data\class_settings_missing.json
JSONDecodeError on data\class_settings_corrupt.json
```

Instructor note: keep logging simple and deterministic. Do not add advanced logging frameworks in Basics hour.

## Discussion prompts to reinforce reasoning

Ask these during debrief:

1. “Why do we retry numeric input but not retry file parsing forever?”
2. “When should we use defaults versus stopping the program?”
3. “What is one risk of using `except Exception` everywhere?”
4. “Where did `else` help readability in your code?”
5. “What did `finally` guarantee in the demo?”

Suggested target answers:

1. Numeric input can be corrected immediately by the user; repeated prompt is natural.
2. Defaults are useful when safe fallback exists; stop when critical data is truly required.
3. It can mask unrelated bugs and slow debugging.
4. It cleanly separated success path from error path.
5. It always ran to mark completion of each load attempt.

## Expanded facilitation guide: minute-by-minute lab support

Use this section when you want a more detailed live teaching rhythm during the 25–35 minute lab block. The goal is to keep students coding independently while still giving structured checkpoints that reduce panic and improve completion rates.

### Minute 0–3: launch with confidence and constraints

Say:

“Open your starter file. Read the code once without editing. Put your cursor on each fragile line: `int(raw_count)`, `float(raw_fee)`, and `json.load(handle)`. Those are our hardening targets.”

Then add:

“You are not rewriting the whole app. You are adding resilience exactly where failure is expected. Keep your code simple and specific.”

This framing prevents over-engineering and keeps novice learners from feeling lost.

### Minute 3–8: first hardening target (integer conversion)

Prompt learners:

“Wrap only the integer conversion in `try/except ValueError`. If conversion fails, print a clear correction message and ask again.”

What to watch for:

- Students placing `input()` outside the loop.
- Students forgetting `continue`.
- Students converting once, then never re-prompting.

Helpful coaching sentence:

“A retry loop is your safety net. If input is wrong, stay in loop. If input is valid, exit loop by returning the value.”

### Minute 8–12: second hardening target (float conversion)

Prompt:

“Now repeat the same pattern for `float()`. Keep this separate from integer handling so the user gets precise feedback.”

If students try one combined mega-function too early, steer them back:

“You can generalize later. For now, duplicate the pattern intentionally so the logic stays readable.”

This matters for beginners: repetition builds pattern recognition.

### Minute 12–18: file loading hardening with two specific exceptions

Prompt:

“Move file loading into a helper function and catch only these two errors: `FileNotFoundError` and `json.JSONDecodeError`.”

Guide learners toward safe fallback:

“Return a default dictionary so the program can still print a summary.”

Watch for this mistake:

```python
except FileNotFoundError:
    print("error")
```

If they print and then forget `return`, the function may return `None` and fail later. Coaching line:

“In every error branch, return a known fallback object so downstream code stays predictable.”

### Minute 18–23: preserve business-rule validation

Many students confuse exception handling with all validation. Remind them:

“`ValueError` catches conversion problems. But if someone enters `-5`, that is valid numeric text with invalid business meaning. Use `if` checks after conversion.”

Quick board example:

```python
value = prompt_int("Enter quantity: ")
if value <= 0:
    print("Quantity must be greater than zero.")
```

Then tie it back:

“Exceptions protect operations. Conditionals enforce rules.”

### Minute 23–28: run deterministic tests A, B, C

Require each learner to execute all three scenario tests. Ask them to read outputs out loud in pairs:

- A: invalid numbers recover.
- B: missing file falls back.
- C: corrupt file falls back.

Partner-reading improves attention to exact behavior and catches silent failures quickly.

### Minute 28–32: polish messages and flow

Ask students to improve message clarity:

- State what went wrong.
- State what to do next.
- Avoid blame language.

Good message:

“Friendly error: please enter a whole number (example: 10).”

Weak message:

“Invalid.”

Why this matters:

User-facing quality is not just avoiding crashes; it is helping recovery.

### Minute 32–35: final verification and share-outs

End lab with two volunteer demos:

1. one run with invalid numeric input recovery,
2. one run with missing or corrupt JSON fallback.

Ask classmates:

“Which specific exceptions were caught? Did the app still complete?”

This reinforces both required outcomes in public and helps anchor good habits.

## Expanded misconception clinic (for real-time correction)

Use these targeted corrections when you hear common misconceptions.

### Misconception: “If I catch `Exception`, I am safer.”

Correction script:

“It feels safer, but it often makes debugging less safe. Catch-all blocks can hide bugs you did not intend to handle. Specific catches are safer because they match known failure modes.”

### Misconception: “`finally` is required in every `try`.”

Correction:

“`finally` is optional. Use it when you truly need an always-run action. In this hour, we use it to demonstrate guaranteed completion messages.”

### Misconception: “If I have `else`, I do not need `except`.”

Correction:

“`else` runs only when no exception happened. It does not replace error handling. Think of `else` as success-only space.”

### Misconception: “Validation should be done inside `except`.”

Correction:

“Use `except` for exceptions from operations like `int()`, file open, or JSON parse. Use regular `if` statements for business constraints like positive ranges.”

### Misconception: “Silent `pass` is cleaner.”

Correction:

“Silent failure is confusing for users and harmful for support. At minimum, print a friendly message. Better yet, also log the event in the optional extension.”

## Instructor language bank for supportive coaching

When students struggle, phrasing matters. Use these lines:

- “Great, you found the failure point. Now let’s make it recoverable.”
- “Your logic is close; you just need a loop so users can correct input.”
- “Nice catch on the exception type. That specificity is exactly the professional habit.”
- “You fixed the crash. Now improve the message so a real user knows what to do.”
- “Let’s shrink the `try` block to only risky lines. Smaller `try` blocks are easier to reason about.”

These prompts keep tone encouraging while still holding technical standards.

## Optional challenge prompts for fast finishers (still Basics-safe)

Only offer after required criteria are met.

1. Add a simple menu:
   - `1` Load valid file
   - `2` Load missing file
   - `3` Load corrupt file
   - `4` Quit

2. Add retry limit for numeric input (for example, max 3 attempts), then exit politely.

3. Add one extra specific catch for `PermissionError` if platform allows simulation (do not require in grading).

4. Expand summary to show whether defaults were used.

5. Add timestamp text to `error_log.txt` using plain strings (no advanced libraries required).

Reinforce:

“These are enhancements, not substitutes for specific exception handling.”

## Classroom-safe boundaries and technical guardrails

Keep this hour classroom-safe and deterministic:

- Use local files only; no external network calls.
- Use fixed filenames from this script so all learners can reproduce outputs.
- Avoid destructive file operations.
- Avoid advanced frameworks or dependency installs.
- Keep all demonstrations in plain Python standard library (`json`, `pathlib`).

If learners ask for broad architecture:

“Great question for Advanced track. For Basics, we focus on reliable and readable local exception handling patterns.”

## Quick formative checks during instruction

### Checkpoint A (after talk points)

Prompt:

“Which exception type is expected when `int('abc')` runs?”

Expected response: `ValueError`.

### Checkpoint B (after demo)

Prompt:

“If a JSON file exists but has broken syntax, which exception should we catch?”

Expected response: `json.JSONDecodeError`.

### Checkpoint C (end of lab)

Prompt:

“If your code handles only `FileNotFoundError` and `JSONDecodeError`, what happens to a typo bug?”

Expected response: It still surfaces, which helps debugging.

## Quick check / exit ticket (required by runbook)

Ask exactly:

**Why is catching a specific exception better than catching all exceptions?**

Model answer to accept:

“Specific catches handle expected errors clearly and avoid hiding unrelated bugs. Catch-all blocks can swallow important issues, making debugging harder and behavior less reliable.”

## Instructor debrief script (final 2–3 minutes)

Use this close:

“Today we moved from scripts that crash to scripts that recover. You used specific exception handling for the two most common failure points in beginner CLI apps: conversion and file parsing. You also practiced friendly feedback, continued execution, and safe defaults. That is practical software quality work.”

Then preview Session 12:

“In capstone hours, this same resilience pattern will make your project demos stable under real user mistakes.”

## Assessment rubric for this hour (lightweight)

Use this quick rubric while circulating:

- **Meets**: specific exceptions, friendly messages, program continues, valid summary output.
- **Approaching**: partial handling (only conversion or only file), some crashes remain.
- **Not yet**: broad catch-all everywhere, silent pass, or crash on first bad input.

If needed, require one final successful run with:

- one invalid numeric input,
- one missing or corrupt file,
- visible final summary output.

## Instructor troubleshooting appendix

### Issue: student cannot trigger `JSONDecodeError`

Cause: corrupt file is accidentally valid.

Fix: verify `class_settings_corrupt.json` is missing a closing brace exactly as provided.

### Issue: `FileNotFoundError` not triggered

Cause: student created the supposed missing file by accident.

Fix: delete `data/class_settings_missing.json` and rerun.

### Issue: key lookup causes crash (`KeyError`)

Cause: defaults or loaded JSON missing expected key.

Fix: use `settings.get("course_name", "Unknown Course")` in summary.

Note: `KeyError` is outside required catches for today, but this is a good defensive improvement.

### Issue: learners ask if `except Exception as e` is ever allowed

Suggested answer:

“In advanced production contexts, there are controlled cases for broader catches at system boundaries with strong logging and re-raising strategies. In Basics, we prioritize specific catches to build correct habits first.”

## Full speaking script block (optional near-verbatim delivery)

You can read this section directly if you want a smooth continuous lecture delivery.

“Team, this hour is about exception handling. Up to now, your programs worked mostly when input and files were perfect. Real users are not perfect, and files are not always perfect. Professional code must keep working when expected runtime errors happen.

First, a distinction: syntax errors versus exceptions. Syntax errors happen before your program starts. Missing colon, missing quote—Python refuses to run. `try/except` is not for that. Exceptions happen while running valid code. For example, converting text like `five` to an integer throws `ValueError`. Opening a file that does not exist throws `FileNotFoundError`. Parsing broken JSON throws `JSONDecodeError`.

Now the pattern. `try` contains risky code. `except` handles expected failures. `else` runs only when no exception occurred. `finally` always runs, success or failure.

Why do we care about specific exceptions? Because they keep intent clear and bugs visible. If I expect a conversion problem, I catch `ValueError`. If I catch everything, I can hide mistakes that I should fix, like typo bugs.

Watch this first function. We prompt for a positive integer. If conversion fails, we show a friendly message and ask again. If the number is negative or zero, that is not an exception—it is a business rule check—so we use `if` logic and continue.

Now file loading. We try opening and parsing a JSON file. If file is missing, we show a user-friendly message and continue with defaults. If JSON is corrupt, same: message plus defaults. On success, we print success in the `else` block. And in `finally`, we always print a completion line so we can see every attempt ended.

Notice what I did not do: I did not wrap the whole script in `except Exception`. I kept the risky operations local and specific.

Your lab now is to harden a starter script with the same strategy. There are two required hardening points: numeric conversion and JSON load. On error, friendly message, continue running. Specific exception catches only. At the end, your program must still print a summary.

During lab, if your program crashes on `ten` or on a missing file, you are not done yet. If your program says nothing after an error, you are not done yet. If your program catches everything broadly, you are not done yet.

Optional extension after you meet the core goal: append errors to `error_log.txt`.

Final quick check before we close: why is specific catch better than catch-all? Because it handles expected failures without masking unexpected bugs. That is how we build programs that are both user-friendly and debuggable.”

## End-of-hour checklist for instructor

Before ending, confirm:

- You explicitly taught `try/except/else/finally`.
- You explicitly covered `ValueError`, `FileNotFoundError`, `json.JSONDecodeError`.
- Live demo showed numeric input hardening + JSON file load hardening.
- Lab required specific exception handling and continue-on-error behavior.
- Students were warned against broad `Exception` and silent `pass`.
- Quick check question was asked and answered.

If all are true, Hour 44 goals are complete.
