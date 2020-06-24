const preorderTraversal = function(root){
    const res = [];
    // border condition
    if(!root){
        return res;
    }
    // init stack structure
    const stack = [];
    // root node enter the stack
    stack.push(root);
    // while stack is not empty, pop and push again and again
    while(stack.length){
        // the top node of stack is marked as current node 
        const cur = stack.pop();
        // add current node's value to the result
        res.push(cur.val);
        // if current node has right child
        if(cur.right){
            stack.push(cur.right);
        }
        // if current node has right child
        if(cur.left){
            stack.push(cur.left);
        }
    }
    return res;
};