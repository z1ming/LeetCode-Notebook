# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归-深度优先搜索
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 先判断节点是否为空
        if not root:
            return 0

        children = [root.left, root.right]
        # 如果没有叶子
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
# 时间复杂度：O（N）我们访问每个节点一次，时间复杂度为O（N），其中N是节点个数
# 空间复杂度：最坏情况下，递归会调用Nci，因此栈的空间开销是O（N）。但在最好情况下，树是完全平衡的，高度只有logN，因此再这种情况下空间复杂度只有O（logN）

# 方法二：深度优先搜索迭代
# 从一个包含根节点的栈开始，当前深度为1
# 然后开始迭代，弹出当前栈顶元素，将它的孩子节点压入栈中。当遇到叶子节点时更新最小深度。
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack,min_depth = [(1,root)],float('inf')

        while stack:
            depth,root = stack.pop()
            children = [root.left,root.right]
            if not any(children):
                min_depth = min(min_depth,depth)
            for c in children:
                if c:
                    stack.append([depth+1,c])
        return min_depth
# 时间复杂度：每个节点恰好被访问一遍，复杂度为O（N）。
# 空间复杂度：最坏的情况下我们会在栈中保存郑科树，此时空间复杂度为O（N）

# 方法三：宽度优先搜索迭代
# 利用宽度优先搜索迭代，我们按照树的层次迭代，第一个访问到的叶子就是最小深度的节点，这样就不要遍历所有的节点了。
# 导入双向队列
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            node_deque = deque([(1,root),])

        while node_deque:
            depth,root = node_deque.popleft()
            children = [root.left,root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth+1,c))
