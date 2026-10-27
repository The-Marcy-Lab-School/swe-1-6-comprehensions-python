import ast
import inspect
import textwrap

from modify import get_favorites, get_titles, sorted_plays, total_seconds

TEST_SUITE_NAME = "Modify Tests"


def make_playlist():
    """A fresh playlist for every test, so no test can change another's data."""
    return [
        {"title": "Night Drive", "artist": "Nova", "seconds": 209, "plays": 120, "is_favorite": True},
        {"title": "Paper Boats", "artist": "The Tides", "seconds": 184, "plays": 0, "is_favorite": False},
        {"title": "Slow Burn", "artist": "Nova", "seconds": 251, "plays": 45, "is_favorite": True},
        {"title": "Static", "artist": "Kilo", "seconds": 158, "plays": 300, "is_favorite": False},
        {"title": "Low Tide", "artist": "The Tides", "seconds": 232, "plays": 0, "is_favorite": True},
    ]


def nodes_in(func):
    """Every piece of syntax in a function, read with Python's ast module.

    Reading the code with ast rather than searching it as text means that words
    in comments and strings never count. A comment that says "no for loop here"
    does not count as a for loop.
    """
    source = textwrap.dedent(inspect.getsource(func))
    return list(ast.walk(ast.parse(source)))


def has_for_loop(func):
    return any(isinstance(node, ast.For) for node in nodes_in(func))


def has_comprehension(func):
    return any(isinstance(node, (ast.ListComp, ast.GeneratorExp)) for node in nodes_in(func))


def methods_called_in(func):
    methods = set()
    for node in nodes_in(func):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            methods.add(node.func.attr)
    return methods


def test_total_seconds_still_works():
    """total_seconds - adds up the length of every song"""
    assert total_seconds(make_playlist()) == 1034
    assert total_seconds([]) == 0


def test_total_seconds_uses_sum():
    """total_seconds - sum() over a comprehension replaces the accumulator loop"""
    assert not has_for_loop(total_seconds), "Replace the for loop with sum()."
    assert has_comprehension(total_seconds), (
        "sum() needs a list of numbers. Build it from the playlist with a comprehension."
    )


def test_get_titles_still_works():
    """get_titles - returns every song's title, in order"""
    assert get_titles(make_playlist()) == ["Night Drive", "Paper Boats", "Slow Burn", "Static", "Low Tide"]
    assert get_titles([]) == []


def test_get_titles_is_a_comprehension():
    """get_titles - the loop is now a comprehension"""
    assert not has_for_loop(get_titles), "Replace the for loop with a comprehension."
    assert "append" not in methods_called_in(get_titles), "The accumulator list should be gone."


def test_get_favorites_still_works():
    """get_favorites - returns the favorite songs, in order"""
    favorites = get_favorites(make_playlist())
    assert [song["title"] for song in favorites] == ["Night Drive", "Slow Burn", "Low Tide"]
    assert get_favorites([]) == []


def test_get_favorites_is_a_comprehension():
    """get_favorites - the loop is now a comprehension with an if"""
    assert not has_for_loop(get_favorites), "Replace the for loop with a comprehension."
    assert "append" not in methods_called_in(get_favorites), "The accumulator list should be gone."


def test_sorted_plays_leaves_the_original_alone():
    """sorted_plays - returns a new list, highest first, and leaves the original alone"""
    plays = [45, 300, 0, 120]
    result = sorted_plays(plays)

    assert result == [300, 120, 45, 0]
    assert plays == [45, 300, 0, 120], "The caller's list must survive. .sort() changes it in place."
    assert result is not plays
    assert sorted_plays([]) == []
