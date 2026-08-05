"""
Sort List (LeetCode 148)
Given the head of a linked list, sort it in ascending order and return the sorted list.
Uses merge sort to achieve O(n log n) time complexity.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    """Sort the linked list in ascending order and return the sorted list."""
    if not head or not head.next:
        return head

    mid_node = middleNode(head)
    right_head = mid_node.next
    mid_node.next = None

    left = sortList(head)
    right = sortList(right_head)

    return mergeTwoLists(left, right)


def middleNode(head):
    """Find the middle node of the linked list using slow/fast pointers."""
    if not head or not head.next:
        return head
    slow = head
    fast = head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeTwoLists(l1, l2):
    """Merge two sorted linked lists into one sorted linked list."""
    dummy = ListNode()
    cursor = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
        cursor = cursor.next
    cursor.next = l1 if l1 else l2
    return dummy.next
