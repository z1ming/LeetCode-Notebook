# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        self.ans = 0
        if self.dfs(root)==2:
            self.ans+=1
        return self.ans
    
    
    #0： 该结点附近有未被监视结点，安装监控器
    #1：该结点周围有监控器或该结点不存在，都不用安装监控器
    #2：该结点附近没有监控器，表示其附近需要监控器
    def dfs(self,root):
        if not root:
            return 1
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l==2 or r==2:
            self.ans+=1
            return 0
        elif l==0 or r==0:
            return 1
        else:
            return 2