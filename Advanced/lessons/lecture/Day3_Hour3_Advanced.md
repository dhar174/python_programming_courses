# Advanced Day 3, Hour 3: Context Managers + Safer File Operations

## Learning Objectives
- Employ the `with` statement for consistent context management beyond just file reading.
- Develop "atomic" or safe save patterns to avoid data corruption.

## Instructor Script & Talk Points

**(10–20 min)**

We've used `with open(...)` to handle reading lines from a text file, which is called a *context manager*. Context managers guarantee that resource cleanup (like closing a file, closing a database connection, or releasing a lock) triggers automatically—even if an exception crashes your program in the middle.

**Why `with` Matters Beyond Files:**
While managing generic file objects is its most famous use case, context managers are incredibly versatile. You can write your own context managers to suppress logs, switch database connections, or benchmark code execution blocks.

**Atomic-ish Saves:**
A common pitfall is overwriting an existing good file. If your program reads `data.json`, begins writing new content directly to `data.json`, and then suddenly crashes mid-write due to a typo or power failure... your original `data.json` is partially overwritten and corrupted. 

To fix this, we use an atomic-style safe save pattern:
1. Write our updated file to a temporary location (like `data.json.tmp`).
2. Close the temporary file.
3. Replace the original file with the newly written temp file programmatically using `pathlib` or `os.replace`.

This guarantees that if the write fails midway, the original target file remains untouched and safe.

## Live Demo

**(5–10 min)**

*Instructor Notes:*
1. Start by making a fake `data.json` file.
2. Demonstrate how to write to `data.json.tmp` iteratively.
3. Once the temporary file is flushed and closed, import `os` or `pathlib.Path` to `replace` the real file with the temp file.
4. Intentionally raise a generic exception midway through writing `data.json.tmp` to show that the real `data.json` remained complete and uncorrupted.

## Practice Activity (Lab)

**(25–35 min)**

**Lab: Safe Save Utility**

1. Write a new standalone utility function called `save_json_safe(path, data)`.
2. This function should write the dictionary `data` to a temporary JSON file (append `.tmp` to the path) using `with open(...)` securely.
3. Make the function seamlessly `replace` the primary file with the `.tmp` file using the `os` standard library if the write succeeds.
4. Hook up `save_json_safe(...)` into your Capstone's service layer to securely serialize your tracker data back into JSON.
5. Simulate a failure by throwing `raise Exception("Simulated Failure")` right after the data starts to serialize. Check your file to ensure it was kept entirely whole.

**Optional Extension:**
Whenever you call `save_json_safe`, quickly parse the timestamp and copy the original `data.json` over to a new file named like `data_20260101_1350.json.bak` *before* the overwrite occurs, creating a rolling backup log.

**Completion Criteria:**
- The utility properly writes a `.tmp` file, using `with` statements effectively.
- Files aren't left half-written. The overwrite logic successfully executes safely.
# Day 3, Hour 3: Context Managers + Safer File Operations
**Python Programming Advanced - Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap and transition from logging: 5 minutes
- Why `with` matters beyond "closing a file": 12 minutes
- Safe save patterns and file corruption thinking: 13 minutes
- Live demo (`save_json_safe` with `pathlib`): 10 minutes
- Hands-on lab (safe save utility): 15 minutes
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Explain what a context manager does in practical terms
2. Use `with` consistently for safer resource handling
3. Describe why naive file writes can leave half-written or corrupted output
4. Implement a write-temp-then-replace pattern for JSON saves
5. Use `pathlib` to make file paths easier to reason about
6. Distinguish between a convenient save and a safer save
7. Prepare your project for persistence work without teaching bad habits

---

## Section 1: Recap and Framing (5 minutes)

**(5 min)**

**Quick Check:** What is the primary advantage of writing to a temporary file *first* when saving data?

*Expected answer:* If an error occurs halfway through generating the new file, your current pristine data is not truncated, damaged, or entirely lost. You are replacing the file purely instantly only after the operation finishes completely.
### Why This Hour Follows Logging

**[Instructor speaks:]**

