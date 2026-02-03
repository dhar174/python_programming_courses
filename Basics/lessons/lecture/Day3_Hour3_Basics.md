# Day 3, Hour 3: Working with Text – split() and join()
**Python Programming Basics – Session 3**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Hour 10: 3 minutes
- String Methods Overview: 5 minutes
- The split() Method: 10-12 minutes
- The join() Method: 8-10 minutes
- Practical Text Processing Patterns: 5 minutes
- Live Demo (Word Count and Rebuild): 5-10 minutes
- Hands-On Lab (Sentence Stats): 25-35 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Use `.split()` to break strings into lists of words
2. Understand how `.split()` handles whitespace by default
3. Use `.join()` to combine list elements into a single string
4. Count words in a sentence programmatically
5. Find the longest word in a text string
6. Rebuild strings with custom separators
7. Recognize and handle edge cases (empty input, punctuation)

---

## Section 1: Recap & Transition from Hour 10 (3 minutes)

### Quick Review

**[Instructor speaks:]**

Welcome back! In Hour 10, we learned f-strings and made our program output look professional. You upgraded the Tip Calculator to display currency with proper formatting using `.2f`.

Quick check: **Who's now using f-strings in all their output instead of concatenation?**

[Wait for responses]

Excellent! Once you start using f-strings, you'll never want to go back to `+` concatenation.

### From Formatting to Processing

**[Instructor speaks:]**

So far, we've been **displaying** strings. Now we're going to learn how to **process** them—how to break text apart, analyze it, and put it back together in new ways.

**Real-world examples where this matters:**
- **Parsing user input:** "First Last" → split into first and last name
- **Word counting:** Count words in a document or tweet
- **Data cleaning:** "New York" → "new_york" for a filename
- **CSV processing:** "John,Doe,25" → extract individual fields
- **Text analysis:** Find the most common words in a file

**Hour 11 (right now)** is about two essential string methods: **`split()`** and **`join()`**. These are the foundation of text processing.

Let's dive in!

---

## Section 2: String Methods Overview (5 minutes)

### What Are String Methods?

**[Instructor speaks:]**

We've already used a few string methods:

```python
text = "Hello"
print(text.upper())      # "HELLO"
print(text.lower())      # "hello"
```

**Reminder:** A **method** is a function that belongs to an object. Strings are objects, and they come with built-in methods we can call using the dot `.` notation.

**The pattern:**
```python
string_variable.method_name()
```

### Key String Methods We'll Use Today

**[Instructor speaks:]**

Today we're focusing on two methods that work together:

1. **`.split()`** — Breaks a string into a list of substrings
2. **`.join()`** — Combines a list of strings into a single string

**The relationship:**
```python
sentence = "Python is awesome"

words = sentence.split()        # Break apart
# words is now: ['Python', 'is', 'awesome']

rebuilt = " ".join(words)       # Put back together
# rebuilt is now: "Python is awesome"
```

Think of them as opposites:
- `split()`: string → list
- `join()`: list → string

Let's explore each in detail.

---

## Section 3: The split() Method (10-12 minutes)

### Basic Usage: Splitting on Whitespace

**[Instructor speaks:]**

The most common use of `.split()` is to break a sentence into words:

```python
sentence = "Python is awesome"

words = sentence.split()
print(words)
```

**Output:**
```python
['Python', 'is', 'awesome']
```

**What happened?**
- `.split()` with no arguments splits on **whitespace** (spaces, tabs, newlines)
- It returns a **list** of strings
- Each word becomes an element in the list

**[Key insight]:** Notice the return type changes from `str` to `list`. This is important.

### Checking the Type

**[Instructor speaks:]**

Let's verify:

```python
sentence = "Hello world"

words = sentence.split()

print(type(sentence))    # <class 'str'>
print(type(words))       # <class 'list'>
print(words)             # ['Hello', 'world']
```

**Why does this matter?** Because now you can use list operations:

