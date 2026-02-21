# Repository Custom Instructions for Python Programming Courses

## Repository Overview

This repository contains comprehensive instructional materials for a 96-hour Python Programming course package delivered by GlobalIT. The course is structured as two 48-hour modules:

- **Module 1: Python Programming (Basic)** - Covers fundamentals, data structures, functions, OOP basics, and file I/O (PCEP certification aligned)
- **Module 2: Python Programming (Advanced)** - Covers design patterns, GUI development, databases, REST APIs, data analysis, and testing (PCAP certification aligned)

**Key Technologies**: Marp (Markdown Presentation Ecosystem), Jupyter Notebooks, GitHub Actions, Python 3.x

## Repository Structure

```
.
├── .github/
│   ├── workflows/          # CI/CD pipelines (marp-action.yml, autograder.yml)
│   ├── agents/             # Custom AI agent configurations
│   └── ISSUE_TEMPLATE/     # Issue templates for course development
├── Basics/                 # Module 1 materials (48 hours)
│   ├── Instructor/         # Instructor runbooks (source of truth)
│   ├── lessons/            # Markdown source files for slides
│   ├── assignments/        # Jupyter notebooks with autograder configs
│   ├── quizzes/            # Multiple choice quizzes
│   └── themes/             # CSS themes for slides (python-dark.css, python-light.css)
├── Advanced/               # Module 2 materials (48 hours)
│   ├── Instructor/         # Instructor runbooks (source of truth)
│   ├── lessons/            # Markdown source files for slides
│   ├── assignments/        # Jupyter notebooks with autograder configs
│   ├── quizzes/            # Multiple choice quizzes
│   └── themes/             # CSS themes for slides
├── _site/slides/           # Generated HTML/PDF/PPTX slides (build output)
├── .marprc.yml             # Primary Marp configuration (used by CI)
├── AGENTS.md               # Comprehensive agent documentation
└── README.md               # Course package overview
```

**Important**: The AGENTS.md file contains extensive documentation about the repository structure, development workflow, and best practices. Always reference it for detailed guidance.

## Build and Test Commands

### Slide Generation

**Primary method (replicates CI):**
```bash
npx @marp-team/marp-cli -c .marprc.yml
```
Output: `./_site/slides/` (HTML, PDF, PPTX, PNG)

**Build specific file:**
```bash
# HTML
npx @marp-team/marp-cli Basics/lessons/filename.md -o output.html

# PDF
npx @marp-team/marp-cli Basics/lessons/filename.md -o output.pdf --pdf

# PPTX
npx @marp-team/marp-cli Basics/lessons/filename.md -o output.pptx --pptx
```

**Watch mode for development:**
```bash
npx @marp-team/marp-cli -w -c .marprc.yml
```

**Note**: No `package.json` exists - always use `npx` to run Marp CLI directly.

### Slide Validation

```bash
# Validate locally generated slides (default: Basics/lessons/slides/)
./validate_slides.sh

# Or specify a different directory
./validate_slides.sh _site/slides  # For CI-built slides
```
Checks for proper structure, navigation, CSS variables, and file integrity. Defaults to `Basics/lessons/slides/` for local development. For CI output, use `_site/slides/`.

### Autograder Testing

**Local testing workflow** (mimics CI for assignments):
```bash
# Navigate to assignment config directory
cd Basics/assignments/Basics_Day1_homework/

# Install dependencies and convert notebook
python -m pip install nbconvert
jupyter nbconvert --to script ../Basics_Day1_homework.ipynb --output day1.py

# Run converted script
python day1.py

# Compare output to expected values in criteria.json
```

**Critical**: All autograder paths in `setup.json` are relative to the config directory. Notebooks are referenced as `../Basics_DayX_homework.ipynb`.

### Python Environment

