# Day 5, Hour 4: Dictionary Iteration + Counting Pattern (Course Hour 20)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 20 – Dictionary iteration + counting pattern  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. This hour deepens dictionary skills from Hour 19 and introduces the frequency-counting pattern. The three key mechanics are: iterating with `dict.items()` to access key-value pairs in a loop, the counting idiom `d[word] = d.get(word, 0) + 1`, and cleaning input (lowercase, punctuation stripping) to produce accurate counts. Keep scope tight. Do not introduce `collections.Counter`, dict comprehensions, `sorted()` with `key=` on dict items (it is fine to use `sorted()` on keys for display, but do not require complex sort keys in the lab), or `defaultdict`. The lab is the Word Counter. The optional extension is simple punctuation stripping with `str.replace()`.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:
1. Use `dict.items()` to iterate over key-value pairs together in a for loop.
2. Explain what `dict.keys()` and `dict.values()` return and when each is useful.
3. Build a frequency counter using the pattern `d[word] = d.get(word, 0) + 1`.
4. Count how many times each word appears in a sentence entered by the user.
5. Handle case inconsistencies by normalizing text to lowercase before counting.
6. Describe how to extend the pattern to strip simple punctuation from words.
7. Print a clear word-frequency report sorted by word for easy reading.

The counting pattern we cover today appears everywhere in real Python: analyzing logs, surveying survey data, processing user input, and building any kind of frequency analysis. It is one of those techniques that every Python programmer reaches for regularly."

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Recap of dict fundamentals, transition to iteration, and motivation for counting
- **0:05–0:15** `items()`, `keys()`, `values()`: the three dict view methods
- **0:15–0:28** The counting pattern: `d.get(word, 0) + 1` explained step by step
- **0:28–0:38** Live demo: word frequency counter for a hard-coded sentence
- **0:38–0:48** Common pitfalls: punctuation, case sensitivity, `None` from missing default
- **0:48–0:57** Guided lab: Word Counter (user input)
- **0:57–1:00** Debrief, Session 5 recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour20_dict_iteration_demo.py`.
- Prepare a sample sentence with intentional repetition: `"the cat sat on the mat the cat"`.
- Be ready to show the output of `dict.items()`, `dict.keys()`, and `dict.values()` separately.
- Be ready to step through the counting loop iteration by iteration on the board or verbally.
- Be ready to show what happens without `.lower()`: `"The"` and `"the"` count as different words.
- Have a second sentence ready for a second run: `"to be or not to be that is the question"`.
- If some learners type slowly, have a starter file ready.

**Say:** "This hour ties together everything we have learned about dictionaries. Please type with me—the counting pattern especially needs to be felt, not just read."

---

## 3) Opening Script: From Storing to Processing (~5 minutes)

### 3.1 Recap and frame the hour

**Say:**
"Welcome to the final hour of Session 5 and of Day 5.

In Hour 19, we learned the fundamentals of dictionaries: how to create them, how to read values safely, how to update or add entries, and how to check whether a key exists.

That knowledge was about working with a dictionary we already have. Today's hour is about building dictionaries from scratch during runtime—constructing a dict by processing information one piece at a time.

Specifically, we will learn how to count things. When you have a stream of items—words, events, votes, inputs—and you want to know how many times each one appeared, a dictionary is the perfect tool."

### 3.2 The real problem that motivates counting

**Say:**
"Imagine you are building a word-cloud generator. You need to know which words appear most often in a document. Or imagine you are analyzing a sales log and want to know which products were ordered most frequently. Or you are building a voting system and need to tally votes per candidate.

In all of these situations, you are asking the same question: 'For each unique thing I have seen, how many times did I see it?'

That question maps perfectly onto a dictionary. The unique thing is the key. The count is the value.

By the end of this hour, you will have the pattern memorized and will be able to apply it to any counting problem you encounter."

### 3.3 Connect to prior learning

**Say:**
"Before we write the counting pattern, let me close a gap from the last hour. When we printed the inventory, I used `for item, qty in inventory.items()` but I did not fully explain what `.items()` is.

Today we start there. Understanding `items()` properly will make the rest of the hour much clearer."

---

## 4) Core Concept: Dict Iteration with `items()`, `keys()`, `values()` (~10 minutes)

### 4.1 Why iteration matters

**Say:**
"In Hour 19, we printed the inventory neatly by looping over `inventory.items()`. But why not just `for item in inventory`? Let me show you the difference."

**Type:**

```python
inventory = {
    "apples": 30,
    "bananas": 12,
    "milk": 5,
    "bread": 8,
    "eggs": 24,
}

