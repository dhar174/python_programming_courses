# Day 4 Advanced Lecture Script Context Map

## 1. OVERVIEW

**Task:** Draft Day 4 Advanced lecture scripts (4 hours across 4 files)  
**Branch:** `copilot/draft-lecture-materials-day4`  
**Target Output:** Four markdown lecture script files ready for instructor delivery  

---

## 2. SESSION & CONTENT STRUCTURE

### Session 4 Schedule (Day 4 = Hours 13–16)

| Hour | Focus Topic | Runbook Coverage | Outcomes |
|------|-------------|------------------|----------|
| 13 | HTTP client work: requests + JSON contracts | JSON API consumption, error handling, timeouts | Consume APIs gracefully, handle network failures |
| 14 | Security basics (appropriate scope) | Env vars, hashing, secret management | Keep secrets out of code, use basic hashing |
| 15 | Capstone planning workshop (choose delivery path) | Scope, milestones, folder structure | Lock capstone scope, choose UI/API path |
| 16 | Checkpoint 2: Persistence-ready core + JSON save/load | Package layout, JSON persistence, logging | Deliver core that can save/load state reliably |

### Runbook Details for Each Hour

**Hour 13: HTTP client work (requests + JSON contracts)**
- Instructor talk points (10–20 min):
  - GET vs POST at high level
  - JSON parsing and error cases
  - Timeouts and status codes (practical)
  - Always set timeout (`timeout=5` or `timeout=(3,10)`)
  - Prefer `response.raise_for_status()` and handle `requests.HTTPError`
  - Treat JSON as contract: validate required keys/types before use
  - Use small "client wrapper" function to avoid repeating request logic
- Live demo (5–10 min): Call public sample API or provided endpoint, show try/except for requests exceptions
- Lab (25–35 min): Write small script calling HTTP endpoint, parse JSON, display key fields, handle non-200 status with friendly message, add timeout to all requests, structured error handling (network errors → "service unreachable", 4xx/5xx → show status + safe message, bad JSON → fallback + logging)
- Completion: Successful request/parsed output, graceful failure handling, no indefinite hangs, friendly message for timeout/404/500/invalid JSON
- Common pitfalls: No timeout (hangs), assuming JSON structure without checks

**Hour 14: Security basics (appropriate scope)**
- Instructor talk points (10–20 min):
  - Environment variables for secrets
  - Hashing vs encryption (high-level)
  - Don't roll your own crypto; keep it simple
- Live demo (5–10 min): Read API key from env var, hash string with hashlib (sha256) for comparison-only use
- Lab (25–35 min): Add env var support for API key, implement simple 'admin' action gated by key, do not hard-code key, create `.env.example` with placeholders (NO real secrets), update `.gitignore` to exclude `.env`, add README note about setting env vars
- Completion: Key loaded from env/config, admin action gated and logged
- Common pitfalls: Accidentally committing secrets, confusing hashing with encryption
- **Note:** Course does NOT require OAuth/JWT—keep advanced auth as optional discussion only

**Hour 15: Capstone planning workshop (choose delivery path)**
- Instructor talk points (10–20 min):
  - Milestones: core → persistence → UI → analytics → tests → package
  - Definition of done for each milestone
- Live demo (5–10 min): Sample folder structure and README skeleton, simple issue checklist
- Lab (25–35 min): Write one-page plan (bullets) with scope (features), data model summary, chosen UI surface(s), persistence plan, analytics idea, test plan; create README skeleton with run instructions placeholders
- Completion: Plan exists and is realistic, README skeleton created
- Common pitfalls: Scope too big, no plan for error handling or tests

**Hour 16: Checkpoint 2: Persistence-ready core + JSON save/load**
- Instructor talk points (10–20 min): Checkpoint grading focus: correctness + structure + error handling + logging
- Live demo (5–10 min): 'Fast grade' procedure: run, load missing file, save, reload, trigger validation
- Lab/Checkpoint (45–60 min): Build persistence-ready core with package layout under src/, JSON save/load (safe save recommended), logging to file, custom exceptions, demo script showing save → restart → load
- Completion: State persists across runs, errors handled without crashing, logs contain meaningful entries
- Common pitfalls: Dumping objects directly to JSON, corrupting JSON and not handling JSONDecodeError

---

## 3. FILE NAMING & TARGET DIRECTORY

### Naming Convention
- **Pattern:** `DayX_HourY_Advanced.md`
- **Examples for Day 4:**
  - `Advanced/lessons/lecture/Day4_Hour13_Advanced.md`
  - `Advanced/lessons/lecture/Day4_Hour14_Advanced.md`
  - `Advanced/lessons/lecture/Day4_Hour15_Advanced.md`
  - `Advanced/lessons/lecture/Day4_Hour16_Advanced.md`

