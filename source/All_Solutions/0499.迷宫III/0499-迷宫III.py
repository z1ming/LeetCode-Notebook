from typing import List
import heapq


class Solution:
    def findShortestWay(self, maze: List[List[int]], start: List[int], destination: List[int]) -> str:

        lx = len(maze)
        ly = len(maze[0])

        mark = [[0 for _ in range(ly)] for _ in range(lx)]
        move = {(0, 1, "r"), (0, -1, "l"), (1, 0, "d"), (-1, 0, "u")}
        stk = [(0, "", start)]
        tmp = 10001
        res = None
        while stk:
            d, s, cur = heapq.heappop(stk)
            a, b = cur

            if mark[a][b]:
                continue
            mark[a][b] = 1

            # 选择一个方向
            for x, y, m in move:
                ta, tb, td = a, b, d
                if s and m == s[-1]:
                    continue
                ts = s + m
                # print(ts)
                while 0 <= ta + x < lx and 0 <= tb + y < ly and not maze[ta + x][tb + y]:
                    ta += x
                    tb += y
                    td += 1
                    # mark[ta][tb] = 1
                    if ta == destination[0] and tb == destination[1]:
                        if td == tmp and ts < res:
                            res = ts
                        elif td < tmp:
                            res = ts
                            tmp = td

                if not mark[ta][tb]:
                    heapq.heappush(stk, (td, ts, (ta, tb)))
        return res or "impossible"
