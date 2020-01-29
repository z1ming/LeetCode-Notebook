class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans, flag = [], True
        def f(r):
            nonlocal ans, flag
            if r and flag:
                if not voyage or r.val != voyage.pop(0):
                    flag = False
                elif r.left and r.right and r.left.val != voyage[0]:
                    ans += [r.val]
                    f(r.right); f(r.left)
                else:
                    f(r.left); f(r.right)
        f(root)
        return ans if flag else [-1]