# Day 11, Hour 1: Files — Reading and Writing Text

## Instructor Use Notes (Read First)

This script is designed to be read almost verbatim during class. It is intentionally detailed so you can teach confidently even if learners are seeing file I/O for the first time.

- **Runbook alignment:** Session 11, Hour 41 (Files: reading and writing text)
- **Time model:**
  - Talk + teach: 10–15 minutes
  - Live demo: 5–10 minutes
  - Lab: 25–35 minutes
  - Quick check + wrap: remaining minutes
- **Scope guard:** This hour is strictly Basics.
  We stay with plain text files, `with open(...) as f`, and line-by-line reading/writing.
- **Important non-goals for this hour:** JSON structure design, full path-manipulation lesson, advanced parsing, classes, databases.

---

## Outcomes (state these clearly at the top of class)

By the end of this hour, learners will be able to:

1. Open files safely using `with`.
2. Write lines to a text file using `write()`.
3. Read lines from a text file using `readlines()` (and see `read()`).
4. Explain where a file was saved by checking:
   - the **current working directory** (CWD), and
   - the file’s **absolute path**.
5. Load saved data back and print it clearly.

---

## Materials + Setup Checklist (Instructor)

Before learners start typing:

1. Confirm everyone is in the same lesson/project folder.
2. Confirm everyone can run a Python script from that folder.
3. Ask learners to close unrelated terminals to reduce confusion about working directory.
4. Remind learners: “Today we are saving data that survives after the script stops.”

Suggested opening line:

> “Up to now, most of our variables lived only while the script ran. Today we’re making data persistent by writing to files and then loading it back.”

---

## Section Plan (for your pacing and transitions)

1. Why files matter (motivation)
2. Core talk points (10–15 min)
3. Live demo: shopping list save + load (5–10 min)
4. Guided lab: contacts/tasks save + load (25–35 min)
5. Debrief, pitfalls, quick check

---

## Why This Matters (2–3 minute motivation)

Use this framing:

- Without files, a script “forgets” everything after it ends.
- With files, we can:
  - save shopping lists,
  - store contacts,
  - track tasks,
  - and generate simple reports.
- This is the first step toward real apps that keep data between runs.

Short analogy:

> “Memory variables are like writing on a whiteboard that gets erased when class ends. Files are like writing in a notebook you can open tomorrow.”

---

## Instructor Talk Points (10–15 min)

Use these 12 talk points in order. Pause for prediction questions between points.

### 1) What is a text file in this context?

A text file is plain characters, line by line. Examples:

- `shopping.txt`
- `contacts.txt`
- `tasks.txt`

We are **not** doing JSON in this hour; we are doing plain text lines.

### 2) File path vs filename

- A **filename**: `shopping.txt`
- A **path**: where that file lives on disk
- If you provide only a filename, Python uses the current working directory.

Say this out loud:

> “When learners say ‘Python can’t find my file,’ 80% of the time they’re in the wrong folder.”

### 3) Working directory (CWD) controls relative file access

Introduce this concept operationally:

- `Path.cwd()` tells us the current folder of execution.
- `Path("shopping.txt").resolve()` gives the full absolute location.

This is critical for completion criteria (“can locate file on disk”).

### 4) `with open(...) as f` is the default safe pattern

Core syntax:

```python
with open("shopping.txt", "w", encoding="utf-8") as f:
    f.write("Apples\n")
```

Explain:

- `with` creates a context block.
- File is automatically closed at block end.
- Safer than manual `open()` + `close()` because it still closes on errors.

### 5) Common file modes for this lesson

- `"r"` read
- `"w"` write (overwrites file)
- `"a"` append (adds to end)

You can mention append briefly, but keep practice focused on `"w"` then `"r"` per runbook.

### 6) `write()` writes exactly what you pass

Important behavior:

- `f.write("Milk")` writes `Milk` only.
- `f.write("Milk\n")` writes `Milk` and a new line.

This is where newline pitfalls start. Make this explicit.

### 7) `read()` vs `readlines()`

- `read()` returns one big string (entire file).
- `readlines()` returns a list of strings (one entry per line, newline included).

