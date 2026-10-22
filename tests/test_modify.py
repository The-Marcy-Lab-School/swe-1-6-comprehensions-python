import inspect

from modify import sorted_names, squares_of

TEST_SUITE_NAME = "Modify Tests"


def test_squares_of_still_works():
    """squares_of - same results after the refactor"""
    assert squares_of([1, 2, 3]) == [1, 4, 9]
    assert squares_of([]) == []
    assert squares_of([-2]) == [4]


def test_squares_of_is_a_comprehension():
    """squares_of - the loop is now a comprehension"""
    body = [line.strip() for line in inspect.getsource(squares_of).splitlines()[1:]
            if line.strip() and not line.strip().startswith("#")]
    assert len(body) == 1, "One line: a return with a comprehension."
    assert "append" not in body[0], "The accumulator list should be gone."


def test_sorted_names_is_pure():
    """sorted_names - returns a sorted list and leaves the original alone"""
    users = [{"name": "Zo"}, {"name": "Ada"}]
    result = sorted_names(users)

    assert [u["name"] for u in result] == ["Ada", "Zo"]
    assert [u["name"] for u in users] == ["Zo", "Ada"], (
        "The caller's list must survive. .sort() changes it in place."
    )
    assert result is not users
