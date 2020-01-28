class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # 整体思路是维护一个当前正在处理的果树类型组ts，最大长度为2
        # 假设输入数据是 [1,2,2,3]
        # 初始化时，ts = []，碰到前面的 1 和 2时，直接把 1 和 2 放到ts里，因为 ts 目前是空的，同时 cur_len + 1
        # 碰到第二个 2，由于 2 在 ts 里面，所以目前仍然没有出现第三个类别，不做处理，cur_len + 1
        # 碰到 3 时，出现了第三个类别，此时需要结算一次，看如果 cur_len > max_len， 把 cur_len 赋给 max_len
        # 然后更新一下 ts，此时 ts 应该 = [2, 3]
        # 还有一些细节需要处理，具体可以参考代码
        p1 = None
        p2 = None
        cur_len = None
        max_len = None
        ts = []
        for i, t in enumerate(tree):
            # 判断是否遇到了第三个类别
            if t in ts:
                cur_len += 1
                if t == ts[0]:
                    p1 = p2
                    p2 = i
                    ts = ts[::-1]
                
            else:
                if len(ts) == 0:
                    ts.append(t)
                    p1 = i
                    cur_len = 1
                elif len(ts) == 1:
                    ts.append(t)
                    p2 = i
                    cur_len += 1                
                else:
                    # 此时遇到了第三个类别，结算一次
                    if max_len is None or cur_len > max_len:
                        #print(p1, p2, i, cur_len)
                        max_len = cur_len
                    cur_len = i - p2 + 1
                    p1 = p2
                    p2 = i
                    ts = [ts[1], t]
                    
        if max_len is None or cur_len > max_len:
            max_len = cur_len
        return max_len