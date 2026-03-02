# Day 2 — Hour 6 (Session 2): String Methods (Normalize, Search, Replace)

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 2, Hour 6  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab

---

## Instructor Deliverable Script (Largely Verbatim)

> This hour reinforces the runbook outcomes: use common string methods, explain immutability, and apply methods in practical text-cleaning.

---

## 0) Learning Outcomes (read aloud, 2 minutes)

“By the end of this hour, you will be able to:
1. Use `.lower()`, `.upper()`, `.strip()`, `.replace()`, and `.find()` correctly.
2. Explain why string methods usually return a new string.
3. Decide when to use `in` versus `find()`.
4. Clean a messy sentence and detect keyword presence reliably.”

---

## 1) Agenda + Timing (2 minutes)

- **0:00–0:05** Reset, outcomes, method overview
- **0:05–0:18** Talk track: immutability + core methods
- **0:18–0:26** Live demos: cleanup pipeline + `find()` with `-1`
- **0:26–0:52** Guided lab: Text Sanitizer
- **0:52–0:58** Debrief, pitfalls, quick checks
- **0:58–1:00** Transition to Hour 7

---

## 2) Setup and Framing (instructor prep)

Before class, open `hour6_methods_demo.py` and prepare sample strings:
- `"   HELLO world   "`
- `"Python    is      great"`
- `"student@example.com"`
- `"no-at-symbol.com"`

**Say:**
“Hour 5 taught us how to access text by position. Hour 6 teaches us how to transform text and search it cleanly. Think of these methods as your text toolbox.”

---

## 3) Talk Track (10–15 minutes)

### 3.1 Motivation: why methods matter

**Say:**
“Real input is messy: random spacing, inconsistent case, typo-like formatting. Before any logic, we often normalize text. Normalization means making text consistent so our checks and comparisons behave predictably.”

“Today you’ll learn simple, practical cleaning steps used in almost every beginner automation script.”

### 3.2 Case conversion

**Type and narrate:**

```python
text = "Hello World"
print(text.lower())
print(text.upper())
print(text.title())
```

**Say:**
“Case conversion is often step one in matching. If user types `PYTHON`, we still want to detect `python`.”

### 3.3 Immutability (critical concept)

**Type:**

```python
original = "Hello"
result = original.lower()

print(original)
print(result)
```

**Say:**
“Strings are immutable, which means we cannot change characters in place. Methods return a new string. If you don’t assign the result, your variable stays unchanged.”

**Type:**

```python
name = "  Alice  "
name.strip()
print(name)  # still has spaces
```

Then fix:

```python
name = name.strip()
print(name)
```

### 3.4 Whitespace cleanup with `strip`

```python
raw = "   hello   "
print(raw.strip())
print(raw.lstrip())
print(raw.rstrip())
```

**Say:**
“`strip()` cleans edges, not the middle. That distinction matters in our lab.”

### 3.5 Replacement with `replace`

```python
message = "I like cats. Cats are great!"
print(message.replace("cats", "dogs"))
```

**Say:**
“`replace` is case-sensitive and returns a new string.”

### 3.6 Search with `find` and membership with `in`

```python
sentence = "Hello, Python!"
print(sentence.find("Python"))
print(sentence.find("Java"))
print("Python" in sentence)
```

**Say:**
“`find` returns a position or `-1` if missing. Use `in` for clean True/False checks. Use `find` when you need exact location.”

---

## 4) Live Demo Script (5–10 minutes)

## Demo A: Normalization pipeline

**Say:**
“Let’s clean messy input in a reproducible sequence.”

```python
raw_input = "   HELLO world   "
cleaned = raw_input.strip().lower()

print(f"Before: '{raw_input}'")
print(f"After:  '{cleaned}'")
```

**Expected output:**

```text
Before: '   HELLO world   '
After:  'hello world'
```

## Demo B: Multiple-space normalization (important accuracy fix)

**Say this explicitly:**
“Runbook mentions replacing multiple spaces with one. A single `.replace("  ", " ")` is not enough for cases with 3 or more spaces. We need a repeat-until-clean pattern.”

```python
messy = "Python    is      great"
cleaned = messy.strip().lower()

while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")

print(f"Original: '{messy}'")
print(f"Cleaned:  '{cleaned}'")
```

**Expected output:**

