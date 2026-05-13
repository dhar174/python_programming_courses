# Day 11 Hour 3 (Hour 43): Directories + Paths with `pathlib` (Instructor Script)

## Instructor intent and alignment

This hour is the bridge between “I can read/write one file” and “I can build programs that keep working when moved to another machine, another folder, or another teammate’s environment.” In Hour 42, learners saved JSON. In Hour 43, we make that persistence reliable by teaching directory creation and file discovery with `pathlib`.

This script is aligned to the runbook for Hour 43 and intentionally emphasizes portable path patterns:

- Teach `Path.cwd()` conceptually so students understand working directory behavior.
- Use a **script/project-relative base path** for implementation reliability.
- Avoid hardcoded personal folders (`Desktop`, `Downloads`, user-specific home paths).
- Use directory discovery (`iterdir`, `glob`) instead of hardcoding file names.

If learners leave this hour with one key habit, it should be: “My code computes paths from the project, not from my personal machine layout.”

## Outcomes (state these at the start)

By the end of this hour, learners will be able to:

1. Use `pathlib` to build reliable file paths.
2. Create a `data/` directory safely if it does not exist.
3. List directory contents with `iterdir()` and pattern-match files with `glob()`.
4. Discover available JSON files dynamically and choose one deterministically.
5. Explain why discovery avoids hardcoding and improves portability.

## Prerequisites and setup check (quick)

Learners should already be able to:

- Run Python scripts from a terminal and/or IDE.
- Read and write JSON at a basic level (`json.dump`, `json.load`).
- Understand basic `if` statements and loops.

Ask learners to confirm:

- They are in their course project folder.
- They can run `python --version`.
- They can create and run a new `.py` file in their project.

---

## Suggested minute-by-minute flow (for instructor pacing)

- **0:00–0:04** — Hook + outcomes
- **0:04–0:18** — Talk points (conceptual framing + best practices)
- **0:18–0:28** — Live demo (create folder, save JSON, discover files)
- **0:28–0:55** — Hands-on lab (build it independently, run from different starts)
- **0:55–1:00** — Debrief + quick-check question

If class pace is slower, trim optional extension first, not the deterministic discovery pattern.

---

## Talk points (10–15 min): speaking guide

Use this section as near-verbatim lecture notes if helpful.

### 1) Relative vs absolute paths

“Let’s begin with a very practical question: *where exactly is your file?* In Python, there are two common path styles:

- **Absolute path**: full location from the drive/root, like
  `C:\Users\Ava\Downloads\data.json` (Windows)
  or `/Users/ava/Downloads/data.json` (macOS/Linux).
- **Relative path**: location relative to a base folder, like `data/data.json`.

Absolute paths are not always wrong, but they are usually bad for shared code because they include machine-specific details. If I hardcode my personal `Downloads` path and send you the script, it fails on your computer.”

Pause and ask:

> “If you see `C:\Users\myname\Desktop\...` in shared code, what risk do you immediately see?”

Expected learner response: It works only for one user/machine.

Reinforce:

“Exactly. We want paths that survive movement: different user account, different machine, different terminal starting folder.”

### 2) Why `open("data.json")` sometimes works and sometimes fails

“Many beginners start with this:

```python
with open("data.json") as file:
    ...
```

Sometimes it works. Sometimes it throws `FileNotFoundError`. Why? Because `"data.json"` is a **relative path**. Relative to what? Relative to the **current working directory** (CWD), not necessarily the script’s folder.”

Explain with a simple scenario:

- Script is in `project/app.py`.
- Data file is in `project/data/data.json`.
- If terminal is started in `project/`, maybe things work if code is written carefully.
- If terminal is started in parent folder and script is run with a different command path, naive relative assumptions can break.

“So the bug is often not the file itself. The bug is *which folder Python thinks is the base*.”

### 3) `Path.cwd()` and `Path("data")`: concept first

“`pathlib` gives us a modern way to work with paths as objects, not fragile strings.

- `Path.cwd()` shows the current working directory.
- `Path("data")` means a relative path called `data` from the current working directory.

So `Path.cwd() / "data"` and `Path("data")` are both tied to CWD unless we anchor them differently.”

Show this short conceptual snippet:

```python
from pathlib import Path

print(f"Current working directory: {Path.cwd()}")
print(f"Relative path object: {Path('data')}")
```

Say clearly:

“I am showing `Path.cwd()` so you understand behavior. I am **not** saying ‘build final app logic from CWD.’ CWD can change depending on where you launched the command.”

### 4) Reliable pattern: script/project-relative base directory

“For production-minded basic code, we anchor paths to the script or project root, then join into `data/`.

Core pattern:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
```

`__file__` is the current script path. `resolve()` gives us an absolute, normalized path. `.parent` gives the folder containing the script.”

Important classroom caveat:

“This pattern assumes your script is in the project root. If your script sits one level deeper (for example `project/src/app.py`), then your project root might be `BASE_DIR.parent`. The idea is unchanged: choose a stable project-relative base once, then build all paths from that.”

Say this explicitly to avoid confusion:

“Our **best-practice target today** is: derive from script/project location, not from a personal folder and not from whichever folder the terminal happened to start in.”

### 5) Creating folders safely: `mkdir(exist_ok=True)`

“If our app needs `data/`, we should create it safely:

```python
DATA_DIR.mkdir(exist_ok=True)
```

`exist_ok=True` means:
- if folder doesn’t exist, create it
- if it already exists, do not crash”

Optionally mention parent directories (without dwelling too long):

“If you need to create multiple missing levels, add `parents=True`. Today, `data/` is one level under the project root, so `exist_ok=True` is enough.”

### 6) Discover files dynamically: `iterdir()` and `glob()`

“Hardcoding file names can become fragile:

- maybe the file is `data.json` today
- tomorrow it’s `settings.json` or `save_2026_01_13.json`

Directory discovery lets the program inspect what exists.

- `iterdir()` gives every item in a directory.
- `glob("*.json")` gives items matching a pattern.”

Use this pattern:

```python
all_items = sorted(DATA_DIR.iterdir(), key=lambda p: p.name.lower())
json_files = sorted(DATA_DIR.glob("*.json"), key=lambda p: p.name.lower())
```

Call out deterministic ordering:

“Notice `sorted(...)`. File system iteration order is not guaranteed. Sorting gives consistent output, consistent demos, consistent tests, and fewer ‘it worked on my machine’ moments.”

### 7) Why discovery avoids hardcoding

“Directory discovery gives three practical wins:

1. **Resilience**: code adapts if filenames change.
2. **Visibility**: easier debugging because you can print what exists.
3. **Scalability**: supports multiple save files without rewriting core logic.”

Bridge to lab:

“In the lab, you’ll create `data/data.json`, print discovered files, and if multiple JSON files exist, choose one deterministically so your program behavior is predictable.”

### 8) Project-relative best practice statement (say this exactly)

“In shared code, we avoid hardcoded `Desktop` or `Downloads` paths. We build a stable base path from the script/project root and join into `data/`. We use `Path.cwd()` to understand runtime context, but we do not depend on CWD as our final architecture.”

Pause for a quick comprehension check:

> “What is the difference between ‘knowing CWD’ and ‘depending on CWD’?”

Desired answer: CWD helps debug context, but reliable code should use a stable project-relative anchor.

---

## Live demo (5–10 min): create folder, write JSON, discover files

### Demo goal to announce

“We will write one script that:

1. Computes a project-relative `data/` folder path with `pathlib`.
2. Creates that folder if needed.
3. Saves JSON into the folder.
4. Lists directory contents and prints JSON file names.
5. Handles the ‘no JSON files found’ case deterministically.
6. If JSON files exist, chooses one deterministic file path.”

### Demo script (runnable)

Create a file such as `path_demo.py` in the project root and paste:

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def build_paths() -> tuple[Path, Path]:
    """
    Return (base_dir, data_dir) anchored to this script location.
    """
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    return base_dir, data_dir


def ensure_data_dir(data_dir: Path) -> None:
    """
    Create data directory if it does not exist.
    """
    data_dir.mkdir(exist_ok=True)


def write_demo_json(target_file: Path) -> None:
    """
    Write a small JSON payload to demonstrate persistence.
    """
    payload: dict[str, Any] = {
        "student": "demo_user",
        "score": 100,
        "level": 5,
    }
    with target_file.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def list_all_items(data_dir: Path) -> list[Path]:
    """
    Return all directory items sorted by name (deterministic order).
    """
    return sorted(data_dir.iterdir(), key=lambda p: p.name.lower())


def list_json_files(data_dir: Path) -> list[Path]:
    """
    Return *.json files sorted by name (deterministic order).
    """
    return sorted(data_dir.glob("*.json"), key=lambda p: p.name.lower())


def choose_json_file(json_files: list[Path]) -> Path | None:
    """
    Deterministically choose the first file in sorted order.
    Return None if no JSON files exist.
    """
    if not json_files:
        return None
    return json_files[0]


def main() -> None:
    base_dir, data_dir = build_paths()

    # Teach CWD conceptually, but do not depend on it for path logic.
    print(f"Current working directory (concept): {Path.cwd()}")
    print(f"Script/project-relative base (implementation): {base_dir}")

    ensure_data_dir(data_dir)
    print(f"Ensured data directory exists: {data_dir}")

    print("\nDiscovery pass 1 (before writing any demo save):")
    json_files_before = list_json_files(data_dir)
    if not json_files_before:
        print("No save files found.")
    else:
        for file_path in json_files_before:
            print(f"- {file_path.name}")

    demo_file = data_dir / "save1.json"
    write_demo_json(demo_file)
    print(f"Wrote demo JSON to: {demo_file}")

    print("\nAll items currently in data/:")
    all_items = list_all_items(data_dir)
    if not all_items:
        print("- (empty directory)")
    else:
        for item in all_items:
            item_type = "DIR " if item.is_dir() else "FILE"
            print(f"- [{item_type}] {item.name}")

    print("\nDiscovery pass 2 (after writing demo save):")
    json_files = list_json_files(data_dir)
    if not json_files:
        print("No save files found.")
    else:
        for file_path in json_files:
            print(f"- {file_path.name}")

    selected = choose_json_file(json_files)
    if selected is None:
        print("Chosen file: None (no JSON files available)")
    else:
        print(f"Chosen file (deterministic): {selected}")


if __name__ == "__main__":
    main()
```

