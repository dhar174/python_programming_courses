# Basics Day 5 — Session 5 (Hours 17–20)
Python Programming (Basic) • Tuples, Sets, and Dictionaries

## Session 5 Overview
- Hour 17: Tuples + unpacking
- Hour 18: Sets – uniqueness + membership
- Hour 19: Dictionaries fundamentals
- Hour 20: Dictionary iteration + counting pattern

---

# Hour 17: Tuples + Unpacking

## Learning Outcomes
- Create a tuple using parentheses and commas
- Explain immutability: why tuples cannot be changed after creation
- Unpack a tuple into individual variables
- Identify the single-item tuple gotcha: `(x,)` vs `(x)`
- Build a coordinate-tracker program storing 5 (x, y) points

---

## What Is a Tuple?

### Ordered, Immutable Sequence
```python
point = (3, 7)        # a tuple with two values
print(point)          # (3, 7)
print(point[0])       # 3
print(point[1])       # 7
```

### Key Properties
- **Ordered** — items have a fixed position
- **Immutable** — you cannot add, remove, or change items after creation
- **Allows duplicates** — same value can appear multiple times
- Written with parentheses `()` and commas

---

## Tuple vs List

| Feature | List | Tuple |
|---------|------|-------|
| Created with | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable? | ✅ Yes | ❌ No |
| Use when | Order changes | Fixed record |
| Example | Shopping cart | GPS coordinate |

### Why Use Tuples?
- Protect data from accidental changes
- Communicate intent: "this should not change"
- Common for returning multiple values from a function

---

## Creating Tuples

```python
# Basic tuple
colors = ("red", "green", "blue")

# Single-item tuple — MUST have trailing comma
one = (42,)        # ✅ tuple with one item
not_one = (42)     # ❌ just the number 42, not a tuple!

# Empty tuple
empty = ()

# Without parentheses (still works)
coords = 10, 20    # same as (10, 20)
```

---

## Immutability Demo

```python
point = (3, 7)

# Trying to change a tuple item → TypeError
point[0] = 99   # TypeError: 'tuple' object does not support item assignment

# Trying to append → AttributeError
point.append(5)  # AttributeError: 'tuple' object has no attribute 'append'
```

### Speaker Note
> Immutability is a feature, not a bug. When you see a tuple, you know it won't be modified anywhere in the program.

---

## Unpacking Tuples

```python
point = (3, 7)

# Unpack into named variables
x, y = point
print(x)   # 3
print(y)   # 7

# Swap two values elegantly
a = 10
b = 20
a, b = b, a
print(a, b)   # 20 10

# Unpack in a loop
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")
```

---

## Lab: Coordinate Tracker

### Instructions (30 minutes)

**Goal:** Store 5 (x, y) coordinate points as tuples in a list, display them, and find the min/max x values.

```python
# Starter structure
points = [
    (2, 5),
    (8, 1),
    (4, 9),
    (1, 3),
    (6, 7)
]

# Step 1: Print each point
# Step 2: Extract all x values
# Step 3: Find min and max x
```

**Completion Criteria:**
- Uses tuples (not lists) for each point
- Correctly prints all 5 points
- Produces the correct min and max x values

---

## Lab: Solution Walk-Through

```python
points = [(2, 5), (8, 1), (4, 9), (1, 3), (6, 7)]

# Print each point
print("All coordinates:")
for x, y in points:
    print(f"  ({x}, {y})")

# Extract x values and compute min/max
x_values = [x for x, y in points]
print(f"\nMin x: {min(x_values)}")   # 1
print(f"Max x: {max(x_values)}")    # 8
```

**Optional Extension:** Compute distance from origin: `import math; d = math.sqrt(x*x + y*y)`

---

## Common Pitfalls — Hour 17

### Pitfall 1: Single-item tuple missing comma
```python
one = (42)    # ❌ This is just the integer 42
one = (42,)   # ✅ This is a tuple containing 42
print(type((42)))    # <class 'int'>
print(type((42,)))   # <class 'tuple'>
```

### Pitfall 2: Trying to change a tuple
```python
location = (40.7128, -74.0060)
location[0] = 41.0    # TypeError — tuples are immutable
```

---

## Quick Check — Hour 17

**Exit Ticket Question:** Why might you choose a tuple over a list?

**Model Answer:** "A tuple is a good choice when the data is fixed and should not change — like a coordinate, a date (year, month, day), or a record with a set number of fields. Using a tuple signals to other programmers (and your future self) that this data is intentionally read-only."

**Recap:**
- Tuples: ordered, immutable, created with `(value, value)`
- Single-item needs trailing comma: `(value,)`
- Unpack with `x, y = point`
- Great for fixed records like coordinates, dates, or paired data

