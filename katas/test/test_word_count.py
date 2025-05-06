import unittest

from katas.word_count import count_words

class MyTestCase(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(count_words("hello world"), 2)  # add assertion here

    def test_word_count_empty(self):
        self.assertEqual(count_words(" "), 0)

    def test_word_count_characters(self):
        self.assertEqual(count_words("a b c d e"), 5)

    def test_word_count_long_words(self):
        self.assertEqual(count_words("abcd efg hijk lmnop qrs tuv wx yz"), 8)


if __name__ == '__main__':
    unittest.main()