### Demo narration script (what to say while coding/running)

1. **Start with `build_paths()`**
   - “I’m deriving `base_dir` from `__file__`, not from CWD.”
   - “This keeps path logic stable even if terminal launch folder changes.”

2. **Show CWD without depending on it**
   - “I still print `Path.cwd()` for visibility and debugging.”
   - “Understanding CWD helps explain behavior, but CWD is not our anchor.”

3. **Create data folder**
   - “`mkdir(exist_ok=True)` prevents errors when rerunning scripts.”
   - “Rerunnable scripts are a professionalism habit.”

4. **Write JSON using `Path.open()`**
   - “With `pathlib`, paths remain `Path` objects end-to-end.”
   - “Using `encoding='utf-8'` is explicit and good practice.”

5. **List with `iterdir()`**
   - “This includes files and folders.”
   - “I sort by lowercase name for deterministic output.”

6. **Filter with `glob("*.json")`**
   - “Pattern matching finds only JSON files.”
   - “Again, sort to avoid non-deterministic ordering.”

7. **No-files behavior**
   - “If there are zero JSON files, print `No save files found.`”
   - “Never assume a file exists unless you checked.”

8. **Deterministic choice**
   - “When multiple JSON files exist, I pick the first sorted one.”
   - “Even a simple deterministic rule is better than random behavior.”

### Optional micro-variation during demo

If time allows, create an extra file manually:

```python
extra_file = data_dir / "z_backup.json"
write_demo_json(extra_file)
```

