# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 返回层次遍历，将结果的最后以为添加到结果中
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels = []
        if not root:
            return levels
        def helper(node,level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root,0)
        res = []
        for i in levels:
            res.append(i[-1])
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 利用字典，对于同一深度作为键时，最后访问的值为最右侧节点
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict() # depth -> node.val
        max_depth = -1

        queue = deque([(root,0)])
        while queue:
            node,depth = queue.popleft()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth,depth)

                rightmost_value_at_depth[depth] = node.val
                queue.append((node.left,depth + 1))
                queue.append((node.right,depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]