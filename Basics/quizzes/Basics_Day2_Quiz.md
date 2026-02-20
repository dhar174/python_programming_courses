# Python Basics - Day 2 Quiz

**Topics Covered:**
- String fundamentals: indexing, slicing, and length
- String methods: normalize, search, and replace
- Input/output and type conversion
- Checkpoint: Integrating fundamental concepts

**Instructions:**
- Answer all questions
- For multiple choice, select the best answer
- For code questions, write your answer or predict the output
- Check your answers at the end
- Review explanations for any questions you missed

**Total Questions: 30**
**Time Estimate: 45-60 minutes**

---

## Section 1: String Fundamentals (Questions 1-8)

### Question 1
What is the result of the following code?

```python
text = "Python"
print(text[0])
```

A) `P`  
B) `y`  
C) `0`  
D) An error

**Your Answer:** ___

---

### Question 2
What does negative indexing allow you to do in Python strings?

A) Create negative numbers  
B) Access characters from the end of the string  
C) Remove characters from a string  
D) Reverse a string

**Your Answer:** ___

---

### Question 3
What is the result of this code?

```python
word = "Python"
print(word[-1])
```

A) `P`  
B) `y`  
C) `n`  
D) An error

**Your Answer:** ___

---

### Question 4
What does the slice `text[1:4]` return for `text = "Python"`?

A) `Pyt`  
B) `yth`  
C) `ytho`  
D) `tho`

**Your Answer:** ___

---

### Question 5
What will this code print?

```python
message = "Hello"
print(message[:3])
```

A) `Hel`  
B) `Hell`  
C) `Hello`  
D) `llo`

**Your Answer:** ___

---

### Question 6
What does `len("Python")` return?

A) `5`  
B) `6`  
C) `7`  
D) An error

**Your Answer:** ___

---

### Question 7
How do you check if the word "code" is in the string `text = "I love to code"`?

A) `text.has("code")`  
B) `"code" in text`  
C) `text.contains("code")`  
D) `text.find("code") != -1`

**Your Answer:** ___

---

### Question 8
What is the result of this code?

```python
text = "Programming"
print(text[3:])
```

A) `Pro`  
B) `gram`  
C) `gramming`  
D) `Programming`

**Your Answer:** ___

---

## Section 2: String Methods (Questions 9-16)

### Question 9
What will this code output?

```python
name = "ALICE"
print(name.lower())
```

A) `ALICE`  
B) `alice`  
C) `Alice`  
D) An error

**Your Answer:** ___

---

### Question 10
What does the `.strip()` method do?

A) Removes all spaces from a string  
B) Removes leading and trailing whitespace  
C) Removes all vowels  
D) Removes special characters

**Your Answer:** ___

---

### Question 11
What will this code print?

```python
text = "  hello world  "
print(text.strip())
```

A) `hello world`  
B) `  hello world  `  
C) `helloworld`  
D) `hello  world`

**Your Answer:** ___

---

### Question 12
Are strings mutable (changeable) in Python?

A) Yes, you can modify strings in place  
B) No, strings are immutable  
C) Only if you use special methods  
D) It depends on the string length

**Your Answer:** ___

---

### Question 13
What will this code output?

```python
text = "hello"
text.upper()
print(text)
```

A) `HELLO`  
B) `hello`  
C) `Hello`  
D) An error

**Your Answer:** ___

---

### Question 14
What does the `.replace()` method return?

A) Nothing - it modifies the original string  
B) A new string with replacements made  
C) A list of replaced characters  
D) The number of replacements

**Your Answer:** ___

---

### Question 15
What will this code print?

```python
sentence = "I love Python"
print(sentence.count("o"))
```

A) `1`  
B) `2`  
C) `3`  
D) `0`

**Your Answer:** ___

---

### Question 16
What does `text.find("x")` return if "x" is NOT in the string?

A) `0`  
B) `-1`  
C) `None`  
D) An error

**Your Answer:** ___

---

## Section 3: Input/Output and Type Conversion (Questions 17-24)

### Question 17
What data type does the `input()` function always return?

A) `int`  
B) `float`  
C) `str`  
D) It depends on what the user types

**Your Answer:** ___

---

