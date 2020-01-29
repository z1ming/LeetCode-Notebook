class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if j * 2 - i <= n and text[i:j] == text[j:j*2-i] and text[i:j] not in seen:
                    ans += 1
                    seen.add(text[i:j])
        return ans
