'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() # 创建一个伪节点，方便返回结果
        carry = 0 # 进位
        # 遍历两个链表，直到两个链表都为空，并且没有进位
        while l1 or l2 or carry:
            # 计算当前位的和
            s = carry
            # 如果当前链表不为空，则将当前节点的值加入到和中，并移动到下一个节点
            if l1:
                s += l1.val
                l1 = l1.next
            # 如果当前链表不为空，则将当前节点的值加入到和中，并移动到下一个节点
            if l2:
                s += l2.val
                l2 = l2.next
            # 创建一个新的节点，值为当前位的和对10取余的结果
            cur.next = ListNode(s % 10)
            # 更新进位为当前位的和除以10的结果
            carry = s // 10
            # 移动到下一个节点
            cur = cur.next
        # 返回结果链表，跳过伪节点
        return dummy.next
        