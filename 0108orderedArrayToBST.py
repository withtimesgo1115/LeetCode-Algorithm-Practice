"""
Convert Sorted Array to Binary Search Tree (LeetCode 108).

Given an integer array nums where the elements are sorted in ascending
order, convert it to a height-balanced binary search tree.
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
