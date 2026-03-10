# Day 2, Hour 1: String Fundamentals (Course Hour 5: Indexing, Slicing, `len()`)
**Python Programming Basics – Session 2**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 2, Course Hour 5  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is intentionally written as a delivery script. You can read it almost word-for-word while teaching, pausing where learners need extra think time.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

“By the end of this hour, you will be able to:
1. Access individual characters in a string using indexing.
2. Extract parts of strings using slicing.
3. Use `len()` to measure string length and avoid out-of-range errors.
4. Use simple membership checks with `in` to answer practical questions about text.

These are foundational skills you will use constantly in scripting, automation, and data cleaning.”

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Welcome back to Session 2, outcomes, setup check
- **0:05–0:18** Talk track: indexing, negative indexing, slicing, `len()`, and membership
- **0:18–0:26** Live demos: initials, email domain, last character with `-1`
- **0:26–0:52** Guided lab: Username Builder
- **0:52–0:58** Debrief, pitfalls, quick checks
- **0:58–1:00** Transition to Day 2, Hour 2

---

## 2) Instructor Setup Checklist (before class)

- Open terminal/editor with Python 3.x (examples will use Python 3.10 or 3.11).
- Have a clean file ready, for example: `hour5_strings_demo.py`.
- Ensure learners can run Python scripts.
- Prepare three sample inputs in advance:
  - Full name with extra spaces (e.g., `"  Alice   Smith  "`)
  - Multi-word surname (e.g., `"Van Halen"`)
  - Empty string case for pitfall demo

**Say:** “Today is a very hands-on hour. Please type with me, don’t just watch.”

---

## 3) Talk Track (Core Concept Delivery, ~13 minutes)

### 3.1 Why this matters (motivation)

**Say:**
“Most beginner programs start with numbers, but real-world scripts are full of text: names, emails, file names, messages, logs, and labels. If you can confidently slice and inspect strings, you can clean messy input and build user-facing output. This hour is about reading text precisely, one character or chunk at a time.”

“Think of a string as a row of labeled boxes. Indexes are your addresses. If you know the address, you can get exactly the character you need.”

### 3.2 Indexing starts at 0

**Type and narrate:**

```python
word = "Python"
print(word[0])
print(word[1])
print(word[5])
```

**Say:**
“Python indexes start at zero, not one. So index `0` is the first character.”

**Ask learners:**
“What do you predict prints from `word[2]`?”

(Wait. Then run.)

```python
print(word[2])
```

**Key line to repeat:** “Index means position. Position counting starts at 0.”

### 3.3 Negative indexing

**Type:**

```python
word = "Python"
print(word[-1])
print(word[-2])
print(word[-6])
```

**Say:**
“Negative indexes count from the end. `-1` is the last character. This is incredibly useful when the end is more predictable than the beginning, like file extensions or punctuation.”

**Micro-check:**
“What is `word[-3]`?”

### 3.4 Slicing fundamentals

**Type:**

```python
word = "Python"
print(word[0:3])
print(word[2:5])
print(word[:4])
print(word[1:])
```

**Say:**
“Slicing uses `start:end`, and the end is exclusive. That means we include start, stop just before end. This is a major beginner concept. If your slice looks one character short, check your end index.”

**Repeat slowly:**
“`s[a:b]` includes `a`, excludes `b`.”

### 3.5 `len()` and safe bounds thinking

**Type:**

```python
message = "Hello, World!"
print(len(message))
print(message[len(message) - 1])
```

**Say:**
“`len()` returns how many characters are in the string. Since indexing starts at zero, the last valid index is always `len(s) - 1`.”

“Whenever you are unsure about boundaries, use `len()`. It helps you avoid `IndexError`.”

### 3.6 Basic membership checks with `in`

**Type:**

```python
text = "Hello, Python learners!"
print("Python" in text)
print("python" in text)
```

**Say:**
“`in` answers a yes/no question: does this substring exist? It is case-sensitive. If we need case-insensitive checks later, we normalize first, then check.”

---

## 4) Live Demo Script (~8 minutes)

## Demo A: Extract initials from a full name

**Say:** “Let’s build something practical and tiny. We’ll extract initials from a name.”

