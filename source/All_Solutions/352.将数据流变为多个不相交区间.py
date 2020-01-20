# 给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。
#
# 例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#  
#
# 进阶：
# 如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
#
# 提示：
# 特别感谢 @yunhong 提供了本问题和其测试用例。

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []

    def addNum(self, val: int) -> None:
        # 二分查找插入的坐标
        m = bisect.bisect(self.d,val)
        if m % 2 == 0:
            if m < len(self.d) and self.d[m] - val == 1:# 如果插入的值与右侧区间差值为一时，更新
                self.d[m] = val
            else:
                self.d.insert(m,val)
                self.d.insert(m,val)
            if m > 0 and self.d[m] - self.d[m-1] <= 1: # 根据现有情况选择是否区间合并
                self.d.pop(m)
                self.d.pop(m - 1)
    def getIntervals(self) -> List[List[int]]:
        return zip(self.d[::2],self.d[1::2])  # 按奇偶顺序打包输出


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()