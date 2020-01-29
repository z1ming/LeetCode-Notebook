class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        n = len(arr)
        ans = [0] * (n - 2)+[arr[-1]] +[-1]
        for i in range(n - 3, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans