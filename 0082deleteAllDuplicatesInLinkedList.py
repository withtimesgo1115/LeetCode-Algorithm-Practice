"""
Remove All Duplicates from Sorted Linked List (LeetCode 82)

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.
Uses a dummy node to ensure all nodes have a precursor.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    dummy = ListNode()
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            val = cur.next.val
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
