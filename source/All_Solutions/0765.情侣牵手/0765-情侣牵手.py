class Solution(object):
    def minSwapsCouples(self, row):
        """
        每两个座位成一对，假定左边的人都是合法的不变，如果TA右边的人与TA匹配则
        跳过，不匹配则找到TA的匹配对象的与TA右边的人交换。
        """
        def find_another(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find_another(p1)
            if row[i+1] != p2:
                j = row.index(p2)
                row[i+1], row[j] = row[j], row[i+1]
                c += 1

        return c