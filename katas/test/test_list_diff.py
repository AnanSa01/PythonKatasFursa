import unittest

from katas.list_diff import find_difference


class MyTestCase(unittest.TestCase):
    def test_list_diff(self):
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)  # add assertion here

    def test_list_diff_negative(self):
        self.assertEqual(find_difference([-1, -2, -3, -4, -5]), 4)

    def test_list_diff_large(self):
        self.assertEqual(find_difference([101, 2222, -3, 6, 0.5]), 2225)


if __name__ == '__main__':
    unittest.main()
