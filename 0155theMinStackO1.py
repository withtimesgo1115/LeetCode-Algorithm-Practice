"""
Min Stack (LeetCode 155) - O(1) getMin solution
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Uses an auxiliary stack to track the minimum value at each level.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.stack2 = []  # auxiliary stack to store minimum values

    def push(self, x):
        self.stack.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self):
        if self.stack.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack2[-1]
