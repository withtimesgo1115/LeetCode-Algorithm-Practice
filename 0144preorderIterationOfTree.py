"""
Binary Tree Preorder Traversal (LeetCode 144)
Given the root of a binary tree, return the preorder traversal of its node values.
Uses an iterative approach with a stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    """Return the preorder traversal of the binary tree's node values."""
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
