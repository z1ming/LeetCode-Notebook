class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            id, flag, time = log.split(':')
            if flag == 'end':
                castTime  = 0
                while stack and stack[-1][0] == 'cast':
                    _, t = stack.pop()
                    castTime += t

                curId, curTime = stack.pop()
                res[curId] += int(time) - int(curTime) - castTime + 1
                stack.append(('cast', int(time) - int(curTime) + 1))
            else:
                stack.append((int(id), time))
                castTime = 0
        return res


