# Functions with Collections (Day 9, Hour 3 – Course Hour 35)

**Python Programming Basics – Session 9**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 9, Course Hour 35 – Functions with collections  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## 1. Learning Outcomes

By the end of this hour, you will be able to:

1. Understand how to pass collections (lists, tuples, dicts) to functions and recognize that functions receive a reference to the original collection, not a copy.
2. Recognize the difference between returning a new collection vs. mutating the original, and understand when each approach is appropriate.
3. Build functions that aggregate or transform collection data, using iteration and conditional logic to process multiple items.
4. Use function parameters and return values effectively with collections, ensuring proper documentation and clear function contracts.
5. Apply best practices for collection handling in functions, including writing clear docstrings and avoiding common mutation pitfalls.

---

## 2. Instructor Prep and Delivery Note

**Critical teaching points to emphasize:**
- Collections (lists, dictionaries) are passed by reference into functions. This is fundamentally different from how simple types like integers and strings behave.
- Students must make an explicit decision for each function: "Do I mutate, or do I return?"
- Docstrings are not optional when working with collections—they prevent silent bugs caused by unexpected mutations.

**Setup checklist:**
- Open an empty editor file called `hour35_collections_demo.py` for live coding.
- Open a second empty file called `hour35_normalize_lab.py` to distribute as the lab starter.
- Verify that your Python interpreter is ready and your terminal is visible.
- Have the runbook reference (Hour 35: Functions with collections) open as a backup reference.

**Prerequisite knowledge check:**
- Students should be comfortable defining functions with parameters and return statements.
- Students should be familiar with list iteration using both `for item in list:` and `for i in range(len(list)):`.
- Students should understand `.strip()` and `.title()` string methods from earlier sessions.

---

## 3. Opening Script: Collections and Function References (~3 minutes)

**[Read aloud]**

"Good morning. Over the last few hours, we've been passing simple values—numbers and strings—into functions. When you pass the number `5` into a function, or the string `"hello"`, Python doesn't worry about making a copy. It just passes the value, and if the function changes something internally, the outside world is unaffected.

But today we're stepping into a different world: the world of collections. When you write a function that takes a list of 1,000 customer records, or a dictionary of settings, you face a choice that doesn't exist with simple types.

Here's the key insight: Python doesn't make a copy of that 1,000-item list to hand to your function. That would waste memory. Instead, Python passes a *reference*—a direct link to the original list. Your function and your main code are looking at the *same* list.

This means: if your function modifies that list, the original list changes. The list is 'mutated.' And that can be either exactly what you want, or a silent bug that destroys your program.

By the end of this hour, you'll know how to make that choice deliberately, and how to write code that makes your intention crystal clear to the next person who reads it—which is often yourself, three months later."

---

## 4. Conceptual Briefing: Mutation vs. Return – A Decision Tree (~12 minutes)

**[Say:]**
"Let's talk about the two fundamental patterns for handling collections in functions."

### 4.1 Pattern 1: Mutating the Collection In-Place

**[Narrate as you type:]**

```python
# hour35_collections_demo.py

def empty_the_list(my_list):
    """
    WARNING: This function modifies the original list in place.
    Clears all items from the provided list.
    """
    my_list.clear()

groceries = ["Milk", "Eggs", "Bread"]
print("Before function call:")
print(f"  groceries = {groceries}")

empty_the_list(groceries)

print("After function call:")
print(f"  groceries = {groceries}")
```

**[Expected output:]**
```
Before function call:
  groceries = ['Milk', 'Eggs', 'Bread']
After function call:
  groceries = []
```

**[Continue speaking:]**

"Notice what happened. The function received a reference to `groceries`. Inside the function, we called `.clear()` on that reference. Since we're working with the real list—not a copy—the original `groceries` list was completely emptied.

This pattern is called **in-place mutation** or **destructive mutation**. It's fast and memory-efficient. But it has a big downside: if you weren't expecting the function to destroy your data, you're in trouble."

### 4.2 Pattern 2: Returning a New Collection

**[Say:]**
"The safer alternative is to leave the original list alone and return a brand-new list."

**[Type and narrate:]**

