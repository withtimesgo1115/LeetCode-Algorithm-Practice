"""
堆操作（Heap Operations）—— 下沉与上浮

算法描述：
    堆（Heap）是一种特殊的完全二叉树，通常用数组来表示。
    在大顶堆（Max Heap）中，每个节点的值都大于或等于其子节点的值。

    数组中索引为 i 的节点：
        - 左子节点索引：2 * i + 1
        - 右子节点索引：2 * i + 2
        - 父节点索引：(i - 1) // 2

    本文件实现了两个核心堆操作：

一、下沉操作（down_heap / sift down）：
    将位于索引 low 的元素向下移动，以恢复堆的性质。
    常用于堆排序和删除堆顶元素后的调整。

    步骤：
        1. 从当前节点开始，找到其较大的子节点。
        2. 如果当前节点小于较大的子节点，则交换两者。
        3. 继续向下比较，直到当前节点大于等于其子节点或到达叶子节点。

二、上浮操作（up_heap / sift up）：
    将位于索引 high 的元素向上移动，以恢复堆的性质。
    常用于向堆中插入新元素后的调整。

    步骤：
        1. 从新插入的节点开始，与其父节点比较。
        2. 如果父节点小于当前节点，则交换两者。
        3. 继续向上比较，直到当前节点小于等于其父节点或到达根节点。

时间复杂度：
    - 单次下沉/上浮：O(log n)，最多移动树的高度层。
    - 建堆（对所有非叶节点执行下沉）：O(n)
    - 堆排序：O(n log n)
空间复杂度：O(1)，原地操作。

示例（大顶堆）：
    数组表示：[1, 3, 2, 6, 5, 4]
    对应的完全二叉树：
            1
          /   \
         3     2
        / \   /
       6   5 4

    执行 down_heap(heap, 0, 5) 后：
    数组变为：[6, 5, 4, 3, 1, 2]
    对应的完全二叉树：
            6
          /   \
         5     4
        / \   /
       3   1 2
"""

import math


def down_heap(heap, low, high):
    """Sift down: move the element at index `low` downward to restore heap property.

    Args:
        heap: The list representing the heap.
        low: The starting index (top of the subtree).
        high: The ending index (bottom of the subtree).
    """
    i = low
    j = i * 2 + 1
    while j <= high:
        # If right child exists and is larger than left child, pick right child
        if j + 1 <= high and heap[j + 1] > heap[j]:
            j = j + 1
        # If current node is smaller than the larger child, swap them
        if heap[i] < heap[j]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = j * 2 + 1
        else:
            break


def up_heap(heap, low, high):
    """Sift up: move the element at index `high` upward to restore heap property.

    Args:
        heap: The list representing the heap.
        low: The starting index (top boundary).
        high: The ending index (the newly inserted element).
    """
    i = high
    j = (i - 1) // 2
    while j >= low:
        if heap[j] < heap[i]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = (i - 1) // 2
        else:
            break
