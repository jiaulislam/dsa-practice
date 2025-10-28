import unittest
from solutions.array.week_1_002_maximum_average_subarray_i import find_maximum_average


class TestMaximumAverageSubarray(unittest.TestCase):
    def test_basic_case_1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_basic_case_2(self):
        nums = [5, 5, 5, 5]
        k = 1
        expected = 5.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_single_element(self):
        nums = [42]
        k = 1
        expected = 42.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_all_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        k = 2
        expected = -1.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_all_positive_numbers(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = 4.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_mixed_positive_negative(self):
        nums = [-5, 10, -3, 8, -1]
        k = 2
        expected = 3.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_k_equals_array_length(self):
        nums = [1, 2, 3, 4]
        k = 4
        expected = 2.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_large_numbers(self):
        nums = [10000, 20000, 30000, 40000, 50000]
        k = 3
        expected = 40000.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_zeros_included(self):
        nums = [0, 0, 0, 1, 2]
        k = 3
        expected = 1.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_duplicate_elements(self):
        nums = [2, 2, 2, 2, 2]
        k = 3
        expected = 2.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_alternating_pattern(self):
        nums = [1, -1, 1, -1, 1, -1]
        k = 2
        expected = 0.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_decreasing_sequence(self):
        nums = [10, 8, 6, 4, 2]
        k = 2
        expected = 9.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_increasing_sequence(self):
        nums = [1, 3, 5, 7, 9]
        k = 2
        expected = 8.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_fractional_result(self):
        nums = [1, 2, 3]
        k = 2
        expected = 2.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_large_array_small_k(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 2
        expected = 9.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_edge_case_two_elements(self):
        nums = [100, -100]
        k = 1
        expected = 100.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_negative_zero_positive(self):
        nums = [-3, 0, 5, -2, 1]
        k = 3
        expected = 4.0 / 3.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_maximum_at_beginning(self):
        nums = [9, 8, 1, 2, 3]
        k = 2
        expected = 8.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_maximum_at_end(self):
        nums = [1, 2, 3, 8, 9]
        k = 2
        expected = 8.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_precision_case(self):
        nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
        k = 5
        expected = 3.6
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_minimum_constraints(self):
        nums = [1]
        k = 1
        expected = 1.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_maximum_k_value(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        expected = 5.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_boundary_values(self):
        nums = [-10000, 10000, -5000, 5000]
        k = 2
        expected = 2500.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_identical_averages(self):
        nums = [1, 2, 2, 1, 1, 2]
        k = 3
        expected = 5.0 / 3.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_very_small_differences(self):
        nums = [100, 110, 120, 130, 140]
        k = 2
        expected = 135.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_stress_case_large_array(self):
        nums = list(range(1, 101))
        k = 50
        expected = 75.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_negative_maximum(self):
        nums = [-10, -5, -8, -3, -6]
        k = 2
        expected = -4.5
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_empty_nums(self):
        nums = []
        k = 1
        expected = 0.0
        result = find_maximum_average(nums, k)
        self.assertAlmostEqual(result, expected, delta=0.00001)

    def test_empty_nums_with_negative_k(self):
        nums = []
        k = -1
        with self.assertRaises(ValueError):
            find_maximum_average(nums, k)


if __name__ == "__main__":
    unittest.main()
