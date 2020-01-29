class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        d = collections.defaultdict(lambda: 1)
        def f(r, i):
            if r:
                if not d[i - 2] & 1:
                    d['ans'] += r.val
                d[i] = r.val
                f(r.left, i + 1)
                f(r.right, i + 1)
        f(root, 0)
        return d['ans'] - 1