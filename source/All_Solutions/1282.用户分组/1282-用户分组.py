class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # 贪心：将所有群组个数相同ID映射在一起，用户分组人数不超过所属群组最大数，可直接构建一个组。否则，切割当前组=
        # /c-tan-xin-jian-dan-rong-yi-li-jie-by-charon____/
        n = len(groupSizes)
        if n == 0:
            return []
        res = []
        d = {}
        for i in range(n):
            d.setdefault(groupSizes[i], []).append(i)
        for key in d.keys():
            if len(d[key]) <= key:
                res.append(d[key])
            else:
                cur = len(d[key]) // key
                while cur:
                    res.append([d[key].pop(0) for _ in range(key)])
                    cur -= 1
                if len(d[key]) > 0:
                    res.append(d[key])
        return res
