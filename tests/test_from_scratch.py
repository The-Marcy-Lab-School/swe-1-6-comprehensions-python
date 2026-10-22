import inspect

from from_scratch import (
    all_in_stock,
    cheapest,
    count_by_category,
    double_every_number,
    first_sold_out,
    flatten,
    in_stock,
    label_each,
    long_words,
    only_numbers,
    pair_up,
    total_price,
)

TEST_SUITE_NAME = "From Scratch Tests"

PRODUCTS = [
    {"name": "Tea", "price": 4, "stock": 12, "category": "drink"},
    {"name": "Mug", "price": 9, "stock": 0, "category": "kitchen"},
    {"name": "Pot", "price": 25, "stock": 3, "category": "kitchen"},
    {"name": "Cocoa", "price": 6, "stock": 0, "category": "drink"},
]


def is_comprehension(func):
    """One return, and a for inside brackets on that line."""
    body = [line.strip() for line in inspect.getsource(func).splitlines()[1:]
            if line.strip() and not line.strip().startswith(("#", '"', "'"))]
    return len(body) == 1 and body[0].startswith("return") and " for " in body[0]


def test_double_every_number():
    """double_every_number - returns a new list with each number doubled"""
    assert double_every_number([1, 2, 3]) == [2, 4, 6]
    assert double_every_number([]) == []

    nums = [1, 2, 3]
    assert double_every_number(nums) is not nums, "Return a NEW list."
    assert nums == [1, 2, 3]


def test_double_every_number_is_a_comprehension():
    """double_every_number - written as a list comprehension"""
    assert is_comprehension(double_every_number), (
        "Write this as a single return with a list comprehension."
    )


def test_long_words():
    """long_words - keeps only the words at least `minimum` letters long"""
    assert long_words(["hi", "hello", "hey"], 3) == ["hello", "hey"]
    assert long_words(["hi"], 5) == []


def test_in_stock():
    """in_stock - filters a list of dictionaries by one of their values"""
    assert [p["name"] for p in in_stock(PRODUCTS)] == ["Tea", "Pot"]
    assert in_stock([]) == []


def test_total_price():
    """total_price - combines the prices into one number"""
    assert total_price(PRODUCTS) == 44
    assert total_price([]) == 0


def test_cheapest():
    """cheapest - returns the product with the lowest price"""
    assert cheapest(PRODUCTS)["name"] == "Tea"
    assert cheapest([]) is None


def test_first_sold_out():
    """first_sold_out - returns the first product with no stock, or None"""
    assert first_sold_out(PRODUCTS)["name"] == "Mug"
    assert first_sold_out([PRODUCTS[0]]) is None
    assert first_sold_out([]) is None


def test_count_by_category():
    """count_by_category - a frequency counter built with .get(key, 0)"""
    assert count_by_category(PRODUCTS) == {"drink": 2, "kitchen": 2}
    assert count_by_category([]) == {}


def test_label_each():
    """label_each - numbers each word, counting from 1"""
    assert label_each(["a", "b"]) == ["1. a", "2. b"]
    assert label_each([]) == []


def test_pair_up():
    """pair_up - matches each name to the score in the same position"""
    assert pair_up(["Ada", "Zo"], [90, 80]) == {"Ada": 90, "Zo": 80}
    assert pair_up([], []) == {}
    # zip stops at the shorter one, which is the behaviour we want here.
    assert pair_up(["Ada", "Zo"], [90]) == {"Ada": 90}


def test_all_in_stock():
    """all_in_stock - True only when every product has stock"""
    assert all_in_stock(PRODUCTS) is False
    assert all_in_stock([PRODUCTS[0], PRODUCTS[2]]) is True
    assert all_in_stock([]) is True


def test_flatten():
    """flatten - one flat list out of a list of rows"""
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[1], [], [2, 3]]) == [1, 2, 3]
    assert flatten([]) == []


def test_flatten_leaves_the_rows_alone():
    """flatten - the grid that went in is unchanged"""
    grid = [[1, 2], [3]]
    flatten(grid)
    assert grid == [[1, 2], [3]]


def test_only_numbers():
    """only_numbers - keeps ints and floats, drops everything else"""
    assert only_numbers([1, "two", 3.5, None, 4]) == [1, 3.5, 4]
    assert only_numbers(["a", None]) == []
    assert only_numbers([]) == []


def test_only_numbers_drops_booleans():
    """only_numbers - a bool is an int, and still does not count"""
    assert only_numbers([True, 7, False]) == [7]
