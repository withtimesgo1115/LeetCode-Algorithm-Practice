"""
145. 二叉树的后序遍历

题目描述：
    给你一棵二叉树的根节点 root ，返回其节点值的后序遍历。

    后序遍历的顺序为：左子树 -> 右子树 -> 根节点（Left, Right, Root）。

    本实现使用迭代方式（基于栈）完成后序遍历，而非递归方式。
    核心思路是：按照"根->右->左"的顺序入栈并收集结果，
    最后将结果数组反转，即可得到"左->右->根"的后序遍历序列。

示例 1：
    输入：root = [1, null, 2, null, null, 3]
    输出：[3, 2, 1]
    解释：
        1
         \
          2
         /
        3
    后序遍历顺序：3 -> 2 -> 1

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [1]
    输出：[1]

提示：
    - 树中节点的数目在范围 [0, 100] 内
    - -100 <= Node.val <= 100

进阶：递归解法很简单，你可以使用迭代算法完成此题吗？

复杂度分析：
    时间复杂度：O(n)，每个节点访问一次。
    空间复杂度：O(n)，栈的最大深度为树的高度，最坏情况下为 O(n)。
"""


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root):
    """Return the postorder traversal of a binary tree's node values."""
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        cur = stack.pop()
        res.insert(0, cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res
