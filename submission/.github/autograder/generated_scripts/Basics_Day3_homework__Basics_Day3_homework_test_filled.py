#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 3 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


age = 17
has_membership = True
can_join = 13 <= age <= 17 and has_membership
needs_parent_form = age < 16 and can_join
print(f"Age: {age}")
bracket = "teen" if 13 <= age <= 17 else "child" if age < 13 else "adult"
print(f"Bracket: {bracket}")
print(f"Has membership: {has_membership}")
print(f"Can join teen workshop: {can_join}")
print(f"Needs parent form: {needs_parent_form}")

bill = 48.50
tip = bill * 0.18
total = bill + tip
people = 2
print(f"Bill: ${bill:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
per_person = bill * (1 + 0.18) / people
print(f"Per person ({people}): ${per_person:.2f}")

sentence = "Python makes debugging easier"
words = sentence.split()
print(f"Word count: {len(words)}")
print(f"Longest word: {max(words, key=len).lower()}")
print(f"Pipe version: {' | '.join(words)}")
print(f"CSV version: {','.join(words)}")

debug_value = "17"
print(f"Debug value: {debug_value}")
print(f"Debug type before fix: {type(debug_value).__name__}")
debug_value = int(debug_value)
print(f"Debug type after fix: {type(debug_value).__name__}")
items = [0, 1, 2, 3, 4]
print(f"Index 5 exists: {5 < len(items)}")
print("Debug rule: Change one thing at a time")

