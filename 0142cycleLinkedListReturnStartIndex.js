function ListNode(val) {
    this.val = val;
    this.next = null;
}

const detectCycle = function(head){
    // when the head exists then iterate the list
    while(head){
        // if we found the flag, just return the node 
        if(head.flag){
            return head;
            // if we cannot found the flag this time
        }else{
            // create a flag
            head.flag = true;
            // then jump to the next node
            head = head.next;
        }
    }
    // default result is null node
    return null;
}