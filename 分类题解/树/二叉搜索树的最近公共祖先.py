# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树
# T
# 的两个结点
# p、q，最近公共祖先表示为一个结点
# x，满足
# x
# 是
# p、q
# 的祖先且
# x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉搜索树: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
#
# 示例
# 1:
#
# 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# 输出: 6
# 解释: 节点
# 2
# 和节点
# 8
# 的最近公共祖先是
# 6。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            if not current_node:
                return False

            left = recurse_tree(current_node.left)

            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:  # =2即父结点是其本身，>2即搜索到p和q
                self.ans = current_node

            # 有一个为真即可返回
            return mid or left or right

        recurse_tree(root)
        return self.ans