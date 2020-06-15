/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    return check(root,root);
};

var check = function(p, q){
    if(p === null && q === null) return true;
    if(p === null || q === null) return false;
    return (p.val === q.val) && check(p.left,q.right) && check(p.right, q.left);
}