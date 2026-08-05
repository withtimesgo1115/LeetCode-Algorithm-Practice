"""
Min Stack (LeetCode 155) - O(n) getMin solution
Design a stack that supports push, pop, top, and retrieving the minimum element.
Uses a simple scan to find the minimum (O(n) time for getMin).
"""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        return min(self.stack)
