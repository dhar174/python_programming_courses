# Day 5, Hour 3: Dictionaries Fundamentals (Course Hour 19)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 19 – Dictionaries fundamentals  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 19. The entire hour focuses on Python dictionaries: what they are, how key-value thinking works, how to create and manipulate them, and — critically — how to access them safely using `get()` rather than crashing with a `KeyError`. Stay firmly within Basics scope: do not introduce dict comprehensions, `collections.defaultdict`, or nested dictionaries beyond a passing mention. The two key outcomes are (1) creating, reading, adding, and updating a dictionary by key, and (2) always using `get()` or an `in`-check before accessing a key that might be missing. The live demo types an inventory dictionary from scratch and deliberately triggers a `KeyError` to make the contrast with `get()` vivid and memorable. The guided lab turns learners loose to build their own interactive inventory manager. Every "Say:" block is written to be read nearly verbatim; adapt phrasing to your natural voice as needed, but do not skip the conceptual explanations — they are load-bearing.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Create a dictionary using curly-brace literal syntax and the `dict()` constructor, and explain in plain language what makes a dictionary different from a list, tuple, or set.
2. Access individual values by their key using bracket notation, and explain clearly why Python raises a `KeyError` when a key does not exist.
3. Add new entries and update existing entries in a dictionary using the same assignment syntax, and use an `in`-check to decide which action is appropriate.
4. Access dictionary values safely using `get(key)` and `get(key, default)`, and choose confidently between bracket access and `get()` depending on whether a missing key is expected or an error.
5. Build the Inventory Manager program: create a dictionary of five items with quantities, ask the user for an item name and a quantity to add, update the correct key safely, and print the full inventory — without crashing on a missing key."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 18 (sets); introduce the key-value problem that dictionaries solve
- **0:05–0:14** Core concept: what a dictionary is, real-world analogy, literal syntax, reading values by key
- **0:14–0:22** Adding and updating entries: assignment syntax, `in`-check, what happens when a key already exists
- **0:22–0:29** Safe access with `get()`: `get(key)`, `get(key, default)`, side-by-side comparison with bracket notation
- **0:29–0:33** Removing entries: `del`, `pop()`, `clear()`
- **0:33–0:38** Keys must be unique and hashable: duplicate key rule, valid key types, what cannot be a key
- **0:38–0:43** Live demo: Inventory Dictionary — typed live, showing `KeyError` vs `get()`, updating quantities, adding items
- **0:43–0:58** Guided lab: Inventory Manager
- **0:58–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open two clean files before class: `hour19_dict_demo.py` for the live demo, and `hour19_lab_inventory.py` with blank comment placeholders as a starter for learners.
- Have a Python REPL terminal open alongside your editor — you will drop into it for quick one-liner experiments in Sections 4 and 5.
- Plan to **deliberately crash the program** with a `KeyError` during the demo — this is intentional and pedagogically essential. Warn learners that you are doing it on purpose.
- Confirm learners have completed Hour 18 (sets) and are comfortable with the concept of collection types in Python. This hour builds directly on that understanding.
- Have a whiteboard or screen annotation tool ready for Section 4 to sketch the key → value arrow diagram.
- Prepare three short interactive questions to ask during the concept walkthrough; they are marked with **[Ask learners]** throughout this script.

**Say:** "Open your editor, create a fresh file called `hour19_dict_demo.py`, and get your terminal ready alongside it. Dictionaries are one of the most important data structures in all of Python — almost every real program uses them. This hour is going to feel very relevant very quickly."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 18

**Say:**
"Last hour we explored sets. We found out that a set is an unordered collection of *unique* values — no duplicates ever, and membership checks with `in` are extremely fast. Sets are brilliant for the 'have I seen this before?' problem. We built a Unique Visitors program and saw how converting a list to a set instantly strips all the duplicates.

So at this point in the course, we have four collection types under our belt: lists, which are ordered and mutable; tuples, which are ordered and immutable; sets, which are unordered and store only unique values; and today — dictionaries, which are the most powerful and flexible of the four for many common real-world tasks.

Take thirty seconds: remind your neighbour — or remind yourself if you're working solo — what you remember about sets. What makes them special? What would you use one for? … Great. Hold that thought and let's bridge into today."

### 3.2 The limitation that motivates dictionaries

**Say:**
"Here is a question. Suppose I give you a list like this:"

```python
items = ["apples", "bananas", "oranges", "pears", "grapes"]
quantities = [12, 5, 8, 3, 20]
```

**Say:**
"I have my five fruits in one list and their quantities in another. This works, but it is fragile. How many apples do I have? I have to know that 'apples' is at index 0, and then look up `quantities[0]`. If I accidentally sort one list but not the other, my data is corrupted. If I insert a new fruit in the middle of `items`, I have to remember to insert the matching quantity at the exact same position in `quantities`.

This is a common beginner pattern, and it breaks. There has to be a better way to say: 'apples goes with 12, bananas goes with 5, oranges goes with 8'. And there is. It is called a dictionary."

**[Transition]** "Let us learn what a dictionary is."

---

## 4) Concept: What Is a Dictionary?

### 4.1 The real-world analogy