Show that newline characters remain in each line until stripped.

### 8) Cleaning line endings

When printing loaded lines cleanly:

```python
clean_line = line.strip()
```

`strip()` removes surrounding whitespace, including newline at line end.

### 9) Deterministic output habits

For classroom reliability:

- Use fixed sample data.
- Print clear headings.
- Number output consistently.

Avoid random data in required examples.

### 10) Error awareness without over-scoping

At Basics level, we can gently guard read step:

- If file may not exist, catch `FileNotFoundError`.
- Keep message simple and actionable.

Do not turn this hour into full exception design; Hour 44 goes deep.

### 11) Operational file-location check (required for this hour)

Every learner should print:

1. CWD
2. File absolute path
3. Whether the path exists

This makes “file location” measurable and not vague.

### 12) Mental model recap

Use this recap sentence:

> “We open with `with`, write lines with `write()`, include `\n`, read back with `readlines()`, clean with `strip()`, and confirm location with CWD + absolute path.”

---

## Live Demo (5–10 min)

### Demo Goal

Write a shopping list to a file, then read and print it.

### Instructor Narrative (what to say while coding)

Use this sequence:

1. “First, we will save a list to `shopping.txt`.”
2. “Then we will print where the file lives.”
3. “Finally, we will read it back and display numbered items.”

### Live Demo Code (single runnable script)

```python
from pathlib import Path

shopping_items = ["Apples", "Bananas", "Bread", "Milk"]  # Fixed sample data for deterministic classroom output

file_path = Path("shopping.txt")

print("=== FILE LOCATION CHECK ===")
print(f"Current working directory: {Path.cwd()}")
print(f"Absolute path for target file: {file_path.resolve()}")

print("\n=== WRITE STEP ===")
with open(file_path, "w", encoding="utf-8") as f:
    for item in shopping_items:
        f.write(item + "\n")
print("Shopping list written to file.")

print("\n=== VERIFY FILE EXISTS ===")
print(f"File exists? {file_path.exists()}")

print("\n=== READ STEP ===")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Items loaded from file:")
for index, line in enumerate(lines, start=1):
    print(f"{index}. {line.strip()}")
```

### Expected Output Shape (exact words may include your local path)

```text
=== FILE LOCATION CHECK ===
Current working directory: C:\...\your_folder
Absolute path for target file: C:\...\your_folder\shopping.txt

=== WRITE STEP ===
Shopping list written to file.

=== VERIFY FILE EXISTS ===
File exists? True

=== READ STEP ===
Items loaded from file:
1. Apples
2. Bananas
3. Bread
4. Milk
```

### Debrief Prompts Right After Demo

Ask:

1. “What would happen if I removed `\n` from the write line?”
2. “Why are we using `line.strip()` before printing?”
3. “Where exactly is this file on disk?”

Expected learner answers:

- Without `\n`, all items may appear merged in one line of file content.
- `strip()` removes newline/extra whitespace for clean display.
- File is in CWD unless a different path is provided.

---

## Quick Micro-Variation (Optional 2-minute in-demo branch)

If time allows, show this mini read contrast:

```python
with open("shopping.txt", "r", encoding="utf-8") as f:
    entire_text = f.read()
print(entire_text)
```

Then say:

> “`read()` is useful when you want the whole file as one string. `readlines()` is often easier when your data is one item per line.”

Keep this short; main lab uses line-based flow.

---

## Hands-on Lab (25–35 min)

## Lab Title

**Save and Load (Text): Contacts or Tasks**

### Lab Prompt (what learners must do)

1. Create a list of contacts or tasks in Python.
2. Save each item to a text file, one per line.
3. Load items back from the same file.
4. Print them as a numbered list.
5. Print CWD and absolute file path so the file location is explicit.

Allowed simple formats:

- Tasks only, e.g., `Buy batteries`
- Contact format, e.g., `Ava Lee|555-0199`

### Scope Reminder to Learners

Keep it simple:

- one `.txt` file
- write with `"w"`
- read with `"r"`
- line-per-item format

No advanced parsing required.

---

