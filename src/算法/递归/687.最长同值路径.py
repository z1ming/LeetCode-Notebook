# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:
#
# 2
# 示例 2:
#
# 输入:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:
#
# 2
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node:
                return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

# 时间复杂度：O(N)，其中N是树中节点数。我们处理每个节点一次。
# 空间复杂度：O(H)，其中H是树的高度。我们递归调用栈可以达到H层的深度。