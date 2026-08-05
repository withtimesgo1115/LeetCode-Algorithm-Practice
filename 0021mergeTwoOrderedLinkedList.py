"""
LeetCode #21 - Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list
should be made by splicing together the nodes of the first two lists.
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
