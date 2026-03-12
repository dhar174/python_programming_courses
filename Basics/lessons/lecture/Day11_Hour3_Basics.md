# Day 11, Hour 3: Directories and Paths

## 🎯 Outcomes
*   Use `pathlib` to build reliable paths.
*   Create a data directory if needed.
*   List directory contents (`iterdir` / `glob`) to discover available files.

## 🗣️ Instructor Talk Points (10–15 min)

*   **Relative vs Absolute Paths**: Explain that absolute paths (`C:\Users\Name\Desktop\file.txt`) break if the code moves. Relative paths (`data\file.txt`) are relative to the *working directory* where the script was run.
*   **The Problem with `open("data.txt")`**: Depending on where the terminal is opened, the script might look in the wrong place. We need a reliable way to compute paths.
*   **Introducing `pathlib`**: It's Python's modern, object-oriented way to handle paths. Instead of strings, we use `Path` objects.
    *   `Path.cwd()`: Gets the current working directory.
    *   Building paths: `Path("data") / "user.json"` (Note the clever use of `/` to join paths).
*   **Creating Folders Safely**: `Path("data").mkdir(exist_ok=True)`. This creates the folder and safely ignores the command if it already exists without crashing.
*   **Listing Files**: Why list files? To "discover" save files instead of hardcoding their names.
    *   `Path("data").iterdir()`: Loops over everything in the folder.
    *   `Path("data").glob("*.json")`: Finds all files matching the pattern.
*   **Path Best Practice (Portable)**: Create a project-relative base directory derived from the script location and join it into `data/`. Avoid pointing directly to a user's `Downloads` or `Desktop` folder.

## 💻 Live Demo (5–10 min)

**Demo**: Create a `data/` folder, write a file into it natively, list contents, and print found JSON files.

```python
import json
from pathlib import Path

# 1. Define folder path safely inside cwd
data_dir = Path.cwd() / "data"

# Create the folder if it doesn't already exist
data_dir.mkdir(exist_ok=True)
print(f"Ensured data directory exists at: {data_dir}")

# 2. Write a file INTO that folder using pathlib's '/' operator
save_file = data_dir / "save1.json"

dummy_data = {"score": 100, "level": 5}
with open(save_file, "w") as f:
    json.dump(dummy_data, f)
print(f"Saved dummy data to: {save_file}\n")

# 3. List contents to discover save files using .glob()
print("Discovering save files...")
found_files = list(data_dir.glob("*.json"))

if not found_files:
    print("No save files found.")
else:
    for f in found_files:
        print("- Found:", f.name) # .name gives just the filename, not the whole path
```

## 🛠️ Hands-on Lab (25–35 min)

### Lab: Data Directory

**Prompt:**
1.  Use `pathlib` to create a `data/` folder safely.
2.  Save some JSON data (like game scores or settings) into `data/data.json`. Ensure your program runs without crashing regardless of where the terminal starts (within reason).
3.  Print the names of all `.json` files currently existing in `data/`.
4.  If multiple JSON files exist, list them out and try to intelligently load the first match.

**Completion Criteria:**
*   Uses `pathlib` or `os.path` to correctly target the `data/` folder.
*   The folder is created safely with `exist_ok=True`.
*   Learner successfully lists directory contents and can dynamically identify which json data file path they are loading.

**Common Pitfalls to Watch For:**
*   Hard-coding absolute paths (`/users/bob/python/...`), which breaks on other machines.
*   Running from an unexpected or different working directory which breaks the relative assumption behind `Path.cwd()`.

**Optional Extensions (stay in Basics scope):**
*   Add a feature to let the user select the save file they want to load.

## ✅ Quick Check / Exit Ticket
**Question:** What’s the difference between a relative and an absolute path, and why do we prefer relative paths when sharing code?
**Answer:** Absolute paths define exactly where a file exists from the hard drive's root letter (e.g. `C:\`). A relative path describes where a file is starting *from* the folder where the program is executed. Relative paths allow code to be zipped up, shared, and run on another computer without breaking.
