# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def helper(node,level):
            # start the current level
            if len(levels) == level:
                levels.append([])
            # append the current node value
            levels[level].append(node.val)
            # process child nodes for the next level
            if node.left:
                helper(node.left,level + 1)
            if node.right:
                helper(node.right,level + 1)
        helper(root,0)
        return levels
# 时间复杂度：O(N),因为每个结点恰好会被运算一次。
# 空间复杂度：O(N)，保存输出结果的数组包含N个结点的值。

# 方法二：迭代
# 使用队列，可以使用deque的append和popleft()函数来快速实现队列的功能。
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # go to next level
            level += 1
        return levels
# 时间复杂度：O(N),因为每个结点恰好会被运算一次。
# 空间复杂度：O(N)，保存输出结果的数组包含N个结点的值。