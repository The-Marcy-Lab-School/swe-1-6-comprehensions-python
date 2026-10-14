import builtins

import pytest
from modify import ask_for_number, run_menu_choice, safe_int, set_age

TEST_SUITE_NAME = "Modify Tests"


def test_run_menu_choice_uses_a_dictionary():
    """run_menu_choice - behaves the same, without an if/elif chain"""
    import inspect

    source = inspect.getsource(run_menu_choice)
    assert "elif" not in source, (
        "Replace the if/elif chain with a dictionary of functions."
    )

    tasks = []
    assert run_menu_choice("add", tasks) == "1 task(s)"
    assert run_menu_choice("add", tasks) == "2 task(s)"
    assert run_menu_choice("count", tasks) == "2 task(s)"
    assert run_menu_choice("clear", tasks) == "0 task(s)"
    assert run_menu_choice("nonsense", tasks) == "Unknown choice"


def test_safe_int_converts():
    """safe_int - converts a number written as text"""
    assert safe_int("25") == 25
    assert safe_int("0") == 0


def test_safe_int_returns_none_on_junk():
    """safe_int - returns None instead of raising on something unconvertible"""
    assert safe_int("abc") is None
    assert safe_int("") is None
    assert safe_int("3.5") is None


def test_set_age_accepts_a_sensible_age():
    """set_age - sets the age when it is in range"""
    person = {"name": "Ada"}
    assert set_age(person, 30)["age"] == 30
    assert set_age(person, 0)["age"] == 0


def test_set_age_raises_on_a_bad_age():
    """set_age - raises ValueError rather than storing nonsense"""
    with pytest.raises(ValueError):
        set_age({"name": "Ada"}, -1)
    with pytest.raises(ValueError):
        set_age({"name": "Ada"}, 200)


def feed(monkeypatch, answers):
    """Stand in for a person typing, one answer per input() call."""
    supply = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda *a: next(supply))


def test_ask_for_number_takes_the_first_good_answer(monkeypatch, capsys):
    """ask_for_number - returns straight away when the answer is a number"""
    feed(monkeypatch, ["25"])
    assert ask_for_number("Age: ") == 25
    capsys.readouterr()


def test_ask_for_number_keeps_asking(monkeypatch, capsys):
    """ask_for_number - asks again until int() succeeds"""
    feed(monkeypatch, ["abc", "", "3.5", "7"])
    assert ask_for_number("Age: ") == 7

    lines = []
    for line in capsys.readouterr().out.splitlines():
        if line.strip():
            lines.append(line)
    printed = lines
    assert len(printed) == 3, (
        "Each bad answer should say something before asking again."
    )