```python
def keep_only_first_item(my_list):
    """
    Returns a NEW list containing only the first item from my_list.
    Does NOT modify my_list.
    """
    new_list = []
    
    if len(my_list) > 0:
        new_list.append(my_list[0])
    
    return new_list

groceries = ["Milk", "Eggs", "Bread"]
print("Original before function call:")
print(f"  groceries = {groceries}")

short_list = keep_only_first_item(groceries)

print("Original after function call:")
print(f"  groceries = {groceries}")
print("Returned list:")
print(f"  short_list = {short_list}")
```

**[Expected output:]**
```
Original before function call:
  groceries = ['Milk', 'Eggs', 'Bread']
Original after function call:
  groceries = ['Milk', 'Eggs', 'Bread']
Returned list:
  short_list = ['Milk']
```

**[Continue:]**

"This time, we created a brand-new empty list inside the function. We filled it with processed data, and then returned it. The original `groceries` list was never touched. It's completely safe.

The cost? A tiny bit more memory (because we created a new list) and a few extra lines of code. But the payoff is huge: no surprises, no silent data destruction."

### 4.3 The Decision: When to Use Each Pattern

**[Say:]**

"So which pattern should you use?

**Return a new collection** if:
- The function's job is to transform or filter data (like cleaning names, sorting records, or selecting specific items).
- You want to keep the original data as a reference.
- The list is reasonably small (under a million items).
- You're writing code for readability and safety.

**Mutate in-place** if:
- Your function's job is to sort or shuffle the existing list without extracting specific items.
- Memory is extremely tight (processing millions of items).
- You have explicitly documented the mutation in your docstring.
- Everyone reading the code knows it's going to destroy the original.

For a beginner, my advice is: **default to returning a new collection**. It's safer. Once you're comfortable, you can optimize by mutating when you're sure it's the right choice."

### 4.4 Function Contracts and Docstrings

**[Say:]**

"Here's the professional standard: whenever a function works with a collection, you must write a docstring that tells the reader whether the function mutates or returns. This is called a **function contract**—it's your promise to the rest of the code about what the function will and won't do."

**[Type:]**

```python
def clean_list_inplace(my_list):
    """
    MUTATES the provided list by removing empty strings.
    Does not return anything (None).
    """
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] == "":
            my_list.pop(i)

def remove_empty_strings(my_list):
    """
    Returns a NEW list with all empty strings removed.
    Does NOT modify the original list.
    """
    result = []
    for item in my_list:
        if item != "":
            result.append(item)
    return result
```

**[Say:]**

"Notice how the docstrings tell the story. The first function explicitly says it MUTATES. The second says it does NOT modify the original. When someone (including future you) reads these, there's zero confusion about what will happen."

---

## 5. Live Demo: Normalize Names – Two Ways (~15 minutes)

**[Say:]**

"Let's work through a realistic data-cleaning scenario. Imagine you have a list of names from a form, but they're messy: uppercase, lowercase, extra spaces. We need to normalize them."

**[Type slowly and narrate each step:]**

```python
# Raw data from a user form
raw_names = ["  alice smith", "BOB  JONES", " cHarLiE bRoWn "]

print("=" * 50)
print("APPROACH 1: Return a new list (Safer)")
print("=" * 50)

def clean_names_return_new(name_list):
    """
    Returns a NEW list of cleaned, title-cased names.
    Original list is never modified.
    """
    cleaned = []
    for name in name_list:
        # Strip whitespace, then title-case it
        clean = name.strip().title()
        cleaned.append(clean)
    
    return cleaned

print(f"Original names (before): {raw_names}")
cleaned_copy = clean_names_return_new(raw_names)
print(f"Returned new list: {cleaned_copy}")
print(f"Original names (after): {raw_names}")
print("→ Notice: Original is unchanged!")

print("\n" + "=" * 50)
print("APPROACH 2: Mutate in-place (Faster)")
print("=" * 50)

def clean_names_inplace(name_list):
    """
    MUTATES the list by cleaning all names in-place.
    The original list is modified. No return value.
    """
    for i in range(len(name_list)):
        name_list[i] = name_list[i].strip().title()

# Reset for second demo
raw_names = ["  alice smith", "BOB  JONES", " cHarLiE bRoWn "]

print(f"Original names (before): {raw_names}")
clean_names_inplace(raw_names)
print(f"Original names (after): {raw_names}")
print("→ Notice: Original was modified!")

print("\n" + "=" * 50)
print("Which approach is better?")
print("=" * 50)
print("For most beginner use cases: Return a new list.")
print("It's safer and easier to reason about.")
print("When memory is critical: Mutate in-place.")
```