```python
words = sentence.split()

print(len(words))        # 2 (number of words)
print(words[0])          # 'Hello' (first word)
print(words[1])          # 'world' (second word)
```

### Whitespace Handling

**[Instructor speaks:]**

`.split()` is smart about whitespace—it strips leading/trailing spaces and handles multiple spaces:

```python
# Multiple spaces
text = "Hello    world"
print(text.split())      # ['Hello', 'world']

# Leading/trailing spaces
text = "  Python  "
print(text.split())      # ['Python']

# Mix of spaces and tabs
text = "one\ttwo\tthree"
print(text.split())      # ['one', 'two', 'three']
```

**[Key point]:** When you call `.split()` without arguments, Python splits on **any whitespace** and ignores empty strings in the result.

### Quick Check #1

**[Instructor asks:]**

What will this code print?

```python
text = "Learn Python today"
words = text.split()

print(len(words))
print(words[0])
print(words[-1])
```

[Pause for student predictions]

**Answer:**
```
3
Learn
today
```

- `len(words)` is 3 (three words in the list)
- `words[0]` is the first word: `'Learn'`
- `words[-1]` is the last word: `'today'` (negative indexing!)

### Splitting on a Specific Delimiter

**[Instructor speaks:]**

You can also split on a **specific character** by passing it as an argument:

```python
# Splitting on commas (CSV format)
data = "John,Doe,25,Engineer"
fields = data.split(",")
print(fields)
# ['John', 'Doe', '25', 'Engineer']

# Splitting on hyphens
phone = "555-123-4567"
parts = phone.split("-")
print(parts)
# ['555', '123', '4567']

# Splitting on pipes
items = "apple|banana|cherry"
fruits = items.split("|")
print(fruits)
# ['apple', 'banana', 'cherry']
```

**When you specify a delimiter:**
- Python splits **only** on that character
- Multiple consecutive delimiters create empty strings

```python
text = "a,,b"
parts = text.split(",")
print(parts)         # ['a', '', 'b']
```

Notice the empty string `''` in the middle—that's because there's nothing between the two commas.

### Practical Pattern: Extracting Name Parts

**[Instructor speaks:]**

A common use case:

```python
full_name = input("Enter your full name: ")
# User types: "Alice Johnson"

parts = full_name.split()
first_name = parts[0]
last_name = parts[1]

print(f"First: {first_name}")
print(f"Last: {last_name}")
```

**Output:**
```
First: Alice
Last: Johnson
```

**[Warning]:** This assumes the user enters exactly two words. In production code, you'd check the length of `parts` first to avoid an `IndexError`.

### Counting Words

**[Instructor speaks:]**

The simplest way to count words:

```python
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())

print(f"Word count: {word_count}")
```

**Example:**
```
Enter a sentence: Python is easy to learn
Word count: 5
```

**Why this works:** `sentence.split()` creates a list of words, and `len()` tells us how many items are in that list.

---

## Section 4: The join() Method (8-10 minutes)

### Basic Usage: Joining a List into a String

**[Instructor speaks:]**

`.join()` is the opposite of `.split()`. It takes a list of strings and combines them into a single string.

**The syntax is a bit unusual:**

```python
separator.join(list_of_strings)
```

**Not:** ~~`list.join(separator)`~~

**The separator comes first, then you call `.join()` on it, passing the list.**

Let's see it in action:

```python
words = ['Python', 'is', 'awesome']

sentence = " ".join(words)
print(sentence)
# "Python is awesome"
```

**Breaking this down:**
- `" "` is the separator (a space)
- `.join(words)` combines the words with that separator between each

### Different Separators

**[Instructor speaks:]**

You can use any string as the separator:

```python
words = ['apple', 'banana', 'cherry']

# Join with spaces
print(" ".join(words))           # "apple banana cherry"

# Join with commas
print(",".join(words))            # "apple,banana,cherry"

# Join with comma and space
print(", ".join(words))           # "apple, banana, cherry"

# Join with newlines
print("\n".join(words))
# Output:
# apple
# banana
# cherry

# Join with nothing (concatenate)
print("".join(words))             # "applebananacherry"

# Join with hyphens
print("-".join(words))            # "apple-banana-cherry"

# Join with pipes
print(" | ".join(words))          # "apple | banana | cherry"
```

