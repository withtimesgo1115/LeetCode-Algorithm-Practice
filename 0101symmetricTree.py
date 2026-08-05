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
