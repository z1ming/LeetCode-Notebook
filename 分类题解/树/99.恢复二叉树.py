# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1, 3, null, null, 2]
#
#    1
#   /
#  3
#   \
#     2
#
# 输出: [3, 1, null, null, 2]
#
#    3
#   /
#  1
#   \
#     2


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur,prev,drops = root,TreeNode(float('-inf')),[]
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur:temp = temp.right
                if not temp.right:
                    temp.right,cur = cur,cur.left
                    continue
                temp.right = None
            if cur.val < prev.val:drops.append((prev,cur))
            prev,cur = cur,cur.right
        drops[0][0].val,drops[-1][1].val = drops[-1][1].val,drops[0][0].val