### Quick Check #2

**[Instructor asks:]**

What will this code print?

```python
items = ['Python', 'Java', 'JavaScript']
result = " and ".join(items)

print(result)
```

[Pause for student predictions]

**Answer:**
```
Python and Java and JavaScript
```

The separator `" and "` is inserted **between** each element.

### The Split-Process-Join Pattern

**[Instructor speaks:]**

A common pattern in text processing:

1. **Split** the string into parts
2. **Process** the parts (filter, transform, etc.)
3. **Join** them back together

**Example: Convert sentence to hyphen-separated:**

```python
sentence = "Learn Python today"

# Split into words
words = sentence.split()        # ['Learn', 'Python', 'today']

# Process: convert to lowercase
words_lower = [word.lower() for word in words]  # ['learn', 'python', 'today']

# Join with hyphens
result = "-".join(words_lower)  # 'learn-python-today'

print(result)
```

**[Note]:** The list comprehension `[word.lower() for word in words]` is a preview of concepts we'll cover later. For now, understand that we're transforming each word.

**Simplified version for now:**

```python
sentence = "Learn Python today"

words = sentence.split()
result = "-".join(words)

print(result)        # "Learn-Python-today"
```

### Common Use Case: Building File Paths or URLs

**[Instructor speaks:]**

```python
# Building a URL-friendly string
words = ['Python', 'Programming', 'Basics']
url_slug = "-".join(words).lower()

print(url_slug)      # "python-programming-basics"
```

This is how many websites generate URLs from titles.

### Why join() Requires a List of Strings

**[Instructor speaks:]**

`.join()` only works with lists (or other iterables) of **strings**. If you have numbers, you must convert them first:

```python
# WRONG - This will error
numbers = [1, 2, 3]
result = ",".join(numbers)      # TypeError!

# RIGHT - Convert to strings first
numbers = [1, 2, 3]
result = ",".join([str(n) for n in numbers])
print(result)                   # "1,2,3"
```

**Or more simply:**

```python
numbers = [1, 2, 3]
result = ",".join(str(n) for n in numbers)
print(result)        # "1,2,3"
```

**[For now]:** Just remember that `.join()` expects strings. If you see a `TypeError`, check that all elements are strings.

---

## Section 5: Practical Text Processing Patterns (5 minutes)

### Pattern 1: Word Count

**[Instructor speaks:]**

```python
text = input("Enter text: ")
word_count = len(text.split())

print(f"Words: {word_count}")
```

**Simple and effective.** This works for most cases.

### Pattern 2: Finding the Longest Word

**[Instructor speaks:]**

```python
sentence = "Python is an amazing programming language"

words = sentence.split()
longest = max(words, key=len)

print(f"Longest word: {longest}")
# "programming"
```

**Breaking this down:**
- `max(words, key=len)` finds the word with the maximum length
- `key=len` tells Python to compare words by their length

**Alternative (more beginner-friendly):**

```python
words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Longest word: {longest}")
```

**We'll cover loops in detail later**, but this pattern is worth seeing now.

### Pattern 3: Reversing Word Order

**[Instructor speaks:]**

```python
sentence = "I love Python"

words = sentence.split()
words.reverse()                  # Reverse the list in place
reversed_sentence = " ".join(words)

print(reversed_sentence)
# "Python love I"
```

**Or more concisely:**

```python
sentence = "I love Python"
reversed_sentence = " ".join(sentence.split()[::-1])

print(reversed_sentence)
# "Python love I"
```

**The `[::-1]` is slice notation for "reverse the list".** We'll cover slicing in detail later.

### Pattern 4: Removing Extra Spaces

**[Instructor speaks:]**

