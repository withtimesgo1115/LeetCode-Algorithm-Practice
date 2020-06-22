function ListNode(val){
    this.val = val;
    this.next = null;
};

const deleteDuplicates = function(head){
    if(!head) return null;
    let cur = head;
    while(cur && cur.naxt){
        if(cur.val === cur.next.val){
            cur.next = cur.next.next;
        }else{
            cur = cur.next;
        }
    }
    return head;
};


