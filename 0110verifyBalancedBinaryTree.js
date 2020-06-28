const isBalanced = function(root){
    // define a flag, if there is a differnce of absolute larger than 1
    // the flag will be marked as false
    let flag = true;
    // define recursion logic using dfs
    function dfs(root){
        // empty tree, height is 0 and flag is false, just return
        if(!root || !flag){
            return 0;
        }
        // define a left child tree's height
        const left = dfs(root.left);
        // define a right child tree's height
        const right = dfs(root.right);
        //if the height difference is larger than 1, flag will be changed to false
        // return a uneffective value 0
        if(Math.abs(left-right) > 1){
            flag = false;
            return 0;
        }
        // return current subtree's height
        return Math.max(left,right) + 1;
    }

    // dfs's entrance
    dfs(root);
    // return flag value
    return flag;
}