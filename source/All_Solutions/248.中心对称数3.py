# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
# 写一个函数来计算范围在 [low, high] 之间中心对称数的个数。
#
# 示例:
#
# 输入: low = "50", high = "100"
# 输出: 3
# 解释: 69，88 和 96 是三个在该范围内的中心对称数
# 注意:
# 由于范围可能很大，所以 low 和 high 都用字符串表示。

class Solution:
    # 找到长度为n的中心对称数
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 对于n - 1是偶数的解来说，
        # 只要再n-1的解的每个数中间加上0或1或8就可以得到n的解
        # 对于n-1是奇数的解来说，只要在n-2的解的每个数中间加上00，
        # 11，88，69，96就可以得到n的解
        # 用动态规划一步步推算即可
        record = dict()
        record[1] = ['0','1','8']
        record[2] = ['11','69','88','96']
        pair = ['00','11','88','69','96']
        if n <= 2:
            return record[n]
        cnt = 3
        while cnt <= n:
            tmp = []
            if (cnt - 1) % 2 == 0: # 如果前一个是偶数长度，那么直接在中间加长度位1的就可以
                for item in record[cnt - 1]:
                    for num in record[1]:
                        tmp.append(item[:len(item)//2] + num + item[len(item)//2:])
            else:  # 如果前一个是奇数长度，那么就在中间加长度为2的就可以，注意要额外加00
                for item in record[cnt - 2]:
                    for num in pair:
                        tmp.append(item[:len(item)//2] + num + item[len(item)//2:])
            record[cnt] = tmp
            cnt += 1
        return record[n]

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        if len(low) > len(high):
            return 0
        ans = 0
        if len(low) == len(high):
            record = self.findStrobogrammatic(len(low))
            for i in record:
                if int(low) <= int(i) <= int(high):
                    ans += 1
        else:
            if len(high) - len(low) == 1:
                record1 = self.findStrobogrammatic(len(low))
                record2 = self.findStrobogrammatic(len(high))
                for i in range(len(record1)):
                    if int(record1[i]) >= int(low):
                        ans += len(record1) - i
                        break
                for j in range(len(record2)):
                    if int(record2[j]) > int(high):
                        ans += j
                        break
            else:
                record1 = self.findStrobogrammatic(len(low))
                record2 = self.findStrobogrammatic(len(high))
                for i in range(len(record1)):
                    if int(record1[i]) >= int(low):
                        ans += len(record1) - i
                        break
                for j in range(len(record2)):
                    if int(record2[j]) >= int(high):
                        ans += j
                        break
                n = len(low) + 1
                while n < len(high):
                    ans += len(self.findStrobogrammatic(n))
                    n += 1
        return ans