**Say:**
"The name 'dictionary' is a great clue. Think of an actual physical dictionary — a book where every word has a definition. If I want to know what 'ephemeral' means, I do not read the entire dictionary from page one. I flip straight to the 'E' section and look up 'ephemeral'. The *word* is the **key** and the *definition* is the **value**. The dictionary gives me a direct path from one piece of information to another.

Python's `dict` works exactly the same way. You store pairs of information: a key and its associated value. You use the key to look up the value instantly — no looping, no index arithmetic, no searching."

**Draw on whiteboard (or annotate on screen):**
```
KEY          →   VALUE
"apples"     →   12
"bananas"    →   5
"oranges"    →   8
"pears"      →   3
"grapes"     →   20
```

**Say:**
"Here is another analogy if the dictionary one does not click: think of a contacts app on your phone. You search for 'Maria' — that is the key. The app instantly shows you Maria's phone number — that is the value. You do not scroll through every contact alphabetically; you type the name and get the number. That is exactly what a Python dictionary does.

Or think of a locker system at a gym. Each locker has a number on it — that is the key. Inside each locker is somebody's bag — that is the value. The locker number gives you direct access to the contents. Different lockers, different keys, different contents."

**[Ask learners]** "Before I show you any code, can someone give me another real-world example of a key-value relationship? Something where you look up one thing to find another?"

*(Accept answers: student ID → grade, username → password hash, zip code → city name, book title → author, etc. Briefly acknowledge each one and confirm it fits the key → value pattern.)*

### 4.2 The key-value mental model

**Say:**
"Here is the core mental model: a dictionary is a *mapping*. It maps each key to exactly one value. The keys form a set — they must be unique. The values can be anything, and they can repeat. Every entry in a dictionary is a key-value *pair*.

In Python's documentation and in most teaching, you will also see the word 'item' used to mean a single key-value pair. When I say 'an item in the dictionary', I mean one key together with its value."

### 4.3 Creating a dictionary with literal syntax

**Say:**
"Let us write this in code. The syntax for a dictionary literal uses curly braces — just like a set. But unlike a set, which is just a list of values, a dictionary contains *pairs* connected by a colon. The key is on the left of the colon, and the value is on the right. Pairs are separated by commas."

Type in the REPL or demo file:

```python
# Dictionary literal: {key: value, key: value, ...}
inventory: dict[str, int] = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}

print(inventory)
```

**Say:**
"Notice the type hint I wrote: `dict[str, int]`. This tells anyone reading the code — including you six months from now — that the keys are strings and the values are integers. You do not have to write type hints, but they are a helpful habit and they make code more readable. Let us run this and see what prints."

*(Run it.)*

**Say:**
"Python prints the dictionary back to us, curly braces and all, with the colon notation. You can already see the structure clearly. The order Python prints them in is the *insertion order* — since Python 3.7, dictionaries remember the order you added entries. That is a nice guarantee to have."

**[Ask learners]** "What is the difference between what we just wrote and a set? A set also uses curly braces. How are they different?"

*(Listen for: a set has individual values separated by commas; a dictionary has key-colon-value pairs. Confirm and reinforce.)*

### 4.4 Reading a value by its key

**Say:**
"To get a value back out of the dictionary, you use square bracket notation — the same square brackets you use to index a list. But instead of a number, you put the key inside."

Type in the REPL:

```python
print(inventory["apples"])   # 12
print(inventory["grapes"])   # 20
```

**Say:**
"Python looks up the key 'apples', finds it in the dictionary, and gives back its value, 12. This is called *key lookup* or *subscript access*. It is very fast — Python does not scan through the whole dictionary; it uses the key directly, much like how the locker number takes you straight to the right locker.

Now — what happens if the key does not exist? Let me try something intentional."

```python
print(inventory["mangoes"])   # 🔴 KeyError!
```

**Say:**
"Python raises a `KeyError`. It is telling us: 'I looked everywhere in this dictionary, and there is no key called mangoes.' The program crashes. This is the most common dictionary error beginners encounter, and we will spend real time today learning how to avoid it properly. Keep that error message in mind — we will come back to it in Section 7."

---

## 5) Creating and Reading Dictionaries

### 5.1 Alternative: the `dict()` constructor

**Say:**
"There is a second way to create a dictionary: the `dict()` built-in constructor. You pass keyword arguments where the keyword becomes the string key and the value becomes the value."

Type in REPL:

```python
# Using the dict() constructor
scores: dict[str, int] = dict(alice=95, bob=87, carol=91)
print(scores)
# {'alice': 95, 'bob': 87, 'carol': 91}
```

**Say:**
"This style is clean and readable for small dictionaries, but it only works when your keys are valid Python identifiers — simple names without spaces or special characters. If your keys are more complex, like 'item code' with a space, you must use the curly-brace literal. For this course, the literal form is the standard — use it by default."

### 5.2 Creating an empty dictionary

**Say:**
"You will often want to start with an empty dictionary and add things to it dynamically. There are two equivalent ways:"

```python
# These two are identical
empty_a: dict[str, int] = {}
empty_b: dict[str, int] = dict()

print(type(empty_a))   # <class 'dict'>
print(type(empty_b))   # <class 'dict'>
```

**Say:**
"Important warning: remember that an empty set uses `set()`, not `{}`. An empty pair of curly braces always means an empty *dictionary*, not an empty set. This catches many beginners. If you want an empty set, you must write `set()`. If you want an empty dictionary, write `{}` or `dict()`. Write that difference down somewhere visible."

