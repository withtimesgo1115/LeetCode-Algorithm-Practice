"""Postorder traversal of a binary tree using iteration (stack-based).
Returns node values in postorder (left, right, root) sequence.
"""


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root):
    """Return the postorder traversal of a binary tree's node values."""
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.insert(0, cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res
