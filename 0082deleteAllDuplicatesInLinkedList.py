"""
82. 删除排序链表中的重复元素 II

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。
返回 已排序的链表 。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

提示：
- 链表中节点数目可能满足 0 <= 节点数 <= 300
- -100 <= Node.val <= 100
- 链表已经按升序排列
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
