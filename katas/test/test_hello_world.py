import unittest
from katas.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello world")

    def test_hello_world_negative(self):
        self.assertNotEqual(hello_world(), "Hello, World!")
