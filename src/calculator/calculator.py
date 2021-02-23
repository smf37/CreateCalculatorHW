from src.calculator.Addition import Addition
from src.calculator.Subtraction import Subtraction
from src.calculator.Division import Division
from src.calculator.Multiplication import Multiplication
from src.calculator.Square import Square
from src.calculator.SquareRoot import Square_Root

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = round(Division(a, b), 9)
        return self.result

    def square(self, a):
        self.result = Square(a)
        return self.result

    def squareRoot(self, a):
        self.result = Square_Root(a)
        return self.result
