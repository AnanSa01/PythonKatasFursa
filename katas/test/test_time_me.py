import unittest

from katas.time_me import measure_execution_time, sample_function, quick_function


class MyTestCase(unittest.TestCase):
    def test_time_me(self):
        self.assertAlmostEqual(measure_execution_time(sample_function), 500, places=0)  # add assertion here

    def test_time_me_second(self):
        self.assertAlmostEqual(measure_execution_time(quick_function), 0.004, places=0)


if __name__ == '__main__':
    unittest.main()
