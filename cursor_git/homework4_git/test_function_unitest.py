from funcc import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_check_sum(self):
        self.assertEqual(Calculator.add(3, 4), 7)

    def test_check_different(self):
        self.assertEqual(Calculator.subtract(4, 8), -4)

    def test_check_multiply(self):
        self.assertEqual(Calculator.multiply(3, 5), 15)

    def test_check_division(self):
        self.assertEqual(Calculator.divide(18, 6), 3)


if __name__ == '__main__':
    unittest.main()
