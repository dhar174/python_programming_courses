import importlib.util
import pytest
from pathlib import Path

# Dynamically load the module
spec = importlib.util.spec_from_file_location("generate_slides", "Basics/generate_slides.py")
generate_slides = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_slides)
get_output_paths = generate_slides.get_output_paths

def test_get_output_paths_no_match():
    repo_root = Path("/repo")
    # Not in Basics/Advanced
    input_path = repo_root / "Other" / "lessons" / "slides" / "test.md"
    assert get_output_paths(input_path, repo_root) == []

    # Not in lessons/slides
    input_path = repo_root / "Basics" / "lecture" / "test.md"
    assert get_output_paths(input_path, repo_root) == []

    # Too shallow
    input_path = repo_root / "Basics" / "lessons" / "readme.md"
    assert get_output_paths(input_path, repo_root) == []

def test_get_output_paths_basics_no_day():
    repo_root = Path("/repo")
    input_path = repo_root / "Basics" / "lessons" / "slides" / "intro.md"
    # rel_path.parts is ('Basics', 'lessons', 'slides', 'intro.md') -> length 4
    # parts[0] == 'Basics'
    # parts[1:3] == ('lessons', 'slides')
    # is_source_backed_slides_path == True
    expected = [repo_root / "Basics" / "lessons" / "slides" / "intro.html"]
    assert get_output_paths(input_path, repo_root) == expected

def test_get_output_paths_basics_with_day():
    repo_root = Path("/repo")
    input_path = repo_root / "Basics" / "lessons" / "slides" / "day-01" / "lesson1.md"
    # module_name = 'basics'
    # day_dir = 'day-01'
    expected = [
        repo_root / "Basics" / "lessons" / "slides" / "day-01" / "lesson1.html",
        repo_root / "slides" / "basics" / "day-01" / "lesson1.html"
    ]
    assert get_output_paths(input_path, repo_root) == expected

def test_get_output_paths_advanced_with_day():
    repo_root = Path("/repo")
    input_path = repo_root / "Advanced" / "lessons" / "slides" / "day-05" / "adv_lesson.md"
    # module_name = 'advanced'
    # day_dir = 'day-05'
    expected = [
        repo_root / "Advanced" / "lessons" / "slides" / "day-05" / "adv_lesson.html",
        repo_root / "slides" / "advanced" / "day-05" / "adv_lesson.html"
    ]
    assert get_output_paths(input_path, repo_root) == expected

def test_get_output_paths_deduplication(tmp_path):
    # To test deduplication, we need two paths to resolve to the same location.
    repo_root = tmp_path

    # Create a structure where we can have a symlink or just the same path generated.
    # In the actual code, deduplication happens via resolved_path = path.resolve()

    # Let's say we have:
    # input_path = repo_root / "Basics" / "lessons" / "slides" / "day-01" / "test.md"
    # output1 = Basics/lessons/slides/day-01/test.html
    # output2 = slides/basics/day-01/test.html

    # If we make slides/basics a symlink to Basics/lessons/slides
    (repo_root / "Basics" / "lessons" / "slides" / "day-01").mkdir(parents=True)
    (repo_root / "slides").mkdir()
    (repo_root / "slides" / "basics").symlink_to(repo_root / "Basics" / "lessons" / "slides")

    input_path = repo_root / "Basics" / "lessons" / "slides" / "day-01" / "test.md"

    # path1 = repo_root / "Basics" / "lessons" / "slides" / "day-01" / "test.html"
    # path2 = repo_root / "slides" / "basics" / "day-01" / "test.html"
    # path2.resolve() will be the same as path1.resolve()

    results = get_output_paths(input_path, repo_root)
    assert len(results) == 1
    assert results[0] == repo_root / "Basics" / "lessons" / "slides" / "day-01" / "test.html"

@pytest.mark.parametrize("input_rel, expected_rels", [
    ("Basics/lessons/slides/day-01/test.md", ["Basics/lessons/slides/day-01/test.html", "slides/basics/day-01/test.html"]),
    ("Advanced/lessons/slides/day-02/test.md", ["Advanced/lessons/slides/day-02/test.html", "slides/advanced/day-02/test.html"]),
    ("Basics/lessons/slides/intro.md", ["Basics/lessons/slides/intro.html"]),
    ("Other/lessons/slides/test.md", []),
])
def test_get_output_paths_parameterized(input_rel, expected_rels):
    repo_root = Path("/repo")
    input_path = repo_root / input_rel
    expected = [repo_root / rel for rel in expected_rels]
    assert get_output_paths(input_path, repo_root) == expected
