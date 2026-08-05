"""
485. 最大连续 1 的个数 (Max Consecutive Ones)

给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

示例 1：
    输入：nums = [1,1,0,1,1,1]
    输出：3
    解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3。

示例 2：
    输入：nums = [1,0,1,1,0,1]
    输出：2

提示：
    1 <= nums.length <= 10^5
    nums[i] 不是 0 就是 1
"""


def find_max_consecutive_ones(nums: list[int]) -> int:
    """Return the maximum number of consecutive 1s in the array."""
    count = 0
    max_count = 0

    if 0 not in nums:
        return len(nums)

    for num in nums:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count