No specific Python package manager is configured. Use system Python 3.x or create a virtual environment as needed:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install jupyter nbconvert
```

## CI/CD Pipelines

### GitHub Actions Workflows

1. **Marp Slide Build** (`.github/workflows/marp-action.yml`)
   - **Triggers**: Push to `main` (paths: `Basics/lessons/**.md`, `Advanced/lessons/**.md`, `.marprc.yml`)
   - **Outputs**: Slides to GitHub Pages at `_site/slides/`
   - **Uses**: `KoharaKazuya/marp-cli-action@v4` with `.marprc.yml`
   - **Requires**: `GH_PAT` secret for deployment

2. **Autograder** (`.github/workflows/autograder.yml`)
   - **Triggers**: Push/PR to `main`, plus manual `workflow_dispatch`
   - **Uses**: `webtech-network/autograder@v1` with `io` template preset
   - **Config files per assignment**:
      - `criteria.json` - Test cases with stdin/stdout expectations
      - `setup.json` - Notebook conversion and dependency installation
      - `feedback.json` - Optional custom feedback messages
   - **Runtime note**: The workflow prepares `submission/.github/autograder/` at runtime and generates a v1-compatible `setup.json`. It also parses `Basics_Day1_Quiz.html` and `Basics_Day2_Quiz.html` (from `Basics/quizzes/Basics_Day1/` or `Basics/quizzes/`) into autograder-compatible `tests[]` JSON and writes quiz grading results to `submission/.github/autograder/quiz_grades.json`. Quiz grading reads exported answer JSON files (`Basics_Day1_Quiz_answers.json` / `Basics_Day2_Quiz_answers.json`) instead of running notebook conversion commands. When triggered manually via `workflow_dispatch`, it also commits/pushes autograder output changes to a timestamped `autograder-results-*` branch. Keep authoring assignment configs in `Basics/assignments/Basics_DayX_homework/`.

### Configuration Files

- **`.marprc.yml`**: Primary Marp config (YAML), used by CI
  - Input: `./Basics/lessons` (Note: Currently only Basics is auto-built)
  - Output: `./_site/slides`
  - Formats: HTML, PDF, PPTX, PNG
  
- **`marp.config.mjs`**: Alternative ES module config (JavaScript)
- **`marp.config.ts`**: TypeScript configuration option

## Development Workflow

### Source of Truth: Instructor Runbooks

**Always reference these files for content creation**:
- `Basics/Instructor/Python_Basics_Instructor_Runbook_4hr_Days.md`
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`

These define day-by-day (12 days), hour-by-hour (4 hours/day) breakdown, learning objectives, and activities.

### Content Creation Guidelines

1. **Lecture Scripts** (Markdown files for instructor delivery):
   - Location: `Basics/lessons/lecture/DayX_HourY_Basics.md` or `Advanced/lessons/lecture/DayX_HourY_Advanced.md`
   - Must be readable verbatim during instruction with minimal paraphrasing

2. **Slides** (Marp-compatible Markdown):
   - Use `---` for slide separators
   - Front matter is **optional**. When used, prefer fields like:
     - `title`, `description`, `author`
     - `theme` (typically `python-light` or `python-dark`)
     - `size` (e.g., `16:9`) and `paginate: true` as needed
   - If you need explicit Marp features (e.g., via CLI/GitHub Action), you may also add `marp: true` in the front matter, but existing slides work without it.
   - Themes available: `python-dark`, `python-light` (in respective `themes/` directories)

3. **Homework Assignments** (Jupyter Notebooks):
   - Location: `Basics/assignments/Basics_DayX_homework.ipynb`
   - **Critical**: Avoid IPython magics like `%%writefile` - breaks `nbconvert`
   - Must be deterministic (no random values, unseeded state, or live timestamps)
   - Numeric precision must match exactly what's in `criteria.json` (e.g., `85.50` not `85.5`)

4. **Quizzes** (Markdown + HTML):
   - Location: `Basics/quizzes/Basics_DayX_Quiz.md` and `Basics/quizzes/Basics_DayX_Quiz.html` (or `Basics/quizzes/Basics_DayX/Basics_DayX_Quiz.html`)
   - 20-40 questions per quiz, one per day
   - Include correct answers and explanations

### Autograder Configuration Requirements

For each assignment (e.g., Day 1), create:
```
Basics/assignments/
├── Basics_Day1_homework.ipynb           # Student notebook
└── Basics_Day1_homework/                # Config directory
    ├── setup.json                        # Dependency install, conversion
    ├── criteria.json                     # Test specifications
    └── feedback.json                     # Optional custom feedback
```

**setup.json structure**:
```json
{
  "file_checks": ["../Basics_Day1_homework.ipynb"],
  "commands": [
    "python -m pip install --quiet --upgrade pip",
    "python -m pip install nbconvert",
    "jupyter nbconvert --to script ../Basics_Day1_homework.ipynb --output day1.py",
    "if [ ! -f day1.py ]; then echo 'ERROR: Conversion failed'; exit 1; fi"
  ]
}
```

**criteria.json structure**:
```json
{
  "tests": [
    {
      "name": "Test description",
      "command": ["python", "day1.py"],
      "stdin": "",
      "expected_stdout": ["Expected output line 1", "Expected output line 2"],
      "points": 10
    }
  ]
}
```

**Important warnings**:
- Do NOT rename notebooks, config files, or move assignment directories
- All paths in `setup.json` are relative to the config directory
- Notebooks must be self-contained with no external dependencies
- Keep the assignment notebook name stable (`Basics_DayX_homework.ipynb`), because workflow pre-flight checks look for that filename under `submission/`.

## Code Style and Standards

### Markdown
- Standard syntax with Marp directives
- Headers: `#` for titles, `##` for sections
- Code blocks: Triple backticks with language identifier
- Lists: `-` for unordered, `1.` for ordered

### Python
- Follow PEP 8 guidelines
- Naming: `snake_case` (functions/variables), `PascalCase` (classes), `UPPER_CASE` (constants)
- Documentation: Use docstrings for functions and classes
- Imports: Standard library, third-party, local (in that order)

### Jupyter Notebooks
- One concept per cell
- Use Markdown cells for explanations
- Keep code cells focused and testable
- Include expected outputs

## Common Commands Reference

```bash
# Build all slides (CI method)
npx @marp-team/marp-cli -c .marprc.yml

# Watch mode for development
npx @marp-team/marp-cli -w -c .marprc.yml

# Validate slides (defaults to Basics/lessons/slides/)
./validate_slides.sh

# Validate CI output (if _site exists)
./validate_slides.sh _site/slides

# Test assignment locally
cd Basics/assignments/Basics_Day1_homework/
python -m pip install nbconvert
jupyter nbconvert --to script ../Basics_Day1_homework.ipynb --output day1.py
python day1.py

# Check git status with no pager
git --no-pager status
git --no-pager diff

# List branches
git branch -a
```

## Key Facts and Tips

1. **No package.json**: Use `npx` to run Marp CLI directly
2. **Autograder paths**: All paths in `setup.json` are relative to the assignment's config directory
3. **Deterministic outputs**: Assignment scripts must produce identical output on every run
4. **IPython magics**: Avoid in notebooks - use Markdown code blocks instead
5. **Theme locations**: `Basics/themes/` and `Advanced/themes/`
6. **CI triggers**: Changes to `Basics/lessons/**.md`, `Advanced/lessons/**.md`, or `.marprc.yml`
7. **Pages deployment**: Requires `GH_PAT` secret
8. **Instructor runbooks**: Primary source of truth for all content

## Validation Steps

Before committing changes:

1. **For slides**: Build locally with `npx @marp-team/marp-cli -c .marprc.yml`
2. **For assignments**: Test conversion and run script locally
3. **For notebooks**: Restart kernel and run all cells
4. **For slides validation**: Run `./validate_slides.sh` to validate HTML in `Basics/lessons/slides/` (or `./validate_slides.sh _site/slides` for CI output)
5. **Always**: Check git status and review changes before pushing

## Custom Agents Available

This repository has specialized agents configured in `.github/agents/`:
- `frontend-slides-batch.agent.md` - Batch HTML slide generation
- `presentations-orchestrator.agent.md` - Presentation build orchestration
- `presentations-marp-writer.agent.md` - Marp presentation writing
- `python_educator.agent.md` - Python educational content specialist
- `technical-content-evaluator.agent.md` - Technical content quality evaluation

Use these agents for specialized tasks in their respective domains.

## Additional Resources

- **AGENTS.md**: Comprehensive repository documentation (read this for detailed guidance)
- **README.md**: Course overview and learning objectives
- **Marp Documentation**: https://marp.app/
- **Global Autograder**: https://github.com/webtech-network/autograder
- **Python Institute**: https://pythoninstitute.org/
