# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
#
# 示例 1：
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans,dic = [],{}
        def f(r):
            if not r:
                return ' '
            s = str(r.val) + f(r.left) + f(r.right)
            if s not in dic:
                dic[s] = True
            elif dic[s]:
                ans.append(r)
                dic[s] = False
            return s
        f(root)
        return ans