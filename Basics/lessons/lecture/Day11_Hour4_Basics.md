# Day 11, Hour 4: Exception Handling

## 🎯 Outcomes
*   Use `try/except` to catch common runtime errors.
*   Catch specific exceptions when practical.

## 🗣️ Instructor Talk Points (10–15 min)

*   **Exceptions vs Syntax Errors**: Syntax errors prevent code from running at all (e.g., missing a quote). Exceptions happen *during runtime* when syntactically correct code tries to do something impossible (e.g., dividing by zero or opening a file that doesn't exist).
*   **The `try/except` block**: How we "catch" exceptions instead of letting the program crash.
    *   `try`: Put the risky code here.
    *   `except`: Put the code to handle the error here. This only runs if an error happened in the `try` block.
*   **Catching Specific Exceptions**: Introduce common built-in Python exceptions:
    *   `ValueError`: E.g., trying to parse `"xyz"` as an integer.
    *   `FileNotFoundError`: Trying to read a file that isn't there.
    *   `TypeError`: E.g., adding an integer to a string.
*   **The Problem with a Bare `except:`**: Catching *all* exceptions broadly (like `except Exception:`) is generally bad practice because it can hide unexpected bugs (like a typo in a variable name). Always catch *specific* errors.
*   **`else` and `finally`**:
    *   `else`: Runs only if *no* exception occurred in the `try` block.
    *   `finally`: Runs *always*, no matter what (good for cleaning up resources, though less necessary with `with open()`).

## 💻 Live Demo (5–10 min)

**Demo**: Wrap numeric user input and file loading in `try/except` blocks to show friendly error handling.

```python
import json

# Example 1: Handling bad user input (ValueError)
while True:
    try:
        user_input = input("Enter a positive number: ")
        number = int(user_input)
        if number < 0:
            print("That's not positive!")
        else:
            print(f"Great! I love the number {number}.")
            break # Break out of the loop if successful
    except ValueError:
        print("Error: That wasn't a valid number. Try again.")

# Example 2: Handling file errors
file_path = "nonexistent_file.json"
print("\nAttempting to load configuration...")
try:
    with open(file_path, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"Error: The configuration file '{file_path}' was not found.")
except json.JSONDecodeError:
    print("Error: The file exists, but it contains invalid JSON.")
except Exception as e:
    # A generic catch-all at the very end as a last resort
    print(f"An unexpected error occurred: {e}")
else:
    # This block only runs if NO errors occurred
    print("Configuration loaded successfully!")
```

## 🛠️ Hands-on Lab (25–35 min)

### Lab: Harden Your Program

**Prompt:**
1.  Take an existing script (like the text-parsing, tip calculator, or the JSON loading activity from Hour 2).
2.  Add a `try/except` block around any numeric input conversions (`int()` or `float()`).
3.  Add a `try/except` block around the JSON load or text file read step.
4.  On error, show a friendly message and allow the program to continue running (for example, by having the input prompt inside a `while` loop that doesn't break until the input is successful).

**Completion Criteria:**
*   The program continues gracefully after bad input (e.g., user types `"five"` instead of `5`).
*   The program handles missing or corrupt files gracefully instead of crashing abruptly.
*   Exception handling is kept *specific* when possible (`ValueError`, `FileNotFoundError`).

**Common Pitfalls to Watch For:**
*   Catching `Exception` broadly everywhere, which can inadvertently swallow unrelated logic errors.
*   Swallowing errors silently (using `pass` inside an `except` block with no `print` message) so the user is confused about what happened.

**Optional Extensions (stay in Basics scope):**
*   Log the errors to a separate text file called `error_log.txt` (keeping it simple with `with open("error_log.txt", "a")`.

## ✅ Quick Check / Exit Ticket
**Question:** Why is catching a *specific* exception (like `ValueError`) considered better practice than catching *all* exceptions (`except Exception:`)?
**Answer:** Catching all exceptions risks masking other underlying problems. For instance, if you have a typo in your script that throws a `NameError`, a broad `except` block might hide that crash and pretend it was just a file loading issue, making it impossible to debug. Catching specific errors tells you exactly what went wrong and how to handle it.
