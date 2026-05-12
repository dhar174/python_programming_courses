# Day 3, Hour 3: Context Managers and Safer File Operations

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 3, Hour 3 of 48, also Hour 11 in the Advanced runbook sequence
- **Focus**: Using context managers consistently and saving JSON data with a write-temp-then-replace pattern so tracker files are less likely to be corrupted.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 3, Hour 11.
- **Prerequisites**: Learners should have completed Day 3 Hour 1 and Day 3 Hour 2 or have an equivalent project shape: `project_root/src/tracker/` contains package code, the demo runs from the project root, and logging can write to `logs/app.log`.
- **Advanced trajectory**: This hour stays on the PCAP-to-PCPP1 path. Learners are not building a database transaction system, cloud storage layer, full repository pattern, or production-grade crash recovery. The advanced step is learning a professional file-writing habit: write the new content somewhere temporary, close it, then replace the original.
- **Instructor goal**: By the end of this hour, every learner can implement `save_json_safe(path, data)`, save tracker-style JSON data to `data/tasks.json`, simulate a concrete failure, and explain why the original file is safer than it would be with a direct overwrite.

Important instructor positioning:

- Continue the Day 3 execution convention. Source code lives in `src/tracker/`. Data can live in `data/tasks.json`. Logs can live in `logs/app.log`.
- Use consistent vocabulary: `Task`, `TaskService`, `to_dict()`, `data/tasks.json`, `logs/app.log`, and `src/tracker/`. If learners use different names, ask them to preserve the responsibilities rather than copy names mechanically.
- Keep the hour practical. We are not deep-diving into filesystem internals, `fsync`, database transactions, file locking APIs, advanced `tempfile` patterns, or cloud storage consistency.
- Be honest about the phrase **atomic-ish**. The write-temp-then-replace pattern protects against many application-level failures and exceptions before replacement. It is not a perfect guarantee against power loss, OS crashes, unusual filesystem behavior, or every network drive edge case.
- On Windows, mention that `Path.replace()` can fail if the destination file is open or locked by another process, such as an editor, preview pane, antivirus scanner, sync tool, or spreadsheet application.
- Make the failure simulation concrete. Do not say "raise after JSON starts to serialize" if the code uses one `json.dump()` call. Show a naive unsafe partial write separately, and use a safe helper with `simulate_failure=True` that raises after the temporary file is written but before replacement.
- Prefer simple cleanup. The reference helper removes the temporary file in the exception path with `tmp_path.unlink(missing_ok=True)` so students do not collect stale `.tmp` files during practice.

---

## Timing Overview

| Segment | Time | Purpose |
| --- | ---: | --- |
| Opening bridge from logging | 5 min | Connect Day 3 Hour 2 logging to preventing damaged data before it happens |
| Outcomes, setup, and vocabulary | 8 min | Define context manager, resource cleanup, target path, temp path, replace, and atomic-ish save |
| Concept briefing: `with`, paths, and direct-write risk | 10 min | Explain why `with` matters beyond files and why direct overwrites can corrupt good data |
| Live demo: write JSON to temp, then replace | 8 min | Build and run `save_json_safe()` with `pathlib`, cleanup, failure simulation, and Windows notes |
| Guided lab: safe save utility for tracker data | 25 min | Learners implement the helper, save tracker data, simulate failure, and verify file state |
| Quick checks, pitfalls, and wrap-up | 4 min | Confirm understanding, review common learner situations, and bridge to decorators |

This is a one-hour plan. The timed teaching headings total exactly 60 minutes: 5 + 8 + 10 + 8 + 25 + 4. The guided lab is 25 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If discussion runs long, shorten the concept examples rather than shrinking the student practice. The required outcome is practical: saves use `with` plus a temp-replace pattern, and the original file is not left half-written after the simulated failure.

---

## Learning Outcomes

By the end of this hour, learners will be able to:

