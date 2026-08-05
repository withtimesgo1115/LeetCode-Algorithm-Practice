"""
LeetCode 232. 用栈实现队列

题目描述：
    请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

    实现 MyQueue 类：
        - void push(int x) 将元素 x 推到队列的末尾
        - int pop() 从队列的开头移除并返回元素
        - int peek() 返回队列开头的元素
        - boolean empty() 如果队列为空，返回 True；否则返回 False

示例：
    输入：
        ["MyQueue", "push", "push", "peek", "pop", "empty"]
        [[], [1], [2], [], [], []]
    输出：
        [null, null, null, 1, 1, false]

    解释：
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); // queue is: [1]
        myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
        myQueue.peek();  // 返回 1
        myQueue.pop();   // 返回 1，队列变为 [2]
        myQueue.empty(); // 返回 false

提示：
    1 <= x <= 9
    最多调用 100 次 push、pop、peek 和 empty
    假设所有操作都是有效的（例如，一个空的队列不会调用 pop 或者 peek 操作）

进阶：你能否实现每个操作均摊时间复杂度为 O(1) 的队列？

本文件使用 stack1 处理入队，stack2 处理出队，
当 stack2 为空时将 stack1 的元素全部倒入 stack2，实现 FIFO 行为。
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
