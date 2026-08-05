"""
LeetCode #4 - Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
"""


def find_median_sorted_arrays(nums1, nums2):
    """
    Brute force approach - O((m+n) log(m+n)) time.

    Merge both arrays, sort, then find the median.
    """
    merged = sorted(nums1 + nums2)
    length = len(merged)

    if length % 2 == 0:
        return 0.5 * (merged[length // 2 - 1] + merged[length // 2])
    else:
        return merged[length // 2]
