function ListNode(val){
    this.val = val;
    this.next = null;
}

const removeNthFromEnd = function(head, n){
    //initialize dummy node
    const dummy = new ListNode();
    // note that dummy'next node is head node
    dummy.next = head;
    // define two pointers pointing dummy 
    let fast = dummy;
    let slow = dummy;

    // fast node moves n steps, use n as counter
    while(n!==0){
        fast = fast.next;
        n--;
    }

    // fats and slow pointers move together
    while(fast.next){
        fast = fast.next;
        slow = slow.next;
    }

    // slow pointer delete the next node which is what we want to delete
    slow.next = slow.next.next;

    //return the head node
    return dummy.next;
};