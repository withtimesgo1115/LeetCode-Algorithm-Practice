"""
LeetCode 101. 对称二叉树

给你一个二叉树的根节点 root，检查它是否轴对称。

如果二叉树的左子树和右子树呈镜像翻转，则该二叉树是对称的。

示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true

示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false

提示：
    树中节点数目在范围 [1, 1000] 内
    -100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 定义一个递归函数，判断两个子树是否对称
        def dfs(left, right):
            # 如果两个子树都为空，则对称
            if left is None and right is None:
                return True
            # 如果其中一个子树为空，则不对称
            if left is None or right is None:
                return False
            # 如果两个子树的根节点值不相等，则不对称
            if left.val != right.val:
                return False
            # 递归判断左子树的左子树和右子树的右子树是否对称
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
        
        
        
        