### 5.3 Checking the length

**Say:**
"The `len()` function works on dictionaries just as it does on lists. It tells you how many key-value pairs are in the dictionary."

```python
print(len(inventory))   # 5
```

---

## 6) Adding and Updating Entries

### 6.1 Adding a new entry

**Say:**
"Here is the beautiful simplicity of dictionaries: adding a new entry and updating an existing entry use *exactly the same syntax*. You write `dictionary[key] = value`. If the key does not already exist, Python creates it. If it does already exist, Python overwrites the old value with the new one."

Type and run:

```python
# Adding a brand-new key
inventory["mangoes"] = 7
print(inventory)
# {'apples': 12, 'bananas': 5, ..., 'mangoes': 7}
```

**Say:**
"Mangoes did not exist before. Python created a new entry for it with value 7. Now it is in the dictionary. Let us check the length."

```python
print(len(inventory))   # 6
```

### 6.2 Updating an existing entry

**Say:**
"Now suppose we get a delivery of 10 more apples. We currently have 12. We want to update the count to 22."

```python
# Updating an existing key
inventory["apples"] = 22
print(inventory["apples"])   # 22
```

**Say:**
"Python found the key 'apples', it already existed, and it replaced 12 with 22. The dictionary now has 22 apples. The old value is gone — dictionaries do not keep history. There is still only one entry for 'apples'."

### 6.3 The `in` operator for dictionaries

**Say:**
"The `in` operator works with dictionaries, and by default it checks *keys* — not values. So `'apples' in inventory` asks: 'Is there a key called apples in this dictionary?' The answer is True or False."

```python
print("apples" in inventory)    # True
print("mangoes" in inventory)   # True  (we just added it!)
print("durians" in inventory)   # False

# Not-in also works
print("durians" not in inventory)  # True
```

**Say:**
"This is extremely useful for safe access. Before you look something up, you can check whether the key exists. Like this:"

```python
item_to_check: str = "pears"

if item_to_check in inventory:
    print(f"{item_to_check}: {inventory[item_to_check]} in stock")
else:
    print(f"{item_to_check} is not in our inventory")
```

**Say:**
"The `in`-check followed by bracket access is safe — you only do the bracket lookup *after* confirming the key exists. This pattern is perfectly correct. However, there is an even more elegant built-in tool designed exactly for this situation, and that is `get()`. We will meet it in the next section."

### 6.4 Common trap: the accidental new key

**Say:**
"Here is a pitfall I want you to see right now, because it will happen to you eventually. If you make a typo in a key name when *assigning*, Python does not raise an error — it silently creates a *new* entry with the misspelled name."

```python
# Oops: typo creates an unwanted new key
inventory["applez"] = 999   # Note the 'z'
print(len(inventory))       # Now 7, not 6!
print("apples" in inventory)   # True  (original is fine)
print("applez" in inventory)   # True  (whoops, we made a ghost entry)
```

**Say:**
"This can cause subtle bugs. Your apple count looks fine but you have a phantom 'applez' entry floating around. The fix is careful typing, and later in the optional extension section we will look at normalizing keys to lowercase to reduce some of this class of problem. For now: type your keys carefully and always test with a print to confirm what you expect."

---

## 7) Safe Access with `get()`

### 7.1 The problem `get()` solves

**Say:**
"Let us revisit the `KeyError` crash from earlier. When we wrote `inventory['mangoes']` and mangoes was not in the dictionary, Python blew up. That is the correct behaviour for Python: failing loudly is better than silently returning a wrong answer. But there are many situations where a missing key is *expected* — it is not a bug, it is just a normal part of the data. In those cases, a crash is unhelpful.

Think about the lab we are about to do: the user types a fruit name, and we look it up. The user might type a fruit that is not in the inventory. We do not want to crash. We want to handle it gracefully. That is exactly what `get()` is designed for."

### 7.2 `get(key)` — returns `None` by default

**Say:**
"The `get()` method takes a key as its argument and returns the corresponding value if the key exists. If the key does not exist, instead of raising a `KeyError`, it returns `None`. `None` is Python's way of saying 'no value here' — it is not a crash, it is a quiet, safe signal."

Type and run:

```python
# Safe lookup — no crash even if key is missing
result = inventory.get("apples")
print(result)       # 12  (key exists)

result = inventory.get("durians")
print(result)       # None  (key does not exist, no crash)
```

**Say:**
"The program does not crash. It returns `None`. We can test for that:"

```python
item: str = "durians"
result = inventory.get(item)

if result is None:
    print(f"'{item}' is not in our inventory.")
else:
    print(f"We have {result} {item} in stock.")
```

**Say:**
"This is safe, readable, and very Pythonic. Notice I wrote `result is None` rather than `result == None` — that is the recommended style in Python for checking against `None` specifically."

### 7.3 `get(key, default)` — return your own fallback value

**Say:**
"Even better: `get()` accepts a second optional argument — a *default value* to return when the key is missing. Instead of returning `None`, it returns whatever you specify."

```python
# get() with a default value
apples_count = inventory.get("apples", 0)
print(apples_count)   # 12  (key exists, default is ignored)

durians_count = inventory.get("durians", 0)
print(durians_count)  # 0   (key missing, returns the default 0)
```