1. Explain what a context manager does: setup on entry, cleanup on exit, including cleanup when an exception occurs.
2. Use `with` consistently when writing files so file handles are closed predictably.
3. Explain why context managers matter beyond ordinary files, including locks, connections, temporary resources, and other setup/cleanup pairs.
4. Use `pathlib.Path` to build and inspect paths such as `data/tasks.json` without fragile string concatenation.
5. Describe why opening a good JSON file directly in write mode can destroy it before new content is safely written.
6. Implement `save_json_safe(path, data)` using a same-directory temporary file and `Path.replace()`.
7. Use `json.dump(..., indent=2)` inside a `with` block and write a trailing newline for readable JSON output.
8. Clean up temporary files if a write or pre-replace step fails.
9. Simulate a failure and verify that the original target file still contains the previous valid data.
10. Explain the honest caveat: write-temp-then-replace is safer than direct overwrite, but it is not a full durability guarantee against every possible machine or filesystem failure.
11. Identify common pitfalls: overwriting a good file with bad data, assuming the working directory is stable, trying to dump custom objects directly, leaving stale `.tmp` files, and keeping the target file open in another program on Windows.
12. Recognize that deeper integration into `TaskService` or a persistence layer is useful but optional today; the required lab can be completed as a standalone helper.

---

## Instructor Prep Before Class

Before learners arrive, complete this checklist:

- Keep the runbook section for Session 3, Hour 11 visible. The required scope is context managers and safer file operations. The required lab is `save_json_safe(path, data)`, saving tracker data to JSON, simulating failure, and discussing what can go wrong without safe saves.
- Open the Day 3 Hour 2 logging lesson or your notes from it. The bridge sentence is: "Logging tells us what happened; safer file operations reduce the chance that a bad save damages data in the first place."
- Prepare a small working directory or demo folder with no important files in it. If you are demoing inside a learner project, use `data/tasks.json`, not a real production file.
- Decide how you will show file contents. In an editor, open `data/tasks.json`. In PowerShell, you can use:

```powershell
Get-Content data/tasks.json
```

- Prepare this board note:

```text
Safe save pattern:
1. Build target path.
2. Build temp path in the same directory.
3. Write JSON to temp with with.
4. Close temp successfully.
5. Replace target with temp.
```

- Prepare a second board note:

```text
with manages cleanup.
Temp-then-replace protects the good target.
They solve different parts of the problem.
```

- Prepare to demonstrate both paths:
  - unsafe direct write that leaves `data/tasks.json` broken
  - safe helper with `simulate_failure=True` that leaves the previous `data/tasks.json` untouched
- If using Windows, close any editor preview or file viewer that may lock `data/tasks.json` before calling `Path.replace()`. Tell learners that a locked destination can cause `PermissionError`.
- If a learner asks about `tempfile.NamedTemporaryFile`, acknowledge that it exists and is useful, but keep the class on the simple same-directory `.tmp` naming pattern today. That pattern is readable, testable, and enough for the runbook goal.

---

## Opening Bridge from Logging (5 minutes)

### Instructor talk track

"Welcome back. In the previous hour, we added logging and error reporting. We made the program better at telling developers what happened. A good log file can tell us that a save failed, which task was being processed, and what exception was raised."

"That is useful, but logging does not undo damage. If a program corrupts `data/tasks.json`, a log entry may help us diagnose the problem, but the user's data may already be broken."

Display:

```text
Logging tells us what happened.
Safe file operations reduce the chance of corrupting data in the first place.
```

"That is today's bridge. Last hour was about visibility after events happen. This hour is about safer habits before and during file writes."

"You have already used `with open(...)` in earlier Python work. Many learners remember the phrase 'it closes the file automatically.' That is true, but today we need a stronger mental model. A context manager is about reliable setup and reliable cleanup. Closing a file is one example. Releasing a lock, closing a network connection, cleaning up a temporary resource, or restoring a setting can all follow the same pattern."

"Then we will combine that idea with a safer save pattern. The pattern is simple enough to remember: write the new JSON to a temporary file first. If that succeeds, replace the original. If something fails before replacement, the old file is still there."

Pause and ask:

"If your tracker already has a `data/tasks.json` file with good tasks in it, what is the worst thing that could happen if we open that file directly in write mode and then crash halfway through?"

Take two or three answers. Guide learners toward "the original file may already be truncated or partly overwritten."

"Exactly. We are not trying to make file saving scary. We are trying to make it responsible."

### Transition

"Let's name the vocabulary for this hour, then we will look at a concrete direct-write failure and a safer replacement pattern."

---

## Outcomes, Setup, and Vocabulary (8 minutes)

### Instructor talk track

"By the end of this hour, you should be able to write a helper like this and explain every line of it."

Display:

```python
save_json_safe("data/tasks.json", tracker_data)
```

