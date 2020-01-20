# 给定一个二叉树，统计该二叉树数值相同的子树个数。
#
# 同值子树是指该子树的所有节点都拥有相同的数值。
#
# 示例：
#
# 输入: root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# 输出: 4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):
        # 基本情况，该节点没有子节点
        if node.left is None and node.right is None:
            # 找到单值子树
            self.count += 1
            return True

        is_uni = True
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val
        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val
        self.count += is_uni
        return is_uni