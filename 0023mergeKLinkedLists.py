"""
Merge K Sorted Linked Lists (LeetCode 23)

Given an array of sorted linked lists, merge all of them into one sorted linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    nodes = []
    for n in lists:
        while n:
            nodes.append(n)
            n = n.next
    nodes.sort(key=lambda node: node.val)
    result = None
    for node in reversed(nodes):
        node.next = result
        result = node
    return result