Then re-run and show that sorted selection still chooses `save1.json` (assuming lexical order), proving deterministic behavior.

### What to highlight after running

Ask:

1. “Did our path logic rely on CWD for final behavior?” (No.)
2. “Can this script be rerun safely?” (Yes, `exist_ok=True`.)
3. “Is file discovery hardcoded?” (No, uses `glob`.)
4. “Is selection deterministic?” (Yes, sorted then first.)

---

## Hands-on lab (25–35 min): data folder + deterministic discovery

### Lab framing for learners

“You will now build your own version of this pattern. Your goal is not just to make it work once. Your goal is to make it reliable.”

### Lab requirements (present clearly)

Create a script (for example `lab_data_paths.py`) that does all of the following:

1. Create a `data/` folder safely using `pathlib`.
2. Save JSON to `data/data.json`.
3. Run correctly even if terminal starts from different locations (within reason) by anchoring paths to script/project location.
4. Print the names of all files in `data/`.
5. Find all `.json` files in `data/` with `glob("*.json")`.
6. If multiple JSON files exist, choose one deterministically (sorted first match) and print the chosen path.
7. If no JSON files exist, print a clear no-files message.

### Suggested lab scaffold (students can start from this)

```python
from __future__ import annotations

import json
from pathlib import Path


def get_data_dir() -> Path:
    base_dir = Path(__file__).resolve().parent
    return base_dir / "data"


def main() -> None:
    data_dir = get_data_dir()
    data_dir.mkdir(exist_ok=True)

    print("Discovery pass 1 (before writing):")
    json_files_before = sorted(data_dir.glob("*.json"), key=lambda p: p.name.lower())
    if not json_files_before:
        print("No save files found.")
        print("Chosen JSON path: None")
    else:
        print("JSON files discovered:")
        for path in json_files_before:
            print(f"- {path.name}")
        print(f"Chosen JSON path: {json_files_before[0]}")

    target_file = data_dir / "data.json"
    payload = {"app": "lab", "status": "ok"}
    with target_file.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)

    print(f"Data directory: {data_dir}")
    print("All file names in data/:")
    for path in sorted(data_dir.iterdir(), key=lambda p: p.name.lower()):
        print(f"- {path.name}")

    print("\nDiscovery pass 2 (after writing data.json):")
    json_files = sorted(data_dir.glob("*.json"), key=lambda p: p.name.lower())
    if not json_files:
        print("No save files found.")
        print("Chosen JSON path: None")
    else:
        chosen = json_files[0]
        print("JSON files discovered:")
        for path in json_files:
            print(f"- {path.name}")
        print(f"Chosen JSON path: {chosen}")


if __name__ == "__main__":
    main()
```

### Instructor support script during lab circulation

When students are coding, walk and ask targeted questions:

1. “Where does your base path come from?”
2. “Are you using `Path.cwd()` as final logic, or just as debug information?”
3. “Did you include `exist_ok=True`?”
4. “Are your glob results sorted?”
5. “What happens if no JSON files exist?”

These questions quickly reveal whether learners understand the reliability goal.

### Run-from-different-starts check (within reason)

Have learners test at least two launches:

- Launch from project folder.
- Launch from a parent folder using a path to the script.

Expected result: their script still points to the same `data/` location because it is script-relative.

If using an IDE, note:

- IDEs often set CWD to project folder automatically, which can hide path bugs.
- Ask learners to test in terminal too.

### Deterministic multi-file test

Ask learners to create at least one extra JSON file in `data/`, for example:

- `a.json`
- `z.json`

Then rerun and confirm:

- `glob("*.json")` results are sorted.
- Chosen file is the first sorted entry every time.

This demonstrates reproducible behavior.

### Minimal expected output shape (example)

Actual absolute paths differ by machine, but output should look roughly like:

```text
Data directory: C:\...\project\data
All file names in data/:
- a.json
- data.json
- z.json
JSON files discovered:
- a.json
- data.json
- z.json
Chosen JSON path: C:\...\project\data\a.json
```

