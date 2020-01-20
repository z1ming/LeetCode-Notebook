# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归
# 不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
# 时间复杂度 : O(N)O(N)。每个结点访问一次。
# 空间复杂度 : O(N)O(N)。我们跟进了整棵树。

# 方法二：迭代
# 通过使用栈，上面的递归法可以转化为迭代法，这里使用深度优先搜索，比广度优先搜索要快一些。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
# 时间复杂度 : O(N)O(N)。每个结点访问一次。
# 空间复杂度 : O(N)O(N)。我们跟进了整棵树。

# 方法三：中序遍历
# 对二叉搜索树执行中序遍历，会发现得到一个从小到大排列的序列
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
# 疑问：中序遍历怎么实现呢？？
        stack,inorder = [],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
# 时间复杂度 : 最坏情况下(树为二叉搜索树或破坏条件的元素是最右叶结点)为O(N)。
# 空间复杂度 : O(N) 用于存储 stack。