"The helper will accept a path and serializable data. Serializable means the data can be converted to JSON. A list of dictionaries is serializable. A dictionary containing strings, numbers, booleans, lists, and other dictionaries is serializable. A custom `Task` object is usually not serializable directly. For custom objects, use a method like `to_dict()` first."

"Here is the vocabulary."

"A **context manager** is an object used with `with`. It has entry behavior and exit behavior. For a file, entry means 'open the file and give me a file object.' Exit means 'close the file even if the block ends because of an exception.'"

Display:

```python
with Path("data/tasks.json").open("w", encoding="utf-8") as file:
    file.write("example")
```

"A **target path** is the file we ultimately want to update. In our tracker, that might be `data/tasks.json`."

"A **temporary path** is a side file where we write the new content first. For `data/tasks.json`, our temp path will be `data/tasks.json.tmp`. For a target path with no suffix, such as `tasks`, our temp path will be `tasks.tmp`. That detail matters because suffix logic can surprise people."

"A **replace** operation means the temp file becomes the real file. In `pathlib`, we can call `tmp_path.replace(target_path)`."

"The phrase **atomic-ish save** means we are trying to make the visible update happen in a single replacement step after the data has already been written. It is safer than direct overwrite. But I want to be precise: this is not a promise against every power loss, OS crash, sync tool conflict, or unusual filesystem. We are not teaching full durability engineering today. We are teaching a better application-level habit."

Display:

```text
Direct overwrite:
    open real file in write mode -> old content may be gone immediately

Temp-then-replace:
    write side file -> replace real file only after success
```

"One more vocabulary phrase: **working directory**. Relative paths like `data/tasks.json` are interpreted relative to the process's current working directory, not necessarily the file where your code lives. In this course, we run from the project root. That makes `data/tasks.json`, `logs/app.log`, and `python -m src.tracker.demo` line up predictably. If you run from inside `src/tracker/`, those same relative paths can point somewhere else or fail."

### Instructor check for understanding

Ask:

"What does `with` help with: choosing the filename, closing the resource, or converting objects to JSON?"

Expected answer:

"Closing the resource or performing cleanup. It does not choose paths or serialize custom objects by itself."

Ask:

"If `Task` is a custom object, what do we usually need before JSON?"

Expected answer:

"Convert it to plain data, often with `to_dict()`."

### Transition

"Now let's make the risk visible. We will start with the unsafe version on purpose."

---

## Concept Briefing: `with`, Paths, and Direct-Write Risk (10 minutes)

### Part 1: What `with` gives us

**Instructor talk track**

"Many Python examples teach files like this."

```python
file = open("data/tasks.json", "w", encoding="utf-8")
file.write("example")
file.close()
```

"That code depends on us reaching `file.close()`. If an exception happens before that line, cleanup becomes unreliable unless we write extra `try`/`finally` code. The `with` statement gives us a cleaner pattern."

```python
from pathlib import Path

path = Path("data/tasks.json")

with path.open("w", encoding="utf-8") as file:
    file.write("example")
```

"When the block ends, Python asks the context manager to clean up. For a file object, that means close the file. That is true whether the block ends normally or because an exception was raised."

"That idea shows up beyond ordinary files. We might use context managers for database connections, locks around shared resources, temporary directories, captured output, network sessions, or testing helpers that temporarily change state. The shared idea is not 'files are special.' The shared idea is 'enter a controlled context, do work, leave the context cleanly.'"

Display:

```text
Context manager mental model:
enter -> work -> exit cleanup
```

"However, `with` alone does not make direct overwrites safe. It closes the file handle, but if we opened the real target in write mode, the real target may already have been truncated."

### Part 2: Why direct writes can corrupt useful data

**Instructor talk track**

"Let's imagine `data/tasks.json` currently contains good data."

```json
[
  {
    "task_id": 1,
    "title": "Draft project plan",
    "is_complete": false
  }
]
```

"Now we do this."

```python
from pathlib import Path

target_path = Path("data/tasks.json")

with target_path.open("w", encoding="utf-8") as file:
    file.write("[\n")
    file.write('  {"task_id": 2, "title": "Broken save"')
    raise RuntimeError("simulated crash during direct write")
```

"This is a deliberately unsafe demonstration. We open the real target path in write mode. On many systems, that truncates the file immediately. Then we write only part of the JSON and raise an exception. The result is not the old good file. The result may be a half-written file that is no longer valid JSON."

