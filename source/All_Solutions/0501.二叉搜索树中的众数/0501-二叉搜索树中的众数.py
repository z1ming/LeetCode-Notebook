class Solution(object):
    def findMode(self, root):
        stack = [(root, 0)]
        ret, pre, cnt, maxCnt = set(), None, 1, 1
        while stack:
            node, status = stack.pop()
            if not node:
                continue
            if status == 0:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
            else:
                if pre:
                    if pre.val == node.val:
                        cnt += 1
                    else:
                        cnt = 1
                    if cnt > maxCnt:
                        ret = set([node.val])
                        maxCnt = cnt
                    elif cnt == maxCnt:
                        ret.add(node.val)
                else:
                    ret.add(node.val)
                pre = node
        return list(ret)