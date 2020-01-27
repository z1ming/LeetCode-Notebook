class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = {}
        def dfs(node):
            l = dfs(node.left) if node.left else 0
            r = dfs(node.right) if node.right else 0
            s = node.val + l + r
            self.d[s] = self.d.get(s, 0) + 1
            return s
        if not root:
            return []
        dfs(root)
        maxv = max(self.d.values())
        res = filter(lambda x : self.d[x] == maxv, self.d)
        return res