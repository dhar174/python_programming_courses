# Day 5, Hour 3: Dictionaries Fundamentals (Course Hour 19)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 19 – Dictionaries fundamentals  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. This hour introduces dictionaries as the fourth and most versatile data structure of Session 5. Dictionaries map keys to values. The critical patterns for this hour are: creating a dict literal, reading a value with `dict[key]`, the `KeyError` when a key is missing, the safe alternative `dict.get(key, default)`, updating an existing entry, and adding a new entry. Stay within Basics scope. Do not introduce `defaultdict`, `Counter`, `OrderedDict`, dict comprehensions, `setdefault()`, or `.copy()`. The lab is the Inventory Manager. The demo centers on an inventory dict that demonstrates `KeyError` vs `get()` clearly.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:
1. Explain what a dictionary is using the key-value concept in plain language.
2. Create a dictionary literal with string keys and numeric values.
3. Access a value by its key using `dict[key]` and understand what `KeyError` means.
4. Access a value safely using `dict.get(key, default)` to avoid crashes on missing keys.
5. Update an existing entry and add a new entry to a dictionary.
6. Check whether a key exists in a dictionary using `in`.
7. Build an Inventory Manager program that stores item quantities, updates them on request, and handles missing keys gracefully.

Dictionaries are one of the most powerful and widely used structures in Python. They appear in web APIs, configuration files, JSON data, database results, and countless everyday scripts. Mastering the fundamentals today sets you up for everything that follows."

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Recap of sets, transition to dictionaries, and the key-value concept
- **0:05–0:15** Creating a dict, reading values, and the KeyError
- **0:15–0:25** `get()` with a default, `in` for key checking, updating and adding entries
- **0:25–0:35** Live demo: inventory dict with updates, KeyError, and safe access
- **0:35–0:45** Common pitfalls: case sensitivity, accidental new key, string vs number keys
- **0:45–0:57** Guided lab: Inventory Manager
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour19_dicts_demo.py`.
- Prepare a sample inventory dict mentally: `{"apples": 30, "bananas": 12, "milk": 5, "bread": 8, "eggs": 24}`.
- Be ready to show a deliberate `KeyError` and then immediately contrast with `get()`.
- Be ready to demonstrate that assigning to a new key silently creates the entry (no error, but this can be a pitfall).
- Be ready to show case sensitivity: `"Apples"` and `"apples"` are different keys.
- If some learners type slowly, have a starter file with comments only ready.

**Say:** "Dictionaries are the structure you will use most in real Python programs. Please type with me today—the key-value idea clicks much faster when you experience it hands-on."

---

## 3) Opening Script: The Key-Value Concept (~5 minutes)

### 3.1 Recap and frame the new structure

**Say:**
"Welcome back. Let's briefly place where we are.

In this session we have studied:
- Lists: ordered, mutable collections
- Tuples: ordered, immutable records
- Sets: unordered collections of unique values

Each structure answers a different kind of question. Lists answer 'What is item number three?' Tuples answer 'What are the two fixed parts of this record?' Sets answer 'Is this value present, and how many unique values do I have?'

Today's structure—the dictionary—answers a completely different question: 'What is the value that belongs to this key?'"

### 3.2 Real-world analogy: an actual dictionary

**Say:**
"The name 'dictionary' is a perfect analogy. In a real dictionary, every entry has two parts: the word (which is the key) and the definition (which is the value).

You do not look up a definition by number—you look it up by name. You say, 'I want the definition of the word *algorithm*,' and the dictionary jumps directly to that entry.

Python dictionaries work the same way. You say, 'Give me the value associated with the key *apples*,' and Python goes directly to that entry. You do not need to know which position it is in, just the key."

### 3.3 More real-world examples

**Say:**
"Let me give you a few more examples so the concept is concrete before we see any code.

- A phone book: name → phone number
- An inventory system: product name → quantity in stock
- A student record: field name → value (like `'grade': 'A'`, `'age': 19`)
- A configuration file: setting name → setting value
- A word frequency counter: word → how many times it appears in a document

Every one of these is a mapping from some unique identifier—the key—to some piece of data—the value.

That is all a dictionary is: a collection of named values."

---

## 4) Core Concept: Creating and Reading a Dictionary (~10 minutes)

### 4.1 Dictionary literal syntax

**Say:**
"A dictionary is written with curly braces, colons separating each key from its value, and commas separating the pairs."

**Type:**

```python
inventory = {
    "apples": 30,
    "bananas": 12,
    "milk": 5,
    "bread": 8,
    "eggs": 24,
}

