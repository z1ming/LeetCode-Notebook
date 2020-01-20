# 给定一个
# N
# 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个
# 3
# 叉树:
#
# 返回其层序遍历:
#
# [
#     [1],
#     [3, 2, 4],
#     [5, 6]
# ]
#

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        queue = [(0,root)]
        while queue:
            level,node = queue.pop(0)
            if len(res) == level:      # 判断当前结点的层次信息
                res.append([node.val])
            else:
                res[level].append(node.val)
            if node.children:
                for i in node.children:
                    queue.append((level+1,i))
        return res