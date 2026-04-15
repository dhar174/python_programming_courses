# Day 11 — Session 11: File I/O, JSON, Paths & Exception Handling

**Course:** Python Programming (Basic)  
**Day:** 11 · Session 11  
**Hours covered:** 41–44  
**Slides:** [`day-11-session-11.html`](day-11-session-11.html) &nbsp;(64 slides)

---

## Session Overview

| Hour | Topic | Key Concept |
|------|-------|-------------|
| 41 | Files — reading and writing text | `with open()`, context manager, `read()` / `write()` |
| 42 | JSON persistence (stdlib json) | `json.dump()` / `json.load()`, `to_dict()` / `from_dict()` |
| 43 | Directories + paths (pathlib preferred) | `Path`, `mkdir(exist_ok=True)`, `iterdir()`, `glob()` |
| 44 | Exception handling (full Basics treatment) | `try/except/else/finally`, specific exceptions, safe patterns |

---

## Learning Outcomes

By the end of Session 11, learners can:

### Hour 41 — Files: reading and writing text
- Open a file safely using `with open()`
- Read all file content with `read()`, iterate lines with `readlines()` or direct iteration
- Write lines to a file with `write()`, remembering to include `\n`
- Explain why `with` is preferred over manual `open()`/`close()`
- Check whether a file exists with `os.path.exists()` before reading

### Hour 42 — JSON persistence
- Serialize a Python dict or list to a JSON file with `json.dump()`
- Load JSON back into Python with `json.load()`
- Identify which Python types map to valid JSON
- Add `to_dict()` and `from_dict()` helpers to a class for JSON compatibility
- Explain why custom objects cannot be passed directly to `json.dump()`

### Hour 43 — Directories + paths (pathlib)
- Use `pathlib.Path` to build portable file paths with the `/` operator
- Create a `data/` directory safely using `mkdir(exist_ok=True)`
- List directory contents with `iterdir()` and filter with `glob()`
- Anchor paths to the script's own directory with `Path(__file__).parent`
- Distinguish relative paths from absolute paths

### Hour 44 — Exception handling
- Use `try/except` to catch and handle runtime errors gracefully
- Distinguish the `try`, `except`, `else`, and `finally` clauses
- Catch specific exceptions: `ValueError`, `FileNotFoundError`, `json.JSONDecodeError`
- Write a robust `get_int()` input loop that retries on bad input
- Explain why catching `Exception` broadly is discouraged

---

## Labs

| Hour | Lab | Timebox | Description |
|------|-----|---------|-------------|
| 41 | Save and Load (text) | 30 min | Write contacts to a `.txt` file one-per-line (`name\|phone`); load back and print |
| 42 | Save and Load (JSON) | 30 min | Export `Contact` objects to `data.json`; reload on startup; no crash if missing |
| 43 | Data folder | 30 min | Create `data/` with pathlib; save/load `data/contacts.json`; print `data/` contents |
| 44 | Harden your program | 30 min | Wrap JSON load and `int()` conversions in `try/except`; show friendly errors |

---

## Files

| File | Description |
|------|-------------|
| [`day-11-session-11.html`](day-11-session-11.html) | Self-contained HTML slide deck (64 slides) |
| [`index.html`](index.html) | Session index / landing page |
| [`README.md`](README.md) | This file |

---

## Navigation

Inside the slide deck, use:

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| Swipe left/right | Mobile navigation |

---

## Scope Guardrail

This session stays within the **Basics** course scope.

Topics covered in this session:
- File I/O with `with open()` — text files
- JSON serialization/deserialization with the stdlib `json` module
- Path handling with `pathlib.Path`
- Exception handling: `try/except/else/finally`, specific exceptions

Topics **excluded from full coverage** (covered in the Advanced course; only brief, optional previews may appear):

| Topic | Why It Is Advanced |
|-------|------------------|
| Custom exception classes (`class MyError(Exception)`) | Requires inheritance understanding |
| Exception chaining (`raise X from Y`) | Advanced error propagation patterns |
| Custom context managers (`__enter__` / `__exit__`) | Advanced OOP and protocol design |
| `contextlib.contextmanager` decorator | Advanced generator-based context managers |
| Binary file I/O (`"rb"`, `"wb"`) | Encoding details and struct module |
| `csv` module | Structured text formats — Advanced course |
| `pickle` module | Security implications — not a safe beginner tool |
| Database persistence (`sqlite3`) | Requires SQL knowledge — Advanced |
| Advanced `pathlib` (`symlink_to`, `chmod`, `stat`) | OS-level file operations |
| `logging` module | Structured logging — Advanced error handling |

---

*Generated from `Basics/lessons/slides/day-11/day-11-session-11.md`*