print(inventory)
print(type(inventory))
```

Run it.

**Say:**
"Python shows us the entire dictionary when we print it. The format is the same as we wrote it: curly braces, key-colon-value pairs.

`type(inventory)` confirms `<class 'dict'>`.

Notice I put each pair on its own line with a trailing comma after the last entry. This is a style choice, but it is a very readable one—especially when dictionaries grow large. Python allows it, and it makes the structure easier to read."

### 4.2 Accessing a value by key

**Type:**

```python
print(inventory["apples"])
print(inventory["milk"])
```

Run it.

**Say:**
"The syntax for reading a value is `dict[key]`. You put the key inside square brackets, just like indexing a list—except instead of a position number, you use the key name.

`inventory['apples']` gives us `30`. `inventory['milk']` gives us `5`.

This is the most fundamental operation in every dict program: look up a value by its key."

### 4.3 KeyError: what happens with a missing key

**Say:**
"Now let me show you what happens if the key does not exist."

**Type:**

```python
print(inventory["oranges"])  # This will cause a KeyError
```

Run it.

**Say:**
"We get a `KeyError: 'oranges'`. Python is telling us: I searched the dictionary and I cannot find a key called 'oranges'.

This is not an unusual error. It is one of the most common errors in dict-heavy programs. The good news is it is easy to prevent.

Before I show you the prevention, let me emphasize: do not feel afraid of this error. It is informative. It tells you exactly which key caused the problem."

### 4.4 Safe access with `get()`

**Say:**
"The `get()` method is the standard way to read from a dictionary without risking a `KeyError`. It takes two arguments: the key you want, and a default value to return if the key is not present."

**Type:**

```python
# Safe access with a default value
quantity = inventory.get("oranges", 0)
print(f"Oranges in stock: {quantity}")

# Key that exists
quantity = inventory.get("apples", 0)
print(f"Apples in stock: {quantity}")
```

Run it.

**Say:**
"When we call `inventory.get('oranges', 0)`, Python looks for the key 'oranges'. It is not there, so Python returns the default we specified: `0`. No error.

When we call `inventory.get('apples', 0)`, Python finds 'apples' and returns its value, `30`. The default is ignored when the key exists.

The second argument to `get()` is the default return value. You can use `0`, an empty string, `None`, or whatever makes sense for your program.

Make a habit of using `get()` whenever there is any chance the key might be missing."

### 4.5 Checking for key existence with `in`

**Say:**
"An alternative to `get()` is checking explicitly whether the key exists before reading."

**Type:**

```python
item = "bread"
if item in inventory:
    print(f"{item}: {inventory[item]} in stock")
else:
    print(f"{item} is not in the inventory")

item = "oranges"
if item in inventory:
    print(f"{item}: {inventory[item]} in stock")
else:
    print(f"{item} is not in the inventory")
