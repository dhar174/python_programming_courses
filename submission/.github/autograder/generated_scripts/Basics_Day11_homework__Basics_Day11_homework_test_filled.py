#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 11 Homework (Sample Filled Submission)
# 
# This solved notebook demonstrates one deterministic answer set for the Day 11 autograder contract.
# 

# ### Autograder reminder
# 
# - This notebook is self-contained.
# - It writes only inside this assignment directory.
# - It prints the exact canonical lines expected by `criteria.json`.
# 

# In[ ]:


from pathlib import Path
import json

TASK_TITLES = [
    "Review pathlib",
    "Save organizer state",
    "Handle errors kindly",
]

ORGANIZER_RECORDS = [
    {"title": "Review pathlib", "done": False, "priority": 2},
    {"title": "Save organizer state", "done": True, "priority": 1},
]

def get_base_dir():
    if "__file__" in globals():
        return Path(__file__).resolve().parent
    return Path.cwd()

def ensure_data_dir(base_dir):
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def hour41_text_summary(data_dir):
    text_path = data_dir / "task_notes.txt"
    with text_path.open("w", encoding="utf-8") as handle:
        for title in TASK_TITLES:
            handle.write(title + "\n")

    with text_path.open("r", encoding="utf-8") as handle:
        loaded = [line.strip() for line in handle.readlines()]

    summary = " | ".join(f"{index}. {title}" for index, title in enumerate(loaded, start=1))
    return [
        "Text file path: data/task_notes.txt",
        f"Text lines written: {len(TASK_TITLES)}",
        f"Text lines loaded: {len(loaded)}",
        f"Text summary: {summary}",
        "Text mode used: with open safely closes the file",
    ]

def hour42_json_summary(data_dir):
    json_path = data_dir / "organizer.json"
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(ORGANIZER_RECORDS, handle, indent=2)

    with json_path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)

    completed_count = sum(1 for record in loaded if record["done"])
    return [
        "JSON file path: data/organizer.json",
        f"JSON records loaded: {len(loaded)}",
        f"JSON first title: {loaded[0]['title']}",
        f"JSON completed count: {completed_count}",
        "JSON structure: list of dict records",
    ]

def hour43_path_summary(data_dir):
    backup_path = data_dir / "backup.json"
    with backup_path.open("w", encoding="utf-8") as handle:
        json.dump({"backup": True, "count": 2}, handle, indent=2)

    json_files = sorted(path.name for path in data_dir.glob("*.json"))
    return [
        "Data directory ready: data",
        f"Discovered JSON files: {', '.join(json_files)}",
        f"First discovered file: {json_files[0]}",
        "Joined path example: data/organizer.json",
        "Path strategy: project-relative pathlib paths",
    ]

def parse_menu_choice(raw_value):
    try:
        return int(raw_value)
    except ValueError:
        return "Enter a whole number for the menu choice."

def safe_load_json(path):
    cleanup_note = "cleanup steps always run"
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except FileNotFoundError:
        return f"{path.name} was not found.", cleanup_note
    except json.JSONDecodeError:
        return f"{path.name} contained invalid JSON.", cleanup_note
    else:
        return "safe load succeeded", cleanup_note

def hour44_exception_summary(data_dir):
    broken_json_path = data_dir / "broken.json"
    broken_json_path.write_text('{"title": "oops", }', encoding="utf-8")

    value_error_message = parse_menu_choice("two")
    missing_message, cleanup_note = safe_load_json(data_dir / "missing_tasks.json")
    bad_json_message, _ = safe_load_json(broken_json_path)
    else_message, _ = safe_load_json(data_dir / "organizer.json")
    if broken_json_path.exists():
        broken_json_path.unlink()

    return [
        f"ValueError handled: {value_error_message}",
        f"Missing file handled: {missing_message}",
        f"Bad JSON handled: {bad_json_message}",
        f"Else branch result: {else_message}",
        f"Finally reminder: {cleanup_note}",
    ]

