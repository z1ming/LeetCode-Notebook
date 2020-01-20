# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None:return
            helper(root.left)
            helper(root.right)
            if root.left:
                pre = root.left
                while pre.right:pre = pre.right # 找到左子树的最右结点
                pre.right = root.right # 左子树的最右结点和root.right链接
                root.right = root.left # root的左子树变为右子树
                root.left = None  # 将root左子树置空
            root = root.right
        helper(root)