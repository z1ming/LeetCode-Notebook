# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。
#
#  
#
# 示例 1：
#
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
#
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        res = []
        for c in set(A[0]):  # 遍历A[0]中的字符串c,set()去重
            count = [w.count(c) for w in A]  # c在各字符串中的出现次数保存在count中
            s = c * min(count)
            for i in s:
                res.append(i)
        return res
