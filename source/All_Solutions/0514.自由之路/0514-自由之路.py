class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        # 用哈希字典 charPos 记录 ring 中每个字符出现的所有位置，加快查找
        charPos = {}
        for i, char in enumerate(ring):
            if char not in charPos:
                charPos[char] = []
            charPos[char].append(i)
        
        n = len(ring)
        
        # last，curr 中存放二元组：
        #       （轮盘指针处在的位置，到达该位置需要的最少步数）
        # last 表示上一个找到字符的情况
        # curr 表示当前字符的情况，每一轮进行填充
        # last 初始化为一个元素(0, 0)，表示最开始轮盘处在位置 0，已经走了0 步
        last = [(0, 0)]
        curr = []
        
        for char in key:                    # 当前要找的字符
            for currPos in charPos[char]:   # 要指向该字符，指针应该到达的所有位置
                leastStep = last[0][1] + n  # 到达该位置所需最少步数，初始化为一个较大的值
                for (lastPos, lastStep) in last:    # 上个字符所有可能位置，及其相应累积的最少步数
                    # 从上个字符的位置，到达当前位置，所需的最少步数
                    leastStep = min(lastStep + min((currPos + n - lastPos) % n, (lastPos + n - currPos) % n) + 1, leastStep)
                # 找到到达当前位置的最少步数，把（位置，步数）放入 curr
                curr.append((currPos, leastStep))
            
            # 填好 curr 后，滚动 last 和 curr 两个数组
            last, curr = curr, last
            curr.clear()
        
        # 返回最少步数
        return min(list(map(lambda x: x[1], last)))

