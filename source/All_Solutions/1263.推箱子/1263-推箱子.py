class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n, g = len(grid), len(grid[0]), collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[grid[i][j]] += [complex(i, j)]
        def f(b, s): 
            nonlocal time
            time += 1
            return (abs((b - target).real) + abs((b - target).imag) + s, abs(b - target), time)
        player, box, target, time = *g['S'], *g['B'], *g['T'], 1
        floor = {player, target, box, *g['.']}
        alphaStarQueue = [(f(box, 1), 1, player, box)]
        directions, visited = (1, 1j, -1, -1j), set()
        low = dict.fromkeys(floor, 0)
        dfn = low.copy()
        count = 0
        index = {}
        def tarjan(currIndex, parentIndex):
            nonlocal count
            count += 1
            dfn[currIndex] = low[currIndex] = count
            index[count] = currIndex
            for direction in directions:
                nextIndex = currIndex + direction
                if nextIndex in floor and nextIndex != parentIndex:
                    if not low[nextIndex]:
                        tarjan(nextIndex, currIndex)
                    low[currIndex] = min(low[currIndex], low[nextIndex])
        tarjan(box, -1)
        for currIndex in floor:
            connect = [currIndex]
            while dfn[connect[-1]] != low[connect[-1]]:
                connect.append(index[low[connect[-1]]])
            for w in connect[: -1]:
                low[w] = low[connect[-1]]
        while alphaStarQueue:
            _, steps, currPlayer, currBox = heapq.heappop(alphaStarQueue)
            for direction in directions:
                nextPlayer, nextBox = currBox - direction, currBox + direction
                if nextBox in floor \
                    and nextPlayer in floor \
                        and (nextPlayer, currBox) not in visited \
                            and low[currPlayer] == low[nextPlayer]:
                    if nextBox == target:
                        return steps
                    heapq.heappush( alphaStarQueue, (f(nextBox, steps + 1), steps + 1, currBox, nextBox))
                    visited.add((nextPlayer, currBox))
        return -1