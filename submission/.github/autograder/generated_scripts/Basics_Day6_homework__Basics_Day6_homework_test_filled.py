#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 6 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


print("Task: keep insertion order and allow duplicates -> list")
print("Task: fast unique membership checks -> set")
print("Task: lookup phone by name -> dict")
print("Tradeoff: set removes duplicates but loses original order")

numbers = [4, 12, 8, 18, 27]
emails = ["ana@example.com", "bob@example.com", "ana@example.com", "cy@example.com"]
words = ["python", "data", "python", "loops", "data", "python"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
x, y = (5, 9)
print(f"Filtered > 10: {[number for number in numbers if number > 10]}")
print(f"Unique emails: {sorted(set(emails))}")
print(f"Word counts: {counts}")
print(f"Coordinates unpacked: x={x} y={y}")

contacts = {}
contacts["Ava"] = "555-0101"
print("Added: Ava -> 555-0101")
contacts["Ben"] = "555-0102"
print("Added: Ben -> 555-0102")
print(f"Search Ava: {contacts.get('Ava', 'Not found')}")
print(f"Search Zoe: {contacts.get('Zoe', 'Not found')}")
print(f"Contact count: {len(contacts)}")

checkpoint_contacts = {
    "Ava": "555-0101",
    "Eli": "555-0129",
    "Liam": "555-0128",
    "Mia": "555-0130",
    "Zoe": "555-0131",
}
print(f"Lookup Mia: {checkpoint_contacts.get('Mia', 'Not found')}")
print(f"Lookup Noah: {checkpoint_contacts.get('Noah', 'Not found')}")
print(f"Total contacts: {len(checkpoint_contacts)}")
print(f"Contacts (sorted): {', '.join(sorted(checkpoint_contacts))}")
print("Safe lookup used: dict.get")

