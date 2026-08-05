"""
LeetCode 239. 滑动窗口最大值

题目描述：
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。

示例 1：
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]

    解释：
        滑动窗口的位置                最大值
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

示例 2：
    输入：nums = [1], k = 1
    输出：[1]

提示：
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length

本文件使用单调递减双端队列实现 O(n) 时间复杂度。
队列中存储数组下标，保持队列中对应元素值单调递减。
"""

from collections import deque


def max_sliding_window(nums, k):
    res = []
    window = deque()

    if not nums or k <= 0:
        return res

    for i in range(len(nums)):
        # Remove the element that has fallen out of the window
        if i - window[0] >= k:
            window.popleft()

        # Remove elements smaller than the current element
        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        window.append(i)

        # Start recording results once the first full window is formed
        if i >= k - 1:
            res.append(nums[window[0]])

    return res
