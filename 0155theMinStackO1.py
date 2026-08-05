"""
155. 最小栈（Min Stack）

设计一个支持 push、pop、top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类：
    - MinStack() 初始化堆栈对象。
    - void push(int val) 将元素 val 推入堆栈。
    - void pop() 移除堆栈顶部的元素。
    - int top() 获取堆栈顶部的元素。
    - int getMin() 获取堆栈中的最小元素。

示例 1：
    输入：
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    输出：
    [null,null,null,null,-3,null,0,-2]

    解释：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.

提示：
    -2^31 <= val <= 2^31 - 1
    pop、top 和 getMin 操作总是在非空栈上调用
    push、pop、top 和 getMin 最多被调用 3 * 10^4 次
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
