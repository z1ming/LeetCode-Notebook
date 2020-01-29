class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        import collections
        hs = collections.Counter(arr)
        return len(hs) == len(set(hs.values()))

        hs = {}
        for num in arr:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        hs2 = {}
        for i in hs.values():
            if i in hs2:
                return False
            else:
                hs2[i] = None
        return True

        hs = {}
        for num in arr:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        hs2 = {i:None for i in hs.values()}
        return len(hs2) == len(hs)

        hs = {}
        for num in arr:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        l = list(hs.values())
        for i in range(len(l)-1):
            if l[i] in l[i+1:]:
                return False
        return True

        hs = {}
        for num in arr:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        return len(hs) == len(set(hs.values()))