**Say:**
"This pattern is incredibly useful. The default 0 says: 'if we do not have this item, pretend we have zero of it.' For an inventory system where missing means zero stock, this is exactly right. You can use any default value: a string, a list, a boolean — whatever makes sense in context."

### 7.4 Side-by-side comparison

**Say:**
"Let me put the three access patterns side by side so you can see the trade-offs clearly."

```python
# Pattern 1: Bracket access — fast and direct, but crashes if key is missing
# Use when you are CERTAIN the key exists
quantity = inventory["apples"]

# Pattern 2: in-check then bracket — explicit, readable, two lines
# Use when you need to branch on existence anyway
if "apples" in inventory:
    quantity = inventory["apples"]

# Pattern 3: get() — concise, safe, Pythonic
# Use when a missing key is a normal/expected case
quantity = inventory.get("apples", 0)
```

**[Ask learners]** "When would you choose pattern 1 over pattern 3? … When would pattern 3 be the wrong choice?"

*(Listen for: pattern 1 is appropriate when you are truly certain the key exists and a missing key would be a genuine programming bug — you *want* the crash because it signals something is broken. Pattern 3 is appropriate when the user input might not match, when data might be incomplete, etc. Confirm and synthesize.)*

**Say:**
"There is no single right answer for every situation, but as a beginner default: when in doubt, use `get()` with a sensible default. It is almost always safer."

---

## 8) Removing Entries

**Say:**
"Sometimes you need to remove a key-value pair from a dictionary. Python gives you three tools for this."

### 8.1 `del` — direct deletion

```python
# del removes the key entirely
print("pears" in inventory)   # True
del inventory["pears"]
print("pears" in inventory)   # False
print(len(inventory))         # one fewer entry
```

**Say:**
"If you `del` a key that does not exist, Python raises a `KeyError` — same as bracket access. So only use `del` when you are sure the key is there, or wrap it in an `if key in dict` check first."

### 8.2 `pop()` — remove and return

```python
# pop() removes the key AND returns its value
removed_value = inventory.pop("bananas")
print(f"Removed bananas, they had quantity: {removed_value}")

# pop() with a default avoids KeyError for missing keys
missing = inventory.pop("durians", 0)
print(f"Removed durians: {missing}")   # 0, no crash
```

**Say:**
"`pop()` is like `get()` in that it accepts a default. When you need to both remove an entry *and* do something with its value, `pop()` is the right tool."

### 8.3 `clear()` — empty the entire dictionary

```python
# clear() removes ALL entries — use carefully!
temp_dict: dict[str, int] = {"a": 1, "b": 2}
temp_dict.clear()
print(temp_dict)   # {}
print(len(temp_dict))  # 0
```

**Say:**
"You will not need `clear()` often, but it exists. It is the nuclear option: wipes the entire dictionary in one call. The dictionary object itself still exists — it is just empty."

---

## 9) Key Concepts: Keys Must Be Unique and Hashable

### 9.1 What happens when you assign the same key twice

**Say:**
"Dictionary keys must be unique. There is no such thing as two entries with the same key. If you try to create a dictionary literal with a duplicate key, Python does not raise an error — the *last* value wins silently."

```python
# Duplicate key in a literal — last value wins
prices: dict[str, float] = {
    "apple": 1.20,
    "banana": 0.50,
    "apple": 2.50,   # duplicate!
}
print(prices)
# {'apple': 2.50, 'banana': 0.50}
# The 1.20 is gone. No error was raised.
```

**Say:**
"This is a footgun. Python does not warn you. The first apple price was silently discarded. The lesson: if you are building a dictionary literal by hand and something seems off, check for duplicate keys. Good editors and linters will flag this, but you should develop the habit of spotting it yourself."

### 9.2 What types can be keys

**Say:**
"Keys must be *hashable*. Without going deep into the theory: hashable means Python can compute a fixed fingerprint — a hash — for the value, and that fingerprint does not change over time. Any *immutable* built-in type is hashable and therefore usable as a key."

Valid key types:

```python
# Strings — the most common key type
d: dict = {"name": "Alice"}

# Integers — very common for ID-like keys
d[42] = "the answer"

# Floats — valid, but unusual and risky due to floating-point precision
d[3.14] = "pi"

# Booleans — valid (True and False are ints internally: 1 and 0)
d[True] = "yes"

# Tuples — valid IF all elements inside are also hashable
d[(1, 2)] = "coordinate"

print(d)
```

**Say:**
"Now, what cannot be a key?"

```python
# Lists CANNOT be keys — they are mutable (unhashable)
bad_dict = {[1, 2, 3]: "a list key"}   # 🔴 TypeError: unhashable type: 'list'
```

**Say:**
"Python raises a `TypeError` immediately. Lists are mutable — they can change — so Python cannot compute a stable hash for them. Sets also cannot be keys for the same reason. If you need a tuple-like key, use a tuple, not a list.

For this course, your keys will almost always be strings. Integer keys come up in some patterns. That is all you need to remember for now: string and integer keys — always safe."

---

## 10) Live Demo: Inventory Dictionary

*[Open `hour19_dict_demo.py` in your editor and type everything below live — do not paste it. Narrate every line as you type.]*

**Say:**
"Let us put everything together in one flowing demo. I am going to build an inventory dictionary from scratch, demonstrate the `KeyError` deliberately, and then show you the safe `get()` solution. Type along with me."

