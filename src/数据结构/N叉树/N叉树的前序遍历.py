# 给定一个
# N
# 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个
# 3
# 叉树:
#
# 返回其前序遍历: [1, 3, 5, 6, 2, 4]。
#
#
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?

# 方法一：递归
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        a = []
        for i in root.children:
            a += self.preorder(i)
        return [root.val] + a

# 方法二：迭代
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output