# Loop directly over a dict — what do we get?
for thing in inventory:
    print(thing)
```

Run it.

**Say:**
"When you loop directly over a dictionary, you get only the keys—not the values. Python's default dict iteration is key iteration.

This is useful when you only need the keys—for example, to check or display them. But when you need both key and value together, you use `.items()`."

### 4.2 `dict.items()` — the paired view

**Type:**

```python
# items() gives (key, value) pairs
for item, qty in inventory.items():
    print(f"{item}: {qty}")
```

Run it.

**Say:**
"`.items()` returns each entry as a pair. We unpack each pair into two variables—`item` and `qty`—in the loop header. This is exactly the same tuple unpacking pattern we learned in Hour 17. A dictionary entry, when you iterate with `items()`, behaves like a two-item tuple.

So our Session 5 topics connect directly: the unpacking skill from Hour 17 is the same skill we use here with `items()`."

### 4.3 `dict.keys()` — keys only

**Type:**

```python
# keys() gives only the keys
for key in inventory.keys():
    print(key)
```

**Say:**
"`.keys()` explicitly returns the keys. This is the same as just `for key in inventory`, but it is more explicit about your intent. Use it when you want to communicate clearly that you only care about keys."

### 4.4 `dict.values()` — values only

**Type:**

```python
# values() gives only the values
for qty in inventory.values():
    print(qty)

