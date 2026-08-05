"""
LeetCode 110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的
绝对值不超过 1。

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：true

示例 2：
    输入：root = [1,2,2,3,3,null,null,4,4]
    输出：false

示例 3：
    输入：root = []
    输出：true

提示：
    树中的节点数在范围 [0, 5000] 内
    -10^4 <= Node.val <= 10^4
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
