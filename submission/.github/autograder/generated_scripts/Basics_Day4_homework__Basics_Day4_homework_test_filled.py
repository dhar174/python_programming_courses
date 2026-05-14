#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 4 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


roster = ["Ava", "Ben", "Cara", "Dev", "Eli"]
print(f"Roster size: {len(roster)}")
print(f"First learner: {roster[0]}")
print(f"Last learner: {roster[-1]}")
print(f"Middle learners: {roster[1:4]}")
roster[2] = "Cora"
roster.append("Finn")
print(f"Updated roster: {roster}")

names = ["Anna", "Christopher", "Chloe", "Maya", "Leo"]
total_length = sum(len(name) for name in names)
print(f"Name count total: {total_length}")
print(f"Longest name: {max(names, key=len)}")
print(f"Average length: {total_length / len(names):.2f}")
print(f"Starts with C: {[name for name in names if name.startswith('C')]}")
roster_for_uppercase = ["Anna", "Chris", "Maya", "Leo"]
print(f"Uppercase roster: {[name.upper() for name in roster_for_uppercase]}")

seats = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
flat_seats = [seat for row in seats for seat in row]
print(f"Rows: {len(seats)}")
print(f"Columns per row: {len(seats[0])}")
print(f"Seat at row 2 col 3: {seats[1][2]}")
print(f"Flattened seats: {','.join(flat_seats)}")
print(f"Total seats: {len(flat_seats)}")

raw_tags = "python, lists, loops, strings"
clean_tags = [tag.strip() for tag in raw_tags.split(',')]
print(f"Raw tags: {raw_tags}")
print(f"Clean tags: {clean_tags}")
print(f"Tag count: {len(clean_tags)}")
print(f"Slug: {'-'.join(clean_tags)}")
print(f"Contains 'loops': {'loops' in clean_tags}")

