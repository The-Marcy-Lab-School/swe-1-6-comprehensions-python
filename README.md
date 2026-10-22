# Comprehensions and Built-in Iteration

Practice saying in one line what used to take a loop, and knowing when not to.

**Practicing:** list comprehensions, `sum`/`min`/`max`, `sorted`, `enumerate`,
`zip`, `any`, `all`

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `double_every_number`](#question-1-double_every_number)
  - [Question 2: `long_words`](#question-2-long_words)
  - [Question 3: `in_stock`](#question-3-in_stock)
  - [Question 4: `total_price`](#question-4-total_price)
  - [Question 5: `cheapest`](#question-5-cheapest)
  - [Question 6: `first_sold_out`](#question-6-first_sold_out)
  - [Question 7: `count_by_category`](#question-7-count_by_category)
  - [Question 8: `label_each`](#question-8-label_each)
  - [Question 9: `pair_up`](#question-9-pair_up)
  - [Question 10: `all_in_stock`](#question-10-all_in_stock)
  - [Question 11: `flatten`](#question-11-flatten)
  - [Question 12: `only_numbers`](#question-12-only_numbers)
  - [Question 13: test first, then write it](#question-13-test-first-then-write-it)
- [Modify](#modify)
  - [Question 14: `squares_of`](#question-14-squares_of)
  - [Question 15: `sorted_names`](#question-15-sorted_names)
- [Debug](#debug)
  - [Question 16: `top_three`](#question-16-top_three)
  - [Question 17: `any_expensive`](#question-17-any_expensive)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it to read
a comprehension back to you in plain English, or having it quiz you on when a
plain loop is the better choice. Ask it a hundred questions — that is the
whole point. What you do not do is ask it for the function. Paste this at the
start of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. A comprehension is where
generated code most often looks right and is not, so read every one it hands
you from the `for` outward before you keep it.

You own every line either way, and you will be asked to explain it.

## Setup

Clone your repository in `development/mod-1` and then `cd` into it. Set up
your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k in_stock` for one
question. Every push runs the tests on GitHub and reports your score in the
**Actions** tab.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

When you are done working on this assignment, turn off your virtual
environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. From Scratch
2. Modify
3. Debug

Read a comprehension **from the `for` outward**, not left to right:

```python
[num * 2 for num in nums]
#         ^-- start here: "for each num in nums"
#  ^-- then this: "give me num * 2"
```

Most questions here use the same list of products:

```python
{"name": "Tea", "price": 4, "stock": 12, "category": "drink"}
```

**A comprehension is not always the answer.** Two questions here are
deliberately not comprehensions, and the right tool is named in each. The
[comprehension section of the Python tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
is the reference worth keeping open.

One question asks you to write a test before you write the function, in a
`student_tests/` folder of your own. The grader replaces `tests/` before it
runs, so that folder is where your own tests are safe.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `double_every_number`

Write a function `double_every_number` that returns a **new** list with every
number doubled.

```python
double_every_number([1, 2, 3])
# [2, 4, 6] — a new list, the original untouched
double_every_number([])
# [] — nothing in, nothing out
```

Write this one as a comprehension. The tests check that the body is a single
`return`.

### Question 2: `long_words`

Write a function `long_words` that takes a list of words and a `minimum`, and
returns the words at least that many letters long.

```python
long_words(["hi", "hello", "hey"], 3)
# ["hello", "hey"] — "hi" is two letters, so it is dropped
```

A comprehension can end with an `if`, which keeps only the values that pass.

### Question 3: `in_stock`

Write a function `in_stock` that returns the products with stock left.

```python
in_stock(products)
# the Tea and Pot dictionaries — Mug and Cocoa are at 0
```

Same shape as `long_words`, with the test reaching into each dictionary.

### Question 4: `total_price`

Write a function `total_price` that adds up every product's price.

```python
total_price(products)
# 44 — 4 + 9 + 25 + 6
total_price([])
# 0
```

A comprehension builds a list. This question wants one number out of many, and
Python has a built-in for exactly that.

### Question 5: `cheapest`

Write a function `cheapest` that returns the product with the lowest price, or
`None` when there are no products.

```python
cheapest(products)["name"]
# "Tea" — at 4, the lowest price
cheapest([])
# None
```

`min()` takes the same `key=` argument `max()` does.

### Question 6: `first_sold_out`

Write a function `first_sold_out` that returns the **first** product with no
stock, or `None` when every product has some.

```python
first_sold_out(products)["name"]
# "Mug" — the first one at 0, and it stops looking there
first_sold_out([])
# None
```

This one is **not** a comprehension. A comprehension visits every value before
it finishes, and this question is done the moment it finds one. Use a loop
with an early `return`.

### Question 7: `count_by_category`

Write a function `count_by_category` that counts how many products are in each
category.

```python
count_by_category(products)
# {"drink": 2, "kitchen": 2}
count_by_category([])
# {}
```

This one is **not** a comprehension either. You are building a dictionary up
as you go, and each step depends on what is already in it.

Hint: a dictionary's `.get()` takes a second argument, which it returns when
the key is not there yet. That saves writing an `if` to check whether you have
seen a category before.

### Question 8: `label_each`

Write a function `label_each` that numbers each word, starting at 1.

```python
label_each(["a", "b"])
# ["1. a", "2. b"] — numbered from one, not zero
```

Hint: `enumerate()` gives you the position and the value together, and it
takes a `start=` argument.

### Question 9: `pair_up`

Write a function `pair_up` that matches each name to the score in the same
position.

```python
pair_up(["Ada", "Zo"], [90, 80])
# {"Ada": 90, "Zo": 80}
pair_up(["Ada", "Zo"], [90])
# {"Ada": 90} — zip stops at the shorter list
```

Hint: `zip()` walks two lists side by side. A comprehension with `{}` instead
of `[]` builds a dictionary.

### Question 10: `all_in_stock`

Write a function `all_in_stock` that returns `True` only when every product
has stock.

```python
all_in_stock(products)
# False — Mug and Cocoa are at 0
all_in_stock([])
# True
```

That empty case surprises people, and it is not a quirk. "Every product has
stock" is true of no products, because there is none without.

### Question 11: `flatten`

Write a function `flatten` that takes a list of rows and returns every number
in them as one flat list.

```python
flatten([[1, 2], [3, 4]])
# [1, 2, 3, 4] — both rows, end to end
flatten([[1], [], [2, 3]])
# [1, 2, 3] — the empty row contributes nothing
flatten([])
# [] — no rows, no numbers
```

A comprehension can have **two `for` clauses**, and they read in the same
order you would write the nested loop: the outer one first, then the inner
one.

```py
for row in grid:         # outer
    for number in row:   # inner
```

Put those two in one comprehension, in that order, and take `number` as the
result. Getting them the wrong way round is the mistake to watch for, because
`row` has to exist before anything can loop over it.

### Question 12: `only_numbers`

Write a function `only_numbers` that takes a list of mixed values and returns
a **new** list of just the numbers. Booleans do not count as numbers here.

```python
only_numbers([1, "two", 3.5, None, 4])
# [1, 3.5, 4] — the string and the None are gone
only_numbers([True, 7, False])
# [7] — the booleans are gone too
only_numbers(["a", None])
# [] — nothing numeric in there
```

[`isinstance(value, int)`](https://docs.python.org/3/library/functions.html#isinstance)
asks whether a value is of a given type, and it takes a **tuple** of types
when more than one will do. It is what you want here rather than
`type(value) == int`, because it is the check Python programmers read and
write.

That second example is the catch. In Python a `bool` **is** an `int`, so
`isinstance(True, int)` comes back `True` and `True` sneaks into your list.
Your condition needs a second part that rules booleans out.

### Question 13: test first, then write it

`src/from_scratch.py` has a stub for `initials`, which returns nothing. Here
is the whole requirement, in words:

> `initials` takes a full name and returns one initial per part of it, each
> capitalized and followed by a dot. `"Ada Lovelace"` gives `"A.L."`.

Work in this order, and do not skip to the end:

- Write one test for that requirement in `student_tests/test_initials.py`.
- Run it. It fails, because the stub returns `None`. Paste that error into a
  comment at the top of the file.
- Now write `initials` so the test passes.
- Add a second test, for a name with a middle name, and make that pass too.

```sh
python3 -m pytest student_tests
```

That order is the point of the question. A test written after the fact tends
to agree with whatever you already wrote, including the parts that are wrong.
A test written first is a statement of what the function owes you, and the
failure proves the test can actually tell.

**Your tests go in `student_tests/`, not `tests/`.** The grader replaces
`tests/` with its own copy, so anything you write there is thrown away.
`student_tests/` is yours and is never touched. The grader checks you have two
tests with docstrings, that the recorded error is there, and that both tests
pass.

## Modify

### Question 14: `squares_of`

`squares_of` builds its list with a loop and an accumulator. Rewrite it as a
comprehension, keeping the results identical.

The tests check the `append` is gone and the body is one line.

### Question 15: `sorted_names`

`sorted_names` sorts the caller's list in place and hands it back. Change it so
the caller's list survives.

```python
users = [{"name": "Zo"}, {"name": "Ada"}]
sorted_names(users)
# returns Ada then Zo
# users is still Zo then Ada
```

`.sort()` changes a list in place and returns `None`. `sorted()` leaves the
original alone and returns a new list. That difference is why
`result = nums.sort()` is a bug people write once and never forget.

## Debug

### Question 16: `top_three`

`top_three` should return the three **highest** scores. It returns the three
lowest.

```python
top_three([10, 90, 50, 70, 30])
# want [90, 70, 50], gets [10, 30, 50]
```

`sorted()` takes one more argument than it is being given here.

### Question 17: `any_expensive`

`any_expensive` should return `True` if **any** product costs more than 100.
It only ever looks at the first one.

```python
any_expensive([cheap, pricey])
# want True, gets False
```

Work out why the loop never reaches the second product. Then replace the whole
thing with the built-in that answers this exact question.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

This is the last Mod 1 assignment, and the one that makes your earlier code
look long. You got this!