```

Run it.

**Say:**
"The `in` operator on a dictionary checks whether the key exists. It does not check values—only keys.

Both approaches are valid:
- Use `in` when you want to do different things depending on whether the key exists.
- Use `get()` when you just want a safe read with a fallback default.

For the Inventory Manager lab, you will want to use one or both of these patterns to avoid crashing when a user asks for an item that is not in stock."

---

## 5) Updating and Adding Entries (~8 minutes)

### 5.1 Updating an existing entry

**Say:**
"Updating an entry in a dictionary is simple: assign a new value to an existing key."

**Type:**

```python
print(f"Apples before: {inventory['apples']}")
inventory["apples"] = 45
print(f"Apples after: {inventory['apples']}")
```

Run it.

**Say:**
"We changed the quantity for 'apples' from 30 to 45. The assignment `inventory['apples'] = 45` finds the key 'apples' and updates its value.

This is mutation—we are changing the dictionary in place. The key stays the same; the value is replaced."

### 5.2 Incrementing a value

**Say:**
"In real inventory programs, you often want to increase or decrease a quantity rather than setting it to a fixed number."

**Type:**

```python
# Receive a delivery of 10 more bananas
inventory["bananas"] += 10
print(f"Bananas: {inventory['bananas']}")

# Sell 3 loaves of bread
inventory["bread"] -= 3
print(f"Bread: {inventory['bread']}")
```

Run it.

**Say:**
"The `+=` and `-=` operators work on dictionary values the same way they work on regular variables. `inventory['bananas'] += 10` is shorthand for `inventory['bananas'] = inventory['bananas'] + 10`."

### 5.3 Adding a new entry

**Say:**
"Adding a new key to a dictionary uses the exact same assignment syntax as updating. If the key already exists, the value is updated. If the key does not exist, Python creates a new entry."

**Type:**

```python
# Add a new item
inventory["yogurt"] = 15
print(f"Yogurt: {inventory['yogurt']}")
print(f"Total unique items: {len(inventory)}")
```

Run it.

**Say:**
"Python silently added 'yogurt' to the dictionary. There is no separate 'add' method—assignment is the universal operation for both creating and updating entries.

This is both convenient and dangerous. It is convenient because adding new items is effortless. It is dangerous because a typo in a key name will silently create a new entry instead of raising an error.

For example, if I type `inventory['Apples'] = 50` with a capital A, Python does not update the existing 'apples' entry—it creates a brand-new entry called 'Apples'. The original 'apples' entry is still there, unchanged. This is a classic beginner bug."

**Type:**

```python
print("apples" in inventory)   # True — original
print("Apples" in inventory)   # Check — is there a capital version?
```

**Say:**
"Run this to see whether the capital version accidentally exists in your current dict. The point is: dictionary keys are case-sensitive strings. Always be consistent with your key names."

---

## 6) Full Live Demo: Inventory System (~8 minutes)

### 6.1 Build the complete demo

**Say:**
"Let me put everything together in a short but complete inventory program."

**Type:**

```python
# hour19_dicts_demo.py

inventory = {
    "apples": 30,
    "bananas": 12,
    "milk": 5,
    "bread": 8,
    "eggs": 24,
}

# --- Show current inventory ---
print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")

# --- Ask user for an item to restock ---
item_name = input("\nEnter an item to restock: ").strip().lower()
restock_qty = int(input(f"How many more {item_name} to add? "))

if item_name in inventory:
    inventory[item_name] += restock_qty
    print(f"Updated! {item_name} is now {inventory[item_name]}.")
else:
    print(f"'{item_name}' was not found in inventory.")
    print(f"Here is what is available: {sorted(inventory.keys())}")

