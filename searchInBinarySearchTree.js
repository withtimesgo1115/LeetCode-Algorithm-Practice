// this function is used to find certain data in a binary search tree
function search(root, n){
    if(!root){
        return;
    }
    if(root.val === n){
        console.log("the target node is: ", root);
    }else if(root.val > n){
        search(root.left, n);
    }else{
        search(root.right, n);
    }
}

function insert(root, n){
    if(!root){
        root = new TreeNode(n);
        return;
    }
    if(root.val === n){
        return;
    }
    else if(root.val > n){
        insert(root.left, n);
    }else{
        insert(root.right, n);
    }
}

function deleteNode(root, n){
    if(!root){
        return;
    }
    if(root.val === n){
        if(!root.left && !root.right){
            root = null;
        }else if(root.left){
            const maxLeft = findMax(root.left);
            root.val = maxLeft.val;
            deleteNode(root.left, maxLeft.val);
        }else{
            const minRight = findMin(root.right);
            root.val = minRight.val;
            deleteNode(root.right, minRight.val);
        }
    }else if(root.val > n){
        deleteNode(root.left, n);
    }else{
        deleteNode(root.right, n);
    }
}

function findMax(root){
    while(root.right){
        root = root.right;
    }
}

function findMin(root){
    while(root.left){
        root = root.left;
    }
}