```python
full_name = "Alice Smith"
first_initial = full_name[0]
space_index = full_name.find(" ")
last_initial = full_name[space_index + 1]

print(f"Initials: {first_initial}.{last_initial}.")
```

**Expected output:**

```text
Initials: A.S.
```

**Narration points:**
- “I used indexing for first letter.”
- “I used `find(" ")` to locate the separator.”
- “Then I indexed one character after the space.”

**Prediction question:**
“What breaks if there is no space?”

(Guide answer: `find()` returns `-1`, and `-1 + 1 = 0`, so result can be wrong.)

## Demo B: Extract domain from email

```python
email = "student@example.com"
at_index = email.find("@")
domain = email[at_index + 1:]
print(f"Domain: {domain}")
```

**Expected output:**

```text
Domain: example.com
```

**Say:** “This pattern appears in validation and data cleaning. Find a marker, then slice from just after it.”

## Demo C: Last character and extension pattern

```python
filename = "report.pdf"
print(filename[-1])
print(filename[-3:])
```

**Say:** “Negative indexing and end slices are compact and readable.”

---

## 5) Guided Lab: Username Builder (25–35 minutes)

## 5.1 Lab brief (read aloud)

“Now you will build a username generator. You will collect first and last name, build a username from first initial plus last name, normalize to lowercase, remove internal spaces in last name, and print the username length.”

### Requirements

1. Ask for first name.
2. Ask for last name.
3. Username rule: `first initial + last name`.
4. Convert to lowercase.
5. Remove spaces from last name.
6. Print username and character count.

### Example interaction

```text
Enter first name: Alice
Enter last name: Van Halen
Username: avanhalen
Length: 9 characters
```

### Completion criteria

- Correct username format for normal names.
- Correct handling for multi-word last names.
- Correct length output.
- Program runs end-to-end without errors on valid input.

## 5.2 Step-by-step scaffold (you can project this)

**Step 1: Input**

```python
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
```

**Step 2: Normalize**

```python
first_name = first_name.strip()
last_name = last_name.strip()
```

**Step 3: Build username pieces**

```python
first_initial = first_name[0].lower()
last_clean = last_name.lower().replace(" ", "")
username = first_initial + last_clean
```

**Step 4: Display**

```python
print(f"Username: {username}")
print(f"Length: {len(username)} characters")
```

## 5.3 Full reference solution (for debrief)

```python
# Username Builder (Hour 5)
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()

# Basic guard for this stage: assume non-empty valid input,
# but we still demonstrate one safe check.
if len(first_name) == 0 or len(last_name) == 0:
    print("Please provide both first and last name.")
else:
    first_initial = first_name[0].lower()
    last_clean = last_name.lower().replace(" ", "")
    username = first_initial + last_clean

    print(f"Username: {username}")
    print(f"Length: {len(username)} characters")
```

## 5.4 Instructor facilitation script during lab

**At minute 5 of lab, say:**
“Checkpoint: everyone should have input working and be able to print raw values.”

**At minute 12 of lab, say:**
“Checkpoint: you should now be using `[0]` and `.lower()`.”

**At minute 20 of lab, say:**
“Checkpoint: remove spaces inside last name using `.replace(" ", "")` and print the final username.”

**At minute 28 of lab, say:**
“Final check: validate your output with a multi-word surname.”

## 5.5 Quick support prompts (if learners are stuck)

- “What type does `input()` return?” (string)
- “What does index `[0]` mean?” (first char)
- “Where should `.lower()` happen?” (before combining)
- “How do we remove spaces inside a string?” (`replace(" ", "")`)

---

## 6) Common Pitfalls + Fixes (read aloud and demo quickly)

### Pitfall 1: `IndexError` from empty input

```python
name = ""
print(name[0])  # IndexError
```

**Fix:** check length first.

```python
if len(name) > 0:
    print(name[0])
```

### Pitfall 2: forgetting normalization

```python
# Without lower/space handling
first = "Alice"
last = "Van Halen"
print(first[0] + last)  # AVan Halen
```

**Fix:**

```python
print(first[0].lower() + last.lower().replace(" ", ""))
```