# --- Safe read using get() ---
check = "oranges"
qty = inventory.get(check, 0)
print(f"\nStock check for '{check}': {qty}")
```

Run it with a few different inputs.

**Say:**
"Notice a few things in this demo:

First, I used `inventory.items()` in the `for` loop to get both the key and value at the same time. We will explore `items()` in depth in the next hour—for now, just notice that it exists and lets you print a neat inventory table.

Second, I used `.strip().lower()` on the user's input. `strip()` removes accidental spaces. `lower()` normalizes the case so that 'Apples', 'APPLES', and 'apples' all match the lowercase key in the dictionary.

Third, the `get()` call at the end shows a safe read for 'oranges', which is not in the inventory. The default `0` prevents a crash.

These three patterns—`items()`, normalizing input, and `get()`—are the core moves in any real dictionary-driven program."

---

## 7) Common Pitfalls and How to Coach Through Them (~5 minutes)

### 7.1 Pitfall: KeyError on direct access

**Symptom:** learner writes `print(inventory["oranges"])` and gets a `KeyError`.

**Coach with these words:**
"Read the error: `KeyError: 'oranges'`. Python is telling you that key does not exist. Your two options: use `if 'oranges' in inventory` to check first, or switch to `inventory.get('oranges', 0)` for a safe default. Which one fits your program better?"

### 7.2 Pitfall: case sensitivity creating phantom keys

**Symptom:** learner types `inventory["Apples"] = 50` and is confused why `inventory["apples"]` is unchanged.

**Coach with these words:**
"Strings are case-sensitive in Python. 'Apples' with a capital A and 'apples' in lowercase are two completely different keys. Print `list(inventory.keys())` to see all current keys. You likely have both 'apples' and 'Apples' now. To prevent this, normalize your keys to lowercase when the user types them."

### 7.3 Pitfall: accidentally creating a new key via typo

**Symptom:** learner writes `inventory["appels"] = 999` (misspelled) and then cannot understand why `inventory["apples"]` is still 30.

**Coach with these words:**
"Check what is actually in the dictionary: `print(inventory)`. You will see both 'apples' and 'appels'. Dictionary assignment never raises an error, even for brand-new keys. This is why input validation and lowercase normalization are important in real programs."

### 7.4 Pitfall: confusing `dict[key]` with `dict.get(key)`

**Symptom:** learner writes `inventory.get("apples")` expecting it to always return the value, but gets `None` when the default is omitted.

**Coach with these words:**
"If you call `get()` with only one argument and the key is missing, Python returns `None` by default. To get `0` instead of `None`, add the second argument: `inventory.get('apples', 0)`. Always provide a meaningful default when the key might not exist."

### 7.5 Pitfall: confusion between `{}` (empty dict) and `set()`

**Symptom:** learner coming from the previous hour tries to use `set()` for a dictionary.

**Coach with these words:**
"Great instinct from last hour! `set()` gives a set. For a dictionary, use `{}` with key-colon-value pairs, or start with `{}` for an empty dictionary. The braces are shared between sets and dicts—the colon is what makes a value a dict."

---

## 8) Guided Lab: Inventory Manager (~12 minutes)

### 8.1 Introduce the lab

**Say:**
"Your task is to build an Inventory Manager. Here are the requirements:

1. Create a dictionary with 5 items and their quantities. Use string keys (item names) and integer values (quantities).
2. Print the current inventory neatly.
3. Ask the user for an item name.
4. If the item exists in the inventory, ask how much to add and increase the quantity.
5. If the item does not exist, print a friendly message instead of crashing.
6. Print the updated inventory."

### 8.2 Put the requirements on screen

```text
Lab: Inventory Manager
- Create a dict with 5 items and quantities
- Print the current inventory
- Ask user for an item name
- If the item exists: increase quantity by a user-entered amount
- If it does not exist: print a friendly "not found" message
- Print the updated inventory
```

### 8.3 Provide a beginner-friendly starter structure

**Type and leave on screen:**

```python
# hour19_lab_inventory_manager.py

# Step 1: create the inventory dict
inventory = {
    "apples": 30,
    "bananas": 12,
    "milk": 5,
    "bread": 8,
    "eggs": 24,
}

# Step 2: print current inventory
print("=== Inventory ===")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")

# Step 3: ask for user input
item_name = input("\nWhich item do you want to restock? ").strip().lower()

# Step 4: check and update
if item_name in inventory:
    amount = int(input(f"How many {item_name} to add? "))
    inventory[item_name] += amount
    print(f"Updated {item_name}. New quantity: {inventory[item_name]}")
else:
    print(f"'{item_name}' is not in the inventory.")
    print("Available items:", sorted(inventory.keys()))

