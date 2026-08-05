"""
Find the kth largest element in an unsorted array using a min-heap
of size k. The heap root ends up being the kth largest element.
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
