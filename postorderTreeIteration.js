const postorderTraversal = function(root){
    const res = [];
    // border condition
    if(!root){
        return res;
    }
    // initialize the stack 
    const stack = [];
    // push root node to the stack
    stack.push(root);
    // while the stack is not empty, then push and pop again and again
    while(stack.length){
        // mark top node as current node
        const cur = stack.pop();
        // push this root node of current child tree to the top
        res.unshift(cur.val);
        // push left child to the stack
        if(cur.left){
            stack.push(cur.left);
        }
        // push right child to the stack
        if(cur.right){
            stack.push(cur.right);
        }
    }
    return res;
};