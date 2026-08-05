"""
LeetCode 98. 验证二叉搜索树

给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。

有效二叉搜索树定义如下：
    - 节点的左子树只包含小于当前节点的数。
    - 节点的右子树只包含大于当前节点的数。
    - 所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
    输入：root = [2,1,3]
    输出：true

示例 2：
    输入：root = [5,1,4,null,null,3,6]
    输出：false
    解释：根节点的值是 5，但是右子节点的值是 4。

提示：
    树中节点数目范围在 [1, 10^4] 内
    -2^31 <= Node.val <= 2^31 - 1
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