### Question 18
What will happen if you run this code and the user enters "25"?

```python
age = input("Enter your age: ")
print(age + 5)
```

A) Prints `30`  
B) Prints `255`  
C) Prints `25 5`  
D) Raises a `TypeError`

**Your Answer:** ___

---

### Question 19
How do you convert the string "42" to an integer?

A) `str("42")`  
B) `int("42")`  
C) `float("42")`  
D) `convert("42", int)`

**Your Answer:** ___

---

### Question 20
What will this code print?

```python
num = "3.14"
result = float(num)
print(type(result))
```

A) `<class 'str'>`  
B) `<class 'int'>`  
C) `<class 'float'>`  
D) `<class 'number'>`

**Your Answer:** ___

---

### Question 21
What happens when you try to convert an invalid string to a number?

```python
num = int("hello")
```

A) Returns `0`  
B) Returns `None`  
C) Raises a `ValueError`  
D) Raises a `TypeError`

**Your Answer:** ___

---

### Question 22
What will this code print?

```python
price = 19.99
print(f"Price: ${price:.2f}")
```

A) `Price: $19.99`  
B) `Price: $19.9900`  
C) `Price: $20`  
D) An error

**Your Answer:** ___

---

### Question 23
Why is type conversion important when working with user input?

A) It makes the code run faster  
B) It's required by Python  
C) Because `input()` returns a string, but you often need numbers for calculations  
D) It prevents all errors

**Your Answer:** ___

---

### Question 24
What is the result of this code?

```python
x = 5
y = str(x)
print(y + y)
```

A) `10`  
B) `55`  
C) `5 5`  
D) An error

**Your Answer:** ___

---

## Section 4: Checkpoint - Integration (Questions 25-30)

### Question 25
What will this code print?

```python
sentence = "Python is awesome"
words = sentence.split()
print(len(words))
```

A) `3`  
B) `17`  
C) `18`  
D) `4`

**Your Answer:** ___

---

### Question 26
What does the `.split()` method do by default (without arguments)?

A) Splits on commas  
B) Splits on whitespace  
C) Splits each character  
D) Splits on periods

**Your Answer:** ___

---

### Question 27
What will this code output?

```python
words = ["Hello", "World"]
result = " ".join(words)
print(result)
```

A) `HelloWorld`  
B) `Hello World`  
C) `["Hello", "World"]`  
D) An error

**Your Answer:** ___

---

### Question 28
What is the purpose of this code pattern?

```python
text = input("Enter text: ").strip().lower()
```

A) Remove whitespace and convert to lowercase for consistent processing  
B) Validate that the input is text  
C) Make the input shorter  
D) Encrypt the user's input

**Your Answer:** ___

---

### Question 29
How would you find the longest word in a sentence?

```python
sentence = "Python is great"
words = sentence.split()
```

A) `max(words)`  
B) `len(words)`  
C) `max(words, key=len)`  
D) `words.longest()`

**Your Answer:** ___

---

### Question 30
What is a common error pattern when working with strings and numbers?

A) Using `+` to concatenate a string and an integer without conversion  
B) Using too many variables  
C) Writing strings in uppercase  
D) Using the `input()` function

**Your Answer:** ___

---

---

# Answer Key and Explanations

## Section 1: String Fundamentals

### Question 1: **A**
**Explanation:** String indexing in Python starts at 0, so `text[0]` accesses the first character. In `"Python"`, the character at index 0 is `'P'`. Remember: Python uses zero-based indexing for all sequences (strings, lists, etc.).

### Question 2: **B**
**Explanation:** Negative indexing allows you to access characters counting from the end of the string. `-1` refers to the last character, `-2` to the second-to-last, and so on. This is convenient when you don't know the string's length but need to access elements from the end.

### Question 3: **C**
**Explanation:** `word[-1]` accesses the last character of the string. In `"Python"`, the last character is `'n'`. Negative indexing is particularly useful because you don't need to know the string's length to access characters from the end.

### Question 4: **B**
**Explanation:** Slicing `text[1:4]` extracts characters from index 1 up to (but not including) index 4. In `"Python"`: index 1 is `'y'`, index 2 is `'t'`, index 3 is `'h'`, so the result is `"yth"`. Remember the pattern: `[start:stop]` where stop is exclusive.