### Target Directory
- **Base:** `/Advanced/lessons/lecture/`
- **Current state:** Directory contains only `01-intro-to-python.md` (stub)
- **Note:** All Basics lectures are in `/Basics/lessons/lecture/` (e.g., `Day1_Hour1_Basics.md` through `Day3_Hour4_Basics.md`)

---

## 4. LECTURE SCRIPT STANDARDS & STRUCTURE

### Required Components (Per Runbook & AGENTS.md)
Each 1-hour script must include:

1. **Title and Header**
   - Format: `# Day X, Hour Y: [Topic Title]`
   - Example: `# Day 4, Hour 13: HTTP client work: requests + JSON contracts`
   - Module line: `**Python Programming Advanced – Session Y**`

2. **Timing Overview** (Always first section)
   - Total time: 60 minutes per hour
   - Breakdown: 
     - Recap/Opening: 3–5 min
     - Instructor talk points: 10–20 min
     - Live demo: 5–10 min
     - Hands-on lab: 25–35 min
     - Debrief/Exit ticket: 5 min
   - Format as bullet list with min/max ranges

3. **Learning Outcomes for This Hour**
   - List 4–6 concrete, measurable outcomes
   - Begin with "By the end of this hour, you will be able to..."
   - Use action verbs (Consume, Handle, Implement, etc.)

4. **Section Breaks** (Numbered sections for instructor pacing)
   - Section 1: Opening/Recap (time allocation)
   - Section 2: Core Concepts (time allocation)
   - Section 3: Live Demo (time allocation)
   - Section 4: Hands-On Lab (time allocation)
   - Section 5: Debrief & Exit Ticket (time allocation)

5. **Instructor Speech Markers**
   - Use `**[Instructor speaks:]**` before narrative text
   - Use `**[Pause for student predictions]**` or similar for interactive moments
   - Use `**[Key point]:**` or `**[Important]:**` to highlight critical concepts
   - Include natural conversational tone with examples and relatable stories

