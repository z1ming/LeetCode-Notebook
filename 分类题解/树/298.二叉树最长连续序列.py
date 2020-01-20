# 给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。
#
# 该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。
#
# 这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。
#
# 示例 1：
#
# 输入:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# 输出: 3
#
# 解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfs(root,None,0)
    def dfs(self,node,parent,length):
        if not node:return length
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        return max(length, max(self.dfs(node.left,node,length),self.dfs(node.right,node,length)))