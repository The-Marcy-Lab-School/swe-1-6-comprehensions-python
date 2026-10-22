from debug import any_expensive, top_three

TEST_SUITE_NAME = "Debug Tests"


def test_top_three():
    """top_three - returns the three HIGHEST scores"""
    assert top_three([10, 90, 50, 70, 30]) == [90, 70, 50]
    assert top_three([5, 1]) == [5, 1]
    assert top_three([]) == []


def test_any_expensive():
    """any_expensive - True if ANY product costs more than 100"""
    cheap = {"name": "Tea", "price": 4}
    pricey = {"name": "Pot", "price": 250}

    assert any_expensive([cheap, pricey]) is True
    assert any_expensive([cheap]) is False
    assert any_expensive([]) is False
