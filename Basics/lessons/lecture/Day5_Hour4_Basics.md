# Day 5, Hour 4: Dictionary Iteration + Counting Pattern (Course Hour 20)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 20 – Dictionary iteration + counting pattern  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 20 — the final hour of Session 5 and the capstone of our four-hour journey through Python's core data structures. Everything this hour builds directly on Hour 19 (dictionaries fundamentals). Learners already know how to create dictionaries, access values with bracket notation and `get()`, add and update entries, and remove keys. This hour adds the missing piece: *traversal*. We will walk through all three dictionary iteration methods — `keys()`, `values()`, and `items()` — and then develop the **counting pattern**, the single most practically useful dictionary idiom beginners will encounter. The word-frequency counter is the canonical demonstration of the counting pattern, and it is tangible enough that learners immediately see where it applies in real programs (log analysis, survey results, inventory tracking, analytics). Stay firmly within Basics scope: no `collections.Counter`, no `defaultdict`, no dictionary comprehensions. The goal is that every learner leaves this hour able to write a frequency counter from scratch and explain every line. The live demo is typed in front of the class — do not paste pre-written code. Every "Say:" block is written to be read nearly verbatim; adapt to your natural voice but do not skip the conceptual scaffolding — it is load-bearing.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Iterate through a dictionary's keys, values, and key-value pairs using `keys()`, `values()`, and `items()`, and choose the right method for the task at hand.
2. Explain in plain language what `dict.items()` returns and why unpacking `for key, value in d.items()` is more readable than alternatives.
3. Write a frequency-counting loop from scratch using the `d.get(word, 0) + 1` pattern, and explain step by step why this pattern handles both the 'first time we see a word' and the 'word already counted' cases in a single line.
4. Sort and display dictionary results using `sorted(d.items())`, print aligned output with f-strings, and identify the most-frequent item without any library imports.
5. Build a complete Word Counter program: read a sentence, split it into words, build a frequency dictionary, handle punctuation and capitalisation as optional extensions, and print a clean results table."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 19 (dicts fundamentals); introduce the iteration question
- **0:05–0:15** Dictionary iteration: `keys()`, `values()`, and `items()` — all three with examples and comparison
- **0:15–0:28** The counting pattern — three progressive builds: blank dict → manual `if`-branch → elegant `get()` one-liner
- **0:28–0:35** Sorting and displaying results — `sorted()`, aligned f-string output, finding the most common item
- **0:35–0:45** Live demo: Word Frequency Counter — typed live from blank file
- **0:45–0:57** Hands-on lab: Word Counter — guided with hints, full walkthrough solution
- **0:57–1:00** Session 5 wrap-up, forward look to Session 6, exit ticket

---

## 2) Instructor Setup Checklist

- Open two clean, blank files before class: `hour20_word_freq_demo.py` for the live demo and `hour20_lab_word_counter.py` as a guided starting shell for learners.
- Have a Python REPL terminal open alongside your editor — you will use it for quick interactive experiments in Sections 4 and 5.
- Prepare a short "starter sentence" of 12–15 words to type into the demo. Something concrete and slightly repetitive works best; for example: `"the quick brown fox jumps over the lazy dog and the fox"`. The repeated words make the counting effect immediately visible.
- This is the last instructional hour of Session 5. Plan a slightly longer debrief (3–5 minutes) to celebrate what learners have accomplished across all four hours today before the session ends.
- Confirm learners are comfortable with the `get()` method from Hour 19. If any learners missed Hour 19 or look uncertain, pair them with a neighbour during the lab — `get()` is the cornerstone of this hour.
- Have a whiteboard or screen annotation ready for Section 5 to draw the "before / after" state of a dictionary as each word is processed in the counting loop.

**Say:** "Open a fresh file called `hour20_word_freq_demo.py` and have your terminal ready. We are in the final hour of Day 5 and we are going to finish strong — because what we build today is one of the most genuinely useful patterns you will carry with you into every Python project you ever write."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 19

**Say:**
"Let's take a quick minute and make sure we are all standing on the same ground before we build on top of it. Last hour we met dictionaries. Who can remind me — in one sentence — what makes a dictionary different from a list?

…

Right. A list stores values in *order* and you access them by *position* — by index number. A dictionary stores values by *meaning* — by a key you choose. Instead of saying 'give me item at index 0', you say 'give me the value for this key'. That shift from position to meaning is what makes dictionaries so powerful.

We also learned the most important safety rule: never use bare bracket notation `d[key]` on a key you are not certain exists, because Python will raise a `KeyError` and your program will crash. Instead, use `d.get(key)` or `d.get(key, some_default)` — which returns `None` or your default silently if the key is not present.

Let's do a ten-second mental check: in your head, or by typing it out quickly — how do you create a dictionary with three entries? And how do you safely get the value for a key that might not be there? … Great. Hold all of that, because we are about to take dictionaries from *storage* to *action*."

### 3.2 The iteration gap

