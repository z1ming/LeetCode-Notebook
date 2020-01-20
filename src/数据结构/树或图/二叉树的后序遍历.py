# 给定一个二叉树，返回它的 后序 遍历。
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:return []
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res

# 方法二：迭代
# 从跟节点开始依次迭代，弹出栈顶元素输出到输出列表中，然后一次压
# 入它的所有孩子节点，按照从上到下，从左到右的顺序依次压入栈中。
# 因为深度优先搜索后序遍历的顺序是从下到上，从左到右，所以需要将输出列表逆序输出。
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root is not None:
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return output[::-1]
# 时间复杂度：访问每个节点恰好一次，因此时间复杂度为O(N)，其中N是节点的个数，也就是树的大小。
# 空间复杂度：取决于数的结构，最坏情况需要保存整棵树，因此空间复杂度为O(N)。