import unittest

from solutions.array.week_1_005_longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def assertPrefix(self, strs, expected):  # helper keeps individual tests concise
        self.assertEqual(longest_common_prefix(strs), expected)

    def test_basic_shared_prefix(self):
        self.assertPrefix(["flower", "flow", "flight"], "fl")

    def test_no_common_prefix(self):
        self.assertPrefix(["dog", "racecar", "car"], "")

    def test_entire_word_is_prefix(self):
        self.assertPrefix(["interspecies", "interstellar", "interstate"], "inters")

    def test_single_string(self):
        self.assertPrefix(["solo"], "solo")

    def test_contains_empty_string(self):
        self.assertPrefix(["", "prefix", "pre"], "")

    def test_all_identical_strings(self):
        self.assertPrefix(["repeat", "repeat", "repeat"], "repeat")

    def test_incrementally_shrinking_prefix(self):
        strings = ["abcdef", "abcde", "abcd", "abc"]
        self.assertPrefix(strings, "abc")

    def test_mismatch_from_first_character(self):
        self.assertPrefix(["xabc", "yabc", "zabc"], "")

    def test_long_list_short_prefix(self):
        words = ["apricot", "april", "apartment", "ape", "apiary", "apex"]
        self.assertPrefix(words, "ap")

    def test_mixed_length_no_prefix(self):
        words = ["a", "", "alpha"]
        self.assertPrefix(words, "")


if __name__ == "__main__":
    unittest.main()
