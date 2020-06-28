const isValidBST = function(root){
    // define dfs recursion function which requires maxValue and minValue
    function dfs(root, minValue, maxValue){
        if(!root){
            // empty tree can return true
            return true;
        }
        // if left child is larger or equal to current node or right child is smaller or equal to current node, return false
        if(root.val <= minValue || root.val >= maxValue) return false;
        // use recursion to ensure left and right subtrees should both be valid
        return dfs(root.left, minValue, root.val) && dfs(root.right, root.val, maxValue);
    }

    // init minValue and maxValue to INFINITY
    return dfs(root, -Infinity, Infinity);
}