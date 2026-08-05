"""
144. 二叉树的前序遍历（Binary Tree Preorder Traversal）

给你二叉树的根节点 root，返回它节点值的前序遍历。

前序遍历的顺序为：根节点 -> 左子树 -> 右子树。

示例 1：
    输入：root = [1,null,2,3]
    输出：[1,2,3]

示例 2：
    输入：root = [1,2,3,4,5,null,8,null,null,6,7,9]
    输出：[1,2,4,5,6,7,3,8,9]

示例 3：
    输入：root = []
    输出：[]

示例 4：
    输入：root = [1]
    输出：[1]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法是简单的，你能否用迭代算法完成此题？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    """Return the preorder traversal of the binary tree's node values."""
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