Last hour we taught the program how to tell developers what happened. This hour we teach the program how to avoid creating one very common class of problems in the first place: damaged or partial files.

As soon as student projects start saving JSON, reports, or exported data, file handling becomes a real concern. If saving is sloppy, one bug or interruption can destroy perfectly good data.

### The Big Idea

**[Instructor speaks:]**

The simplest version of file writing feels innocent:

```python
with open("tasks.json", "w") as file:
    file.write(json_text)
```

That is already better than forgetting to close the file manually. But we can still do better when the data matters.

The pattern for today is:

1. write new content to a temporary file
2. finish the write successfully
3. replace the original file

This reduces the risk of leaving a half-written file behind if something goes wrong.

---

## Section 2: Context Managers in Practical Terms (12 minutes)

### What `with` Really Means

**[Instructor speaks:]**

Students often memorize that `with open(...)` closes the file automatically. True, but incomplete.

A context manager means:

- setup happens on entry
- cleanup happens on exit
- cleanup still happens even if an exception occurs

That is the real mental model.

Yes, files are the most common beginner example. But the pattern generalizes:

- files
- locks
- database connections
- temporary resources

Today we stay grounded in file operations, because that is where the value is immediately visible.

### Why Naive Saves Are Risky

**[Instructor speaks:]**

Suppose you directly open the real data file in write mode and start writing new JSON. What if one of these happens in the middle?

- the process crashes
- an exception is raised
- the disk write is interrupted
- the program writes bad data after truncating the original file

You can end up replacing a good file with a broken one.

That is why I call the safer pattern "atomic-ish." It is not magic perfection in every environment, but it is far safer than rewriting the real file directly from the first byte.

### `pathlib` Helps, Too

**[Instructor speaks:]**

Students also benefit from `pathlib` because paths become objects with readable operations:

```python
from pathlib import Path

data_file = Path("data") / "tasks.json"
```

That is easier to read and compose than a pile of string concatenation.

We are trying to build habits that scale without becoming obscure.

---

## Section 3: Safe Save Pattern Thinking (13 minutes)

### The Pattern in Plain English

**[Instructor speaks:]**

I want students to hear the save algorithm before they code it:

1. figure out the real target path
2. make sure the parent directory exists
3. build a temp filename in the same directory
4. write the new content to the temp file
5. only after success, replace the original file

That order matters.

### Why Same-Directory Temp Files Help

**[Instructor speaks:]**

Using the same directory for the temp file keeps the replace step more predictable. It also keeps your mental model simple:

- original file lives here
- temp file lives right next to it
- successful write becomes replacement

### Failure Simulation as a Teaching Tool

**[Instructor speaks:]**

One of the strongest things you can do in this hour is simulate a failure on purpose.

Students remember safe-save patterns better when they see what can go wrong without them.

For example:

- write half the JSON
- raise an exception
- compare the file state when using direct write vs temp-replace

That makes the danger concrete instead of theoretical.

---

## Section 4: Live Demo - `save_json_safe(path, data)` (10 minutes)

### Demo Setup

**[Instructor speaks:]**

In this demo, I will write a helper that saves tracker data safely. Focus on the order of operations.

```python
import json
from pathlib import Path


def save_json_safe(path: str | Path, data: list[dict]) -> None:
    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = target_path.with_suffix(target_path.suffix + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")

    temp_path.replace(target_path)


tasks = [
    {
        "task_id": 1,
        "title": "Write outline",
        "priority": "high",
        "is_complete": False,
    },
    {
        "task_id": 2,
        "title": "Book room",
        "priority": "medium",
        "is_complete": True,
    },
]

save_json_safe("data/tasks.json", tasks)
```

### Demo Narration

**[Instructor speaks:]**

Notice what we did **not** do. We did not open the real target file immediately in write mode and hope for the best.

We wrote to a temporary file first. Only after the write finished cleanly did we replace the target.

This pattern protects the existing file from being destroyed by a half-complete write.

### Failure Simulation Discussion

**[Instructor speaks:]**

Now imagine a naive version:

