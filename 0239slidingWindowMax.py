"""
Sliding Window Maximum.
Given an array nums and a window size k, return the maximum
value in each sliding window as it moves from left to right.
Uses a monotonic deque for O(n) time complexity.
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
