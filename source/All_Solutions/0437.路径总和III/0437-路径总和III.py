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