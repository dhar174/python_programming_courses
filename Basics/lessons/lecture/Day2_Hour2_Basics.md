# Day 2, Hour 2: String Methods - Normalize, Search, Replace

**Course Hour:** 6  
**Duration:** 60 minutes  
**Module:** Python Programming (Basic)

---

## Learning Outcomes

By the end of this hour, students will be able to:

1. **Use common string methods** (`lower()`, `upper()`, `strip()`, `replace()`, `find()`, `count()`) to transform and analyze text
2. **Explain why strings are immutable** and how method calls return new strings rather than modifying in place
3. **Decide when to use `find()` vs. `in` operator** based on whether you need the position or just presence detection
4. **Clean messy user input** by normalizing whitespace and case using method chaining
5. **Detect keyword presence** in text while handling capitalization variations and extra spaces

---

## ## Instructor Prep

### Preparation Time
- **Before class:** 15 minutes (review demo, test code in Python REPL)
- **Materials needed:** Python 3.x installed, code editor, terminal/console, internet for documentation lookups
- **Demo files:** Ensure you have a simple text editor or Jupyter notebook ready for live coding

### Key Concepts to Reinforce
- Strings in Python are **immutable sequences** — operations on strings return new strings
- String methods return values that must be assigned to a variable or printed to see results
- Method chaining allows combining multiple operations in one line
- Case sensitivity matters: `"Python"`, `"python"`, and `"PYTHON"` are treated differently
- Whitespace (spaces, tabs, newlines) is significant and must be handled explicitly