# Step 5: print updated inventory
print("\n=== Updated Inventory ===")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")
```

### 8.4 Explain the starter

**Say:**
"This starter demonstrates the complete pattern for a safe, user-friendly inventory program.

Notice `.strip().lower()` on the user input—this normalization is a small addition that prevents most case-sensitivity bugs.

The `for item, qty in inventory.items()` loop lets us print both key and value on each line. We will study `items()` in depth in the next hour, but for now just understand that it gives us key-value pairs together.

Your goal is to get this working end-to-end. Try it once with an item that exists and once with an item that does not."

### 8.5 Optional extension

**Say:**
"If you finish the core lab, try this extension: normalize all keys in the initial dictionary to lowercase when you create it. Then add a feature that lets the user keep restocking multiple items until they type 'done'.

A simpler extension: after the update, also show which item has the highest quantity using `max()` on the values."

**Type the simpler extension hint:**

```python
# Optional extension: find highest-stock item
max_item = max(inventory, key=lambda item: inventory[item])
print(f"\nHighest stock item: {max_item} ({inventory[max_item]} units)")
```

**Say:**
"The `key=lambda item: inventory[item]` part tells `max()` how to compare items—by their dict values rather than by their names alphabetically. Do not worry about fully understanding `lambda` today; that is an Advanced topic. Just know this pattern exists and you can use it."

### 8.6 Instructor circulation prompts

As learners work, walk around and ask:
- "Show me your dictionary. What are the keys? What are the values?"
- "What happens when you type an item that is not in the dict?"
- "Did you use `in` or `get()` for the safety check?"
- "What does `strip().lower()` do to the user's input?"
- "Where does the quantity actually change in your code?"

---

## 9) Debrief and Share-Outs (~4 minutes)

### 9.1 Bring the class back together

**Say:**
"Let's discuss what we built. Dictionaries have more moving parts than lists or sets, so I want to hear how you solved the 'not found' case."

### 9.2 Ask targeted questions

Ask:
- "Who used `if item in inventory` before accessing the value? Who used `get()`? Which felt more natural?"
- "Did anyone encounter a case sensitivity problem? How did you handle it?"
- "Who used `.strip().lower()` on the user input? What problem does that prevent?"
- "Who printed the inventory neatly? What did your loop look like?"

### 9.3 Model a concise explanation

**Say:**
"A strong description of this lab: 'I created a dict with five items. I printed it using a for loop over `items()`. I took user input, normalized it to lowercase, checked with `in` whether the key existed, updated the quantity if found, and printed a friendly message otherwise. Then I reprinted the inventory.'

That is a complete, correct description of a real data-driven program."

---

## 10) Recap Script (~2 minutes)

**Say:**
"Today we introduced dictionaries. The foundational ideas:

- A dictionary stores key-value pairs in curly braces with colons: `{'key': value}`.
- Access a value with `dict[key]`. Missing keys raise `KeyError`.
- Use `dict.get(key, default)` for safe access without crashing.
- Use `key in dict` to check whether a key exists.
- Assign to update or create entries: `dict[key] = new_value`.
- Keys are case-sensitive. Normalize user input with `.lower()` to avoid phantom keys.

In the next hour, we learn how to iterate through a dictionary's entries using `items()`, and we build the frequency-counting pattern—one of the most powerful patterns in beginner Python."

---

## 11) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. What error do you get when you access a key that does not exist with `dict[key]`?
2. How does `dict.get('apples', 0)` behave differently from `dict['apples']` when 'apples' is missing?
3. If you assign `dict['NewKey'] = 100` and 'NewKey' was not in the dict before, what happens?
4. Why should you normalize user input with `.lower()` before looking it up in a dictionary?

**Expected direction of answers:**
- `KeyError` with the missing key name
- `get()` returns the default `0` instead of raising an error
- Python silently creates a new entry for 'NewKey' with value 100
- because 'Apple' and 'apple' are different string keys; normalization prevents phantom entries

---

## 12) Instructor Notes for the Transition to Hour 20

**Say:**
"We now understand the fundamentals of creating, reading, updating, and protecting against missing keys in a dictionary. In the next hour, we deepen that skill by learning how to iterate through an entire dictionary—using `items()` to loop over key-value pairs—and we build the frequency-counting pattern, which you will use in many real programs."

If learners seem shaky, reinforce:
- "`dict[key]` reads a value, but raises an error if the key is missing."
- "`dict.get(key, default)` is always safe."
- "Assignment creates or updates. Keys are case-sensitive."

---

## Appendix: Instructor Reinforcement Notes for Hour 19

### A) Board sketch for visual learners

Draw this on the board:

```text
inventory = {
    "apples" : 30,   ← key : value
    "bananas": 12,
    "milk"   : 5,
}

