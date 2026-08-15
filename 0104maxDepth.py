# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        WHITE, GRAY = 0, 1

        max_depth = 0
        stack = [(WHITE, root, 1)]

        while stack:
            color, node, depth = stack.pop()

            if node is None:
                continue

            if color == WHITE:
                # 当前节点还没有访问
                # 先将当前节点标记为 GRAY
                stack.append((GRAY, node, depth))

                # 将左右子节点放入栈中
                stack.append((WHITE, node.right, depth + 1))
                stack.append((WHITE, node.left, depth + 1))

            else:
                # 当前节点已经被访问
                max_depth = max(max_depth, depth)

        return max_depth        