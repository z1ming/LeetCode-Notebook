# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self,root:TreeNode) -> TreeNode:
        if not root:
            return root
        if root.right:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        else:
            root.val += self.total
            self.total = root.val
            self.convertBST(root.left)
        return root
