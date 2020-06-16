// 后序遍历 递归法 先左节点 后右节点 最后节点的值

function TreeNode(val){
    this.val = val;
    this.left = this.right = null;
}

var postorderTraversal = function(root){
    let ans = [];
    var postorderTraversalNode = (node) => {
        if(node){
            postorderTraversalNode(node.left);
            postorderTraversalNode(node.right);
            ans.push(node.val);
        }
    }
    postorderTraversal(root);
    return ans;
}