## Lab Walkthrough (Guided First, Then Independent)

Use this as your spoken guide.

### Step 1 — Choose a file name

Use one of:

- `tasks.txt`
- `contacts.txt`

Keep it in the current working directory for this required path.

### Step 2 — Build fixed sample data

Task example:

```python
tasks = [
    "Review notes",
    "Email instructor",
    "Practice file I/O",
    "Prepare tomorrow plan",
]
```

Contact example:

```python
contacts = [
    "Ava Lee|555-0199",
    "Noah Kim|555-0142",
    "Mia Chen|555-0188",
]
```

### Step 3 — Print location info first

Require this in every submission:

```python
from pathlib import Path

file_path = Path("tasks.txt")  # or Path("contacts.txt")
print(f"CWD: {Path.cwd()}")
print(f"Target absolute path: {file_path.resolve()}")
```

Why first? It reduces confusion before writing/reading.

### Step 4 — Write one item per line

```python
with open(file_path, "w", encoding="utf-8") as f:
    for item in tasks:
        f.write(item + "\n")
```

or for contacts:

```python
with open(file_path, "w", encoding="utf-8") as f:
    for contact in contacts:
        f.write(contact + "\n")
```

### Step 5 — Verify existence

```python
print(f"Created successfully? {file_path.exists()}")
```

### Step 6 — Read lines back

```python
with open(file_path, "r", encoding="utf-8") as f:
    loaded_lines = f.readlines()
```

### Step 7 — Print numbered output

```python
for index, line in enumerate(loaded_lines, start=1):
    print(f"{index}. {line.strip()}")
```

---

## Full Lab Reference Solution (Tasks version)

Use this after independent work or for support.

```python
from pathlib import Path

tasks = [
    "Review notes",
    "Email instructor",
    "Practice file I/O",
    "Prepare tomorrow plan",
]

file_path = Path("tasks.txt")

print("=== LOCATION ===")
print(f"CWD: {Path.cwd()}")
print(f"Target absolute path: {file_path.resolve()}")

print("\n=== WRITE ===")
with open(file_path, "w", encoding="utf-8") as f:
    for task in tasks:
        f.write(task + "\n")
print("Write complete.")

print("\n=== CHECK FILE ===")
print(f"Exists: {file_path.exists()}")

print("\n=== READ + PRINT ===")
with open(file_path, "r", encoding="utf-8") as f:
    loaded_tasks = f.readlines()

for number, line in enumerate(loaded_tasks, start=1):
    print(f"{number}. {line.strip()}")
```

### Full Lab Reference Solution (Contacts `name|phone` version)

```python
from pathlib import Path

contacts = [
    "Ava Lee|555-0199",
    "Noah Kim|555-0142",
    "Mia Chen|555-0188",
]

file_path = Path("contacts.txt")

print("=== LOCATION ===")
print(f"CWD: {Path.cwd()}")
print(f"Target absolute path: {file_path.resolve()}")

print("\n=== WRITE ===")
with open(file_path, "w", encoding="utf-8") as f:
    for contact in contacts:
        f.write(contact + "\n")
print("Write complete.")

print("\n=== CHECK FILE ===")
print(f"Exists: {file_path.exists()}")

print("\n=== READ + PRINT ===")
with open(file_path, "r", encoding="utf-8") as f:
    loaded_contacts = f.readlines()

for number, line in enumerate(loaded_contacts, start=1):
    print(f"{number}. {line.strip()}")
```

---

## Completion Criteria (Use for grading/spot-check)

A learner is complete when all are true:

1. **File created correctly**
   Their script writes a `.txt` file with one item per line.
2. **File reloaded correctly**
   Their script reads lines back and prints a numbered list.
3. **File location proven**
   Their output includes:
   - current working directory (`Path.cwd()`), and
   - absolute file path (`file_path.resolve()`), and
   - existence check result (`True` expected after write).
4. **Learner can locate file on disk**
   Learner can navigate to printed path in IDE/file explorer and show file exists.

### Fast instructor rubric (pass/fix)

- **Pass:** all four criteria met.
- **Fix needed:** missing one or more criteria.

