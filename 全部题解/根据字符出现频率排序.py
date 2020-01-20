# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
# 方法一：使用sort进行排序
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        res = ''
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
        # 对字典的值进行排序
        dic1 = sorted(dic.items(),key = lambda x:x[1],reverse=True)
        for key,value in dic1:
            res += key * value #实现连续字母，直接用乘
        return res
# 方法二：使用标准程序
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict(Counter(s))# 使用Counter函数迅速生成字典{字母:出现次数}
        l1 = ['' for e in range(len(s)+1)]
        for key,value in dic.items():
            l1[value] += key * value# 将key*value填入l1中索引等于value的位置
        res = ''
        for i in range(-1,-len(l1)-1,-1):# 对l1倒序遍历，即为排序后的字符
            if l1[i] != '':
                res += l1[i]
        return res