from random import randint

class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.s = N - len(blacklist)
        # 小于s的黑名单元素集合
        b_lt_s = {i for i in blacklist if i < self.s}
        # 大于s的非黑名单元素集合
        # 等价于：w_gt_s = {i for i in range(self.s, N)} - set(blacklist)，感谢评论
        w_gt_s = {*range(self.s, N)} - set(blacklist)
        # 做映射，使用zip方便一点
        # 等价于：self.m = {k: v for k,v in zip(b_lt_s, w_gt_s)}
        self.m = dict(zip(b_lt_s, w_gt_s))

    def pick(self):
        """
        :rtype: int
        """
        r = randint(0, self.s-1)
        return r if r not in self.m else self.m[r]