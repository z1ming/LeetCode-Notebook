class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        n = len(arr)
        dic = Counter(arr)
        sorted_dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)
        ans = 0
        for num, count in sorted_dic:
            n -= count
            ans += 1
            if n <= len(arr) / 2:
                break
        return ans