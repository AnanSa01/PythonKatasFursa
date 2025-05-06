import unittest
from katas.is_unique_str import is_unique


class MyTestCase(unittest.TestCase):
    def test_is_unique_str_false(self):
        self.assertEqual(is_unique("banana"), False)  # add assertion here

    def test_is_unique_str_true(self):
        self.assertEqual(is_unique("orange"), True)

    def test_is_unique_str_same_character(self):
        self.assertEqual(is_unique("cccccccc"), False)


if __name__ == '__main__':
    unittest.main()
