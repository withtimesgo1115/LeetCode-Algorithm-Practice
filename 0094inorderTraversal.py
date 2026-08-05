"""
Binary Tree Inorder Traversal (LeetCode 94).

Given the root of a binary tree, return the inorder traversal of its
nodes' values. Implemented iteratively using a stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        # go as far left as possible, pushing nodes onto the stack
        while cur:
            stack.append(cur)
            cur = cur.left
        # pop the top node and record its value
        cur = stack.pop()
        res.append(cur.val)
        # move to the right subtree
        cur = cur.right

    return res