**Say:**
"Here is the gap we filled in Hour 19: we could *create* a dictionary, *read* from it, *update* it, and *safely access* it. But here is something we haven't asked yet: what do you do when you need to look at *every entry* in a dictionary — not just one specific key, but all of them?

Imagine you have a dictionary of fifty inventory items and their quantities. You want to print a full stock report. Or you have a dictionary of student names and scores and you want to find the highest scorer. Or — and this is where we are going today — you have a dictionary that is being *built up* as a program runs, one entry at a time, counting how many times each word appears in a text.

To do any of those things, you need to *iterate* through a dictionary. You need a for-loop that walks through every key, every value, or every key-value pair in turn. That is precisely what we are going to learn in the first part of this hour — and then we are going to use that knowledge to build something genuinely impressive."

---

## 4) Dictionary Iteration Methods

### 4.1 The three iteration views

**Say:**
"Python gives you three built-in methods for looking at a dictionary's contents in a loop. Think of them as three different *views* of the same data:

- `dict.keys()` — gives you just the keys
- `dict.values()` — gives you just the values
- `dict.items()` — gives you key-value pairs together

Let's look at each one. I'm going to type these in the REPL so you can see the output immediately."

Type in the REPL:

```python
inventory = {
    "apples": 12,
    "bananas": 5,
    "oranges": 8,
    "pears": 3,
    "grapes": 20,
}
```

**Say:** "There is our dictionary from Hour 19. Now let's iterate with each of the three methods."

### 4.2 Iterating over keys

**Say:** "First — `keys()`. When you use a plain `for` loop on a dictionary without calling any method, Python iterates over the keys by default. But calling `.keys()` explicitly makes the intent obvious. Both of these are equivalent:"

```python
# Implicit key iteration (works, but intent is hidden)
for item in inventory:
    print(item)

# Explicit key iteration (clearer)
for item in inventory.keys():
    print(item)
```

**Say:**
"Both loops print the same thing:

```
apples
bananas
oranges
pears
grapes
```

**[Ask learners]** When would iterating over just the keys be useful? Think of a real example.

… Good answers: printing a menu of available items, checking whether a key exists without caring about the value, building a sorted list of category names. If you only need the key, `keys()` is the right tool.

One style note: when you see experienced Python developers write `for k in d:` without calling `.keys()`, they are using the default-iterates-over-keys behaviour. Both styles are correct. In teaching code I will usually write `.keys()` explicitly so the intent is visible to you."

### 4.3 Iterating over values

**Say:** "Next — `values()`. Sometimes you genuinely do not care what the keys are. You just want to process all the values."

```python
# Sum all quantities without caring about which item they belong to
total = 0
for qty in inventory.values():
    total += qty

print(f"Total items in stock: {total}")
# Output: Total items in stock: 48
```

**Say:**
"That's clean and readable. We don't need the item names at all, so we don't ask for them.

**[Ask learners]** What other things might you do with just the values? … Find the average, the minimum, the maximum, collect them into a list for further analysis — yes, all of those are great use cases.

A common mistake is trying to call `.values()` when you actually need both the key and the value — for example, if you want to print 'apples: 12'. In that situation, `values()` is the wrong choice. You need `items()`, which we are coming to next."

### 4.4 Iterating over items — the workhorse

**Say:**
"The third method — `items()` — is the one you will use most often. It returns each entry as a *tuple* of `(key, value)`. And because we learned tuple unpacking in Hour 17, we can unpack that tuple right in the `for` loop header:"

```python
for item, qty in inventory.items():
    print(f"{item}: {qty}")
```

**Say:**
"Run that and you get:

```
apples: 12
bananas: 5
oranges: 8
pears: 3
grapes: 20
```

This is beautiful. The loop variable names `item` and `qty` are descriptive and chosen by you — they map directly onto the semantic meaning of your key and value. This is a pattern you will see in almost every real Python program that works with dictionaries.

Let me show you the same loop without the unpacking trick, so you can see why unpacking is the preferred style:"

```python
# Without unpacking — verbose and less readable
for pair in inventory.items():
    print(f"{pair[0]}: {pair[1]}")
```

**Say:**
"That works exactly the same way, but `pair[0]` and `pair[1]` are far less expressive than `item` and `qty`. The unpacking form is not just aesthetic — it makes your code self-documenting. Always prefer `for key, value in d.items()` when you need both sides of the pair."

### 4.5 Comparison: when to use which

**Say:**
"Let me put all three methods side by side as a decision guide you can refer back to:"

```python
inventory = {"apples": 12, "bananas": 5, "oranges": 8}

# Use .keys() when you only need the keys
print("Available items:")
for item in inventory.keys():
    print(f"  - {item}")

# Use .values() when you only need the values
total = sum(inventory.values())
print(f"Total stock: {total}")

# Use .items() when you need both — most common case
print("\nFull inventory:")
for item, qty in inventory.items():
    print(f"  {item:<12} {qty:>4}")
```

**Say:**
"Notice that last print. The `:<12` and `:>4` are *format specifiers* inside f-strings. `:<12` means 'left-align in a field 12 characters wide', and `:>4` means 'right-align in a field 4 characters wide'. This makes the output line up nicely in columns — we will use this again when we print the word frequency results.

Output:
```
Full inventory:
  apples        12
  bananas         5
  oranges         8
```

**[Ask learners]** What does `dict.items()` actually return? Can you describe it in one sentence?

… It returns a view of the dictionary as a sequence of `(key, value)` tuples. 'View' means it reflects the dictionary's current state — if you add or remove entries, the view updates automatically. For our purposes today, the important thing is: it gives you pairs you can unpack in a for-loop."

---

## 5) The Counting Pattern

### 5.1 The problem it solves

**Say:**
"Now we are going to build the counting pattern — and I want you to understand *why* it exists before we look at how it works.

Here is a concrete scenario. I give you a sentence:

```
'the quick brown fox jumps over the lazy dog and the fox'
```

I want to know how many times each word appears. 'the' appears three times. 'fox' appears twice. Everything else appears once.

How would you approach this? The natural data structure is a dictionary: the word is the key, and the count is the value. But here is the challenge — you cannot know in advance which words will appear. You have to *build* the dictionary as you go, word by word, and you have to handle two cases:

1. You see a word for the **first time** — it is not yet in the dictionary. You need to add it with a count of 1.
2. You see a word that is **already in the dictionary**. You need to increase its count by 1.

Your loop has to decide, every iteration, which case it is in. Let's build up to the most elegant solution step by step."

### 5.2 Step 1 — the manual if-branch approach

**Say:**
"The most literal translation of the two-case logic is a simple `if`-statement:"

```python
sentence = "the quick brown fox jumps over the lazy dog and the fox"
words = sentence.split()   # split on spaces → list of word strings

counts: dict[str, int] = {}   # start with an empty dictionary

for word in words:
    if word in counts:
        # Word already seen — increment
        counts[word] = counts[word] + 1
    else:
        # First time seeing this word — initialise to 1
        counts[word] = 1

print(counts)
```

**Say:**
"Let's trace through the first few iterations together. I will draw the state of the dictionary on the board as we go.

- `word = 'the'` → not in `counts` → `counts = {'the': 1}`
- `word = 'quick'` → not in `counts` → `counts = {'the': 1, 'quick': 1}`
- `word = 'brown'` → not in `counts` → `counts = {'the': 1, 'quick': 1, 'brown': 1}`
- (skip ahead…)
- `word = 'the'` again → IS in `counts` → `counts['the']` becomes `1 + 1 = 2`
- `word = 'the'` a third time → IS in `counts` → `counts['the']` becomes `2 + 1 = 3`

The output will be:

```python
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1,
 'over': 1, 'lazy': 1, 'dog': 1, 'and': 1}
```

This is **completely correct**. The `if word in counts` branch handles both cases perfectly. If you understand this version, you already understand the counting pattern conceptually. Keep it — it is not wrong.

But Python has a one-liner that eliminates the `if`/`else` entirely, and once you see how it works, you will use it every time."

### 5.3 Step 2 — introducing `get()` as the bridge

**Say:**
"Recall from Hour 19: `d.get(key, default)` returns the value for `key` if it exists, or returns `default` if it does not — without raising a `KeyError`.

Think about our two cases again:
- First time seeing 'the': `counts.get('the', 0)` → returns `0` (the default)
- Second time seeing 'the': `counts.get('the', 0)` → returns `1` (the stored value)

In *both* cases, the expression `counts.get(word, 0) + 1` gives us the right new value:
- First time: `0 + 1 = 1` ✓
- Second time: `1 + 1 = 2` ✓
- Third time: `2 + 1 = 3` ✓

So we can collapse the `if`/`else` into a single assignment:"

```python
counts[word] = counts.get(word, 0) + 1
```

**Say:**
"Read this line aloud with me: 'Set `counts[word]` equal to whatever is currently in `counts` for this word — defaulting to zero if it's not there yet — plus one.'

That's the whole pattern. It is one line, it handles both cases, and it is the standard Python idiom you will see in production code everywhere. Let's rewrite our counting loop using it:"

### 5.4 Step 3 — the complete elegant version

```python
sentence = "the quick brown fox jumps over the lazy dog and the fox"
words = sentence.split()

counts: dict[str, int] = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

**Say:**
"Four lines to build a complete word frequency counter. This is the counting pattern in its canonical form. Let me point out each piece:

1. `words = sentence.split()` — `str.split()` with no argument splits on any whitespace (spaces, tabs, newlines) and returns a list of strings.
2. `counts: dict[str, int] = {}` — we start with a completely empty dictionary. The type hint `dict[str, int]` is optional but communicates our intent: string keys, integer values.
3. `for word in words:` — iterate through every word in the list.
4. `counts[word] = counts.get(word, 0) + 1` — the counting idiom. 

**[Ask learners]** What is the value of `counts.get('elephant', 0)` in this program? And why?

… Zero — because 'elephant' is not a word in our sentence, so `get()` returns the default of 0. The dictionary does not get a new entry for 'elephant' from the `get()` call — `get()` only *reads*, it does not create. The new entry is only created if `elephant` actually appeared in the loop and we assigned `counts['elephant'] = 0 + 1`."

### 5.5 Side-by-side comparison: `if`-branch vs `get()` pattern

**Say:**
"Let me put both versions next to each other so you can decide which you prefer:"

```python
# Version 1: explicit if-branch (clear, verbose)
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

