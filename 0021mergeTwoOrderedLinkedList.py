"""
LeetCode 21. 合并两个有序链表 (Merge Two Sorted Lists)

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1:
    输入: l1 = [1,2,4], l2 = [1,3,4]
    输出: [1,1,2,3,4,4]

示例 2:
    输入: l1 = [], l2 = []
    输出: []

示例 3:
    输入: l1 = [], l2 = [0]
    输出: [0]

提示:
    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 按非递减顺序排列
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Iterative merge with a dummy head - O(m+n) time, O(1) space.

    Use a cursor to weave nodes from l1 and l2 in sorted order.
    After one list is exhausted, attach the remainder of the other.
    """
    head = ListNode()
    cur = head

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    # Attach whichever list still has remaining nodes
    cur.next = l1 if l1 else l2

    return head.next
