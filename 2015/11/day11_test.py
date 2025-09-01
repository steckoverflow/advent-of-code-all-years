import pytest
from day11 import contains_two_pairs


@pytest.mark.parametrize(
    "i,o",
    [
        ([1, 1, 2, 2], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 4, 5, 6, 6], True),
        ([1, 2, 3, 4, 5, 6], False),
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([8, 5, 17, 1, 2, 2, 26, 15], False),
    ],
)
def test_two_pairs(i, o):
    r = contains_two_pairs(i)
    assert r == o
