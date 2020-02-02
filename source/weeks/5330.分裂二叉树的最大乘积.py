# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def getSum(root):
            if not root:
                return 0
            ret = getSum(root.left) + getSum(root.right) + root.val
            hashmap[root] = ret
            return ret
        hashmap = {}
        totalSum = getSum(root)
        ans = 0
        for k in hashmap:
            ans = max(ans,(totalSum - hashmap[k]) * hashmap[k])
        return ans % (10**9+7)