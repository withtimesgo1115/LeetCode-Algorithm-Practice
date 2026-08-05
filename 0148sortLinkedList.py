"""
148. 排序链表（Sort List）

给你链表的头节点 head，将其按升序排列并返回排序后的链表。

示例 1：
    输入：head = [4,2,1,3]
    输出：[1,2,3,4]

示例 2：
    输入：head = [-1,5,3,4,0]
    输出：[-1,0,3,4,5]

示例 3：
    输入：head = []
    输出：[]

提示：
    链表中节点的数目在范围 [0, 5 * 10^4] 内
    -10^5 <= Node.val <= 10^5

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    """Sort the linked list in ascending order and return the sorted list."""
    if not head or not head.next:
        return head

    mid_node = middleNode(head)
    right_head = mid_node.next
    mid_node.next = None

    left = sortList(head)
    right = sortList(right_head)

    return mergeTwoLists(left, right)


def middleNode(head):
    """Find the middle node of the linked list using slow/fast pointers."""
    if not head or not head.next:
        return head
    slow = head
    fast = head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeTwoLists(l1, l2):
    """Merge two sorted linked lists into one sorted linked list."""
    dummy = ListNode()
    cursor = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
        cursor = cursor.next
    cursor.next = l1 if l1 else l2
    return dummy.next