### Step 1 — Create the inventory

```python
# hour19_dict_demo.py
# Live Demo: Inventory Dictionary

# Step 1: Create the inventory with 5 items
inventory: dict[str, int] = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}

print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")
```

**Say:**
"I'm using `inventory.items()` inside a `for` loop — this gives me each key-value pair as a tuple that I unpack into `item` and `qty`. We will go much deeper into dictionary iteration next hour; for now just know this is the standard way to print all contents. Run it and confirm we see all five items."

*(Run it, confirm output.)*

### Step 2 — Demonstrate `KeyError`

```python
# Step 2: Try to access a missing key — THIS WILL CRASH (on purpose!)
print("\n--- Attempting to access 'mangoes' ---")
print(inventory["mangoes"])   # 🔴 KeyError: 'mangoes'
```

**Say:**
"I am running this *knowing* it will crash. Watch the error message carefully."

*(Run it. Let the traceback appear on screen.)*

**Say:**
"There it is: `KeyError: 'mangoes'`. Python is telling us exactly what went wrong — we tried to look up a key that does not exist. The program stopped dead. In a real application, this kind of unhandled crash would be a serious bug. Let us fix it with `get()`."

### Step 3 — Fix with `get()`

```python
# Step 3: Safe access with get()
print("\n--- Safe access with get() ---")

# get() returns None if key is missing
result = inventory.get("mangoes")
print(f"get('mangoes') → {result}")   # None — no crash!

# get() with a default value of 0
count = inventory.get("mangoes", 0)
print(f"get('mangoes', 0) → {count}")  # 0

# get() with a key that DOES exist — returns the real value
count = inventory.get("apples", 0)
print(f"get('apples', 0) → {count}")   # 12
```

*(Run it.)*

**Say:**
"No crash. `get()` returns 0 for a missing key. And when the key does exist, it returns the real value, 12 — the default is ignored. This is exactly the behaviour we want in the lab."

### Step 4 — Update and add entries

```python
# Step 4: Updating existing entry and adding a new one
print("\n--- Updating inventory ---")

# Delivery arrived: 10 more apples
inventory["apples"] += 10     # same as: inventory["apples"] = inventory["apples"] + 10
print(f"After delivery — apples: {inventory['apples']}")   # 22

# New item arrives
inventory["mangoes"] = 7
print(f"New item added — mangoes: {inventory['mangoes']}")  # 7

print(f"\nInventory now has {len(inventory)} items.")
```

**Say:**
"Notice `inventory['apples'] += 10` — this is the compound assignment operator working on a dictionary value. It reads the current value, adds 10, and writes it back. This is a very common pattern for counters and quantity tracking."

### Step 5 — Check existence before deciding

```python
# Step 5: Using 'in' to decide whether to update or add
print("\n--- Smart update using 'in' check ---")

new_items: dict[str, int] = {"bananas": 8, "kiwis": 15, "oranges": 4}

for item, qty in new_items.items():
    if item in inventory:
        inventory[item] += qty
        print(f"Updated '{item}' → now {inventory[item]}")
    else:
        inventory[item] = qty
        print(f"Added new item '{item}' → {qty}")

print("\n=== Final Inventory ===")
for item, qty in inventory.items():
    print(f"  {item}: {qty}")
```

*(Run the complete file.)*

**Say:**
"Beautiful. We loop through a dictionary of incoming stock, check whether each item already exists, update if it does, and add it fresh if it does not. The complete inventory is printed at the end. This is a realistic pattern — think of a warehouse system receiving a shipment file. Now you build something similar yourself."

---

## 11) Hands-on Lab: Inventory Manager

### 11.1 Lab introduction

**Say:**
"You have seen me build this — now it is your turn. Open `hour19_lab_inventory.py` and build the program step by step. I will give you the spec, then starter hints, then we will walk through the solution together at the end."

### 11.2 Lab specification

**Goal:** Build an interactive inventory manager.

**Requirements:**
1. Create a dictionary called `inventory` with exactly 5 items and their quantities. Use items you choose — fruits, office supplies, game items, anything you like.
2. Print the inventory neatly at the start, labelled "Current Inventory".
3. Ask the user to type an item name.
4. Ask the user how many units to add (as an integer).
5. If the item exists in the inventory, increase its quantity by the entered amount.
6. If the item does not exist, tell the user it was not found — do **not** crash, and do **not** silently create a new key.
7. Print the final inventory, labelled "Updated Inventory".

**Completion criteria:**
- The correct key is updated.
- The program does not crash on a missing key.
- `get()` or an `in`-check is used (not bare bracket access for the user-supplied key).
- The output is readable and labelled.

**Constraints:**
- No imports needed.
- No loops (yet) — a single input/update cycle is enough.
- Keep it simple and correct.

### 11.3 Starter hints

*Share these on screen:*

```python
# hour19_lab_inventory.py
# Inventory Manager — Lab Starter

# 1. Create your inventory dictionary here
inventory: dict[str, int] = {
    # your items here
}

# 2. Print the starting inventory
print("=== Current Inventory ===")
# TODO: print each item and quantity

# 3. Ask the user for an item name and quantity to add
item_name: str = input("Enter item name: ")
add_qty: int = int(input("How many to add? "))

# 4. Check if the item exists, update or warn
# TODO: your logic here

# 5. Print the final inventory
print("\n=== Updated Inventory ===")
# TODO: print each item and quantity
```