"Notice the key point: using `with` did not prevent this corruption. The file is closed cleanly, but it is closed after we damaged the target. `with` solved cleanup. It did not solve the save strategy."

### Part 3: The safer pattern in plain English

**Instructor talk track**

"The safer pattern changes which file is at risk during the write. Instead of writing directly to `data/tasks.json`, we write to `data/tasks.json.tmp`."

Display:

```text
1. Make sure data/ exists.
2. Write the complete JSON to data/tasks.json.tmp.
3. Close the temp file.
4. Replace data/tasks.json with data/tasks.json.tmp.
```

"If something fails while writing the temp file, the target file is still the old one. If something fails after the temp file is written but before replacement, the target file is still the old one. That is much better than destroying the target first and hoping the rest works."

"This is why we want the temp file in the same directory. It keeps the operation simple and predictable. The original and the temp live beside each other. We are not scattering temporary output into a different unknown folder."

### Part 4: Working directory warning

**Instructor talk track**

"One common pitfall is assuming the working directory is stable. If we run from the project root, `Path('data/tasks.json')` means this."

```text
project_root/
    data/
        tasks.json
```

"If we run from a different directory, the same relative path can point somewhere else. That is why our course keeps saying: run package demos from the project root with `python -m src.tracker.demo` or, on Windows, `py -m src.tracker.demo`."

"You can also print `Path.cwd()` while debugging path confusion. Do not leave noisy debug prints everywhere; use them as a temporary diagnostic."

### Transition

"Now I will code the helper. Watch the order: target path, temp path, write with `with`, optional simulated failure, replace, cleanup on exception."

---

## Live Demo: Write JSON to Temp, Then Replace (8 minutes)

### Demo framing

**Instructor talk track**

"In the demo, I am going to use plain tracker-style dictionaries. If your project already has `Task` objects, you would call `task.to_dict()` first. I am keeping the demo focused on file safety, not rebuilding the service layer."

"First, here is a small data set."

```python
tasks = [
    {
        "task_id": 1,
        "title": "Write logging summary",
        "is_complete": True,
    },
    {
        "task_id": 2,
        "title": "Save tracker data safely",
        "is_complete": False,
    },
]
```

### Live-code the helper

Type or display the following code:

```python
import json
from pathlib import Path
from typing import Any


def save_json_safe(
    path: str | Path,
    data: Any,
    *,
    simulate_failure: bool = False,
) -> None:
    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = target_path.with_name(f"{target_path.name}.tmp")

    try:
        with tmp_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
            file.write("\n")

        if simulate_failure:
            raise RuntimeError("simulated failure before replace")

        tmp_path.replace(target_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise
```

### Narrate each important line

**Instructor talk track**

"`Path(path)` lets the caller pass either a string like `'data/tasks.json'` or an existing `Path` object."

"`target_path.parent.mkdir(parents=True, exist_ok=True)` creates the destination directory if it does not already exist. If the target is just `'tasks.json'`, the parent is the current directory, represented by `.`. Calling `mkdir` with `exist_ok=True` is harmless there."

"`tmp_path = target_path.with_name(f'{target_path.name}.tmp')` means the temp file sits in the same directory as the target. For `data/tasks.json`, this becomes `data/tasks.json.tmp`. For `tasks`, this becomes `tasks.tmp`. This avoids a common bug where suffix-based code behaves oddly for files with no suffix."

"The `with` block writes the JSON and closes the temp file. Closing matters because we want the data finished before replacement."

"The `simulate_failure` flag is only for teaching and testing. It raises after the temp file has been written but before `replace()`. That lets us prove the target remains safe if a failure happens before the final replacement."

"`tmp_path.replace(target_path)` replaces the target with the temp file. On Windows, this can fail if the target is locked by another process. If a learner gets `PermissionError`, ask whether the JSON file is open in an editor preview, spreadsheet app, or sync tool."

"The `except` block removes the temp file and then re-raises the exception. We do not silently hide save failures. We clean up and let the caller decide how to report or log the problem."

### Run the normal save

Type:

```python
save_json_safe("data/tasks.json", tasks)
```

Then show the file:

```powershell
Get-Content data/tasks.json
```

Expected content shape:

```json
[
  {
    "task_id": 1,
    "title": "Write logging summary",
    "is_complete": true
  },
  {
    "task_id": 2,
    "title": "Save tracker data safely",
    "is_complete": false
  }
]
```

### Run the simulated failure

Type:

