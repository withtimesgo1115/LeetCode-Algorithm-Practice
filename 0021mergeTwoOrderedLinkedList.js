//define the nodes
function ListNode(val, next){
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

// main logic
const mergeTwoLists = function(l1, l2){
    // define the head node to ensure the linked list can be accessed
    let head = new ListNode();
    // define cursor which is just like a neil to merge all the nodes
    let cur = head;
    // make the cursor wave between l1 and l2
    while(l1 && l2){
        // if the first data of l1 is smaller than l2
        if(l1.val <= l2.val){
            // link the node of l1
            cur.next = l1;
            // l1 will move to the next node to update the node
            l1 = l1.next;
        }else{
            // link the node of l2
            cur.next = l2;
            // l2 will move to the next node to update the node
            l2 = l2.next;
        }

        // cursor also needs to move to the next
        cur = cur.next;
    }

// handle two linked lists have different length 
cur.next = l1 !== null ? l1 : l2;
// return start node of the merged list
return head.next;
};