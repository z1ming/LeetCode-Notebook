class Solution:
    # input: baba 6 baab 4
    # k = [0,n1)
    # s:   index where a match stops in s1
    # cnt: number of s2 in each s1
    #
    # prefix         middle      suffix
    #          +----A cycle---+
    #          |              |
    #    +-----+--------------+---------
    #    |baba|baba|baba|baba|baba|baba|
    #    +-----------------------------+
    #  s |    |0   |  2 |    |0   |  2 |
    #    +-----------------------------+
    # cnt|   0|   1|   2|   2|   3|   4|
    #    +---------+----+---------+----+

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        tmp = set(s1)
        if not all(s in tmp for s in s2): return 0
        if n1 == 0: return 0
        
        j = 0
        cnt = 0
        s = {}
        cnts = []
        for k in range(n1):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                if j == len(s2):
                    j = 0
                    cnt += 1
                    if i in s:
                        k0, cnt0 = s[i] # k,cnt of starting point of cycle
                        prefix_k = k0 + 1   # number of s1 in prefix
                        prefix_c = cnt0     # number of s2 in prefix
                        
                        # (k - k0):     number of s1 in cycle
                        # (cnt - cnt0): number of s2 in cycle
                        middle_k = (n1 - prefix_k) // (k - k0) * (k - k0)
                        middle_c = (n1 - prefix_k) // (k - k0) * (cnt - cnt0)
                        
                        suffix_k = n1 - prefix_k - middle_k
                        suffix_c = cnts[k0 + suffix_k] - cnt0

                        print(prefix_k, middle_k, suffix_k)
                        print(prefix_c, middle_c, suffix_c)
                        return (prefix_c + middle_c + suffix_c) // n2
                    s[i] = (k,cnt)
            cnts.append(cnt)
        # if there isn't a cycle
        return s[max(s, key = lambda k:s[k][1])][1] // n2
        
        