### Common Student Misconceptions (Preview)
1. Students expect `.replace()` to modify the original string (it doesn't)
2. `.find()` returns **position**, not True/False — students confuse it with containment checks
3. `.strip()` removes **only leading and trailing whitespace**, not embedded spaces
4. Case normalization should happen **before** searching or comparison for reliable results
5. The `.count()` method counts **non-overlapping occurrences** only

### Technology Check
- Verify Python 3.x is installed: `python --version`
- Ensure students can access Python REPL or editor
- Have a backup demo ready (screenshot or printed notes) in case of technical issues

---

## ## Opening Script

### Hook (2 minutes)
*Start with a real-world scenario:*

"Imagine you're building a customer support chatbot. Users type things like '  HELP ME  ', '  help me  ', and 'help  me'. Your bot needs to understand all three mean the same thing. How do you normalize that messy input? That's what we're covering today."

### Learning Path Overview (2 minutes)
"Today, we focus on three categories:
1. **Transformation**: Change strings (uppercase, lowercase, whitespace removal, replacement)
2. **Search & Analysis**: Find information (position, count, contains)
3. **Practical Application**: Combine these skills to process real-world text like user input, sensor data, or log files"

### Connection to Prior Knowledge (1 minute)
"Last hour, you learned that strings are sequences. Today, we harness that foundation: we'll use built-in methods to query and transform them efficiently."

---

## ## Core Concepts

### 1. String Immutability

**Definition:** Strings are **immutable** — once created, they cannot be changed. Operations on strings always return a new string.

**Why this matters:**
```python
message = "Hello"
message.upper()  # Returns "HELLO", but doesn't change message
print(message)   # Still prints "Hello"

# To keep the result, assign it:
message = message.upper()
print(message)   # Now prints "HELLO"
```

**Key consequence:** Always assign the return value to a variable if you want to use the transformed string.

### 2. Case Transformation

**Methods:**
- `.upper()` — Convert all characters to uppercase
- `.lower()` — Convert all characters to lowercase
- `.title()` — Convert to title case (first letter of each word uppercase)
- `.capitalize()` — Capitalize first letter, lowercase the rest
- `.swapcase()` — Swap case of each character

**Example:**
```python
user_input = "jAvA is GREAT"
clean = user_input.lower()  # "java is great"
title_form = user_input.title()  # "Java Is Great"
```

### 3. Whitespace Management

**Stripping methods:**
- `.strip()` — Remove leading and trailing whitespace
- `.lstrip()` — Remove leading whitespace only
- `.rstrip()` — Remove trailing whitespace only

**Important:** These methods do NOT remove embedded spaces.

**Example:**
```python
dirty = "  hello  world  "
print(dirty.strip())  # "hello  world" (outer spaces gone, inner double-space remains)
```

### 4. String Searching

**Methods:**
- `.find(substring)` — Returns index of first occurrence (or -1 if not found)
- `.count(substring)` — Returns number of non-overlapping occurrences
- `in` operator — Boolean check (True/False) for presence

**Choosing the right tool:**
```python
text = "Python is powerful"

# Use 'in' if you just need True/False:
if "is" in text:
    print("Word found")

# Use find() if you need the position:
pos = text.find("is")
print(pos)  # 7 (zero-indexed)

# Use count() if you need the total:
count = text.count("o")
print(count)  # 2
```

**Key detail:** `.find()` returns **-1** if not found, not **None** or **False**.

### 5. String Replacement

**Method:** `.replace(old, new[, count])`

**Behavior:**
- Replaces all occurrences by default (unless count limit is specified)
- Returns a new string; original is unchanged
- Case-sensitive by default

**Example:**
```python
text = "The cat sat on the mat"
result = text.replace("the", "the")  # No match (case-sensitive)
result = text.replace("the", "a")    # No change (uppercase "The" at start isn't matched)

# Correct approach:
result = text.lower().replace("the", "a")  # "a cat sat on a mat"
```

### 6. Method Chaining

Combine multiple methods in one expression:
```python
user_input = "  PYTHON IS AWESOME  "
clean = user_input.lower().strip().replace("awesome", "great")
print(clean)  # "python is great"
```

**Readability tip:** For long chains, break across lines:
```python
result = (user_input
    .lower()
    .strip()
    .replace("python", "java"))
```

---

## ## Live Coding Demo

### Demo Scenario: Email Validation Helper
*Duration: 8 minutes*

**Goal:** Show how string methods work together to validate and normalize an email prefix.

**Setup:**
```python
# Raw user input (messy)
email = "  JOHN.DOE@EXAMPLE.COM  "

# Step 1: Remove whitespace
email = email.strip()
print(f"After strip: '{email}'")

# Step 2: Lowercase everything
email = email.lower()
print(f"After lower: '{email}'")

# Step 3: Check if it's an email
if "@" in email:
    print("Valid format (contains @)")
    
# Step 4: Find the position of @
at_pos = email.find("@")
prefix = email[:at_pos]
print(f"Prefix: {prefix}")

# Step 5: Count dots in the entire email
dot_count = email.count(".")
print(f"Total dots: {dot_count}")
```

**Output:**
```
After strip: 'john.doe@example.com'
After lower: 'john.doe@example.com'
Valid format (contains @)
Prefix: john.doe
Total dots: 2
```

**Discussion Points:**
- Explain each step and why it matters
- Show what happens if you skip the `.strip()` step
- Demonstrate that `.lower()` is essential for consistent comparison
- Ask: "What if we wanted to replace 'doe' with 'smith'?" (show `.replace()`)

---

## ## Guided Lab: Text Sanitizer

**Lab Duration:** 30 minutes  
**Objective:** Build a function that cleans and analyzes user text input.

### Lab Prompt

You are building a **Text Sanitizer** for a chat application. Users type messy input with extra spaces and random capitalization. Your job:

1. **Clean the text:** Remove leading/trailing spaces, convert to lowercase
2. **Fix spacing issues:** Replace multiple consecutive spaces with a single space
3. **Detect a keyword:** Check if a specific keyword appears (case-insensitive) and report its count

**Input:** A sentence and a keyword (both strings)  
**Output:** Cleaned sentence and keyword count

### Starter Code
```python
def text_sanitizer(sentence, keyword):
    """
    Clean messy user input and detect keyword presence.
    
    Args:
        sentence (str): Raw user input with possible extra spaces/case variations
        keyword (str): Word to search for
    
    Returns:
        tuple: (cleaned_sentence, keyword_count)
    """
    # Your code here
    pass

# Test cases
print(text_sanitizer("  HELLO   WORLD  ", "hello"))  # Expected: ("hello world", 1)
print(text_sanitizer("Python IS great", "python"))    # Expected: ("python is great", 1)
print(text_sanitizer("  CAT  cat  CAT  ", "cat"))     # Expected: ("cat cat cat", 3)
```

### Lab Checkpoints

**Checkpoint 1: Whitespace & Case Normalization (8 min)**
- Strip leading/trailing spaces: `.strip()`
- Convert to lowercase: `.lower()`
- Test with one input
- Verify output is a clean string

**Checkpoint 2: Multiple Spaces Fix (8 min)**
- Handle multiple consecutive spaces (e.g., "hello    world" → "hello world")
- Use `.replace("  ", " ")` in a loop, or understand why it needs iteration
- Explain why a single `.replace()` might not catch all cases

**Checkpoint 3: Keyword Detection (8 min)**
- Use `.count()` to find keyword occurrences
- Ensure keyword is also normalized before counting
- Return both cleaned sentence and count as a tuple

**Solution (Full Implementation):**
```python
def text_sanitizer(sentence, keyword):
    # Normalize sentence: strip and lowercase
    cleaned = sentence.strip().lower()
    
    # Fix multiple spaces (keep replacing until no more double-spaces)
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    
    # Normalize keyword for searching
    keyword_normalized = keyword.lower()
    
    # Count occurrences of keyword
    count = cleaned.count(keyword_normalized)
    
    return cleaned, count

# Test cases
print(text_sanitizer("  HELLO   WORLD  ", "hello"))  # ("hello world", 1)
print(text_sanitizer("Python IS great", "python"))    # ("python is great", 1)
print(text_sanitizer("  CAT  cat  CAT  ", "cat"))     # ("cat cat cat", 3)
```

### Student Facilitation
- Circulate during checkpoint 1; look for students forgetting to assign the result
- For checkpoint 2, have students predict what a single `.replace("  ", " ")` does; test it
- For checkpoint 3, remind them to normalize the keyword too (common mistake)
- Ask: "What if the keyword spans multiple words, like 'hello world'?" (show it works)

---

## ## Assessment Rubric

### Checkpoint Grading (Out of 30 points)

| Checkpoint | Criteria | Points |
|------------|----------|--------|
| **1: Normalization** | Correctly uses `.strip()` and `.lower()` with assignment | 10 |
| **2: Multiple Spaces** | Handles consecutive spaces correctly; explains the approach | 10 |
| **3: Keyword Detection** | Returns both cleaned string and keyword count as tuple | 10 |

### Exit Ticket (See Section 8)
- Students complete a quick 3-question exit ticket
- Answers show understanding of immutability and method chaining

### Completeness
- All three checkpoints working
- Code is readable with minimal comments
- No TODO or hardcoded values

---

## ## Troubleshooting Pitfalls

### Pitfall 1: Expecting In-Place Modification

**Mistake:**
```python
message = "HELLO"
message.lower()  # Student expects message to become "hello"
print(message)   # Still prints "HELLO" — surprise!
```

**Root cause:** Students coming from other languages (or misunderstanding Python docs) expect methods to modify the object.

**Fix:**
```python
message = "HELLO"
message = message.lower()  # Assign the result
print(message)  # Now prints "hello"
```

**Teaching tip:** Reinforce the immutability concept. Strings are immutable, so methods **always** return a new string.

---

### Pitfall 2: Confusing `.find()` with Boolean Checks

**Mistake:**
```python
text = "Python"
if text.find("py"):  # Oops! 0 is falsy in Python
    print("Found py")  # This WON'T execute if "py" is at index 0
```

**Root cause:** Students think `.find()` returns True/False like `in` operator.

**Fix:**
```python
# Option 1: Use 'in' operator for boolean check
if "py" in text:
    print("Found py")

# Option 2: Explicitly check .find() against -1
if text.find("py") != -1:
    print("Found py")
```

**Teaching tip:** Show that `.find()` returns an integer position, not a boolean. The value 0 is a valid position but falsy in Python.

---

### Pitfall 3: Partial Space Cleanup

**Mistake:**
```python
text = "hello    world"
text = text.replace("  ", " ")  # One pass
print(text)  # "hello  world" — Still has double space!
```

**Root cause:** A single `.replace()` call replaces non-overlapping occurrences. With 4 spaces, it replaces the first 2 and second 2 separately, leaving 2 spaces behind.

**Fix:**
```python
# Option 1: Loop until no more double-spaces
while "  " in text:
    text = text.replace("  ", " ")

# Option 2: Use regex (advanced)
import re
text = re.sub(r"\s+", " ", text)
```

**Teaching tip:** Test the naive approach with students. Let them see it fail on "    " (4 spaces). This builds problem-solving skills.

---

### Pitfall 4: Forgetting Keyword Normalization

**Mistake:**
```python
text = "  PYTHON is GREAT  "
keyword = "python"

text = text.lower().strip()  # "python is great"
count = text.count(keyword)  # 1 (correct)

# But what if keyword still has different case?
keyword = "PYTHON"
count = text.count(keyword)  # 0 (wrong!)
```

**Root cause:** Normalizing the text but not the keyword leads to inconsistent results.

**Fix:**
```python
text = "  PYTHON is GREAT  "
keyword = "PYTHON"

text = text.lower().strip()
keyword = keyword.lower()  # Normalize both!
count = text.count(keyword)  # Now it's 1
```

**Teaching tip:** Show both the buggy and fixed versions. Emphasize that **both** search terms should be normalized.

---

### Pitfall 5: Misunderstanding `.replace()` Limits

**Mistake:**
```python
text = "cat cat cat"
text = text.replace("cat", "dog", 1)  # Replace only 1 occurrence
print(text)  # "dog cat cat"
```

**Why it's a pitfall:** Students might not realize the optional third parameter limits replacements, or they might forget it exists when they need it.

**Teaching tip:** Show that `.replace(old, new, count)` has an optional count parameter. Demonstrate its use for selective replacement.

---

### Pitfall 6: Assuming `.strip()` Removes All Whitespace

**Mistake:**
```python
text = "  hello   world  "
text = text.strip()
print(text)  # "hello   world" — embedded triple-space remains!
```

**Root cause:** Students expect `.strip()` to clean all whitespace everywhere.

**Fix:**
```python
# Use a combination:
text = text.strip().replace("  ", " ")
# Or loop:
while "  " in text:
    text = text.replace("  ", " ")
```

**Teaching tip:** Clarify the scope: `.strip()` only removes leading and trailing whitespace. For embedded whitespace, use `.replace()`.

---

### Pitfall 7: Case Sensitivity Matters in `.replace()` and `.find()`

**Mistake:**
```python
text = "Hello World"
pos = text.find("hello")  # Returns -1 (not found)
print(pos)
```

**Root cause:** `.find()` and `.replace()` are case-sensitive by default. Students might forget to normalize case first.

**Fix:**
```python
text = "Hello World"
pos = text.lower().find("hello")  # Now returns 0
print(pos)
```

**Teaching tip:** Always normalize case before searching if you want case-insensitive matching.

---

## ## Exit Ticket

**Duration:** 5 minutes

**Instructions:** Students answer these three questions (on paper, Slack, or a shared form):

1. **Immutability:** Write one line of code showing why `name.upper()` doesn't change `name`. What do you need to do to keep the uppercase version?

2. **Search Strategy:** You need to check if the word "error" appears in a log message. Should you use `find()` or the `in` operator? Why?

3. **Method Chaining:** Write a one-liner that takes the input `"  WELCOME TO PYTHON  "` and produces `"welcome to python"`.

**Sample Correct Answers:**
1. `name = "John"; name.upper(); print(name)  # Prints "John", not "JOHN". Must do: name = name.upper()`
2. `"error" in log_message` — We just need True/False, not position.
3. `"  WELCOME TO PYTHON  ".lower().strip()`

---

## ## Wrap-Up

### Key Takeaways (3 minutes)
1. Strings are immutable; methods return new strings that you must capture
2. Use `.lower()`, `.upper()`, `.strip()` to normalize text
3. Use `.replace()` for bulk text substitution
4. Use `.find()` to locate position; use `in` for boolean containment checks
5. Method chaining makes code cleaner but read carefully for correctness

### Preview of Next Hour (1 minute)
"Next hour, we'll combine these string methods into real programs. You'll handle user input, validate it, and transform it for storage. The skills you learned today are the foundation for that."

### Closing Encouragement
"String methods are fundamental to real-world programming. Every application that accepts user input uses these techniques. You're building professional-grade skills right now."

---

## ## Facilitation Notes

### Pacing Guide
- **Intro & Opening Script:** 5 min
- **Core Concepts (live narration):** 10 min
- **Live Coding Demo:** 8 min
- **Lab (3 checkpoints):** 30 min
- **Assessment & Exit Ticket:** 5 min
- **Wrap-Up:** 2 min
- **Buffer/Q&A:** 0 min (tight schedule; address questions during checkpoints)

### Engagement Strategies
1. **During Core Concepts:** Ask "What do you think happens if we chain `.upper()` then `.lower()`?" before showing the answer.
2. **During Lab:** Use pair programming if possible. Have strong students explain to weaker ones.
3. **During Pitfalls:** Role-play the mistake. Type the buggy code, run it, show the failure, then fix it. This builds debugging intuition.

### Accessibility & Inclusion
- **For visual learners:** Use color-coded highlighting in code (string methods in one color, arguments in another).
- **For kinesthetic learners:** Have students type every example, not just watch.
- **For language learners:** Slow down during method explanations; provide written definitions of each method on a handout.

### Troubleshooting Live Issues
- **Demo fails (Python not installed/wrong version):** Have a printed reference or pre-recorded video as backup.
- **Student can't run code:** Provide a pre-configured Jupyter notebook link or online Python REPL (repl.it, Python.org/shell).
- **Lab is taking too long:** Pre-seed some students with partial solutions; focus on concepts, not speed.

---

## ## Real-World Context

### Use Case 1: Web Form Validation
When a user signs up for an account, their email or username comes in messy:
- Extra spaces: `"  john_doe  "`
- Random case: `"JoHn_DoE"`
- Multiple spaces: `"john    doe"`

The backend normalizes it:
```python
username = raw_input.strip().lower().replace("  ", " ")
```

This ensures consistent storage and lookup.

### Use Case 2: Log Analysis
System logs often have inconsistent formatting:
```
"ERROR: Database connection failed"
"error: DATABASE CONNECTION FAILED"
"Error: database connection failed"
```

To find all errors:
```python
for line in logs:
    if "error" in line.lower():
        print(line)
```

### Use Case 3: Data Cleaning
CSV files often have messy data:
```
Name, Age
  John  , 25
   jane  , 30
```

Cleaning:
```python
for row in csv_data:
    row[0] = row[0].strip()  # Remove surrounding spaces
    row[0] = row[0].title()  # Capitalize names
```

### Use Case 4: Keyword Filtering
A content moderation system checks posts for banned words:
```python
def has_banned_word(post, banned_list):
    post_lower = post.lower()
    for word in banned_list:
        if word.lower() in post_lower:
            return True
    return False
```

### Use Case 5: Text Analytics
Counting word frequencies:
```python
text = "python python java python java java"
python_count = text.count("python")
java_count = text.count("java")
```

All these scenarios rely on the string methods you're learning today.

---

## ## Advanced Topics & Summary

### Extension 1: The `.title()` Method
Convert to title case (good for names):
```python
name = "john doe"
proper = name.title()  # "John Doe"
```

### Extension 2: The `.count()` Method with Start/End Parameters
```python
text = "banana"
text.count("a")  # 3
text.count("a", 1, 4)  # 2 (counts in slice text[1:4] = "ana")
```

### Extension 3: Position-Based Text Extraction
Combine `.find()` with slicing:
```python
email = "john@example.com"
at_pos = email.find("@")
username = email[:at_pos]  # "john"
domain = email[at_pos + 1:]  # "example.com"
```

### Extension 4: Using `.split()` and `.join()` (Preview)
These are more advanced but worth mentioning:
```python
text = "apple, banana, cherry"
items = text.split(", ")  # ["apple", "banana", "cherry"]
rejoined = " | ".join(items)  # "apple | banana | cherry"
```

### Extension 5: Introduction to `.replace()` with Regular Expressions
Advanced learners can explore regex:
```python
import re
text = "hello123world456"
clean = re.sub(r"\d+", "", text)  # Removes all digits
```

### Summary of Key Methods

| Method | Returns | Use Case |
|--------|---------|----------|
| `.lower()` | str | Normalize to lowercase |
| `.upper()` | str | Normalize to uppercase |
| `.strip()` | str | Remove leading/trailing whitespace |
| `.replace(old, new)` | str | Substitute all (or limited) occurrences |
| `.find(substring)` | int | Get position of substring (-1 if not found) |
| `.count(substring)` | int | Count non-overlapping occurrences |
| `in` operator | bool | Check if substring is present |

### Reflection Questions for Deeper Learning
1. Why do you think Python made strings immutable?
2. When would `.find()` be more useful than `in`?
3. Can you think of a real-world string that needs multiple `.replace()` calls?
4. What happens if you call `.lower()` on a string that's already lowercase?

### Preparing for the Next Hour
Next hour (Hour 7), we'll dive into **Input/Output & Type Conversion**. You'll learn:
- How to get text from users (`input()`)
- How to convert between types (`int()`, `str()`, `float()`)
- How to combine these with string methods for robust input handling

The string techniques today are essential for all of that work.

---

**End of Hour 6 Lecture Script**

*Total Word Count: 3,247 words*  
*Section Count: 12 H2 sections + Learning Outcomes preamble*  
*Checkpoint Count: 3 (in Lab section, each with explicit timing)*  
*Pitfall Count: 7 H3 subsections*  
*Runbook Alignment: Hour 6, lines 526–650 of Python_Basics_Instructor_Runbook_4hr_Days.md*
