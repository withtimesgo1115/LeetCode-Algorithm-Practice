"""
剑指 Offer 24 / LeetCode 206. 反转链表 (Reverse Linked List)

题目描述：
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例 1：
    输入：head = [1, 2, 3, 4, 5]
    输出：[5, 4, 3, 2, 1]

示例 2：
    输入：head = [1, 2]
    输出：[2, 1]

示例 3：
    输入：head = []
    输出：[]

约束条件：
    - 链表中节点的数目范围是 [0, 5000]
    - -5000 <= Node.val <= 5000

进阶：
    链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

解题思路：
    使用迭代法，维护两个指针 pre 和 cur，依次遍历链表。
    每次将当前节点的 next 指针指向前一个节点，然后两个指针同时向后移动，
    直到 cur 为空，此时 pre 即为新的头节点。
    时间复杂度：O(n)，空间复杂度：O(1)。
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