---

# Hour 18: Sets – Uniqueness + Membership

## Learning Outcomes
- Create a set from a list to remove duplicates
- Use `add()` to add items to a set
- Use `in` for fast membership testing
- Understand that sets are unordered (no indexing)
- Explain union and intersection conceptually

---

## What Is a Set?

### An Unordered Collection of Unique Items
```python
visitors = {"Alice", "Bob", "Charlie", "Alice", "Bob"}
print(visitors)     # {'Alice', 'Bob', 'Charlie'} — duplicates removed!
print(len(visitors))  # 3, not 5
```

### Key Properties
- **No duplicates** — automatically removes repeated values
- **Unordered** — no guaranteed position, no indexing
- **Fast membership test** — `in` is very efficient for sets
- Written with curly braces `{}` or `set()`

---

## Creating Sets

```python
# From a literal
fruits = {"apple", "banana", "cherry"}

# From a list (removes duplicates)
names_list = ["Alice", "Bob", "Alice", "Carol", "Bob"]
unique_names = set(names_list)
print(unique_names)    # {'Alice', 'Carol', 'Bob'} — order not guaranteed

# Empty set — MUST use set(), not {}
empty = set()     # ✅ empty set
not_empty = {}    # ❌ this creates an empty DICT, not a set!
```

---

## Set Operations

```python
visitors = {"Alice", "Bob", "Charlie"}

# Add an item
visitors.add("Diana")
print(visitors)     # has 4 items

# Membership test — very fast!
print("Alice" in visitors)    # True
print("Zara" in visitors)     # False

# Adding a duplicate changes nothing
visitors.add("Alice")
print(visitors)
```

---

## Conceptual: Union and Intersection

```python
group_a = {"Alice", "Bob", "Carol"}
group_b = {"Bob", "Carol", "Dave"}

# Union — everyone in either group
print(group_a | group_b)
# {'Alice', 'Bob', 'Carol', 'Dave'}

# Intersection — only those in both groups
print(group_a & group_b)
# {'Bob', 'Carol'}
```

### Speaker Note
> Keep this conceptual for now. The key idea: union = OR, intersection = AND. Real use cases: finding common attendees, filtering overlapping data.

---

## Lab: Unique Visitors

### Instructions (30 minutes)

**Goal:** Collect 10 visitor names (duplicates allowed), then use a set to find unique visitors.

```python
# Step 1: Collect names
names = []
for i in range(10):
    name = input(f"Enter visitor name {i+1}: ")
    names.append(name)

# Step 2: Convert to set for uniqueness
unique = set(names)

# Step 3: Report
print(f"\nTotal entries: {len(names)}")
print(f"Unique visitors: {len(unique)}")
print("Names:", sorted(unique))
```

**Completion Criteria:**
- Correct unique count
- Can explain why duplicates disappear

---

## Common Pitfalls — Hour 18

### Pitfall 1: Expecting order to be preserved
```python
tags = {"python", "basics", "beginner"}
# Do NOT write code that depends on a specific order
# tags[0]  ← TypeError: 'set' object is not subscriptable
for tag in tags:
    print(tag)   # order is not guaranteed
```

### Pitfall 2: Creating an empty set with `{}`
```python
my_set = {}        # ❌ This creates a dict!
my_set = set()     # ✅ This creates an empty set
```

### Pitfall 3: Forgetting `sorted()` for display
```python
# For consistent output in tests or display
print(sorted(my_set))   # convert to sorted list first
```

---

## Quick Check — Hour 18

**Exit Ticket Question:** When is a set better than a list?

**Model Answer:** "Use a set when you care about uniqueness — removing duplicates, or checking if something is present. Sets make `in` very fast. Use a list when order matters or you need to access items by position."

**Recap:**
- Sets store unique items only, duplicates auto-removed
- Created with `{value, value}` or `set(iterable)`
- Unordered: no indexing, no guaranteed print order
- `add()` to insert, `in` for membership, duplicates ignored automatically

---

# Hour 19: Dictionaries Fundamentals

## Learning Outcomes
- Create a dictionary with key/value pairs
- Access values by key
- Add and update entries
- Use `get()` to safely access a key that might not exist
- Avoid `KeyError` crashes in real programs

---

## What Is a Dictionary?

### A Lookup Table: Keys Map to Values
```python
inventory = {
    "apples":  10,
    "bananas": 5,
    "oranges": 8
}

print(inventory["apples"])    # 10
print(inventory["bananas"])   # 5
```

