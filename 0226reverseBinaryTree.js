const invertTree = function(root){
    // define recursion border
    if(!root){
        return root;
    }
    // swap right child's child nodes in recursion way
    let right = invertTree(root.right);
    // swap left child's child nodes in recursion way
    let left = invertTree(root.left);
    // swap left and right child node in current iteration 
    root.left = right;
    root.right = left;
    // return current root node
    return root;
}