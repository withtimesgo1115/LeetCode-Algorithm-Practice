"""
LeetCode 19. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1:
    输入: head = [1,2,3,4,5], n = 2
    输出: [1,2,3,5]

示例 2:
    输入: head = [1], n = 1
    输出: []

示例 3:
    输入: head = [1,2], n = 1
    输出: [1]

提示:
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？
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
