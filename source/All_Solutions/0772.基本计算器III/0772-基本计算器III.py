class Solution:
    def calculate(self, s: str) -> int:
        def helper(pre, curr, next, sign):
            if sign == '+':
                pre += curr
                curr = next
            elif sign == '-':
                pre += curr
                curr = -next
            elif sign == '*':
                curr *= next
            elif sign == '/':
                curr = int(curr / next)
            return pre, curr, 0

        def cal(s):
            pre, curr, next = 0, 0, 0
            sign = '+'
            i = 0
            while i < len(s):
                if s[i].isnumeric():
                    next = next * 10 + int(s[i])
                elif s[i] == '(':
                    count = 1
                    i += 1
                    j = i
                    while i < len(s):
                        if s[i] == '(':
                            count += 1
                        elif s[i] == ')':
                            count -= 1
                        if count == 0:
                            break
                        i += 1
                    next = cal(s[j:i])
                if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
                    pre, curr, next = helper(pre, curr, next, sign)
                    sign = s[i]
                i += 1
            return pre + curr

        return cal(s)

