"""
LeetCode 92. 反转链表 II

给你单链表的头指针 head 和两个整数 left 和 right，其中 left <= right。
请你反转从位置 left 到位置 right 的链表节点，返回反转后的链表。

示例 1：
    输入：head = [1,2,3,4,5], left = 2, right = 4
    输出：[1,4,3,2,5]

示例 2：
    输入：head = [5], left = 1, right = 1
    输出：[5]

提示：
    链表中节点数目为 n
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
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
