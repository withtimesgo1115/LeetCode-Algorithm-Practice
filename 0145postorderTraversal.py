"""
Binary Tree Postorder Traversal (LeetCode 145)
Given the root of a binary tree, return the postorder traversal of its node values.
Uses a recursive approach: left subtree, right subtree, then root.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    """Return the postorder traversal of the binary tree's node values."""
    ans = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

    postorder(root)
    return ans
