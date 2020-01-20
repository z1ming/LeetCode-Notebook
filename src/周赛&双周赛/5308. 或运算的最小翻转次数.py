# 给你三个正整数 a、b 和 c。
#
# 你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。
#
# 「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
#
# 输入：a = 2, b = 6, c = 5
# 输出：3
# 解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = format(a, 'b')
        bin_b = format(b, 'b')
        bin_c = format(c, 'b')

        n = max(max(len(bin_c), len(bin_a)), len(bin_b))
        while len(bin_a) < n:
            bin_a = '0' + bin_a
        while len(bin_b) < n:
            bin_b = '0' + bin_b
        while len(bin_c) < n:
            bin_c = '0' + bin_c
        count = 0
        for i in range(n - 1, -1, -1):
            if bin_c[i] == '0':
                if bin_a[i] == '1':
                    count += 1
                if bin_b[i] == '1':
                    count += 1
            else:
                if bin_a[i] == '0' and bin_b[i] == '0':
                    count += 1
        return count