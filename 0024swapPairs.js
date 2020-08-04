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
// recursion method
/*
在本题中：

返回值：交换完成的子链表
调用单元：设需要交换的两个点为 head 和 next，head 连接后面交换完成的子链表，next 连接 head，完成交换
终止条件：head 为空指针或者 next 为空指针，也就是当前无节点或者只有一个节点，无法进行交换
*/
var swapPairs = function(head) {
    if(!head || !head.next){
        return head;
    }
    let second = head.next;
    let third = second.next;
    second.next = head;
    head.next = swapPairs(third);
    return second;
};