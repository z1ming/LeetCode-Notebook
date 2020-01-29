class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            cur_sum = left_sum + right_sum + node.val
            cur_count = left_count + right_count + 1
            ans = max(ans, cur_sum / cur_count)
            return cur_sum, cur_count

        dfs(root)
        return ans

