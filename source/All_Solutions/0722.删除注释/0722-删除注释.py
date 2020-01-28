class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        k = 0;
        cc = False
        hh = True
        for sc in source:
            tmp = ''
            L = len(sc)
            if L == 0:
                continue
            for i in range(L):
                if k < 0:
                    k += 1
                    continue

                if sc[i] == r'/' and i < L-1 and sc[i+1] == r'/':
                    if cc:
                        continue;
                    break;
                elif sc[i] == r'/' and i < L-1 and sc[i+1] == r'*':
                    if cc:
                        continue
                    cc = True
                    k = -1
                elif sc[i] == r'*' and i < L-1 and sc[i+1] == r'/':
                    if not cc:
                        tmp += sc[i]
                        continue
                    cc = False
                    k = -1
                else:
                    if not cc:
                        tmp += sc[i]
            if len(tmp) > 0:
                if hh:
                    ret.append(tmp)
                else:
                    ret[-1] += tmp
            if cc:
                hh = False
            else:
                hh = True
        return ret