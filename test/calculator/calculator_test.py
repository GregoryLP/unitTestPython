import unittest
from unitTestPython.calculator import Calculator
from unitTestPython.calculator import calculate


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result = self.calc.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_square_root(self):
        result = self.calc.square_root(4)
        self.assertAlmostEqual(result, 2, places=7)

def test_calculate(self):
    result = calculate("add", 1, 2)
    self.assertEqual(result, 3)

    result = calculate("substract", 2, 1)
    self.assertEqual(result, 1)

    result = calculate("multiply", 2, 3)
    self.assertEqual(result, 6)

    result = calculate("divide", 6, 3)
    self.assertEqual(result, 2)

    result = calculate("power", 2, 3)
    self.assertEqual(result, 8)

    result = calculate("square_root", 4)
    self.assertAlmostEqual(result, 2, places=7)

if __name__ == "__main__":
    unittest.main()