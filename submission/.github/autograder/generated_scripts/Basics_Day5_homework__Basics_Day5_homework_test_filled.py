#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 5 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


coordinates = (12, 34)
x_value, y_value = coordinates
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
roles = ("mentor", "student") + ("reviewer",)
print(f"Coordinates tuple: {coordinates}")
print(f"X value: {x_value}")
print(f"Y value: {y_value}")
print(f"First three days: {days[:3]}")
print(f"Updated roles: {roles}")

colors = ["blue", "red", "green", "blue", "violet", "red", "green"]
unique_colors = set(colors)
print(f"Raw item count: {len(colors)}")
print(f"Unique item count: {len(unique_colors)}")
print(f"Is 'blue' present: {'blue' in unique_colors}")
print(f"Is 'yellow' present: {'yellow' in unique_colors}")
print(f"Unique sorted colors: {sorted(unique_colors)}")

profile = {"name": "Nia", "role": "analyst", "city": "Accra"}
profile["city"] = "Lagos"
print(f"Profile keys: {sorted(profile)}")
print(f"Learner name: {profile['name']}")
print(f"Learner role: {profile['role']}")
print(f"Updated city: {profile['city']}")
print(f"Has 'email' key: {'email' in profile}")

words = "python data python rocks data python rocks fun".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
summary = ", ".join(f"{word}={counts[word]}" for word in sorted(counts))
print(f"Total words: {len(words)}")
print(f"Unique words: {len(counts)}")
print(f"Count for 'python': {counts['python']}")
print(f"Count for 'data': {counts['data']}")
print(f"Word counts: {summary}")

