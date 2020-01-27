class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        row = len(maze)
        col = len(maze[0])
        visited = set()
        stack = [(start[0],start[1])]
        while stack:
            i,j = stack.pop()
            if [i,j] == destination:
                return True
            visited.add((i, j))
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = i
                tmp_j = j
                while 0 <= tmp_i + x < row and 0 <= tmp_j + y < col and maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                if tmp_i == i and tmp_j == j:
                    continue
                if (tmp_i,tmp_j) not in visited:
                    stack.append((tmp_i,tmp_j))
        return False
