# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法：递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        begin = 0
        end = len(nums) - 1
        if begin > end:
            return None
        mid = (begin + end) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[begin:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:end+1])
        return root