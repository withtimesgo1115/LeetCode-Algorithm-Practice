"""
Invert (mirror) a binary tree by recursively swapping
the left and right children of every node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return root

    right = invert_tree(root.right)
    left = invert_tree(root.left)
    root.left = right
    root.right = left

    return root
