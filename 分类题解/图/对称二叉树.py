# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isMatch(l,r):
            if not l and not r:
                return True
            if not r or not l:
                return False
            return l.val == r.val and isMatch(l.left,r.right) and isMatch(l.right,r.left)
        return isMatch(root.left,root.right)
# 时间复杂度：O(N)，因为我们遍历整个输入树一次，所以总的运行时间为O(N)，其中n是书中结点的总数。
# 空间复杂度：递归调用的次数受数的高度限制。在最糟糕的情况下，树是线性的，其高度为O(n)。因此，
# 在最糟糕的情况下，由栈上的递归调用造成的空间复杂度为O（n）。

# 方法二：利用队列实现迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def Tree(p,q):
            stack = [(q,p)]
            while stack:
                a,b = stack.pop()
                if not a and not b:
                    continue
                if a and b and a.val == b.val:
                    stack.append((a.left,b.right))
                    stack.append((a.right,b.left))
                else:
                    return False
            return True
        return Tree(root.left,root.right)
# 时间复杂度：O(n)，因为我们遍历整个输入树一次，因此总的运行时间为O（n），其中n是树中结点的总数。
# 空间复杂度：搜索队列需要额外的空间。在最糟糕的情况下，我们不得不向队列中插入O(n)个结点。因此，空间复杂度为O(n)。