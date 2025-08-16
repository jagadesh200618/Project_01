from enum import Enum

class Operation(Enum):
    Bracket = 0,
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

    def __str__(self):



x = TreeNode(Operation.Addition, 2, 3)
print(x)
