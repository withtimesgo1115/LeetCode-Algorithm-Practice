"""
LeetCode 88. 合并两个有序数组

给你两个按非递减顺序排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n，
分别表示 nums1 和 nums2 中的元素数目。请你合并 nums2 到 nums1 中，使合并后的
数组同样按非递减顺序排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，
nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0，应忽略。
nums2 的长度为 n。

示例 1：
    输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    输出：[1,2,2,3,5,6]
    解释：需要合并 [1,2,3] 和 [2,5,6]，合并结果是 [1,2,2,3,5,6]。

示例 2：
    输入：nums1 = [1], m = 1, nums2 = [], n = 0
    输出：[1]
    解释：需要合并 [1] 和 []，合并结果是 [1]。

示例 3：
    输入：nums1 = [0], m = 0, nums2 = [1], n = 1
    输出：[1]
    解释：需要合并的数组是 [] 和 [1]，合并结果是 [1]。注意，因为 m = 0，
    所以 nums1 中没有元素。nums1 中初始仅剩的 0 应当被忽略。

提示：
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9
"""


def merge(nums1, m, nums2, n):
    # i points to the last meaningful element in nums1
    # j points to the last element in nums2
    # k points to the last position in nums1
    i = m - 1
    j = n - 1
    k = m + n - 1

    # compare from the end and place the larger value at position k
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    # if nums2 still has remaining elements, copy them into nums1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
