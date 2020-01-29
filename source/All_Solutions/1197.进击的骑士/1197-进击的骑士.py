from collections import deque, defaultdict

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        steps = 0
        start = [0, 0]
        x_length = abs(x - start[0])
        y_length = abs(y - start[1])
        while x_length + y_length > 7:
            if x_length >= y_length:
                if x > start[0]:
                    start[0] += 2
                else:
                    start[0] -= 2

                if y > start[1]:
                    start[1] += 1
                else:
                    start[1] -= 1
            else:
                if x > start[0]:
                    start[0] += 1
                else:
                    start[0] -= 1

                if y > start[1]:
                    start[1] += 2
                else:
                    start[1] -= 2
            x_length = abs(x - start[0])
            y_length = abs(y - start[1])
            steps += 1

        mem = defaultdict(lambda: float('inf'))
        surround = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        mem[tuple(start)] = steps
        d = deque()
        d.append(tuple(start))

        while d:
            # print(d)
            i, j = d.popleft()
            current_length = abs(y - j) + abs(x - i)
            if i == x and j == y:
                break
            for di, dj in surround:
                ni, nj = i + di, j + dj
                length = abs(y - nj) + abs(x - ni)
                if mem[(i, j)] + 1 < mem[(ni, nj)]:
                    if length <= current_length or current_length <= 3:
                        d.append((ni, nj))
                        mem[(ni, nj)] = mem[(i, j)] + 1

        return mem[(x, y)]