6. **Code Examples**
   - Fenced with triple backticks and language specification: ````python`
   - Include inline comments for clarity
   - Show both good and bad examples where applicable
   - Keep examples concise but complete

7. **Emphasis & Formatting**
   - **Bold** for key terms, function names, tool names
   - `code font` for variable names, module names, commands
   - Bullet points for lists of related items
   - > Blockquotes for tips or side notes (optional)

8. **Lab Prompt / Hands-On Instructions**
   - Clear, step-by-step instructions
   - Expected completion time: 25–35 min
   - Include "Completion criteria" checklist
   - List "Common pitfalls to watch for"
   - Optional extensions (keep in scope)

9. **Debrief & Quick Check / Exit Ticket**
   - 1–3 reflection or short-answer questions
   - Assess understanding of core concepts

### Typical Per-Hour File Statistics
- **Line count range:** ~800–1,200 lines (Markdown formatted)
- **Content density:** Comprehensive, verbatim-readable with minimal paraphrasing
- **Code examples:** 8–15 snippets per hour

### Example Structure (from Basics Hour 2)
See `/Basics/lessons/lecture/Day1_Hour2_Basics.md` for reference pattern:
- **Timing Overview:** Detailed breakdown (6–8 lines)
- **Learning Outcomes:** 6 outcomes
- **Section 1 (Recap):** ~300 lines with subsections for print(), strings, comments
- **Section 2 (Core Concepts):** Multiple subsections with talk points + examples
- **Section 3 (Demo):** Live-coding walkthrough with narrative
- **Section 4 (Lab):** Lab prompt with exercises
- **Section 5 (Debrief):** Exit ticket questions

---

## 5. KEY REFERENCE FILES

### Runbook Source
- **File:** `/Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`
- **Session 4 Section:** Lines 1015–1600+ (covers Hours 13–16 in detail)
- **Key data:** Outcomes, instructor talk points, demo steps, lab prompt, completion criteria, pitfalls, extensions, quick checks

### Documentation & Standards
- **File:** `/AGENTS.md`
- **Lecture Script Standards Section:** "Writing Lecture Scripts" subsection
  - Location naming: `Basic topics: Basics/lessons/lecture/DayX_HourY_Basics.md`; `Advanced topics: Advanced/lessons/lecture/DayX_HourY_Advanced.md`
  - Per-hour file requirement (not combined files)
  - Content requirements: Comprehensive, readable verbatim, minimal paraphrasing, well-structured with code examples

### Basics Lecture Examples
- `/Basics/lessons/lecture/Day1_Hour1_Basics.md` – ~806 lines, complete template
- `/Basics/lessons/lecture/Day1_Hour2_Basics.md` – ~1,154 lines (largest), full narrative style
- `/Basics/lessons/lecture/Day2_Hour5_Basics.md` – ~846 lines, midrange example
- **Statistics:** Basics hours average 900–1,100 lines per hour

---

## 6. DEPENDENCIES & RELATED MATERIALS

### Required Inputs (Already Provided)
- ✓ Runbook `/Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` – Detailed Hour 13–16 content
- ✓ Basics lecture scripts (reference pattern) – Located in `/Basics/lessons/lecture/`
- ✓ AGENTS.md standards documentation – Lecture script standards + naming conventions

### Potential Supporting Files to Reference
- `/Advanced/python_advanced_48_h_syllabus_12_x_4_h_pcap_path_to_pcpp_1.md` – Advanced module syllabus for context
- `/Basics/python_basics_48_h_syllabus_12_x_4_h_pcep_pcap_aligned.md` – Basics syllabus for comparable content patterns
- Runbook prerequisites section (line ~34) – Confirms learners are comfortable with functions, basic classes, control flow, exceptions, file I/O

### Not Required for This PR
- Homework notebooks (Jupyter `.ipynb`)
- Quizzes (multiple choice)
- Slide decks (Marp `.md` in `/Advanced/lessons/slides/`)
- Tests or autograder configs

---

## 7. SKILLS DIRECTORIES & skills_used.md CONTEXT

### Available Skills for Reference

**.github/skills** (76+ directories with SKILL.md files):
- `context-map` – Context mapping methodology
- `documentation-writer` – Technical documentation patterns
- `create-agentsmd` – Creating AGENTS.md files
- `finalize-agent-prompt` – Prompt refinement
- `memory-merger` – Consolidating memory/documentation files
- `create-implementation-plan` – Implementation planning
- **Relevant:** Any markdown content generation or educational material skills

**.claude/skills** (7 directories):
- `frontend-design/` – Design patterns (not needed)
- `pptx/` – Presentation generation (not needed)
- `pdf/` – PDF generation (not needed)
- `theme-factory/` – Theme creation (not needed)
- `web-artifacts-builder/` – Web artifact generation (not needed)
- `webapp-testing/` – Test automation (not needed)

### Skills Likely Used for This PR
- **`context-map`** – Creating this context map
- **`documentation-writer`** – Writing lecture scripts (educational documentation)
- **`create-agentsmd`** or similar – Structuring instructor-facing materials
- **`finalize-agent-prompt`** – Refining and testing lecture script content
- **Potentially:** `memory-merger` if consolidating runbook content into scripts

### skills_used.md Requirement
- Create file at PR root: `/skills_used.md` (likely)
- List each skill used from `.github/skills` and `.claude/skills`
- Include brief justification for each (why it was needed)
- Format: Markdown with skill name, path, and description

---

## 8. TESTING & VALIDATION

### What to Verify (Before PR Submission)

1. **File Naming & Location**
   - [ ] Files follow `DayX_HourY_Advanced.md` pattern
   - [ ] Files saved in `/Advanced/lessons/lecture/`
   - [ ] No duplicates or overwrites of existing files

2. **Content Completeness**
   - [ ] All 4 hours (13–16) have corresponding script files
   - [ ] Runbook content incorporated (outcomes, talk points, demo, lab, completion, pitfalls)
   - [ ] Learning outcomes section present in each file
   - [ ] Timing overview matches runbook pacing (10–20 min talk, 5–10 min demo, 25–35 min lab)

3. **Markdown Formatting**
   - [ ] Headers use correct levels (H1 for title, H2 for sections)
   - [ ] Code blocks are properly fenced with ````python`
   - [ ] Emphasis markers are balanced (**bold**, `code`)
   - [ ] Lists are consistent (bullet vs. numbered)
   - [ ] No trailing whitespace or broken links

4. **Instructional Quality**
   - [ ] Content is verbatim-readable (minimal paraphrasing needed)
   - [ ] Instructor speech markers present (`**[Instructor speaks:]**`)
   - [ ] Interactive prompts included (`**[Pause for student predictions]**`)
   - [ ] Key points highlighted (`**[Key point]:**`)
   - [ ] Code examples are complete, runnable, and well-commented

5. **Consistency with Basics Examples**
   - [ ] Structure mirrors Day1_Hour2_Basics.md structure
   - [ ] Tone and voice are consistent with existing scripts
   - [ ] Lab instructions follow the same clarity standard

### Manual Testing (For Delivery Readiness)
- [ ] Instructor reads entire script aloud to estimate timing fit within 60-minute hour
- [ ] Code examples are tested to ensure correctness
- [ ] Lab exercises are verified to be completable in 25–35 minutes with moderate pacing

### CI/CD Checks (If Applicable)
- [ ] Markdown linting passes (if configured)
- [ ] No broken relative links
- [ ] File size reasonable (800–1,200 lines expected)

