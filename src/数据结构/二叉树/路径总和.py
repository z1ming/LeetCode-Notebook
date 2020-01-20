# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 如何能遍历跟->叶子节点呢？
# 方法1：递归
# 遍历整棵树，如果当前节点不是叶子，对它的所有孩子节点，递归调用hesPathSum函数，
# 其中sum值减去当前节点的权值；如果当前节点是叶子，检查sum值是否为0，也就是是否找到了给定的目标和。
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right: # if search a leaf
            return sum == 0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

# 方法二：迭代
# 利用深度优先粗略访问每个节点，同时更新剩余的目标和。
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        de = [(root,sum - root.val),]
        while de:
            node,curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right,curr_sum - node.right.val))
            if node.left:
                de.append((node.left,curr_sum - node.left.val))
        return False
# 时间复杂度：和递归方法相同是0(N)
# 空间复杂度：当树不平衡的最坏情况是0(N)。在最好情况