### Question 5: **A**
**Explanation:** `message[:3]` is shorthand for `message[0:3]`, which means "from the beginning up to (but not including) index 3". For `"Hello"`, this gives us indices 0, 1, and 2: `"Hel"`. Omitting the start index defaults to 0.

### Question 6: **B**
**Explanation:** `len("Python")` counts the number of characters in the string. `"Python"` has 6 characters: P-y-t-h-o-n. The `len()` function is fundamental for working with strings and other sequences.

### Question 7: **B**
**Explanation:** The `in` operator is the most Pythonic and readable way to check for substring membership: `"code" in text` returns `True` if "code" is found anywhere in the string. While option D (`text.find("code") != -1`) also works, `in` is clearer and more direct for simple containment checks.

### Question 8: **C**
**Explanation:** `text[3:]` is shorthand for "from index 3 to the end". In `"Programming"`, index 3 is `'g'`, so we get `"gramming"`. Omitting the stop index means "continue to the end of the string".

---

## Section 2: String Methods

### Question 9: **B**
**Explanation:** The `.lower()` method converts all alphabetic characters to lowercase. `"ALICE".lower()` returns `"alice"`. This method is useful for case-insensitive comparisons (e.g., checking if a user entered "yes", "Yes", or "YES").

### Question 10: **B**
**Explanation:** The `.strip()` method removes leading (beginning) and trailing (ending) whitespace, including spaces, tabs, and newlines. It does NOT remove spaces from the middle of the string. This is essential for cleaning up user input.

### Question 11: **A**
**Explanation:** `.strip()` removes the leading and trailing spaces from `"  hello world  "`, resulting in `"hello world"`. The space between "hello" and "world" remains because `.strip()` only affects the edges of the string.

### Question 12: **B**
**Explanation:** Strings in Python are immutable, meaning they cannot be changed after creation. When you call string methods like `.upper()` or `.replace()`, they return NEW strings rather than modifying the original. This is a fundamental property of strings that affects how you write code.

### Question 13: **B**
**Explanation:** Because strings are immutable, `text.upper()` returns a new string `"HELLO"`, but doesn't modify the original `text`. Since we didn't assign the result to anything (`text = text.upper()`), the original `text` still contains `"hello"`. This is a common mistake - always remember that string methods return new strings!

### Question 14: **B**
**Explanation:** The `.replace()` method returns a new string with all occurrences of a substring replaced. For example, `"hello".replace("l", "L")` returns `"heLLo"`. The original string remains unchanged because strings are immutable.

### Question 15: **B**
**Explanation:** The `.count()` method returns the number of non-overlapping occurrences of a substring. In `"I love Python"`, the letter "o" appears twice: once in "love" and once in "Python". This method is case-sensitive, so "o" and "O" are counted separately.

### Question 16: **B**
**Explanation:** The `.find()` method returns the index of the first occurrence of a substring, or `-1` if the substring is not found. This convention allows you to check `if text.find("x") != -1:` to see if the substring exists. For simple existence checks, using `in` is more readable.

---

## Section 3: Input/Output and Type Conversion

### Question 17: **C**
**Explanation:** The `input()` function ALWAYS returns a string (`str`), regardless of what the user types. Even if the user enters "42", you get the string `"42"`, not the integer `42`. This is why type conversion is essential when you need numeric input.

### Question 18: **D**
**Explanation:** Since `input()` returns a string, `age` is `"25"` (a string). Trying to use `+` between a string and an integer (`"25" + 5`) raises a `TypeError` with a message like "can only concatenate str (not 'int') to str". You must convert first: `int(age) + 5`.

### Question 19: **B**
**Explanation:** The `int()` function converts a string to an integer. `int("42")` returns the integer `42`. The string must contain a valid integer representation, or a `ValueError` will be raised. For decimal numbers, use `float()` instead.

### Question 20: **C**
**Explanation:** `float("3.14")` converts the string to a floating-point number. The `type()` function then returns `<class 'float'>`, confirming the conversion was successful. Use `float()` when working with decimal numbers.