**[Expected output:]**
```
==================================================
APPROACH 1: Return a new list (Safer)
==================================================
Original names (before): ['  alice smith', 'BOB  JONES', ' cHarLiE bRoWn ']
Returned new list: ['Alice Smith', 'Bob Jones', 'Charlie Brown']
Original names (after): ['  alice smith', 'BOB  JONES', ' cHarLiE bRoWn ']
→ Notice: Original is unchanged!

==================================================
APPROACH 2: Mutate in-place (Faster)
==================================================
Original names (before): ['  alice smith', 'BOB  JONES', ' cHarLiE bRoWn ']
Original names (after): ['Alice Smith', 'Bob Jones', 'Charlie Brown']
→ Notice: Original was modified!

==================================================
Which approach is better?
==================================================
For most beginner use cases: Return a new list.
It's safer and easier to reason about.
When memory is critical: Mutate in-place.
```

**[Say:]**

"Both approaches work. Both are valid Python. The choice depends on your context and your intent. In production data pipelines, returning a new list is the default because it prevents silent bugs. In-place mutation is an optimization for when you're absolutely sure you want to destroy the original."

---

## 6. Practice Walkthrough: Extracting Specific Items (~8 minutes)

**[Say:]**

"Let's do a smaller, guided example together. I'm going to write a function that does something common: filtering a list to keep only items that match a condition."

**[Type step by step, explaining each line:]**

```python
# A list of student scores
scores = [45, 87, 92, 65, 78, 91, 55, 88]

def get_passing_scores(score_list):
    """
    Returns a NEW list containing only scores >= 70.
    Passing score is 70.
    Original list is not modified.
    """
    passing = []
    
    for score in score_list:
        if score >= 70:
            passing.append(score)
    
    return passing

print("All scores:", scores)
result = get_passing_scores(scores)
print("Passing scores only:", result)
```

**[Expected output:]**
```
All scores: [45, 87, 92, 65, 78, 91, 55, 88]
Passing scores only: [87, 92, 78, 91, 88]
```

**[Say:]**

"Notice three things:

1. We created a brand-new empty list called `passing` inside the function.
2. We looped through the original list, checking a condition, and only appending items that meet it.
3. We returned the new list and captured it in a variable `result`.

The original `scores` list is untouched. This is the pattern you'll use hundreds of times in Python."

---

## 7. Lab with Full Checkpoints: Normalize Contacts (~30 minutes)

**[Say:]**

"Now it's your turn. You're going to write a contact-cleaning function from scratch. Your task is realistic: you've received a messy list of contact names from a form, and you need to normalize them so they're consistent and professional-looking."

### 7.1 Lab Specification

**[Display or hand out:]**

```
TASK: Normalize Contacts

You have a list of contact names that need cleaning:
  ["  sarah jones ", "MARK smith", " tina turner  "]

Write a function called normalize_contacts(contacts) that:
  1. Strips all leading and trailing whitespace from each name
  2. Converts each name to title case (capitalize the first letter of each word)
  3. Returns (or modifies in-place—your choice) the cleaned list

Example output:
  ["Sarah Jones", "Mark Smith", "Tina Turner"]

Your function MUST:
  - Have a docstring explaining whether you mutate or return
  - Work correctly on the provided test data
  - Be readable and follow the patterns we just showed

Choose your approach:
  Option A: Return a new list (safe, default)
  Option B: Mutate in-place (fast, but destructive)
  Write your choice in your docstring!
```

### 7.2 Checkpoint Breakdown with Time Estimates

**Checkpoint 1 (2 min):** Set up your file and create the raw data list.
```python
# Create the raw data exactly as shown
raw_contacts = ["  sarah jones ", "MARK smith", " tina turner  "]
print("Original:", raw_contacts)
```

**Checkpoint 2 (5 min):** Write the function stub with a docstring.
```python
def normalize_contacts(contacts):
    """
    [Your docstring here explaining your approach]
    """
    pass
```

