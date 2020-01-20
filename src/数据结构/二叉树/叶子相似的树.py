# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#
#
#
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
#
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
#
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:  # 如果该节点为叶子结点
                    yield node.val
                yield from dfs(node.left) # 将左子树的叶子全部迭代出来
                yield from dfs(node.right)  # 将右子树的叶子全部迭代出来
        return list(dfs(root1)) == list(dfs(root2))