If no JSON files exist at discovery time, they should get:

```text
No save files found.
Chosen JSON path: None
```

---

## Completion criteria (use for grading/spot checks)

A submission meets expectations when all are true:

1. Uses `pathlib` path objects for core path operations.
2. Targets a project/script-relative `data/` directory (not hardcoded personal folders).
3. Creates folder safely with `mkdir(exist_ok=True)`.
4. Saves JSON to `data/data.json`.
5. Lists file names in `data/` using directory iteration.
6. Discovers JSON files with `glob("*.json")`.
7. Sorts discovery results for deterministic ordering.
8. Implements explicit no-files handling.
9. If multiple JSON files exist, chooses one deterministically and prints chosen path.

Stretch quality indicators:

- Uses small helper functions for readability.
- Uses clear variable names (`data_dir`, `json_files`, `chosen_file`).
- Uses `encoding="utf-8"` and consistent output formatting.

---

## Common pitfalls and instructor interventions

### Pitfall 1: Hardcoded absolute paths

**Example of issue**

```python
data_dir = Path("C:/Users/Ava/Desktop/data")
```

**Why it fails**

- Tied to one username and one machine.
- Breaks in class VMs, on teammates’ systems, and in CI.

**Intervention line**

“Replace personal machine paths with a computed project-relative base derived from `__file__`.”

### Pitfall 2: CWD-dependent final pattern

**Example of issue**

```python
data_dir = Path.cwd() / "data"
```

**Why it’s fragile**

- Works only when command runs from the expected directory.
- Fails when launched from different terminal location.

**Intervention line**

“Use `Path.cwd()` for awareness/debugging, not as your final anchor for project data paths.”

### Pitfall 3: Forgetting `exist_ok=True`

**Example of issue**

```python
data_dir.mkdir()
```

**Problem**

- Crashes on second run if folder already exists.

**Intervention line**

“Make scripts rerunnable: `mkdir(exist_ok=True)`.”

### Pitfall 4: Assuming `glob()` order

**Example of issue**

```python
json_files = list(data_dir.glob("*.json"))
chosen = json_files[0]
```

**Problem**

- Order may differ across environments/filesystems.

**Intervention line**

“Sort first, then choose: deterministic behavior is a quality habit.”

### Pitfall 5: Not handling empty results

**Problem**

- Index error when `json_files[0]` on empty list.

**Intervention line**

“Always branch on empty list before choosing an element.”

### Pitfall 6: Mixing strings and paths inconsistently

**Problem**

- String concatenation with slashes can become messy and platform-fragile.

**Intervention line**

“Keep values as `Path` objects until the final display step.”

---

## Optional extension (if learners finish early)

### Extension: allow user to choose file name

Goal: keep discovery logic, but let user optionally specify target name.

Rules:

- If user enters blank input, default to `data.json`.
- Force `.json` suffix if missing.
- Save to chosen file in `data/`.
- Re-run discovery and deterministic selection.

Example extension snippet:

```python
name = input("Enter save filename (blank = data.json): ").strip()
if not name:
    name = "data.json"
if not name.lower().endswith(".json"):
    name += ".json"

target = data_dir / name
```

Teaching note:

This extension reinforces that path handling and input handling are connected. Even here, avoid accepting full absolute paths from users in a basics script unless that is explicitly the lesson goal.

---

## Full reference implementation (for instructor answer key)

Use this if you need a complete, classroom-safe model solution.

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def get_project_base() -> Path:
    """
    Return a stable base directory for project-relative paths.
    Assumes this script is stored in the project root.
    """
    return Path(__file__).resolve().parent


def get_data_dir(base_dir: Path) -> Path:
    """
    Return project data directory path.
    """
    return base_dir / "data"


def ensure_directory(path: Path) -> None:
    """
    Ensure directory exists without crashing if already present.
    """
    path.mkdir(exist_ok=True)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    """
    Save payload as formatted JSON.
    """
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def discover_all_files(directory: Path) -> list[Path]:
    """
    Return all files/directories sorted by lowercase name.
    """
    return sorted(directory.iterdir(), key=lambda p: p.name.lower())


