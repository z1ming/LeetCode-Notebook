# 给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。
#
# 结点 p 的后继是值比 p.val 大的结点中键值最小的结点。
#
#  
#
# 示例 1:
#
#
#
# 输入: root = [2,1,3], p = 1
# 输出: 2
# 解析: 这里 1 的顺序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val > p.val:
                return self.inorderSuccessor(root.left, p) or root
            return self.inorderSuccessor(root.right, p)