# Comprehensions and Built-in Iteration

Practice naming the job a loop does and choosing the tool built for that job.

**Practicing:** list comprehensions, `sum()`/`min()`/`max()`/`len()`, the accumulator pattern, frequency counters, finding the first match, `sorted()` and `.sort()`

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [Modify](#modify)
  - [Question 1: `total_seconds`](#question-1-total_seconds)
  - [Question 2: `get_titles`](#question-2-get_titles)
  - [Question 3: `get_favorites`](#question-3-get_favorites)
  - [Question 4: `sorted_plays`](#question-4-sorted_plays)
- [Debug](#debug)
  - [Question 5: `favorites_only`](#question-5-favorites_only)
  - [Question 6: `ranked_plays`](#question-6-ranked_plays)
  - [Question 7: `find_song`](#question-7-find_song)
  - [Question 8: `plays_per_artist`](#question-8-plays_per_artist)
  - [Question 9: `average_plays`](#question-9-average_plays)
  - [Question 10: `sort_ratings`](#question-10-sort_ratings)
  - [Question 11: `shout_favorites`](#question-11-shout_favorites)
- [From Scratch](#from-scratch)
  - [Question 12: `song_labels`](#question-12-song_labels)
  - [Question 13: `long_songs`](#question-13-long_songs)
  - [Question 14: `unplayed_titles`](#question-14-unplayed_titles)
  - [Question 15: `total_plays`](#question-15-total_plays)
  - [Question 16: `longest_seconds`](#question-16-longest_seconds)
  - [Question 17: `count_by_artist`](#question-17-count_by_artist)
  - [Question 18: `most_played`](#question-18-most_played)
  - [Question 19: `first_by_artist`](#question-19-first_by_artist)
  - [Question 20: `first_unplayed_index`](#question-20-first_unplayed_index)
  - [Question 21: `top_plays`](#question-21-top_plays)
  - [Question 22: test first, then write it](#question-22-test-first-then-write-it)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine, and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you write every line you submit. For this assignment that means asking it to read a comprehension back to you in plain English, or having it show you a loop and quiz you on which job the loop does. Ask it a hundred questions — that is the whole point. What you do not do is ask it for the function. Paste this at the start of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question is asking, clarify confusing wording, and highlight the relevant concepts I need to know — but do not provide the full solution or code that directly answers the question. Instead, rephrase the problem in simpler terms, identify what is being tested, and suggest what steps or thought processes might help. Ask me guiding questions to make sure I am thinking critically. Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from it, and then you verify that code line by line. For this assignment your spec has to name the job each function does and the tool you expect for it. A comprehension is where generated code most often looks right and is not, so read every one it hands you from the `for` outward before you keep it.

You own every line either way, and you will be asked to explain it.

## Setup

Clone your repository in `development/mod-1` and then `cd` into it. Set up your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k total_plays` for one question. Every push runs the tests on GitHub and reports your score in the **Actions** tab.

75% of tests passing counts as complete. Submit at that point even if it is not perfect. Treat submitting as a checkpoint rather than a finish line, and come back to improve it.

When you are done working on this assignment, turn off your virtual environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. Modify
2. Debug
3. From Scratch

Modify comes first as a warm-up. Every Modify question starts from a loop that already works, and you rewrite it with a shorter tool. Debug comes next. Each Debug question hides a surprise about one of this lesson's tools, and finding the surprise in someone else's code first means you are less likely to write it into your own. From Scratch comes last, and there you choose the tool for each job yourself.

Every question names the section of the lesson that teaches its tool. If a question uses a tool you have not seen yet, read that section first.

Almost every question uses a playlist: a list of song records that all have the same keys.

```python
{"title": "Night Drive", "artist": "Nova", "seconds": 209, "plays": 120, "is_favorite": True}
```

**Before you write any function, name the job it does.** Each job has its own tool:

| Job                                                | Tool                                                           |
| -------------------------------------------------- | -------------------------------------------------------------- |
| Do something with every value, such as printing it | a `for` loop                                                   |
| Transform every value into a new list              | a list comprehension                                           |
| Keep the values that pass a test (filter)          | a list comprehension with `if`                                 |
| Combine every value into one                       | `sum()`, `min()`, `max()`, `len()`, or the accumulator pattern |
| Find the first value that passes a test            | a `for` loop with an early `return`                            |
| Put the values in order                            | `sorted()` or `.sort()`                                        |

Read a comprehension **from the `for` outward**, not left to right:

```python
[song["title"] for song in playlist]
#                  ^-- start here: "for each song in playlist"
#  ^-- then this: "give me song["title"]"
```

Some tests check which tool you used, not only what your function returns. When a question names a tool, use that tool.

One question asks you to write a test before you write the function, in a `student_tests/` folder of your own. The grader replaces `tests/` before it runs, so that folder is where your own tests are safe.

## Modify

Rewrite the four functions in `src/modify.py`. Every test that checks a function's results already passes before you change anything, and it has to keep passing after you change it. That is how you know the rewrite does exactly what the loop did.

### Question 1: `total_seconds`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _`sum()`, `min()`, `max()`, and `len()`_

`total_seconds` adds up the length of every song with an accumulator loop. Rewrite it with `sum()`.

```python
total_seconds(playlist)
# 1034 — the same answer before and after
total_seconds([])
# 0
```

`sum()` needs a list of numbers, and `playlist` is a list of records. Build the list of numbers with a comprehension first. The tests check that the `for` loop is gone.

### Question 2: `get_titles`

**Lesson section:** _2. Transforming with List Comprehensions_

`get_titles` builds a list of titles with a loop and `.append()`. Rewrite it as a comprehension, keeping the results identical.

The tests check that the `for` loop and the `.append()` are gone.

### Question 3: `get_favorites`

**Lesson section:** _3. Filtering with an `if`_

`get_favorites` builds a list of the favorite songs with a loop, an `if`, and `.append()`. Rewrite it as a comprehension, keeping the results identical.

The tests check that the `for` loop and the `.append()` are gone.

### Question 4: `sorted_plays`

**Lesson section:** _6. Sorting with `sorted()` and `.sort()`_

`sorted_plays` takes a list of play counts and returns them highest first. It also reorders the caller's list, which the caller never asked for. Change it so the caller's list survives.

```python
plays = [45, 300, 0, 120]
sorted_plays(plays)
# returns [300, 120, 45, 0]
# plays is still [45, 300, 0, 120]
```

`.sort()` changes a list in place. Python has a second sorting tool that leaves the original alone and returns a new list.

## Debug

Fix the seven functions in `src/debug.py`. Each one runs without a syntax error and gives the wrong answer, or crashes, for a reason that has to do with how one of this lesson's tools behaves. Before you change anything, predict why it goes wrong, then use `print()` or `src/playground.py` to check your prediction.

### Question 5: `favorites_only`

**Lesson section:** _3. Filtering with an `if`_

`favorites_only` should return the favorite song records. It returns a list of `True` and `False` instead.

```python
favorites_only(playlist)
# want the Night Drive, Slow Burn and Low Tide records
# gets [True, False, True, False, True]
```

Read the comprehension from the `for` outward. Which part decides what is collected, and which part decides what is kept?

### Question 6: `ranked_plays`

**Lesson section:** _6. Sorting with `sorted()` and `.sort()`_, in the _Predict, then run_ box about `.sort()`

`ranked_plays` should return every play count, highest first. It returns `None`.

```python
ranked_plays(playlist)
# want [300, 120, 45, 0, 0], gets None
```

The play counts are sorted correctly. Work out where they went.

### Question 7: `find_song`

**Lesson section:** _5. Finding the First Match_

`find_song` should return the record of the song with a given title. It finds the first song and nothing else.

```python
find_song(playlist, "Night Drive")["title"]
# "Night Drive" — works
find_song(playlist, "Static")
# want the Static record, gets None
```

Trace the loop by hand for `"Static"`. How many songs does it look at before it returns?

### Question 8: `plays_per_artist`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _The Accumulator Pattern_ and _Generating a Frequency Counter_

`plays_per_artist` should total the plays for every artist. It only ever remembers the last song, and it crashes on an empty playlist.

```python
plays_per_artist(playlist)
# want {"Nova": 165, "The Tides": 0, "Kilo": 300}, gets {"The Tides": 0}
plays_per_artist([])
# want {}, gets UnboundLocalError
```

An accumulator has three parts: the starting value, the combining step, and the return. One of them is in the wrong place, and moving it fixes both problems.

### Question 9: `average_plays`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _`sum()`, `min()`, `max()`, and `len()`_

`average_plays` should return the average number of plays. It works for a full playlist and crashes on an empty one.

```python
average_plays(playlist)
# 93.0 — works
average_plays([])
# want 0, gets ZeroDivisionError
```

An empty playlist is a real case: a user who just signed up has one. Handle it before the division happens.

### Question 10: `sort_ratings`

**Lesson section:** _6. Sorting with `sorted()` and `.sort()`_, and _2. Transforming with List Comprehensions_

`sort_ratings` takes ratings that users typed in, so every rating is a string. It should return them as numbers, lowest first. It puts them in a strange order and leaves them as strings.

```python
sort_ratings(["9", "10", "7"])
# want [7, 9, 10], gets ["10", "7", "9"]
```

Strings are sorted one character at a time, the way words are put in alphabetical order, so `"10"` comes before `"7"` because `"1"` comes before `"7"`. Turn the strings into numbers before you sort them. A comprehension can do that in one step.

### Question 11: `shout_favorites`

**Lesson section:** _Advanced Topics_, under _A New List Shares Its Dictionaries_

`shout_favorites` should return the favorite songs with their titles in capital letters. The returned titles are correct, but the titles in the **original** playlist change too.

```python
shout_favorites(playlist)
# returns the favorites titled "NIGHT DRIVE", "SLOW BURN", and "LOW TIDE" — correct
playlist[0]["title"]
# want "Night Drive", gets "NIGHT DRIVE"
```

The comprehension builds a new list. Work out whether it also builds new dictionaries, or whether the new list holds the same dictionaries as `playlist`. The Advanced Topics section of the lesson covers this.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 12: `song_labels`

**Lesson section:** _2. Transforming with List Comprehensions_

Write a function `song_labels` that returns a **new** list with one label for each song.

```python
song_labels(playlist)
# ["Night Drive by Nova", "Paper Boats by The Tides", ...] — one label per song
song_labels([])
# []
```

Write this one as a comprehension. The tests check that there is no `for` loop.

### Question 13: `long_songs`

**Lesson section:** _3. Filtering with an `if`_

Write a function `long_songs` that takes a playlist and a `min_seconds`, and returns the song records that are at least that long.

```python
long_songs(playlist, 230)
# the Slow Burn and Low Tide records — 251 and 232 seconds
long_songs(playlist, 1000)
# [] — no song is that long
```

Write this one as a comprehension too. The test reaches into each record for its `"seconds"`.

### Question 14: `unplayed_titles`

**Lesson section:** _3. Filtering with an `if`_, where one comprehension transforms and filters

Write a function `unplayed_titles` that returns the **titles** of the songs that have never been played.

```python
unplayed_titles(playlist)
# ["Paper Boats", "Low Tide"] — the two songs with 0 plays
```

This question does two jobs at once. One comprehension can do both: the `if` decides which songs to keep, and the expression before the `for` decides what to collect from each one.

### Question 15: `total_plays`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _`sum()`, `min()`, `max()`, and `len()`_

Write a function `total_plays` that adds up the plays of every song.

```python
total_plays(playlist)
# 465
total_plays([])
# 0
```

The tests check that there is no `for` loop. Python has a built-in function for this job.

### Question 16: `longest_seconds`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _`sum()`, `min()`, `max()`, and `len()`_

Write a function `longest_seconds` that returns the length, in seconds, of the longest song.

```python
longest_seconds(playlist)
# 251 — Slow Burn
```

Same shape as `total_plays`, with a different built-in function. The tests check that there is no `for` loop.

### Question 17: `count_by_artist`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _Generating a Frequency Counter_

Write a function `count_by_artist` that counts how many songs each artist has on the playlist.

```python
count_by_artist(playlist)
# {"Nova": 2, "The Tides": 2, "Kilo": 1}
count_by_artist([])
# {}
```

This is a frequency counter: an accumulator whose starting value is an empty dictionary. It builds a lookup table that maps each artist to the number of songs by that artist. The first time an artist appears, the artist is not a key yet. Think about which way of reading a dictionary can handle a missing key.

### Question 18: `most_played`

**Lesson section:** _4. Reduce a List of Values Into One Value_, under _The Accumulator Pattern_

Write a function `most_played` that returns the **whole record** of the song with the most plays, or `None` when the playlist is empty.

```python
most_played(playlist)["title"]
# "Static" — 300 plays
most_played([])
# None
```

`max()` can tell you the highest number of plays, but not which song has it. None of the built-in functions does this job, so write an accumulator. Start with the first song in the playlist, and replace it only when the current song has more plays than the song you are holding. An empty playlist has no first song, so handle that case before the loop.

When two songs tie, return the one that comes first in the playlist.

### Question 19: `first_by_artist`

**Lesson section:** _5. Finding the First Match_

Write a function `first_by_artist` that returns the **first** song record by a given artist, or `None` when the artist has no songs on the playlist.

```python
first_by_artist(playlist, "Nova")["title"]
# "Night Drive" — Slow Burn is by Nova too, but it comes later
first_by_artist(playlist, "Nobody")
# None
```

This one is **not** a comprehension. A comprehension checks every song before it finishes, and this question is done the moment it finds one. Use a loop with an early `return`.

### Question 20: `first_unplayed_index`

**Lesson section:** _5. Finding the First Match_

Write a function `first_unplayed_index` that returns the **index** of the first song with no plays, or `-1` when every song has been played.

```python
first_unplayed_index(playlist)
# 1 — Paper Boats, the second song
first_unplayed_index([])
# -1
```

Same job as `first_by_artist`, but the answer is a position instead of a record. `enumerate()` gives you the index and the song together.

### Question 21: `top_plays`

**Lesson section:** _Combining Steps_

Write a function `top_plays` that takes a playlist and a number `n`, and returns the `n` highest play counts, highest first.

```python
top_plays(playlist, 2)
# [300, 120]
top_plays(playlist, 10)
# [300, 120, 45, 0, 0] — there are only five songs, so you get all five
```

This question does three jobs in a row. Name each one, write each one on its own line, and give each result a name. The playlist that went in must be unchanged.

### Question 22: test first, then write it

**Lesson section:** _3. Filtering with an `if`_, and the Test-Driven Development lesson for writing the test first

`src/from_scratch.py` has a stub for `titles_by`, which returns nothing. Here is the whole requirement, in words:

> `titles_by` takes a playlist and an artist, and returns the titles of every song by that artist, in playlist order. When the artist has no songs on the playlist, it returns an empty list.

Work in this order, and do not skip to the end:

- Write one test for that requirement in `student_tests/test_titles_by.py`.
- Run it. It fails, because the stub returns `None`. Paste that error into a comment at the top of the file.
- Now write `titles_by` so the test passes.
- Add a second test, for an artist with no songs on the playlist, and make that pass too.

```sh
python3 -m pytest student_tests
```

That order is the point of the question. A test written after the fact tends to agree with whatever you already wrote, including the parts that are wrong. A test written first is a statement of what the function owes you, and the failure proves the test can actually tell.

**Your tests go in `student_tests/`, not `tests/`.** The grader replaces `tests/` with its own copy, so anything you write there is thrown away. `student_tests/` is yours and is never touched. The grader checks that you have two tests with docstrings, that the recorded error is there, and that both tests pass.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score, then open a pull request to your instructor for feedback.

## Good luck!

This is the last Mod 1 assignment, and the one that makes your earlier code look long. You got this!