```python
messy_text = "  Hello    world   "

# Split removes extra spaces, join rebuilds cleanly
clean_text = " ".join(messy_text.split())

print(f"'{clean_text}'")
# 'Hello world'
```

**Why this works:** `.split()` breaks on any whitespace and ignores empties, `.join()` rebuilds with single spaces.

---

## Section 6: Live Demo – Word Count and Rebuild (5-10 minutes)

### Demo Script: Sentence Statistics

**[Instructor speaks:]**

Now I'm going to build a small program that:
1. Takes a sentence as input
2. Counts the words
3. Finds the longest word
4. Rebuilds the sentence with a custom separator

Watch how I use `split()` and `join()` together.

**[Open editor and create `sentence_stats.py`]**

**[Instructor types and speaks:]**

```python
# sentence_stats.py
# Purpose: Analyze and transform a sentence

print("=== Sentence Statistics ===\n")

# Get user input
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Calculate statistics
word_count = len(words)

# Find longest word
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

# Rebuild with different separators
hyphenated = "-".join(words)
piped = " | ".join(words)

# Display results
print("\n--- Statistics ---")
print(f"Word count: {word_count}")
print(f"Longest word: '{longest}' ({len(longest)} characters)")

print("\n--- Transformations ---")
print(f"Hyphenated: {hyphenated}")
print(f"Piped: {piped}")
```

**[Run the program]**

```
=== Sentence Statistics ===

Enter a sentence: Python programming is incredibly powerful

--- Statistics ---
Word count: 5
Longest word: 'programming' (11 characters)

--- Transformations ---
Hyphenated: Python-programming-is-incredibly-powerful
Piped: Python | programming | is | incredibly | powerful
```

**[Instructor explains the key parts:]**

