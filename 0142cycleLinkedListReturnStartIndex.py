"""
142. 环形链表 II（Linked List Cycle II）

给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，
则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾端连接到链表
中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos
不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改链表。

示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：返回索引为 1 的链表节点
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：返回索引为 0 的链表节点
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：返回 null
    解释：链表中没有环。

提示：
    链表中节点的数目范围在范围 [0, 10^4] 内
    -10^5 <= Node.val <= 10^5
    pos 的值为 -1 或者链表中的一个有效索引
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 定义快慢指针，初始都指向链表头节点
        fast, slow = head, head
        while True: # 无限循环，直到快慢指针相遇或链表无环
            if not (fast and fast.next): 
                return # 如果快指针为空或快指针的下一个节点为空，说明链表无环，返回 None
            # 快指针每次移动两步，慢指针每次移动一步
            fast, slow = fast.next.next, slow.next
            if fast == slow:  # 如果快慢指针相遇，说明链表有环，跳出循环
                break
        # 当快慢指针相遇时，将快指针重新指向链表头节点，慢指针保持在相遇点
        fast = head
        # 快慢指针每次都移动一步，直到再次相遇，相遇点即为环的入口节点
        while fast != slow:
            fast, slow = fast.next, slow.next
        # 返回环的入口节点
        return slow
        
        
