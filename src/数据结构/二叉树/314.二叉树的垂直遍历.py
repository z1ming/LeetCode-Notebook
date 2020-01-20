# 给定一个二叉树，返回其结点 垂直方向（从上到下，逐列）遍历的值。
#
# 如果两个结点在同一行和列，那么顺序则为 从左到右。
#
# 示例 1：
#
# 输入: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
# 9   20
#     /\
#    /  \
#   15   7
#
# 输出:
# 
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # 迭代
        from collections import defaultdict
        if not root: return []

        lookup = defaultdict(list)

        def dfs(root,loc,depth):
            if not root:
                return
            lookup[loc].append([depth,root.val])
            dfs(root.left,loc - 1,depth + 1)
            dfs(root.right, loc + 1, depth + 1)
        dfs(root,0,0)
        return [[b for a, b in sorted(v,key=lambda x:x[0])] for k,v in sorted(lookup.items())]