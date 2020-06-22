function ListNode(val){
    this.val = val;
    this.next = null;
}

const reverseList = function(head){
    // define pre pointer
    let pre = null;
    // define cur pointer pointing head node
    let cur = head;
    // when cur doesn't point to null, iterate 
    while(cur != null){
        // record the next node
        let next = cur.next;
        // reverse the pointer
        cur.next = pre;
        // move pre forward 
        pre = cur;
        // move cur forward
        cur = next;
    }
    // reverse finished, pre will become the head node of the new list
    return pre;
};