# Day 2 — Hour 7 (Session 2): Input/Output + Type Conversion

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 2, Hour 7  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab

---

## Instructor Deliverable Script (Largely Verbatim)

> This script follows the runbook: `input()`, `int()`, `float()`, happy-path conversion, ValueError preview, and a hands-on unit converter.

---

## 0) Learning Outcomes (read aloud)

“By the end of this hour, you will be able to:
1. Explain why `input()` always returns a string.
2. Convert string input into numbers using `int()` and `float()`.
3. Build a small converter program with readable output.
4. Recognize `ValueError` and explain, at a basics level, why it appears.”

---

## 1) Agenda + Timing

- **0:00–0:05** Warm-up and outcomes
- **0:05–0:18** Talk track: input model + type conversion
- **0:18–0:26** Live demos: conversion success + ValueError preview
- **0:26–0:52** Guided lab: Unit Converter
- **0:52–0:58** Debrief + pitfalls + quick checks
- **0:58–1:00** Transition to Hour 8 checkpoint

---

## 2) Framing and Setup

Prepare file: `hour7_input_conversion.py`.

Have these sample values ready:
- Valid integers: `25`, `0`, `-3`
- Valid floats: `98.6`, `12.5`
- Invalid numeric text: `"hello"`, `"3.5"` for `int()` demo

**Say:**
“We are shifting from static scripts to interactive scripts. Today your programs will ask users for input and then do real calculations. This is where type conversion becomes essential.”

---

## 3) Talk Track (10–15 minutes)

### 3.1 The important truth about `input()`

**Type and narrate:**

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(type(name))
```

**Say:**
“`input()` always returns text, which means `str`. Even if a user types digits, Python still receives a string.”

Now show:

```python
age = input("Enter your age: ")
print(type(age))
```

**Say:**
“If `age` is text, arithmetic will fail unless we convert.”

### 3.2 Why conversion is required

```python
age = input("Enter your age: ")
# next_year = age + 1  # TypeError if uncommented
```

**Say:**
“`"25" + 1` is mixing text and number types. Python protects you with an error rather than guessing.”

### 3.3 Conversion functions

```python
age = int("25")
price = float("19.99")
print(age + 1)
print(price * 2)
```

**Say:**
“Use `int()` for whole numbers, `float()` when decimals are possible.”

### 3.4 Direct conversion from `input()`

```python
quantity = int(input("How many items? "))
temperature = float(input("Temperature in °F: "))
```

**Say:**
“This is concise and common, but remember: if input is invalid, conversion raises `ValueError`.”

### 3.5 ValueError preview (not full exception handling yet)

```python
# int("hello") -> ValueError
# int("3.5")   -> ValueError
```

**Say:**
“Today we use happy-path assumptions for practice. We preview errors now; deeper handling comes later when we formally learn debugging and exceptions.”

---

## 4) Live Demo Script (5–10 minutes)

## Demo A: Small temperature converter

```python
fahrenheit_text = input("Enter temperature in °F: ")
print(f"Raw input type: {type(fahrenheit_text)}")

fahrenheit = float(fahrenheit_text)
celsius = (fahrenheit - 32) * 5 / 9

print(f"Converted type: {type(fahrenheit)}")
print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
```

**Narration points:**
- “We inspected type before and after conversion.”
- “Math formulas need numeric types.”

## Demo B: Show `ValueError` intentionally

```python
print(int("3.5"))
```

**Say:**
“Python raises `ValueError` because `int()` expects whole-number text.”

Then show acceptable alternatives:

```python
print(float("3.5"))
print(int(float("3.5")))
```

**Say:**
“Choose conversion based on data expectations, not on what ‘works once’.”

---

## 5) Guided Lab: Unit Converter (25–35 minutes)

## 5.1 Lab instructions (read aloud)

“You will build one converter. Choose either Miles→Kilometers or Fahrenheit→Celsius. Collect user input, convert type, run formula, and print clear formatted output.”

### Required tasks

1. Print a title line.
2. Ask user for one numeric input.
3. Convert input with `float()`.
4. Apply formula.
5. Print result with units and decimal formatting.

### Formulas

- Miles to km: `km = miles * 1.60934`
- °F to °C: `celsius = (fahrenheit - 32) * 5 / 9`

### Example output A

```text
=== Miles to Kilometers Converter ===
Enter distance in miles: 10
10.0 miles = 16.09 kilometers
```

### Example output B

```text
=== Temperature Converter ===
Enter temperature in °F: 98.6
98.6°F = 37.0°C
```

### Completion criteria

- Correct conversion on test input.
- Input converted to number type.
- Output includes units and readable formatting.
- Program runs without syntax/type errors on valid input.

## 5.2 Scaffold starter code

```python
print("=== Unit Converter ===")

