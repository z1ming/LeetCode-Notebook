from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        move = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        lx = len(maze)
        ly = len(maze[0])
        mark = [[0 for _ in range(ly)] for _ in range(lx)]
        stk = [(0, start)]

        while stk:
            d, cur = heapq.heappop(stk)
            a, b = cur
            if mark[a][b]:
                continue
            if a == destination[0] and b == destination[1]:
                return d
            mark[a][b] = 1

            for x, y in move:
                ta, tb = cur
                td = d
                while 0 <= ta + x < lx and 0 <= tb + y < ly and not maze[ta + x][tb + y]:
                    ta += x
                    tb += y
                    td += 1
                if not mark[ta][tb]:
                    heapq.heappush(stk, (td, (ta, tb)))

        return -1
