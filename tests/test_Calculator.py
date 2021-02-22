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

    def test_addition(self):
        file = Reader("testCases/Unit_Test_Addition.csv").content
        print("test addition")
        for row in file:
            result = float(row[2])
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))







