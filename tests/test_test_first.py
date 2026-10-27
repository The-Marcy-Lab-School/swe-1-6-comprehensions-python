"""Checks the test-first question.

tests/ is restored from the template before grading, so the student's own test
lives in student_tests/test_titles_by.py where it survives. These run that file
and check the three things the question asks for.
"""

import re
import subprocess
import sys
from pathlib import Path

from from_scratch import titles_by

TEST_SUITE_NAME = "Test First"

STUDENT = Path(__file__).resolve().parent.parent / "student_tests"
FILE = STUDENT / "test_titles_by.py"


def written():
    return FILE.read_text(encoding="utf-8") if FILE.is_file() else ""


def functions(text):
    return re.findall(r"^def (test_\w+)\s*\(", text, re.M)


def test_titles_by():
    """titles_by - the titles of every song by one artist, in playlist order"""
    playlist = [
        {"title": "Night Drive", "artist": "Nova", "seconds": 209, "plays": 120, "is_favorite": True},
        {"title": "Paper Boats", "artist": "The Tides", "seconds": 184, "plays": 0, "is_favorite": False},
        {"title": "Slow Burn", "artist": "Nova", "seconds": 251, "plays": 45, "is_favorite": True},
    ]
    assert titles_by(playlist, "Nova") == ["Night Drive", "Slow Burn"]
    assert titles_by(playlist, "The Tides") == ["Paper Boats"]
    assert titles_by(playlist, "Nobody") == []
    assert titles_by([], "Nova") == []


def test_two_tests_with_docstrings():
    """your tests - two test functions, each with a docstring"""
    text = written()
    names = functions(text)
    assert len(names) >= 2, (
        f"Expected two test functions in student_tests/test_titles_by.py, "
        f"found {len(names)}."
    )

    bodies = re.split(r"^def test_\w+\s*\([^)]*\):", text, flags=re.M)[1:]
    missing = [n for n, b in zip(names, bodies)
               if not re.match(r"\s*(\"\"\"|''')", b)]
    assert not missing, f"These need a docstring: {', '.join(missing)}"


def test_records_the_first_failure():
    """your tests - the error from the first run is recorded in a comment"""
    comments = "\n".join(re.findall(r"#.*", written()))
    assert "AssertionError" in comments, (
        "Paste the error from your first run into a comment at the top of "
        "student_tests/test_titles_by.py. The stub returns None, so the first "
        "run fails with an AssertionError."
    )


def test_student_tests_pass():
    """your tests - both of them pass against src/from_scratch.py"""
    if not functions(written()):
        raise AssertionError("No test functions written yet.")

    root = STUDENT.parent
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(FILE), "-q", "-p", "no:cacheprovider"],
        cwd=root, capture_output=True, text=True,
        env={"PYTHONPATH": str(root / "src"), "PATH": "/usr/bin:/bin"},
    )
    assert result.returncode == 0, (
        "Your own tests do not pass:\n" + result.stdout[-1500:]
    )
