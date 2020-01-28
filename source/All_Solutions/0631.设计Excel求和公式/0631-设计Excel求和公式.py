class Excel:
    def __init__(self, H: int, W: str):
        self.w = self.char_to_num(W)
        self.h = H
        self.nums = [[0]*(self.w+1) for _ in range (self.h+1)]
        for i in range (1, self.h+1):
            self.nums[i][0] = i
        for i in range (1, self.w+1):
            self.nums[0][i] = chr(ord('A')+i-1)

        self.prev_sum = {}

    def char_to_num(self, c):
        return ord(c)-ord('A')+1

    def in_strs(self, s, strs):
        count = 0
        for string in strs:
            if string.find(':') == -1:
                if s == string:
                    count += 1
            else:
                idx = string.find(':')+1
                if string[:1]<=s[:1]<=string[idx:idx+1] and int(string[1:idx-1])<=int(s[1:])<=int(string[idx+1:]):
                    count += 1
        return count

    def set(self, r: int, c: str, v: int) -> None:
        v_old = self.get(r, c)
        self.nums[r][self.char_to_num(c)] = v

        curr = c+str(r)
        if curr in self.prev_sum:
            del self.prev_sum[curr]

        if len(self.prev_sum) > 0:
            candidate = []
            while curr:
                for key in self.prev_sum:
                    if curr == key:
                        continue
                    prev = self.prev_sum[key]
                    ct = self.in_strs(curr, prev)
                    if ct > 0:
                        self.nums[int(key[1:])][self.char_to_num(key[0])] += ct*(v-v_old)
                        candidate.append(key)

                curr = None if not candidate else candidate.pop(-1)

    def get(self, r: int, c: str) -> int:
        return self.nums[r][self.char_to_num(c)]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.prev_sum[c+str(r)] = [x for x in strs]

        sums = 0
        while strs:
            s = strs.pop(0)
            
            if s.find(':') == -1:
                sums += self.nums[int(s[1:])][self.char_to_num(s[:1])]
            else:
                idx = s.find(':')+1
                h_start = int(s[1:idx-1])
                h_end = int(s[idx+1:])

                w_start = self.char_to_num(s[:1])
                w_end = self.char_to_num(s[idx])

                for i in range (h_start, h_end+1):
                    for j in range (w_start, w_end+1):
                        sums += self.nums[i][j]

        self.nums[r][self.char_to_num(c)] = sums
        return sums

