class Solution(object):
    def reverseParentheses(self, s):
        while '(' in s:
            s = re.sub(r'\(([^()]*)\)', lambda x:x.group(1)[::-1], s)
        return s