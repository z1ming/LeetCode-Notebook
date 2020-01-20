# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# 方法一：递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype:int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
        return max(left_height,right_height)
# 时间复杂度：每个节点访问一次，因此时间复杂度是O(N)，N是节点的数量
# 空间复杂度：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，
# 递归将会被调用N次（树的高度），因此保持调用栈的存储将是O(N)。但在最好的情况下
# （树是完全平衡的），树的高度将是log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))。
# 疑问：树的高度为什么是log(N)？
# 方法二：迭代
# 使用DFS策略访问每个结点，同时每次访问时更新最大深度。
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()  # pop 默认返回最后一个元素
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth
# 时间复杂度：0(N)
# 空间复杂度：O(N)