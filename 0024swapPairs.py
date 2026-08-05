"""
Swap Nodes in Pairs (LeetCode 24)

Given a linked list, swap every two adjacent nodes and return the modified list.
Uses a recursive approach.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    second = head.next
    third = second.next
    second.next = head
    head.next = swapPairs(third)
    return second
