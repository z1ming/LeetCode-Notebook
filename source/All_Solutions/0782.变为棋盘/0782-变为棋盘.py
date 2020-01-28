class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)): return -1
        row = sum(board[0])
        col = sum(board[i][0] for i in range(n))
        r = sum(board[0][i] != i % 2 for i in range(n))
        c = sum(board[i][0] != i % 2 for i in range(n))
        if n % 2 == 0:
            if not (row * 2 == n and col * 2 == n):
                return -1
            return (min(r, n - r) + min(c, n - c))//2
        else:
            if not ((row == n // 2 or row == n // 2 + 1) and (col == n // 2 or col == n // 2 + 1)):
                return -1
            resr = n - r if row * 2 > n else r
            resc = n - c if col * 2 > n else c
            return (resr + resc)//2
