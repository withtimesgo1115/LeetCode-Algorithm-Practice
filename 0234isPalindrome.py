'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
 

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head # 定义快指针
        slow = head # 定义慢指针
        pre = None # pre 保存反转后的前半部分链表
        # 快慢指针找到链表中点，并反转前半部分链表
        while fast and fast.next:
            fast = fast.next.next # 快指针每次走两步
            # 反转链表操作
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        # 如果链表长度为奇数，slow需要再往前走一步
        if fast:
            slow = slow.next
        # 比较反转后的前半部分链表和后半部分链表
        while slow:
            # 如果前半部分链表和后半部分链表的值不相等，则不是回文链表，直接返回False
            if pre.val != slow.val:
                return False
            # 如果相等，则继续比较下一个节点
            pre = pre.next
            slow = slow.next
        return True
        



        


        