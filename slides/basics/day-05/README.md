# Day 5 — Session 5: Tuples, Sets, and Dictionaries

**Course:** Python Programming (Basic)  
**Day:** 5 · Session 5  
**Hours covered:** 17–20  
**Slides:** [`day-05-session-5.html`](day-05-session-5.html) &nbsp;(43 slides)

---

## Session Overview

| Hour | Topic | Key Concept |
|------|-------|-------------|
| 17 | Tuples + Unpacking | Immutable sequences; `x, y = point` |
| 18 | Sets – Uniqueness + Membership | Auto-deduplication; unordered; fast `in` |
| 19 | Dictionaries Fundamentals | Key→value lookup; `get()` for safety |
| 20 | Dictionary Iteration + Counting | `items()` loop; counting pattern |

---

## Learning Outcomes

By the end of Session 5, learners can:

### Hour 17 — Tuples
- Create a tuple using parentheses and commas
- Explain immutability and why tuples cannot be changed
- Unpack a tuple into individual variables with `x, y = point`
- Identify the single-item tuple gotcha: `(x,)` vs `(x)`
- Build a coordinate-tracker program storing (x, y) points

### Hour 18 — Sets
- Create a set from a list to remove duplicates
- Use `add()` to insert items into a set
- Use `in` for fast membership testing
- Understand that sets are unordered (no indexing)
- Explain union (`|`) and intersection (`&`) conceptually

### Hour 19 — Dictionaries
- Create a dictionary with key/value pairs
- Access values by key using `dict[key]` and `dict.get(key, default)`
- Add and update entries
- Avoid `KeyError` crashes with safe access patterns

### Hour 20 — Dictionary Iteration + Counting
- Iterate over keys, values, and items with `.keys()`, `.values()`, `.items()`
- Apply the counting pattern: `d[word] = d.get(word, 0) + 1`
- Build a word-frequency counter from user input
- Normalize and clean text before counting

---

## Labs

| Hour | Lab | Description |
|------|-----|-------------|
| 17 | Coordinate Tracker | Store 5 (x, y) points as tuples; find min/max x |
| 18 | Unique Visitors | Collect 10 names; find unique count with a set |
| 19 | Inventory Manager | Build a restocking tool with safe dict access |
| 20 | Word Counter | Count word frequencies from user input |

---

## Files

| File | Description |
|------|-------------|
| [`day-05-session-5.html`](day-05-session-5.html) | Self-contained HTML slide deck (43 slides) |
| [`index.html`](index.html) | Session index / landing page |
| [`README.md`](README.md) | This file |

---

## Navigation

Inside the slide deck, use:

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| Swipe left/right | Mobile navigation |

---

## Scope Guardrail

This session stays within the **Basics** course scope.  
Topics intentionally **excluded** (covered in the Advanced course):
- `collections.namedtuple`, `collections.Counter`, `collections.defaultdict`
- Set comprehensions and dictionary comprehensions
- Nested dictionaries deeper than one level
- `OrderedDict` (unnecessary in Python 3.7+)
- File I/O, OOP, or class definitions

---

*Generated from `Basics/lessons/day-05-session-5.md`*
