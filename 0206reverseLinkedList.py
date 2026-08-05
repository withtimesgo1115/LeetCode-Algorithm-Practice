"""
LeetCode 206. 反转链表

题目描述：
    给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

示例 2：
    输入：head = [1,2]
    输出：[2,1]

示例 3：
    输入：head = []
    输出：[]

提示：
    链表中节点的数目范围是 [0, 5000]
    -5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式反转。你能否用两种方法解决这道题？

本文件提供两种解法：
    - 迭代法：时间复杂度 O(n)，空间复杂度 O(1)
    - 递归法：时间复杂度 O(n)，空间复杂度 O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head):
    """Iteration method. Time: O(n), Space: O(1)."""
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


def reverse_list_recursive(head):
    """Recursion method. Time: O(n), Space: O(n)."""
    if not head or not head.next:
        return head

    node = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return node
