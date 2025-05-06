import unittest

from katas.reduce_list import reduce_array


class MyTestCase(unittest.TestCase):
    def test_reduce_list(self):
        self.assertEqual(reduce_array([10, 15, 7, 20, 25]), [10, 5, -8, 13, 5])  # add assertion here

    def test_reduce_list_large(self):
        self.assertEqual(reduce_array([500, -33, 77, 0, 1]), [500, -533, 110, -77, 1])

    def test_reduce_list_equal(self):
        self.assertEqual(reduce_array([5, 5, 5, 5, 5]), [5, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
