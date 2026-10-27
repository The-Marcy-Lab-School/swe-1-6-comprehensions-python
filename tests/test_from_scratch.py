import ast
import inspect
import textwrap

from from_scratch import (
    count_by_artist,
    first_by_artist,
    first_unplayed_index,
    long_songs,
    longest_seconds,
    most_played,
    song_labels,
    top_plays,
    total_plays,
    unplayed_titles,
)

TEST_SUITE_NAME = "From Scratch Tests"


def make_playlist():
    """A fresh playlist for every test, so no test can change another's data."""
    return [
        {"title": "Night Drive", "artist": "Nova", "seconds": 209, "plays": 120, "is_favorite": True},
        {"title": "Paper Boats", "artist": "The Tides", "seconds": 184, "plays": 0, "is_favorite": False},
        {"title": "Slow Burn", "artist": "Nova", "seconds": 251, "plays": 45, "is_favorite": True},
        {"title": "Static", "artist": "Kilo", "seconds": 158, "plays": 300, "is_favorite": False},
        {"title": "Low Tide", "artist": "The Tides", "seconds": 232, "plays": 0, "is_favorite": True},
    ]


def uses_comprehension_not_loop(func):
    """True when a function builds its list with a comprehension and has no for loop.

    The code is read with Python's ast module rather than searched as text, so
    words in comments and strings never count.
    """
    source = textwrap.dedent(inspect.getsource(func))
    nodes = list(ast.walk(ast.parse(source)))
    has_loop = any(isinstance(node, ast.For) for node in nodes)
    has_comprehension = any(isinstance(node, (ast.ListComp, ast.GeneratorExp)) for node in nodes)
    return has_comprehension and not has_loop


def test_song_labels():
    """song_labels - one "title by artist" label per song"""
    assert song_labels(make_playlist()) == [
        "Night Drive by Nova",
        "Paper Boats by The Tides",
        "Slow Burn by Nova",
        "Static by Kilo",
        "Low Tide by The Tides",
    ]
    assert song_labels([]) == []


def test_song_labels_is_a_comprehension():
    """song_labels - written as a comprehension, not a for loop"""
    assert uses_comprehension_not_loop(song_labels), "Transforming is a job for a comprehension."


def test_long_songs():
    """long_songs - keeps the songs at least `min_seconds` long"""
    assert [song["title"] for song in long_songs(make_playlist(), 230)] == ["Slow Burn", "Low Tide"]
    assert [song["title"] for song in long_songs(make_playlist(), 251)] == ["Slow Burn"]
    assert long_songs(make_playlist(), 1000) == []
    assert long_songs([], 100) == []


def test_long_songs_is_a_comprehension():
    """long_songs - written as a comprehension with an if, not a for loop"""
    assert uses_comprehension_not_loop(long_songs), "Filtering is a job for a comprehension."


def test_unplayed_titles():
    """unplayed_titles - the titles of the songs with no plays"""
    assert unplayed_titles(make_playlist()) == ["Paper Boats", "Low Tide"]
    assert unplayed_titles([make_playlist()[0]]) == []
    assert unplayed_titles([]) == []


def test_unplayed_titles_is_a_comprehension():
    """unplayed_titles - one comprehension that filters and transforms"""
    assert uses_comprehension_not_loop(unplayed_titles), (
        "One comprehension can filter and transform at the same time."
    )


def test_total_plays():
    """total_plays - adds up the plays of every song"""
    assert total_plays(make_playlist()) == 465
    assert total_plays([]) == 0


def test_total_plays_uses_a_built_in():
    """total_plays - a built-in function over a comprehension, not a for loop"""
    assert uses_comprehension_not_loop(total_plays), "Python has a built-in function for this job."


def test_longest_seconds():
    """longest_seconds - the length of the longest song"""
    assert longest_seconds(make_playlist()) == 251
    assert longest_seconds([make_playlist()[3]]) == 158


def test_longest_seconds_uses_a_built_in():
    """longest_seconds - a built-in function over a comprehension, not a for loop"""
    assert uses_comprehension_not_loop(longest_seconds), "Python has a built-in function for this job."


def test_count_by_artist():
    """count_by_artist - a frequency counter of artists"""
    assert count_by_artist(make_playlist()) == {"Nova": 2, "The Tides": 2, "Kilo": 1}
    assert count_by_artist([make_playlist()[3]]) == {"Kilo": 1}
    assert count_by_artist([]) == {}


def test_most_played():
    """most_played - the whole record of the song with the most plays"""
    playlist = make_playlist()
    assert most_played(playlist) is playlist[3], "Return the song's record itself."
    assert most_played(playlist[:3])["title"] == "Night Drive"
    assert most_played([]) is None


def test_most_played_keeps_the_first_of_a_tie():
    """most_played - when two songs tie, the earlier one wins"""
    playlist = make_playlist()
    assert most_played([playlist[1], playlist[4]])["title"] == "Paper Boats"


def test_first_by_artist():
    """first_by_artist - the first song by an artist, or None"""
    playlist = make_playlist()
    assert first_by_artist(playlist, "Nova") is playlist[0]
    assert first_by_artist(playlist, "The Tides") is playlist[1]
    assert first_by_artist(playlist, "Nobody") is None
    assert first_by_artist([], "Nova") is None


def test_first_unplayed_index():
    """first_unplayed_index - the index of the first song with no plays, or -1"""
    playlist = make_playlist()
    assert first_unplayed_index(playlist) == 1
    assert first_unplayed_index([playlist[0], playlist[2], playlist[4]]) == 2
    assert first_unplayed_index([playlist[0], playlist[3]]) == -1
    assert first_unplayed_index([]) == -1


def test_top_plays():
    """top_plays - the n highest play counts, highest first"""
    assert top_plays(make_playlist(), 2) == [300, 120]
    assert top_plays(make_playlist(), 3) == [300, 120, 45]
    assert top_plays(make_playlist(), 10) == [300, 120, 45, 0, 0]
    assert top_plays([], 3) == []

    playlist = make_playlist()
    top_plays(playlist, 2)
    assert playlist == make_playlist(), "The playlist that went in must be unchanged."