```python
original_text = Path("data/tasks.json").read_text(encoding="utf-8")

try:
    save_json_safe(
        "data/tasks.json",
        [{"task_id": 999, "title": "This should not replace the file"}],
        simulate_failure=True,
    )
except RuntimeError as error:
    print(f"Caught expected failure: {error}")

after_text = Path("data/tasks.json").read_text(encoding="utf-8")
print(after_text == original_text)
print(Path("data/tasks.json.tmp").exists())
```

Expected output:

```text
Caught expected failure: simulated failure before replace
True
False
```

**Instructor talk track**

"The `True` tells us the original file content did not change. The `False` tells us the temp file was cleaned up. This is the concrete proof we wanted."

"Now compare that with the unsafe partial-write demonstration. In the unsafe version, the target itself was the file being damaged. In the safe version, the target is not touched until the final replace step."

### Optional demo: path with no suffix

If time permits, run:

```python
save_json_safe("tasks", {"status": "works without a suffix"})
print(Path("tasks").read_text(encoding="utf-8"))
Path("tasks").unlink(missing_ok=True)
```

**Instructor talk track**

"This is a sanity check for our temp naming. The target `'tasks'` becomes temp `'tasks.tmp'`, not an empty or surprising path."

### Transition

"Now you will implement the helper yourself. The goal is not to memorize my exact variable names. The goal is to preserve the order of operations and prove the target stays safe."

---

## Guided Lab: Safe Save Utility for Tracker Data (25 minutes)

### Lab purpose

**Instructor talk track**

"Your lab is to build a safe save helper and use it with tracker-style data. This can be standalone today. If your service layer is ready, you may integrate it lightly. If your service layer is not ready, do not derail the hour by restructuring everything. Save a list of dictionaries first."

"The required result is a helper that uses `with`, writes to a temp file, replaces only after success, and leaves no half-written target after a simulated failure."

### Student prompt

Create or update a small file in your project, such as `src/tracker/storage.py` or a temporary demo module used only for this exercise. Implement:

```python
save_json_safe(path, data)
```

Then use it to save tracker data to:

```text
data/tasks.json
```

Your tracker data may come from:

- a list of plain dictionaries
- a list like `[task.to_dict() for task in service.list_tasks()]`
- a small hard-coded sample if your service layer is not ready

### Lab timing checklist

| Lab step | Suggested time | Done when |
| --- | ---: | --- |
| Create sample tracker data | 4 min | Learner has a list of dictionaries or data from `to_dict()` |
| Implement `save_json_safe()` | 8 min | Helper creates parent directory, temp path, `with` block, JSON dump, replace |
| Run normal save | 4 min | `data/tasks.json` exists and contains readable JSON |
| Simulate failure | 5 min | Learner proves old target remains unchanged and temp is cleaned up |
| Reflect and optionally integrate | 4 min | Learner can explain the pattern; stretch learners connect it to `TaskService` or logging |

### Starter code

Offer this if learners need scaffolding:

```python
import json
from pathlib import Path
from typing import Any


def save_json_safe(
    path: str | Path,
    data: Any,
    *,
    simulate_failure: bool = False,
) -> None:
    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = target_path.with_name(f"{target_path.name}.tmp")

    try:
        with tmp_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
            file.write("\n")

        if simulate_failure:
            raise RuntimeError("simulated failure before replace")

        tmp_path.replace(target_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


sample_tasks = [
    {
        "task_id": 1,
        "title": "Review logs/app.log",
        "is_complete": True,
    },
    {
        "task_id": 2,
        "title": "Save data/tasks.json safely",
        "is_complete": False,
    },
]

save_json_safe("data/tasks.json", sample_tasks)
```

### If using existing `TaskService`

For learners who are ready, show this adaptation:

```python
tracker_data = [task.to_dict() for task in service.list_tasks()]
save_json_safe("data/tasks.json", tracker_data)
```

**Instructor note**

Keep this as an adaptation, not a requirement. Some learners may have `get_all_tasks()`, `list_items()`, or a property instead of `list_tasks()`. The concept is: convert domain objects to plain dictionaries before JSON.

### Concrete unsafe failure simulation

Ask learners to create a known good file first:

```python
save_json_safe(
    "data/tasks.json",
    [{"task_id": 1, "title": "Original good task", "is_complete": False}],
)
```

Then show the unsafe direct-write example separately:

