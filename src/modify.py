def total_seconds(playlist):
    total = 0
    for song in playlist:
        total += song["seconds"]
    return total


def get_titles(playlist):
    titles = []
    for song in playlist:
        titles.append(song["title"])
    return titles


def get_favorites(playlist):
    favorites = []
    for song in playlist:
        if song["is_favorite"]:
            favorites.append(song)
    return favorites


def sorted_plays(plays):
    plays.sort(reverse=True)
    return plays
