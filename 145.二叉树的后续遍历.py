# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        # 与前序中序一样，同样的套路,先定义helper函数，然后递归
        def helper(root):
            if not root:
                return []
            # 以下三行代码按照左->右->根的顺序写
            helper(root.left)
            helper(root.right)
            output.append(root.val)

        helper(root)
        return output
# time:O(N)。我们遍历了每个结点
# space:O(N)，取决于树的结构，最坏情况存储整棵树，因此空间复杂度是O(N)

# 方法二：迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 处理边界条件
        if not root:
            return []
        # 先弹出根节点，再依次压入左孩子，右孩子；这样弹出顺序为根->右->左。最后逆序恰好为左->右->根
        stack, output = [root,],[] # 提前把root压入栈中了
        while stack:
            root = stack.pop()     # 弹出根节点
            if root:
                output.append(root.val)
                if root.left:      # 如果左孩子不为空，压入左孩子
                    stack.append(root.left)
                if root.right:     # 如果右孩子不为空，压入右孩子
                    stack.append(root.right)
        return output[::-1]