**Checkpoint 3 (8 min):** Write the loop that processes each name.
- Start with an empty list (if using "return new list" approach)
- Loop through each name in contacts
- For each name, apply `.strip().title()`
- Either append to new list or reassign in the original list

**Checkpoint 4 (5 min):** Add the return statement (if using "return new list" approach) or verify in-place changes.
- If returning: `return cleaned_list`
- If mutating: No return needed, but double-check that the original list was updated

**Checkpoint 5 (3 min):** Call your function and capture/display the result.
```python
# If you returned a new list:
cleaned = normalize_contacts(raw_contacts)
print("Cleaned:", cleaned)

# If you mutated in-place:
normalize_contacts(raw_contacts)
print("Cleaned:", raw_contacts)
```

**Checkpoint 6 (2 min):** Verify the output is correct.
- All names should have proper capitalization: "Sarah Jones", "Mark Smith", "Tina Turner"
- No extra spaces before or after any name

**Checkpoint 7 (5 min):** (Stretch) Add a second test case to verify your function works generally.
```python
test_names = ["  juan perez  ", "LISA ANDERSON", "  mike wilson"]
result = normalize_contacts(test_names)
print("Test result:", result)
```

### 7.3 Instructor Guidance During Lab Time

**Common mistakes to watch for:**

1. **Forgot to capture the return value:** Students call `normalize_contacts(names)` but don't assign to a variable, then print the original raw names and wonder why nothing changed.
   - **Remediation:** Ask "What did the function return? Where did you put it?"

2. **Loop variable reassignment (mutation attempt with wrong pattern):** 
   ```python
   for name in contacts:
       name = name.strip().title()  # This doesn't work!
   ```
   - This reassigns the loop variable `name` but doesn't update the list.
   - **Remediation:** Show them `contacts[i] = ...` pattern or "create a new list and return it."

3. **Missing or incorrect docstring:** Remind them the docstring is not optional. It's the contract.

### 7.4 Walkthrough Solution (Show After 25 Minutes)

**[Say:] "Let me show you one complete solution. You might have taken a different approach, and that's fine—as long as it works."**

```python
# Hour 35: Normalize Contacts Lab Solution
# Using the "return new list" approach (safest for beginners)

def normalize_contacts(contacts):
    """
    Returns a NEW list of normalized contact names.
    Each name is stripped of whitespace and title-cased.
    The original list is NOT modified.
    """
    cleaned = []
    
    for name in contacts:
        # Strip whitespace from both ends, then title-case
        normalized_name = name.strip().title()
        cleaned.append(normalized_name)
    
    return cleaned

# Test data from the form (messy)
raw_data = ["  sarah jones ", "MARK smith", " tina turner  "]

print("BEFORE NORMALIZATION:")
print(f"  {raw_data}")

# Call the function and capture the result
normalized_data = normalize_contacts(raw_data)

print("\nAFTER NORMALIZATION:")
print(f"  {normalized_data}")

print("\nWAS ORIGINAL MODIFIED?")
print(f"  Original: {raw_data}")
print(f"  → No, it's still messy. The function returned a new list.")
```

**[Expected output:]**
```
BEFORE NORMALIZATION:
  ['  sarah jones ', 'MARK smith', ' tina turner  ']

AFTER NORMALIZATION:
  ['Sarah Jones', 'Mark Smith', 'Tina Turner']

WAS ORIGINAL MODIFIED?
  Original: ['  sarah jones ', 'MARK smith', ' tina turner  ']
  → No, it's still messy. The function returned a new list.
```

**[Say:]**

"This is the gold standard for data transformation functions. You take in messy data, you return clean data, and the original is left untouched. This pattern is used in every data science library, every web framework, and every real-world Python program."

---

## 8. Troubleshooting Pitfalls: Seven Common Mistakes

**Pitfall 1: Forgetting to Capture the Return Value**

**Problem:** Student writes:
```python
normalize_contacts(names)
print(names)
```

They expect `names` to be changed, but it's not—because the function returned a new list and they didn't capture it.

**Remedy:** "If your function returns something, you must assign it to a variable: `cleaned = normalize_contacts(names)`. Then print `cleaned`."

---

**Pitfall 2: Trying to Mutate by Reassigning the Loop Variable**

