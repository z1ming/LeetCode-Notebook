# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
# 调用
# next()
# 将返回二叉搜索树中的下一个最小的数。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmp = self.stack.pop()
        if tmp.right:
            self.push_stack(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)

    def push_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()