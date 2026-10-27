def favorites_only(playlist):
    return [song["is_favorite"] for song in playlist]


def ranked_plays(playlist):
    plays = [song["plays"] for song in playlist]
    return plays.sort(reverse=True)


def find_song(playlist, title):
    for song in playlist:
        if song["title"] == title:
            return song
        else:
            return None


def plays_per_artist(playlist):
    for song in playlist:
        totals = {}
        totals[song["artist"]] = totals.get(song["artist"], 0) + song["plays"]
    return totals


def average_plays(playlist):
    plays = [song["plays"] for song in playlist]
    return sum(plays) / len(plays)


def sort_ratings(ratings):
    return sorted(ratings)


def shout_favorites(playlist):
    favorites = [song for song in playlist if song["is_favorite"]]
    for song in favorites:
        song["title"] = song["title"].upper()
    return favorites
