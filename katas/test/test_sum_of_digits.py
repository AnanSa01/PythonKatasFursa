import unittest

from katas.sum_of_digits import sum_of_digits

class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("hello 5 times to my 3 friends"), 8)  # add assertion here

    def test_sum_of_digits_just_numbers(self):
        self.assertEqual(sum_of_digits("12345"), 15)

    def test_sum_of_digits_no_numbers(self):
        self.assertEqual(sum_of_digits("no numbers!"), 0)

if __name__ == '__main__':
    unittest.main()
