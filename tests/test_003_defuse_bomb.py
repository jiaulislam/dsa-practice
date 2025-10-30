import unittest

from solutions.array.week_1_003_defuse_bomb import decrypt_bf, decrypt_sw


class TestDecryptBruteForce(unittest.TestCase):
    def test_decrypt_variants(self):
        cases = [
            ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
            ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
            ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
            ([1, 2, 3], 1, [2, 3, 1]),
            ([1, 2, 3], -1, [3, 1, 2]),
            ([4, 5, 6], 2, [11, 10, 9]),
            ([1, 2, 3, 4], 3, [9, 8, 7, 6]),
            ([9, 1, 2, 3, 4], -3, [9, 16, 14, 12, 6]),
            ([100], 0, [0]),
        ]

        for code, k, expected in cases:
            with self.subTest(code=code, k=k):
                self.assertEqual(decrypt_bf(code, k), expected)

    def test_multiple_wraps_positive_k(self):
        code = [8, 6, 7, 5, 3, 0, 9]
        k = 4
        expected = [21, 15, 17, 20, 23, 30, 26]
        self.assertEqual(decrypt_bf(code, k), expected)

    def test_multiple_wraps_negative_k(self):
        code = [2, 7, 0, 5, 8, 4]
        k = -4
        expected = [17, 19, 21, 13, 14, 20]
        self.assertEqual(decrypt_bf(code, k), expected)


class TestDecryptSlidingWindow(unittest.TestCase):
    def test_decrypt_variants(self):
        cases = [
            ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
            ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
            ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
            ([1, 2, 3], 1, [2, 3, 1]),
            ([1, 2, 3], -1, [3, 1, 2]),
            ([4, 5, 6], 2, [11, 10, 9]),
            ([1, 2, 3, 4], 3, [9, 8, 7, 6]),
            ([9, 1, 2, 3, 4], -3, [9, 16, 14, 12, 6]),
            ([100], 0, [0]),
        ]

        for code, k, expected in cases:
            with self.subTest(code=code, k=k):
                self.assertEqual(decrypt_sw(code, k), expected)

    def test_multiple_wraps_positive_k(self):
        code = [8, 6, 7, 5, 3, 0, 9]
        k = 4
        expected = [21, 15, 17, 20, 23, 30, 26]
        self.assertEqual(decrypt_sw(code, k), expected)

    def test_multiple_wraps_negative_k(self):
        code = [2, 7, 0, 5, 8, 4]
        k = -4
        expected = [17, 19, 21, 13, 14, 20]
        self.assertEqual(decrypt_sw(code, k), expected)


if __name__ == "__main__":
    unittest.main()
