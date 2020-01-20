# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
#
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = heapq.nlargest(k,nums)[::-1] # 返回nums中前k大的数并倒序排列，即[4,5,8]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool,val) # 将val推入并返回最下值
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)