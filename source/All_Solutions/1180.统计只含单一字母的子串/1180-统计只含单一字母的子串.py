class Solution:
    def countLetters(self, S: str) -> int:
        if not S:
            return 0
        left = 0
        n = len(S)
        res = 0
        while left < n:
            com_alp = S[left]
            right = left
            while right < n and S[right] == com_alp:
                right += 1
            res += ((1 + right- left) * (right - left)) // 2      
            left = right
        return res