"""
Linked List Cycle (LeetCode 141)
Given the head of a linked list, determine if the linked list has a cycle in it.
Uses a flag-marking approach to detect cycles.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    """Return True if the linked list has a cycle, False otherwise."""
    while head:
        if head.flag:
            return True
        else:
            head.flag = True
            head = head.next
    return False
