function ListNode(val){
    this.val = val;
    this.next = null;
}

const reverseBetween = function(head, m, n){
    //define pre\cur and use leftHead to store the precessor of the interval
    let pre, cur, leftHead;
    // use dummy node
    const dummy = new ListNode();
    dummy.next = head;
    // define a cursor called p which is used to iterate the list
    let p = dummy;
    // move p (m-1) steps and let p stay at the previous position of the interval 
    for(let i = 0; i < m - 1; i++){
        p = p.next;
    }
    //store the precursor node at leftHead
    leftHead = p;
    // start is the first node of the reverse interval
    let start = leftHead.next;
    // pre points to start
    pre = start;
    // cur points to the next node of start
    cur = pre.next;
    // reverse operation
    for(let i = m; i < n; i++){
        // next should be declared in the loop
        let next = cur.next;
        cur.next = pre;
        pre = cur;
        cur = next;
    }
    // leftHead.next is the first node (pre) of the reverse linked list
    leftHead.next = pre;
    // make the last node of the interval point to cur
    start.next = cur;
    // dummy.next always points to the head node
    return dummy.next;
};