If fix needed, give one precise next action:

- “Add `\n` while writing.”
- “Print CWD to verify path.”
- “Open with `with` so file closes safely.”

---

## Common Pitfalls to Watch For (and exact coaching language)

### Pitfall 1: Wrong path or wrong working directory

Symptoms:

- `FileNotFoundError` on read
- File created, but learner “can’t find it”

Coaching script:

> “Let’s print `Path.cwd()` and `file_path.resolve()` first.
> If the folder is not where you expect, run the script from the correct folder or update the path.”

Quick fix checklist:

1. Print CWD.
2. Confirm file name spelling.
3. Confirm script execution folder.
4. Re-run write step, then check `.exists()`.

### Pitfall 2: Forgetting newline characters

Symptoms:

- All records appear as one long line in file.
- Printed output doesn’t match intended line structure.

Coaching script:

> “`write()` only writes exactly what you give it.
> Add `'\n'` for each item to put each record on its own line.”

Quick fix:

```python
f.write(item + "\n")
```

### Pitfall 3 (brief mention): Misusing `"w"` when expecting append behavior

Symptoms:

- Old contents disappear each run.

Coaching:

> “`'w'` starts fresh each time. That is fine for this lab’s required behavior.
> Use `'a'` only when you intentionally want to add to existing content.”

Keep this note short to avoid scope drift.

---

## Instructor Live Support Patterns During Lab

When circulating, ask these in order:

1. “Show me your CWD line.”
2. “Show me your absolute path line.”
3. “Show me where you add `\n` while writing.”
4. “Show me where you call `readlines()`.”
5. “Show me where you print cleaned lines with `strip()`.”

This sequence finds most issues in under one minute.

If a learner is stuck, avoid typing for them immediately.
Instead, coach with micro-prompts:

- “What does your script print before writing?”
- “What does `.exists()` show?”
- “Is your read step opening the same filename?”

---

## Suggested Minute-by-Minute Facilitation Plan

### Minutes 0–3: Context and outcomes

- Explain persistence vs temporary memory.
- State two outcomes clearly:
  - use `with`
  - read/write lines.

### Minutes 3–12: Talk points

- Cover CWD/path, file modes, `write`, `read`, `readlines`.
- Ask one prediction question every 2–3 minutes.

### Minutes 12–20: Live demo

- Run shopping demo exactly once end-to-end.
- Make one deliberate mistake (remove `\n`) and fix live if time allows.

### Minutes 20–50: Lab

- First 8 minutes guided steps.
- Next 15–20 minutes independent.
- Final 5–7 minutes spot checks and debrief.

### Minutes 50–60: Quick check + recap

- Exit ticket question on `with`.
- Confirm everyone can locate their file.

---

## Differentiation Guidance

### For learners who need more support

- Provide them the tasks version (single field, no separator).
- Have them complete only:
  - write 3 lines
  - read and print 3 lines
  - print CWD + absolute path.

### For learners who finish early (still Basics)

Use **optional** extensions only (not required for completion):

1. Add a timestamp header line.
2. Export a pretty report text file.

Clearly say:

> “These extensions are enrichment only.
> They are not required for today’s pass criteria.”

---

## Optional Extensions (Strictly Non-Required)

These are explicitly optional and should not block core completion.

### Optional Extension A — Timestamp Header Line

Goal: write a first line such as `Generated: 2026-01-13 10:30:00`.

Example:

```python
from datetime import datetime
from pathlib import Path

items = ["Review notes", "Email instructor", "Practice file I/O"]
file_path = Path("tasks_with_header.txt")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    for item in items:
        f.write(item + "\n")
```

Instructor note: timestamp value changes by run, so output is not fixed.
That is acceptable here because this is optional enrichment.

### Optional Extension B — Pretty Report Export

Goal: create a second file with simple formatting.

Example:

```python
from pathlib import Path

loaded_items = ["Review notes", "Email instructor", "Practice file I/O"]
report_path = Path("tasks_report.txt")

with open(report_path, "w", encoding="utf-8") as f:
    f.write("TASK REPORT\n")
    f.write("===========\n")
    for i, item in enumerate(loaded_items, start=1):
        f.write(f"{i}. {item}\n")
```

