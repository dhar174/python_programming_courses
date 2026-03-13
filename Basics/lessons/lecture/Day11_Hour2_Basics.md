# Day 11, Hour 2: JSON Persistence

## 🎯 Outcomes
*   Serialize data to JSON.
*   Load JSON back into Python structures.

## 🗣️ Instructor Talk Points (10–15 min)

*   **What is JSON?**: JavaScript Object Notation. It's a lightweight, standard format for storing and transporting data. Even though "JavaScript" is in the name, it's used by almost every programming language.
*   **The `json` Module**: Python's standard library includes the `json` module, so there's nothing to install.
    *   `json.dump(data, file)`: Writes Python data to a file in JSON format.
    *   `json.load(file)`: Reads JSON data from a file and converts it back into Python data.
*   **What JSON can store**: 
    *   Dictionaries (`dict`) become JSON objects.
    *   Lists (`list`) and Tuples (`tuple`) become JSON arrays.
    *   Strings (`str`), Numbers (`int`, `float`), Booleans (`True`, `False` -> `true`, `false`), and `None` (`null`).
*   **Mapping objects**: You can't directly dump custom class objects. You must convert them to dictionaries first (e.g., using a `.to_dict()` method or reading their `.__dict__` attribute).

## 💻 Live Demo (5–10 min)

**Demo**: Dump a dictionary (representing user settings) to `data.json`, load it back, and print it.

```python
import json

# 1. Create some data (a dictionary)
user_settings = {
    "username": "python_student",
    "theme": "dark",
    "notifications_enabled": True,
    "volume": 0.8
}

print("Saving settings...")
# Write data to a JSON file
with open("data.json", "w") as f:
    # indent=4 makes the file readable for humans!
    json.dump(user_settings, f, indent=4) 

print("Settings saved successfully.\n")

# 2. Reading the data back from the JSON file
print("Loading settings...")
try:
    with open("data.json", "r") as f:
        loaded_settings = json.load(f)
        
    print("Welcome back,", loaded_settings["username"])
    print("Theme is set to:", loaded_settings["theme"])
    print("Type of loaded_settings:", type(loaded_settings)) # Prove it's a dict!
except FileNotFoundError:
    print("No settings file found. Using defaults.")
except json.JSONDecodeError:
    print("The settings file is corrupted!")
```

## 🛠️ Hands-on Lab (25–35 min)

### Lab: Save and Load (JSON)

**Prompt:**
1.  Take an app from a previous day (like the contact manager or a simple to-do list) and export its data to `data.json` instead of a regular text file.
2.  On startup, write code to try and load `data.json` if it is present. If it doesn't exist, start with an empty dictionary or list.
3.  After changes are made to the data during the app's run, save them again.

**Completion Criteria:**
*   Data persists across runs of the script correctly.
*   The script does not crash when the file is missing (use an `if` check with `os.path.exists()` or a `try/except` block).

**Common Pitfalls to Watch For:**
*   `JSONDecodeError`: This happens if the file gets corrupted or someone manually edits it with a syntax mistake.
*   Trying to use `json.dump()` directly on a custom object instead of converting it to a basic data type (like a dictionary) first.

**Optional Extensions (stay in Basics scope):**
*   Add a feature to backup the previous JSON file before overwriting it.
*   Use `indent=2` or `indent=4` in `json.dump()` to make the JSON file "pretty-printed" and easy to read.

## ✅ Quick Check / Exit Ticket
**Question:** Why can’t `json.dump()` write a custom object unless you convert it to a dictionary or another basic supported type first?
**Answer:** Because JSON is a standardized text format meant to be read by *any* language. It only understands basic generic structures like objects (mappings), arrays, strings, numbers, and booleans. It has no concept of a specific Python class or object memory structure.