**Problem:** Student writes:
```python
for name in contacts:
    name = name.strip().title()  # This does NOT update the list!
print(contacts)  # Still messy!
```

**Remedy:** "When you reassign `name`, you're only changing the loop variable, not the list. To mutate, use indexing: `for i in range(len(contacts)): contacts[i] = contacts[i].strip().title()`"

---

**Pitfall 3: Missing Docstring**

**Problem:** Function is ambiguous—does it mutate or return?

**Remedy:** Every collection function must have a docstring. It's the contract. Make it a habit now.

---

**Pitfall 4: Mutating a List While Iterating Forward Over It**

**Problem:** Student removes or inserts items while using `for i in range(len(my_list))`.

```python
for i in range(len(contacts)):
    if "old" in contacts[i]:
        contacts.pop(i)  # This skips the next item!
```

**Remedy:** If you must mutate while iterating, iterate backward: `for i in range(len(contacts) - 1, -1, -1):`

---

**Pitfall 5: Forgetting to Return the New List**

**Problem:** Student builds a new list but forgets the `return` statement.

```python
def clean_names(names):
    cleaned = []
    for name in names:
        cleaned.append(name.strip().title())
    # Oops, no return!

result = clean_names(names)
print(result)  # None!
```

**Remedy:** "If you build a new list, always return it at the end."

---

**Pitfall 6: Assuming Strings Are Mutable**

**Problem:** Student tries to mutate a string inside a function.

```python
def uppercase_it(s):
    s[0] = "X"  # TypeError: 'str' object does not support item assignment
```

**Remedy:** "Strings are immutable. You can't change them. You can only create new strings: `s = s.upper()`"

---

**Pitfall 7: Modifying a Dictionary Inside a Function and Forgetting to Document It**

**Problem:** Function mutates a dictionary, but the docstring doesn't say so.

```python
def update_user(user_dict):
    """Updates the user's age."""  # Not clear that the dict is mutated!
    user_dict["age"] = 30
```

**Remedy:** "Always be explicit: 'MUTATES the provided dictionary by updating the age field.' or 'Returns a NEW dict with the age updated.'"

---

## 9. Quick-Check Questions: Formative Assessment (~5 minutes)

**[After the lab, ask these questions. Allow students to discuss and respond.]**

**Question 1:** "When you pass a list into a function, does Python make a copy of the list, or does it pass a reference to the original?"

**Expected answer:** "It passes a reference. The function sees the same list you see."

---

**Question 2:** "If a function builds a new list and returns it, and you call the function but don't assign the result to a variable, what happens to the new list?"

**Expected answer:** "It gets thrown away. You have to capture it in a variable like `result = my_func(data)`."

---

**Question 3:** "What is the purpose of a docstring when working with collections?"

**Expected answer:** "To tell the reader whether the function mutates the original list or returns a new one. It's the contract between the function and whoever calls it."

---

**Question 4:** "You have a function that strips and title-cases names. Which approach is safer for beginners: returning a new list, or mutating in-place?"

**Expected answer:** "Returning a new list is safer because the original data is never touched. Less chance of accidental data loss."

---

**Question 5:** "You're iterating through a list and removing items. Should you iterate forward with `for i in range(len(my_list))` or backward with `for i in range(len(my_list) - 1, -1, -1)`?"

**Expected answer:** "Backward. If you iterate forward and remove items, you'll skip elements because the indices shift."

---

## 10. Wrap-Up Narrative: Recap and Preview (~2 minutes)

**[Read aloud, naturally, as a closing thought]**

"Today was about making a critical choice: when you pass a collection into a function, you have the power to change it. That's powerful, but it requires discipline.

Here's what we've learned:

**One:** Collections are passed by reference. The function receives a direct link to the original list or dictionary.

**Two:** You choose your strategy. Either mutate (change the original in-place), or return a new collection. There's no right answer for every situation, but beginners should favor returning a new collection because it's safer.

**Three:** Always use a docstring to make your intention crystal clear. Other programmers (or future you) will thank you.

**Four:** Watch out for common traps: forgetting to capture return values, trying to reassign loop variables when you mean to mutate the list, and removing items while iterating forward.

Next hour, we're going to go even deeper. We'll learn about debugging functions, about writing tests to verify they work correctly, and about organizing your functions into libraries so you can reuse them forever.

