# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
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

# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 使用BFS，BFS其实就相当于层次遍历，DFS包含三种方式：先序，后序，中序
        # 用数组存储结果
        levels = []
        if not root:
            return levels  # 考虑边界条件

        # 使用辅助函数进行递归
        def helper(node, level):  # 该函数有两个参数，结点及所在层级
            if len(levels) == level:
                levels.append([])

            # append当前结点值
            levels[level].append(node.val)

            # 处理孩子结点
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels
# time:O(N)。因为每个结点恰好会被运算一次
# space:O(N)。保存输出结果的数组包含N个结点的值

# 方法二：迭代
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 使用队列进行迭代
        levels = []
        if not root:
            return levels
        # 初始化队列只包含一个节点root和层次编号0：level= 0
        level = 0
        queue = deque([root,])
        while queue:
            # 从当前层开始
            levels.append([])
            # 计算当前层的节点个数
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft() # 将这些元素从队列中弹出
                levels[level].append(node.val)  # 将这些元素加入levels当前层的空列表中
                # 将他们的孩子节点作为下一层压入队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 进入下一层
            level += 1
        return levels
# time:O(N)。因为每个结点恰好会被运算一次
# space:O(N)。保存输出结果的数组包含N个结点的值