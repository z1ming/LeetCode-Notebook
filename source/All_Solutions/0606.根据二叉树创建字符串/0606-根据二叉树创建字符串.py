class Solution(object):
    def tree2str(self, t):
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        result = str(t.val)
        if t.left:
            result += "(" + self.tree2str(t.left) + ")"
        else:
            result += "()"
        if t.right:
            result += "(" + self.tree2str(t.right) + ")"
        return result