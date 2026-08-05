"""
Binary Tree Level Order Traversal (LeetCode 102).

Given the root of a binary tree, return the level order traversal
of its nodes' values (i.e., from left to right, level by level).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level = []
        # process all nodes at the current level
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)

    return res
