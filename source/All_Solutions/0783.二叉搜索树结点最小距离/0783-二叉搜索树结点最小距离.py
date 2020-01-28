class Solution:
    def __init__(self):
        self.minus = 2 ** 31
        self.pre = 2 ** 31
        
    def dfs(self,root):
        if not root:
            return
        
        self.dfs(root.right)
        self.minus = min(self.minus, self.pre - root.val)
        self.pre = root.val
        self.dfs(root.left)
      
    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        
        
        return self.minus