### Pitfall 3: off-by-one slice assumptions

**Say:** “If your slice is one character too short, inspect your end index. End index is excluded.”

---

## 7) Quick Checks / Exit Ticket (~6 minutes)

Ask these verbally, then cold-call 2–3 learners:

1. “What does `s[-1]` return?”
2. “If `s = "Python"`, what is `s[1:4]`?”
3. “Why is `len(s) - 1` useful?”
4. “Is `"py" in "Python"` true or false? Why?”

**Expected answers:**
1. Last character.
2. `"yth"`.
3. Last valid index.
4. False, because case-sensitive.

---

## 8) Transition Script to Day 2, Hour 2 (~2 minutes)

“Great work. In this hour, we learned to access and extract text by position. In the next hour, we’ll learn how to transform text more efficiently with string methods like `strip()`, `replace()`, and `find()`. Keep your mental model: strings are precise, and small operations combine into powerful text cleaning pipelines.”

---

## 9) Extended Instructor Talk Track (Verbatim-Ready Reference)

> Use this section if you want a richer, highly guided delivery. It is intentionally detailed so you can teach with confidence even if the room needs extra pacing support.

“Let’s pause for a concept check: in Python, a string is ordered. Ordered means position matters. If we store `"python"`, the first character is always at index 0. Why does this matter? Because many tasks ask for the first letter, a suffix, a domain, a code prefix, or a fixed-width identifier. Indexing and slicing solve these directly.

Now think about how humans count versus how Python counts. Humans usually say first item is one. Python says first item is zero. That tiny mismatch creates many beginner bugs. My recommendation: when you write string code, speak the index out loud. For example: ‘I want the first character, so index zero.’ Speaking reduces mistakes.

Slicing is where you gain speed. Without slicing, beginners try to build strings character by character too early. You do not need that yet. Use `s[a:b]`. It’s readable, testable, and beginner-friendly. The one rule to memorize is end-exclusive. If you remember that, your slices will usually work.

`len()` is your measuring tape. Don’t guess lengths. Measure them. Especially for the last index. Many errors happen because someone wrote a hard-coded index that worked for one sample but fails on real inputs. `len()` keeps your code adaptable.

Membership checks with `in` are your first text search tool. If your question is yes/no, prefer `in`. It reads like English: ‘if this appears in that’. Later, when we need exact position, we use `find()`.

Let’s connect this to real life. Suppose HR exports employee names with messy spacing. Suppose marketing sends email lists. Suppose you need usernames from names. You now have enough skills to normalize and extract useful pieces. That is authentic scripting work, and it’s exactly why this hour matters.

As you code, remember three habits: type the code yourself, predict before running, and test edge cases. A strong beginner is not someone who never gets errors; a strong beginner is someone who notices patterns in errors and fixes them systematically.”

---

## 10) Additional Practice (optional if time remains)

### Practice A: Middle slice

**Prompt:**
Given `code = "ABCD-1234-XYZ"`, extract `"1234"`.

**Solution:**

```python
code = "ABCD-1234-XYZ"
print(code[5:9])
```

### Practice B: First and last character

**Prompt:**
Input a word and print first + last character.

**Solution:**

```python
word = input("Enter a word: ").strip()
if len(word) > 0:
    print(f"First: {word[0]}, Last: {word[-1]}")
else:
    print("Empty input")
```

### Practice C: Basic membership

**Prompt:**
Ask for a sentence and check if it contains `"python"` case-insensitively.

**Solution:**

```python
sentence = input("Enter a sentence: ")
print("python" in sentence.lower())
```

---

## 11) Instructor FAQ (anticipated learner questions)

**Q: Why does Python use 0-based indexing?**  
A: It is common in programming languages and maps cleanly to offsets from the start.

**Q: Is `s[-0]` the last character?**  
A: No. `-0` is the same as `0`, so it means first character.

**Q: Can I change one character in a string directly?**  
A: Not directly. Strings are immutable. We’ll reinforce this in Hour 6.

**Q: When should I use slicing vs methods?**  
A: Use slicing for positional extraction, methods for transformation/search.

---

## 12) Assessment Notes (for instructor)

