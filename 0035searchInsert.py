'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 数组长度
        n = len(nums)
        # 如果目标值大于数组中所有元素，返回数组长度，这是处理特殊情况的边界条件
        if nums[n - 1] < target:
            return n
        # 二分查找法，初始化左右指针
        left = 0
        right = n - 1
        # 当左指针小于右指针时，继续查找
        while left < right:
            # 计算中间位置的索引
            mid = (left + right) // 2
            # 如果中间位置的元素小于目标值，说明目标值在右半部分，更新左指针为 mid + 1
            if nums[mid] < target:
                left = mid + 1
            # 否则，说明目标值在左半部分或等于中间位置的元素，更新右指针为 mid
            else:
                right = mid
        # 返回左指针的位置，即目标值应该插入的位置
        return left