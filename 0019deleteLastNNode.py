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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 定义一个头结点，方便删除操作
        dummy = ListNode(0)
        dummy.next = head
        p = dummy # 定义一个指针p，指向头结点
        q = dummy  # 定义一个指针q，指向头结点

        # 让q指针先走n+1步，这样p和q之间就有n个节点的间隔
        for _ in range(n + 1):
            q = q.next
        # 让p和q同时走，直到q走到链表的末尾，这样p就指向了倒数第n个节点的前一个节点
        while q:
            p = p.next
            q = q.next
        # 删除倒数第n个节点
        p.next = p.next.next
        # 返回链表的头结点
        return dummy.next
            

        
