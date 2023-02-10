import unittest
import sys
sys.path.append('')
from script.calculator import *




class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

        result = self.calc.add(-1, -2)
        self.assertEqual(result, -3)

        result = self.calc.add(2.5, 1.5)
        self.assertEqual(result, 4)

        result = self.calc.add("a", "b")
        self.assertEqual(result, "ab")

    def test_subtraction(self):
        result = self.calc.subtract(2, 1)
        self.assertEqual(result, 1)

        result = self.calc.add(-1, -2)
        self.assertEqual(result, 1)

        result = self.calc.add(2.5, 1.5)
        self.assertEqual(result, 1)

        result = self.calc.add("a", "b")
        self.assertEqual(result, "b")

    def test_multiplication(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

        result = self.calc.add(-1, -2)
        self.assertEqual(result, -2)

        result = self.calc.add(2.5, 1.5)
        self.assertEqual(result, 3.75)

        result = self.calc.add("a", "b")
        self.assertEqual(result, "ab")

    def test_division(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

        result = self.calc.add(-1, -2)
        self.assertEqual(result, -0.5)

        result = self.calc.add(2.5, 1.5)
        self.assertEqual(result, 2.08)

    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

        result = self.calc.add(-2, -2)
        self.assertEqual(result, 4)

        result = self.calc.add(2.5, 1.5)
        self.assertEqual(result, 3,95)

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