# Day 9, Hour 3: Functions with Collections (Course Hour 35)
**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 35 – Functions with collections  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. A critical transition for beginners is understanding that lists and dictionaries update "in place" (mutation) whereas simple types like integers or strings don't. Explain the difference clearly, and underscore the necessity of a good docstring to communicate the side effects of your function.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Pass collections (lists and dictionaries) into functions safely.
2. Decide when to modify a list in place (mutate) versus returning an entirely new collection.
3. Use simple docstrings to document your function's expected inputs and behaviors."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: How collections go into functions
- **0:05–0:20** Core concept: Mutation vs Returning a new list
- **0:20–0:30** Core concept: Warning strings (docstrings)
- **0:30–0:40** Live demo: Two ways to normalize names
- **0:40–0:55** Guided lab: Normalize Contacts
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour35_collections_demo.py` ready for live coding.
- Open another empty file named `hour35_normalize_lab.py` to serve as the starter for the lab portion.
- **Say:** "Please have your editor open to a new file called `collections_testing.py`. We are going to look at the two different ways functions can treat your data."

---

## 3) Opening Script: How Collections Go Into Functions (~5 minutes)

**Say:**
"In the last hour, we passed numbers and strings into functions. Those are simple, immutable data types in Python. 

But what happens when you pass a list of 1,000 customers into a function to be sorted or cleaned? Python doesn't want to burn computer memory making a massive copy of 1,000 items if it doesn't have to. So, instead of passing a copy, Python passes a direct reference to the original list.

This means if you alter the list inside your function, the *original* list outside the function changes too. This is called **mutation**.

When working with lists and dictionaries, you have to decide: Do I want to change the original, or do I want to build a brand new one and hand it back?"

---

## 4) Concept: Mutation vs Returning a New List

### 4.1 Modifying in-place (Mutation)

**Type and narrate:**

```python
# hour35_collections_demo.py

def empty_the_list(my_list):
    # This directly modifies the original list!
    my_list.clear()

groceries = ["Milk", "Eggs", "Bread"]
print("Before:", groceries)

# We pass the real list into the function
empty_the_list(groceries)

print("After:", groceries)
```

**Say:**
"Notice how the function `empty_the_list` doesn't have a `return` statement. It doesn't need one! Because we passed a reference to the list, calling `.clear()` directly wiped out the original `groceries` list. 

This is fast and efficient, but it can be dangerous if you didn't mean to destroy your original data."

### 4.2 Building a new list

**Say:**
"If you want to keep the original data safe, the safer alternative is to have your function create a brand new list, copy or modify the data into the new list, and `return` the new list."

**Type and narrate:**

```python
def keep_only_first_item(my_list):
    # Create a fresh, empty list
    new_list = []
    
    # Grab just the first item
    if len(my_list) > 0:
        new_list.append(my_list[0])
        
    # Send the brand new list out
    return new_list

groceries = ["Milk", "Eggs", "Bread"]
print("Original:", groceries)

# We must capture the return value in a new variable
short_list = keep_only_first_item(groceries)

print("Original is still safe:", groceries)
print("Returned list:", short_list)
```

**Say:**
"By creating a new empty list inside the function, we guarantee we aren't mutating the original. The original remains safe and untouched."

---

## 5) Concept: Docstrings

**Say:**
"Because a function might mutate your data *or* it might return new data, it's critical to tell the other programmers (or yourself in six months) what the function does. We do this using a **docstring**."

**Type and narrate (adding to previous code):**

```python
def empty_the_list(my_list):
    """
    Clears all items from the provided list.
    WARNING: This modifies the list in place!
    """
    my_list.clear()
```

**Say:**
"A docstring is a multi-line string (three double quotes) immediately following the `def` line. It doesn't do anything functionally, but tools like VS Code will display this text when you hover over the function later. It's the professional standard for documenting expectations."

---

## 6) Live Demo: Two Ways to Normalize Names

**Say:**
"Let's look at a very realistic data cleaning scenario. We have a list of messy email names, and we need to strip whitespace and convert them to title case."

**Type and show both approaches:**

```python
names = ["  alice", "BOB  ", " cHarLiE "]

# Method 1: Return a new list (Safer, often preferred)
def clean_names_new(name_list):
    """Returns a new list of cleaned, title-cased names."""
    cleaned = []
    for name in name_list:
        clean = name.strip().title()
        cleaned.append(clean)
    return cleaned

# Method 2: Mutate in-place (Faster, but alters original)
def clean_names_inplace(name_list):
    """Cleans names by modifying the list in place."""
    for i in range(len(name_list)):
        # Extract, clean, and reassign over the old value
        clean = name_list[i].strip().title()
        name_list[i] = clean

print("Original raw:", names)
clean_version = clean_names_new(names)
print("New List:", clean_version)
print("Original is safe:", names)

print("\nRunning in-place mutation...")
clean_names_inplace(names)
print("Original was destroyed/mutated:", names)
```

**Say:**
"Both are valid Python. Returning a new list is often best practice because it avoids accidentally destroying data you might need later. In-place mutation is used when lists are millions of records long and memory is tight."

---

## 7) Hands-on Lab: Normalize Contacts

### 7.1 Lab overview

**Say:**
"For your lab, you are going to practice writing a cleaning function for a list of contacts. You need to write the function and prove it works on sample data by printing the state of the list before and after."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Normalize Contacts**

**Task:**
1. Create a raw list of messy contact names: `["  sarah jones ", "MARK smith", " tina turner  "]`
2. Write a function called `normalize_contacts(contacts)`.
3. The function must iterate through the list, remove all leading/trailing whitespace (`strip`), and capitalize the first letter of each name (`title`).
4. **Choose your approach**: You can either mutate the list in place, OR return a brand new list. 
5. Add a simple docstring to your function explaining which approach you took.
6. Run the function on your raw list, and print the resulting clean data.

**Requirements:**
- The final printed output must properly format "Sarah Jones", "Mark Smith", and "Tina Turner".

---

**Instructor Note for Circulation:**
Look to see if learners returning a new list forget to assign the returned value to a variable (e.g., they call `normalize_contacts(names)` but don't capture the output, then print the raw names wondering why nothing happened). If they are mutating in place, ensure they aren't trying to iterate using a basic `for name in contacts: name = name.strip()` because reassigning the loop variable `name` does not alter the underlying list. They must use `contacts[i] = ...` if mutating.

### 7.3 Walkthrough solution

**After 15 minutes, show a possible 'New List' solution:**

```python
# hour35_normalize_lab.py

def normalize_contacts(contacts):
    """
    Takes a list of messy strings.
    Returns a brand new list of cleaned, title-cased strings.
    """
    clean_list = []
    for person in contacts:
        clean_name = person.strip().title()
        clean_list.append(clean_name)
    
    return clean_list

raw_data = ["  sarah jones ", "MARK smith", " tina turner  "]
print(f"Before: {raw_data}")

# Crucial: capture the return value!
finished_data = normalize_contacts(raw_data)

print(f"After: {finished_data}")
```

**Say:**
"This is an incredibly common data science and scripting pattern: suck in dirty data, pass it through a cleaning function, and capture the sparkling clean result."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"When you pass a list or dictionary into a function, the function can actually change the original data. If you don't explicitly want to change the original data, create an empty list inside your function, fill it up, and return it. Always use docstrings to leave a warning for the next programmer."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: What is one advantage of returning a new list instead of modifying the list in place?"

**Expected answer:** Let them answer. "It keeps the original data intact and safe, avoiding unexpected bugs caused by accidental data destruction."