```python
from pathlib import Path

target_path = Path("data/tasks.json")

try:
    with target_path.open("w", encoding="utf-8") as file:
        file.write("[\n")
        file.write('  {"task_id": 2, "title": "Half-written task"')
        raise RuntimeError("simulated failure during direct write")
except RuntimeError as error:
    print(f"Caught expected direct-write failure: {error}")

print(target_path.read_text(encoding="utf-8"))
```

Discuss:

- The target file was opened directly.
- The original good content was not protected.
- The file is now invalid or incomplete JSON.
- The `with` block closed the file, but closing a damaged file does not restore the previous content.

Then reset the file to good data:

```python
save_json_safe(
    "data/tasks.json",
    [{"task_id": 1, "title": "Original good task", "is_complete": False}],
)
```

Now run the safe simulated failure:

```python
before = Path("data/tasks.json").read_text(encoding="utf-8")

try:
    save_json_safe(
        "data/tasks.json",
        [{"task_id": 3, "title": "Should not replace original"}],
        simulate_failure=True,
    )
except RuntimeError as error:
    print(f"Caught expected safe-save failure: {error}")

after = Path("data/tasks.json").read_text(encoding="utf-8")
print(before == after)
print(Path("data/tasks.json.tmp").exists())
```

Expected result:

```text
Caught expected safe-save failure: simulated failure before replace
True
False
```

### Completion criteria

Learners are done when:

- `save_json_safe(path, data)` accepts a string or `Path`.
- The helper uses `Path(path)` and avoids fragile manual path concatenation.
- The parent directory is created with `mkdir(parents=True, exist_ok=True)`.
- The helper writes JSON to a temp file in the same directory as the target.
- The JSON write happens inside a `with` block.
- The helper replaces the target only after the temp write completes.
- The helper cleans up the temp file if an exception occurs before replacement.
- Normal save creates or updates `data/tasks.json`.
- Simulated failure leaves the original target content unchanged.
- The learner can answer: "What is one advantage of writing to a temp file first?"

### Common learner situations and coaching responses

| Situation | Coaching response |
| --- | --- |
| Learner writes directly to `data/tasks.json` | Ask: "What file is at risk if an exception happens after the first write?" Then redirect to temp first. |
| Learner uses `open()` without `with` | Ask them to rewrite it with a context manager. The goal is reliable cleanup without manual close calls. |
| Learner dumps `Task` objects directly | Remind them JSON understands plain data, not arbitrary Python objects. Use `to_dict()` first. |
| Learner creates temp file in a different folder | Keep it beside the target for today's pattern. It is easier to reason about and avoids cross-location confusion. |
| Learner uses suffix logic that breaks for `tasks` | Suggest `target_path.with_name(f"{target_path.name}.tmp")`; it works for both `tasks.json` and `tasks`. |
| Learner sees `PermissionError` on Windows | Check whether the target is open or locked in another process. Close editor preview panes, spreadsheet views, or sync conflicts. |
| Learner assumes `data/tasks.json` is always under the project root | Ask them to print `Path.cwd()` and run from the project root with `python -m src.tracker.demo`. |
| Learner wants to build a full persistence architecture | Affirm the instinct, then keep the required lab standalone. Mark service-layer integration as stretch. |
| Learner asks if this is perfectly atomic | Use the honest caveat: it protects many application-level failures but not every power loss, OS crash, or filesystem edge case. |

### Stretch options if learners finish early

Choose one, not all:

1. Add a timestamped backup before replacement.
2. Add a `load_json(path)` helper that returns an empty list if the file does not exist and raises a clear error for invalid JSON.
3. Log successful saves and failed saves to `logs/app.log` using the previous hour's logging pattern.
4. Connect `save_json_safe()` to a small `TaskService.save()` method while keeping object-to-dictionary conversion explicit.

For the timestamped backup, use a simple pattern:

```python
from datetime import datetime
from pathlib import Path
import shutil


def backup_existing_file(target_path: Path) -> None:
    if not target_path.exists():
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = target_path.with_name(
        f"{target_path.stem}_{timestamp}{target_path.suffix}.bak"
    )
    shutil.copy2(target_path, backup_path)
```

**Instructor note**

This extension should happen before `tmp_path.replace(target_path)`, after the temp write succeeds. Keep it optional. Do not let backup naming consume the main lab.

---

## Quick Checks, Pitfalls, and Wrap-Up (4 minutes)

### Quick checks

Ask these aloud:

