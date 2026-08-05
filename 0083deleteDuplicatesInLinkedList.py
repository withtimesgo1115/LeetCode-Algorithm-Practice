"""
Remove Duplicates from Sorted List (LeetCode 83).

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head:
        return None
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
