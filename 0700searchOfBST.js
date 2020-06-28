var searchBST = function(root, val) {
    if(!root){
        return null;
    }
    if(root.val === val){
        return root;
    }
    else if(root.val < val){
        return searchBST(root.right, val);
    }
    else{
        return searchBST(root.left, val);
    }
};