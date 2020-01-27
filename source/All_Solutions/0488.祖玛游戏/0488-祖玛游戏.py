class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board,hand):
            if not board:
                return 0
            res = float("inf")
            i = 0
            while i<len(board):
                j=i+1
                while j<len(board) and board[i]==board[j]:
                    j+=1
                need = 3-(j-i)
                if hand[board[i]]>=need:
                    need = max(0,need) #为了解决已经有的连接的球，并且球数可能大于3个
                    hand[board[i]]-=need
                    temp = dfs(board[:i]+board[j:],hand)
                    if temp>=0:
                        res = min(res,need+temp)
                    hand[board[i]]+=need
                i=j
            return res if res!=float('inf') else -1
        return dfs(board,collections.Counter(hand))