### Key Properties
- **Key–value pairs** — every item has a name (key) and data (value)
- **Keys must be unique** — no two items share the same key
- **Ordered** (Python 3.7+) — insertion order is preserved
- **Mutable** — you can add, update, and remove entries

---

## Creating Dictionaries

```python
# Basic dictionary
student = {
    "name": "Alice",
    "grade": 92,
    "passed": True
}

# Empty dictionary
empty = {}
also_empty = dict()

# Dictionary from keyword arguments
config = dict(host="localhost", port=8080)
```

---

## Accessing Values

```python
inventory = {"apples": 10, "bananas": 5}

# Direct access — KeyError if key missing
print(inventory["apples"])     # 10
print(inventory["grapes"])     # KeyError: 'grapes'

# Safe access with get() — returns None if missing
print(inventory.get("grapes"))           # None
print(inventory.get("grapes", 0))        # 0  (default value)

# Check before accessing
if "grapes" in inventory:
    print(inventory["grapes"])
```

---

## Adding and Updating Entries

```python
inventory = {"apples": 10, "bananas": 5}

# Add a new key
inventory["oranges"] = 8
print(inventory)   # {'apples': 10, 'bananas': 5, 'oranges': 8}

# Update an existing key
inventory["apples"] = 15
print(inventory["apples"])   # 15

# Increment a value
inventory["bananas"] += 3
print(inventory["bananas"])  # 8
```

---

## KeyError Demo

```python
inventory = {"apples": 10, "bananas": 5}

# This CRASHES
count = inventory["grapes"]   # KeyError: 'grapes'

# Safe alternatives
count = inventory.get("grapes", 0)      # returns 0 — no crash
count = inventory.get("grapes")         # returns None — no crash

if "grapes" in inventory:
    count = inventory["grapes"]
else:
    count = 0
```

### Speaker Note
> `get()` is your best friend for safe dictionary access. Teach learners to default to `get()` whenever the key might not exist.

---

## Lab: Inventory Manager

### Instructions (30 minutes)

**Goal:** Build a simple inventory system using a dictionary.

```python
# Step 1: Create inventory
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8,
    "grapes": 3,
    "pears": 6
}

# Step 2: Ask for item and quantity
item = input("Which item to restock? ").lower()
qty = int(input("How many to add? "))

# Step 3: Update safely
if item in inventory:
    inventory[item] += qty
    print(f"Updated {item}: {inventory[item]} units")
else:
    print(f"'{item}' not found in inventory.")

# Step 4: Print full inventory
print("\nCurrent Inventory:")
for key, value in inventory.items():
    print(f"  {key}: {value}")
```

**Completion Criteria:**
- Updates correct key without crashing on missing key
- Prints full inventory neatly

---

## Common Pitfalls — Hour 19

### Pitfall 1: Case sensitivity
```python
inventory = {"Apples": 10}
name = input("Item: ")         # user types "apples"
print(inventory[name])         # KeyError — "apples" ≠ "Apples"

# Fix: normalize keys once, then normalize the user input
inventory = {"apples": 10}
name = input("Item: ").lower()
print(inventory.get(name, 0))   # safe if key is missing
```

### Pitfall 2: Accidental new key
```python
inventory = {"apples": 10}
inventory["applez"] = 5    # typo creates a new key instead of updating!
```

### Pitfall 3: Direct access on unknown key
```python
# Always prefer get() when you're unsure
qty = inventory.get("grapes", 0)   # safe — returns 0 if missing
```

---

## Quick Check — Hour 19

**Exit Ticket Question:** What happens if you access a missing key with `dict[key]`?

**Model Answer:** "Python raises a `KeyError` and your program crashes. To avoid this, use `dict.get(key)` which returns `None` by default, or `dict.get(key, default_value)` to return a fallback instead of crashing."

**Recap:**
- Dict = key → value lookup table
- `dict[key]` = direct access (crashes if missing)
- `dict.get(key, default)` = safe access
- Add/update: `dict[key] = value`
- Check existence: `key in dict`

---

# Hour 20: Dictionary Iteration + Counting Pattern

## Learning Outcomes
- Iterate over dictionary keys, values, and items
- Use the `items()` method in a `for` loop
- Apply the counting pattern: `d[word] = d.get(word, 0) + 1`
- Build a word-frequency counter from user input

---

## Iterating Over Dictionaries

```python
scores = {"Alice": 92, "Bob": 87, "Carol": 95}

# Iterate over keys (default)
for name in scores:
    print(name)

# Iterate over values
for score in scores.values():
    print(score)

# Iterate over key-value pairs (most common)
for name, score in scores.items():
    print(f"{name}: {score}")
```

---

## The items() Method

