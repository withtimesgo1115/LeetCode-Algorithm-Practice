const inorderTraversal = function(root){
    const res = [];
    const stack = [];
    // use a cur node as cursor
    let cur = root;

    while(cur || stack.length){
        // use a while loop to record all the nodes when we find the leftest leaf node
        while(cur){
            stack.push(cur);
            cur = cur.left;
        }
        // pop out of the element
        cur = stack.pop();
        // push this element to the result array
        res.push(cur.val);
        // try to read cur node's right child
        cur = cur.right;
    }
    return res;
}