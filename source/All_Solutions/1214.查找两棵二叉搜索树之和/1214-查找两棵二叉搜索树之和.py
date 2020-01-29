class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        d = set()
        def f(r):
            if r:
                d.add(target - r.val)
                f(r.left)
                f(r.right)
        f(root1)
        ans = False
        def g(r):
            nonlocal ans
            if r and not ans:
                if r.val in d:
                    ans = True
                g(r.left)
                g(r.right)
        g(root2)
        return ans