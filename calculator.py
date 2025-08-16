from enum import Enum
from typing import Optional

class Operation(Enum):
    Order = 1,
    Division = 2,
    Multiply = 3,
    Addition = 4,
    Subraction = 5,


class TreeNode:
    def __init__(self, data, left, right):
        self.data: Operation = data
        self.left = left
        self.right = right

    def eval(self):
        if self.data == Operation.Order:
            return self.left ** self.right
        elif self.data == Operation.Division:
            if self.right == 0: return ZeroDivisionError
            return self.left / self.right
        elif self.data == Operation.Multiply:
            return self.left * self.right
        elif self.data == Operation.Subraction:
            return self.left - self.right
        elif self.data == Operation.Addition:
            return self.left + self.right

    def __str__(self):
        if self.data == Operation.Order:
            return f"{self.left} ** {self.right}"
        elif self.data == Operation.Division:
            return f"{self.left} / {self.right}"
        elif self.data == Operation.Multiply:
            return f"{self.left} * {self.right}"
        elif self.data == Operation.Subraction:
            return f"{self.left} - {self.right}"
        elif self.data == Operation.Addition:
            return f"{self.left} + {self.right}"
        return ""


class BinaryTree:
    def __init__(self):
        self.tree: Optional[TreeNode] = None

    def parser(self, inp):
        tokens = BinaryTree.tokenize(inp)
        for i in tokens:
            self.append(i)
        return self.tree

    def append(self, token):
        pass

    @staticmethod
    def tokenize(inp):
        token = []
        digit = ""
        for i in inp:
            if i.isspace():
                continue
            elif i.isdigit():
                digit += i
            elif not i.isdigit():
                if digit != "":
                    token.append(eval(digit))
                    digit = ""
                if i == "+":
                    token.append(Operation.Addition)
                elif i == "-":
                    token.append(Operation.Subraction)
                elif i == "*":
                    token.append(Operation.Multiply)
                elif i == "/":
                    token.append(Operation.Division)
                elif i == "**":
                    token.append(Operation.Order)
                else:
                    token.append(i)
        return token

    def eval(self):
        pass


x = BinaryTree.tokenize("23 + 34 + 44 - 67 / 34 * 35")
print(x)
