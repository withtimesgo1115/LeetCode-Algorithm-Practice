/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

 // iteration method 
 // time: O(n). space: O(1)
 var reverseList = function(head){
     let cur = head;
     let prev = null;
     while(cur){
         let temp = cur.next;
         cur.next = prev;
         prev = cur;
         cur = temp;
     }
     return prev;
 };

 // recursion method
 // time: O(n) space: O(n)
 var reverseList = function(head){
     if(!head || !head.next) return head;
     
     const node = reverseList(head.next);
     head.next.next = head;
     head.next = null;

     return node;
 };