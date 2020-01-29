class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left = self.getHigh(root.left)
        right = self.getHigh(root.right)
        if left == right:
            return root
        elif left < right:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)
        
    def getHigh(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max(self.getHigh(root.left), self.getHigh(root.right))