inventory["apples"]       → 30          (direct access)
inventory["oranges"]      → KeyError    (missing key)
inventory.get("oranges", 0) → 0         (safe access)
inventory["apples"] = 45  → updates     (mutation)
inventory["yogurt"] = 15  → adds new    (creation)
```

Point to each row and ask: "What does Python return here? What does Python do here?"

### B) Short extra practice prompts

If you have extra minutes:

1. If `d = {'a': 1, 'b': 2}`, what does `d['b']` return?
2. What does `d.get('c', -1)` return?
3. After `d['a'] = 99`, what does `d['a']` return?
4. What does `'a' in d` return? What does `'z' in d` return?
5. If the user types 'APPLES', what key does `'APPLES'.lower()` produce?

### C) Instructor language for gentle correction

- "Read the `KeyError` message. What key was Python looking for? Is that key in your dictionary?"
- "Print `list(inventory.keys())` and look carefully. Do you see a capitalization difference?"
- "Before accessing the value, add `if key in inventory` as a guard. That one line prevents most crashes."
- "Is your assignment updating an existing key or accidentally creating a new one? Print the dict after and count the keys."

### D) Coaching if learners ask about defaultdict or Counter

If a learner asks about `collections.defaultdict` or `collections.Counter`, say:

"Both of those exist and are useful for more advanced programs. `defaultdict` automatically provides a default value when you access a missing key. `Counter` is a specialized dict for counting. Both are Advanced-scope tools—they are in the next session. For now, the `get(key, 0)` pattern gives you the same power for counting without any imports."

### E) Final teaching reminder to yourself

The hour succeeds if learners leave with this mental model:

"A dictionary maps keys to values. I read with `dict[key]`, protect with `.get(key, default)`, check with `in`, and update or create with assignment. Keys are case-sensitive."

---

## Speaker Notes: Scope Guardrails

**Teach in this hour:**
- Dictionary literal creation with curly braces and colons
- Reading values with `dict[key]` and the `KeyError` it raises when key is missing
- Safe reading with `dict.get(key, default)`
- Checking key existence with `in`
- Updating an existing entry via assignment
- Adding a new entry via assignment
- Incrementing a value with `+=`
- Input normalization with `.strip().lower()`
- Brief use of `dict.items()` in a loop (full coverage in Hour 20)
- `dict.keys()` for displaying available keys

**Do NOT introduce in this hour:**
- `collections.defaultdict` (out of scope — Advanced)
- `collections.Counter` (out of scope — Advanced)
- Dict comprehensions (out of scope — Basics generally avoids comprehensions)
- `dict.setdefault()` (too advanced; `get()` is sufficient for Basics)
- `dict.update()` with another dict (not needed for this lab)
- `dict.pop()` and `dict.popitem()` (not needed for this lab)
- Nested dictionaries (save for Session 6 or later when learners have more confidence)
- `dict.copy()` (not needed for Basics at this stage)
- Sorting a dict by values (the lambda extension is optional; do not require it)

Keep the conceptual message simple: **dictionaries map keys to values. Read safely with `get()`, check with `in`, update or create with assignment.**