# Version 2: get() pattern (concise, idiomatic)
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

**Say:**
"Both versions produce identical output. Version 1 is perfectly fine and many beginners find it easier to read initially because the two cases are spelled out explicitly. Version 2 is what you'll see in professional Python code. The runbook for this course lists both as acceptable for the lab completion criteria — so you are free to use either.

My recommendation: understand Version 1 first so the logic is solid in your head, then adopt Version 2 once you feel confident. The `get()` pattern rewards you with fewer lines and fewer opportunities to introduce a typo."

---

## 6) Sorting and Displaying Results

### 6.1 Why sorting matters

**Say:**
"We now have a dictionary of word counts. But if we just `print(counts)`, the output is unsorted and potentially hard to read, especially for a large text. Let's look at how to produce useful, well-formatted output."

### 6.2 Sorting with `sorted(d.items())`

**Say:**
"We cannot sort a dictionary in place — dictionaries in Python 3.7+ maintain insertion order, but they don't have a sort method like lists do. Instead, we sort the *items* of the dictionary into a list of tuples, and then iterate over that sorted list.

`sorted(d.items())` returns a list of `(key, value)` tuples sorted by key alphabetically:"

```python
sentence = "the quick brown fox jumps over the lazy dog and the fox"
words = sentence.split()
counts: dict[str, int] = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Sort alphabetically by word (the key)
for word, count in sorted(counts.items()):
    print(f"{word}: {count}")
```

**Output:**
```
and: 1
brown: 1
dog: 1
fox: 2
jumps: 1
lazy: 1
over: 1
quick: 1
the: 3
```

**Say:**
"Clean and alphabetical. Notice that `sorted()` without any extra arguments sorts tuples by their first element — which is the key (the word). That gives us alphabetical order for free."

### 6.3 Sorting by count (descending)

**Say:**
"What if we want to sort by *frequency* — most common word first? We use the `key` parameter of `sorted()` with a small function. Don't worry about the `lambda` syntax right now — just read it as 'sort using the second element of each pair, in reverse':"

```python
# Sort by count, highest first
for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word}: {count}")
```

**Output:**
```
the: 3
fox: 2
quick: 1
brown: 1
jumps: 1
over: 1
lazy: 1
dog: 1
and: 1
```

**Say:**
"The most frequent word is at the top. If `lambda` looks mysterious right now, that is fine — we cover it properly in a later session. The pattern `key=lambda pair: pair[1]` simply means 'when comparing two pairs, use the second element — the count — as the sort key'. You can copy this pattern today without fully understanding every piece of it."

### 6.4 Printing aligned output

**Say:**
"For a professional-looking report, we can use f-string format specifiers to align the columns:"

```python
print(f"\n{'Word':<15} {'Count':>5}")
print("-" * 22)
for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word:<15} {count:>5}")
```

**Output:**
```
Word              Count
----------------------
the                   3
fox                   2
quick                 1
brown                 1
jumps                 1
over                  1
lazy                  1
dog                   1
and                   1
```

**Say:**
"The `:<15` format specifier left-aligns the word in a field 15 characters wide. The `:>5` right-aligns the count in a field 5 characters wide. Headers use the same specifiers so the columns line up perfectly. This is polish, not functionality — but learners who add this to their lab submission will have genuinely impressive output."

### 6.5 Finding the most common item

**Say:**
"One more useful trick: finding the single most common word. We can use `max()` with the same key trick:"

```python
most_common_word = max(counts, key=counts.get)
print(f"Most common word: '{most_common_word}' ({counts[most_common_word]} times)")
```

**Say:**
"`max(counts, key=counts.get)` iterates over the keys of `counts` and finds the one whose associated value is the largest. It uses `counts.get` — note: no parentheses, we are passing the method itself as a function — as the comparison key. The result is the key with the highest count.

This is an advanced-looking line that you can use without fully understanding its mechanics yet. File it away as a useful idiom: 'to find the key with the maximum value in a dictionary, use `max(d, key=d.get)`'."

---

## 7) Live Demo: Word Frequency Counter

### 7.1 Transition to the demo

**Say:**
"Everything we have covered in the last twenty minutes comes together right now. We are going to type a complete word frequency counter from scratch — no pasting, no shortcuts. I want you to type along with me so your muscle memory builds. If you fall behind, don't panic — keep watching, and I will pause after each logical block.

Open `hour20_word_freq_demo.py` if it isn't already open."

### 7.2 Full demo — type live

**Say:** "Let's start with the sentence and the basic counting loop. I will use `input()` so the user can provide their own text:"

