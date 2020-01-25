# 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。
#
# 格式
#
# 该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
#
# 你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。
#
# 示例 1:
#
# 输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
#
# 输出: [1]

class Solution:

    # 贪心法

    def findMinHeightTrees(self, n, edges):

        if n <= 2:
            return [i for i in range(n)]

        from collections import defaultdict
        from collections import deque

        in_degrees = [0] * n
        # True 表示保留，如果设置为 False 则表示删除
        res = [True] * n
        # 邻接表
        adjs = defaultdict(list)
        for edge in edges:
            in_degrees[edge[0]] += 1
            in_degrees[edge[1]] += 1
            adjs[edge[0]].append(edge[1])
            adjs[edge[1]].append(edge[0])

        deque = deque()

        for i in range(n):
            if in_degrees[i] == 1:
                deque.append(i)

        # 根据示例，可知，最后可能剩下 1 个结点或者 2 个结点
        # 或者自己画一个图也能分析出来
        while n > 2:
            size = len(deque)
            # 一次减去当前队列这么多个结点
            n -= size
            for i in range(size):
                top = deque.popleft()
                res[top] = False

                successors = adjs[top]
                # 它和它的邻接点的入度全部减 1
                successors.append(top)

                for item in successors:
                    # 一个结点的入度重复减是没有关系的
                    # 我们只关心在最边界的那个结点，把它移除，所以可以认为是贪心法
                    in_degrees[item] -= 1

                    if in_degrees[item] == 1:
                        deque.append(item)

        return [i for i in range(len(res)) if res[i]]

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/minimum-height-trees/solution/tan-xin-fa-gen-ju-tuo-bu-pai-xu-de-si-lu-python-da/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。