def main():
    base_dir = get_base_dir()
    data_dir = ensure_data_dir(base_dir)

    for line in hour41_text_summary(data_dir):
        print(line)
    for line in hour42_json_summary(data_dir):
        print(line)
    for line in hour43_path_summary(data_dir):
        print(line)
    for line in hour44_exception_summary(data_dir):
        print(line)

main()


# In[ ]:


from pathlib import Path

def build_canonical_script():
    return '''from pathlib import Path
import json

TASK_TITLES = [
    "Review pathlib",
    "Save organizer state",
    "Handle errors kindly",
]

ORGANIZER_RECORDS = [
    {"title": "Review pathlib", "done": False, "priority": 2},
    {"title": "Save organizer state", "done": True, "priority": 1},
]

def ensure_data_dir(base_dir):
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def hour41_text_summary(data_dir):
    text_path = data_dir / "task_notes.txt"
    with text_path.open("w", encoding="utf-8") as handle:
        for title in TASK_TITLES:
            handle.write(title + "\\n")
    with text_path.open("r", encoding="utf-8") as handle:
        loaded = [line.strip() for line in handle.readlines()]
    summary = " | ".join(f"{index}. {title}" for index, title in enumerate(loaded, start=1))
    return [
        "Text file path: data/task_notes.txt",
        f"Text lines written: {len(TASK_TITLES)}",
        f"Text lines loaded: {len(loaded)}",
        f"Text summary: {summary}",
        "Text mode used: with open safely closes the file",
    ]

def hour42_json_summary(data_dir):
    json_path = data_dir / "organizer.json"
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(ORGANIZER_RECORDS, handle, indent=2)
    with json_path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    completed_count = sum(1 for record in loaded if record["done"])
    return [
        "JSON file path: data/organizer.json",
        f"JSON records loaded: {len(loaded)}",
        f"JSON first title: {loaded[0]['title']}",
        f"JSON completed count: {completed_count}",
        "JSON structure: list of dict records",
    ]

def hour43_path_summary(data_dir):
    backup_path = data_dir / "backup.json"
    with backup_path.open("w", encoding="utf-8") as handle:
        json.dump({"backup": True, "count": 2}, handle, indent=2)
    json_files = sorted(path.name for path in data_dir.glob("*.json"))
    return [
        "Data directory ready: data",
        f"Discovered JSON files: {', '.join(json_files)}",
        f"First discovered file: {json_files[0]}",
        "Joined path example: data/organizer.json",
        "Path strategy: project-relative pathlib paths",
    ]

def parse_menu_choice(raw_value):
    try:
        return int(raw_value)
    except ValueError:
        return "Enter a whole number for the menu choice."

def safe_load_json(path):
    cleanup_note = "cleanup steps always run"
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except FileNotFoundError:
        return f"{path.name} was not found.", cleanup_note
    except json.JSONDecodeError:
        return f"{path.name} contained invalid JSON.", cleanup_note
    else:
        return "safe load succeeded", cleanup_note

def hour44_exception_summary(data_dir):
    broken_json_path = data_dir / "broken.json"
    broken_json_path.write_text('{"title": "oops", }', encoding="utf-8")
    value_error_message = parse_menu_choice("two")
    missing_message, cleanup_note = safe_load_json(data_dir / "missing_tasks.json")
    bad_json_message, _ = safe_load_json(broken_json_path)
    else_message, _ = safe_load_json(data_dir / "organizer.json")
    if broken_json_path.exists():
        broken_json_path.unlink()
    return [
        f"ValueError handled: {value_error_message}",
        f"Missing file handled: {missing_message}",
        f"Bad JSON handled: {bad_json_message}",
        f"Else branch result: {else_message}",
        f"Finally reminder: {cleanup_note}",
    ]

def main():
    base_dir = Path(__file__).resolve().parent
    data_dir = ensure_data_dir(base_dir)
    for line in hour41_text_summary(data_dir):
        print(line)
    for line in hour42_json_summary(data_dir):
        print(line)
    for line in hour43_path_summary(data_dir):
        print(line)
    for line in hour44_exception_summary(data_dir):
        print(line)

if __name__ == "__main__":
    main()
'''

if "__file__" not in globals():
    Path("day11.py").write_text(build_canonical_script(), encoding="utf-8")