### Question 21: **C**
**Explanation:** Trying to convert an invalid string to a number raises a `ValueError` with a message like "invalid literal for int() with base 10: 'hello'". This is why it's important to validate user input or use try/except blocks to handle conversion errors gracefully.

### Question 22: **A**
**Explanation:** The f-string format specifier `:.2f` formats a float with exactly 2 decimal places. `f"${19.99:.2f}"` produces `"$19.99"`. The `:.2f` means "format as a float with 2 digits after the decimal point". This ensures consistent formatting for currency and other precise values.

### Question 23: **C**
**Explanation:** Type conversion is crucial because `input()` always returns strings, but you typically need numbers for mathematical operations. Without conversion, trying to add numbers will concatenate strings instead (`"5" + "3"` gives `"53"`, not `8`). Always convert user input to the appropriate type before calculations.

### Question 24: **B**
**Explanation:** `str(5)` converts the integer `5` to the string `"5"`. Then `y + y` concatenates two strings: `"5" + "5" = "55"`. The `+` operator works differently depending on the operand types: with numbers it adds, with strings it concatenates.

---

## Section 4: Checkpoint - Integration

### Question 25: **A**
**Explanation:** `.split()` breaks the string into a list of words: `["Python", "is", "awesome"]`. The `len()` function then counts how many items are in the list: `3`. This pattern (split then count) is common for word counting.

### Question 26: **B**
**Explanation:** When called without arguments, `.split()` splits on any whitespace (spaces, tabs, newlines) and removes empty strings from the result. This is the most common use case. To split on a specific character, pass it as an argument: `.split(",")` splits on commas.

### Question 27: **B**
**Explanation:** The `.join()` method combines a list of strings into a single string, using the string it's called on as a separator. `" ".join(["Hello", "World"])` joins the words with a space between them: `"Hello World"`. Note the syntax: the separator calls `.join()` on the list.

### Question 28: **A**
**Explanation:** This pattern chains methods to normalize user input: `.strip()` removes leading/trailing whitespace, then `.lower()` converts to lowercase. This makes comparisons more robust: "Yes", " yes ", and "YES" all become "yes". Method chaining works because each method returns a string, which you can immediately call another method on.

### Question 29: **C**
**Explanation:** `max(words, key=len)` finds the word with the maximum length. The `key=len` parameter tells `max()` to compare words by their length rather than alphabetically. Option A (`max(words)`) would return the lexicographically largest word ("is"), not the longest. This is a powerful pattern for finding items based on custom criteria.

### Question 30: **A**
**Explanation:** A very common error is trying to concatenate strings and numbers without conversion: `"Age: " + 25` raises a `TypeError`. You must convert first: `"Age: " + str(25)` or use an f-string: `f"Age: {25}"`. Python won't implicitly convert types for string concatenation, which helps catch bugs but requires explicit conversions.

---

## Scoring Guide

- **25-30 correct:** Excellent! You have a strong grasp of Day 2 concepts.
- **20-24 correct:** Good work! Review the topics where you missed questions.
- **15-19 correct:** Fair understanding. Spend extra time practicing the concepts you missed.
- **Below 15:** Review the Day 2 materials and practice the exercises again.

---

## Key Takeaways from Day 2

1. **Indexing:** Strings use zero-based indexing; negative indices count from the end.

2. **Slicing:** Use `[start:stop]` to extract substrings; stop is exclusive.

3. **String Methods:** Methods like `.lower()`, `.strip()`, and `.replace()` return NEW strings (immutability).

4. **Input:** `input()` always returns a string - convert it when you need numbers.

5. **Type Conversion:** Use `int()`, `float()`, and `str()` to convert between types.

6. **Error Handling:** Be prepared for `ValueError` when converting invalid strings.

7. **Integration:** Combine `.split()`, `.join()`, and string methods to process text effectively.

8. **Common Pitfalls:** Remember immutability, always convert input types, and use appropriate string operations.

---

## Next Steps

After completing this quiz:

1. Review any questions you missed and read the explanations carefully
2. Complete the Day 2 homework notebook for hands-on practice
3. Practice writing small programs that process user input and manipulate strings
4. Experiment with combining multiple string methods in a single chain
5. Prepare for Day 3: Lists, conditionals, and control flow

Keep practicing - string manipulation is foundational to Python programming! 🚀