Again, optional only.

---

## Quick Check / Exit Ticket (Required)

Ask exactly:

> “Why is using `with` recommended for file handling?”

Strong answer:

> “`with` automatically closes the file when the block ends, even if an error happens.
> That prevents resource leaks and reduces file corruption risk.”

Acceptable shorter answer:

> “It guarantees proper closing and is safer than manual `open()`/`close()`.”

---

## Debrief Script (End-of-Hour Close)

Use this short closing narrative:

> “Today you wrote real data to disk and loaded it back.
> You practiced the core file workflow used everywhere in Python scripting:
> open with `with`, write with `write`, read with `readlines`, clean with `strip`.
> Most importantly, you proved where your file is by printing CWD and absolute path.
> That path awareness will save you hours of debugging.”

Then ask for one volunteer to screenshare:

1. Their script output
2. Their file in file explorer/IDE
3. The matching absolute path

---

## Board Notes / Slide Notes (Concise Reference)

If you need a quick board summary:

```text
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("line\n")

with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

Remember:

- CWD controls relative paths
- Print absolute path to locate files
- Add "\n" when writing line-by-line
- Use .strip() when printing loaded lines

---

## Troubleshooting Appendix (Instructor Rapid Response)

### A) Learner gets `FileNotFoundError`

Checklist:

1. Did they run write step before read step?
2. Same filename in both places?
3. CWD unexpected?
4. Typo in extension (`.text` vs `.txt`)?

Recovery script:

```python
from pathlib import Path

