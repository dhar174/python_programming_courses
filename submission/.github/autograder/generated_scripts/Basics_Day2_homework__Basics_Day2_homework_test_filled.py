#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 2 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


course = "Python Programming"
print(f"Length: {len(course)}")
print(f"First character: {course[0]}")
print(f"Last character: {course[-1]}")
words = course.split()
print(f"First word: {words[0]}")
print(f"Second word: {words[1]}")

message = "  Hello, WORLD!  "
clean_message = message.strip()
print(f"Stripped: {clean_message}")
print(f"Lowercase: {clean_message.lower()}")
print(f"Uppercase: {clean_message.upper()}")
print(f"Replaced: {clean_message.replace('WORLD', 'Python')}")
print(f"Find 'WORLD': {clean_message.find('WORLD')}")
print(f"Count 'l': {clean_message.count('l')}")

celsius = 100.0
fahrenheit = celsius * 9 / 5 + 32
miles = 26.2
kilometers = miles * 1.60934
print(f"{celsius:.1f}C = {fahrenheit:.1f}F")
print(f"{miles:.1f} miles = {kilometers:.2f} km")

sentence = "The quick brown fox jumps over the lazy dog"
sentence_words = sentence.split()
print(f"Word count: {len(sentence_words)}")
print(f"Character count: {len(sentence)}")
print(f"Characters (no spaces): {len(sentence.replace(' ', ''))}")
print(f"Longest word: {max(sentence_words, key=len)}")
print(f"Title case: {sentence.title()}")

