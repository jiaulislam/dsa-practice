import sys
import os
import pytest
from typing import List
from solutions.array.sliding_window_technique import max_sum_subarray

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestMaxSumSubarray:
    def test_basic_positive_case(self):
        """Test with basic positive numbers"""
        arr = [1, 4, 2, 9, 5]
        k = 3
        # Windows: [1,4,2]=7, [4,2,9]=15, [2,9,5]=16
        assert max_sum_subarray(arr, k) == 16

    def test_single_element_window(self):
        """Test with k=1 (single element windows)"""
        arr = [1, -3, 2, 1, -1]
        k = 1
        assert max_sum_subarray(arr, k) == 2

    def test_window_size_equals_array_length(self):
        """Test when k equals array length"""
        arr = [1, 2, 3, 4]
        k = 4
        assert max_sum_subarray(arr, k) == 10

    def test_all_negative_numbers_should_fail(self):
        """Test with all negative numbers - this should fail with current implementation"""
        arr = [-1, -4, -2, -3]
        k = 2
        assert max_sum_subarray(arr, k) == -5

    def test_all_negative_numbers_current_behavior(self):
        """Test current buggy behavior with negative numbers"""
        arr = [-1, -4, -2, -3]
        k = 2
        # Current code returns 0 (incorrect)
        assert max_sum_subarray(arr, k) == -5

    def test_mixed_positive_negative(self):
        """Test with mix of positive and negative"""
        arr = [2, -1, 3, -2, 4]
        k = 3
        # Windows: [2,-1,3]=4, [-1,3,-2]=0, [3,-2,4]=5
        assert max_sum_subarray(arr, k) == 5

    def test_two_element_array(self):
        """Test with minimum viable array"""
        arr = [3, 7]
        k = 2
        assert max_sum_subarray(arr, k) == 10

    @pytest.mark.parametrize(
        "arr,k",
        [
            ([1, 2, 3], 5),
            ([5], 2),
            ([], 1),
        ],
    )
    def test_invalid_k_greater_than_length(self, arr: List[int], k: int):
        """Test when k > array length"""
        with pytest.raises(ValueError):
            max_sum_subarray(arr, k)

    @pytest.mark.parametrize("k", [0, -1, -5])
    def test_invalid_k_values(self, k: int):
        """Test with invalid k values"""
        arr = [1, 2, 3, 4]
        with pytest.raises(ValueError):
            max_sum_subarray(arr, k)

    def test_duplicate_elements(self):
        """Test with duplicate elements"""
        arr = [2, 2, 2, 2, 2]
        k = 3
        assert max_sum_subarray(arr, k) == 6

    def test_zeros_in_array(self):
        """Test with zeros"""
        arr = [0, 1, 0, 2, 0]
        k = 2
        # Windows: [0,1]=1, [1,0]=1, [0,2]=2, [2,0]=2
        assert max_sum_subarray(arr, k) == 2

    def test_large_numbers(self):
        """Test with large numbers"""
        arr = [1000000, 2000000, 3000000]
        k = 2
        assert max_sum_subarray(arr, k) == 5000000

    def test_boundary_bug_demonstration(self):
        """This test demonstrates the boundary bug in current implementation"""
        arr = [1, 2, 3, 4, 5]
        k = 3
        assert max_sum_subarray(arr, k) == 12

    def test_boundary_bug_last_window_missed(self):
        """Test that exposes the boundary bug - last window is not considered"""
        arr = [1, 2, 10, 20]  # Last window [10,20]=30 should be max
        k = 2
        # Current buggy implementation misses the last window [10,20]=30
        # and only considers [1,2]=3, [2,10]=12, missing [10,20]=30
        assert max_sum_subarray(arr, k) == 30

    def test_negative_sum_initialization_bug(self):
        """Test that exposes the negative sum initialization bug"""
        arr = [-5, -1, -3, -2]
        k = 2
        # All windows are negative, but current implementation returns 0
        # Windows: [-5,-1]=-6, [-1,-3]=-4, [-3,-2]=-5
        # Should return -4 (least negative), but returns 0
        assert max_sum_subarray(arr, k) == -4

    def test_mixed_with_negative_result_expected(self):
        """Test where maximum sum is negative but greater than 0 initialization"""
        arr = [-10, -1, -5, -2, -20]
        k = 3
        # Windows: [-10,-1,-5]=-16, [-1,-5,-2]=-8, [-5,-2,-20]=-27
        # Should return -8, but current implementation returns 0
        assert max_sum_subarray(arr, k) == -8

    def test_window_exceeds_remaining_elements_boundary(self):
        """Test boundary condition when window size causes index issues"""
        arr = [5, 10, 15]
        k = 3
        # Only one window possible: [5,10,15]=30
        # Current boundary bug might miss this
        assert max_sum_subarray(arr, k) == 30

    def test_alternating_pattern_boundary_issue(self):
        """Test with alternating pattern where last window is crucial"""
        arr = [1, 10, 1, 10, 1, 100]
        k = 2
        # Windows: [1,10]=11, [10,1]=11, [1,10]=11, [10,1]=11, [1,100]=101
        # Last window [1,100]=101 should be maximum but might be missed
        assert max_sum_subarray(arr, k) == 101
