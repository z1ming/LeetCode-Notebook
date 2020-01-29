class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        maxlen = 0
        reslen = 0
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum <= maxCost:
                reslen += 1
            elif sum>0:
                sum -= arr[i-reslen]
            maxlen = max(maxlen,reslen)
        return maxlen