file_path = Path("tasks.txt")
print(Path.cwd())
print(file_path.resolve())
print(file_path.exists())
```

If `exists()` is `False`, write step likely failed or path mismatch.

### B) Learner output has blank lines between items

Cause:

- They may have both line breaks in data and extra newline handling in print.

Fix:

- Use `line.strip()` in print loop.

### C) Learner sees all text in one line

Cause:

- Missing `\n` while writing.

Fix:

- Append newline per record in write loop.

### D) Learner can run script but cannot find file in editor sidebar

Cause:

- Script executed from different terminal location.

Fix:

- Print CWD.
- Change terminal to expected folder.
- Run again.
- Refresh editor file tree.

---

## Verbatim Teaching Script (Use as Live Speaking Guide)

The section below is intentionally written as a near-verbatim script you can read with minor personalization. It is split by classroom time windows so you can stay on pace.

### Minute 0–2: Opening and relevance

“Welcome back, everyone. In this hour we are learning one of the most practical Python skills: saving data to a file, then loading it back.
So far, many of our variables existed only while the script ran. Once the script ended, data was gone.
Today we solve that by writing text files.

By the end of this hour, you will be able to:

1. open files safely with `with`,
2. write lines using `write()`,
3. read lines using `readlines()`,
4. and prove where your file is saved by printing both your current working directory and absolute path.

That last part matters. If you can’t find your file, your code is not done yet.”

Pause and ask:

“Quick thumbs check: who has ever saved a file and then couldn’t find it?”
(Most hands go up.)
“Perfect. We’re going to fix that permanently today.”

### Minute 2–5: Concept framing and vocabulary

“Let’s define our core terms in plain language:

- A **text file** is plain characters.
- A **line** is one row of text ending with newline.
- A **filename** is something like `tasks.txt`.
- A **path** is where that file lives.
- The **current working directory**, or CWD, is the folder your script is running from.

When we pass only `tasks.txt`, Python looks in the CWD.
So if your script is running in a different folder than you think, your file might be created somewhere else.

This is why today we always print:

1. `Path.cwd()`
2. `file_path.resolve()`
3. `file_path.exists()`

If we print those three things, we can always answer: ‘Where is my file?’”

### Minute 5–9: Safe file-opening pattern

“Now the syntax pattern:

`with open('tasks.txt', 'w', encoding='utf-8') as f:`

Say it with me: **with open as f**.

`with` is recommended because it closes the file automatically when the block ends, even if an error occurs.
If we manually open and forget to close, we can leak resources or leave files in a bad state.

For this lesson we use modes:

- `'w'` write (start fresh / overwrite),
- `'r'` read,
- and optional mention: `'a'` append.

We are not building an append-heavy app yet, but I want you to know `'a'` exists.”

Ask:

“If I use `'w'` on an existing file, does it keep old content?”
Expected response: “No, it overwrites.”

### Minute 9–12: Reading and writing details

“Now the key methods:

- `write()` writes exactly the string you give it.
- `read()` reads all text into one big string.
- `readlines()` reads into a list, one item per line.

Important detail: `write()` does not automatically add line breaks.
If you want one item per line, add `'\n'`.

When reading with `readlines()`, each line usually still has `'\n'` at the end.
So before printing, use `strip()` for clean output.”

Mini prediction:

“What happens if I forget `'\n'` while writing a loop of items?”
Expected answer: “Everything gets stuck together.”

### Minute 12–20: Live demo script

“I’m now running a full save-and-load demo with shopping items.
Watch for four checkpoints:

1. print CWD,
2. print absolute path,
3. write list,
4. read and print numbered lines.

While I type, your job is to predict each output section.”

As you run, narrate:

“Here is `file_path = Path('shopping.txt')`.
Before writing, I print CWD and absolute path.
Now we open in write mode and loop through fixed list data.
Notice I explicitly add `'\n'` each time.
After writing, we check `exists()` to verify file creation.
Then we open same file in read mode and call `readlines()`.
Finally, we print each line with `strip()` and numbering.”

After run:

“Look at the screen:

- We know exactly where the file was created.
- We confirmed it exists.
- We read back exactly what we wrote.

This is a complete persistence cycle.”

### Minute 20–22: Transition to lab

“Your lab now follows the same pattern.
You’ll create either a tasks list or contacts list, save it to a text file, load it back, and print it clearly.

Required today:

- one item per line,
- CWD + absolute path output,
- and successful reload.

Optional additions exist, but they are non-required and only for early finishers.”

### Minute 22–35: Guided lab phase script

“For the first phase, code with me:

Step 1: choose filename (`tasks.txt` or `contacts.txt`).
Step 2: create a fixed Python list.
Step 3: print CWD and absolute path.
Step 4: write lines with `'\n'`.
Step 5: check `.exists()`.
Step 6: read with `readlines()`.
Step 7: print numbered, stripped lines.

If you get an error, do not panic.
Your first debug question is: ‘What folder am I running in?’”

Walk room and repeat:

“Show me your CWD line.”
“Show me where you add newline.”
“Show me your read step.”

### Minute 35–48: Independent lab phase script

“Now work independently for 10–13 minutes.
You may choose tasks or contacts format.

If you finish early, optional extension:

- add timestamp header line, or
- export pretty report file.

Reminder: those are enrichment only, not required.”

As you circulate, use this coaching script:

“Tell me what is supposed to happen.
Show me what happened instead.
Where do we see that in output?
Which line of code controls that behavior?”

This encourages debugging thinking, not code copying.

### Minute 48–55: Debrief script

“Let’s debrief with two volunteer solutions.

Volunteer one: tasks version.
Volunteer two: contacts `name|phone` version.

As we review, everyone check:

- Did they print CWD?
- Did they show absolute path?
- Did `.exists()` show True?
- Did output print clean numbered lines?

If all yes, that is complete.”

### Minute 55–60: Exit ticket script

“Final quick check:

Why is `with` recommended for file handling?”

Call on two learners:

- one short answer,
- one full answer.

Close:

“Great work. You now have the core workflow that every data-saving script depends on.”

---

## Structured Question Bank (Use During Teaching)

Use these prompts to keep learners active rather than passive.

### Prediction Questions

1. “If I remove `\n`, what changes in the saved file?”
2. “If I run from a different folder, where will the file go?”
3. “What data type does `readlines()` return?”
4. “Why call `strip()` before printing?”
5. “What does `'w'` do to existing content?”

### Debugging Questions

1. “What is your current working directory right now?”
2. “Is read step opening same filename as write step?”
3. “What does `file_path.exists()` return?”
4. “Where is the exact mismatch between expected and actual output?”
5. “What is one small change to test next?”

### Reflection Questions

1. “How does saving to file change what your app can do tomorrow?”
2. “What bug did you hit, and what print helped you solve it?”
3. “Which is easier for this task: `read()` or `readlines()`? Why?”

---

## Assessment Support: Spot-Check Prompts by Completion Criterion

When grading quickly, ask one proof question per criterion.

### Criterion 1 — File created correctly

Prompt: “Run your write step now. What does your console show right after write?”

Expected evidence:

- Success message and `exists()` True.

### Criterion 2 — File reloaded correctly

Prompt: “Run your read step now. Show me numbered output.”

Expected evidence:

- Items printed as list, not one merged line.

### Criterion 3 — Location proven

Prompt: “Show me CWD and absolute path lines.”

Expected evidence:

- Both printed clearly, paths are valid.

### Criterion 4 — Locate on disk

Prompt: “Open file explorer/editor and navigate to that absolute path.”

Expected evidence:

- Learner can visibly open the file from that path.

---

## Instructor Notes on Scope Control (Avoid Overrun)

Because this hour is foundational, it is easy to drift into too many side topics. Use these boundaries:

- Keep required file path minimal (current folder + simple filename).
- Keep required data format simple (line-per-item).
- Keep required parsing minimal (`strip()` only).
- Keep required methods focused (`write`, `readlines`, optional mention of `read`).
- Keep exception handling light (single-file not-found awareness only).

Avoid in required path:

- nested folder creation workflows,
- CSV module deep dive,
- JSON serialization details,
- complex validation frameworks.

If a strong learner asks advanced questions, answer briefly and park for later hour:

> “Great question. We’ll go deeper in upcoming sessions. For now, let’s lock in the core pattern first.”

---

## Model Classroom-Safe Data Sets (Deterministic)

Use these fixed samples to prevent sensitive or unpredictable outputs.

### Shopping demo set

- Apples
- Bananas
- Bread
- Milk

### Tasks lab set

- Review notes
- Email instructor
- Practice file I/O
- Prepare tomorrow plan

### Contacts lab set

- Ava Lee|555-0199
- Noah Kim|555-0142
- Mia Chen|555-0188

These are deterministic, neutral, and classroom-safe.

---

## Minimal Required Path (to prevent scope overrun)

For this required hour, keep the path minimal:

- use `Path("shopping.txt")`, `Path("tasks.txt")`, or `Path("contacts.txt")`
- keep file in current working directory
- verify with CWD + absolute path print

We intentionally avoid deeper directory management in this required flow.
Directory-specific path work is covered later.

---

## Instructor Self-Check Before Ending the Hour

Confirm all required runbook targets were covered:

- [x] Outcomes: open files with `with`; read lines and write lines
- [x] Talk points: file paths and working directory; `with open(...) as f`; `read/readlines/write`
- [x] Live demo: shopping list write then read/print
- [x] Lab: contacts/tasks one-per-line; load and print; simple format (`name|phone` acceptable)
- [x] Completion criteria: file created/reloaded correctly; learner can locate file on disk
- [x] Pitfalls: wrong path/working directory; forgetting newline characters
- [x] Optional extension mention: timestamp header line and pretty report export
- [x] Quick check: why `with` is recommended
- [x] Operationalized location check: CWD + absolute path + exists check

If all boxes are checked, Hour 41 objective is complete.

---

## Short Homework Suggestion (Optional, 5–10 minutes outside class)

Create `my_notes.txt` with five lines:

1. one thing learned today,
2. one question still unclear,
3. one error they hit,
4. how they fixed it,
5. one practice goal for tomorrow.

Then write a script to read and print those five lines in numbered format.

This reinforces the same read/write loop without adding scope.

---

## Final Instructor Wrap Statement

> “Great work. You now know how to persist simple data with text files, load it back, and verify file location clearly.
> These habits—especially using `with` and checking CWD/absolute path—are foundational for everything we build next.”
