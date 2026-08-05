"""Binary Search Tree operations: search, insert, and delete.
Provides standard BST functionality with a TreeNode class.
"""


class TreeNode:
    """Binary search tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root, n):
    """Search for a node with value n in the BST. Returns the node if found, else None."""
    if not root:
        return None
    if root.val == n:
        return root
    elif root.val > n:
        return search(root.left, n)
    else:
        return search(root.right, n)


def insert(root, n):
    """Insert a value n into the BST. Returns the root of the modified tree."""
    if not root:
        return TreeNode(n)
    if root.val == n:
        return root
    elif root.val > n:
        root.left = insert(root.left, n)
    else:
        root.right = insert(root.right, n)
    return root


def delete_node(root, n):
    """Delete a node with value n from the BST. Returns the root of the modified tree."""
    if not root:
        return None
    if root.val == n:
        if not root.left and not root.right:
            return None
        elif root.left:
            max_left = _find_max(root.left)
            root.val = max_left.val
            root.left = delete_node(root.left, max_left.val)
        else:
            min_right = _find_min(root.right)
            root.val = min_right.val
            root.right = delete_node(root.right, min_right.val)
    elif root.val > n:
        root.left = delete_node(root.left, n)
    else:
        root.right = delete_node(root.right, n)
    return root


def _find_max(root):
    """Find the node with the maximum value in a BST subtree."""
    while root.right:
        root = root.right
    return root


def _find_min(root):
    """Find the node with the minimum value in a BST subtree."""
    while root.left:
        root = root.left
    return root