def discover_json_files(directory: Path) -> list[Path]:
    """
    Return all .json files sorted by lowercase name.
    """
    return sorted(directory.glob("*.json"), key=lambda p: p.name.lower())


def choose_deterministic(json_files: list[Path]) -> Path | None:
    """
    Choose the first file in sorted list, or None if empty.
    """
    if not json_files:
        return None
    return json_files[0]


def print_discovery(all_items: list[Path], json_files: list[Path]) -> None:
    """
    Print discovered items and JSON files.
    """
    print("All items in data/:")
    if not all_items:
        print("- (empty directory)")
    else:
        for item in all_items:
            print(f"- {item.name}")

    print("\nJSON files in data/:")
    if not json_files:
        print("No save files found.")
    else:
        for file_path in json_files:
            print(f"- {file_path.name}")


def main() -> None:
    base_dir = get_project_base()
    data_dir = get_data_dir(base_dir)

    # Concept check: CWD is useful information, but not our path anchor.
    print(f"CWD (conceptual): {Path.cwd()}")
    print(f"Base directory (implementation): {base_dir}")

    ensure_directory(data_dir)

    primary_file = data_dir / "data.json"
    payload: dict[str, Any] = {
        "course": "python_basics",
        "hour": 43,
        "topic": "pathlib_directories",
    }
    save_json(primary_file, payload)
    print(f"Saved JSON to: {primary_file}")

    all_items = discover_all_files(data_dir)
    json_files = discover_json_files(data_dir)
    print_discovery(all_items, json_files)

    chosen = choose_deterministic(json_files)
    if chosen is None:
        print("\nChosen JSON file: None")
    else:
        print(f"\nChosen JSON file (deterministic): {chosen}")


if __name__ == "__main__":
    main()
