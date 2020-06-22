function ListNode(val){
    this.val = val;
    this.next = null;
}

const hasCycle = function(head){
    // when the head exists, continue the iteration
    while(head){
        // if flag has been set up, the loop exists 
        if(head.flag){
            return true;
        }else{
            // if flag does not exist, then set up a flag firstly
            head.flag = true;
            // go to the next one
            head = head.next;
        }
    }
    // default result is to return false
    return false;
};