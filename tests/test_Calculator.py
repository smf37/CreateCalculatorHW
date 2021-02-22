import unittest

from src.calculator.calculator import Calculator
from csvReader.csv_Reader import Reader


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_Addition(self):
        file = Reader("testCases/Unit_Test_Addition.csv").content
        print("test addition\n")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))

    def test_Subtraction(self):
        file = Reader("testCases/Unit_Test_Subtraction.csv").content
        print("test subtraction\n")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))

    def test_Division(self):
        file = Reader("testCases/Unit_Test_Division.csv").content
        print("test division\n")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.division(row[0], row[1]), float(row[2]))

    def test_Multiplication(self):
        file = Reader("testCases/Unit_Test_Multiplication.csv").content
        print("test multiplication\n")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.multiply(row[0], row[1]), float(row[2]))

    def test_Square(self):
        file = Reader("testCases/Unit_Test_Square.csv").content
        print("test square\n")
        for row in file:
            result = float(row[1])
            self.assertEqual(self.calculator.square(row[0]), float(row[1]))

    def test_Square_Root(self):
        file = Reader("testCases/Unit_Test_Square_Root.csv").content
        print("test square root\n")
        for row in file:
            result = float(row[1])
            self.assertEqual(self.calculator.squareRoot(row[0]), float(row[1]))
            self.assertAlmostEqual(self.calculator.result, result)