```

---

## Debrief prompts (last 5 minutes)

Use 2–4 of these questions:

1. “What problem does `pathlib` solve compared with manual string path building?”
2. “What is CWD, and why can relying on it be risky?”
3. “What does `mkdir(exist_ok=True)` buy us in day-to-day coding?”
4. “Why sort `glob()` results before selecting a file?”
5. “How does directory discovery reduce hardcoded assumptions?”

Invite one student to explain:

“How would you adapt today’s pattern if your script were in `src/` and `data/` were at project root?”

Expected idea:

- Adjust base directory once (for example `Path(__file__).resolve().parent.parent`) and keep the rest unchanged.

---

## Quick-check / exit ticket

**Question:** What is the difference between a relative path and an absolute path, and why do we prefer project-relative path construction in shared code?

**Strong answer:**
An absolute path contains a full machine-specific location from the drive/root (for example a full `C:\...` path). A relative path is interpreted from a base location. In shared code, we prefer constructing paths from a stable project/script-relative base so the code works across machines and different terminal start locations. We can inspect `Path.cwd()` to understand runtime context, but we should avoid making CWD the final dependency for core file paths.

---

## Instructor close-out reminder

Before ending the hour, reinforce one sentence:

“Reliable Python file handling starts with reliable path construction: anchor to project/script root, create folders safely, discover files dynamically, and keep behavior deterministic.”

---

## Extended instructor speaking script (optional near-verbatim delivery)

Use this when you want a slower, fully narrated version of the hour. You can read this almost directly.

“Team, today we are solving a real software reliability problem: paths that work on my machine but fail on yours. This is one of the most common beginner-to-intermediate pain points, and fixing it now will save you time for the rest of this course and in real jobs.

Let’s start with a quick truth: files are not floating in space. Every file path is interpreted from somewhere. If that ‘somewhere’ is unstable, your program becomes unstable. That ‘somewhere’ is often the current working directory. If your terminal starts in a different folder, your file path can silently point to the wrong place.

Here is where many people get tricked: they run their code from an IDE, and the IDE quietly uses the project folder as working directory. Everything looks correct. Then they run the same script in a plain terminal started elsewhere and suddenly get `FileNotFoundError`. So the code wasn’t truly robust. It was accidentally correct in one environment.

Our goal today is not to memorize `pathlib` methods. Our goal is to adopt a reliable mental model:

1. choose a stable base path once
2. build all internal data paths from that base
3. create required folders safely
4. discover what files exist instead of assuming file names
5. make selection behavior deterministic

If you implement those five ideas, your code quality jumps immediately.

Now, concept check: what is an absolute path? Full path from drive/root. What is a relative path? Path interpreted from a base location. Are relative paths bad? No. They are excellent if you control the base correctly.

And this is our key nuance: we teach `Path.cwd()` because it explains behavior, but we do not anchor core app data logic to CWD. Instead, we anchor to script/project location. That gives us stability across launch contexts.

You may wonder, ‘Can I ever use `Path.cwd()` in real code?’ Yes, for diagnostics, for CLI tools intentionally designed around working directory, or for specific workflows where CWD is the contract. But for today’s persistent app data in a project repository, script/project-relative is the better default.

Second concept: folder creation. Robust scripts are rerunnable. If I run the same script ten times, it should not fail on run two because a directory already exists. `mkdir(exist_ok=True)` gives us rerun safety.

Third concept: discovery. Hardcoded file names seem easy until the first rename, backup, or versioned save file. If your app can inspect `data/` and identify all JSON files, you can adapt to changes with minimal code edits.

Fourth concept: deterministic ordering. Operating systems and filesystems do not guarantee the same order when listing files. If you pick ‘the first file’ without sorting, your behavior may differ across machines. Sorting is a tiny step that prevents inconsistent outcomes.

As we code, I want you to keep asking: ‘Is this robust if someone else runs it from a different place?’ That question is what professional developers ask every day.

In lab time, I care less about fancy output and more about path reliability. If your script correctly creates `data/`, writes `data/data.json`, lists files, handles no-files case, and deterministically chooses one JSON file when multiple exist, you have met the real goal.

Let’s build this carefully and narrate each choice so you understand not just what to type, but why each line exists.”

---

## Guided Q&A prompts to deepen understanding

Use these during lecture or lab debrief. Each prompt includes a model explanation you can paraphrase.

### Prompt 1

**Ask:** “Why is `Path(__file__).resolve().parent` usually more stable than `Path.cwd()` for app data paths?”

**Model explanation:**
`__file__` points to the script location, which usually stays tied to project layout. `Path.cwd()` depends on where the command was launched. Since launch location changes frequently, CWD-based paths can break unexpectedly. Script-relative anchoring reduces that variability.

### Prompt 2

**Ask:** “What does `exist_ok=True` protect us from?”

**Model explanation:**
It prevents `mkdir` from raising an error when the directory already exists, making scripts safe to rerun.

### Prompt 3

**Ask:** “Why use `glob("*.json")` instead of hardcoding `data.json`?”

**Model explanation:**
Discovery supports multiple files, renamed files, and dynamic workflows. Hardcoding one file name locks behavior and fails when naming changes.

### Prompt 4

**Ask:** “Why sort file lists before choosing one?”

**Model explanation:**
Directory iteration order is not guaranteed. Sorting guarantees reproducible behavior and avoids machine-dependent selection differences.

### Prompt 5

**Ask:** “Is absolute path always wrong?”

**Model explanation:**
No, absolute paths can be useful in specific system tasks, deployment scripts, or controlled environments. But for shared classroom projects, hardcoded personal absolute paths are fragile and not portable.

### Prompt 6

**Ask:** “What does ‘within reason’ mean when we test from different terminal starts?”

**Model explanation:**
It means we test realistic launch contexts (project folder, parent folder, IDE terminal), but we still assume the project structure exists and script location is valid. We are not testing broken installations.

---

## Troubleshooting playbook for instructor (rapid diagnosis)

Use this checklist when a learner says, “It doesn’t work.”

### Step A: Read the exact error, don’t guess

Ask learner to read the full traceback. Identify:

- exception type (`FileNotFoundError`, `PermissionError`, etc.)
- exact line number
- exact path shown

Most path bugs are obvious once the printed path is inspected.

### Step B: Print path diagnostics

Have learner add:

```python
print(f"CWD: {Path.cwd()}")
print(f"Script file: {Path(__file__).resolve()}")
print(f"Base dir: {base_dir}")
print(f"Data dir: {data_dir}")
```

Compare expected and actual values.

### Step C: Validate directory exists when expected

Have learner run:

```python
print(data_dir.exists(), data_dir.is_dir())
```

If false, check whether `mkdir` executed before write operations.

### Step D: Validate file discovery assumptions

If learner expects JSON files but sees none, ask them to print:

```python
for item in sorted(data_dir.iterdir(), key=lambda p: p.name.lower()):
    print(item.name)
