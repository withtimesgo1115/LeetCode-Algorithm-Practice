"""
Reverse Linked List II (LeetCode 92).

Reverse a linked list from position m to position n (1-indexed).
Return the head of the modified linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, m, n):
    # use a dummy node to simplify edge cases
    dummy = ListNode()
    dummy.next = head

    # move p to the node just before the reversal interval
    p = dummy
    for _ in range(m - 1):
        p = p.next

    # leftHead is the predecessor of the reversal interval
    leftHead = p
    # start is the first node of the reversal interval
    start = leftHead.next
    # pre and cur are used for the actual reversal
    pre = start
    cur = pre.next

    # reverse the links within the interval
    for _ in range(m, n):
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node

    # connect the predecessor to the new head of the reversed section
    leftHead.next = pre
    # connect the original first node to the node after the reversed section
    start.next = cur

    return dummy.next