```python
with open("data/tasks.json", "w", encoding="utf-8") as file:
    file.write("{")
    raise RuntimeError("simulated failure")
```

What happens? The original file is already being overwritten. That is exactly the situation we want to avoid.

With a temp file, the broken write damages the temp file instead of the trusted original.

### Teaching Notes During the Demo

- Show the `data/` directory before and after the save.
- Emphasize that `with` guarantees cleanup behavior around the file handle.
- Explain that path objects make code more readable than manual string paths.
- Remind students not to assume the working directory is always what they think it is.

---

## Section 5: Hands-On Lab - Safe Save Utility (15 minutes)

### Lab Framing

**[Instructor speaks:]**

Your task is to give your tracker project a save path that is safer than a naive overwrite.

Even if your project does not have real persistence yet, build the helper now. Future-you will be grateful when Session 7 and beyond arrive.

### Student Task

1. Create a helper named something like `save_json_safe`.
2. Accept a path and plain serializable data.
3. Use `pathlib`.
4. Write to a temp file first.
5. Replace the original only after the temp write succeeds.
6. If time allows, simulate a failure and explain why the safe pattern is better.

### Suggested Starter Shape

```python
import json
from pathlib import Path


def save_json_safe(path, data):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + ".tmp")

    with temp.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")

    temp.replace(target)
```

### Completion Criteria

Students are done when:

- saves use `with` and the safe temp-replace pattern
- the target file ends up fully written
- the helper works with a realistic tracker data structure
- students can explain why this is safer than writing directly to the target file

### Circulation Notes

- If a student is still using string path concatenation everywhere, introduce `Path`.
- If a student writes directly to the target file, ask what happens if the program crashes halfway through.
- If a student forgets to ensure the parent directory exists, help them add `mkdir(parents=True, exist_ok=True)`.
- If a student tries to dump custom objects directly, remind them to convert through `to_dict()` first.

### Common Pitfalls to Watch For

- overwriting a good file with bad data
- assuming the working directory is stable
- forgetting that custom objects are not directly JSON serializable
- creating the temp file in a confusing or unrelated location

### Optional Extensions

- create a timestamped backup before replace
- add a separate `load_json()` helper with clean error handling
- add logging around save success and save failure

---

## Section 6: Failure Simulation and Troubleshooting Notes (Optional Extension Window)

### A Simple Instructor-Led Failure Drill

**[Instructor speaks:]**

If the room is moving well, run a short thought experiment or live simulation:

1. write directly to the real file
2. intentionally interrupt the write
3. inspect the damaged result
4. repeat the scenario conceptually with a temp file

The goal is not drama. The goal is memory. Students remember safe-save patterns better when they can picture the broken alternative.

### Sample Misconceptions and How to Respond

- "Using `with` alone makes a save fully safe."  
  Response: `with` manages cleanup of the file handle. It does not by itself protect against partial overwrites of the target file.

- "If the JSON dump starts, the file is probably fine."  
  Response: Partial writes can still leave unusable output.

- "I can dump custom objects directly and Python will figure it out."  
  Response: Usually not. Convert to plain data first.

- "The working directory is always the project root."  
  Response: Never assume that without checking. Path handling should be deliberate.

### Strong Save Utility Characteristics to Praise

- clear path construction
- directory creation before write
- temp file and replace flow
- plain serializable input
- readable function name and purpose

---

## Section 7: Debrief and Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

I want students to explain the pattern in one sentence:

"I save to a temp file first so a failed write does not destroy the good file."

If they can say that clearly, they understand the heart of the method.

### Exit Ticket

Ask students:

**What is one advantage of writing to a temp file first?**

Expected ideas:

- it reduces the chance of corrupting the original file
- it allows the write to fail safely before replacement
- it makes persistence more robust

### Instructor Closing Line

**[Instructor speaks:]**

Excellent. Your project can now save more responsibly. In the final hour of Session 3, we will look at decorators so we can apply repeated cross-cutting behavior such as timing, validation, or toy authorization without duplicating wrapper logic everywhere.
