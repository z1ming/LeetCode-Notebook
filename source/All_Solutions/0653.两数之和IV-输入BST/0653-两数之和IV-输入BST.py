# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        # 深度优先搜索
        def dfs(node):
            # target目标值与当前值求差
            if k - node.val in exist:
                self.res = True
                return 
            else:
                exist.add(node.val)

            # 当前没有符合调条件的数据，继续
            if not self.res: 
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)

        exist = set()
        self.res = False
        dfs(root)
        return self.res