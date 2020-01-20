# 你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。
#
# 请你写出一个函数来判定起始玩家是否存在必胜的方案。
#
# 示例：
#
# 输入: s = "++++"
# 输出: true
# 解析: 起始玩家可将中间的 "++" 翻转变为 "+--+" 从而得胜。

from functools import lru_cache
class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                if not self.canWin(s[:i]+"--"+s[i+2:]):
                    return True
        return False