1. "What is one advantage of writing to a temp file first?"
2. "Does `with` alone prevent a target file from being half-overwritten?"
3. "Why do we usually convert `Task` objects with `to_dict()` before JSON?"
4. "What can cause `Path.replace()` to fail on Windows?"

Expected answers:

1. "If the write fails before replacement, the original good file can remain unchanged."
2. "No. `with` closes the file, but it does not change the fact that direct write mode may have truncated the target."
3. "JSON needs plain serializable data such as dictionaries, lists, strings, numbers, booleans, and `None`."
4. "The destination file may be open or locked by another process, such as an editor previewing the JSON file."

### Common pitfalls to restate

- **Overwriting a good file with bad data**: Directly opening `data/tasks.json` in write mode puts the trusted file at risk immediately.
- **Assuming working directory is stable**: Relative paths depend on where the process starts. For this course, run from the project root.
- **Thinking `with` solves every save problem**: `with` handles cleanup; temp-then-replace handles the save strategy.
- **Leaving stale `.tmp` files**: Clean up temp files in an exception path when the code stays readable.
- **Overstating atomicity**: Say "atomic-ish" or "safer," not "impossible to corrupt under all conditions."
- **Over-integrating too soon**: The helper can be standalone today. Deeper service-layer persistence is optional or a future step.

### Wrap-up talk track

"Today we added a small but professional habit. We did not build a database. We did not build a full storage architecture. We learned a safer way to write files that matter."

"The two ideas are connected but different. `with` helps resources clean themselves up. The temp-then-replace pattern protects the target file from being the thing we damage while we are still generating new content."

"If you remember one sentence, remember this:"

```text
Write the new file completely first; replace the old file only after success.
```

"In the next hour, we will move from file safety into decorators. Decorators let us wrap repeated behavior around functions, such as timing, validation, or simple authorization checks, without copying the same setup and cleanup logic everywhere. The same professional theme continues: keep repeated infrastructure behavior clean, visible, and reusable."

---

## Instructor Reference Solution

Use this solution as the instructor's answer key. It is intentionally small and standalone. It can live in `src/tracker/storage.py`, a demo file, or a notebook cell for the lab. If placed inside a package module, keep imports consistent with the Day 3 package structure.

```python
import json
from pathlib import Path
from typing import Any


def save_json_safe(
    path: str | Path,
    data: Any,
    *,
    simulate_failure: bool = False,
) -> None:
    """Save JSON data using a temp file and replace pattern.

    The simulate_failure flag is for teaching and tests. It raises after the
    temp file is written but before the target file is replaced.
    """
    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = target_path.with_name(f"{target_path.name}.tmp")

    try:
        with tmp_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
            file.write("\n")

        if simulate_failure:
            raise RuntimeError("simulated failure before replace")

        tmp_path.replace(target_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def demo() -> None:
    tasks = [
        {
            "task_id": 1,
            "title": "Review logs/app.log",
            "is_complete": True,
        },
        {
            "task_id": 2,
            "title": "Save data/tasks.json safely",
            "is_complete": False,
        },
    ]

    save_json_safe("data/tasks.json", tasks)
    original_text = Path("data/tasks.json").read_text(encoding="utf-8")

    try:
        save_json_safe(
            "data/tasks.json",
            [{"task_id": 999, "title": "Should not replace the file"}],
            simulate_failure=True,
        )
    except RuntimeError as error:
        print(f"Caught expected failure: {error}")

    after_text = Path("data/tasks.json").read_text(encoding="utf-8")
    print(after_text == original_text)
    print(Path("data/tasks.json.tmp").exists())

    save_json_safe("tasks", {"status": "works without a suffix"})
    print(Path("tasks").read_text(encoding="utf-8"))
    Path("tasks").unlink(missing_ok=True)


if __name__ == "__main__":
    demo()
```

Expected key results:

- A normal call to `save_json_safe("data/tasks.json", tasks)` creates readable JSON.
- A simulated failure raises `RuntimeError`, leaves `data/tasks.json` unchanged, and removes `data/tasks.json.tmp`.
- A call to `save_json_safe("tasks", {"status": "works without a suffix"})` works and uses a temp file named `tasks.tmp` internally.

Reference explanation for the exit ticket:

"Writing to a temp file first means the existing good file is not touched until the new content has been written successfully. If the write fails before replacement, the old file can remain intact instead of being left half-written."
