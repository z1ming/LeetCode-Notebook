# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        # 后序遍历的最后一个点为跟节点
        root = TreeNode(postorder[-1])
        # 查找跟节点在中序遍历中的位置
        mid = inorder.index(postorder[-1])
        # 构建左子树
        root.left = self.buildTree(inorder[:mid],postorder[:mid])
        # 构建右子树
        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root
# 复杂度分析：
# 时间复杂度：O(N log N)，这里N是二叉树的结点个数，算法中每个节点都会被看到一次，是线性级别的，
# 递归的深度是对数级别的，因此时间复杂度是O(N log N)
# 空间复杂度：O(N),构造一棵树需要N个结点(待讨论)