```text
Original: 'Python    is      great'
Cleaned:  'python is great'
```

**Instructor emphasis:**
“This handles 2 spaces, 3 spaces, 8 spaces—any run of spaces.”

## Demo C: `find()` returning -1

```python
email_1 = "student@example.com"
email_2 = "nosymbol.example.com"

print(email_1.find("@"))
print(email_2.find("@"))

if email_2.find("@") == -1:
    print("Missing @ symbol")
```

---

## 5) Guided Lab: Text Sanitizer (25–35 minutes)

## 5.1 Lab instructions (read aloud)

“You will build a text sanitizer script. The script should accept a sentence and keyword, clean the sentence, and report keyword presence.”

### Required behavior

1. Input a sentence.
2. Input a keyword.
3. Normalize sentence with:
   - `strip()`
   - `lower()`
   - collapse multiple internal spaces to a single space (must work for 3+ spaces)
4. Normalize keyword with `strip().lower()`.
5. Print cleaned sentence.
6. Print whether keyword exists (`True/False`).

### Example interaction

```text
Enter a sentence:    Python    IS      great   
Enter keyword to find:  is
Cleaned: 'python is great'
Keyword 'is' found: True
```

### Completion criteria

- Cleaned output is normalized and readable.
- Multiple spaces are fully collapsed (3+ handled).
- Keyword detection is correct.
- Script runs end-to-end.

## 5.2 Scaffolded starter

```python
sentence = input("Enter a sentence: ")
keyword = input("Enter keyword to find: ")

cleaned = sentence.strip().lower()

# TODO: collapse 2+ spaces repeatedly until stable

keyword_clean = keyword.strip().lower()
found = keyword_clean in cleaned

print(f"Cleaned: '{cleaned}'")
print(f"Keyword '{keyword_clean}' found: {found}")
```

## 5.3 Reference solution

```python
# Text Sanitizer (Hour 6)
sentence = input("Enter a sentence: ")
keyword = input("Enter keyword to find: ")

# Normalize sentence
cleaned = sentence.strip().lower()

# Collapse runs of spaces (works for 3+ spaces too)
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")

# Normalize keyword
keyword_clean = keyword.strip().lower()

# Containment check
found = keyword_clean in cleaned

# Output
print(f"Cleaned: '{cleaned}'")
print(f"Keyword '{keyword_clean}' found: {found}")
```

## 5.4 Facilitation timeline

- **Minute 5 of lab:** “Everyone should have sentence + keyword input complete.”
- **Minute 10:** “Make sure `.strip().lower()` is applied to sentence.”
- **Minute 15:** “Add the while-loop for multi-space collapse.”
- **Minute 22:** “Normalize keyword and perform containment check.”
- **Minute 30:** “Test with sentence containing 5+ spaces between words.”

## 5.5 Test cases to project

1. Input: `"   HELLO    world   "`, keyword `"world"` → found `True`
2. Input: `"Python      basics"`, keyword `"advanced"` → found `False`
3. Input: `"   DATA   CLEANING   "`, keyword `"data"` → found `True`
4. Input: `"one two"`, keyword `" three "` → found `False`

---

## 6) Common Pitfalls and Teaching Responses

### Pitfall 1: expecting in-place modification

```python
text = "hello"
text.replace("e", "a")
print(text)  # still 'hello'
```

**Response:** “Assign it back: `text = text.replace(...)`.”

### Pitfall 2: incorrect `find` condition

```python
pos = "abc".find("a")
if pos:
    print("Found")
```

**Why wrong:** `pos` can be `0`, and `0` is falsy.

**Fix:**

```python
if pos != -1:
    print("Found")
```

### Pitfall 3: partial space cleanup

```python
cleaned = cleaned.replace("  ", " ")
```

**Issue:** one pass may leave double spaces after collapsing larger runs.

**Fix:** use loop:

```python
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")
```

### Pitfall 4: forgetting keyword normalization

**Fix reminder:** `keyword_clean = keyword.strip().lower()`.

---

## 7) Quick Checks / Exit Ticket (6 minutes)

Ask and discuss briefly:

1. “Why do we assign back after calling string methods?”
2. “When do we use `in` instead of `find()`?”
3. “What does `find()` return when target is missing?”
4. “How do we reliably collapse 3+ spaces into one?”

