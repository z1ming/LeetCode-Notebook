class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        data = []
        for i, j in Counter(barcodes).most_common():
            data += [i] * j
        l = len(data)
        ans = [0] * l
        ans[::2] = data[:(l+1)//2]
        ans[1::2] = data[(l+1)//2:]
        return ans