```python
# hour20_word_freq_demo.py
# Word Frequency Counter — live demo

# Step 1: Get a sentence from the user
sentence: str = input("Enter a sentence: ")

# Step 2: Split into words
words: list[str] = sentence.split()

# Step 3: Build a frequency dictionary
counts: dict[str, int] = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

**Say:**
"Three steps, and we already have a working frequency counter. Let's run it with our test sentence: `the quick brown fox jumps over the lazy dog and the fox`

Pause: what do you expect `counts` to look like? … Type your prediction. Now let's add output and run it."

```python
# Step 4: Display results sorted by frequency
print(f"\nWord frequency for: '{sentence}'")
print(f"Total words: {len(words)} | Unique words: {len(counts)}")
print()
print(f"{'Word':<15} {'Count':>5}")
print("-" * 22)

for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word:<15} {count:>5}")

# Step 5: Most common word
most_common = max(counts, key=counts.get)
print()
print(f"Most common: '{most_common}' ({counts[most_common]} times)")
```

**Say:**
"Run the program. Enter: `the quick brown fox jumps over the lazy dog and the fox`

Expected output:

```
Word frequency for: 'the quick brown fox jumps over the lazy dog and the fox'
Total words: 12 | Unique words: 9

Word              Count
----------------------
the                   3
fox                   2
and                   1
brown                 1
dog                   1
jumps                 1
lazy                  1
over                  1
quick                 1

Most common: 'the' (3 times)
```

**[Ask learners]** What happens if two words are tied for most common? … `max()` returns the first one it encounters in that case — whichever comes first in the dictionary's internal order. That is fine for our purposes.

Now let's try a deliberately tricky input: `Hello hello HELLO world world`

What do you predict the output will be?

… Run it. You get:

```
Hello                 1
hello                 1
HELLO                 1
world                 2
```

**[Ask learners]** Is that what we actually want? 'Hello', 'hello', and 'HELLO' are all three counted separately — because Python strings are case-sensitive. This is the case-inconsistency pitfall, and we will fix it in the extension section. For now, the program is *correct* by Python's rules, even if the output is not what a human reader might expect."

---

## 8) Hands-on Lab: Word Counter

### 8.1 Lab specification

**Say:**
"You are now going to build your own version of the Word Counter independently. Here is the specification. Open `hour20_lab_word_counter.py`."

**Lab prompt (display on screen or dictate):**

```
Lab: Word Counter
Write a Python program that:

1. Prompts the user to enter a sentence (any length).
2. Splits the sentence into individual words.
3. Builds a frequency dictionary: each unique word maps to the
   number of times it appears in the sentence.
4. Prints each word and its count — one word per line.

Minimum requirements:
- Correct counts for all words.
- Uses the `d.get(word, 0) + 1` pattern OR an if-check approach.
- Iterates using `.items()` to print results.

Optional extensions (if you finish early):
- Normalize all words to lowercase before counting.
- Strip trailing punctuation (period, comma, exclamation mark)
  using str.replace().
- Sort the output alphabetically or by frequency.
- Print the most common word at the end.
- Print the total word count and the unique word count.
```

### 8.2 Hints to offer if learners are stuck

**Say (if asked):**
"If you are not sure where to start, think about it in steps:
1. Use `input()` to get the sentence.
2. Use `.split()` to turn it into a list.
3. Start with `counts = {}`.
4. Write a for-loop over the words and apply the counting pattern.
5. Write a second for-loop using `.items()` to print."

**Starter shell (optional — write on board or paste into their file):**

```python
# hour20_lab_word_counter.py

sentence = input("Enter a sentence: ")
words = sentence.split()
counts = {}

# TODO: build the frequency dictionary

# TODO: print each word and its count
```

### 8.3 Circulate and observe

**Say:**
"You have 10–12 minutes. I will come around. When you finish the minimum requirements, try the optional extensions — they are genuinely interesting and not far out of reach."

**While circulating, watch for:**
- Learners who iterate the list correctly but forget to start with `counts = {}`.
- Learners who print `counts` directly instead of iterating with `.items()`.
- Learners who try to modify the dictionary inside the iteration loop (see pitfalls section).
- Learners who skip the `get()` pattern and use `counts[word] += 1` — this will raise a `KeyError` on the first encounter; redirect them to initialise with `0` first or use `get()`.

### 8.4 Full walkthrough solution

**Say:**
"Let's walk through a complete solution. I'll build it from the minimum requirements up to the optional extensions so everyone can see the whole arc."

**Minimum solution:**

```python
# hour20_lab_word_counter.py — minimum solution

sentence: str = input("Enter a sentence: ")
words: list[str] = sentence.split()

counts: dict[str, int] = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f"{word}: {count}")
```

**Say:**
"Seven lines including the blank one. If you got this working, you have fully met the lab requirements. Now let's look at each optional extension."

**Extension 1 — lowercase normalization:**

```python
sentence: str = input("Enter a sentence: ")
words: list[str] = sentence.split()

