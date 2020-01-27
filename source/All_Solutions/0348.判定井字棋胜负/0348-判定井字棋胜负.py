class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.lookup = defaultdict(int)
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player = str(player)
        self.lookup[player +"r" + str(row)] += 1
        self.lookup[player+"c" + str(col)] += 1
        self.lookup[player+"r+c" + str(row + col)] += 1
        self.lookup[player+"r-c" + str(row - col)] += 1
        if max(self.lookup[player +"r" + str(row)], self.lookup[player+"c" + str(col)], self.lookup[player+"r+c" + str(row + col)], self.lookup[player+"r-c" + str(row - col)]) == self.n:
            return player
        return 0 
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)