**Expected highlights:**
- Strings are immutable.
- `in` for boolean presence, `find` for location.
- Missing means `-1`.
- Use a loop with `replace("  ", " ")` until stable.

---

## 8) Transition Script to Hour 7

“Excellent. You can now clean and search text reliably. In Hour 7, we’ll connect this to user interaction: collecting input, converting to numbers with `int()` and `float()`, and producing correct numeric calculations.”

---

## 9) Extended Verbatim Teaching Script (for deeper pacing)

“Let’s emphasize a powerful beginner pattern: normalize first, analyze second. If case and spaces are inconsistent, your checks become unreliable. For example, if one learner types `PYTHON`, another types ` python `, and a third types `Python`, we still want one consistent internal format for logic. That is why we use `.strip().lower()` so often.

Now, immutability can feel strange at first. You might think calling a method changes the original string. It does not. In Python, strings are immutable objects. Methods return a new value. This design prevents accidental side effects and makes behavior predictable. It also means your assignment line is not optional; it is required.

`replace` is deceptively simple. Beginners often use it once and assume all spacing problems are solved. But when there are long runs of spaces, one pass may not fully normalize text. That is why we introduced a small loop. It’s still Basics-level and very practical.

`find` gives us location data; `in` gives us a direct yes/no answer. A great rule is: if you only need True/False, use `in` for readability. If you need index position for slicing, use `find`.

As you practice today, I want you to build one skill beyond syntax: verification. Don’t trust one test input. Test with normal input, messy input, and a negative case. In professional work, robust behavior on varied input matters more than one perfect demo.

Let’s walk through a model debugging thought process for this lab. If your keyword search fails unexpectedly, first print the cleaned sentence and cleaned keyword with quotes. Quotes reveal hidden spaces. Then check casing. Then check spelling. This simple process solves most beginner string bugs.

Finally, remember we are still in Basics scope. We are intentionally not using regex yet. You can do useful cleaning with just methods and a loop. That is a great foundation and exactly what we want today.”

---

## 10) Optional Extensions (if time remains, still Basics)

1. Count keyword occurrences with `.count()`.
2. Add title-case output for display after cleaning.
3. Print the first index of keyword if found.

### Extension example

```python
sentence = "python python basics"
keyword = "python"

count = sentence.count(keyword)
first_pos = sentence.find(keyword)

print(f"Count: {count}")
print(f"First position: {first_pos}")
```

---

## 11) Instructor FAQ

**Q: Why not use regex for multiple spaces?**  
A: Regex is useful later, but out of scope for Basics. The loop pattern is clear and sufficient now.

**Q: Does `strip()` remove punctuation?**  
A: No, only leading/trailing whitespace by default.

**Q: Why use lowercase for keyword checks?**  
A: To make comparison case-insensitive.

**Q: Can `.replace()` remove all spaces?**  
A: Yes with `.replace(" ", "")`, but that removes word boundaries too. Use carefully.

---

## 12) Observation Rubric (informal)

- **Meets:** full cleanup + correct keyword detection + clear output
- **Almost:** keyword check correct but spacing cleanup incomplete
- **Needs support:** confusion about immutability or `find` logic

---

## 13) Scope Guardrails

Keep in scope:
- strings + methods
- basic loops for cleanup
- containment checks

Out of scope:
- regex
- NLP libraries
- file-based processing pipelines

---

## 14) Close (60-second script)

“Today you learned one of the most practical workflows in Python: normalize text, then search it. You can now use methods intentionally, avoid immutability mistakes, and handle messy spacing robustly—including long runs of spaces. In Hour 7, we’ll combine text handling with numeric input conversion to build accurate interactive scripts.”

---

## 15) Additional practice prompts for homework / spare minutes

1. Clean a product title string with inconsistent spaces and case.
2. Check if a sentence contains any of three keywords using `in`.
3. Find the first position of `"@"` in several emails.
4. Convert names to title case for display but keep lowercase for matching.
5. Replace all hyphens with spaces and normalize spacing.
6. Build a tiny phrase cleaner that trims and collapses spaces.
7. Explain, in one sentence, why strings are immutable.
8. Predict output of five method chains before running.
9. Identify bug in code where `replace` result is not assigned.
10. Create a two-line report: cleaned text + keyword found.

