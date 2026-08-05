"""
Reverse a singly linked list.
Provides both iterative O(n) time / O(1) space
and recursive O(n) time / O(n) space solutions.
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
