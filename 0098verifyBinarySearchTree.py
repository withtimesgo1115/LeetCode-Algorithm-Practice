"""
Validate Binary Search Tree (LeetCode 98).

Given the root of a binary tree, determine if it is a valid binary
search tree (BST). A valid BST is defined such that the left subtree
contains only nodes with values less than the node's value, and the
right subtree contains only nodes with values greater than the node's value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True
        # node value must be strictly within the (min_val, max_val) range
        if node.val <= min_val or node.val >= max_val:
            return False
        # both subtrees must also be valid BSTs with updated bounds
        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, float('-inf'), float('inf'))
