# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path_num=0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        递归往下一次深度遍历根节点循环
        :param root:
        :param sum:
        :return:
        """
        if root==None:return self.path_num
        self.getPathNum(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)

        return self.path_num



    def getPathNum(self,root:TreeNode,sum:int):
        """
        依据当前树找目标值，进而找到路径数量
        :param root:
        :param sum:
        :return:
        """
        if root==None:return
        if root.val==sum:
            self.path_num+=1
        new_sum = sum-root.val
        self.getPathNum(root.left,new_sum)
        self.getPathNum(root.right,new_sum)