---

## 9. FILES TO MODIFY

| File | Purpose | Action | Notes |
|------|---------|--------|-------|
| `/Advanced/lessons/lecture/Day4_Hour13_Advanced.md` | HTTP client + JSON contracts | Create | New file, ~1000–1100 lines |
| `/Advanced/lessons/lecture/Day4_Hour14_Advanced.md` | Security basics | Create | New file, ~1000–1100 lines |
| `/Advanced/lessons/lecture/Day4_Hour15_Advanced.md` | Capstone planning workshop | Create | New file, ~1000–1100 lines |
| `/Advanced/lessons/lecture/Day4_Hour16_Advanced.md` | Checkpoint 2: JSON persistence | Create | New file, ~1000–1100 lines |
| `/skills_used.md` | List of skills applied | Create | Document which skills were used from `.github/skills` and `.claude/skills` |

---

## 10. NOTABLE CONSTRAINTS & CONSIDERATIONS

1. **No Python Code Tests Required**
   - Scripts are instructor-facing, not student code
   - Code examples are illustrative; no automated grading
   - Lab prompts reference learner activities (not auto-graded in this PR)

2. **Advanced Module Specifics**
   - Learners have completed 48-hour Basics course
   - Expected prerequisite: functions, basic classes, control flow, exceptions, file I/O
   - Focus on practical skills (requests, logging, JSON, environment variables, capstone planning)

3. **Capstone Context**
   - Capstone runs throughout the course
   - Hours 15–16 focus on planning + checkpoint delivery
   - Domain model is free-form (tasks, inventory, contacts, notes, expenses, etc.)

4. **Scope Boundaries**
   - Hour 14 (Security): Keep auth **simple**; no OAuth/JWT required
   - Hour 13 (HTTP): Focus on requests library + JSON parsing; no REST API server building here (comes later in Session 9)
   - Hour 15–16: Planning + checkpoint focus, not comprehensive capstone delivery

5. **Integration Notes**
   - These scripts align with `/Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` (lines 1015–1600+)
   - Scripts will feed into instructional delivery via CHOICE/LogicalLabs platform
   - Scripts may later generate slides via Marp (if needed; not part of this PR)

---

## 11. REFERENCE PATTERN SUMMARY

### From Day 1 Hour 2 (Basics) – Structure Template
```
# Day 1, Hour 2: [Topic Title]
**Python Programming Basics – Session 1**

## Timing Overview
- [Breakdown of 60-minute hour with time allocations]

## Learning Outcomes for This Hour
1. [Outcome 1]
2. [Outcome 2]
...6. [Outcome 6]

---

## Section 1: [Recap/Opening] (X minutes)
### [Subsection A]
**[Instructor speaks:]**
[Narrative explanation]

### [Subsection B]
**[Instructor speaks:]**
[Code example with explanation]

---

## Section 2: [Core Concepts] (X minutes)
### [Topic A]
**[Instructor speaks:]**
[Explanation + example]

### [Topic B]
[Explanation + code + common mistake]

---

## Section 3: Live Demo (X minutes)
**[Instructor speaks:]**
[Narrated demo steps with code]

---

## Section 4: Hands-On Lab (X minutes)
### Lab: [Lab Title]
- [Step 1]
- [Step 2]
- ...

**Completion criteria:**
- [Criterion 1]
- [Criterion 2]

**Common pitfalls:**
- [Pitfall 1]
- [Pitfall 2]

**Optional extensions:**
- [Extension 1]

---

## Section 5: Debrief & Exit Ticket (X minutes)
**Quick check:**
1. [Question 1]
2. [Question 2]
```

---

## 12. SUMMARY CHECKLIST FOR PR SUBMISSION

- [ ] Four lecture script files created: Day4_Hour13, 14, 15, 16 in `/Advanced/lessons/lecture/`
- [ ] Each file follows DayX_HourY_Advanced.md naming pattern
- [ ] Content derived from `/Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` Session 4 section (hours 13–16)
- [ ] Structure mirrors `/Basics/lessons/lecture/Day1_Hour2_Basics.md` reference template
- [ ] All required components present: title, timing, outcomes, 5 sections, lab prompt, quick check, code examples
- [ ] Markdown formatting is clean, consistent, and passes linting
- [ ] Skills used documented in `/skills_used.md` with paths and justifications
- [ ] PR title: "Advanced: Draft Day 4 lecture scripts (Hours 13–16)"
- [ ] PR description includes module affected, files changed, testing approach
- [ ] No broken links, trailing whitespace, or syntax errors
- [ ] Line count per file approximately 1,000–1,100 lines (range for Basics is 800–1,200)

___BEGIN___COMMAND_DONE_MARKER___0
