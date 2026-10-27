from debug import (
    average_plays,
    favorites_only,
    find_song,
    plays_per_artist,
    ranked_plays,
    shout_favorites,
    sort_ratings,
)

TEST_SUITE_NAME = "Debug Tests"


def make_playlist():
    """A fresh playlist for every test, so no test can change another's data."""
    return [
        {"title": "Night Drive", "artist": "Nova", "seconds": 209, "plays": 120, "is_favorite": True},
        {"title": "Paper Boats", "artist": "The Tides", "seconds": 184, "plays": 0, "is_favorite": False},
        {"title": "Slow Burn", "artist": "Nova", "seconds": 251, "plays": 45, "is_favorite": True},
        {"title": "Static", "artist": "Kilo", "seconds": 158, "plays": 300, "is_favorite": False},
        {"title": "Low Tide", "artist": "The Tides", "seconds": 232, "plays": 0, "is_favorite": True},
    ]


def test_favorites_only():
    """favorites_only - returns the favorite songs' records"""
    favorites = favorites_only(make_playlist())
    assert isinstance(favorites[0], dict), "Return the song records, not True and False."
    assert [song["title"] for song in favorites] == ["Night Drive", "Slow Burn", "Low Tide"]
    assert favorites_only([]) == []


def test_ranked_plays():
    """ranked_plays - every play count, highest first"""
    assert ranked_plays(make_playlist()) == [300, 120, 45, 0, 0]
    assert ranked_plays([]) == []


def test_find_song():
    """find_song - finds a song anywhere in the playlist, not just at the start"""
    playlist = make_playlist()
    assert find_song(playlist, "Night Drive") is playlist[0]
    assert find_song(playlist, "Static") is playlist[3]
    assert find_song(playlist, "Low Tide") is playlist[4]
    assert find_song(playlist, "Nothing Here") is None
    assert find_song([], "Static") is None


def test_plays_per_artist():
    """plays_per_artist - totals the plays for every artist"""
    assert plays_per_artist(make_playlist()) == {"Nova": 165, "The Tides": 0, "Kilo": 300}


def test_plays_per_artist_empty():
    """plays_per_artist - an empty playlist gives an empty dictionary"""
    assert plays_per_artist([]) == {}


def test_average_plays():
    """average_plays - the mean number of plays"""
    assert average_plays(make_playlist()) == 93
    assert average_plays([make_playlist()[3]]) == 300


def test_average_plays_empty():
    """average_plays - an empty playlist averages 0 instead of crashing"""
    assert average_plays([]) == 0


def test_sort_ratings():
    """sort_ratings - typed-in ratings come back as numbers, lowest first"""
    assert sort_ratings(["9", "10", "7"]) == [7, 9, 10]
    assert sort_ratings(["3", "20", "100"]) == [3, 20, 100]
    assert sort_ratings([]) == []


def test_shout_favorites():
    """shout_favorites - returns the favorites with their titles in capitals"""
    shouted = shout_favorites(make_playlist())
    assert [song["title"] for song in shouted] == ["NIGHT DRIVE", "SLOW BURN", "LOW TIDE"]
    assert shouted[0]["artist"] == "Nova", "Keep every other key in each record."


def test_shout_favorites_leaves_the_playlist_alone():
    """shout_favorites - the titles in the original playlist do not change"""
    playlist = make_playlist()
    shout_favorites(playlist)
    assert [song["title"] for song in playlist] == [
        "Night Drive", "Paper Boats", "Slow Burn", "Static", "Low Tide",
    ], "The original playlist's titles changed. Which dictionaries does the filtered list hold?"
