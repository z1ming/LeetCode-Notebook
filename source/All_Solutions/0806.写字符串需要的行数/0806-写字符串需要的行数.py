class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        total = 0
        resArr = [0] * 2
        for ch in S:
            if (total % 100 + widths[ord(ch) - 97]) > 100:
                total = total + 100 - (total % 100) + widths[ord(ch) - 97]
            else:
                total += widths[ord(ch) - 97]
        resArr[0] = total // 100 if total // 100 == total / \
            100 else total // 100 + 1
        resArr[1] = total % 100
        return resArr