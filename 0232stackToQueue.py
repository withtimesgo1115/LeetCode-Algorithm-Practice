"""
Implement a queue using two stacks.
stack1 handles pushes; stack2 handles pops and peeks,
reversing the order to achieve FIFO behavior.
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """Push element x to the back of queue."""
        self.stack1.append(x)

    def pop(self):
        """Removes the element from the front of queue and returns it."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """Get the front element."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """Returns whether the queue is empty."""
        return not self.stack1 and not self.stack2
