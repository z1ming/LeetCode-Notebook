你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

# 请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
#
# 请注意秘密数字和朋友的猜测数都可能含有重复数字。
#
# 示例 1:
#
# 输入: secret = "1807", guess = "7810"
#
# 输出: "1A3B"
#
# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
# 示例 2:
#
# 输入: secret = "1123", guess = "0111"
#
# 输出: "1A1B"
#
# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        res = [0,0]
        for x,y in zip(secret,guess):
            if x == y:
                s_c[x] -= 1
                g_c[y] -= 1
                res[0] += 1
        for k in s_c and g_c:
            res[1] += min(s_c[k], g_c[k])
        return '{}A{}B'.format(res[0], res[1])