# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
# time:O(N)
# space:O(N)

# 方法二：迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return

        queue = deque([root,])
        while queue:
            cur = queue.popleft()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root
# time:O(N)
# space:O(N)