class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root,ma=0,mi=100000):
            if not root:
                return ma-mi
            return max(helper(root.left,max(ma,root.val),min(mi,root.val)),helper(root.right,max(ma,root.val),min(mi,root.val)))
        return helper(root)