**Say:**
"Work through each `TODO` comment in order. The trickiest part is step 4 — deciding how to check. You can use `get()` with a default or an `in`-check. Both are correct; pick whichever feels more natural to you right now.

You have fifteen minutes. I will circulate. If you finish early, try the extension tasks at the bottom of this script. Go."

*(Give 15 minutes of work time. Circulate, answer questions, nudge stuck learners with questions like: "What does `get()` return when the key is missing?" and "What would you need to check before adding to a quantity?" without giving away the answer.)*

### 11.4 Walkthrough solution

**Say:**
"Let us look at a clean solution together. As always, there are several correct approaches — I will show one that uses `get()` for the existence check. If yours looks a bit different but works correctly and does not crash, it is valid."

```python
# hour19_lab_inventory.py
# Inventory Manager — Full Solution

# 1. Create inventory
inventory: dict[str, int] = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}

# 2. Print starting inventory
print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4} units")

# 3. Get user input
item_name: str = input("\nEnter item name: ").strip()
add_qty: int = int(input("How many to add? "))

# 4. Update or warn
current_qty: int | None = inventory.get(item_name)

if current_qty is None:
    print(f"\n'{item_name}' is not in the inventory. No changes made.")
else:
    inventory[item_name] = current_qty + add_qty
    print(f"\nUpdated '{item_name}': {current_qty} → {inventory[item_name]}")

# 5. Print final inventory
print("\n=== Updated Inventory ===")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4} units")
```

**Say:**
"A few details worth noting in this solution:

First, I used `.strip()` on the user's input. This trims any accidental leading or trailing spaces the user might have typed. If the user types ' apples ' with spaces around it, the raw string would not match 'apples' in the dictionary — `.strip()` fixes that.

Second, in the `print` format strings I used `{item:<12}` and `{qty:>4}`. The `<12` means 'left-align in a field 12 characters wide'; the `>4` means 'right-align in a field 4 characters wide'. This lines up the columns so the output looks like a proper table. These are f-string format specifiers — a nice finishing touch that we covered earlier in the course.

Third, the `get()` call stores `None` in `current_qty` if the key is missing, and we check `is None` to decide which branch to take. If the key exists, `current_qty` is the integer value and we add to it directly.

**[Ask learners]** "What would happen if the user typed 'Apples' with a capital A? … Right — it would not match 'apples' in the dictionary. This is case sensitivity in action — one of our key pitfalls, which I want to discuss now."

### 11.5 Design discussion

**Say:**
"One thing this solution does not handle: what if the user types a negative number? Should we allow removing stock? What if they type something that is not a number at all and `int()` crashes?

These are real concerns in production code. For this lab, we are keeping it simple — we trust the user to enter a positive integer. But notice how quickly requirements grow. A real inventory system would need: input validation, the ability to subtract stock, a loop to handle multiple updates, saving to a file, and so on. The dictionary is just one piece of that system. Today we are building the foundation."

---

## 12) Common Pitfalls

**Say:**
"Let me walk through the most common mistakes I see learners make with dictionaries. Recognising these patterns will save you debugging time."

### 12.1 Case sensitivity

```python
inventory: dict[str, int] = {"apples": 12, "bananas": 5}

user_input: str = "Apples"   # Capital A

# This will NOT find the key
print(inventory.get(user_input, 0))   # 0 — not 12!

# Fix: normalize the input to lowercase
print(inventory.get(user_input.lower(), 0))   # 12 ✅
```

**Say:**
"Python strings are case-sensitive. `'Apples'` and `'apples'` are two completely different strings. If your keys are all lowercase, call `.lower()` on any user input before using it as a key. If you want to be consistent regardless of input, normalize everything to lowercase when you *store* it too. We will do this in the optional extension."

### 12.2 Typo creates a new key

```python
inventory: dict[str, int] = {"apples": 12}

# Typo: 'appels' instead of 'apples'
inventory["appels"] = 99   # Silent — no error!

print(inventory)
# {'apples': 12, 'appels': 99}  ← ghost key
```

**Say:**
"Python does not know the difference between a typo and an intentional new key. Both look the same to the interpreter. The only defence is careful typing and, in larger systems, having a defined set of valid keys that you check against. For now: print your dictionary frequently while developing so you spot unexpected keys early."

### 12.3 Confusing dict syntax with list syntax

```python
# A list uses integer indices
my_list: list[str] = ["a", "b", "c"]
print(my_list[0])   # "a"  — integer index

# A dict uses keys (usually strings)
my_dict: dict[str, int] = {"a": 1, "b": 2}
print(my_dict["a"])   # 1  — string key

# Common confusion: trying an integer on a string-keyed dict
print(my_dict[0])   # 🔴 KeyError: 0
```

**Say:**
"Both use square brackets, so beginners sometimes write `my_dict[0]` thinking it will return the first item. It does not — it looks for the *key* 0, which does not exist. Dictionaries are not indexed by position; they are indexed by key. If you want the first item, you need to know what key to ask for."

### 12.4 Bare bracket access on user-supplied keys

```python
item: str = input("Enter item: ")

# ❌ Dangerous: crashes if item is not in inventory
print(inventory[item])

# ✅ Safe: use get() with a default
print(inventory.get(item, "Not found"))
```

