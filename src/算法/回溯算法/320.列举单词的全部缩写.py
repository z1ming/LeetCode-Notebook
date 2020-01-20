# 请你写出一个能够举单词全部缩写的函数。
#
# 注意：输出的顺序并不重要。
#
# 示例：
#
# 输入: "word"
# 输出:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        def helper(i,tmp,cnt):
        # cnt 表示前面已经记录多少数字了
            if i == len(word):
                if cnt > 0: tmp += str(cnt)
                res.append(tmp)
            else:
                helper(i + 1,tmp,cnt + 1)
                helper(i + 1,tmp + (str(cnt) if cnt > 0 else "")+word[i],0)
        helper(0,"",0)
        return res