These prompts are included so this file remains a complete, instructor-ready packet for Hour 6.

---

## 16) Appendix A — Extended Minute-by-Minute Delivery Script

### 00:00–00:04 Reconnect and intent

“Welcome back. Last hour we accessed text by position. This hour we clean and search text. In real scripts, messy text is normal. Your skill today is to make messy text consistent before making decisions.

Open a new file named `hour6_text_sanitizer.py`. Keep terminal and editor side-by-side so you can run often.”

### 00:04–00:08 Core workflow framing

“Today we will use a repeatable pattern:
1. capture text,
2. normalize text,
3. inspect or search text,
4. report clear results.

If you remember this pipeline, you can solve many beginner text tasks confidently.”

### 00:08–00:12 Method demonstration with predictions

“Type:

```python
sample = "  PyTHon Basics  "
print(sample.lower())
print(sample.upper())
print(sample.strip())
```

Before running each line, predict output. Prediction is deliberate practice. Strong debugging starts with prediction.”

### 00:12–00:16 Immutability checkpoint

“Now type this exactly:

```python
text = "  HELLO  "
text.strip()
print(f"'{text}'")
```

What happened? Spaces remained. Why? Because strings are immutable. `strip()` produced a new string we didn’t store.

Now fix:

```python
text = text.strip()
print(f"'{text}'")
```

Repeat this phrase: methods return new strings.”

### 00:16–00:20 `replace` and case sensitivity

“Type:

```python
msg = "Cats and cats"
print(msg.replace("cats", "dogs"))
```

Only lowercase `cats` changes. Case sensitivity matters. We usually normalize case first for consistent behavior.”

### 00:20–00:24 `find` vs `in`

“Type:

```python
line = "Learning Python is fun"
print(line.find("Python"))
print(line.find("Java"))
print("Python" in line)
```

Use `in` for boolean checks. Use `find()` when position is needed for slicing or diagnostics.”

### 00:24–00:28 Multiple-space normalization emphasis

“Now the important robustness fix for this hour: collapsing spaces must handle 3+ spaces. One replace pass is not enough in all cases.

Type:

```python
messy = "A    B      C"
cleaned = messy
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")
print(cleaned)
```

This loop is still Basics-level and reliable.”

### 00:28–00:32 Lab briefing

“You’ll create a text sanitizer with sentence input and keyword search. Required behavior includes trimming, lowercasing, collapsing extra spaces fully, and keyword detection.”

### 00:32–00:40 Lab support checkpoint 1

“Make sure everyone has sentence input working. Then normalize with `.strip().lower()`. Print in quotes while debugging so hidden spaces become visible.”

### 00:40–00:46 Lab support checkpoint 2

“Add the `while` loop for space collapse and test with intentionally messy input containing long runs of spaces.

If output still has doubles, print each iteration to observe changes.”

### 00:46–00:52 Lab support checkpoint 3

“Normalize keyword with `.strip().lower()`. Use `in` for containment. Verify with one true case and one false case.”

### 00:52–00:56 Debrief

“Who can explain in one sentence why we assigned back after each method call? Who can explain why looped replace works for 3+ spaces?”

### 00:56–01:00 Exit ticket and transition

“Exit ticket:
1. Why does `find()` return `-1`?
2. What’s the simplest boolean membership check?
3. Why can one replace pass be insufficient?

Great work. Next hour we connect user input and numeric conversion.”

---

## 17) Appendix B — Extra Lab Variants (Basics Scope)

### Variant 1: Name cleaner

Prompt: Clean a full name and print display version in title case.

```python
full_name = input("Enter full name: ")
cleaned = full_name.strip().lower()
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")

display_name = cleaned.title()
print(f"Stored:  '{cleaned}'")
print(f"Display: '{display_name}'")
```

### Variant 2: Product title normalizer

```python
title = input("Product title: ")
cleaned = title.strip().lower()
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")
print(f"Normalized title: '{cleaned}'")
```

### Variant 3: Keyword index reporter

```python
text = input("Sentence: ").strip().lower()
while "  " in text:
    text = text.replace("  ", " ")
keyword = input("Keyword: ").strip().lower()

pos = text.find(keyword)
if pos != -1:
    print(f"Found at index {pos}")
else:
    print("Not found")
```

### Variant 4: Duplicate-space detector

