const levelOrder = function(root){
    // init result array
    const res = [];
    // handle border condition
    if(!root){
        return res;
    }
    // init a queue to use BFS
    const queue = [];
    // push the first element (root node) to the queue
    queue.push(root);
    // while the queue is not empty, loop following logic
    while(queue.length) {
        // level is used to store current layer's node
        const level = [];
        // store the initial length of the queue
        const len = queue.length;
        // iterate all the nodes of current layer
        for(let i = 0; i < len; ++i){
            // get and remove the head element of the queue
            const top = queue.shift();
            // get current node's value
            level.push(top.val);
            // if current node has left child, then push to the next layer
            if(top.left){
                queue.push(top.left);
            }
            // if current node has right child, then push to the next layer
            if(top.right){
                queue.push(top.right);
            }
        }
        // push current layer array
        res.push(level);
    }
    // return result array
    return res;
}