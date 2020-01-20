# 给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左叶节点。返回新的根。
#
# 例子:
#
# 输入: [1,2,3,4,5]
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# 输出: 返回二叉树的根 [4,5,2,#,#,3,1]
#
#    4
#   / \
#  5   2
#     / \
#    3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = parent_right = None
        while root:
            root_left = root.left
            root.left = parent_right
            parent_right = root.right
            root.right = parent
            parent = root
            root = root_left
        return parent