1. **Line 8:** Get the sentence from the user
2. **Line 11:** Split into a list of words
3. **Line 14:** Count words using `len()` on the list
4. **Lines 17-20:** Loop through to find the longest word (we'll cover loops formally later)
5. **Lines 23-24:** Rebuild the sentence with different separators using `.join()`

**[Key teaching moment]:** Notice how `.split()` and `.join()` let us transform text easily. We broke it apart, analyzed it, and put it back together in different ways.

### Handling Edge Cases

**[Instructor speaks:]**

Let's test with edge cases:

**Test 1: Empty input**
```
Enter a sentence: 

--- Statistics ---
Word count: 0
Longest word: '' (0 characters)
```

**Test 2: Single word**
```
Enter a sentence: Hello

--- Statistics ---
Word count: 1
Longest word: 'Hello' (5 characters)

--- Transformations ---
Hyphenated: Hello
Piped: Hello
```

**Test 3: Extra spaces**
```
Enter a sentence:   Hello    world  

--- Statistics ---
Word count: 2
Longest word: 'Hello' (5 characters)
```

**Notice:** `.split()` handles extra spaces gracefully.

**[Important note]:** In a production program, you'd add validation to check if the input is empty before processing. For now, we'll trust the user to provide valid input.

---

## Section 7: Hands-On Lab – Sentence Stats (25-35 minutes)

### Lab Overview

**[Instructor speaks:]**

Now it's your turn! You're going to build a sentence statistics program that analyzes text input.

**Lab Goal:** Create a program that splits, analyzes, and transforms user input.

### Lab Instructions: Sentence Stats

**Scenario:** You're building a text analysis tool that provides statistics and transformations for user input.

**Requirements:**

Create a Python script called `sentence_analyzer.py` that:

1. **Prompts the user for a sentence**

2. **Calculates and displays:**
   - Total word count
   - The longest word in the sentence
   - The length of the longest word

3. **Shows transformations:**
   - Original sentence
   - Words joined with pipes: `word1 | word2 | word3`
   - Words joined with hyphens: `word1-word2-word3`

4. **Uses `.split()` and `.join()` appropriately**

### Starter Template

```python
# sentence_analyzer.py
# Purpose: Analyze and transform text input

print("=== Sentence Analyzer ===\n")

# Get user input
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Calculate statistics
word_count = len(words)

# TODO: Find the longest word
longest_word = ""
# Your code here to find longest word

# TODO: Create transformations
piped_version = ""  # Join with " | "
hyphenated_version = ""  # Join with "-"

# Display results
print("\n--- Statistics ---")
print(f"Word count: {word_count}")
print(f"Longest word: {longest_word}")
print(f"Length of longest word: {len(longest_word)}")

print("\n--- Transformations ---")
print(f"Original: {sentence}")
print(f"Piped: {piped_version}")
print(f"Hyphenated: {hyphenated_version}")
```

### Example Output

**Test Case 1:**
```
=== Sentence Analyzer ===

Enter a sentence: The quick brown fox jumps

--- Statistics ---
Word count: 5
Longest word: brown
Length of longest word: 5

--- Transformations ---
Original: The quick brown fox jumps
Piped: The | quick | brown | fox | jumps
Hyphenated: The-quick-brown-fox-jumps
```

**Test Case 2:**
```
=== Sentence Analyzer ===

Enter a sentence: Python programming is amazing

--- Statistics ---
Word count: 4
Longest word: programming
Length of longest word: 11

--- Transformations ---
Original: Python programming is amazing
Piped: Python | programming | is | amazing
Hyphenated: Python-programming-is-amazing
```

### Completion Criteria

Your solution must:
- ✅ Use `.split()` to break the sentence into words
- ✅ Correctly count the number of words
- ✅ Identify the longest word in the sentence
- ✅ Use `.join()` to create both transformations (piped and hyphenated)
- ✅ Display output in a clear, formatted way
- ✅ Run without errors

### Common Pitfalls to Watch For

**[Instructor speaks:]**

As you work, watch out for these common mistakes:

1. **Forgetting to assign the result of split():**
   ```python
   # WRONG - split() doesn't modify the original string
   sentence.split()
   word_count = len(sentence)    # This counts characters, not words!
   
   # RIGHT - save the result
   words = sentence.split()
   word_count = len(words)
   ```

2. **Using join() incorrectly:**
   ```python
   # WRONG - trying to call join on the list
   result = words.join(" | ")    # AttributeError!
   
   # RIGHT - call join on the separator
   result = " | ".join(words)
   ```

3. **Comparing word lengths as strings:**
   ```python
   # This works, but for the wrong reason
   longest = max(words)  # Finds alphabetically last, not longest!
   
   # Correct comparison by length
   longest = max(words, key=len)
   ```

4. **Punctuation attached to words:**
   ```python
   sentence = "Hello, world!"
   words = sentence.split()      # ['Hello,', 'world!']
   # The comma and exclamation are part of the words
   ```
   
   **For this lab, don't worry about stripping punctuation.** We'll cover that in future lessons.

### Optional Extensions

If you finish early, try these:

1. **Strip Punctuation:** Remove common punctuation marks (`,`, `.`, `!`, `?`) from words before analysis

2. **Average Word Length:** Calculate and display the average length of words

3. **Reverse Word Order:** Show the sentence with words in reverse order

4. **Title Case Transformation:** Show the sentence with the first letter of each word capitalized

**Example of Optional Extension #2:**

```python
# Average word length
total_characters = sum(len(word) for word in words)
average_length = total_characters / word_count
print(f"Average word length: {average_length:.1f} characters")
```

**[Instructor speaks:]**

Alright, you have 25-35 minutes. Remember:
- `.split()` returns a list
- `.join()` is called on the separator, not the list
- Test with different sentences, including ones with extra spaces
- Read error messages—they'll guide you to the fix

Let's analyze some text!

---

## Section 8: Debrief & Exit Ticket (5 minutes)

### Solution Walkthrough

**[Instructor shares solution:]**

```python
# sentence_analyzer.py
# Purpose: Analyze and transform text input

print("=== Sentence Analyzer ===\n")

# Get user input
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Calculate statistics
word_count = len(words)

# Find the longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Alternative using max()
# longest_word = max(words, key=len) if words else ""

# Create transformations
piped_version = " | ".join(words)
hyphenated_version = "-".join(words)

# Display results
print("\n--- Statistics ---")
print(f"Word count: {word_count}")
print(f"Longest word: {longest_word}")
print(f"Length of longest word: {len(longest_word)}")

print("\n--- Transformations ---")
print(f"Original: {sentence}")
print(f"Piped: {piped_version}")
print(f"Hyphenated: {hyphenated_version}")
```

**[Key points to highlight:]**

1. **Line 11:** `.split()` with no arguments splits on whitespace
2. **Line 14:** `len(words)` counts the words (not characters)
3. **Lines 17-20:** Loop to find the longest word (or use `max(words, key=len)`)
4. **Lines 25-26:** `.join()` is called on the separator string
5. **The pattern:** Split → Analyze → Join back together

### Common Issues Students Encountered

**[Instructor speaks:]**

Let me address a few things I saw as I walked around:

[Adjust based on actual student work, but common issues include:]

1. **Calling join on the list:** Remember, it's `" | ".join(words)`, not `words.join(" | ")`
2. **Forgetting to save the split result:** You must assign `sentence.split()` to a variable
3. **Empty input:** If the user presses Enter without typing, `words` is an empty list, which can cause issues when finding the longest word

### Extensions Showcase

**[Instructor speaks:]**

If anyone completed the extensions, let's see what you built!

[Call on 1-2 students who finished extensions to share their screen briefly]

Great work! The punctuation stripping and average word length are useful additions.

### Exit Ticket

**[Instructor asks:]**

Before we wrap up Hour 11, answer this in your notes or in the chat:

**Question:** What type does `.split()` return, and why does that matter?

**Expected answer:** `.split()` returns a `list` of strings. This matters because it allows us to use list operations like `len()` (to count words), indexing (to access specific words), and iteration (to process each word).

---

## Recap: What We Accomplished

In this hour, you:
✅ Learned `.split()` to break strings into lists of words  
✅ Used `.split()` with and without delimiters  
✅ Learned `.join()` to combine lists back into strings  
✅ Counted words programmatically using `len()` on split results  
✅ Found the longest word in a sentence  
✅ Transformed sentences with custom separators  
✅ Handled edge cases like extra whitespace  

**This is powerful text processing knowledge.** You can now take user input, break it apart, analyze it, and transform it. These patterns show up everywhere—parsing data files, cleaning text, building search features, and more.

In Hour 12, we'll focus on **debugging habits**—how to read error messages, use print-debugging effectively, and troubleshoot like a pro.

**Great work! Take a quick 5-minute break.**

---

## Quick Reference Card (for students)

**split() Method:**
```python
# Split on whitespace (default)
words = sentence.split()

# Split on specific character
fields = data.split(",")

# Examples
"Hello world".split()           # ['Hello', 'world']
"a,b,c".split(",")              # ['a', 'b', 'c']
"  extra  spaces  ".split()     # ['extra', 'spaces']
```

**join() Method:**
```python
# Syntax: separator.join(list)
words = ['Python', 'is', 'awesome']

" ".join(words)                 # 'Python is awesome'
"-".join(words)                 # 'Python-is-awesome'
", ".join(words)                # 'Python, is, awesome'
" | ".join(words)               # 'Python | is | awesome'
"".join(words)                  # 'Pythonisawesome'
```

**Common Patterns:**
```python
# Word count
word_count = len(text.split())

# Find longest word
longest = max(words, key=len)

# Clean extra spaces
clean = " ".join(messy.split())

# Split-Process-Join
words = sentence.split()
result = "-".join(words)
```

**Remember:**
- `.split()` returns a list
- `.join()` is called on the separator: `separator.join(list)`
- `.join()` only works with lists of strings
- `.split()` with no arguments handles any whitespace

---

**End of Hour 11 Script**
