# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value * 10 + root.val)
            self.dfs(root.right, value * 10 + root.val)
            # 如果到达了叶子节点，将该数加到结果中
            if not root.left and not root.right:
                self.res += value * 10 + root.val
# 方法二：迭代（stack + dfs）
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack,res = [(root,root.val)],0  # 使用栈保存节点和值
        while stack:
            node,value = stack.pop()  # 弹出节点和值
            if node:
                if not node.left and not node.right: # 到达了叶子节点
                    res += value
                if node.left:
                    stack.append((node.left,value * 10 + node.left.val))
                if node.right:
                    stack.append((node.right,value * 10 + node.right.val))
        return res

# 方法三：dfs+queue
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue,res = collections.deque([(root,root.val)]),0
        while queue:
            node,value = queue.popleft()  # 出队
            if node:
                if not node.left and not node.right: #如果到达了叶子节点，加到结果中
                    res += value
                if node.left:
                    queue.append((node.left,value * 10 + node.left.val))
                if node.right:
                    queue.append((node.right,value * 10 + node.right.val))
        return res