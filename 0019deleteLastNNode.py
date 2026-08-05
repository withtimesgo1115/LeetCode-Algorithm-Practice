"""
LeetCode #19 - Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of
the list and return its head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Two-pointer (fast/slow) approach - O(L) time, O(1) space.

    Use a dummy node. Move the fast pointer n steps ahead, then move
    both fast and slow together until fast reaches the last node.
    The slow pointer will then be just before the node to remove.
    """
    dummy = ListNode()
    dummy.next = head

    fast = dummy
    slow = dummy

    # Advance fast pointer by n steps
    for _ in range(n):
        fast = fast.next

    # Move both pointers until fast reaches the last node
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from the end
    slow.next = slow.next.next

    return dummy.next
