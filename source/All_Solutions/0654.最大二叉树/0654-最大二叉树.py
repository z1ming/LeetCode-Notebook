class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []: return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[0 : max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1 :])
        return root

