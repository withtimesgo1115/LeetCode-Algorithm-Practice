"""
LeetCode 94. 二叉树的中序遍历

给定一个二叉树的根节点 root，返回它的中序遍历。

中序遍历的顺序为：左子树 -> 根节点 -> 右子树。

示例 1：
    输入：root = [1,null,2,3]
    输出：[1,3,2]

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [1]
    输出：[1]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 定义颜色标记法，白色是新节点，灰色是已访问过的节点
        WHITE, GRAY = 0, 1
        res = [] # 定义结果列表
        stack = [(WHITE, root)] # 定义栈，初始时将根节点标记为白色并入栈
        while stack: # 当栈不为空时，继续循环
            # 弹出栈顶元素，获取颜色和节点
            color, node = stack.pop()
            # 如果节点为空，则继续下一次循环
            if node is None: continue
            # 如果节点是白色，则将其右子节点、当前节点和左子节点按顺序入栈，并将当前节点标记为灰色
            # 入栈顺序和出栈顺序相反，所以先入栈右子节点，再入栈当前节点，最后入栈左子节点
            # 这样在出栈时就会先访问左子节点，再访问当前节点，最后访问右子节点，实现中序遍历
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                # 如果节点是灰色，则将其值加入结果列表
                res.append(node.val)
        return res # 返回结果列表