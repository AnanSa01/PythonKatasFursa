import unittest
from katas.list_flatten import flatten_list

class MyTestCase(unittest.TestCase):
    def test_list_flatten(self):
        nested_list = [
            1,
            [2, 3],
            [4, [5, 6]],
            7
        ]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5, 6, 7])  # add assertion here

    def test_list_flatten_other(self):
        nested_list = [
            [1,1,1,1,1,1],
            [2, 3, [4,4,4,4]],
            [4, [5, 6,[7,7,7,7,[8,8,8]]]],
            7
        ]
        self.assertEqual(flatten_list(nested_list), [1,1,1,1,1,1, 2, 3, 4,4,4,4,4, 5, 6,7,7,7,7,8,8,8, 7])

    def test_list_flatten_no_nested(self):
        self.assertEqual(flatten_list([5,5,5,5,5]),[5,5,5,5,5])




if __name__ == '__main__':
    unittest.main()
