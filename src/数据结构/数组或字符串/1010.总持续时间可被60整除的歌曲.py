# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
#
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。
#
#  
#
# 示例 1：
#
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 示例 2：
#
# 输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
#

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]

        from collections import defaultdict
        dic = defaultdict(int)

        res = 0
        for t in time:
            resi = (60 - t) % 60
            if resi in dic:
                res += dic[resi]  # 如果出现在字典中，说明有一对结果
            dic[t] += 1
        return res
# 时间复杂度： O(n),这里n是数组的长度，算法把数组看了两次
# 空间复杂度：O(n)，使用了长度为N的哈希表