"""
Merge Sorted Array (LeetCode 88).

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
as one sorted array. nums1 has a size of m + n, where the first m elements
are valid and the remaining n elements are zeros to be filled.
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
