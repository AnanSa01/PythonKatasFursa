import unittest

from katas.do_n_times import do_n_times, say_hello, print_message


class MyTestCase(unittest.TestCase):
    def test_do_n_times_say_hello(self):
        result = "Hello!\nHello!\nHello!\n"
        self.assertEqual(do_n_times(say_hello, 3), result)

    def test_do_n_times_print_message(self):
        result = "Python is fun!\nPython is fun!\n"
        self.assertIn(do_n_times(print_message, 2), result)

    def test_do_n_times_both_of_them(self):
        result = "Python is fun!\nPython is fun!\nHello!\nHello!\nHello!\nPython is fun!\n"
        input = do_n_times(print_message, 2)
        input += do_n_times(say_hello, 3)
        input += do_n_times(print_message, 1)
        self.assertIn(input, result)


if __name__ == '__main__':
    unittest.main()
