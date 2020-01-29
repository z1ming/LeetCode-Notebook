class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        cnt = 0 #统计变量，全部26个字符，频率相同的个数，当cnt==s1字母的个数的时候，就是全部符合题意，返回真
        p = q = 0 #滑动窗口[p,q]
        while q < l2:
            c2[s2[q]] += 1
            if c1[s2[q]] == c2[s2[q]]: #对于遍历到的字母，如果出现次数相同
                cnt += 1               #统计变量+1
            if cnt == len(c1):         #判断结果写在前面，此时证明s2滑动窗口和s1全部字符相同，返回真
                return True
            q += 1                     #滑动窗口右移
            if q - p + 1 > l1:         #这是构造第一个滑动窗口的特殊判断，里面内容是维护边界滑动窗口
                if c1[s2[p]] == c2[s2[p]]:    #判断性的if写在前面，因为一旦频率变化，这个统计变量就减1
                    cnt -= 1
                c2[s2[p]] -= 1                #字典哈希表移除最前面的字符
                if c2[s2[p]] == 0:            #由于counter特性，如果value为0，必须删除它
                    del c2[s2[p]]
                p += 1                        #最前面的下标右移动
        return False
