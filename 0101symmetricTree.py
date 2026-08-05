"""
Symmetric Tree (LeetCode 101).

Given the root of a binary tree, check whether it is a mirror of
itself (i.e., symmetric around its center).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def check(p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val == q.val
                and check(p.left, q.right)
                and check(p.right, q.left))

    return check(root, root)
