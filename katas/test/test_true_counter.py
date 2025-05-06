import unittest

from katas.true_counter import count_true_values

class MyTestCase(unittest.TestCase):
    def test_true_counter(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)  # add assertion here

    def test_true_counter_all_true(self):
        self.assertEqual(count_true_values([True, True, True, True, True]), 5)

    def test_true_counter_all_false(self):
        self.assertEqual(count_true_values([False, False, False, False]), 0)


if __name__ == '__main__':
    unittest.main()
