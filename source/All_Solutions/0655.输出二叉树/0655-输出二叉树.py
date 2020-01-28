class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        depth = self.getDepth(root)  # one - based
        width = 2 ** depth - 1  # 满二叉树
        out = [["" for j in range(width)] for i in range(depth)] # 初始化
        self.fill(root, out, 0, 0, width)
        return out

    def fill(self, root: TreeNode, out: List[List[str]], depth: int, start: int, end: int):
        if not root or start > end:
            return
        middle = start + (end - start) // 2  # 中间位置
        out[depth][middle] = str(root.val)  # 填充
        self.fill(root.left, out, depth + 1, start, middle - 1)
        self.fill(root.right, out, depth + 1, middle + 1, end)

    def getDepth(self, root: TreeNode) -> int:  # one-based
        if not root:
            return 0
        return max([self.getDepth(root.left), self.getDepth(root.right)]) + 1

