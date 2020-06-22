// use dummy node to make sure all the node has a precursor
function ListNode(val){
    this.val = val;
    this.next = null;
}

const deleteDuplicates = function(head){
    if(!head || !head.next) return head;
    // define a dummy which is an empty node at the start position
    let dummy = new ListNode();
    // dummy's next pointer points to head node
    dummy.next = head;
    // cur iterates from dummy
    let cur = dummy;
    // while there are at least two nodes following dummy node
    while(cur.next && cur.next.next){
        // compare two nodes following cur 
        if(cur.next.val === cur.next.next.val){
            // if these two values are the same, store this data
            let val = cur.next.val;
            // check following elements continuously
            while(cur.next && cur.next.val === val){
                // if exists, jump up to the next 
                cur.next = cur.next.next;
            }
        }else{
            // if there is no duplicates, just iterate
            cur = cur.next;
        }
    }
    // return starting node
    return dummy.next;
};