# Useful for aggregate operations
total = sum(inventory.values())
print(f"\nTotal items in stock: {total}")
```

Run it.

**Say:**
"`.values()` returns just the values. This is useful for aggregate calculations: total stock, average quantity, minimum or maximum value.

Notice `sum(inventory.values())` gives us the total of all quantities without needing to manually loop and accumulate."

### 4.5 Ask for predictions

**Ask learners:**
- "If I use `for key in inventory`, do I get keys or values?"
- "If I use `for k, v in inventory.items()`, what are `k` and `v`?"
- "If I use `sum(inventory.values())`, what does that compute?"

Pause for answers, then confirm.

---

## 5) The Counting Pattern (~12 minutes)

### 5.1 Introduce the problem clearly

**Say:**
"Now let's solve the word-frequency problem step by step.

I have a sentence: `'the cat sat on the mat the cat'`.

I want to produce a dictionary that looks like this:

```text
{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```

Key is the word. Value is how many times it appears. Let me walk you through the counting loop."

### 5.2 Start with the naive approach and its problem

**Type:**

```python
sentence = "the cat sat on the mat the cat"
words = sentence.split()
print(words)
```

Run it.

**Say:**
"`split()` with no arguments splits on whitespace and returns a list of words. We now have a list we can loop over.

Now, here is the challenge: how do we count each word? My instinct might be to write:

```python
counts = {}
for word in words:
    counts[word] += 1  # This will FAIL
```

Let me show you why this fails."

**Type and run:**

```python
counts = {}
for word in words:
    counts[word] += 1
```

Run it.

**Say:**
"We get a `KeyError: 'the'`. Why? Because on the very first iteration, when we see 'the' for the first time, the key 'the' does not yet exist in the dictionary. So `counts['the']` raises a `KeyError` before `+= 1` can even run.

The fundamental problem is: we cannot increment a value that does not exist yet. We need to handle the first occurrence separately from subsequent occurrences."

### 5.3 The `if-else` approach (intuitive but verbose)

**Type:**

```python
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
```

Run it.

**Say:**
"This works correctly. On the first occurrence of a word, the `else` branch creates the entry with value `1`. On every subsequent occurrence, the `if` branch increments it.

This is readable and clear. For beginners who find the next version too dense, this is a perfectly valid solution. Use it if the one-liner pattern does not feel natural yet.

But there is a more compact, idiomatic Python way."

### 5.4 The `get()` counting idiom

**Type:**

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

Run it.

**Say:**
"This produces exactly the same result. Let me break down this one line:

`counts.get(word, 0)` says: 'Get the current count for this word. If there is no count yet, treat it as 0.'

Then we add 1 to that result.

Then we assign back to `counts[word]`.

So on the first occurrence of 'the': `counts.get('the', 0)` returns `0`. Add 1. Assign `counts['the'] = 1`.

On the second occurrence of 'the': `counts.get('the', 0)` returns `1`. Add 1. Assign `counts['the'] = 2`.

On the third: `counts.get('the', 0)` returns `2`. Add 1. Assign `counts['the'] = 3`.

This pattern is elegant because it collapses the first-occurrence and subsequent-occurrence logic into one line. The `get()` default handles the 'not yet seen' case silently."

### 5.5 Make learners say the pattern back

**Ask learners:**
"In your own words, what does `counts.get(word, 0) + 1` compute?"

Take two or three responses. You want to hear something like: "It gets the current count, defaulting to zero if the word hasn't been seen, then adds one."

**Say:**
"That is exactly right. The key insight is: `get()` with a default of `0` turns a missing key into a starting value, and then we increment it. This is the one-liner version of the if-else pattern."

### 5.6 Printing the result sorted

**Type:**

```python
print("\nWord counts:")
for word in sorted(counts):
    print(f"  {word}: {counts[word]}")
```

**Say:**
"When we use `sorted(counts)`, we iterate over the keys in alphabetical order. The output is now consistent and easy to scan, rather than depending on insertion order.

This is a small but important polish. In real programs, sorted output makes logs, reports, and outputs much easier to read."

---

## 6) Handling Case and Punctuation (~8 minutes)

### 6.1 Case sensitivity problem

**Say:**
"Let me show you a real problem that will occur the moment you use real text."

**Type:**

```python
sentence = "The cat sat on the mat. The cat."
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

Run it.

**Say:**
"Look at the output. 'The' and 'the' are counted separately. 'mat.' with the period and 'mat' without are treated as different words. 'cat.' and 'cat' are different words too.

This is not the result we want. We want 'the', 'The', and 'THE' to all count as the same word, and we want to ignore punctuation."

### 6.2 Fix with `.lower()`

**Type:**

```python
sentence = "The cat sat on the mat. The cat."
words = sentence.split()
counts = {}
for word in words:
    word = word.lower()  # normalize case
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

Run it.

**Say:**
"Now 'The' and 'the' are counted together as 'the': 3 occurrences. But we still have 'mat.' and 'cat.' with trailing periods. That is the punctuation problem."

### 6.3 Simple punctuation stripping with `replace()`

**Say:**
"For beginner-level text cleaning, the simplest approach is to use `replace()` to remove specific punctuation characters."

**Type:**

```python
sentence = "The cat sat on the mat. The cat."
# Remove periods and commas before splitting
clean = sentence.replace(".", "").replace(",", "")
words = clean.split()

counts = {}
for word in words:
    word = word.lower()
    counts[word] = counts.get(word, 0) + 1

print("Word counts:")
for word in sorted(counts):
    print(f"  {word}: {counts[word]}")
```

Run it.

**Say:**
"Now the counts are clean. 'cat' appears twice, 'the' appears three times, and every other word appears once.

The cleaning approach here is simple: call `replace()` for each punctuation character you want to remove. This is not the most powerful text-processing technique in Python—for production-grade NLP you would use regular expressions or a library—but for beginner programs it is clear, readable, and effective.

In the lab, if you want to attempt the optional extension, this is exactly the technique to use."

### 6.4 Reinforce the full pattern

**Say:**
"Let me now state the complete, clean counting recipe so you can use it in the lab:

1. Start with an empty dictionary: `counts = {}`
2. Get your list of words by splitting the sentence
3. Loop over the words
4. Normalize each word with `.lower()`
5. Use the get-plus-one idiom: `counts[word] = counts.get(word, 0) + 1`
6. After the loop, print with `for word in sorted(counts)`

That is the recipe. It is five lines of logic and it solves a real problem."

---

## 7) Full Live Demo: Word Frequency Counter (~5 minutes)

**Say:**
"Let me now write the complete demo, clean and commented, so you have a reference model for the lab."

**Type:**

```python
# hour20_dict_iteration_demo.py

sentence = "to be or not to be that is the question to be"

# Step 1: clean and split
words = sentence.lower().split()

# Step 2: build frequency dict
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Step 3: display sorted results
print("Word Frequency Report")
print("=" * 24)
for word in sorted(counts):
    print(f"  {word:<12} {counts[word]}")

# Step 4: summary stats
total_words = sum(counts.values())
unique_words = len(counts)
print(f"\nTotal words:  {total_words}")
print(f"Unique words: {unique_words}")
```

Run it.

**Say:**
"A few new things here:

`sentence.lower().split()` chains the two operations in one step. We lowercase the whole sentence first, then split. This is equivalent to the two-step version but slightly more compact.

`{word:<12}` in the f-string left-aligns the word in a field 12 characters wide, producing a neat two-column table.

`sum(counts.values())` gives the total word count.

`len(counts)` gives the number of unique words.

These summary stats are small additions that make the output much more informative. For the lab, they are a natural extension."

---

## 8) Common Pitfalls and How to Coach Through Them (~4 minutes)

### 8.1 Pitfall: KeyError in the counting loop

**Symptom:** learner writes `counts[word] += 1` without initializing the key first.

**Coach with these words:**
"Your first instinct—`counts[word] += 1`—is natural, but it fails on the very first time you see a word. The key does not exist yet, so there is no value to increment. Use `counts[word] = counts.get(word, 0) + 1` instead. The `get()` default of `0` handles the first-occurrence case."

### 8.2 Pitfall: forgetting `.lower()` and counting 'The' and 'the' separately

**Symptom:** learner sees 'The' and 'the' as different entries in the output.

**Coach with these words:**
"Try printing the keys and you'll see 'The' and 'the' are separate. Python string comparison is case-sensitive, so `'The' == 'the'` is `False`. Add `word = word.lower()` inside the loop before the `get()` line. That normalizes every word to lowercase so they merge correctly."

### 8.3 Pitfall: words including punctuation like 'cat.' and 'cat'

**Symptom:** learner sees 'cat.' and 'cat' counted separately.

**Coach with these words:**
"The period is still attached to the word because `split()` only splits on spaces. To strip the period, call `replace('.', '')` on the sentence before splitting, or call `word.strip('.')` on each word inside the loop. For the optional extension, try `replace()` on the full sentence first—it is the simplest approach."

### 8.4 Pitfall: `get()` without a default returning `None`

**Symptom:** learner writes `counts.get(word) + 1` and gets `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.

**Coach with these words:**
"When you call `get()` with only one argument and the key is missing, Python returns `None`. You cannot add 1 to `None`. Always include the second argument—the default: `counts.get(word, 0)`. The `0` is what makes the arithmetic work on first occurrence."

### 8.5 Pitfall: printing the dict directly instead of using a loop

**Symptom:** learner prints `print(counts)` and gets an unformatted wall of text.

**Coach with these words:**
"Printing the raw dict is useful for quick debugging, but for a clean report, use `for word in sorted(counts): print(f'{word}: {counts[word]}')`. That gives one entry per line in alphabetical order."

---

## 9) Guided Lab: Word Counter (~12 minutes)

### 9.1 Introduce the lab

**Say:**
"Your task is to build the Word Counter. Here are the requirements:

1. Ask the user to enter a sentence.
2. Split the sentence into words.
3. Build a frequency dictionary using the counting pattern.
4. Print each word and its count.
5. Normalize words to lowercase so case differences do not affect counts.

The optional extension is to strip simple punctuation (periods and commas) before counting."

### 9.2 Put the requirements on screen

```text
Lab: Word Counter
- Input a sentence from the user
- Split into words
- Build a frequency dictionary: word → count
- Normalize to lowercase
- Print each word and its count (sorted)
Optional: strip periods and commas before counting
```

### 9.3 Provide a beginner-friendly starter structure

**Type and leave on screen:**

```python
# hour20_lab_word_counter.py

# Step 1: get user input
sentence = input("Enter a sentence: ")

# Step 2: normalize and split
words = sentence.lower().split()

# Step 3: count words
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Step 4: print results
print("\nWord Frequency:")
for word in sorted(counts):
    print(f"  {word}: {counts[word]}")

# Step 5: summary
print(f"\nTotal words: {sum(counts.values())}")
print(f"Unique words: {len(counts)}")
```

### 9.4 Explain the starter

**Say:**
"This is the complete minimal solution. It implements every required step:
- Line 4 takes user input.
- Line 7 normalizes to lowercase and splits.
- Lines 10–11 run the counting loop.
- Lines 14–15 print the sorted report.
- Lines 18–19 add summary statistics.

Your first goal is to run this and try it with a sentence that has repeated words. Then try one where the same word appears with different capitalization—like 'The' and 'the'—and confirm they are counted together."

### 9.5 Optional extension: punctuation stripping

**Type the extension:**

```python
# Optional extension: strip common punctuation
sentence = input("Enter a sentence: ")

# Remove periods, commas, question marks, exclamation marks
clean = (sentence
         .replace(".", "")
         .replace(",", "")
         .replace("?", "")
         .replace("!", ""))

words = clean.lower().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("\nWord Frequency (punctuation stripped):")
for word in sorted(counts):
    print(f"  {word}: {counts[word]}")
```

**Say:**
"Notice the chained `.replace()` calls. Each call returns a new string with one character removed, and we immediately call `.replace()` again on the result. This is method chaining, and it is a common Python pattern for successive transformations.

For a beginner extension, this is clean and readable. You do not need to know anything about regular expressions to make it work."

### 9.6 Optional second extension

**Say:**
"If you want a second challenge: after building the frequency dict, find and print the most common word. You can do this with `max(counts, key=lambda w: counts[w])` — but if lambda syntax feels uncomfortable, you can also just use a manual loop to track the maximum."

**Type the manual approach:**

```python
# Find the most frequent word (manual approach)
max_word = None
max_count = 0
for word, count in counts.items():
    if count > max_count:
        max_count = count
        max_word = word

print(f"\nMost common word: '{max_word}' ({max_count} times)")
```

**Say:**
"This manual approach reinforces `items()` iteration and a max-tracking pattern that works in many other situations. It is also more transparent than the one-liner lambda version—you can follow each step."

### 9.7 Instructor circulation prompts

As learners work, walk around and ask:
- "Show me your counting line. What does `counts.get(word, 0)` return on the first time we see a word?"
- "What happens if you forget `.lower()`? Try a sentence with 'The' at the start."
- "What does `sorted(counts)` sort by? Keys or values?"
- "How many unique words does your sentence have? Does `len(counts)` match your expectation?"
- "What does `sum(counts.values())` compute? Is that the same as `len(words)`?"

---

## 10) Debrief, Share-Outs, and Session 5 Close (~5 minutes)

### 10.1 Bring the class back together

**Say:**
"Let's debrief the Word Counter and then close Session 5.

First, the lab. You built a program that reads text, splits it into words, builds a frequency dictionary, and reports the results. That is a real, useful program that you could adapt for a dozen different tasks right now."

### 10.2 Ask targeted questions

Ask:
- "Who can explain the counting idiom in one sentence?"
- "Who tried the punctuation extension? What did you use and how?"
- "Who found the most common word? What approach did you use—the manual loop or the lambda one-liner?"
- "Who connected the `items()` loop back to the tuple unpacking from Hour 17?"

### 10.3 Session 5 recap

**Say:**
"Before we close, let me zoom out and summarize the full arc of Session 5.

We covered four data structures today:
- **Tuples** (Hour 17): ordered, immutable, ideal for fixed-size records like coordinates. Unpack with `x, y = point`.
- **Sets** (Hour 18): unordered, unique values. Convert a list to a set to deduplicate. `add()` ignores repeats.
- **Dicts fundamentals** (Hour 19): key-value storage. Read safely with `get()`. Check with `in`. Update or create with assignment.
- **Dict iteration + counting** (Hour 20): loop over `items()` for key-value pairs. Build frequency counters with the `get(word, 0) + 1` idiom.

These four structures—lists from Session 4, plus tuples, sets, and dicts from today—are the core collection tools in Python. Nearly every real program uses at least two of them.

The question you should carry forward is not 'How do I use each structure?' but 'Which structure should I reach for when?'"

### 10.4 The four-structure decision guide

**Say:**
"Here is a simple decision guide you can keep in mind:

| Question | Use |
|---|---|
| Is order important, and will the size change? | List |
| Is order important, but the data is fixed? | Tuple |
| Do I need unique values only? | Set |
| Do I need to look up a value by name? | Dictionary |

That is not the whole story—there are more nuances—but this guide is accurate for ninety percent of the beginner decisions you will face."

---

## 11) Recap Script (~2 minutes)

**Say:**
"For Hour 20 specifically, here is what to take away:

- `dict.items()` returns key-value pairs as tuples. Use it when you need both key and value in a loop.
- `dict.keys()` returns keys only. `dict.values()` returns values only.
- The frequency-counting idiom: `d[word] = d.get(word, 0) + 1`.
- Normalize with `.lower()` before counting to merge 'The' and 'the'.
- Use `sorted(counts)` to iterate keys alphabetically for clean output.
- `sum(counts.values())` = total item count. `len(counts)` = unique item count.

In the next session, we will begin exploring functions: how to define reusable blocks of code that take input and produce output. The data structures we mastered today will show up immediately inside those functions."

---

## 12) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. What does `dict.items()` produce when used in a for loop?
2. Why does `counts[word] += 1` fail on the first occurrence of a new word?
3. What does `counts.get(word, 0) + 1` return when `word` has never been seen?
4. What is the difference between `len(counts)` and `sum(counts.values())`?

**Expected direction of answers:**
- `items()` produces key-value pairs (like tuples) — both the key and value together per iteration
- on the first occurrence the key does not exist, so `counts[word]` raises `KeyError`
- `get()` returns the default `0`; add 1 gives `1` — the first occurrence is correctly initialized to `1`
- `len(counts)` is the number of unique keys (unique words); `sum(counts.values())` is the total of all values (total word occurrences)

---

## 13) Instructor Notes for the Transition to Session 6

**Say:**
"We have now built a solid foundation in Python's core data structures. The next session introduces functions. Functions will change the way you organize and think about your programs. Instead of writing everything in one flat sequence of lines, you will learn to break programs into named, reusable blocks.

The data structures you learned today will show up immediately. You will write functions that accept lists or dicts as arguments, process them, and return results. Everything you practiced this session is groundwork for that next step."

If learners seem shaky on today's counting pattern, reinforce before dismissing:
- "The key idiom: `counts[word] = counts.get(word, 0) + 1`."
- "The key loop: `for word, count in counts.items():`."

---

## Appendix: Instructor Reinforcement Notes for Hour 20

### A) Board sketch for visual learners

Draw this on the board and walk through it step by step:

```text
sentence = "the cat sat the cat"
words    = ["the", "cat", "sat", "the", "cat"]

Iteration 1: word = "the"
  counts.get("the", 0) → 0
  counts["the"] = 0 + 1 = 1
  counts = {"the": 1}

Iteration 2: word = "cat"
  counts.get("cat", 0) → 0
  counts["cat"] = 0 + 1 = 1
  counts = {"the": 1, "cat": 1}

Iteration 3: word = "sat"
  counts["sat"] = 0 + 1 = 1
  counts = {"the": 1, "cat": 1, "sat": 1}

Iteration 4: word = "the"
  counts.get("the", 0) → 1
  counts["the"] = 1 + 1 = 2
  counts = {"the": 2, "cat": 1, "sat": 1}

Iteration 5: word = "cat"
  counts.get("cat", 0) → 1
  counts["cat"] = 1 + 1 = 2
  counts = {"the": 2, "cat": 2, "sat": 1}
```

Say: "Notice that `get()` with default `0` handles iteration 1 for any new word, and returns the real count for any word already seen."

### B) Short extra practice prompts

If you have extra minutes:

1. What does `counts.items()` return? How would you use it in a loop?
2. What is the result of `counts.get("zebra", 0)` if 'zebra' is not in `counts`?
3. If `counts = {"a": 3, "b": 1, "c": 2}`, what does `sorted(counts)` return?
4. What does `max(counts.values())` return for the same dict?
5. Write one line to print every key in `counts` that has a count greater than 1.

### C) Instructor language for gentle correction

- "Read the error. `KeyError` on the counting line means the key does not exist yet. Use `get(word, 0)` to handle first occurrence."
- "Print a few values from your `counts` dict. Do you see separate entries for uppercase and lowercase versions of the same word? Add `.lower()` before counting."
- "You are printing `counts` as a raw dict. That works, but use a sorted loop for a cleaner report."
- "Where exactly are you building the counts dict? Make sure the `counts = {}` line is outside the loop."

### D) Common conceptual misunderstanding: `items()` returns what exactly?

If a learner asks "What kind of thing does `items()` return?", say:

"It returns a view object that generates pairs—each pair is a tuple of (key, value). That is why we can unpack in the loop header with `for word, count in counts.items()`. The unpacking is exactly the same as `for x, y in list_of_tuples`—which is why we practiced tuple unpacking in Hour 17."

### E) Coaching if learners ask about Counter

If a learner asks "Why not just use `Counter` from `collections`?", say:

"Great instinct—`Counter` is exactly the right tool for this in an Advanced Python context. It does everything we are doing here in one step. But we are building the pattern by hand first, because once you understand how a frequency dict works from scratch, `Counter` will feel like a natural shortcut rather than a mystery. When you reach the Advanced session, `Counter` will be a one-line replacement for what you built today."

### F) Connecting iteration + counting to real applications

If you want to extend the debrief discussion, mention:
- Log analysis: counting how many times each HTTP status code appears
- Survey data: counting how many people chose each answer option
- Game scores: tallying wins per player
- E-commerce: counting orders per product

Each one uses exactly the same pattern: loop, normalize if needed, and `d[key] = d.get(key, 0) + 1`.

### G) Final teaching reminder to yourself

The hour succeeds if learners leave with this mental model:

"`dict.items()` gives me key and value together in a loop. The counting pattern is `d[word] = d.get(word, 0) + 1`. Normalize with `.lower()`. Print sorted for clean output."

---

## Speaker Notes: Scope Guardrails

**Teach in this hour:**
- `dict.items()` for key-value pair iteration
- `dict.keys()` for key-only iteration
- `dict.values()` for value-only iteration
- `sum(dict.values())` for total
- `len(dict)` for unique key count
- The frequency-counting idiom: `d[word] = d.get(word, 0) + 1`
- The if-else alternative for counting (valid and clear for beginners)
- Normalizing to lowercase with `.lower()` before counting
- Simple punctuation stripping with `str.replace()` (optional extension)
- `sorted(counts)` for alphabetical key iteration in display
- Manual max-tracking loop over `items()` (optional extension)

**Do NOT introduce in this hour:**
- `collections.Counter` (out of scope — Advanced)
- `collections.defaultdict` (out of scope — Advanced)
- Dict comprehensions (out of scope — Basics generally avoids comprehensions)
- `sorted()` with complex `key=` functions as a required concept (lambda is optional/extension only)
- Regular expressions for text cleaning (out of scope — Advanced)
- `nltk` or other NLP libraries (out of scope)
- Sorting a dict by values as a required outcome (optional only)
- Merging two dicts with `update()` or `|=` (save for a later session)
- `enumerate()` on dict views (not needed for this lab)

Keep the conceptual messages clear and repeatable:
1. **`items()` gives you both key and value.** Use it whenever you need to work with the full pair.
2. **`d[word] = d.get(word, 0) + 1` is the counting idiom.** Memorize it. Apply it to any counting problem.
