"""
Linked List Cycle II (LeetCode 142)
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.
Uses a flag-marking approach to detect the cycle start.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head):
    """Return the node where the cycle begins, or None if there is no cycle."""
    while head:
        if head.flag:
            return head
        else:
            head.flag = True
            head = head.next
    return None
