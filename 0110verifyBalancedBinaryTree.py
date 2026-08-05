"""
Balanced Binary Tree (LeetCode 110).

Given a binary tree, determine if it is height-balanced. A height-balanced
binary tree is defined as a binary tree in which the absolute difference
between the heights of the left and right subtrees of every node is no
more than 1.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    flag = True

    def dfs(node):
        nonlocal flag
        if not node or not flag:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left - right) > 1:
            flag = False
            return 0
        return max(left, right) + 1

    dfs(root)
    return flag
