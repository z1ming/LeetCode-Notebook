# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
#
# 返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
#  
#
# 示例 1：
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
#  方法一 最大公约数
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def helper(a,b):
            # 先对长度求最大公约数
            n = min(a,b)
            for i in range(n,0,-1):
                if a % i == 0 and b % i == 0:
                    return i
        max_ = helper(len(str1),len(str2))
        if str1[:max_] == str2[:max_] and str1[:max_]*(len(str1)//max_) == str1 and str2[:max_]*(len(str2)//max_) == str2:
            return str1[:max_]
        else:
            return ''
# 方法二 递归
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
#
# 返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
#  
#
# 示例 1：
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
#
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
#
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''
        if len(str1) == len(str2):
            return str1
        elif len(str1) > len(str2):
            str1 = str1[len(str2):len(str1)]
        else:
            str2 = str2[len(str1):len(str2)]
        return self.gcdOfStrings(str1,str2)