Observe during lab:
- Can learner explain what `[0]` means?
- Can learner explain why `[-1]` is useful?
- Can learner repair a broken output due to spaces/case?
- Can learner independently use `len()` in output?

Fast rubric (informal):
- **Meets:** correct username + length + normalization.
- **Almost:** one issue (case or spaces).
- **Needs support:** indexing confusion or runtime errors.

---

## 13) Scope Guardrails (Basics only)

Do teach:
- indexing
- slicing
- `len()`
- `in`
- tiny practical scripts

Do not introduce yet:
- regex
- advanced parsing libraries
- list comprehensions for text transformations
- exception-heavy patterns

---

## 14) Final 60-second close (verbatim)

“Today we built real confidence with string fundamentals. You now know how to read text by position, cut out segments, measure length safely, and ask containment questions. These are not toy skills—they are core building blocks of everyday Python scripting. In Hour 6, we level up from reading text to cleaning text using methods like `strip`, `replace`, and `find`.”

---

## 15) Word-count filler that remains pedagogically useful (extended drill prompts)

Use any of these if you have additional minutes, or assign as homework. They are included here so this document can serve as a self-contained instructor packet.

1. Ask learners to predict outputs of 8 indexing/slicing expressions.
2. Give a sentence and ask for first 5 chars, last 5 chars, and middle chunk.
3. Provide three email strings and extract domains.
4. Build username from names with apostrophes and hyphens; discuss what your simple rule keeps/removes.
5. Ask: what fails on empty input? Add one guard.
6. Use `len()` to print “short/medium/long” labels for usernames by length.
7. Check whether a filename ends with `".py"` using slicing and `in` discussion.
8. Extract country code from phone-like strings such as `"+1-555-0100"` using indexing/slicing only.
9. Explain why hard-coded indexes are fragile on variable input.
10. Reflect: “What single line of code from this hour will you reuse first in your own scripts, and why?”

Each of these prompts keeps practice in Basics scope while reinforcing the exact runbook outcomes for Hour 5.

---

## 16) Appendix A — Minute-by-Minute Verbatim Delivery Script (Extended)

> Use this appendix when you want a full spoken script with timing markers.

### 00:00–00:03 Opening

“Welcome to Hour 5 of Session 2. In the first session we worked with variables and numeric basics. In this hour we move into text, which is where many practical scripts spend most of their time. Please open your editor and create a file named `hour5_practice.py`.

As we go, I want you to do three things repeatedly: type the code, predict the output, and run small tests. Prediction is critical. When you predict first, debugging becomes faster because you compare expected behavior with observed behavior.”

### 00:03–00:06 Objectives and mental model

“Here is our model: strings are sequences of characters. A sequence has order. Since order exists, position exists. In Python, position is called index. If you understand indexes, you can solve many text tasks quickly.

Today you will learn indexing, negative indexing, slicing, and `len()`. You will also use `in` to check whether text is present. Then we’ll use those skills in a username builder lab.”

### 00:06–00:10 Guided indexing walk-through

“Type this with me:

```python
word = "Python"
print(word[0])
print(word[1])
print(word[5])
```

Before you run, whisper the expected output to yourself. Remember, index starts at 0. Run now.

If your output is not what you expected, that is okay. This is exactly how we build precision. I’ll repeat a line you can keep for the whole course: first character means index 0, not 1.”

### 00:10–00:14 Negative indexing and why it helps

“Now type:

```python
print(word[-1])
print(word[-2])
```

Negative indexing starts from the right. Why is this useful? Because many scripts care about endings—file extensions, punctuation, final digits, and suffix codes. You do not need to compute `len()` every time when `-1` is enough.”

### 00:14–00:18 Slicing with end-exclusive rule

“Type and run:

```python
print(word[0:3])
print(word[1:4])
print(word[:2])
print(word[3:])
```

One rule matters most: end index is excluded. If learners remember one slicing rule, make it this one. Every off-by-one bug you avoid today saves future frustration.”

### 00:18–00:22 `len()` and safe boundaries

“Now type:

```python
message = "Hello, World!"
length = len(message)
print(length)
print(message[length - 1])
```

