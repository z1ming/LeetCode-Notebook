# 给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 示例 1:
#
# 输入: "bcabc"
# 输出: "abc"
# 示例 2:
#
# 输入: "cbacdcbc"
# 输出: "acdb"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 记录字符串最后一次出现的索引
        letter_idx = {}
        for idx, latter in enumerate(s):
            letter_idx[latter] = idx
        # 记录字母是否在栈中
        letter_in_stack = [None for _ in range(26)]
        n = len(s)
        stack = []
        for i in range(n):
            # 如果该字母在栈中，跳过
            if letter_in_stack[ord(s[i]) - ord('a')]:
                continue
            # 如果当前字母的ASCII码小于栈顶元素且栈顶元素在后面还有，pop；
            while stack and ord(stack[-1]) > ord(s[i]) and letter_idx[stack[-1]] > i:
                top = stack.pop()
                # 弹出了就不在栈中了，更新状态为False
                letter_in_stack[ord(top) - ord('a')] = False
            # 将s中的字母压入栈中，并更新状态为True
            stack.append(s[i])
            letter_in_stack[ord(s[i]) - ord('a')] = True

        return ''.join(stack)