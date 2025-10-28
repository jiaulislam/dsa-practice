import sys
import os
import pytest
from solutions.array.week_1_001_contains_duplicate import contains_duplicate

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # simple true case: duplicate within k
        ([1, 2, 3, 1], 3, True),
        # duplicate but beyond k → false
        ([1, 2, 3, 1], 2, False),
        # multiple duplicates; one pair within k
        ([1, 0, 1, 1], 1, True),
        # no duplicates at all
        ([1, 2, 3, 4], 1, False),
        # duplicates but exactly at k distance
        ([1, 2, 3, 1, 2, 3], 3, True),
        # duplicates separated by > k
        ([1, 2, 3, 1, 2, 3], 2, False),
        # duplicates adjacent
        ([99, 99], 1, True),
        # large k bigger than array length
        ([5, 6, 5], 10, True),
        # empty array
        ([], 1, False),
        # single element
        ([7], 0, False),  # there is no pair of distinct indices
    ],
)
def test_contains_nearby_duplicate(nums, k, expected):
    assert contains_duplicate(nums, k) is expected


def test_invalid_k_negative():
    """If k is negative maybe your function should treat as no valid distance → always False."""
    assert contains_duplicate([1, 1], -1) is False


def test_duplicates_many_times():
    nums = [1, 2, 1, 3, 1, 2, 1]
    # there are many 1's; we set k small so that the only valid one is when indices are close
    assert contains_duplicate(nums, 2) is True
