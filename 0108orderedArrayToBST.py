"""
LeetCode 108. 将有序数组转换为二叉搜索树

给你一个整数数组 nums，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。

高度平衡二叉树是一棵满足如下条件的二叉树：
    - 每个节点的左右两个子树的高度差的绝对值不超过 1。

示例 1：
    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案。

示例 2：
    输入：nums = [1,3]
    输出：[3,1]
    解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums 按严格递增顺序排列
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if not nums:
        return None

    def buildBST(low, high):
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = buildBST(low, mid - 1)
        node.right = buildBST(mid + 1, high)
        return node

    return buildBST(0, len(nums) - 1)
