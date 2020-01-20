# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。
#
# 给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n 个点的。
#
#  
#
# 先来了解下什么是一个有效的安卓解锁手势:
#
# 每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。
# 解锁手势里不能设置经过重复的点。
# 假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。
# 经过点的顺序不同则表示为不同的解锁手势。
#  
#
#
#  
#
# 解释:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

from functools import lru_cache


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        graph = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8},
        }
        ans = 0

        @lru_cache(None)
        def dfs(status, current, count):
            if count == n:
                return 1
            current_ans = 0 if count < m else 1
            for i in range(1, 10):
                if status & (1 << i) == 0:
                    if i not in graph[current] or ((1 << graph[current][i]) & status):
                        current_ans += dfs(status | (1 << i), i, count + 1)
            return current_ans

        ans += 4 * dfs(1 << 1, 1, 1)
        ans += 4 * dfs(1 << 2, 2, 1)
        ans += dfs(1 << 5, 5, 1)
        return ans