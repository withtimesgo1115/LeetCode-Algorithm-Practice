class Solution{
public:
    // here we define a check function to help us to judge in recursion way
    // this func requires two pointers working separately 
    bool check(TreeNode* p, TreeNode* q){
        // the first step is to judge if current nodes are both empty nodes
        // if this is true, just return ture
        if(!p && !q) return true;
        // once there is an empty node but the other one is not empty
        // return false 
        if(!p || !q) return false;
        // for the common scenario, we should compare the value of these two nodes
        // if the values are the same, check the next node
        // left pointer checks left child node and right pointer checks right child node
        // and meanwhile left pointer also should check right child node
        // while right pointer should check left child node apparently. 
        return (p->val == q->val) && check(p->left,q->right) && check(p->right, q->left);
    }

    // this is the main logic
    // we just pass a root node here 
    bool isSymmetric(TreeNode* root){
        // here we return the result based on check function which requires
        // two pointer pointing to the root node firstly
        return check(root, root);
    }
}