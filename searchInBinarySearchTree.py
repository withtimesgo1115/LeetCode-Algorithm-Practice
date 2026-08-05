"""
700. 二叉搜索树中的搜索 / 450. 二叉搜索树中的删除

题目描述：
    本文件实现了二叉搜索树（BST）的三个核心操作：查找、插入和删除。

    二叉搜索树（Binary Search Tree）的性质：
        - 左子树中所有节点的值均小于根节点的值。
        - 右子树中所有节点的值均大于根节点的值。
        - 左子树和右子树也分别是二叉搜索树。

一、搜索（LeetCode 700）：
    给定二叉搜索树的根节点 root 和一个值 val，
    在 BST 中搜索值等于 val 的节点，返回该子树。
    如果节点不存在，返回 None。

    示例：
        输入：root = [4, 2, 7, 1, 3], val = 2
        输出：[2, 1, 3]（以该节点为根的子树）

        输入：root = [4, 2, 7, 1, 3], val = 5
        输出：None

二、插入（LeetCode 701）：
    给定二叉搜索树的根节点 root、要插入的值 val，
    将值插入 BST 中，返回插入后的根节点。

    示例：
        输入：root = [4, 2, 7, 1, 3], val = 5
        输出：[4, 2, 7, 1, 3, 5]

三、删除（LeetCode 450）：
    给定二叉搜索树的根节点 root 和一个值 key，
    删除 BST 中值等于 key 的节点，返回根节点的引用。

    删除节点的三种情况：
        1. 节点为叶子节点：直接删除。
        2. 节点只有一个子节点：用子节点替代该节点。
        3. 节点有两个子节点：找到左子树中的最大值（或右子树中的最小值）
           替代该节点，然后递归删除替代节点。

    示例：
        输入：root = [5, 3, 6, 2, 4, null, 7], key = 3
        输出：[5, 2, 6, null, 4, null, 7]

提示：
    - 节点数的范围 [0, 10^4]
    - -10^5 <= Node.val <= 10^5
    - 节点值唯一
    - root 可能为空

复杂度分析：
    时间复杂度：O(h)，h 为树的高度。
        - 平均情况（平衡树）：O(log n)
        - 最差情况（退化为链表）：O(n)
    空间复杂度：O(h)，递归调用栈的深度。
"""


class TreeNode:
    """Binary search tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root, n):
    """Search for a node with value n in the BST. Returns the node if found, else None."""
    if not root:
        return None
    if root.val == n:
        return root
    elif root.val > n:
        return search(root.left, n)
    else:
        return search(root.right, n)


def insert(root, n):
    """Insert a value n into the BST. Returns the root of the modified tree."""
    if not root:
        return TreeNode(n)
    if root.val == n:
        return root
    elif root.val > n:
        root.left = insert(root.left, n)
    else:
        root.right = insert(root.right, n)
    return root


def delete_node(root, n):
    """Delete a node with value n from the BST. Returns the root of the modified tree."""
    if not root:
        return None
    if root.val == n:
        if not root.left and not root.right:
            return None
        elif root.left:
            max_left = _find_max(root.left)
            root.val = max_left.val
            root.left = delete_node(root.left, max_left.val)
        else:
            min_right = _find_min(root.right)
            root.val = min_right.val
            root.right = delete_node(root.right, min_right.val)
    elif root.val > n:
        root.left = delete_node(root.left, n)
    else:
        root.right = delete_node(root.right, n)
    return root


def _find_max(root):
    """Find the node with the maximum value in a BST subtree."""
    while root.right:
        root = root.right
    return root


def _find_min(root):
    """Find the node with the minimum value in a BST subtree."""
    while root.left:
        root = root.left
    return root
