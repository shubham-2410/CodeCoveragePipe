import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(fibonacci(-5), [], "Should return an empty list for negative input")

    def test_zero_input(self):
        self.assertEqual(fibonacci(0), [], "Should return an empty list for input 0")

    def test_one_input(self):
        self.assertEqual(fibonacci(1), [0], "Should return [0] for input 1")

    def test_two_input(self):
        self.assertEqual(fibonacci(2), [0, 1], "Should return [0, 1] for input 2")

    def test_positive_input(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3], "Should return correct Fibonacci sequence for input 5")
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Should return correct Fibonacci sequence for input 10")

if __name__ == '__main__':
    unittest.main()
