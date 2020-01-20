# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
# 方法一： 递归 搜索每个结点
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# 方法二： 利用完全二叉树的性质
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_h = right_h = 0
        left = root.left
        right = root.right
        while left:
            left_h += 1
            left = left.left
        while right:
            right_h += 1
            right = right.right
        if left_h == right_h:
            return 2 ** (left_h + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)