```python
raw = input("Enter text: ")
if "  " in raw:
    print("Contains repeated spaces")
else:
    print("No repeated spaces")
```

### Variant 5: Count occurrences

```python
text = input("Sentence: ").strip().lower()
keyword = input("Keyword: ").strip().lower()
print(f"Count: {text.count(keyword)}")
```

---

## 18) Appendix C — Dialogue Prompts for Struggling Learners

Use these prompts one at a time:
- “What do you think your variable contains right now? Print it with quotes.”
- “Did you assign method output back to the same variable?”
- “Can you test with one tiny sentence first?”
- “What should happen if keyword is absent?”
- “Does your space cleanup still work with six spaces?”

This keeps support process-focused without giving away full answers.

---

## 19) Appendix D — Instructor Reflection and Calibration Notes

After class, capture quick notes:
1. Did learners internalize immutability language?
2. Did they overuse `find` for boolean checks?
3. Did they implement the while-loop correctly for multi-space normalization?
4. Were outputs clear and labeled?
5. What support sentence worked best for unblocking learners?

Use these notes to tune Hour 7 pacing.

---

## 20) Appendix E — Extended Troubleshooting and Coaching Map

### Case A: learner says “my cleaned text still has weird spaces”

Use this script:
1. “Print `cleaned` inside quotes.”
2. “Run one pass replace and inspect.”
3. “Add loop until no double spaces remain.”
4. “Re-test with 6 spaces between words.”

### Case B: learner says “find says not found but I can see the word”

Use this script:
1. “Print both strings in lowercase.”
2. “Check for leading/trailing spaces in keyword.”
3. “Use `repr()` or quoted f-string output.”

### Case C: learner used `if pos:` after `find`

Explain quickly:
- `0` means found at start, but `0` is falsy.
- correct check is `pos != -1`.

### Case D: learner chains methods but forgets assignment

Show pattern:

```python
cleaned = raw.strip().lower()
```

Remind: “No assignment, no persistent change.”

---

## 21) Appendix F — Extended Verbatim Mini-Lecture (reinforcement mode)

“Text normalization is one of the most transferable beginner skills in programming. You see it in forms, logs, user commands, CSV imports, and chat processing. The exact tools may evolve, but the thinking pattern remains stable.

A common beginner frustration is ‘my code looks right, but result is wrong.’ Usually this means hidden input variability—extra spaces, inconsistent case, punctuation, or missing markers. Normalization narrows that variability so logic can succeed.

Let’s revisit immutability with an analogy: if a string is a printed sheet, methods like `lower()` produce a new printed sheet rather than editing ink on the old one. You must choose which sheet to keep by assignment.

Now consider readability. Compare:
- `if sentence.find(keyword) != -1:`
- `if keyword in sentence:`
Both are valid, but the second is more readable for boolean checks. Readability is not only style; it reduces bugs and review time.

The while-loop for spaces is an example of progressive cleanup. We repeatedly apply a small rule until no violation remains. This is a powerful idea you will reuse in future topics, including data cleaning and debugging loops.

I also want to emphasize testing strategy. A single passing test means little. Use three categories:
1. normal input,
2. messy but valid input,
3. missing keyword case.

When all three pass, confidence rises significantly.

As we move to Hour 7, remember that clean text and clean numbers often meet in the same script. You might sanitize a user command and also convert numeric values from input. Foundations combine quickly.”

---

## 22) Appendix G — Additional Practice Set with Answers

### Q1: Normalize and count words (simple split preview avoided in core)

```python
text = "  PYTHON    basics   class  "
cleaned = text.strip().lower()
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")
print(cleaned)
```

### Q2: Determine if email likely has `@`

```python
email = input("Email: ").strip().lower()
has_at = "@" in email
print(f"Contains @: {has_at}")
```

### Q3: Replace delimiter style

```python
code = "A-B-C-D"
print(code.replace("-", " "))
```

### Q4: First position report

```python
text = "learn python basics"
pos = text.find("python")
print(pos)
```

### Q5: Robust cleaner function

```python
text = "  HELLO     WORLD  "
cleaned = text.strip().lower()
while "  " in cleaned:
    cleaned = cleaned.replace("  ", " ")
print(cleaned)
```

---

## 23) Appendix H — Instructor Reflection Prompts (expanded)

