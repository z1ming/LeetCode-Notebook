# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
#
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
#
#
# 例子:
#
# 输入: N = 1, K = 1
# 输出: 0
#
# 输入: N = 2, K = 1
# 输出: 0
#
# 输入: N = 2, K = 2
# 输出: 1
#
# 输入: N = 4, K = 5
# 输出: 1
#
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001

# 方法一; 暴力法
class Solution(object):
    def kthGrammar(self,N,K):
        lastrow = "0"
        while len(rows) < N:
            lastrow = "".join(01 if x == '0' else '10' for x in lastrow)
        return rows[-1][K-1]
# 时间复杂度;O（2**N）解析每一行所需的时间和其长度有关。共计2**0+2**1+...+2**(N-1)
# 空间复杂度：O(2**N）最后一行lastrow的长度

# 方法二：递归（父变体）
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        return (1 - int(K%2)) ^ self.kthGrammar(N-1, (K+1)/2)
# 时间复杂度：O(N-1)找出答案需要N-1步
# 空间复杂度：O(1)

# 方法三：递归（翻转变体）
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1:return 0
        if K <= 2 ** (N-2):
            # 递归别忘了self！！！！！
            return self.kthGrammar(N-1,K)
        # 返回相反的数，与1异或；返回原数，与0异或
        return self.kthGrammar(N-1,(K-2**(N-2)))^1
# 时间复杂度;O（N-1）找出答案需要N-1步
# 空间复杂度：O(1）

# 方法四：二进制计数
# bin()返回一个整数或长整数的二进制表示
class Solution(object):
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') % 2
# 时间复杂度;O（log N）即N的二进制表示的位数，如果log N是有界的，那么可将其视作O（1）
# 空间复杂度：O(1）