"""
700. 二叉搜索树中的搜索 (Search in a Binary Search Tree)

给定一个二叉搜索树（BST）和一个值 val 。
你需要在 BST 中找到节点值等于 val 的节点，返回以该节点为根的子树。
如果节点不存在，则返回 NULL 。

示例 1：
    输入：root = [4,2,7,1,3], val = 2
    输出：[2,1,3]

示例 2：
    输入：root = [4,2,7,1,3], val = 5
    输出：[]

提示：
    树中节点数在 [1, 5000] 范围内
    1 <= Node.val <= 10^7
    root 是二叉搜索树
    1 <= val <= 10^7
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
