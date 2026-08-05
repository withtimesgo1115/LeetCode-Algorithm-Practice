"""
剑指 Offer 59 - I / LeetCode 239. 滑动窗口的最大值 (Sliding Window Maximum)

题目描述：
    给定一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到
    数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右
    移动一位。返回滑动窗口中的最大值。

示例 1：
    输入：nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    输出：[3, 3, 5, 5, 6, 7]
    解释：
        滑动窗口的位置                最大值
        -------------------------    -------
        [1  3  -1] -3  5  3  6  7      3
         1 [3  -1  -3] 5  3  6  7      3
         1  3 [-1  -3  5] 3  6  7      5
         1  3  -1 [-3  5  3] 6  7      5
         1  3  -1  -3 [5  3  6] 7      6
         1  3  -1  -3  5 [3  6  7]     7

示例 2：
    输入：nums = [1], k = 1
    输出：[1]

约束条件：
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length

解题思路：
    方法一（本文件实现）：暴力法，对每个窗口遍历其中的 k 个元素求最大值。
    时间复杂度 O(n*k)，空间复杂度 O(1)。
    方法二（更优解法）：使用单调递减双端队列（deque），队列中存储下标，
    保证队列中对应的值单调递减。每次滑动窗口时，移除过期元素和比当前元素
    小的元素，队首即为当前窗口的最大值。时间复杂度 O(n)。
"""


def _calc_max(arr, left, right):
    if not arr:
        return None
    max_num = arr[left]
    for i in range(left, right + 1):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


def max_sliding_window(nums, k):
    length = len(nums)
    res = []
    left = 0
    right = k - 1
    while right < length:
        max_val = _calc_max(nums, left, right)
        res.append(max_val)
        left += 1
        right += 1
    return res
