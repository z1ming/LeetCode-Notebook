class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        resArr = []
        for arr in cpdomains :
            num = arr.split(' ')[0]
            domain = arr.split(' ')[1]
            pointCount = domain.count('.')
            if domain in dic :
                dic[domain] += int(num)
            else :
                dic[domain] = 0
                dic[domain] += int(num)

            startInd = 0

            while pointCount :
                pointCount -= 1
                lIndex = domain.find('.', startInd)
                domain = domain[lIndex + 1:]
                if domain in dic :
                    dic[domain] += int(num)
                else :
                    dic[domain] = 0
                    dic[domain] += int(num)
        for key, value in dic.items() :
            resStr = str(value) + ' ' + key
            resArr.append(resStr)
        return resArr