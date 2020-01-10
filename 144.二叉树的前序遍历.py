# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]

# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        # 定义一个helper函数来进行递归
        def helper(root):
            if not root:
                return
            res.append(root.val) # 先将根结点的值加入到res中
            helper(root.left)  # 把root左子树看成整体，先序遍历是根->左->右，所以程序也按这样的顺序写
            helper(root.right)  # 按根->左->右的顺序，再递归右子树
        helper(root)
        return res
# time:O(N)。我们遍历了每个结点
# space:O(N)，结果是一个数组，与输入长度有关

# 方法二： 迭代
# 每次迭代弹出当前栈顶元素，并将其孩子结点压入栈中，先压右孩子再压左孩子，这样弹出的时候按根根->左->右的顺序。
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()  # 先弹出栈顶元素
            if root:  # 如果根节点存在，将值加入到结果中
                output.append(root.val)
                if root.right:  # 如果左子树不为空
                    stack.append(root.right)
                if root.left:  # 如果左子树不为空
                    stack.append(root.left)
        return output
# time:O(N)。我们遍历了每个结点
# space:O(N)，取决于树的结构，最坏情况存储整棵树，因此空间复杂度是O(N)

# 方法三： 摩里斯遍历，使用过程不需要额外的空间
class Solution(object):
    def preorderTraversal(self, root):

        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output
# time:O(N)。我们遍历了每个结点
# space:O(N)，取决于树的结构，最坏情况存储整棵树，因此空间复杂度是O(N),如果实时输出结果的话，空间复杂度为O(1)
