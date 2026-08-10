"""
LeetCode 21. 合并两个有序链表 (Merge Two Sorted Lists)

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1:
    输入: l1 = [1,2,4], l2 = [1,3,4]
    输出: [1,1,2,3,4,4]

示例 2:
    输入: l1 = [], l2 = []
    输出: []

示例 3:
    输入: l1 = [], l2 = [0]
    输出: [0]

提示:
    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 按非递减顺序排列
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归法
        if not list1: return list2 # 如果 list1 为空，则直接返回 list2
        if not list2: return list1 # 如果 list2 为空，则直接返回 list1
        # 比较两个链表的头节点的值，选择较小的节点作为合并后的链表的头节点
        if list1.val <= list2.val:
            # 如果 list1 的头节点的值较小，则将 list1 的头节点作为合并后的链表的头节点，并递归地合并 list1 的剩余部分和 list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            # 返回合并后的链表的头节点
            return list1
        else:
            # 如果 list2 的头节点的值较小，则将 list2 的头节点作为合并后的链表的头节点，并递归地合并 list1 和 list2 的剩余部分
            list2.next = self.mergeTwoLists(list1, list2.next)
            # 返回合并后的链表的头节点
            return list2