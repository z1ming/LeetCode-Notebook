# 假设你设计一个游戏，用一个 m 行 n 列的 2D 网格来存储你的游戏地图。
#
# 起始的时候，每个格子的地形都被默认标记为「水」。我们可以通过使用 addLand 进行操作，将位置 (row, col) 的「水」变成「陆地」。
#
# 你将会被给定一个列表，来记录所有需要被操作的位置，然后你需要返回计算出来 每次 addLand 操作后岛屿的数量。
#
# 注意：一个岛的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。
#
# 请仔细阅读下方示例与解析，更加深入了解岛屿的判定。
#
# 示例:
#
# 输入: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# 输出: [1,1,2,3]
# 解析:
#
# 起初，二维网格 grid 被全部注入「水」。（0 代表「水」，1 代表「陆地」）
#
# 0 0 0
# 0 0 0
# 0 0 0


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        grid = [[0] * n for _ in range(m)]  # 构建保存岛屿的表格
        island = collections.defaultdict(set)  # 保存岛屿编号和坐标的哈希表

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 上下左右四个方向

        index = 1  # 初始化岛屿编号

        res = []

        for x, y in positions:  # 对每个位置进行遍历
            if grid[x][y]:  # 如果该位置已经有岛屿编号
                res.append(len(island))  # 直接在结果中添加当前哈希表的长度
                continue  # 跳过

            mark = []  # 记录上下左右四个岛屿的编号
            for dx, dy in directions:  # 对上下左右进行遍历
                # 当坐标合法，且该坐标为岛屿时，加入mark
                # 为防止有重复值出现，需要判断该值是否在mark中
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] and grid[x + dx][y + dy] not in mark:
                    mark.append(grid[x + dx][y + dy])

            if len(mark) == 0:  # mark为空，即上下左右都为海洋
                grid[x][y] = index  # 更新该点在grid中的值
                island[index].add((x, y))  # 更新哈希表island
                index += 1  # index + 1

            else:
                temp = mark[0]  # 如果mark不为空，将mark中所有的岛屿编号统一
                grid[x][y] = temp  # 设定mark[0]，即temp为统一值
                island[temp].add((x, y))  # 更新grid[x][y]和哈希表island

                for num in mark[1:]:  # 对于mark中的其他岛屿编号
                    for i, j in island[num]:  # 从哈希表中取出其所有点的坐标i,j
                        grid[i][j] = temp  # 更新grid[i][j]
                    island[temp] |= island[num]  # 更新temp所对应的哈希表，将num对应的坐标加入其中
                    del island[num]  # 删除哈希表中num的条目

            res.append(len(island))  # 在结果中添加当前哈希表island的长度

        return res


