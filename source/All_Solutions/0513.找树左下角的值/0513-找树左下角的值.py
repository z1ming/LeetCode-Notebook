class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        d = {}
        def f(r, i):
            if r:
                d[i] = r.val
                f(r.right, i + 1)
                f(r.left, i + 1)
        f(root, 0)
        return next(reversed(d.values()))