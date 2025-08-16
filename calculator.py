
import numpy as np

class Calculator:
    def __init__(self):
        history = {}

    # 1. Addition
    def add(self, a, b):
        return a + b

    # 2. Subraction
    def sub(self, a, b):
        return a - b

    # 3. Multiplication
    def mul(self, a, b):
        return a * b

    # 4. Division
    def div(self, a, b):
        if b == 0:
            return ZeroDivisionError
        else:
            return a/b

    # 5. Moduls Division
    def mod(self, a, b):
        return a % b

    # 6. Square
    def square(self, x):
        return x ** 2

    # 7. Square Root
    def sqrt(self, x):
        return np.sqrt(x)

    # 8. Percentage
    def percentage(self, x):
        return x / 100