```

Sometimes files exist but have a different extension (`.JSON`, `.txt`, typo).

### Step E: Confirm deterministic choice logic

If chosen file seems inconsistent, check that sorting is present **before** choosing first item.

### Step F: Check for hidden platform gotchas

- Windows backslash vs forward slash issues are mostly solved by using `Path`.
- Case sensitivity varies by filesystem; sorting with `.lower()` helps stable display.
- Locked files can produce permission errors; ask learner to close editors/viewers that hold locks.

### Step G: Keep fixes minimal and test incrementally

After each fix, rerun and observe output. Avoid rewriting everything at once.

Instructor note:

When many students fail similarly, stop and do a 3-minute class reset:

1. show base path pattern again
2. show `mkdir(exist_ok=True)` again
3. show sorted `glob` again

This usually resolves most blockers quickly.

---

## Additional lab facilitation notes (for mixed-pace classrooms)

### Fast-finishers

Give them one of these:

1. Add command-line flag to print absolute chosen path only.
2. Add function that returns summary dictionary:
   - total items
   - total JSON files
   - chosen file name or `None`
3. Add secondary deterministic rule (for discussion only), such as choose newest file after sorted tie-break by name.

Keep scope within Basics and avoid external packages.

### Learners needing support

Provide a reduced target:

1. Make `data/` directory.
2. Save `data/data.json`.
3. Print files with `iterdir()`.

Then layer:

4. `glob("*.json")`
5. sorted results
6. no-files branch
7. deterministic chosen file

This scaffolding prevents overwhelm.

### Pairing strategy

For struggling groups, pair one “navigator” and one “driver”:

- Driver types only.
- Navigator reads requirements and checks completion criteria.
- Switch roles every 6–8 minutes.

This keeps both learners engaged and reduces passive watching.

---

## Rubric-style feedback phrases (copy/paste ready)

Use these concise comments when reviewing student work.

### Strong

- “Great reliability pattern: script-relative base + `pathlib` path joins.”
- “Nice rerunnable folder setup with `mkdir(exist_ok=True)`.”
- “Excellent deterministic handling: sorted `glob` before selecting first file.”
- “Clear no-files branch prevents index errors and improves user feedback.”

### Needs improvement

- “Current solution depends on CWD; anchor to script/project location for portability.”
- “Hardcoded personal absolute path limits shareability. Replace with project-relative construction.”
- “Please sort glob results before choosing one file to keep behavior deterministic.”
- “Handle empty JSON list explicitly before indexing.”

---

## Final recap script (1–2 minutes)

Use this closing language to consolidate transfer:

“Today you moved from file access that works accidentally to file access that works intentionally.
You learned:

- how to reason about relative vs absolute paths
- how CWD affects relative paths
- why we inspect CWD but avoid depending on it for core app data
- how to anchor paths to script/project location
- how to create directories safely with `mkdir(exist_ok=True)`
- how to discover files with `iterdir()` and `glob()`
- why sorted discovery gives deterministic, repeatable behavior

If you keep these habits in your next project, your code will be easier to run, easier to debug, and easier to share.”
