class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()
        def f(r, val):
            if r:
                r.val = val
                self.vals.add(val)
                if r.left:
                    f(r.left, 2*val+1)
                if r.right:
                    f(r.right, 2*val+2)
        f(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals