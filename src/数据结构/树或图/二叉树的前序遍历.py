# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

# 方法二：迭代
# 从跟节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。
# 具体是怎么压的，还没搞清楚。
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # [root, ]是方便多行定义的时候复制的,否则容易在添加元素的过程中缺少逗号出现语法错误.
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output
# 时间复杂度：访问每个节点恰好一次，时间复杂度为O(N)，其中N是节点的个数，也就是树的大小。
# 空间复杂度：取决于数的结构，最坏情况存储整棵树，因此空间复杂度为O(N)。