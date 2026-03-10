#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 4 Homework
# 
# This homework aligns with Day 4 topics:
# 1. Lists fundamentals
# 2. Iterating lists with for-loops
# 3. Nested lists (table-like data)
# 4. Checkpoint: Lists + string handling
# 

# ---
# 

# ## Hour 13 - Lists fundamentals
# 

# In[ ]:


# Exercise 1.1 - Lists fundamentals
roster = ["Ava", "Ben", "Cara", "Dev", "Eli"]
print(f"Roster size: {len(roster)}")
print(f"First learner: {roster[0]}")
print(f"Last learner: {roster[-1]}")
print(f"Middle learners: {roster[1:4]}")
roster[2] = "Cora"
roster.append("Finn")
print(f"Updated roster: {roster}")


# ---
# 

# ## Hour 14 - Iterating lists with for-loops
# 

# In[ ]:


# Exercise 2.1 - Iterating lists with for-loops
name_lengths = {"Anna": 4, "Christopher": 11, "Maya": 4, "Leo": 3, "Chloe": 5}
total = 0
longest_name = ""
for name, length in name_lengths.items():
    total += length
    if len(name) > len(longest_name):
        longest_name = name
average = total / len(name_lengths)
starts_with_c = []
for name in name_lengths:
    if name.startswith("C"):
        starts_with_c.append(name)
upper_names = []
for name in ["Anna", "Chris", "Maya", "Leo"]:
    upper_names.append(name.upper())
print(f"Name count total: {total}")
print(f"Longest name: {longest_name}")
print(f"Average length: {average:.2f}")
print(f"Starts with C: {starts_with_c}")
print(f"Uppercase roster: {upper_names}")


# ---
# 

# ## Hour 15 - Nested lists (table-like data)
# 

# In[ ]:


# Exercise 3.1 - Nested lists
seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"],
]
flattened = []
for row in seats:
    for seat in row:
        flattened.append(seat)
print(f"Rows: {len(seats)}")
print(f"Columns per row: {len(seats[0])}")
print(f"Seat at row 2 col 3: {seats[1][2]}")
print(f"Flattened seats: {','.join(flattened)}")
print(f"Total seats: {len(flattened)}")


# ---
# 

# ## Hour 16 - Checkpoint 2: Lists + string handling
# 

# In[ ]:


# Exercise 4.1 - Checkpoint integration
raw_tags = "python, lists, loops, strings"
pieces = raw_tags.split(",")
clean_tags = []
for item in pieces:
    clean_tags.append(item.strip())
slug = "-".join(clean_tags)
print(f"Raw tags: {raw_tags}")
print(f"Clean tags: {clean_tags}")
print(f"Tag count: {len(clean_tags)}")
print(f"Slug: {slug}")
print(f"Contains 'loops': {'loops' in clean_tags}")


# ---
# 
