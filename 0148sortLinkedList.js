/*
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    // 递归结束条件
    if(!head || !head.next){
        return head;
    }
    // 找到链表中间节点并断开链表 & 递归下探
    let midNode = middleNode(head);
    let rightHead = midNode.next;
    midNode.next = null;

    let left = sortList(head);
    let right = sortList(rightHead);

    return mergeTwoLists(left, right);
};

// 合并
var middleNode = function(head){
    if(!head || !head.next){
        return head;
    }
    let slow = head;
    let fast = head.next.next;
    
    while(fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};

// 合并两个有序链表
var mergeTwoLists = function(l1, l2){
    let head = new ListNode();
    let cursor = head;
    while(l1 && l2){
        if(l1.val <= l2.val){
            cursor.next = l1;
            l1 = l1.next;
        }else{
            cursor.next = l2;
            l2 = l2.next;
        }
        cursor = cursor.next;
    }
    cursor.next = l1 !== null ? l1 : l2;
    return head.next; 
};