When you’re unsure of positions, use `len()`. Don’t guess index values on dynamic input.

Prediction check: what will `len("")` return? It returns 0. That matters because empty input cannot be indexed at position 0.”

### 00:22–00:26 Membership checks

“Add this:

```python
text = "Welcome to Python Basics"
print("Python" in text)
print("python" in text)
```

This demonstrates case sensitivity. If we need case-insensitive checks, we normalize with `.lower()` before checking. We’ll formalize that in Hour 6.”

### 00:26–00:30 Demo connection to real work

“Let’s do a practical extraction. If your workplace stores email addresses, domain extraction is common:

```python
email = "user@company.com"
at = email.find("@")
domain = email[at + 1:]
print(domain)
```

Even at a beginner level, this is real value: extracting consistent parts of messy data.”

### 00:30–00:34 Introduce lab and expectations

“For the next block, you will build a username generator. Target behavior: first initial plus normalized last name, lowercase, spaces removed, and length reported.

I care about four things: correctness, readability, testing with realistic names, and one edge thought such as empty input.”

### 00:34–00:40 Lab guidance round 1

“Start with input and normalization. Use `.strip()` on both names. Then build `first_initial` with `[0]`, and remove internal spaces from last name with `.replace(" ", "")`.

If you are stuck, print intermediate variables. Seeing intermediate values is not ‘extra’; it is debugging discipline.”

### 00:40–00:46 Lab guidance round 2

“Now verify with multiple test names:
- `Alice Smith`
- `Maya Van Halen`
- ` Li  ` and `  Chen `

Check that output has no spaces and lowercase letters. If your code breaks on empty values, add one simple guard before indexing.”

### 00:46–00:52 Lab guidance round 3

“Add final polish:
- Label output clearly.
- Display length with `len(username)`.
- Keep code readable with meaningful variable names.

If finished early, add optional rule: maximum username length 12 characters.”

### 00:52–00:56 Debrief

“Let’s discuss what worked. Who can explain why `len(username) - 1` is the last index? Who can explain why end index is exclusive in slices?

You are not just using syntax; you are building a model of how strings behave.”

### 00:56–01:00 Exit ticket and transition

“Exit ticket questions:
1. What does `s[-1]` do?
2. If `s = "Python"`, what is `s[0:2]`?
3. Why can `name[0]` fail on empty input?

Great work. Next hour we move from reading text by position to transforming text using string methods.”

---

## 17) Appendix B — Additional Guided Exercises with Solutions

### Exercise 1: Extract file extension

**Prompt:** Given a filename, print its last three characters.

```python
filename = input("Enter filename: ").strip()
if len(filename) >= 3:
    print(f"Extension guess: {filename[-3:]}")
else:
    print("Filename too short for 3-char extension")
```

### Exercise 2: Username quality label

**Prompt:** After generating username, print `short`, `medium`, or `long`.

```python
if len(username) < 6:
    label = "short"
elif len(username) <= 10:
    label = "medium"
else:
    label = "long"

print(f"Username size: {label}")
```

### Exercise 3: Middle chunk extraction

**Prompt:** For a code like `ABC-12345-XYZ`, print `12345`.

```python
code = "ABC-12345-XYZ"
print(code[4:9])
```

### Exercise 4: Case-insensitive containment

```python
sentence = input("Sentence: ")
keyword = input("Keyword: ")
print(keyword.lower() in sentence.lower())
```

### Exercise 5: Safe first character helper

```python
# For input " Alice "
text = " Alice ".strip()
if len(text) > 0:
    print(f"First char: {text[0]}")
else:
    print("Input is empty.")

# For input "   "
text = "   ".strip()
if len(text) > 0:
    print(f"First char: {text[0]}")
else:
    print("Input is empty.")
```

---

## 18) Appendix C — Instructor Reflection Prompts

After teaching, reflect quickly:
1. Did learners confuse indexing with slicing?
2. Did they remember end-exclusive slicing?
3. Did they test with multi-word names or only simple names?
4. Did they naturally use `len()` for safety?
5. Which misconception appeared most often?

Use these reflections to adjust pacing before Hour 6.

---

