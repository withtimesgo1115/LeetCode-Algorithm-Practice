"""
二叉搜索树中的搜索 (LeetCode 700)
给定二叉搜索树（BST）的根节点和一个值 val，
在 BST 中找到节点值等于 val 的节点，返回以该节点为根的子树。
如果节点不存在，则返回 None。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif root.val < val:
        return searchBST(root.right, val)
    else:
        return searchBST(root.left, val)
