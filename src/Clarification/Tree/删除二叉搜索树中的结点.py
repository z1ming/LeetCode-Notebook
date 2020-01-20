# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        if root.left is None:
            new_root = root.left
            root.left = None
            return new_root

        # 找到左子树中最大的
        predecessor = self.__maximum(root.left)
        predecessor_copy = TreeNode(predecessor.val)
        predecessor_copy.left = self.__remove_max(root.left)
        predecessor_copy.right = root.right
        root.left = None
        root.right = None
        return predecessor_copy

    def __remove_max(self, node):
        if node.right is None:
            new_root = node.left
            node.left = None
            return new_root
        node.right = self.__remove_max(node.right)
        return node

    def __maximum(self, node):
        while node.right:
            node = node.right
        return node