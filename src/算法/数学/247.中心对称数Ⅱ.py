# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
#
# 找到所有长度为 n 的中心对称数。
#
# 示例 :
#
# 输入:  n = 2
# 输出: ["11","69","88","96"]

class Solution:
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