```python
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# items() returns pairs of (key, value)
for item, count in inventory.items():
    print(f"{item.capitalize()}: {count} units")

# Output:
# Apples: 10 units
# Bananas: 5 units
# Oranges: 8 units
```

---

## The Counting Pattern

```python
# Core pattern: count occurrences of each item
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Build frequency dictionary
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
# {'apple': 3, 'banana': 2, 'cherry': 1}
```

### How It Works
1. `counts.get(word, 0)` — get current count, default 0 if first time seen
2. `+ 1` — increment by one
3. `counts[word] = ...` — store the updated count

---

## Word Frequency Demo

```python
sentence = "to be or not to be that is the question to be"
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display results sorted by word
print("Word Frequencies:")
for word in sorted(frequency):
    print(f"  '{word}': {frequency[word]}")
```

**Output:**
```
Word Frequencies:
  'be': 3
  'is': 1
  'not': 1
  'or': 1
  'question': 1
  'that': 1
  'the': 1
  'to': 3
```

---

## Lab: Word Counter

### Instructions (30 minutes)

**Goal:** Build a word-frequency counter that processes a sentence entered by the user.

```python
# Step 1: Get input
sentence = input("Enter a sentence: ")

# Step 2: Split into words
words = sentence.split()

# Step 3: Count frequencies
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Step 4: Display results
print("\nWord frequencies:")
for word in sorted(frequency):
    print(f"  {word}: {frequency[word]}")
```

**Completion Criteria:**
- Correct counts for all words
- Uses `get()` pattern (or equivalent `if`-check)

**Optional Extension:**
- Normalize to lowercase: `word = word.lower()`
- Strip punctuation: `word = word.replace(",", "").replace(".", "")`

---

## Common Pitfalls — Hour 20

### Pitfall 1: Forgetting to normalize case
```python
sentence = "The the THE"
# Without .lower():
# {'The': 1, 'the': 1, 'THE': 1}  ← wrong!

# With .lower():
words = sentence.lower().split()
# {'the': 3}  ← correct
```

### Pitfall 2: Punctuation counts as part of word
```python
sentence = "Hello, world."
words = sentence.split()
# ['Hello,', 'world.']  ← punctuation attached!

# Simple fix:
words = sentence.replace(",", "").replace(".", "").split()
```

### Pitfall 3: Accessing keys that weren't set
```python
counts = {}
# DON'T do this — KeyError on first occurrence:
# counts[word] += 1

# DO use get():
counts[word] = counts.get(word, 0) + 1
```

---

## Quick Check — Hour 20

**Exit Ticket Question:** What does `dict.items()` produce?

**Model Answer:** "`dict.items()` returns a view of the dictionary's key-value pairs as tuples. In a `for` loop, you can unpack each pair: `for key, value in dict.items()`. This is the standard way to iterate when you need both the key and its value at the same time."

**Recap:**
- `for k in d:` — keys only
- `for v in d.values():` — values only
- `for k, v in d.items():` — both key and value
- Counting pattern: `d[k] = d.get(k, 0) + 1`
- Always normalize (`.lower()`) and clean input before counting

---

## Session 5 Summary

### What We Covered

| Hour | Topic | Key Concept |
|------|-------|-------------|
| 17 | Tuples + Unpacking | Immutable sequences; `x, y = point` |
| 18 | Sets | Automatic uniqueness; unordered; fast `in` |
| 19 | Dictionaries | Key→value lookup; `get()` for safety |
| 20 | Dict Iteration | `items()` loop; counting pattern |

### The Big Picture
You now have four data structure tools:
- **List** — ordered, mutable, allows duplicates
- **Tuple** — ordered, immutable, fixed records
- **Set** — unordered, unique items, fast membership test
- **Dict** — key-value lookup, flexible, mutable

---

## Scope Guardrail Reminder

### Stay in Basics Scope — Session 5

✅ **Teach:**
- Tuple creation, immutability, unpacking
- Set creation, `add()`, `in`, and duplicate removal through conversion from a list
- Union (`|`) and intersection (`&`) — conceptually only
- Dict creation, `[]` access, `get()`, add/update entries
- `items()`, `keys()`, `values()` loops
- Counting pattern with `get(word, 0) + 1`

❌ **Do NOT introduce:**
- Named tuples (`collections.namedtuple`)
- Set comprehensions
- `defaultdict` or `Counter` (those are in the Advanced course)
- `OrderedDict` (unnecessary in Python 3.7+)
- Nested dictionaries deeper than one level
- Dictionary comprehensions (Advanced scope)
- File I/O or database concepts
- OOP or class definitions

> **Speaker note:** If a learner asks about `Counter` or `defaultdict`, acknowledge it's a great next step and point to the Advanced course.
