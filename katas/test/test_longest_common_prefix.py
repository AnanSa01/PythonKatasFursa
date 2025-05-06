import unittest

from katas.longest_common_prefix import longest_common_prefix
class MyTestCase(unittest.TestCase):
    def test_longest_common_prefix(self):
        check = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(check), "fl")  # add assertion here

    def test_longest_common_prefix_no_matches(self):
        check = ["one", "two", "three", "four"]
        self.assertEqual(longest_common_prefix(check), "")

    def test_longest_common_prefix_same_word(self):
        check = ["Hello!", "Hello!", "Hello!", "Hello!", "Hello!"]
        self.assertEqual(longest_common_prefix(check), "Hello!")


if __name__ == '__main__':
    unittest.main()