For now, practice the normalize_contacts pattern. Get comfortable with it. This is a pattern that appears in nearly every Python program ever written."

---

## 11. Facilitation Notes: Pacing, Differentiation, and Extensions

### 11.1 Pacing Strategy

- **Opening script:** 3 min (don't rush; the mental model matters)
- **Conceptual briefing:** 12 min (be clear about mutation vs. return; use analogies if needed)
- **Live demo:** 15 min (code slowly, explain each line, show both outputs)
- **Practice walkthrough:** 8 min (guide them through the filtering example)
- **Lab:** 30 min (let them struggle a little; that's learning)
- **Quick-check questions:** 5 min
- **Wrap-up:** 2 min
- **Buffer:** 5 min (for questions, debugging, or deep dives)

### 11.2 Differentiation

**For students who finish the lab early (Stretch):**
- Add a second test case to verify generalizability
- Write both an in-place and return-new version, compare the docstrings
- Write a function that filters the contacts list to only names containing a certain letter
- Challenge: Write a function that sorts contacts by last name

**For students who are struggling:**
- Pair them with a faster student for the lab portion
- Provide a template with the loop structure and docstring already in place
- Focus on understanding the mutation vs. return decision first; code patterns come second
- Use the checkpoint approach: celebrate each small win

### 11.3 Extensions (If Time Allows)

**Extension 1: Aggregation Pattern**
Show a function that combines multiple items from a list into a single value:
```python
def total_score(scores):
    """Returns the sum of all scores in the list."""
    total = 0
    for score in scores:
        total += score
    return total
```

**Extension 2: Nested Collections**
A function that works with a list of dictionaries:
```python
def extract_names(contacts):
    """Returns a list of names extracted from a list of contact dicts."""
    names = []
    for contact in contacts:
        names.append(contact["name"])
    return names
```

**Extension 3: The `any()` and `all()` Built-ins**
Show how Python provides shortcuts for aggregating boolean conditions:
```python
all_passed = all(score >= 70 for score in scores)
```

---

## 12. Assessment and Differentiation Rubric

### 12.1 Completion-Based Rubric (Normalize Contacts Lab)

| Criterion | Proficient (✓) | Developing (◐) | Not Yet (✗) |
|-----------|---|---|---|
| **Data setup** | Raw list correctly created | List created but with errors | List missing or incorrect |
| **Function definition** | Function named correctly, takes one parameter | Function exists but parameter missing or named wrong | Function not defined |
| **Docstring** | Clear, accurate description of mutation/return approach | Docstring exists but unclear or incomplete | Missing docstring |
| **Processing logic** | Correctly strips and title-cases all names using `.strip().title()` | Some names processed, but logic incomplete or wrong | No processing or incorrect methods used |
| **Output** | All three names correctly formatted: "Sarah Jones", "Mark Smith", "Tina Turner" | Output mostly correct but 1–2 names wrong | Output incorrect or missing |
| **Testing** | Function tested and verified to work | Function called but output not verified | Function not called |

### 12.2 Mastery-Based Progression

**Level 1: Basic Understanding**
- Student can identify whether a function mutates or returns based on reading code.
- Student can write a function that returns a new list.

**Level 2: Applied Understanding**
- Student can write either mutation or return functions with correct logic.
- Student can write docstrings that explain the function's behavior.

**Level 3: Advanced Reasoning**
- Student can explain when to use mutation vs. return based on performance and safety considerations.
- Student can write both mutation and return versions and justify the choice.
- Student can identify and debug common pitfalls in others' code.

### 12.3 Differentiation Pathways

**Struggling students:**
- Provide function skeleton with comments
- Use simpler data (3 names instead of larger lists)
- Focus on understanding the mutation decision first
- Celebrate partial progress

**On-track students:**
- Use the standard lab as-is
- Encourage both mutation and return solutions
- Discuss the tradeoffs

**Advanced students:**
- Ask them to write both versions and compare
- Challenge them with nested structures (list of dicts)
- Have them predict output before running code
- Ask them to teach a struggling peer

---

**End of Hour 35 Lecture Script**

*This script is complete and ready for verbatim classroom delivery. Modify timing as needed based on your classroom dynamics. The key is clarity on the mutation decision—students will carry this insight forward into every function they write.*
