"""
Reverse Linked List (Sword Offer 24 / LeetCode 206)

Reverse a singly linked list and return the new head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    pre = None
    cur = head
    while cur is not None:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    return pre
