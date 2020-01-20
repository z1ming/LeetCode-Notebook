# 给你一棵完全二叉树，请按以下要求的顺序收集它的全部节点：
#
# 依次从左到右，每次收集并删除所有的叶子节点
# 重复如上过程直到整棵树为空
# 示例:
#
# 输入: [1,2,3,4,5]
#  
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# 输出: [[4,5,3],[2],[1]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            height = max(left,right)
            if len(res) == height:
                res.append([])
            res[height].append(root.val)
            return height + 1
        helper(root)
        return res
