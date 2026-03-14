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

## Checkpoint

**(5 min)**

**Quick Check:** What is the primary advantage of writing to a temporary file *first* when saving data?

*Expected answer:* If an error occurs halfway through generating the new file, your current pristine data is not truncated, damaged, or entirely lost. You are replacing the file purely instantly only after the operation finishes completely.
