# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
# 例如：
#
# 输入: 二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13

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