"""
LeetCode 94. 二叉树的中序遍历

给定一个二叉树的根节点 root，返回它的中序遍历。

中序遍历的顺序为：左子树 -> 根节点 -> 右子树。

示例 1：
    输入：root = [1,null,2,3]
    输出：[1,3,2]

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [1]
    输出：[1]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        # go as far left as possible, pushing nodes onto the stack
        while cur:
            stack.append(cur)
            cur = cur.left
        # pop the top node and record its value
        cur = stack.pop()
        res.append(cur.val)
        # move to the right subtree
        cur = cur.right

    return res
