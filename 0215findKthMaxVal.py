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


def find_kth_largest(nums, k):
    heap = []
    n = 0

    def up_heap(low, high):
        i = high
        j = (i - 1) // 2
        while j >= low:
            if heap[j] > heap[i]:
                heap[j], heap[i] = heap[i], heap[j]
                i = j
                j = (i - 1) // 2
            else:
                break

    def down_heap(low, high):
        i = low
        j = 2 * i + 1
        while j <= high:
            if j + 1 <= high and heap[j + 1] < heap[j]:
                j = j + 1
            if heap[i] > heap[j]:
                heap[j], heap[i] = heap[i], heap[j]
                i = j
                j = j * 2 + 1
            else:
                break

    def insert(x):
        nonlocal n
        heap.append(x)
        up_heap(0, n)
        n += 1

    def create_heap():
        for i in range(k):
            insert(nums[i])

    def update_heap():
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                down_heap(0, k)

    create_heap()
    update_heap()
    return heap[0]
