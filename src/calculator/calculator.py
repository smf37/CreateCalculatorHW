

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
        self.result = Division(a, b)
        return self.result

    def square(self, a, b):
        self.result = Square(a, b)
        return self.result

    def squareRoot(self, a, b):
        self.result = SquareRoot(a, b)
        return self.result