**Say:**
"Any time the key comes from outside your code — user input, a file, an API response — treat it as potentially missing. Bracket access is only safe when the key is a literal you typed yourself and you are absolutely certain it exists."

### 12.5 Forgetting that `{}` creates a dict, not a set

```python
mystery = {}
print(type(mystery))   # <class 'dict'>  ← NOT a set!

# To create an empty set:
empty_set = set()
print(type(empty_set))  # <class 'set'>
```

**Say:**
"This catches learners fresh from the sets lesson. Repeat after me: empty curly braces mean empty *dictionary*. An empty set needs `set()`."

---

## 13) Optional Extension: Lowercase + Sorted Print

**Say:**
"If you have finished the lab and want a challenge that stays entirely within Basics scope, here are two extensions. These are real quality-of-life improvements that make your program more robust."

### 13.1 Normalize input to lowercase

**Say:**
"The fix for case sensitivity is simple: call `.lower()` on the user's input before using it as a key. This way, 'Apples', 'APPLES', and 'apples' all resolve to the same key."

```python
# Extension 1: normalize user input
item_name: str = input("Enter item name: ").strip().lower()
```

**Say:**
"Now add a companion step: when you create the dictionary, also normalize all keys to lowercase. That way, the stored keys and the user's input are guaranteed to be in the same case. If your keys are already lowercase string literals, they are already normalized — nothing to change."

```python
# Storing with lowercase keys (already the case if you used lowercase literals)
inventory: dict[str, int] = {
    "apples": 12,   # ✅ already lowercase
    "Bananas": 5,   # ❌ would cause mismatch
}

# Better: normalize at creation time
raw_inventory: dict[str, int] = {"Apples": 12, "BANANAS": 5}
inventory: dict[str, int] = {}
for key, value in raw_inventory.items():
    inventory[key.lower()] = value
# {'apples': 12, 'bananas': 5}
```

**Say:**
"This version stays fully inside Basics scope. We start with an empty dictionary, loop through each key-value pair in `raw_inventory.items()`, lowercase the key, and store the same value under the normalized key. The result is a clean dictionary with predictable lowercase keys. If your literal keys are already lowercase, you do not need this extra step — but when data comes from mixed sources, this loop is a clear and reliable cleanup pattern."

### 13.2 Print inventory sorted by item name

**Say:**
"Dictionaries since Python 3.7 preserve insertion order, but insertion order is not always alphabetical. For a user-facing printout, alphabetical is friendlier. The `sorted()` function works on a dictionary's keys."

```python
# Extension 2: print inventory sorted alphabetically
print("\n=== Updated Inventory (sorted) ===")
for item in sorted(inventory):
    print(f"  {item:<12} {inventory[item]:>4} units")
```

**Say:**
"`sorted(inventory)` returns a sorted list of the dictionary's *keys*. We then use each key to look up the value via `inventory[item]`. This is one of the most common patterns for displaying dictionaries cleanly. The combination of lowercase normalization and sorted print makes your program feel professional."

---

## 14) Debrief, Recap, and Exit Ticket

### 14.1 Concept recap (read aloud)

**Say:**
"Let us consolidate everything we covered this hour. I am going to go through the key ideas. For each one, tell me in your head whether you feel confident, a bit shaky, or unsure — be honest with yourself."

"**One:** A dictionary is a collection of key-value pairs. Keys are unique; values can repeat. You look up a value by its key, not by its position."

"**Two:** You create a dictionary with curly brace literal syntax: `{'key': value, 'key': value}`. An empty dictionary is `{}` — remember, NOT an empty set."

"**Three:** Reading a value by key uses bracket notation: `d['key']`. If the key does not exist, Python raises a `KeyError` — the program crashes."

"**Four:** You add a new entry and update an existing entry with the same syntax: `d['key'] = value`. Python decides whether to create or overwrite based on whether the key already exists."

"**Five:** The `in` operator checks for key existence: `'key' in d` returns `True` or `False`. Use it before bracket access when you are not sure whether a key exists."

"**Six:** `get(key)` returns the value if the key exists, and `None` if it does not — no crash. `get(key, default)` returns your specified default instead of `None`. This is the safest way to access a dictionary when a missing key is a normal possibility."

"**Seven:** Dictionary keys must be hashable — strings and integers are always fine. Lists cannot be keys."

### 14.2 Vocabulary review

**Say:**
"Before we close, here are the key terms from today that you should know by name:
- **Dictionary** — a mapping of key-value pairs
- **Key** — the lookup identifier (must be unique and hashable)
- **Value** — the data associated with a key
- **Item** — a single key-value pair
- **KeyError** — the exception raised when you access a missing key with bracket notation
- **`get()`** — the safe access method that returns `None` (or a default) instead of raising `KeyError`"

### 14.3 Exit ticket

**Say:**
"I have one question for you — the exit ticket. Think about it for thirty seconds before answering."

> **Exit ticket question:** *What happens if you access a missing key with `dict[key]`? What is the alternative, and why would you choose it?*

**Say:**
"Take thirty seconds. Write your answer on paper, type it in a comment in your file, or just think it through clearly."

*(Pause 30 seconds.)*

