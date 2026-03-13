# Day 11, Hour 1: Files – Reading and Writing Text

## 🎯 Outcomes
*   Open files using `with`.
*   Read lines and write lines.

## 🗣️ Instructor Talk Points (10–15 min)

*   **File paths and working directory**: Explain how Python finds files. By default, it looks in the folder where the script is run (the current working directory).
*   **Context Managers (`with`)**: Introduce `with open("filename.txt", "mode") as f:`. This is the Pythonic way to handle files because it automatically closes the file when the block ends, even if an error occurs.
    *   **Modes**:
        *   `"r"`: Read (default)
        *   `"w"`: Write (overwrites existing content)
        *   `"a"`: Append (adds to the end)
*   **Reading Methods**:
    *   `f.read()`: Reads the entire file into a single string.
    *   `f.readlines()`: Reads the file into a list of strings (one per line).
*   **Writing Methods**:
    *   `f.write("text")`: Writes a string to the file. Remember to add `\n` manually if you want newlines!

## 💻 Live Demo (5–10 min)

**Demo**: Write a shopping list to a file; then read and print it.

```python
# 1. Writing to a file using 'w'
shopping_list = ["Apples", "Bananas", "Bread", "Milk"]

print("Writing shopping list...")
with open("shopping.txt", "w") as f:
    for item in shopping_list:
        # We MUST add the newline character manually when writing
        f.write(item + "\n")
        
print("File saved successfully.\n")

# 2. Reading from the file using 'r'
print("Reading shopping list back:")
try:
    with open("shopping.txt", "r") as f:
        # Read lines into a list
        lines = f.readlines()
        
        # Strip newline characters and print
        for i, line in enumerate(lines, 1):
            clean_item = line.strip() 
            print(f"{i}. {clean_item}")
except FileNotFoundError:
    print("Oops! The file 'shopping.txt' was not found.")
```

*   **Instructor Note**: Emphasize how `\n` was necessary during the `write` step, and `.strip()` was necessary to remove it during the `read` step so that we didn't print extra blank lines.

## 🛠️ Hands-on Lab (25–35 min)

### Lab: Save and Load (Text)

**Prompt:**
1.  Write your contacts or daily tasks to a text file (one per line). Keep the format simple (e.g., `Name | Phone` or just the task name).
2.  Load the items back from the file.
3.  Print them to the console in a clear, numbered list format.

**Completion Criteria:**
*   File is created and reloaded correctly.
*   Learner can locate the text file on their disk/workspace.
*   The script runs without throwing a FileNotFoundError.

**Common Pitfalls to Watch For:**
*   Wrong file path or running the script from the wrong working directory.
*   Forgetting to add newline (`\n`) characters when writing, resulting in all text mashed onto one line.
*   Using `'w'` mode to add an item later (which erases the file) instead of `'a'` (append).

**Optional Extensions (stay in Basics scope):**
*   Add a timestamp header line to the top of the file using the `datetime` module.
*   Export a "pretty report" version of the file that adds borders or extra formatting before saving.

## ✅ Quick Check / Exit Ticket
**Question:** Why is using `with` (a context manager) recommended for file handling instead of just calling `file = open(...)` and `file.close()`?
**Answer:** The `with` block guarantees that the file will be closed properly as soon as the block finishes, even if an error crashes the program inside the block. This prevents file corruption and resource leaks.
