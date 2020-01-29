class Solution:
    def confusingNumber(self, N: int) -> bool:
        N = str(N)
        change = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        M = ''
        for x in N:
            if x not in change:
                return False
            M += change[x]
        return ''.join(reversed(N)) != M