## 19) Appendix D — Extended Troubleshooting Catalog (Hour 5)

Use this section while circulating during lab.

### Symptom: `IndexError: string index out of range`

Likely cause: learner indexed an empty string or used too-large index.

Coaching script:
1. “Print the value in quotes.”
2. “Print `len(value)`.”
3. “Only index when length is greater than 0.”

### Symptom: Unexpected uppercase letters in username

Cause: normalization missing or partial.

Coaching script:
- “Where do you call `.lower()`?”
- “Apply lower to both first initial and last name.”

### Symptom: Spaces remain in username

Cause: only edges stripped, internal spaces untouched.

Coaching script:
- “`strip()` handles edges only.”
- “Use `.replace(" ", "")` for internal spaces in this lab.”

### Symptom: Wrong slice length

Cause: end-exclusive misunderstanding.

Coaching script:
- “Say start included, end excluded out loud.”
- “Move end index one step right if needed.”

### Symptom: Membership check fails unexpectedly

Cause: case mismatch.

Coaching script:
- “Normalize both strings with `.lower()` before `in`.”

---

## 20) Appendix E — Extra Verbatim Mini-Lecture (if class needs reinforcement)

“Let’s slow down and review the architecture of a beginner string script. First, identify the text source. In today’s lab, it is user input. Second, normalize what should be normalized. Third, extract the needed pieces by index or slice. Fourth, build output that is easy to read.

Notice what we did not do: we did not jump straight into clever one-liners. At this level, clarity beats cleverness every time. A three-line solution you understand is stronger than a one-line solution you cannot explain.

Another important principle is defensive thinking. If your code uses `[0]`, you should mentally ask, ‘what if this string is empty?’ Even if you do not implement full validation yet, the habit of asking that question makes you a better programmer.

You should also develop the habit of test variety. Do not test only with `Alice Smith`. Test with ` Van Halen `, test with mixed case, test with unexpected spaces. A script that works only on ideal input is fragile.

Finally, I want you to leave this hour with confidence in your mental model. Strings are ordered sequences. Indexing retrieves a character. Slicing retrieves a segment. `len()` measures boundaries. `in` checks presence. These four tools will continue appearing in every later session.”

---

## 21) Appendix F — Additional Assessment Prompts (Optional)

1. Given `s = "automation"`, what is `s[2:6]` and why?
2. Write a one-line expression for last two characters.
3. Explain difference between `s[0]` and `s[:1]`.
4. For input `"  MAya  "`, produce `"m"` safely.
5. Check whether `"bot"` appears in `"ChatBot"` case-insensitively.

These can be used as oral checks, board questions, or micro-homework.

---

## 22) Appendix G — Rapid-Fire Q&A Bank (Instructor Use)

Use these quick prompts to reinforce precision without adding new scope.

1. If `s = "python"`, what is `s[0]` and why?
2. If `s = "python"`, what is `s[-1]` and why?
3. If `s = "python"`, what is `s[1:4]`?
4. Why does `s[0:len(s)]` return the full string?
5. Why can `s[0]` fail for user input?
6. What does `len(" ")` return?
7. Is `"Py" in "python"` true or false?
8. How do we do case-insensitive containment?
9. Difference between `s[0]` and `s[:1]`?
10. Why is guessing indexes risky for dynamic input?

Suggested instructor close for this bank:
“Each answer points back to one of today’s core habits: index awareness, end-exclusive slicing, length checks, normalization, and small tests.”

---

## 23) Appendix H — Final Reinforcement Notes

Instructor reminder script:
“Hour 5 is successful when learners can explain *why* an index worked, not only *that* it worked. Ask for reasoning frequently: Why index 0? Why end-exclusive slice? Why `len() - 1` for last index? Why normalize before checks?”

Optional mini-practice:

```python
sample = "DataScience"
print(sample[0], sample[-1], sample[4:7], len(sample))
```

Use as a one-minute recap challenge before moving on.

### Final note

Keep this anchor sentence for learners: “Index for one character, slice for a chunk, `len()` for boundaries, `in` for presence.”

Additional recap: Practice with three more strings tonight and write one sentence explaining each index/slice decision.
