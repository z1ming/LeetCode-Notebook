# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法：中序遍历二叉搜索树，返回第k小的元素
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        st = []
        p = root
        s = 0
        while p is not None or st:
            while p is not None:
                st.append(p)
                p = p.left
            p = st.pop()
            s += 1
            if s == k:
                return p.val
            p = p.right
# 时间复杂度：O(N),N为树中节点个数
# 空间复杂度：O(log(N))