- Which explanation of immutability landed best?
- Did learners naturally choose `in` for boolean checks?
- Did they understand why looped replace is needed for 3+ spaces?
- Did most learners test false-case keyword search?
- What should be revisited briefly at start of Hour 7?

---

## 24) Appendix I — Rapid-Fire Q&A + Scenario Bank

Use these during the last 10 minutes or as warm-up next class.

### Concept checks

1. Why do string methods often require assignment?
2. What is the difference between `strip()` and `replace(" ", "")`?
3. What does `find()` return when not found?
4. Why is `if pos:` risky after `find()`?
5. When is `in` preferable to `find()`?

### Scenario checks

- Scenario A: Input is `"   HELLO   WORLD   "`. Produce `"hello world"`.
- Scenario B: Input is `"A      B"`. Ensure one space remains.
- Scenario C: Keyword has accidental spaces around it. How to fix?

### Verbatim coaching passage

“When you feel stuck in text cleaning, return to pipeline thinking: normalize, inspect, test, then search. Print intermediate values with quotes to expose hidden spaces. Use lowercase normalization before containment checks if case-insensitive behavior is expected. And remember, one successful test does not prove robustness; test with messy input deliberately.”

### Additional micro-drills

```python
line = "   Data    Cleaning   Basics   "
clean = line.strip().lower()
while "  " in clean:
    clean = clean.replace("  ", " ")
print(clean)
```

```python
text = "python basics"
print(text.find("python"))  # 0
print("python" in text)      # True
```

```python
keyword = "  BASICS "
print(keyword.strip().lower())
```

Use these to consolidate technique and vocabulary without leaving Basics scope.

---

## 25) Appendix J — Final Reinforcement Notes

Instructor reminder script:
“Hour 6 is successful when learners can turn messy text into predictable text and explain each normalization step. Keep repeating the sequence: strip edges, normalize case, collapse repeated spaces, then search.”

Mini-practice block:

```python
raw = "   PYTHON      Course   Basics  "
clean = raw.strip().lower()
while "  " in clean:
    clean = clean.replace("  ", " ")
print(clean)
print("course" in clean)
```

Use this as a fast recap before Hour 7.

---

## 26) Appendix K — Instructor Micro-Workshop Script (15-minute optional)

If you need extra reinforcement before moving forward, run this micro-workshop.

“Open your file and create a new section called `practice_block`.

First task: normalize this exact string: `"   PYTHON      makes    SENSE   "`.

Expected final cleaned value: `"python makes sense"`.

Second task: check whether `"sense"` appears in the cleaned text.

Third task: print first position of `"makes"` using `find()`.

Fourth task: replace `"makes"` with `"teaches"` and print new sentence.

Fifth task: explain, in one sentence, why assignment is needed after each method call.

Now let’s code it step by step together.”

```python
raw = "   PYTHON      makes    SENSE   "
clean = raw.strip().lower()
while "  " in clean:
    clean = clean.replace("  ", " ")

print(clean)
print("sense" in clean)
print(clean.find("makes"))
print(clean.replace("makes", "teaches"))
```

“Notice how one cleaned variable supports multiple operations. That is why normalization early in the script is powerful: it simplifies all downstream logic.

Now pair up and explain your code line-by-line to a partner. Teaching someone else is one of the fastest ways to strengthen your understanding.”

Additional recap script:
“Normalize first, then search. If a result is surprising, print intermediate values in quotes. Keep checks in Basics scope and prefer clear code over compressed one-liners.”

Instructor final reminder:
“Before ending Hour 6, run one final live test with deliberately messy input that includes mixed case, leading spaces, trailing spaces, and long runs of internal spaces. Ask learners to predict the cleaned output before running. Then run the script and compare prediction to result. This quick final cycle reinforces correctness thinking and gives immediate confidence. Encourage learners to explain each transformation line aloud: strip removes edge whitespace, lower normalizes case, while-loop collapses repeated internal spaces, and containment checks verify keyword presence. When learners can narrate that pipeline clearly, they have achieved the objective of this hour.”

Closing checklist for learners:
- I can explain immutability in one sentence.
- I can normalize text with strip + lower.
- I can collapse repeated spaces with a loop that works for 3+ spaces.
- I can use `in` for presence and `find()` for position.
Final note: practice with at least three messy sentences tonight.