counts: dict[str, int] = {}
for word in words:
    word = word.lower()   # normalize before counting
    counts[word] = counts.get(word, 0) + 1
```

**Say:**
"We apply `word.lower()` *before* the counting step. Now 'Hello', 'hello', and 'HELLO' all map to the same key `'hello'`. One line change, significant improvement in results."

**Extension 2 — simple punctuation stripping:**

```python
for word in words:
    word = word.lower()
    word = word.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    counts[word] = counts.get(word, 0) + 1
```

**Say:**
"We chain `str.replace()` calls to remove common punctuation characters. `replace(',', '')` replaces every comma in the string with an empty string — effectively deleting it. We handle period, exclamation mark, and question mark the same way.

Note: this is a simple approach that works well for typical sentences. In later sessions we will see more powerful tools (like `str.strip()` for leading/trailing characters, and eventually regular expressions for advanced pattern matching). But for Basics scope, chaining `replace()` is perfectly acceptable and transparent.

After stripping: `'hello,'` becomes `'hello'`, `'world!'` becomes `'world'`."

**Full enhanced solution:**

```python
# hour20_lab_word_counter.py — full solution with extensions

sentence: str = input("Enter a sentence: ")
words: list[str] = sentence.split()

counts: dict[str, int] = {}
for word in words:
    # Normalize: lowercase and strip common punctuation
    word = word.lower()
    for punct in (",", ".", "!", "?", ";", ":"):
        word = word.replace(punct, "")
    counts[word] = counts.get(word, 0) + 1

print(f"\nResults for: '{sentence}'")
print(f"Total words: {len(words)} | Unique words: {len(counts)}")
print()
print(f"{'Word':<15} {'Count':>5}")
print("-" * 22)

for word, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{word:<15} {count:>5}")

if counts:
    most_common = max(counts, key=counts.get)
    print(f"\nMost common: '{most_common}' ({counts[most_common]} times)")
