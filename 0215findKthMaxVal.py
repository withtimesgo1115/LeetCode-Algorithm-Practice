"""
LeetCode 215. 数组中的第K个最大元素

题目描述：
    给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    你必须设计时间复杂度为 O(n) 的算法解决此问题。

示例 1：
    输入：[3,2,1,5,6,4], k = 2
    输出：5

示例 2：
    输入：[3,2,3,1,2,4,5,5,6], k = 4
    输出：4

提示：
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

本文件使用大小为 k 的最小堆实现：
    维护一个容量为 k 的小顶堆，堆顶即为第 k 大的元素。
    遍历数组，当新元素大于堆顶时替换堆顶并下沉调整。
"""
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用快速选择算法实现
        def quick_select(nums, k):
            pivot = random.choice(nums) # 随机选择一个基准值
            big, equal, small = [], [], [] # 分别存储大于、等于、小于基准值的元素
            for num in nums:
                # 根据基准值将元素分为三类, 大于基准值的放入 big, 小于基准值的放入 small, 等于基准值的放入 equal
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            # 如果大于基准值的元素个数大于等于 k, 则第 k 大的元素在 big 中
            if k <= len(big):
                return quick_select(big, k)
            # 如果大于基准值的元素个数加上等于基准值的元素个数小于 k, 则第 k 大的元素在 small 中
            if len(big) + len(equal) < k:
                return quick_select(small, k - (len(big) + len(equal)))
            return pivot
        return quick_select(nums, k)
