"""
145. 二叉树的后序遍历（Binary Tree Postorder Traversal）

给你一棵二叉树的根节点 root，返回其节点值的后序遍历。

后序遍历的顺序为：左子树 -> 右子树 -> 根节点。

示例 1：
    输入：root = [1,null,2,3]
    输出：[3,2,1]

示例 2：
    输入：root = [1,2,3,4,5,null,8,null,null,6,7,9]
    输出：[4,6,7,5,2,9,8,3,1]

示例 3：
    输入：root = []
    输出：[]

示例 4：
    输入：root = [1]
    输出：[1]

提示：
    树中节点的数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法是简单的，你能否用迭代算法完成此题？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    """Return the postorder traversal of the binary tree's node values."""
    ans = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

    postorder(root)
    return ans