```

**Say:**
"Notice one small refinement: we added `if counts:` before calling `max()`. If the user entered an empty string, `sentence.split()` returns an empty list, `counts` remains empty, and `max()` on an empty dictionary raises a `ValueError`. The `if counts:` guard prevents that crash gracefully.

**[Ask learners]** What does `if counts:` evaluate to when `counts` is empty?

… An empty dictionary is falsy in Python — just like an empty list, empty string, and zero. So `if counts:` is `True` when the dictionary has at least one entry and `False` when it's empty. Clean and Pythonic."

### 8.5 Design discussion

**Say:**
"Take thirty seconds and think about this design choice: we normalize the word *inside* the counting loop, not before it. Could we have normalized all words first, before the loop?

…

Yes — we could do `words = [w.lower() for w in sentence.split()]` before the loop. But we haven't covered list comprehensions yet. The inside-the-loop approach is perfectly clear, step-by-step, and follows the principle of doing one thing at a time.

Also notice that we used a `for punct in (...):` loop inside the counting loop to remove each punctuation character. That inner loop is simple and easy to extend — if you want to also remove brackets or quotes, you just add them to the tuple. When you learn more advanced tools later, you can revisit this code and refactor it. But for now, it is readable, correct, and handles real-world input."

---

## 9) Common Pitfalls

**Say:**
"Before we wrap up, let's name the three pitfalls I see most often with this pattern. These are the things to watch out for — both in your own code and when helping a classmate."

### 9.1 Pitfall 1: punctuation attached to words

**Say:**
"The most common issue is punctuation that attaches itself to words. Python's `str.split()` splits on whitespace — but it does *not* strip punctuation from the individual tokens. So if your sentence is:

```
'Hello, world! The fox said: hello.'
```

then `split()` gives you `['Hello,', 'world!', 'The', 'fox', 'said:', 'hello.']`.

Notice: `'Hello,'` (with a comma) and `'hello.'` (with a full stop) are treated as completely different words from each other and from `'Hello'`. Your count will show three separate entries instead of one.

**Fix:** Strip punctuation before or during the counting step, as we showed in the extension. The simple `replace()` chain handles the most common cases."

```python
# Demonstrating the problem
sentence = "Hello, world! Hello."
words = sentence.split()
print(words)
# ['Hello,', 'world!', 'Hello.']

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
# {'Hello,': 1, 'world!': 1, 'Hello.': 1}
# Three entries — not what we wanted.
```

### 9.2 Pitfall 2: case inconsistency

**Say:**
"As we saw during the demo, Python treats `'Hello'`, `'hello'`, and `'HELLO'` as three different strings. Dictionary keys are exact-match — case included. A word typed at the start of a sentence will have an uppercase first letter; the same word elsewhere will be lowercase.

**Fix:** Always normalize to lowercase with `word.lower()` before using the word as a dictionary key — unless you have a specific reason to preserve case (which is rare for word counting)."

```python
# Demonstrating the problem
words = ["The", "fox", "and", "the", "dog"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
# {'The': 1, 'fox': 1, 'and': 1, 'the': 1, 'dog': 1}
# 'The' and 'the' are separate — but they should be the same word.

# The fix
counts = {}
for word in words:
    counts[word.lower()] = counts.get(word.lower(), 0) + 1
print(counts)
# {'the': 2, 'fox': 1, 'and': 1, 'dog': 1}
```

### 9.3 Pitfall 3: modifying a dictionary while iterating over it

**Say:**
"This is a classic Python trap that catches beginners off guard. If you try to add or remove keys from a dictionary inside a loop that is actively iterating over that dictionary, Python raises a `RuntimeError`:

```
RuntimeError: dictionary changed size during iteration
```

Here is an example that triggers the error:"

```python
counts = {"apple": 3, "banana": 1, "cherry": 2}

# BROKEN — do NOT do this
for word, count in counts.items():
    if count == 1:
        del counts[word]   # RuntimeError!
```

**Say:**
"The fix is to collect the keys you want to remove *first*, and then delete them *after* the loop finishes:"

```python
counts = {"apple": 3, "banana": 1, "cherry": 2}

# CORRECT — collect first, delete after
to_remove: list[str] = []
for word in counts:
    if counts[word] == 1:
        to_remove.append(word)
for word in to_remove:
    del counts[word]

print(counts)
# {'apple': 3, 'cherry': 2}
```

**Say:**
"You won't run into this in today's lab — because we are only reading from the dictionary inside our loop, not modifying it. But keep it in mind for future programs where you might want to filter or clean a dictionary."

---

## 10) Optional Extension: Lowercase + Punctuation Stripping

**Say:**
"Let's look at the normalization extension one more time in a focused way, so the technique is crystal clear. This section is for learners who finished the lab early and want to level up their solution."

### 10.1 Why normalization matters

**Say:**
"Consider analysing a real paragraph — say, a few sentences from a news article. You would encounter:
- Sentence-starting capital letters: `'The'` vs `'the'`
- Commas: `'apple,'` vs `'apple'`
- Periods: `'dog.'` vs `'dog'`
- Exclamation marks, question marks, colons
- Possibly hyphens within compound words

Without normalization, your frequency counter misses patterns that a human reader would naturally group together. Normalization is not fancy — it is just good data hygiene."

### 10.2 `str.lower()` — fixing case

```python
word = "Hello"
print(word.lower())    # 'hello'

word = "PYTHON"
print(word.lower())    # 'python'

word = "already lowercase"
print(word.lower())    # 'already lowercase' (no change)
```

**Say:**
"`str.lower()` returns a *new* string with all characters converted to lowercase. It does not modify the original string — strings in Python are immutable. You must assign the result back (e.g. `word = word.lower()`) or use it directly."

### 10.3 `str.replace()` — removing punctuation

```python
word = "hello,"
clean = word.replace(",", "")
print(clean)    # 'hello'

word = "world!"
clean = word.replace("!", "")
print(clean)    # 'world'
```

**Say:**
"`str.replace(old, new)` returns a new string with every occurrence of `old` replaced by `new`. When `new` is an empty string, every occurrence of `old` is deleted.

We can chain multiple `replace()` calls on a single line:"

```python
word = "Hello,"
clean = word.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
print(clean)    # 'hello'
```

**Say:**
"Read the chain from left to right: first lowercase, then remove comma, then remove period, then remove exclamation mark, then remove question mark. Each method call receives the output of the previous one."

### 10.4 Before and after — seeing the difference

```python
sentence = "To be, or not to be: that is the question!"
print("BEFORE normalization:")
words_raw = sentence.split()
counts_raw: dict[str, int] = {}
for word in words_raw:
    counts_raw[word] = counts_raw.get(word, 0) + 1
for w, c in sorted(counts_raw.items()):
    print(f"  {w!r}: {c}")

print("\nAFTER normalization:")
counts_clean: dict[str, int] = {}
for word in words_raw:
    word = word.lower()
    for punct in (",", ".", "!", "?", ":"):
        word = word.replace(punct, "")
    counts_clean[word] = counts_clean.get(word, 0) + 1
for w, c in sorted(counts_clean.items()):
    print(f"  {w!r}: {c}")
```

**Output — Before:**
```
  'To': 1
  'be,': 1
  'be:': 1
  'is': 1
  'not': 1
  'or': 1
  'question!': 1
  'that': 1
  'the': 1
  'to': 1
```

**Output — After:**
```
  'be': 2
  'is': 1
  'not': 1
  'or': 1
  'question': 1
  'that': 1
  'the': 1
  'to': 2
```

**Say:**
"Before normalization: 10 unique entries — 'To' and 'to' are separate, 'be,' and 'be:' are separate. After normalization: 8 unique entries — 'be' correctly counted 2 times, 'to' correctly counted 2 times. The result is far more meaningful.

Notice `{w!r}` in the f-string — the `!r` conversion applies `repr()` to the value, which wraps strings in quotes and makes invisible characters visible. It is very useful for debugging string content. You don't need it in production output, but it is handy when checking whether punctuation was correctly stripped."

---

## 11) Session 5 Day Wrap-Up

### 11.1 Recap of all four hours

**Say:**
"We have arrived at the end of Day 5 — Session 5 — and I want to take a moment to genuinely appreciate how much ground we covered today. This was a dense, important session.

**Hour 17 — Tuples + Unpacking:**
We learned that a tuple is an ordered, immutable sequence — like a list that has been locked. You use tuples when the data should not change: coordinates, RGB colour values, function return values with multiple parts. We practised the unpacking pattern — `x, y = point` — which lets you assign all elements of a tuple to named variables in one clean line. You built a Coordinate Tracker and handled `ValueError` when a single-item tuple is accidentally written without its trailing comma.

**Hour 18 — Sets: Uniqueness + Membership:**
We discovered the set — an unordered collection of unique values. Sets are Python's answer to 'have I seen this before?' questions and 'give me all the distinct things in this collection'. You saw how adding a duplicate to a set is silently ignored, how `in` checks on sets are fast, and how to convert a list to a set to strip duplicates in one step. You built the Unique Visitors program.

**Hour 19 — Dictionary Fundamentals:**
We introduced the dictionary — the most powerful and flexible collection type in Python for associating meaning with data. You learned the key-value model, how to create dictionaries with literal syntax, how to read, add, and update entries, and — critically — how to access values safely with `get()` rather than risking a `KeyError`. You built an interactive Inventory Manager.

**Hour 20 — Dictionary Iteration + Counting Pattern:**
This hour. We completed the dictionary picture by learning how to traverse all entries with `keys()`, `values()`, and `items()`. Then we built the counting pattern — `d.get(word, 0) + 1` — which is one of the most practically useful idioms in all of Python. We applied it to build a Word Frequency Counter from scratch, added sorted display, found the most common word, and learned to normalize text by converting to lowercase and stripping punctuation. You can now write a frequency counter from memory."

### 11.2 The data structures map

**Say:**
"Step back for a second and look at the full picture of what you now know:

| Structure | Ordered? | Unique values? | Mutable? | Key use case |
|-----------|----------|----------------|----------|--------------|
| `list`    | ✅ Yes   | No             | ✅ Yes   | Ordered sequences, indexing |
| `tuple`   | ✅ Yes   | No             | ❌ No    | Fixed records, unpacking |
| `set`     | ❌ No    | ✅ Yes         | ✅ Yes   | Uniqueness, membership |
| `dict`    | ✅ Yes*  | Keys only      | ✅ Yes   | Key→value lookup, counting |

*Dictionaries maintain insertion order in Python 3.7+.

You have the full toolkit. The question is no longer 'how do I use this structure?' but 'which structure should I reach for?' And that is *exactly* what Session 6 tackles."

### 11.3 Forward look to Session 6

**Say:**
"In our next session — Session 6, Hours 21 through 24 — we are going to step back from individual structures and ask the big design question: **when should I use a list? When should I use a set? When should I use a dictionary?**

We will work through a Refactor Challenge where you first solve a problem using a list, and then improve it by switching to a more appropriate structure. We will also start looking at how structures nest inside each other — a list of dictionaries is one of the most common data shapes in real-world Python, and you will start using it to model more complex data.

Session 6 is where everything clicks together. I am genuinely excited to see you there."

### 11.4 Congratulatory close

**Say:**
"Seriously — take a moment to recognise what you did today. You learned four distinct data structures, wrote four programs from scratch, handled edge cases, and built a word frequency counter that could run on a real piece of text. That is not beginner stuff disguised as beginner stuff — that is actual, practical Python programming skill.

If any part of today felt hard: good. That means you were working in the zone where learning actually happens. If you want to consolidate, go home and type the Word Counter again from memory — no notes. Then run it on a paragraph of text you find interesting. See what the most common words are. That's real programming.

Well done today. Save your files, and I'll see you at Session 6."

---

## 12) Exit Ticket

**Display the following question and give learners 90 seconds to answer in writing or by typing:**

**Question:**
> What does `dict.items()` produce, and why is it useful in a for-loop?

**Expected answer (for instructor reference):**

`dict.items()` returns a view of the dictionary as a sequence of `(key, value)` tuples. In a for-loop, you can unpack each tuple into named variables — for example `for word, count in counts.items():` — which gives you access to both the key and the value on every iteration without any extra indexing. This makes it the standard way to process all entries of a dictionary when you need both pieces of information.

**Bonus follow-up (ask verbally if time allows):**

> What is the difference between `d.get(key)` and `d[key]`?

**Expected answer:** `d[key]` raises a `KeyError` if the key is not in the dictionary. `d.get(key)` returns `None` silently if the key is absent. `d.get(key, default)` returns `default` instead of `None`. The `get()` form is safe for keys that may not be present; bracket notation is safe only when you are certain the key exists.

---

*End of Day 5, Hour 4 (Course Hour 20) — Dictionary Iteration + Counting Pattern*  
*Python Programming Basics – Session 5*
