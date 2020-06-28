function TreeNode(val){
    this.val = val;
    this.left = this.right = null;
}

const sortedArrayToBST = function(nums){
    // border condition
    if(!nums.length){
        return null;
    }

    // root node is the result of pulling the array from the middle position
    const root = buildBST(0, nums.length-1);

    // define a function to build BST
    // its parameters are subarray's index range
    function buildBST(low, high){
        // dicotomy basic judgement
        // if low is higher than high, it shows the recursion has finished then return result from the deepest position
        if(low > high){
            return null;
        }
        // get the middle index 
        const mid = Math.floor(low + (high - low) / 2);
        // create a treenode as root node of current subtree  
        const cur = new TreeNode(nums[mid]);
        // build left subtree
        cur.left = buildBST(low, mid - 1);
        // build right subtree
        cur.right = buildBST(mid + 1, high);
        // return current node
        return cur;
    }
    // return root node
    return root;
}