**Say:**
"Here is the model answer: accessing a missing key with bracket notation raises a `KeyError`, which crashes the program. The alternative is `dict.get(key)` or `dict.get(key, default)`, which returns `None` or the specified default instead of crashing. You choose `get()` whenever the missing key is an expected possibility — for example, any time the key comes from user input or external data that you cannot guarantee is in the dictionary."

### 14.4 Bridge to Hour 20

**Say:**
"Next hour we are going to go deeper into dictionaries by learning how to iterate over them systematically — looping through keys, values, and key-value pairs — and we will explore the counting pattern, which is one of the most powerful and widely used dictionary techniques in all of Python. If you have ever wanted to count how many times each word appears in a text, or how many products fall into each category, that is exactly what we will build.

Before you leave: make sure your lab file runs correctly, handles a missing key gracefully, and prints the inventory in a readable format. If you have time, try the lowercase normalization extension — it will make Hour 20's work easier."

**Say:**
"Great work today. Dictionaries are one of those tools that once you learn, you find yourself reaching for constantly. The key-value mental model will serve you in every language, every framework, and every data-processing task you encounter. See you next hour."

---

## Appendix A: Full Demo File

*Complete reference for `hour19_dict_demo.py` — for instructor use only, not distributed to learners before the demo.*

```python
# hour19_dict_demo.py
# Live Demo: Inventory Dictionary — Course Hour 19

# ── Step 1: Create the inventory ─────────────────────────────────────────────
inventory: dict[str, int] = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}

print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4} units")

# ── Step 2: Trigger a KeyError (intentional) ──────────────────────────────────
print("\n--- Attempting to access 'mangoes' ---")
# Uncomment to demonstrate the crash:
# print(inventory["mangoes"])   # 🔴 KeyError: 'mangoes'

# ── Step 3: Safe access with get() ───────────────────────────────────────────
print("\n--- Safe access with get() ---")
result = inventory.get("mangoes")
print(f"get('mangoes')    → {result}")        # None

count = inventory.get("mangoes", 0)
print(f"get('mangoes', 0) → {count}")         # 0

count = inventory.get("apples", 0)
print(f"get('apples', 0)  → {count}")         # 12

# ── Step 4: Update and add entries ───────────────────────────────────────────
print("\n--- Updating inventory ---")
inventory["apples"] += 10
print(f"After delivery — apples: {inventory['apples']}")    # 22

inventory["mangoes"] = 7
print(f"New item added  — mangoes: {inventory['mangoes']}") # 7
print(f"Inventory now has {len(inventory)} items.")

# ── Step 5: Smart update using 'in' check ────────────────────────────────────
print("\n--- Smart update using 'in' check ---")
new_items: dict[str, int] = {"bananas": 8, "kiwis": 15, "oranges": 4}

for item, qty in new_items.items():
    if item in inventory:
        inventory[item] += qty
        print(f"Updated '{item}' → now {inventory[item]}")
    else:
        inventory[item] = qty
        print(f"Added new item '{item}' → {qty}")

print("\n=== Final Inventory ===")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4} units")
```

---

## Appendix B: Full Lab Solution File

*Complete reference for `hour19_lab_inventory.py`.*

```python
# hour19_lab_inventory.py
# Inventory Manager — Full Solution with Optional Extensions
# Course Hour 19: Dictionaries Fundamentals

# ── Setup ─────────────────────────────────────────────────────────────────────
inventory: dict[str, int] = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}

# ── Print starting inventory ─────────────────────────────────────────────────
print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4} units")

# ── Get user input ────────────────────────────────────────────────────────────
item_name: str = input("\nEnter item name: ").strip().lower()  # Extension: lowercase
add_qty: int = int(input("How many to add? "))

# ── Update or warn ────────────────────────────────────────────────────────────
current_qty: int | None = inventory.get(item_name)

if current_qty is None:
    print(f"\n'{item_name}' is not in the inventory. No changes made.")
else:
    inventory[item_name] = current_qty + add_qty
    print(f"\nUpdated '{item_name}': {current_qty} → {inventory[item_name]}")

# ── Print final inventory (Extension: sorted) ─────────────────────────────────
print("\n=== Updated Inventory ===")
for item in sorted(inventory):                  # Extension: alphabetical sort
    print(f"  {item:<12} {inventory[item]:>4} units")
```

---

## Appendix C: Quick Reference Card

*Print or share with learners as a take-away.*

| Operation | Syntax | Notes |
|---|---|---|
| Create dict | `d = {"a": 1, "b": 2}` | Curly braces, colon pairs |
| Empty dict | `d = {}` | NOT an empty set |
| Read value | `d["key"]` | `KeyError` if missing |
| Safe read | `d.get("key")` | Returns `None` if missing |
| Safe read + default | `d.get("key", 0)` | Returns `0` if missing |
| Add/update entry | `d["key"] = value` | Creates or overwrites |
| Increment value | `d["key"] += 1` | Read-add-write in one step |
| Check key exists | `"key" in d` | Returns `True` or `False` |
| Remove entry | `del d["key"]` | `KeyError` if missing |
| Remove + return | `d.pop("key", default)` | Safe with default |
| Count entries | `len(d)` | Number of key-value pairs |
| Loop all pairs | `for k, v in d.items():` | Both key and value |
| Sorted keys | `sorted(d)` | Returns a list of sorted keys |