# TODO: ask for one numeric value
# value_text = input(...)

# TODO: convert to float
# value = float(value_text)

# TODO: apply one formula and print result
```

## 5.3 Reference solution — Miles to km

```python
print("=== Miles to Kilometers Converter ===")
miles = float(input("Enter distance in miles: "))

km = miles * 1.60934

print(f"{round(miles, 1)} miles = {round(km, 2)} kilometers")
```

## 5.4 Reference solution — °F to °C

```python
print("=== Temperature Converter ===")
fahrenheit = float(input("Enter temperature in °F: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
```

## 5.5 Optional extension (still Basics): menu without loops

```python
print("1. Miles to Kilometers")
print("2. Fahrenheit to Celsius")
choice = input("Choose (1 or 2): ")

if choice == "1":
    miles = float(input("Enter miles: "))
    km = miles * 1.60934
    print(f"{miles:.1f} miles = {km:.2f} kilometers")
elif choice == "2":
    fahrenheit = float(input("Enter °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
else:
    print("Invalid choice")
```

## 5.6 Facilitation timeline

- **Minute 5:** check everyone can collect and print raw input.
- **Minute 10:** confirm conversion to `float` is in place.
- **Minute 18:** formula applied and tested with at least one known value.
- **Minute 25:** format output with units.
- **Minute 30+:** optional menu extension or peer code read.

---

## 6) Common Pitfalls + Fixes

### Pitfall 1: forgetting conversion

```python
price = input("Price: ")
print(price * 3)  # repeats text, not numeric multiplication
```

**Fix:**

```python
price = float(input("Price: "))
print(price * 3)
```

### Pitfall 2: wrong conversion function

```python
count = int("3.5")  # ValueError
```

**Fix:** use `float` when decimals are valid.

### Pitfall 3: bad constants

**Say:**
“Double-check formulas. A correct program with wrong constants still gives wrong answers.”

### Pitfall 4: hard-to-read output

**Fix:** use f-strings with formatting.

```python
print(f"Result: {value:.2f}")
```

---

## 7) Quick Checks / Exit Ticket

Ask verbally:

1. “Why does `input()` return string by default?”
2. “What happens with `int('3.5')`?”
3. “When should we use `float()` instead of `int()`?”
4. “How can we verify variable type while debugging?”

Expected responses:
- Python cannot assume desired type.
- `ValueError`.
- Use `float` if decimals may appear.
- Print with `type(variable)`.

---

## 8) Transition to Hour 8

“You now have the full chain: collect input, convert types, compute, and format output. In Hour 8, you will demonstrate these fundamentals in a mini-assessment: the Receipt Generator checkpoint.”

---

## 9) Extended Verbatim Script (deep teaching mode)

“Let’s build an intuition that will save you hours later: data has types, and operations expect compatible types. When you read from `input()`, you are receiving raw text from the keyboard. Text is flexible but ambiguous. For example, `"25"` could represent an age, a quantity, an ID, or a label. Python does not guess your intent; you must convert intentionally.

This is actually a strength of Python. It forces clarity. If your program crashes with a type error, it is not Python being difficult; it is Python telling you that your assumptions and your data do not yet match.

I want you to adopt a mini workflow every time you write input-based code:
1. Collect raw input.
2. Convert to expected type.
3. Compute.
4. Format output.
5. Test with at least two values.

That five-step pattern is robust and beginner-friendly.

Now, about `ValueError`: if conversion fails, do not panic. Read the message and identify which value could not be converted. In this hour, we are using happy-path inputs, but we still preview the failure mode so it doesn’t feel mysterious when it appears. In a later session, we’ll formalize better handling and debugging habits.

Another habit worth building now is choosing types based on domain meaning. If the input can have decimals—temperature, price, distance—default to `float`. If it must be a whole count—like number of students—use `int`.

Let’s also discuss output readability. Clear labels and units are part of correctness. If your program prints a naked number, users may not know whether it is miles, kilometers, Fahrenheit, or Celsius. Human-friendly output is professional behavior, not an optional extra.

As you work on the lab, predict before running. If you input 10 miles, you should expect about 16 kilometers. If the result is 1600, your formula or decimal handling is likely wrong. Plausibility checks are a beginner superpower.

Finally, keep scope disciplined. We are not building full validation loops yet. We are mastering one reliable slice of the workflow at a time. Strong fundamentals now will make future topics easier and less stressful.”

---

## 10) Additional Practice (optional)

### Exercise A: Seconds to minutes

Prompt: Ask for seconds and print minutes with 2 decimals.

```python
seconds = float(input("Enter seconds: "))
minutes = seconds / 60
print(f"{seconds:.0f} seconds = {minutes:.2f} minutes")
```

### Exercise B: Currency conversion mock

Prompt: Convert USD to EUR with a fixed example rate.

```python
usd = float(input("Enter USD amount: "))
rate = 0.92
eur = usd * rate
print(f"${usd:.2f} USD = €{eur:.2f} EUR")
```

### Exercise C: Type inspector

Prompt: Print values and their types before and after conversion.

```python
raw = input("Enter a number: ")
print(raw, type(raw))
val = float(raw)
print(val, type(val))
```

---

## 11) Instructor FAQ

**Q: Why not always use `float` then?**  
A: You can for many beginner cases, but `int` communicates whole-number intent and avoids accidental fractional values.

**Q: Is `input()` ever numeric automatically?**  
A: No, it always returns string.

**Q: Can we catch errors now with `try/except`?**  
A: We can mention it briefly, but formal exception handling is outside this hour’s target.

**Q: Why do we format output decimals?**  
A: To improve readability and match domain expectations (money, measurements).

---

## 12) Informal Assessment Rubric for the Lab

- **Meets:** conversion and formula are correct, output readable, units included.
- **Almost:** minor formatting issue or one formula typo.
- **Needs support:** missing conversion or persistent type errors.

---

## 13) Scope Guardrails (Basics only)

In scope:
- `input`, `int`, `float`
- simple formulas
- f-string numeric formatting

Out of scope:
- robust exception architecture
- external libraries for units
- loop-based menus with repeated prompting

---

## 14) Final 60-second close

“Today you learned how to move from raw keyboard text to meaningful numeric results. That is one of the most important beginner transitions in programming. You can now collect input, convert it safely on the happy path, compute with formulas, and present readable outputs. In Hour 8, you’ll bring these skills together in a mini-assessment.”

---

## 15) Extra drill prompts (for homework or spare class time)

1. Build a centimeters→meters converter.
2. Build a pounds→kilograms converter.
3. Ask for two numbers and print sum, difference, and product.
4. Show type before and after conversion for both inputs.
5. Try one invalid conversion intentionally and explain the error.
6. Format three output lines with labels and units.
7. Compare int vs float behavior on the same input values.
8. Explain in one sentence why `input()` does not guess type.
9. Write a tiny script that prints “raw value + raw type.”
10. Peer review a partner’s converter for readability and correctness.

These drills keep the hour aligned with Basics outcomes while reinforcing practical confidence.

---

## 16) Appendix A — Extended Minute-by-Minute Delivery Script

### 00:00–00:04 Re-entry and purpose

“Welcome to Hour 7. You already know how to manipulate text. Now we make scripts interactive. Interactivity means users provide values at runtime, and our code must convert those values correctly before math.

Open `hour7_converter.py`. Keep your terminal visible for fast run cycles.”

### 00:04–00:08 Type model reminder

“Every value has a type. If operations and types mismatch, errors appear. `input()` always returns `str`, so numeric operations require conversion.

Repeat this sequence with me: input, convert, compute, format, verify.”

### 00:08–00:12 Demonstrate input type explicitly

“Type:

```python
raw = input("Enter a number: ")
print(raw)
print(type(raw))
```

Even if learner enters 42, type remains `str`. This is expected.”

### 00:12–00:16 Show failure first, then fix

“Now we create and then fix a type mismatch.

```python
age = input("Age: ")
# print(age + 1)  # would fail
```

Fix:

```python
age_num = int(age)
print(age_num + 1)
```

That one conversion line changes what operations are legal.”

### 00:16–00:20 `int` vs `float` decisions

“Use `int` for counts and discrete values. Use `float` for measurements and money-like values.

Type:

```python
count = int("7")
temp = float("98.6")
print(count, temp)
```

Choosing type based on domain meaning builds cleaner code.”

### 00:20–00:24 ValueError preview

“Now we intentionally trigger one error so it feels familiar.

```python
# print(int("3.5"))
# print(int("hello"))
```

`ValueError` means conversion function received text it cannot interpret for that target type.”

### 00:24–00:28 Converter demo and plausibility checks

“Run a converter with known values. If 10 miles becomes 16.09 km, result is plausible. If it becomes 1609, there’s likely a decimal or formula issue.”

### 00:28–00:32 Lab launch

“You’ll build one converter end-to-end. Keep solution simple and clean. Baseline quality beats fancy extras.”

### 00:32–00:40 Lab checkpoint 1

“Ensure everyone has prompt + conversion lines working. If stuck, print raw value and type before conversion.”

### 00:40–00:46 Lab checkpoint 2

“Add formula and verify with one known case. Use f-strings to show units and decimals.”

### 00:46–00:52 Lab checkpoint 3

“Run at least two tests: one integer-like input and one decimal input. Confirm output still looks correct.”

### 00:52–00:56 Debrief and error stories

“Ask learners to share one error and fix. This normalizes debugging as a skill.”

### 00:56–01:00 Exit ticket and transition

“Exit ticket: why does `input()` return string; what causes `ValueError`; when choose `float` over `int`?”

---

## 17) Appendix B — Additional Practice Tasks

### Task 1: Height converter (cm to inches)

```python
cm = float(input("Enter height in cm: "))
inches = cm / 2.54
print(f"{cm:.1f} cm = {inches:.2f} in")
```

### Task 2: Time converter (minutes to hours)

```python
minutes = float(input("Enter minutes: "))
hours = minutes / 60
print(f"{minutes:.0f} minutes = {hours:.2f} hours")
```

### Task 3: Bill split preview

```python
total_bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
per_person = total_bill / people
print(f"Each person pays: ${per_person:.2f}")
```

### Task 4: Distance pace checker

```python
km = float(input("Distance (km): "))
minutes = float(input("Time (minutes): "))
pace = minutes / km
print(f"Pace: {pace:.2f} min/km")
```

### Task 5: Raw/converted type report

```python
value_text = input("Enter numeric text: ")
print(f"Raw: {value_text} ({type(value_text)})")
value_num = float(value_text)
print(f"Converted: {value_num} ({type(value_num)})")
```

---

## 18) Appendix C — Instructor Language for Coaching

When learners freeze, use these process prompts:
- “What does your variable type say right now?”
- “Have you converted before arithmetic?”
- “Can you test with a simple known value?”
- “Does your output include units?”
- “What result did you expect before you ran?”

This promotes independent reasoning rather than answer-copying.

---

## 19) Appendix D — Reflection Notes for Instructor

Post-class reflection:
1. Did learners understand input type behavior?
2. Did they choose `int`/`float` intentionally?
3. Did they test formulas with plausible values?
4. Did they produce readable outputs?
5. Which misconception needs re-teach before checkpoint?

Use notes to refine Hour 8 framing.

---

## 20) Appendix E — Extended Troubleshooting Map for Input + Conversion

### Symptom: `TypeError` during arithmetic

Likely cause: one operand is still string.

Coaching steps:
1. Print both values and types.
2. Convert expected numeric fields.
3. Re-run with one known value.

### Symptom: `ValueError` at conversion

Likely cause: invalid numeric text for target type.

Coaching steps:
1. Read exact input that caused failure.
2. Check if decimal entered where `int` expected.
3. Switch to `float` when decimals are valid.

### Symptom: output numeric but unrealistic

Likely cause: wrong formula or constant.

Coaching steps:
1. Compare formula to prompt.
2. Run with simple benchmark value.
3. Estimate expected range before run.

### Symptom: output unreadable

Likely cause: missing labels/units/formatting.

Coaching steps:
1. Add line labels.
2. Add units.
3. Format decimals with `:.2f` or `:.1f`.

---

## 21) Appendix F — Extended Verbatim Reinforcement Lecture

“Let’s revisit why this hour is a major milestone. Up to now, many examples used fixed values inside code. That’s useful for learning syntax, but real programs accept values from users, files, APIs, and forms. The moment values come from outside your code, type discipline becomes essential.

Python’s `input()` gives you text because text is the safest universal format for keyboard entry. It does not guess your intent. That design puts responsibility in your hands, which is good programming practice.

I want you to remember one principle: conversion is not an afterthought; it is part of data modeling. If your variable represents a count, convert to int. If it represents a measurement, convert to float. Correct type selection simplifies all later code.

Another principle is incremental execution. Beginners often write the whole program first and then run once. That approach creates large debugging surfaces. Instead, run in short cycles: input stage, conversion stage, formula stage, output stage. Each successful stage reduces uncertainty.

Plausibility checks are equally powerful. If you convert 0°F and get 100°C, something is off. Use common-sense estimates as a guardrail. Programming is logic plus sanity checks.

When errors appear, treat them as instructions. `ValueError` tells you conversion target and offending value are incompatible. `TypeError` tells you operation and operand types are incompatible. Error messages are feedback channels, not personal failures.

Output quality matters too. Users need context. A value without units is ambiguous. A value with units and formatting is actionable.

You are now very close to independent mini-app development. Hour 8 checkpoint is your chance to combine input, conversion, calculation, and formatting in one coherent script.”

---

## 22) Appendix G — Additional Practice Set

### Practice 1: Kilograms to pounds

```python
kg = float(input("Enter kilograms: "))
pounds = kg * 2.20462
print(f"{kg:.2f} kg = {pounds:.2f} lb")
```

### Practice 2: Celsius to Fahrenheit

```python
celsius = float(input("Enter °C: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
```

### Practice 3: Age next decade

```python
age = int(input("Enter age: "))
print(f"In 10 years, you will be {age + 10}.")
```

### Practice 4: Area calculator

```python
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
print(f"Area = {area:.2f} square units")
```

### Practice 5: Two-value average

```python
a = float(input("Value 1: "))
b = float(input("Value 2: "))
avg = (a + b) / 2
print(f"Average: {avg:.2f}")
```

---

## 23) Appendix H — Oral Check Questions with Expected Responses

1. **Question:** Why not add `1` directly to `input()` result?  
   **Response:** Because it is string; must convert first.

2. **Question:** Which conversion for decimal input?  
   **Response:** `float()`.

3. **Question:** What does `int('3.5')` do?  
   **Response:** Raises `ValueError`.

4. **Question:** Why include units in output?  
   **Response:** Clarity and correctness for users.

5. **Question:** Best quick type check line?  
   **Response:** `print(type(variable))`.

---

## 24) Appendix I — Instructor Reflection (expanded)

- Did learners repeatedly forget conversion?
- Did they use plausibility checks or trust first output?
- Did they format outputs with units?
- Did they read errors or ignore them?
- Which support phrase improved independence most?

Use insights to plan checkpoint scaffolding.

---

## 25) Appendix J — Rapid-Fire Q&A + Numeric Input Drill Bank

### Quick conceptual questions

1. Why does `input()` return `str`?
2. What error appears for `int("hello")`?
3. What error appears for adding string and int?
4. When should you choose `float()`?
5. How do you inspect type during debugging?

### Short verbal script

“Type mismatch errors are not random; they are feedback that your data model and operations are out of sync. Convert intentionally, test incrementally, and verify plausibility.”

### Drill snippets

```python
raw = input("Number: ")
num = float(raw)
print(f"Type before: {type(raw)}")
print(f"Type after:  {type(num)}")
```

```python
miles = float(input("Miles: "))
km = miles * 1.60934
print(f"{miles:.1f} miles = {km:.2f} km")
```

```python
f = float(input("Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f"{f:.1f}°F = {c:.1f}°C")
```

```python
a = float(input("A: "))
b = float(input("B: "))
print(f"Sum: {a + b:.2f}")
```

### Instructor reminder line

“During support, avoid typing final code for learners. Ask guiding questions about type, formula, and expected range.”

---

## 26) Appendix K — Final Reinforcement Notes

Instructor reminder script:
“Hour 7 is successful when learners understand that interactive programs need type conversion as a normal step, not an emergency fix. Encourage them to check types early and run formulas with known values.”

Mini-practice block:

```python
value_text = input("Enter decimal number: ")
value_num = float(value_text)
print(f"Raw type: {type(value_text)}")
print(f"Numeric type: {type(value_num)}")
print(f"Double: {value_num * 2:.2f}")
```

Use as a quick recap before checkpoint hour.

---

## 27) Appendix L — Instructor Micro-Workshop Script (15-minute optional)

Run this if the class needs extra confidence before checkpoint.

“Let’s do one focused conversion workshop. We’ll build a tiny script that asks for two measurements, converts both to `float`, computes an average, and prints a formatted sentence.

This exercise reinforces four things at once: input is text, conversion is required, formulas need numeric types, and output should be clear.”

```python
value_a_text = input("Enter first measurement: ")
value_b_text = input("Enter second measurement: ")

value_a = float(value_a_text)
value_b = float(value_b_text)

average = (value_a + value_b) / 2

print(f"Input A: {value_a:.2f}")
print(f"Input B: {value_b:.2f}")
print(f"Average: {average:.2f}")
```

“Now modify it:
1. Print raw types before conversion.
2. Print converted types after conversion.
3. Change labels so units are included.

Then answer verbally:
- Why can’t we average raw input strings?
- Why does float make sense for measurements?
- What would change if values were item counts instead?”

This short workshop reliably prepares learners for checkpoint expectations.

Additional recap script:
“Every interactive script follows the same backbone: prompt, convert, compute, format, test. If you remember that sequence, you can build many useful beginner programs without guessing.”

Instructor final reminder:
“Close Hour 7 with one combined demonstration that prints raw input, converted value, converted type, and final computed output. This reinforces the mental bridge from keyboard text to numerical computation. Ask learners to call out where conversion happens, then ask what would fail if conversion was removed. Have them run one plausible test and one edge-like test such as zero. Encourage them to check formula reasonableness, not only syntax correctness. This habit prepares them directly for Hour 8, where they must combine input, conversion, arithmetic, and formatting under a light time constraint. Confidence comes from repeated small success loops: prompt, convert, compute, format, and verify.”

Closing checklist for learners:
- I know `input()` returns `str`.
- I can convert with `int()` and `float()` appropriately.
- I can identify and explain `ValueError` in simple terms.
- I can produce labeled, unit-aware output with formatting.
- I can test with known values and sanity-check results.
Extended reminder:
When supporting learners, ask them to narrate the data journey from raw keyboard text to final numeric output. That narration often reveals hidden assumptions and prevents repeated type mistakes. Encourage one final run with a decimal input and one final run with an integer-like input so they can see that the same conversion workflow supports both cases.

Final instructor checkpoint passage:
“Before ending Hour 7, run one final class-wide practice where everyone enters the same test value and compares output. Shared test values make debugging conversations precise. Ask learners to point to the exact conversion line in their code and explain why it exists. Then ask them to remove that line temporarily and predict the resulting error. This quick contrast locks in understanding. End by reminding learners that conversion is not optional boilerplate; it is the bridge between user text and arithmetic logic, and it is the key skill they will rely on in the checkpoint.”
Done.
