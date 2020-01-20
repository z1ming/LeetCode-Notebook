# 给定一个
# N
# 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个
# 3
# 叉树:
#
# 我们应返回其最大深度，3。
#
# 说明:
#
# 树的深度不会超过
# 1000。
# 树的节点总不会超过
# 5000。

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1